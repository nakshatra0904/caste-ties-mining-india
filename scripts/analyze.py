"""Reproduce observed-data analysis. No simulated observations are used."""
from pathlib import Path
import sys,re,json,hashlib
BASE=Path(__file__).resolve().parents[1]
ROOT=BASE/'data'/'raw'
import numpy as np,pandas as pd,statsmodels.api as sm,statsmodels.formula.api as smf
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
OUT=BASE/'data'/'derived';OUT.mkdir(parents=True,exist_ok=True)
FIG=BASE/'figures';FIG.mkdir(parents=True,exist_ok=True)
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'figure.dpi':150})
def pages(name):
 text=(ROOT/name).read_text(encoding='utf-8')
 a=re.split(r'\\n--- PDF PAGE (\d+) ---\\n',text)
 return {int(a[i]):a[i+1] for i in range(1,len(a),2)}
nat=pages('ec6_report.pdf.txt');mh=pages('maharashtra_ec6.pdf.txt')
provenance=[]
def regions(text,prefix,pdfpage):
 rows=[]
 for l in text.splitlines():
  m=re.match(r'^\s*(\d{2})\s*-\s*(.*?)\s+((?:\d[\d,]*\s+){8}\d[\d,]*)\s*$',l)
  if m:
   nums=[int(x.replace(',','')) for x in m[3].split()]
   row={'code':int(m[1]),'region':m[2].strip()}
   row.update({f'{prefix}_{x}':n for x,n in zip(['rural_oae','rural_hired','rural_total','urban_oae','urban_hired','urban_total','total_oae','total_hired','total'],nums)})
   for k in [0,3,6]: assert nums[k]+nums[k+1]==nums[k+2]
   for k in range(3): assert nums[k]+nums[k+3]==nums[k+6]
   rows.append(row)
 assert len(rows) in [35,36],(prefix,len(rows))
 provenance.append({'dataset':prefix,'pdf_page':pdfpage,'rows':len(rows)})
 return pd.DataFrame(rows)
ns=regions(nat[145],'est',145).merge(regions(nat[169],'emp',169).drop(columns='region'),on='code',validate='one_to_one')
assert ns.est_total.sum()==85176 and ns.emp_total.sum()==557474
ns.to_csv(OUT/'mining_states_raw_2013.csv',index=False)
district=regions(mh[123],'est',123).merge(regions(mh[147],'emp',147).drop(columns='region'),on='code',validate='one_to_one')
assert district.est_total.sum()==6229 and district.emp_total.sum()==29527
def caste_rows(text,key):
 out=[]
 flat=re.sub(r'\s+',' ',text)
 for code in range(1,24):
  pattern=r'(?<!\d)'+str(code).zfill(2)+r'\s*-\s*(.*?)(?=\d{2}\s*-|Subtotal|Total|$)'
  m=re.search(pattern,flat)
  assert m,code
  nums=re.findall(r'(?<![\w.])\d+(?:\.\d+)?(?![\w.])',m[1])
  # Each row ends in four counts interleaved with rounded percentage figures.
  vals=nums[-8:];assert len(vals)==8
  label=re.sub(r'\s+\d+.*$','',m[1]).strip()
  for g,i in zip(['SC','ST','OBC','Others'],[0,2,4,6]):
   out.append({'industry_code':code,'industry':label,'group':g,key:int(vals[i]),key+'_published_pct':float(vals[i+1])})
 return pd.DataFrame(out)
