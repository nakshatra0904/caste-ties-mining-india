"""Published worker cells only: no synthetic respondents or inferred joint recruitment data."""
from pathlib import Path
import sys, json, hashlib, re
R=Path(__file__).resolve().parents[1]
W=R/'data/raw/workers';D=R/'data/derived';F=R/'figures'
import numpy as np
import pandas as pd
import openpyxl
import statsmodels.formula.api as smf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'savefig.dpi':180})
DIV={'05':'Coal and lignite','06':'Oil and natural gas','07':'Metal ores','08':'Other mining / quarrying','09':'Mining support'}
GROUPS=['SC','ST','Remaining'];COLORS=['#174B65','#D88738','#A8B8C2']
rows=[]; extraction=[]
for group,file in [('All','census_b18_all_2011.xlsx'),('SC','census_b18_sc_2011.xlsx'),('ST','census_b18_st_2011.xlsx')]:
 ws=openpyxl.load_workbook(W/file,read_only=True,data_only=True)['Sheet1']
 n=0
 for ri,a in enumerate(ws.iter_rows(values_only=True),1):
  if str(a[4]).zfill(2) not in DIV or str(a[5]).zfill(3)!='000' or str(a[6]).zfill(4)!='0000':continue
  sc=str(a[1]).zfill(2)
  if not sc.isdigit():continue
  n+=1
  region=re.sub(r'^(STATE|UNION TERRITORY)\s*-\s*','',str(a[3])).strip().title()
  for area,offset in [('Total',0),('Rural',3),('Urban',6)]:
   for sex,soff in [('Persons',0),('Male',1),('Female',2)]:
    main=int(a[8+offset+soff] or 0);marg=int(a[17+offset+soff] or 0)
    rows.append(dict(state_code=sc,region=region,division=str(a[4]).zfill(2),industry=DIV[str(a[4]).zfill(2)],group=group,area=area,sex=sex,main=main,marginal=marg,total=main+marg,source_file=file,source_sheet='Sheet1',source_excel_row=ri))
 extraction.append(dict(file=file,division_rows=n,sha256=hashlib.sha256((W/file).read_bytes()).hexdigest()))
x=pd.DataFrame(rows)
key=['state_code','division','area','sex']
assert not x.duplicated(key+['group']).any()
# Missing zero-valued division rows are explicitly padded against the common all-worker grid.
base=x[x.group.eq('All')].set_index(key)
for g in ['SC','ST']:
 z=x[x.group.eq(g)].set_index(key)
 missing=base.index.difference(z.index)
 for idx in missing:
  a=base.loc[idx].to_dict();a.update(dict(zip(key,idx)));a.update(group=g,main=0,marginal=0,total=0,source_excel_row=np.nan,source_file='No published division row; zero after matching all-worker grid')
  x=pd.concat([x,pd.DataFrame([a])],ignore_index=True)
assert x[x.group.eq('All')].state_code.nunique()==36
for g,z in x.groupby('group'):
 pivot=z.pivot(index=['state_code','division','sex'],columns='area',values=['main','marginal'])
 for v in ['main','marginal']:assert (pivot[v]['Total']==pivot[v]['Rural']+pivot[v]['Urban']).all()
 pivot=z.pivot(index=['state_code','division','area'],columns='sex',values=['main','marginal'])
 for v in ['main','marginal']:assert (pivot[v]['Persons']==pivot[v]['Male']+pivot[v]['Female']).all()
wide=x.pivot(index=key,columns='group',values=['main','marginal','total'])
rem=base.reset_index().copy();rem['group']='Remaining'
for v in ['main','marginal','total']:
 vals=wide[v]['All']-wide[v]['SC']-wide[v]['ST']
 assert (vals>=0).all(),(v,vals[vals<0])
 rem[v]=vals.reindex(base.index).values
