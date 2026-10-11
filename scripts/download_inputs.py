"""Optional download of the three exact public inputs. Offline copies are bundled."""
from pathlib import Path
import urllib.request,json,hashlib
R=Path(__file__).resolve().parents[1]
entries=json.loads((R/'provenance/empirical_download_log.json').read_text())
for e in entries:
    if e['status']!='downloaded':continue
    target=R/'data/raw'/e['file']
    if target.exists() and hashlib.sha256(target.read_bytes()).hexdigest()==e['sha256']:
        print('Verified existing input:',e['file']);continue
    req=urllib.request.Request(e['url'],headers={'User-Agent':'Public academic research'})
    with urllib.request.urlopen(req,timeout=60) as response:payload=response.read()
    if hashlib.sha256(payload).hexdigest()!=e['sha256']:
        raise RuntimeError('Source bytes changed; preserve original and investigate before replacement: '+e['file'])
    target.write_bytes(payload)
    print('Downloaded and hash-verified:',e['file'])