cells=caste_rows(nat[195],'establishments').merge(caste_rows(nat[198],'employment').drop(columns='industry'),on=['industry_code','group'],validate='one_to_one')
cells['mean_size']=cells.employment/cells.establishments
cells['est_share_pct']=100*cells.establishments/cells.groupby('industry_code').establishments.transform('sum')
cells['emp_share_pct']=100*cells.employment/cells.groupby('industry_code').employment.transform('sum')
cells['size_relative_others']=cells.mean_size/cells.industry_code.map(cells[cells.group=='Others'].set_index('industry_code').mean_size)
cells['log_mean_size']=np.log(cells.mean_size)
assert cells[cells.industry_code==5].establishments.sum()==73170
assert cells[cells.industry_code==5].employment.sum()==319425
cells.to_csv(OUT/'industry_social_group_cells_2013.csv',index=False)
pca=pd.read_excel(ROOT/'pca_2011.xlsx',dtype={'State':str,'District':str})
for c in ['TOT_P','P_SC','P_ST','P_LIT','P_06']:pca[c]=pd.to_numeric(pca[c])
def demographics(level,state=None):
 p=pca[pca.Level.eq(level)].copy()
 if state:p=p[p.State.eq(state)]
 code='State' if level=='STATE' else 'District'
 total=p[p.TRU.eq('Total')].copy()
 urban=p[p.TRU.eq('Urban')].set_index(code).TOT_P
 total['urban_population']=total[code].map(urban).fillna(0)
 total['population']=total.TOT_P
 total['sc_pct']=100*total.P_SC/total.TOT_P
 total['st_pct']=100*total.P_ST/total.TOT_P
 total['urban_pct']=100*total.urban_population/total.TOT_P
 total['literacy_pct']=100*total.P_LIT/(total.TOT_P-total.P_06)
 total['geo_code']=total[code].astype(int)
 return total[['geo_code','Name','population','sc_pct','st_pct','urban_pct','literacy_pct']]
# Pool Telangana and residual Andhra Pradesh to the 2011 undivided AP geography.
ap=ns[ns.code.isin([36,37])].copy()
aprow=ap.select_dtypes('number').sum().to_dict();aprow.update(code=28,region='Andhra Pradesh undivided')
state=pd.concat([ns[~ns.code.isin([36,37])],pd.DataFrame([aprow])],ignore_index=True)
state=state.merge(demographics('STATE'),left_on='code',right_on='geo_code',validate='one_to_one')
assert len(state)==35 and state.est_total.sum()==85176
district['geo_code']=district.code+496
district=district.merge(demographics('DISTRICT','27'),on='geo_code',validate='one_to_one')
assert len(district)==35 and all(district.region.str.lower()==district.Name.str.lower())
def derive(d):
 d['mean_size']=d.emp_total/d.est_total.replace(0,np.nan)
 d['hired_est_pct']=100*d.est_total_hired/d.est_total.replace(0,np.nan)
 d['mining_rural_pct']=100*d.est_rural_total/d.est_total.replace(0,np.nan)
 d['est_per_100k']=1e5*d.est_total/d.population
 d['emp_per_100k']=1e5*d.emp_total/d.population
 d['log_size']=np.log(d.mean_size)
 d['log_density']=np.log1p(d.est_per_100k)
 d['sc_10pp']=d.sc_pct/10;d['st_10pp']=d.st_pct/10
 d['urban_10pp']=d.urban_pct/10;d['literacy_10pp']=d.literacy_pct/10
 return d
state=derive(state);district=derive(district)
state['is_ut_2011']=state.code.isin([4,7,25,26,31,34,35])
state.to_csv(OUT/'mining_states_matched_census2011.csv',index=False)
district.to_csv(OUT/'mining_maharashtra_districts_matched_2011.csv',index=False)
regrows=[];diagnostics=[];models={}
def regression(label,d,y,x):
 cols=[y]+x
 s=d.replace([np.inf,-np.inf],np.nan).dropna(subset=cols).copy()
 X=sm.add_constant(s[x],has_constant='add');fit=sm.OLS(s[y],X).fit(cov_type='HC3',use_t=True)
 models[label]=fit
 for term in fit.params.index:
  ci=fit.conf_int().loc[term]
  regrows.append(dict(model=label,outcome=y,term=term,beta=fit.params[term],se_hc3=fit.bse[term],p_hc3_t=fit.pvalues[term],ci_low=ci[0],ci_high=ci[1],n=int(fit.nobs),r2=fit.rsquared))
 influence=sm.OLS(s[y],X).fit().get_influence()
 cooks=influence.cooks_distance[0]
 for k,(_,r) in enumerate(s.iterrows()):
  diagnostics.append(dict(model=label,region=r.region,cooks_d=float(cooks[k]),leverage=float(influence.hat_matrix_diag[k]),residual=float(fit.resid.iloc[k])))
 for term in ['sc_10pp','st_10pp']:
  loo=[]
  for i in range(len(s)):
   f=sm.OLS(s[y].drop(s.index[i]),X.drop(s.index[i])).fit()
   loo.append(float(f.params[term]))
  diagnostics.append(dict(model=label,region='LEAVE_ONE_OUT_'+term,cooks_d=np.nan,leverage=np.nan,residual=np.nan,loo_min=min(loo),loo_max=max(loo)))
 return fit