rem['source_file']='Derived: All minus SC minus ST';rem['source_excel_row']=np.nan
x=pd.concat([x,rem],ignore_index=True)
# Verify sums across the 35 historical states/UTs match the India rows, for every cell.
for keys,z in x.groupby(['group','division','area','sex']):
 national=z[z.state_code.eq('00')]
 assert len(national)==1
 for v in ['main','marginal','total']:assert int(national[v].iloc[0])==int(z.loc[z.state_code.ne('00'),v].sum()),(keys,v)
x['marginal_pct']=np.where(x.total>0,100*x.marginal/x.total,np.nan)
x.to_csv(D/'worker_cells_census2011.csv',index=False)

def summaries(z,by):
 sums=z.groupby(by,as_index=False)[['main','marginal','total']].sum()
 sums['marginal_pct']=100*sums.marginal/sums.total
 sums['share_pct']=100*sums.total/sums.groupby([b for b in by if b!='group'],dropna=False).total.transform('sum') if len(by)>1 else 100*sums.total/sums.total.sum()
 return sums
n=x[x.state_code.eq('00') & x.area.eq('Total') & x.sex.eq('Persons') & x.group.ne('All')]
national=summaries(n,['group']);national.to_csv(D/'worker_national_composition2011.csv',index=False)
bydiv=summaries(n,['division','industry','group']);bydiv.to_csv(D/'worker_division_composition2011.csv',index=False)
states=summaries(x[x.state_code.ne('00')&x.area.eq('Total')&x.sex.eq('Persons')&x.group.ne('All')],['state_code','region','group']);states.to_csv(D/'worker_state_composition2011.csv',index=False)
sex=summaries(x[x.state_code.eq('00')&x.area.eq('Total')&x.sex.ne('Persons')&x.group.ne('All')],['sex','group']);sex.to_csv(D/'worker_sex_duration2011.csv',index=False)

# Employment-weighted aggregate LPM. Cell weights are denominators, never microdata n.
a=x[x.state_code.ne('00')&x.area.ne('Total')&x.sex.ne('Persons')&x.group.ne('All')&x.total.gt(0)].copy()
a['group']=pd.Categorical(a.group,categories=['Remaining','SC','ST'])
specs=[('W1','Group only','marginal_pct ~ C(group)'),('W2','Sex + rural/urban','marginal_pct ~ C(group) + C(sex) + C(area)'),('W3','Sex + area + state + division','marginal_pct ~ C(group) + C(sex) + C(area) + C(state_code) + C(division)'),('W4','State-division-sex-area strata','marginal_pct ~ C(group) + C(stratum)')]
a['stratum']=a.state_code+'_'+a.division+'_'+a.sex+'_'+a.area
fits=[];allcoef=[];models=[]
for code,controls,formula in specs:
 model=smf.wls(formula,a,weights=a.total).fit(cov_type='cluster',cov_kwds={'groups':a.state_code,'use_correction':True},use_t=True)
 ci=model.conf_int()
 models.append(dict(model=code,controls=controls,n_cells=len(a),n_states=a.state_code.nunique(),weight_total=int(a.total.sum()),r2=model.rsquared,rank=int(model.model.rank),formula=formula))
 for term in model.params.index:
  rec=dict(model=code,controls=controls,term=term,beta_pp=model.params[term],se_cluster_state=model.bse[term],p_model_based=model.pvalues[term],ci_low=ci.loc[term,0],ci_high=ci.loc[term,1],n_cells=len(a),n_states=a.state_code.nunique(),weight_total=int(a.total.sum()))
  allcoef.append(rec)
  if term in ['C(group)[T.SC]','C(group)[T.ST]']:fits.append(rec)
fits=pd.DataFrame(fits);fits.to_csv(D/'worker_controlled_contrasts2011.csv',index=False)
pd.DataFrame(allcoef).to_csv(D/'worker_regression_all_coefficients2011.csv',index=False)
pd.DataFrame(models).to_csv(D/'worker_model_specs2011.csv',index=False)
a.to_csv(D/'worker_regression_cells2011.csv',index=False)

