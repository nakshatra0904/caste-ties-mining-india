"""Report extension executed in build_report's table/plot namespace."""
wn=pd.read_csv(D/'worker_national_composition2011.csv').set_index('group').reindex(['SC','ST','Remaining'])
wd=pd.read_csv(D/'worker_division_composition2011.csv',dtype={'division':str})
ws=pd.read_csv(D/'worker_state_composition2011.csv',dtype={'state_code':str})
wx=pd.read_csv(D/'worker_sex_duration2011.csv')
wc=pd.read_csv(D/'worker_controlled_contrasts2011.csv')
wm=pd.read_csv(D/'worker_model_specs2011.csv')
coal=pd.read_csv(D/'coal_india_workforce_composition.csv')
ct=pd.read_csv(D/'coal_india_snapshot_totals.csv')
routes=pd.read_csv(D/'makrana_recruitment_routes.csv')
duration=pd.read_csv(D/'ilo_stone_working_year.csv')
emit(r'\chapter{Additional worker composition and recruitment graphs}')
emit('All seven worker graphs use observed published cells or fitted aggregate models. Remaining means All minus SC minus ST in Census graphs, but total minus SC minus ST minus OBC in Coal India graphs; their definitions are source-specific. No individual observations were reconstructed. PNG counterparts are in the archive.')
figstart()
plots=''
for g,col in [('SC','navy'),('ST','orange!70!black'),('Remaining','muted')]:
 z=wd[wd.group.eq(g)].sort_values('division')
 plots+=r'\addplot[fill='+col+',draw=white] coordinates {'+coords(range(5),z.share_pct)+'};\n'+r'\addlegendentry{'+g+'}\n'
emit(axis('width=15cm,height=11cm,ybar stacked,bar width=30pt,ymin=0,ymax=100,xtick={0,1,2,3,4},xticklabels={Coal/lignite,Oil/gas,Metal ores,Other/quarrying,Support},ylabel={Worker share (percent)},xlabel={NIC 2008 division},legend style={at={(0.5,-0.15)},anchor=north,legend columns=3},tick label style={font=\small}',plots))
figend('National SC/ST mining worker composition, main plus marginal, by NIC divisions 05-09. Source: Census 2011 B18, B18SC and B18ST. Remaining contains OBC and other workers. This directly classifies worker identity, unlike EC employment classified by owner identity.')
figstart()
for gender in ['Male','Female']:
 z=wx[wx.sex.eq(gender)].set_index('group').reindex(['SC','ST','Remaining'])
 emit(axis('width=15cm,height=7cm,ybar,bar width=25pt,xtick={0,1,2},xticklabels={SC,ST,Remaining},ymin=0,ymax=40,ylabel={Marginal-worker share (percent)},title={'+gender+'}',r'\addplot[navy,fill=navy] coordinates {'+coords(range(3),z.marginal_pct)+'};'))
 emit(r'\par\vspace{0.4cm}')
figend('Sex-specific marginal-worker shares across NIC 05-09, Census 2011. Marginal denotes work for less than six months during the preceding reference year. It is not a measure of contractor employment, informality or a particular occupation.')
figstart()
plots=r'\addplot[gray,dashed,mark=none] coordinates {(0,-0.5)(0,3.5)};'
for g,col,off in [('SC','navy',-.10),('ST','orange!70!black',.10)]:
 z=wc[wc.term.eq('C(group)[T.'+g+']')]
 co=' '.join(f'({a.beta_pp:.7g},{i+off}) +- ({(a.ci_high-a.ci_low)/2:.7g},0)' for i,(_,a) in enumerate(z.iterrows()))
 plots+=r'\addplot+[only marks,mark=*,color='+col+r',error bars/.cd,x dir=both,x explicit] coordinates {'+co+'};\n'+r'\addlegendentry{'+g+'}\n'