base=['sc_10pp','st_10pp'];control=base+['urban_10pp','literacy_10pp']
regression('S1 state mining log mean size',state,'log_size',base)
regression('S2 state mining log mean size adjusted',state,'log_size',control)
regression('S3 states excluding 2011 UTs',state[~state.is_ut_2011],'log_size',control)
regression('S4 state mining establishment density',state,'log_density',control)
regression('S5 state hired establishment share',state,'hired_est_pct',control)
regression('D1 Maharashtra mining log mean size',district,'log_size',control)
regression('D2 Maharashtra mining establishment density',district,'log_density',control)
regression('D3 Maharashtra hired establishment share',district,'hired_est_pct',control)
regression('D4 Maharashtra size at least 50 establishments',district[district.est_total>=50],'log_size',control)
regdf=pd.DataFrame(regrows)
from statsmodels.stats.multitest import multipletests
mask=regdf.term.isin(['sc_10pp','st_10pp'])
regdf.loc[mask,'p_holm_18']=multipletests(regdf.loc[mask,'p_hc3_t'],method='holm')[1]
regdf.loc[mask,'q_bh_18']=multipletests(regdf.loc[mask,'p_hc3_t'],method='fdr_bh')[1]
regdf.to_csv(OUT/'regression_results.csv',index=False)
pd.DataFrame(diagnostics).to_csv(OUT/'influence_and_leave_one_out.csv',index=False)
# Group contrasts across industries are descriptive aggregates, with no firm-level inference.
cat='log_mean_size ~ C(group, Treatment(reference="Others")) + C(industry_code)'
contr=[]
for name,f in [('equal industry cells',smf.ols(cat,cells).fit()),('establishment weighted cells',smf.wls(cat,cells,weights=cells.establishments).fit())]:
 for term,b in f.params.items():
  if term.startswith('C(group'):
   contr.append(dict(model=name,term=term,beta=b,pct_contrast=100*np.expm1(b),inference='descriptive only; 92 aggregates, not microdata'))
pd.DataFrame(contr).to_csv(OUT/'descriptive_industry_fixed_effects.csv',index=False)
des=[]
for label,d in [('states_35',state),('maharashtra_districts_35',district)]:
 for v in ['est_total','emp_total','mean_size','hired_est_pct','est_per_100k','sc_pct','st_pct','urban_pct','literacy_pct']:
  a=d[v].dropna();q=a.quantile([.1,.25,.5,.75,.9])
  des.append(dict(sample=label,variable=v,n=len(a),missing=len(d)-len(a),mean=a.mean(),sd=a.std(ddof=1),min=a.min(),p10=q.loc[.1],p25=q.loc[.25],median=q.loc[.5],p75=q.loc[.75],p90=q.loc[.9],max=a.max()))
pd.DataFrame(des).to_csv(OUT/'descriptive_statistics.csv',index=False)
state[['est_total','emp_total','mean_size','hired_est_pct','est_per_100k','sc_pct','st_pct','urban_pct','literacy_pct']].corr().to_csv(OUT/'state_correlations.csv')
# Pre-study power calculations, not research observations or treatment estimates.
power=[]
for clusters in [40,80,120]:
 for icc in [.02,.05,.10]:
  m=15;ret=.8;m2=m*ret;n=clusters*m2;deff=1+(m2-1)*icc
  critical=stats.t.ppf(.975,clusters-2)+stats.norm.ppf(.8)
  power.append(dict(clusters=clusters,baseline_firms=clusters*m,retained_firms=int(n),assumed_icc=icc,design_effect=deff,mde_sd=critical*np.sqrt(4*deff/n),assumed_growth_sd=.5,mde_log_growth=critical*np.sqrt(4*deff/n)*.5))