coal=[]
counts={2024:[('A',15439,2491,1037,3361,None),('B',16368,2229,1627,3835,None),('C',113796,21361,17270,26750,None),('D',85455,18520,13209,24350,None)],2026:[('A',15014,2513,1079,3765,278),('B',12648,1617,1042,2199,5),('C',101410,16180,12521,19124,166),('D',85261,15041,12113,15307,61)]}
for year,vals in counts.items():
 for employment_group,total,sc,st,obc,ews in vals:
  for g,count in [('SC',sc),('ST',st),('OBC',obc),('Remaining',total-sc-st-obc)]:
   coal.append(dict(snapshot=f'{year}-01-01',employment_group=employment_group,group=g,count=count,total=total,share_pct=100*count/total,ews_separately_published=ews if g=='Remaining' else np.nan,source=f'Coal Ministry annual report {year-1}-{str(year)[-2:]} chapter 16',pdf_page=5 if year==2024 else 4))
coal=pd.DataFrame(coal);coal.to_csv(D/'coal_india_workforce_composition.csv',index=False)
ct=coal.groupby(['snapshot','group'],as_index=False)['count'].sum();ct['total']=ct.groupby('snapshot')['count'].transform('sum');ct['share_pct']=100*ct['count']/ct['total'];ct.to_csv(D/'coal_india_snapshot_totals.csv',index=False)
assert ct[ct.snapshot.eq('2024-01-01')]['count'].sum()==231058
assert ct[ct.snapshot.eq('2026-01-01')]['count'].sum()==214333
routes=pd.DataFrame([['Relatives / co-workers',40,80,'40 derived from reported 80% of 50'],['Approached employer',7,14,'Published count 7'],['Contractor',3,6,'Published count 3']],columns=['route','count','share_pct','count_status'])
routes['sample']='Makrana individual interviews';routes['n']=50;routes['source']='Arisa / CLRA 2024';routes['pdf_page']=29;routes.to_csv(D/'makrana_recruitment_routes.csv',index=False)
local=pd.DataFrame([['Budhpura','SC',36,'Composition paragraph does not explicitly resolve 37 main vs 47 including home-workers',16],['Budhpura','ST',19,'Composition paragraph does not explicitly resolve 37 main vs 47 including home-workers',16],['Budhpura','OBC',45,'Composition paragraph does not explicitly resolve 37 main vs 47 including home-workers',16],['Makrana','SC',82,'50 individual interviewees',27],['Makrana','ST',0,'50 individual interviewees; no ST interviewees reported',27],['Makrana','OBC',18,'50 individual interviewees',27]],columns=['site','group','published_pct','denominator_note','pdf_page']);local.to_csv(D/'rajasthan_stone_worker_composition.csv',index=False)
ilo=pd.DataFrame([['SC',34],['ST',30],['OBC',30],['General',5]],columns=['group','published_pct']);ilo['n']=115;ilo['source']='ILO 2021 Rajasthan natural stone report';ilo['pdf_page']=55;ilo['note']='Rounded percentages sum to 99; not normalized and not converted to individual counts';ilo.to_csv(D/'ilo_stone_worker_composition2021.csv',index=False)
profiles=pd.DataFrame([
 ['Makrana','Male',45,50,90,'Arisa/CLRA',27,'Count-based'],['Makrana','Illiterate',20,50,40,'Arisa/CLRA',28,'Count-based'],['Makrana','Secondary education or higher',7,50,14,'Arisa/CLRA',28,'Count-based'],['Makrana','Lives locally',48,50,96,'Arisa/CLRA',28,'Count-based'],['Makrana','Uses any PPE',20,50,40,'Arisa/CLRA',31,'Count-based; not adequate protection measure'],['Makrana','Advance received',18,50,36,'Arisa/CLRA',30,'Count-based paragraph; concluding text instead says 38%; discrepancy retained'],['Makrana','Written employment contract',0,50,0,'Arisa/CLRA',29,'Reported none'],['Makrana','Piece-rate paid',np.nan,50,60,'Arisa/CLRA',29,'Published percentage'],['Budhpura main questionnaire','Piece-rate paid',31,37,100*31/37,'Arisa/CLRA',18,'Main instrument excludes 10 home-workers'],['Budhpura main questionnaire','Uses any PPE',21,37,100*21/37,'Arisa/CLRA',23,'Any use; not adequate protection measure'],['ILO Rajasthan two clusters','Illiterate',np.nan,115,40,'ILO',55,'Published rounded percentage'],['ILO Rajasthan two clusters','Has bank account',np.nan,115,30,'ILO',55,'Published rounded percentage'],['ILO Rajasthan two clusters','Resides in work district',np.nan,115,92,'ILO',55,'Published rounded percentage'],['ILO mine-worker subgroup','Provident Fund access',np.nan,np.nan,21,'ILO',62,'Subgroup denominator not reconstructed from 115'],['ILO processing-worker subgroup','Provident Fund access',np.nan,np.nan,29,'ILO',62,'Subgroup denominator not reconstructed from 115']
 ],columns=['sample','indicator','numerator','denominator','pct','producer','pdf_page','measurement_note']);profiles.to_csv(D/'stone_worker_other_details.csv',index=False)
