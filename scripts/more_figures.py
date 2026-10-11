from pathlib import Path
import sys
R=Path(__file__).resolve().parents[1]
import numpy as np,pandas as pd,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
D=R/'data/derived';F=R/'figures'
plt.rcParams.update({'font.size':9,'axes.spines.top':False,'axes.spines.right':False,'figure.dpi':160})
s=pd.read_csv(D/'mining_states_matched_census2011.csv');d=pd.read_csv(D/'mining_maharashtra_districts_matched_2011.csv');c=pd.read_csv(D/'industry_social_group_cells_2013.csv');r=pd.read_csv(D/'regression_results.csv');inf=pd.read_csv(D/'influence_and_leave_one_out.csv');p=pd.read_csv(D/'proposed_trial_power_assumptions.csv')
def save(fig,name,caption):
 fig.text(.06,.01,caption,fontsize=7);fig.tight_layout(rect=[0,.055,1,1]);fig.savefig(F/name);plt.close(fig)
m=c[c.industry_code==5].set_index('group').loc[['SC','ST','OBC','Others']]
fig,ax=plt.subplots(figsize=(8,4));x=np.arange(4);ax.bar(x-.18,m.est_share_pct,.36,label='Establishments',color='#174b65');ax.bar(x+.18,m.emp_share_pct,.36,label='Employment',color='#8da1ac');ax.set(xticks=x,xticklabels=m.index,ylabel='Share of proprietary mining total (%)',xlabel='Owner social group',title='Ownership shares and employment shares diverge');ax.legend();save(fig,'social_group_shares.png','Source: MoSPI EC 2013-14 Tables 12 and 15. Shares recomputed from counts.')
fig,ax=plt.subplots(figsize=(9,6));z=c[c.group=='SC'].sort_values('size_relative_others');ax.barh(z.industry,z.size_relative_others,color=['#a3b3bb' if i!=5 else '#174b65' for i in z.industry_code]);ax.axvline(1,color='grey',ls='--');ax.set(xlabel='SC / Others: workers per establishment',title='SC ownership size contrast across 23 industries');save(fig,'cross_industry_sc_size_ratios.png','Source: EC 2013-14 Tables 12 and 15. Aggregated proprietary establishments only.')
fig,axs=plt.subplots(1,2,figsize=(9,4));
for ax,a,title in zip(axs,[s,d],['35 historical state/UT regions','35 Maharashtra districts']):
 ax.hist(a.mean_size.dropna(),bins=[0,3,6,10,20,40,60],color='#174b65',edgecolor='white');ax.set(xlabel='Workers per mining establishment',ylabel='Regions (count)',title=title)
save(fig,'regional_size_distributions.png','Source: EC 2013-14 and Maharashtra EC 2013. Region means, not individual-firm size distributions.')
fig,ax=plt.subplots(figsize=(8,6));z=s.nlargest(15,'est_per_100k').sort_values('est_per_100k');ax.barh(z.region,z.est_per_100k,color='#174b65');ax.set(xlabel='Mining establishments per 100,000 residents',ylabel='Historical state/UT region',title='Mining establishment density varies geographically');save(fig,'mining_density_states.png','Sources: EC 2013-14 and Census 2011 PCA. Undivided AP includes Telangana.')
fig,ax=plt.subplots(figsize=(8,6));corr=s[['mean_size','hired_est_pct','est_per_100k','sc_pct','st_pct','urban_pct','literacy_pct']].corr();im=ax.imshow(corr,vmin=-1,vmax=1,cmap='BrBG');ax.set(xticks=range(7),yticks=range(7),xticklabels=corr.columns,yticklabels=corr.columns,title='State-level correlations are contextual associations');plt.setp(ax.get_xticklabels(),rotation=45,ha='right');
for i in range(7):
 for j in range(7):ax.text(j,i,f'{corr.iloc[i,j]:.2f}',ha='center',va='center',fontsize=8)
fig.colorbar(im,ax=ax,label='Pearson correlation');save(fig,'state_correlation_heatmap.png','Sources: EC 2013-14; Census 2011 PCA. Pairwise-complete observations; no causal interpretation.')
fig,axs=plt.subplots(1,3,figsize=(12,6));z=r[r.term.isin(['sc_10pp','st_10pp'])]
for ax,codes,title in zip(axs,[['S1','S2','S3','D1','D4'],['S4','D2'],['S5','D3']],['Log mean size','Log (1 + density)','Hired-establishment share (pp)']):
 arows=z[z.model.str.split().str[0].isin(codes)];labs=[]
 for i,(_,a) in enumerate(arows.iterrows()):
  ax.errorbar(a.beta,i,xerr=[[a.beta-a.ci_low],[a.ci_high-a.beta]],fmt='o',color='#174b65',capsize=2);labs.append(a.model.split(' ')[0]+' '+a.term[:2].upper())
 ax.set(yticks=range(len(arows)),yticklabels=labs,xlabel='Coefficient per 10 pp',title=title);ax.axvline(0,color='grey',ls='--');ax.invert_yaxis()
save(fig,'all_regression_intervals.png','All 18 SC/ST composition coefficients; 95% HC3 intervals. Panels use different outcome units and scales.')
fig,axs=plt.subplots(1,2,figsize=(10,4.5));
for ax,model in zip(axs,['S2 state mining log mean size adjusted','D1 Maharashtra mining log mean size']):
 z=inf[(inf.model==model)&~inf.region.str.startswith('LEAVE')].nlargest(8,'cooks_d').sort_values('cooks_d');ax.barh(z.region,z.cooks_d,color='#174b65');ax.set(xlabel="Cook's distance",title=model.split(' ')[0]+' influence diagnostics')
save(fig,'influence_diagnostics.png','OLS influence on adjusted log-size models. Large values identify sensitivity, not erroneous observations.')
fig,ax=plt.subplots(figsize=(8,4));
for icc,g in p.groupby('assumed_icc'):ax.plot(g.baseline_firms,g.mde_sd,marker='o',label=f'Assumed ICC {icc:.2f}')
ax.set(xlabel='Baseline firms (15 per cluster)',ylabel='Minimum detectable effect (outcome SD)',title='Proposed trial power depends on clustering');ax.legend();save(fig,'proposed_trial_power.png','Design calculation only: 80% power, 5% two-sided test, equal assignment, 20% attrition. No trial was run.')
print('Generated 8 additional figures; 12 PNG files in total.')