emit(axis('width=15cm,height=11cm,ytick={0,1,2,3},yticklabels={W1 group only,W2 sex + residence,W3 + state + division,W4 joint strata},yticklabel style={text width=4cm,align=right},y dir=reverse,xlabel={Contrast vs Remaining (percentage points)},legend style={at={(0.5,-0.15)},anchor=north,legend columns=2},tick label style={font=\small}',plots))
figend('Observed aggregate duration differences before and after controls. Employment-weighted WLS on 1,275 cells. W4 absorbs state-by-division-by-sex-by-residence strata. Intervals cluster at 35 historical states and are model-based, not Census enumeration errors or causal caste effects. Missing age, education and occupation controls remain relevant.')
figstart()
for snapshot in ['2024-01-01','2026-01-01']:
 plots=''
 for g,col in [('SC','navy'),('ST','orange!70!black'),('OBC','green!45!black'),('Remaining','muted')]:
  z=coal[coal.snapshot.eq(snapshot)&coal.group.eq(g)].sort_values('employment_group')
  plots+=r'\addplot[fill='+col+',draw=white] coordinates {'+coords(range(4),z.share_pct)+'};\n'+r'\addlegendentry{'+g+'}\n'
 emit(axis('width=15cm,height=8cm,ybar stacked,bar width=30pt,ymin=0,ymax=100,xtick={0,1,2,3},xticklabels={A,B,C,D},ylabel={Share of disclosed employees (percent)},title={'+snapshot+'},xlabel={Employment group},legend style={at={(0.5,-0.2)},anchor=north,legend columns=4}',plots))
 emit(r'\par\vspace{1cm}')
figend('Coal India corporate employee composition by administrative employment group. Source: Coal Ministry annual reports 2023-24 and 2025-26, chapter 16, PDF pages 5 and 4. The 2026 residual contains EWS employees. Snapshots do not identify recruitment probabilities or the reasons for changes in employee stocks.')
figstart()
emit(axis('width=15cm,height=9cm,xbar,xmin=0,xmax=100,ytick={0,1,2},yticklabels={Relatives/co-workers,Approached employer,Contractor},yticklabel style={text width=4cm,align=right},y dir=reverse,xlabel={Percent of 50 interviewed workers},bar width=20pt,tick label style={font=\small}',r'\addplot[fill=navy,draw=navy] coordinates {'+coords(routes.share_pct,range(3))+'};'))
figend('Reported Makrana job-entry routes, Arisa/CLRA 2024, PDF page 29. Published counts are seven direct approaches and three contractor recruits; 40 referral entrants are derived from the published 80 percent of N=50. This is a local supply-chain sample and referrals do not establish shared-caste relationships.')
figstart()
z=ws[ws.group.isin(['SC','ST'])].pivot(index='region',columns='group',values='share_pct');z['combined']=z.SC+z.ST;z=z.nlargest(15,'combined').sort_values('combined')
plots=''
for g,col in [('SC','navy'),('ST','orange!70!black')]:plots+=r'\addplot[fill='+col+',draw=white] coordinates {'+coords(z[g],range(len(z)))+'};\n'+r'\addlegendentry{'+g+'}\n'
emit(axis('width=15cm,height=15cm,xbar stacked,xmin=0,xmax=100,ytick={'+','.join(map(str,range(len(z))))+'},yticklabels={'+','.join('{'+esc(i)+'}' for i in z.index)+'},tick label style={font=\scriptsize},xlabel={Share of workers in NIC 05-09 (percent)},bar width=8pt,legend style={at={(0.5,-0.12)},anchor=north,legend columns=2}',plots))
figend('Fifteen highest SC plus ST worker shares, Census 2011 historical state/UT geography. Some regions have very small workforces; the full count table should accompany comparisons. These are workforce composition shares, not mining participation rates among the regional SC/ST population.')
figstart()
plots=''
for g,col in [('Male','navy'),('Female','orange!70!black')]:
 z=duration[duration.sex.eq(g)].set_index('stage').loc[['Mines','Processing']]
 plots+=r'\addplot[fill='+col+',draw='+col+'] coordinates {'+coords(range(2),z.months_per_year)+'};\n'+r'\addlegendentry{'+g+'}\n'
