"""Offline reproduction with input hash checks, analysis, plots and report source."""
from pathlib import Path
import hashlib,json,subprocess,sys
R=Path(__file__).resolve().parents[1]
for e in json.loads((R/'provenance/empirical_download_log.json').read_text()):
    if e['status']=='downloaded':
        p=R/'data/raw'/e['file']
        if hashlib.sha256(p.read_bytes()).hexdigest()!=e['sha256']:
            raise RuntimeError('Input hash mismatch: '+e['file'])
for e in json.loads((R/'provenance/worker_input_manifest.json').read_text()):
    if e['bundled']:
        p=R/'data/raw/workers'/e['file']
        if hashlib.sha256(p.read_bytes()).hexdigest()!=e['sha256']:
            raise RuntimeError('Worker input hash mismatch: '+e['file'])
for script in ['analyze.py','more_figures.py','analyze_workers.py','build_report.py']:
    subprocess.run([sys.executable,str(R/'scripts'/script)],check=True,cwd=R)
print('Reproduced aggregate analysis and LaTeX source. PDF compilation is a separate step.')