pd.DataFrame(power).to_csv(OUT/'proposed_trial_power_assumptions.csv',index=False)
mine=cells[cells.industry_code.eq(5)].copy();mine['group']=pd.Categorical(mine.group,['SC','ST','OBC','Others']);mine=mine.sort_values('group')
fig,ax=plt.subplots(figsize=(7.6,4.5));ax.bar(mine.group.astype(str),mine.mean_size,color=['#64748b']*3+['#174b65']);ax.set(xlabel='Owner social group in proprietary establishments',ylabel='Workers per establishment',title='Mining establishment size differs across owner social groups')
for i,v in enumerate(mine.mean_size):ax.text(i,v+.09,f'{v:.2f}',ha='center')
ax.set_ylim(0,6.3);fig.text(.1,.01,'Source: MoSPI Sixth Economic Census 2013-14, Tables 12 and 15. Ratios of totals.',fontsize=8);fig.tight_layout(rect=[0,.05,1,1]);fig.savefig(FIG/'mining_size_by_social_group.png');plt.close(fig)
fig,axs=plt.subplots(1,2,figsize=(10,5))
for ax,v,title,unit in zip(axs,['est_total','emp_total'],['Mining establishments','Mining employment'],['Establishments (count)','Workers (count)']):
 a=state.nlargest(10,v).sort_values(v);ax.barh(a.region,a[v],color='#174b65');ax.set(title=title,xlabel=unit)
fig.text(.04,.01,'Source: Sixth Economic Census 2013-14 Tables 2.5 and 4.5. Andhra Pradesh includes Telangana.',fontsize=8);fig.tight_layout(rect=[0,.06,1,1]);fig.savefig(FIG/'mining_top_states.png');plt.close(fig)
fig,axs=plt.subplots(1,2,figsize=(9,4.7))
for ax,x,title in zip(axs,['sc_pct','st_pct'],['SC population share','ST population share']):
 ax.scatter(district[x],district.mean_size,s=25+district.est_total/10,color='#174b65',alpha=.7)
 for _,r in district.nlargest(3,'mean_size').iterrows():ax.annotate(r.region,(r[x],r.mean_size),fontsize=8,xytext=(3,3),textcoords='offset points')
 ax.set(xlabel=title+' (%)',ylabel='Workers per mining establishment',title='Maharashtra districts')
fig.text(.03,.01,'Sources: Maharashtra EC 2013 Tables 2.5/4.5; Census 2011 PCA. Bubble area increases with count.',fontsize=8);fig.tight_layout(rect=[0,.06,1,1]);fig.savefig(FIG/'district_population_and_size.png');plt.close(fig)
rr=pd.DataFrame(regrows);sel=rr[rr.model.isin(['S2 state mining log mean size adjusted','S3 states excluding 2011 UTs','D1 Maharashtra mining log mean size','D4 Maharashtra size at least 50 establishments']) & rr.term.isin(base)]
fig,ax=plt.subplots(figsize=(9,5));labels=[]
for i,(_,r) in enumerate(sel.iterrows()):
 ax.errorbar(r.beta,i,xerr=[[r.beta-r.ci_low],[r.ci_high-r.beta]],fmt='o',color='#174b65',capsize=3);labels.append(r.model.split(' ')[0]+' '+r.term[:2].upper())
ax.axvline(0,color='grey',linestyle='--');ax.set(yticks=range(len(labels)),yticklabels=labels,xlabel='Log mean size coefficient per 10 percentage points of population share',title='Ecological associations have wide uncertainty');ax.invert_yaxis()
fig.text(.1,.01,'OLS; HC3 95% t intervals. S2/S3 states, D1/D4 districts. Associations, not caste-tie effects.',fontsize=8);fig.tight_layout(rect=[0,.06,1,1]);fig.savefig(FIG/'regression_intervals.png');plt.close(fig)
metrics={'national_establishments':85176,'national_employment':557474,'national_mean_size':557474/85176,'rural_est_pct':62810/85176*100,'hired_est_pct':44317/85176*100,'hired_emp_pct':495282/557474*100,'proprietary_est_pct':73170/85176*100,'proprietary_emp_pct':319425/557474*100,'top5_est_share_pct':100*state.nlargest(5,'est_total').est_total.sum()/85176,'top5_emp_share_pct':100*state.nlargest(5,'emp_total').emp_total.sum()/557474,'HHI_est_states':float(np.sum((state.est_total/85176)**2)),'HHI_emp_states':float(np.sum((state.emp_total/557474)**2)),'sc_size_relative_others':float(mine[mine.group.eq('SC')].size_relative_others.iloc[0]),'mining_group_rows':mine.astype({'group':str}).to_dict('records'),'regression_rows':regrows,'power':power,'provenance':provenance}
(OUT/'results.json').write_text(json.dumps(metrics,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in metrics.items() if k not in ['regression_rows','power']},indent=2))
print(rr[rr.term.isin(base)].to_string(index=False))