duration=pd.DataFrame([['Mines','Male',10],['Mines','Female',4.5],['Processing','Male',10],['Processing','Female',8.5]],columns=['stage','sex','months_per_year']);duration['source']='ILO 2021, PDF page 59';duration.to_csv(D/'ilo_stone_working_year.csv',index=False)
rec=pd.DataFrame([['UR',131,131],['SC',48,48],['ST',97,92],['EWS',32,32],['OBC',42,42]],columns=['vacancy_category','advertised','filled']);rec['unfilled']=rec.advertised-rec.filled;rec['fill_pct']=100*rec.filled/rec.advertised;rec['recruitment']='SECL Mining Sirdar FY2024-25';rec['source']='Coal Ministry Annual Report 2025-26, chapter 16';rec.to_csv(D/'secl_vacancy_filling2024_25.csv',index=False)
assert rec.advertised.sum()==350 and rec.filled.sum()==345

def save(name,title,source):
 plt.suptitle(title,fontsize=13,y=.99)
 plt.figtext(.02,.012,source,fontsize=8)
 plt.tight_layout(rect=[0,.075,1,.95]);plt.savefig(F/name,bbox_inches='tight');plt.close()
z=bydiv.pivot(index='division',columns='group',values='share_pct').reindex(columns=GROUPS)
ax=z.plot.bar(stacked=True,color=COLORS,figsize=(9,5));ax.set_xticklabels([DIV[d] for d in z.index],rotation=15,ha='right');ax.set_ylabel('Share of workers (%)');ax.set_xlabel('NIC 2008 division');ax.legend(title='Social group',loc='upper left',bbox_to_anchor=(1,1))
save('worker_caste_by_mining_division.png','Worker composition differs across mining subsectors','Census 2011 B18 / B18SC / B18ST; main + marginal, all sexes. Remaining = All - SC - ST (includes OBC).')
fig,axs=plt.subplots(1,2,figsize=(10,4.7),sharey=True)
for ax,gender in zip(axs,['Male','Female']):
 z=sex[sex.sex.eq(gender)].set_index('group').reindex(GROUPS);ax.bar(z.index,z.marginal_pct,color=COLORS);ax.set_title(gender);ax.set_ylabel('Marginal workers / all workers (%)')
save('worker_sex_and_work_duration.png','Work duration by social group and sex','Census 2011, NIC 05-09. Marginal = worked <6 months; does not measure contract status or job quality.')
fig,ax=plt.subplots(figsize=(9,5.8));offset={'SC':-.1,'ST':.1}
for g,col in [('SC',COLORS[0]),('ST',COLORS[1])]:
 z=fits[fits.term.eq(f'C(group)[T.{g}]')];ys=np.arange(len(z))+offset[g];ax.errorbar(z.beta_pp,ys,xerr=np.array([z.beta_pp-z.ci_low,z.ci_high-z.beta_pp]),fmt='o',label=g,color=col,capsize=4)
