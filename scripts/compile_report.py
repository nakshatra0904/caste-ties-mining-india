"""Compile the report locally with Tectonic or PDFLaTeX."""
from pathlib import Path
import argparse,shutil,subprocess
R=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--engine-path',help='Optional path to a locally installed tectonic or pdflatex executable')
args=parser.parse_args()
engine=args.engine_path or shutil.which('tectonic') or shutil.which('pdflatex')
if not engine:raise SystemExit('Install a local Tectonic or TeX Live/MiKTeX compiler, or supply --engine-path.')
source=R/'report/caste_ties_and_mining_growth_india.tex';out=source.parent
if 'tectonic' in Path(engine).name.lower():
 subprocess.run([engine,'--untrusted','--reruns','2','--outdir',str(out),str(source)],check=True,cwd=R)
else:
 for _ in range(3):subprocess.run([engine,'-interaction=nonstopmode','-halt-on-error','-output-directory='+str(out),str(source)],check=True,cwd=R)
assert source.with_suffix('.pdf').is_file()
print('PDF written to report/'+source.with_suffix('.pdf').name)