emit(axis('width=15cm,height=10cm,ybar,bar width=25pt,ymin=0,ymax=12,xtick={0,1},xticklabels={Mines,Processing},ylabel={Reported average months worked per year},legend style={at={(0.5,-0.15)},anchor=north,legend columns=2}',plots))
figend('Published local working-year averages by sex and stone supply-chain stage. ILO Rajasthan study 2021, PDF page 59. These unadjusted averages do not control for occupation, caste or worker characteristics and should not be read as a causal gender effect.')

emit(r'\chapter{Worker statistics and controlled-result tables}')
emit('All national and state values are derived from actual B18 cells. Census categories and company reservation classifications are kept separate. Model coefficients use percentage points. Full-precision values, source coordinates and all fitted coefficients are archived in CSV files.')
lt('Census 2011 national mining workforce, NIC 05-09',['Group','Main','Marginal','All workers','Worker %','Marginal %'],[[esc(g),num(a.main,0),num(a.marginal,0),num(a.total,0),num(a.share_pct),num(a.marginal_pct)] for g,a in wn.iterrows()])
lt('National workforce composition by mining division',['NIC','Division','Group','Workers','Worker %','Marginal %'],[[esc(a.division),esc(a.industry),esc(a.group),num(a.total,0),num(a.share_pct),num(a.marginal_pct)] for _,a in wd.iterrows()],r'lp{4.5cm}lrrr')
ss=ws.pivot(index=['state_code','region'],columns='group',values=['total','marginal','share_pct'])
sr=[]
for (code,region),a in ss.iterrows():
 total=sum(a['total']);marg=sum(a['marginal']);sr.append([esc(region),num(total,0),num(a['total']['SC'],0),num(a['total']['ST'],0),num(a['share_pct']['SC']),num(a['share_pct']['ST']),num(100*marg/total) if total else '--'])