ax.axvline(0,color='gray',lw=1);ax.set_yticks(range(4),['W1: group only','W2: sex + residence','W3: + state + mineral division','W4: matched joint strata']);ax.invert_yaxis();ax.set_xlabel('Marginal-worker share contrast vs Remaining (percentage points)');ax.legend()
save('worker_controlled_duration_contrasts.png','Unadjusted and controlled worker-cell comparisons','Employment-weighted aggregate WLS; state-clustered model intervals. No causal effects; no age/education controls.')
fig,axs=plt.subplots(1,2,figsize=(11,5),sharey=True)
for ax,year in zip(axs,['2024-01-01','2026-01-01']):
 z=coal[coal.snapshot.eq(year)].pivot(index='employment_group',columns='group',values='share_pct').reindex(columns=['SC','ST','OBC','Remaining']);z.plot.bar(stacked=True,ax=ax,color=COLORS[:2]+['#6B9278',COLORS[2]],legend=False);ax.set_title(year);ax.set_xlabel('Employment group');ax.set_ylabel('Share of reported employees (%)');ax.set_xticklabels(z.index,rotation=0)
axs[1].legend(['SC','ST','OBC','Remaining'],loc='upper left',bbox_to_anchor=(1,1))
save('coal_india_employee_composition.png','Coal India employee composition: two administrative snapshots','Coal Ministry reports, chapter 16. Corporate employee stocks, not all mining workers; Remaining includes EWS in 2026.')
fig,ax=plt.subplots(figsize=(8,4.7));ax.barh(routes.route[::-1],routes.share_pct[::-1],color=COLORS);ax.set_xlim(0,100);ax.set_xlabel('Share of 50 interviewed workers (%)')
for i,v in enumerate(routes.share_pct[::-1]):ax.text(v+1,i,f'{v:.0f}%',va='center')
save('makrana_job_recruitment_routes.png','How interviewed Makrana stone workers obtained jobs','Arisa / CLRA 2024, PDF p29. Local non-probability sample; relatives/co-workers does not establish same-caste referrals.')
z=states[states.group.isin(['SC','ST'])].pivot(index='region',columns='group',values='share_pct');z['combined']=z.SC+z.ST
z=z.nlargest(15,'combined').sort_values('combined')
ax=z[['SC','ST']].plot.barh(stacked=True,color=COLORS[:2],figsize=(8,7));ax.set_xlabel('Share of mining workers (%)');ax.set_ylabel('Historical 2011 state / UT');ax.legend(loc='lower right')
save('worker_sc_st_state_composition.png','Fifteen highest SC + ST worker shares in mining','Census 2011 B18, NIC 05-09. Rankings include small workforces; full counts for all 35 regions are in the CSV/report.')
z=duration.pivot(index='stage',columns='sex',values='months_per_year').reindex(columns=['Male','Female'])
ax=z.plot.bar(color=COLORS[:2],figsize=(8,4.8));ax.set_ylabel('Reported average months worked per year');ax.set_xlabel('Supply-chain stage');ax.set_xticklabels(z.index,rotation=0);ax.set_ylim(0,12)
save('ilo_gender_working_year.png','Working-year differences in the Rajasthan stone study','ILO 2021, PDF p59. Local published averages; occupation, caste and other controls unavailable in this summary.')
summary={'national_workers':int(n.total.sum()),'national_groups':national.to_dict('records'),'controlled_contrasts':fits.to_dict('records'),'model_specs':models,'extraction':extraction,'census_checks':'sex sums, rural/urban sums, nonnegative group residuals, state-to-India sums passed','causal_effect_estimated':False,'missing_individual_controls':['age','education','occupation','tenure','firm characteristics'],'new_figures':7,'census_statistical_basis':'Published B18 industrial classification counts. Source metadata describes counts; no usable sampling/design variance is provided here. State-clustered regression intervals describe a statistical model, not Census enumeration error.'}
(D/'worker_results.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps({'workers':summary['national_workers'],'groups':summary['national_groups'],'contrasts':fits[['model','term','beta_pp','ci_low','ci_high']].to_dict('records'),'models':models,'extraction':extraction},indent=2))
