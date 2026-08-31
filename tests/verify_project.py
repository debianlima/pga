from pathlib import Path
import json, yaml, jsonschema
r=Path(__file__).resolve().parents[1]
req=['README.md','VERSION','manifesto.yaml','competencias.yaml','estado.md','lexico.yaml','skills/pga/SKILL.md','docs/U-PGA-01-msgcd-u20-handoff.md','contratos/pga-1.0/release.schema.json','dados/pga-1.0/U-PGA-02-release-evidence.yaml','docs/U-PGA-02-release-1.0.md','tests/verify_release_1_0.py']
assert all((r/x).exists() for x in req)
assert len(list(r.glob('skills/*/SKILL.md')))==1
assert (r/'VERSION').read_text().strip()=='1.0.0'
m=yaml.safe_load((r/'manifesto.yaml').read_text(encoding='utf-8'))
assert m['versao_contrato']==2 and m['release_alvo']=='v1.0.0'
t=(r/'docs/U-PGA-01-msgcd-u20-handoff.md').read_text(encoding='utf-8')
assert 'Protocolo de Autogovernança' in t
s=json.loads((r/'contratos/pga-1.0/release.schema.json').read_text(encoding='utf-8'))
e=yaml.safe_load((r/'dados/pga-1.0/U-PGA-02-release-evidence.yaml').read_text(encoding='utf-8'))
jsonschema.validate(e,s)
print('PGA_PROJECT_VERIFY=PASS VERSION=1.0.0')
