"""Build a standalone LaTeX report, with all data tables and inline vector plots."""
from pathlib import Path
import sys, json, re, math
R=Path(__file__).resolve().parents[1]
import numpy as np
import pandas as pd
D=R/'data/derived'; O=R/'report'
s=pd.read_csv(D/'mining_states_matched_census2011.csv')
d=pd.read_csv(D/'mining_maharashtra_districts_matched_2011.csv')
c=pd.read_csv(D/'industry_social_group_cells_2013.csv')
reg=pd.read_csv(D/'regression_results.csv')
inf=pd.read_csv(D/'influence_and_leave_one_out.csv')
power=pd.read_csv(D/'proposed_trial_power_assumptions.csv')
sources=json.loads((R/'provenance/source_catalogue.json').read_text(encoding='utf-8'))
result=json.loads((D/'results.json').read_text())
out=[]
def emit(t):out.append(t)
def esc(t):
 t=str(t).replace('\u2019',"'").replace('\u2013','--').replace('\u2014','---').replace('\u00a0',' ')
 return ''.join({'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}.get(x,x) for x in t)
def prose(t):
 parts=re.split(r'(https?://\S+|\[S\d{2}\])',t)
 z=[]
 for p in parts:
  if p.startswith('http'):z.append(r'\url{'+p.rstrip('.')+'}'+('.' if p.endswith('.') else ''))
  elif re.fullmatch(r'\[S\d{2}\]',p):z.append(r'\hyperlink{'+p[1:-1]+'}{'+p+'}')
  else:z.append(esc(p))
 return ''.join(z)
def num(v,k=2):
 if pd.isna(v):return '--'
 return f'{v:,.{k}f}'
def row(v):return ' & '.join(v)+r' \\'
def lt(caption,headers,rows,align=None):
 emit(r'\begingroup\footnotesize\setlength{\tabcolsep}{4pt}')
 emit(r'\begin{longtable}{'+(align or 'l'+'r'*(len(headers)-1))+'}')
 emit(r'\caption{'+esc(caption)+r'}\\\toprule')
 emit(row([esc(x) for x in headers])+r'\midrule\endfirsthead')
 emit(r'\multicolumn{'+str(len(headers))+r'}{l}{\textit{Continued from previous page}}\\\toprule')
 emit(row([esc(x) for x in headers])+r'\midrule\endhead')
 emit(r'\midrule\multicolumn{'+str(len(headers))+r'}{r}{\textit{Continued on next page}}\\\endfoot\bottomrule\endlastfoot')
 emit('\n'.join(row(x) for x in rows))
 emit(r'\end{longtable}\endgroup')
def figstart():emit(r'\clearpage\begin{figure}[p]\centering')
def figend(caption):emit(r'\caption{'+esc(caption)+r'}\end{figure}\clearpage')
def axis(opts,plots):
 return '\\begin{tikzpicture}\n\\begin{axis}['+opts+']\n'+plots+'\n\\end{axis}\n\\end{tikzpicture}\n'
def coords(x,y):return ' '.join(f'({a:.7g},{b:.7g})' for a,b in zip(x,y))
def bars(z,value,title,xlabel,height='10cm'):
 labs=','.join('{'+esc(x)+'}' for x in z.region)
 opts=f'width=15cm,height={height},xbar,xmin=0,ytick={{'+','.join(map(str,range(len(z))))+'},yticklabels={'+labs+'},tick label style={font=\\scriptsize},yticklabel style={text width=4.5cm,align=right},xlabel={'+esc(xlabel)+'},title={'+esc(title)+'},bar width=6pt,axis x line*=bottom,axis y line*=left,enlarge y limits=0.06'
 return axis(opts,r'\addplot[fill=navy,draw=navy] coordinates {'+coords(z[value],range(len(z)))+'};')
def forest(z,title,width='15cm',height='11cm'):
 labs=[a.model.split()[0]+' '+a.term[:2].upper() for _,a in z.iterrows()]
 plots=r'\addplot[gray,dashed,mark=none] coordinates {(0,-0.5)(0,'+str(len(z)-.5)+')};\n'
 co=' '.join(f'({a.beta:.7g},{i}) +- ({(a.ci_high-a.ci_low)/2:.7g},0)' for i,(_,a) in enumerate(z.iterrows()))
 plots+=r'\addplot+[only marks,mark=*,navy,error bars/.cd,x dir=both,x explicit,error bar style={navy}] coordinates {'+co+'};'
 opts='width='+width+',height='+height+',ytick={'+','.join(map(str,range(len(z))))+'},yticklabels={'+','.join('{'+x+'}' for x in labs)+'},y dir=reverse,tick label style={font=\\scriptsize},xlabel={Coefficient per 10 percentage points},title={'+esc(title)+'},enlarge y limits=0.08'
 return axis(opts,plots)
emit(r'''\documentclass[11pt,a4paper]{report}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[margin=2cm]{geometry}
\usepackage{amsmath,amssymb,booktabs,longtable,array,xcolor,colortbl}
\usepackage{tikz,pgfplots}
\pgfplotsset{compat=1.18}
\usepackage[breaklinks=true,colorlinks=true,linkcolor=blue!45!black,urlcolor=blue!55!black]{hyperref}
\usepackage{xurl}
\definecolor{navy}{HTML}{174B65}
\definecolor{muted}{HTML}{8DA1AC}
\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt}
\setcounter{tocdepth}{1}
\setcounter{secnumdepth}{1}
\emergencystretch=3em
\Urlmuskip=0mu plus 2mu\relax
\hypersetup{pdftitle={Caste Ties and Firm Growth in India's Mining Industry},pdfauthor={nakshatra0904}}
\begin{document}
\begin{titlepage}
\centering\vspace*{2cm}
{\Huge\bfseries Caste Ties and Firm Growth\par}
\vspace{0.5cm}{\LARGE India's Mining Industry\par}
\vspace{1cm}{\Large Public-data evidence, source inventory,\par fieldwork design and causal identification\par}
\vspace{1.5cm}{\large Detailed research report\par nakshatra0904\par 11 October 2026\par}
\vfill
\begin{minipage}{0.88\textwidth}
\textbf{Evidence boundary.} I analyzed historical aggregate data from the Sixth Economic Census and Census 2011, fitted nine regional establishment specifications and four controlled worker-duration models, and prepared nineteen figures and a 65-entry source inventory. I did not observe caste ties or longitudinal firm growth and have not estimated a causal caste-network effect. Prospective designs and trial-power calculations are explicitly identified as proposals.
\end{minipage}
\vspace{1cm}
\end{titlepage}
\pagenumbering{roman}
\chapter*{Abstract}\addcontentsline{toc}{chapter}{Abstract}
I extracted mining and quarrying tables containing 85,176 establishments and 557,474 workers. Within the proprietary subset, workers per establishment are 2.63 for SC owners, 3.68 for ST owners, 3.77 for OBC owners and 5.62 for the residual Others category. These aggregate ratios establish a historical difference in establishment scale. They do not identify a network mechanism, an individual-firm size distribution or growth. A demographic merge supports regressions for 35 historical state/UT regions and 35 Maharashtra districts. Adjusted log-size associations with SC and ST population shares have wide HC3 intervals. One unadjusted state-density coefficient has $p=0.036$, but its Benjamini--Hochberg value is $0.651$ across the specified 18-coefficient family. A detailed prospective design combines consent-based relationship measurement, repeated firm outcomes, administrative linkage and a randomized business-introduction intervention. The added Census worker baseline contains 2,105,736 workers, 20.87 percent SC and 17.32 percent ST. Within state-division-sex-residence strata, employment-weighted SC and ST marginal-duration contrasts versus the residual group are +1.49 and +5.08 percentage points; these are descriptive adjusted associations. Local Rajasthan studies report job-entry routes, caste composition and working conditions; Coal India administrative snapshots add employee and vacancy information. I retained all observed-data tables, all nineteen figures, source access classifications and fieldwork modules in this reproducible package.
\tableofcontents\listoffigures\listoftables\clearpage
\pagenumbering{arabic}
''')
md=(R/'report/narrative.md').read_text(encoding='utf-8')
md=md.replace('# Why the completed results cannot identify caste ties and growth', (R/'report/worker_narrative.md').read_text(encoding='utf-8')+'\n# Why the completed results cannot identify caste ties and growth')
inmath=False; para=[]
def flush():
 if para:emit(prose(' '.join(para))+'\n');para.clear()
for l in md.splitlines():
 if l=='```math':flush();emit(r'\[');inmath=True
 elif l=='```':emit(r'\]');inmath=False
 elif inmath:emit(l)
 elif l.startswith('# '):flush();emit(r'\chapter{'+esc(l[2:])+'}')
 elif l.startswith('## '):flush();emit(r'\section{'+esc(l[3:])+'}')
 elif not l.strip():flush()
 else:para.append(l)
flush()

emit(r'\chapter{All graphical results}')
emit('Every graph generated for this study is reproduced below using inline vector coordinates. The archive also contains nineteen PNG versions. State geography is harmonized to Census 2011; district geography uses the 35 historical Maharashtra districts. Captions state the population and units. Proposed trial power is a design calculation, not an observed treatment effect.')
m=c[c.industry_code.eq(5)].set_index('group').loc[['SC','ST','OBC','Others']]
figstart()
emit(axis('width=15cm,height=9cm,ybar,bar width=22pt,xtick={0,1,2,3},xticklabels={SC,ST,OBC,Others},ymin=0,ylabel={Workers per establishment},xlabel={Owner social group},nodes near coords,point meta=explicit symbolic,enlarge x limits=0.2',r'\addplot[fill=navy,draw=navy] coordinates {'+' '.join(f'({i},{a.mean_size:.7g}) [{a.mean_size:.2f}]' for i,(_,a) in enumerate(m.iterrows()))+'};'))
figend('Mean employment scale by owner social group. Proprietary mining and quarrying establishments only. Source: EC6 Tables 12 and 15, PDF pages 195 and 198. Ratios of totals, not firm medians. Others is a residual category.')
figstart()
emit(bars(s.nlargest(10,'est_total').sort_values('est_total'),'est_total','Top ten regions by establishments','Establishments (count)','8cm'))
emit(r'\par\vspace{0.5cm}')
emit(bars(s.nlargest(10,'emp_total').sort_values('emp_total'),'emp_total','Top ten regions by employment','Workers (count)','8cm'))
figend('Geographic concentration in establishments and workers. Mining and quarrying, all ownership forms. Sources: EC6 Tables 2.5 and 4.5. Undivided Andhra Pradesh combines residual Andhra Pradesh and Telangana for comparability with Census 2011.')
figstart()
for v,title in [('sc_pct','SC population share'),('st_pct','ST population share')]:
 scatter=''
 for _,a in d.iterrows():
  size=0.35*math.sqrt(25+a.est_total/10)
  scatter+=r'\addplot[only marks,mark=*,navy,opacity=0.7,mark size='+f'{size:.3f}pt'+'] coordinates {'+coords([a[v]],[a.mean_size])+'};\n'
 emit(axis('width=15cm,height=8cm,xlabel={'+title+' (percent)},ylabel={Workers per establishment},title={Maharashtra historical districts},ymin=0',scatter))
 emit(r'\par\vspace{0.3cm}')
figend('District population composition and mining establishment scale. Each point is one of 35 historical Maharashtra districts; marker area increases with establishment count. Sources: Maharashtra EC6 and Census 2011 PCA. Population shares are contextual variables, not owner identities or caste relationships. Chandrapur has mean size 58.5.')
figstart()
z=reg[reg.term.isin(['sc_10pp','st_10pp']) & reg.model.str.split().str[0].isin(['S2','S3','D1','D4'])]
emit(forest(z,'Selected adjusted log-size specifications'))
figend('Selected SC and ST population-composition coefficients with 95 percent HC3 intervals. S2 all nonempty state/UT regions; S3 excludes 2011 UTs; D1 all Maharashtra districts; D4 districts with at least 50 mining establishments. Outcome is log workers per establishment. Intervals are model-based, not census sampling errors.')
figstart()
opts='width=15cm,height=9cm,ybar,bar width=15pt,xtick={0,1,2,3},xticklabels={SC,ST,OBC,Others},ymin=0,ylabel={Share of proprietary mining total (percent)},xlabel={Owner social group},legend style={at={(0.5,-0.18)},anchor=north,legend columns=2},enlarge x limits=0.2'
plots=''
for v,col,lab in [('est_share_pct','navy','Establishments'),('emp_share_pct','muted','Employment')]:plots+=r'\addplot[fill='+col+',draw='+col+'] coordinates {'+coords(range(4),m[v])+'};\n'+r'\addlegendentry{'+lab+'}\n'
emit(axis(opts,plots))
figend('Owner-group shares of establishments and employment. Proprietary mining only, recomputed from exact counts. Sources: EC6 Tables 12 and 15. The lower SC employment share relative to establishment share reflects smaller aggregate employment scale.')
figstart()
z=c[c.group.eq('SC')].sort_values('size_relative_others').copy();z['region']=z.industry
plot=bars(z,'size_relative_others','SC-owned scale relative to Others-owned scale','Ratio of workers per establishment','17cm')
# Add a reference line at equality within the same axis.
plot=plot.replace(r'\end{axis}',r'\addplot[gray,dashed,mark=none] coordinates {(1,-1)(1,23)};'+r'\end{axis}')
emit(plot)
figend('Cross-industry SC to Others mean-size ratios for 23 EC6 broad industries. Proprietary establishments only. Sources: Tables 12 and 15. A ratio of one is equal aggregate scale. These are broad-sector cells, not adjusted firm-level treatment effects; mining is the Mining and quarrying row.')
figstart()
bins=np.array([0,3,6,10,20,40,60])
for a,title in [(s,'Historical state/UT regions (33 nonempty)'),(d,'Maharashtra districts (35)')]:
 hist,_=np.histogram(a.mean_size.dropna(),bins=bins)
 emit(axis('width=15cm,height=7.5cm,ybar interval,xtick={0,3,6,10,20,40,60},xmin=0,xmax=60,ymin=0,xlabel={Workers per mining establishment},ylabel={Regions (count)},title={'+title+'}',r'\addplot[fill=navy,draw=white] coordinates {'+coords(bins,np.r_[hist,0])+'};'))
 emit(r'\par\vspace{0.3cm}')
figend('Distribution of regional mean sizes. EC6 mining counts and employment. These histograms describe variation in regional ratios, not a size distribution of individual firms. Bin boundaries are 0, 3, 6, 10, 20, 40 and 60 workers per establishment.')
figstart()
emit(bars(s.nlargest(15,'est_per_100k').sort_values('est_per_100k'),'est_per_100k','Top fifteen regions by mining establishment density','Establishments per 100,000 residents','14cm'))
figend('Historical mining establishment density. Sources: EC6 establishment counts and Census 2011 total population. Counts include all ownership forms; the population denominator predates EC6. Undivided Andhra Pradesh includes Telangana.')
figstart()
vs=['mean_size','hired_est_pct','est_per_100k','sc_pct','st_pct','urban_pct','literacy_pct']
labs=['Size','Hired share','Density','SC share','ST share','Urban','Literacy']
cor=s[vs].corr()
emit(r'\small\begin{tabular}{lrrrrrrr}\toprule')
emit(row(['']+[esc(x) for x in labs]))
for i,v in enumerate(vs):
 vals=[]
 for j,w in enumerate(vs):
  a=cor.loc[v,w];col='navy' if a>=0 else 'orange'
  vals.append(r'\cellcolor{'+col+'!'+str(round(abs(a)*40))+'}'+f'{a:.2f}')
 emit(row([esc(labs[i])]+vals))
emit(r'\bottomrule\end{tabular}')
figend('State-level Pearson correlation heatmap. Pairwise-complete observations: 33 for pairs involving size or hired share, 35 otherwise. Blue indicates positive correlation and orange negative correlation; intensity reflects absolute magnitude. Hired share means the share of establishments with hired workers, not the share of workers who are hired. Sources: EC6 and Census 2011.')
figstart()
for codes,title,h in [(['S1','S2','S3','D1','D4'],'Log mean size','7.5cm'),(['S4','D2'],'Log (1 + establishment density)','4.8cm'),(['S5','D3'],'Hired-establishment share (percentage points)','4.8cm')]:
 z=reg[reg.term.isin(['sc_10pp','st_10pp'])&reg.model.str.split().str[0].isin(codes)]
 emit(forest(z,title,height=h))
 emit(r'\par\vspace{0.2cm}')
figend('All 18 social-composition coefficients in nine models, with 95 percent HC3 intervals. Panels use separate outcome units; compare coefficients within an outcome, not across panels. SC/ST shares are scaled in ten percentage points. None passes the stated Holm or Benjamini--Hochberg adjustment over the 18-coefficient family.')
figstart()
for model,title in [('S2 state mining log mean size adjusted','S2 state adjusted log size'),('D1 Maharashtra mining log mean size','D1 district adjusted log size')]:
 z=inf[inf.model.eq(model)&~inf.region.str.startswith('LEAVE')].nlargest(8,'cooks_d').sort_values('cooks_d')
 emit(bars(z,'cooks_d',title,"Cook's distance",'8cm'))
 emit(r'\par\vspace{0.3cm}')
figend("The eight most influential regions in each adjusted log-size regression. Cook's distance measures OLS sensitivity, not a probability that an observation is wrong. Full leverage, residual and leave-one-out coefficient ranges are in the statistical appendix and CSV archive.")
figstart()
plots=''
for icc,g in power.groupby('assumed_icc'):
 plots+=r'\addplot+[mark=*,thick] coordinates {'+coords(g.baseline_firms,g.mde_sd)+'};\n'+r'\addlegendentry{ICC '+f'{icc:.2f}'+'}\n'
emit(axis('width=15cm,height=10cm,xlabel={Baseline firms (15 per cluster)},ylabel={Minimum detectable effect (outcome SD)},legend style={at={(0.5,-0.17)},anchor=north,legend columns=3},xtick={600,1200,1800}',plots))
figend('Illustrative power for a proposed cluster-randomized introduction intervention. Assumptions: 80 percent power, five percent two-sided test, equal assignment, 15 baseline firms per cluster, 20 percent attrition and the stated ICC. Retained cluster size is 12. No intervention was conducted; these are prospective design assumptions.')

emit(r'\chapter{Complete statistical tables}')
emit('All tables below are produced from the archived CSV files. Totals are published census tabulations; HC3 inference concerns a fitted regional model. Missing size values arise where establishment counts are zero. Rounded displays do not replace full precision in the CSV outputs.')
lt('National proprietary mining ownership and employment scale',['Owner group','Establishments','Workers','Mean size','Est. share %','Emp. share %'],[[esc(g),num(a.establishments,0),num(a.employment,0),num(a.mean_size),num(a.est_share_pct),num(a.emp_share_pct)] for g,a in m.iterrows()])
lt('Mining establishments and employment by historical state/UT region',['Historical region','Estab.','Workers','Mean size','Hired %','Density'],[[esc(a.region),num(a.est_total,0),num(a.emp_total,0),num(a.mean_size),num(a.hired_est_pct),num(a.est_per_100k)] for _,a in s.iterrows()],r'p{5.0cm}rrrrr')
lt('State demographic controls and population denominators',['Historical region','Population','SC %','ST %','Urban %','Literacy %'],[[esc(a.region),num(a.population,0),num(a.sc_pct),num(a.st_pct),num(a.urban_pct),num(a.literacy_pct)] for _,a in s.iterrows()],r'p{5.0cm}rrrrr')
lt('Maharashtra historical district mining establishments and employment',['District','Estab.','Workers','Mean size','Hired %','Density'],[[esc(a.region),num(a.est_total,0),num(a.emp_total,0),num(a.mean_size),num(a.hired_est_pct),num(a.est_per_100k)] for _,a in d.iterrows()])
lt('Maharashtra historical district demographic controls',['District','Population','SC %','ST %','Urban %','Literacy %'],[[esc(a.region),num(a.population,0),num(a.sc_pct),num(a.st_pct),num(a.urban_pct),num(a.literacy_pct)] for _,a in d.iterrows()])
names={'est_total':'Establishments','emp_total':'Workers','mean_size':'Mean size','hired_est_pct':'Hired estab. share %','est_per_100k':'Estab. per 100k','sc_pct':'SC population %','st_pct':'ST population %','urban_pct':'Urban population %','literacy_pct':'Literacy %'}
desc=pd.read_csv(D/'descriptive_statistics.csv')
for sample,title in [('states_35','State/UT regions'),('districts_MH_35','Maharashtra districts')]:
 a=desc[desc['sample'].eq(sample)]
 # Use actual sample labels if future naming changes are detected.
 if len(a)==0: a=desc[desc['sample'].str.contains('district')]
 lt(title+': descriptive moments and quartiles',['Variable','N','Missing','Mean','SD','Min','Median','Max'],[[esc(names.get(v.variable,v.variable)),str(v.n),str(v.missing)]+[num(v[x]) for x in ['mean','sd','min','median','max']] for _,v in a.iterrows()],r'p{3.5cm}rrrrrrr')
 lt(title+': distribution percentiles',['Variable','P10','P25','P50','P75','P90'],[[esc(names.get(v.variable,v.variable))]+[num(v[x]) for x in ['p10','p25','median','p75','p90']] for _,v in a.iterrows()])
emit(r'\section{Regression specifications and all coefficients}')
emit('S1: state log size, SC/ST shares only. S2: adds urban and literacy shares. S3: S2 excluding historical UTs. S4: state log(1+density), adjusted. S5: state hired-establishment share, adjusted. D1: district log size, adjusted. D2: district log(1+density), adjusted. D3: district hired-establishment share, adjusted. D4: D1 among districts with at least 50 establishments. All share regressors use ten-percentage-point units; const is the intercept.')
lt('Model sample sizes and fit',['Model','Outcome','N','R squared'],[[esc(a.model.split()[0]),esc(a.outcome),str(a.n),num(a.r2,4)] for _,a in reg.drop_duplicates('model').iterrows()],r'llrr')
lt('All fitted regression coefficients and HC3 inference',['Model','Term','Beta','HC3 SE','t-based p','CI low','CI high'],[[a.model.split()[0],esc(a.term),num(a.beta,4),num(a.se_hc3,4),num(a.p_hc3_t,4),num(a.ci_low,4),num(a.ci_high,4)] for _,a in reg.iterrows()],r'llrrrrr')
social=reg[reg.term.isin(['sc_10pp','st_10pp'])]
lt('Multiple-testing adjustments: 18 SC/ST coefficients',['Model','Term','Unadj. p','Holm p','BH q'],[[a.model.split()[0],esc(a.term),num(a.p_hc3_t,4),num(a.p_holm_18,4),num(a.q_bh_18,4)] for _,a in social.iterrows()],r'llrrr')
loo=inf[inf.region.str.startswith('LEAVE')]
lt('Leave-one-region-out coefficient ranges',['Model','Term','Minimum beta','Maximum beta'],[[a.model.split()[0],esc(a.region.replace('LEAVE_ONE_OUT_','')),num(a.loo_min,4),num(a.loo_max,4)] for _,a in loo.iterrows()],r'llrr')
tops=inf[~inf.region.str.startswith('LEAVE')].sort_values('cooks_d',ascending=False).groupby('model',sort=False).head(3).sort_values('model')
lt('Three highest-influence regions per model',['Model','Region','Cook D','Leverage','Residual'],[[a.model.split()[0],esc(a.region),num(a.cooks_d,4),num(a.leverage,4),num(a.residual,4)] for _,a in tops.iterrows()],r'lp{5cm}rrr')
lt('Complete regional influence diagnostics for all nine models',['Model','Region','Cook D','Leverage','Residual'],[[a.model.split()[0],esc(a.region),num(a.cooks_d,4),num(a.leverage,4),num(a.residual,4)] for _,a in inf[~inf.region.str.startswith('LEAVE')].iterrows()],r'lp{5cm}rrr')
fe=pd.read_csv(D/'descriptive_industry_fixed_effects.csv')
lt('Descriptive industry fixed-effect owner-group contrasts',['Weighting','Group vs Others','Log contrast','Percent contrast'],[[esc(a.model),re.search(r'\[T\.(.*?)\]',a.term)[1],num(a.beta,4),num(a.pct_contrast)] for _,a in fe.iterrows()],r'llrr')
emit('These fixed-effect contrasts summarize 92 aggregate industry by owner-group cells. They do not supply microdata sampling errors or causal firm-level effects. Establishment weighting changes the descriptive target.')
lt('Complete proprietary establishment and employment cells: 23 industries by four groups',['Industry','Group','Estab.','Workers','Mean size','vs Others'],[[esc(a.industry),esc(a.group),num(a.establishments,0),num(a.employment,0),num(a.mean_size),num(a.size_relative_others,3)] for _,a in c.iterrows()],r'p{5cm}lrrrr')
lt('Prospective trial-power assumptions and calculations',['Clusters','Baseline N','Retained N','ICC','DEFF','MDE SD','MDE log'],[[str(a.clusters),str(a.baseline_firms),str(a.retained_firms),num(a.assumed_icc),num(a.design_effect),num(a.mde_sd,3),num(a.mde_log_growth,3)] for _,a in power.iterrows()])
emit('Assumed growth standard deviation is 0.5, not measured in the acquired data. The formula uses retained cluster size 12, a t critical value with G-2 degrees of freedom and a normal 80-percent-power quantile. Actual trial planning requires pilot estimates, unequal cluster-size checks, compliance and spillover analysis.')
emit(r'\section{Complete state correlation matrix}')
cv=['est_total','emp_total','mean_size','hired_est_pct','est_per_100k','sc_pct','st_pct','urban_pct','literacy_pct']
cl=['Est.','Workers','Size','Hired','Density','SC','ST','Urban','Literacy']
cm=s[cv].corr()
lt('State Pearson correlations: all nine analytical variables',['Variable']+cl,[[esc(cl[i])]+[num(cm.loc[v,w]) for w in cv] for i,v in enumerate(cv)])
emit('Correlations use pairwise-complete observations. Hired is the percentage of establishments with hired workers. Pairs involving size or hired share have 33 observations; other pairs have 35. These are geographic associations.')

exec((R/'scripts/report_workers.py').read_text(encoding='utf-8'))

emit(r'\chapter{Full draft fieldwork questionnaire}')
emit('The following 86 measures are a proposed instrument to pilot, translate and revise before any fieldwork. No responses were collected. Consent, private identifier handling and unknown/declined categories are mandatory parts of the protocol. Repeated outcome definitions and relationship event dates are needed to study growth and temporal order.')
q=pd.read_csv(R/'docs/fieldwork_questionnaire.csv')
lt('Draft questionnaire measures and coding instructions',['Module','ID','Question or measure','Coding instruction'],[[esc(a.module),esc(a.question_id),esc(a.question_or_measure),esc(a.coding_and_instruction)] for _,a in q.iterrows()],r'p{1.8cm}lp{7.5cm}p{4.5cm}')

emit(r'\chapter{Source inventory and acquisition priorities}')
emit('The 65 entries are source documents, systems and source families. S02, S07, S09 and S56-S62 supply executed quantitative analysis or selected published empirical summaries. S63 provides acquired survey documentation; other entries are metadata, verified public documentation, conditional or licensed records, candidate families or data still to be collected. Source status is assessed for my research on 11 October 2026; access may change. A URL does not guarantee downloadable microdata.')
for a in sources:
 emit(r'\section{'+esc(a['id']+': '+a['name'])+'}'+r'\hypertarget{'+a['id']+'}{}')
 for key,lab in [('url','Source link'),('access','Access status'),('unit','Unit and coverage'),('social','Caste or relationship information'),('growth','Growth information'),('use','Research use and limitations')]:
  emit(r'\textbf{'+lab+':} '+prose(a[key])+'\n')
emit(r'\chapter{Input provenance and verification record}')
emit('The raw files in the archive are retained with their original institutional authorship. The Ecensus-hosted national PDF is a third-party acquisition route; it is not a new statistical producer. Redistributed public reports and workbook remain subject to their original terms. Code and original report prose have separate licensing.')
logs=json.loads((R/'provenance/empirical_download_log.json').read_text())
emit(r'\section{Downloaded input hashes}')
for filename in ['ec6_report.pdf','maharashtra_ec6.pdf','pca_2011.xlsx']:
 import hashlib
 raw=R/'data/raw'/filename;sha=hashlib.sha256(raw.read_bytes()).hexdigest()
 emit(r'\textbf{'+esc(filename)+r'}: '+num(raw.stat().st_size,0)+' bytes.\\')
 emit(r'\texttt{'+sha[:32]+r'}\\\texttt{'+sha[32:]+'}\n')
emit(r'\section{Additional acquired worker inputs}')
workerlogs=json.loads((R/'provenance/worker_input_manifest.json').read_text(encoding='utf-8'))
for a in workerlogs:
 emit(r'\textbf{'+esc(a['file'])+'}: '+num(a['bytes'],0)+' bytes. '+prose(a['url'])+r'\\')
 emit(r'\texttt{'+a['sha256'][:32]+r'}\\\texttt{'+a['sha256'][32:]+'}\n')
 emit(prose(a['role'])+'\n')
emit('Worker checks additionally reconcile sexes, residence, group residuals and every historical state sum to India. The four weighted models are reproduced from 1,275 observed nonempty cells. Local-study percentages remain published margins; no recruitment-by-caste joint distribution is invented. The ILO rounded 99-percent total and the conflicting Arisa advance percentage are explicitly retained.')
emit(r'\section{Meaningful checks performed}')
emit('Extraction checks verify own-account plus hired-worker establishments equals all establishments, and rural plus urban equals combined totals for every region and column. National mining sums are 85,176 establishments and 557,474 workers; Maharashtra sums are 6,229 and 29,527. Proprietary owner-group sums are 73,170 and 319,425. Join cardinality is enforced, Maharashtra names are compared, residual AP/Telangana counts are pooled, and zero denominators are retained as missing size rather than invented observations. Source hashes, exact coefficients, all figures and archive integrity are checked. Model uncertainty and unavailable causal data remain substantive limitations.')
emit(r'\section{Reporting conventions}')
emit('Data vintages include 2011, EC6 2013--14, ILO 2021, Arisa/CLRA 2024 and Coal India snapshots 2024/2026; source entries state the exact dates. Historical series are not automatically comparable.  Broad industry code 05 in the EC tables means Mining and quarrying; it is not NIC division 05 alone. Establishment is the observed EC unit; enterprise, company, mine, lease and household are different units. Population shares are geographic context. Others is residual. Every proposed design and hypothetical power parameter is marked as such. Reproducibility is the ability to regenerate the observed-data outputs, not proof that causal identification is valid.')
emit(r'\end{document}')
path=O/'caste_ties_and_mining_growth_india.tex'
path.write_text('\n'.join(out),encoding='utf-8')
pd.DataFrame(sources).to_csv(D/'source_catalogue.csv',index=False)
print(json.dumps({'tex':'report/'+path.name,'bytes':path.stat().st_size,'n_captions':sum('\\caption{' in x for x in out),'n_sources':len(sources),'narrative_words':len(md.split())}))