lt('All 35 historical regions: workforce counts and social composition',['Region','Workers','SC count','ST count','SC %','ST %','Marg. %'],sr,r'p{4cm}rrrrrr')
lt('National worker sex and duration cells',['Sex','Group','Main','Marginal','Workers','Marginal %'],[[esc(a.sex),esc(a.group),num(a.main,0),num(a.marginal,0),num(a.total,0),num(a.marginal_pct)] for _,a in wx.iterrows()])
lt('Worker-cell specifications: weighting and control sets',['Model','Controls','Cells','States','Weight sum','Rank','R sq.'],[[a.model,esc(a.controls),str(a.n_cells),str(a.n_states),num(a.weight_total,0),str(a['rank']),num(a.r2,4)] for _,a in wm.iterrows()],r'lp{5cm}rrrrr')
lt('Unadjusted and controlled SC/ST duration contrasts versus Remaining',['Model','Group','Beta pp','Cluster SE','95% low','95% high','Model p'],[[a.model,'SC' if 'SC' in a.term else 'ST',num(a.beta_pp,3),num(a.se_cluster_state,3),num(a.ci_low,3),num(a.ci_high,3),num(a.p_model_based,4)] for _,a in wc.iterrows()])
emit('W1 group-only; W2 sex/residence; W3 additionally state and division effects; W4 joint state-division-sex-residence strata. All models have 1,275 nonempty aggregate cells and 35 state clusters. Point estimates describe the acquired cells; p-values are exploratory model summaries. They are not part of the earlier 18-coefficient EC multiple-testing family and are not used for a causal claim.')
ac=pd.read_csv(D/'worker_regression_all_coefficients2011.csv');ac=ac[ac.model.ne('W4')]
lt('All coefficients including controls in W1-W3',['Model','Term','Beta pp','Cluster SE','95% low','95% high'],[[a.model,esc(a.term),num(a.beta_pp,3),num(a.se_cluster_state,3),num(a.ci_low,3),num(a.ci_high,3)] for _,a in ac.iterrows()],r'lp{6cm}rrrr')
emit(r'W4 includes 550 observed context strata and two group indicators (rank 552). Its focal contrasts are above; every stratum coefficient is in \path{worker_regression_all_coefficients2011.csv}. Small cells and many absorbed terms warrant caution with the finite-sample covariance correction. Omitted reference levels are Remaining, Female, Rural, and the first observed state/division/stratum as applicable.')
lt('Coal India employee counts and shares by snapshot and employment group',['Date','Pay group','Social group','Count','Total','Share %'],[[esc(a.snapshot),esc(a.employment_group),esc(a.group),num(a['count'],0),num(a.total,0),num(a.share_pct)] for _,a in coal.iterrows()])
lt('Coal India full snapshot totals',['Date','Group','Count','Total','Share %'],[[esc(a.snapshot),esc(a.group),num(a['count'],0),num(a.total,0),num(a.share_pct)] for _,a in ct.iterrows()])
rv=pd.read_csv(D/'secl_vacancy_filling2024_25.csv')
lt('SECL Mining Sirdar disclosed FY2024-25 vacancy filling',['Vacancy category','Advertised','Filled','Unfilled','Fill %'],[[esc(a.vacancy_category),str(a.advertised),str(a.filled),str(a.unfilled),num(a.fill_pct)] for _,a in rv.iterrows()])
emit('Source: Coal Ministry annual report 2025-26, chapter 16, PDF page 7. Counts sum to 350 advertised and 345 filled; ST non-joining is reported. No applicant denominator is disclosed here. UR and EWS are vacancy classifications, not caste identities.')
lc=pd.read_csv(D/'rajasthan_stone_worker_composition.csv')
lt('Published Arisa/CLRA local stone-worker composition',['Site','Group','Published %','PDF page','Denominator note'],[[esc(a.site),esc(a.group),num(a.published_pct,0),str(a.pdf_page),esc(a.denominator_note)] for _,a in lc.iterrows()],r'llrrp{7cm}')
il=pd.read_csv(D/'ilo_stone_worker_composition2021.csv')
lt('ILO 2021 two-cluster stone-worker composition',['Group','Published %','Sample N','PDF page'],[[esc(a.group),num(a.published_pct,0),str(a.n),str(a.pdf_page)] for _,a in il.iterrows()])
emit('ILO percentages sum to 99 through publication rounding; they are not normalized and no individual group counts are reconstructed. Different local samples and vintages are never pooled into one representative survey.')
lt('Makrana recruitment routes: individual-interview sample N=50',['Route','Count','Share %','Count provenance'],[[esc(a.route),str(a['count']),num(a.share_pct,0),esc(a.count_status)] for _,a in routes.iterrows()],r'p{4cm}rrp{7cm}')
pf=pd.read_csv(D/'stone_worker_other_details.csv')
lt('Other published stone-worker details with original denominators',['Sample','Indicator','Count','Base','Percent','PDF page'],[[esc(a['sample']),esc(a.indicator),num(a.numerator,0),num(a.denominator,0),num(a.pct),str(a.pdf_page)] for _,a in pf.iterrows()],r'p{3.6cm}p{5cm}rrrr')
emit('A blank count means a published percentage rather than an observed integer count. ILO PF percentages use separate mine/processing subgroups, whose counts are not reconstructed from N=115. Any PPE use is not adequate exposure protection. The Makrana advance paragraph gives 18/50 = 36 percent; the concluding 38-percent figure conflicts and is preserved in the CSV measurement note.')
lt('ILO published average working year',['Stage','Sex','Months/year','PDF page'],[[esc(a.stage),esc(a.sex),num(a.months_per_year,1),'59'] for _,a in duration.iterrows()])
