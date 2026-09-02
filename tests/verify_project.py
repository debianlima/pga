from pathlib import Path
import json, yaml, jsonschema, subprocess
r=Path(__file__).resolve().parents[1]
req=['README.md','VERSION','manifesto.yaml','competencias.yaml','estado.md','lexico.yaml','skills/pga/SKILL.md','docs/U-PGA-01-msgcd-u20-handoff.md','contratos/pga-1.0/release.schema.json','dados/pga-1.0/U-PGA-02-release-evidence.yaml','docs/U-PGA-02-release-1.0.md','tests/verify_release_1_0.py']
assert all((r/x).exists() for x in req)
assert len(list(r.glob('skills/*/SKILL.md')))==1
assert (r/'VERSION').read_text().strip()=='1.0.0'
m=yaml.safe_load((r/'manifesto.yaml').read_text(encoding='utf-8'))
assert m['versao_contrato']==3 and m['release_alvo']=='v1.0.0'
assert m['estado_release']=='homologated'
entries=m['entradas']
ids=[x['id'] for x in entries]; paths=[x['caminho'] for x in entries]
assert len(ids)==len(set(ids)) and len(paths)==len(set(paths))
tracked=set(subprocess.check_output(['git','-C',str(r),'ls-files'], text=True).splitlines())
assert tracked==set(paths), f'namespace divergence tracked_only={sorted(tracked-set(paths))} declared_only={sorted(set(paths)-tracked)}'
telemetry=r/'dados/telemetria-unidades.jsonl'
events=[json.loads(line) for line in telemetry.read_text(encoding='utf-8').splitlines() if line.strip()]
by_unit={}
for event in events:
    by_unit.setdefault(event['unidade'], []).append(event['evento'])
active=(m.get('trabalho_compartilhado') or {}).get('unidade')
for unit, values in by_unit.items():
    expected=['telemetria_inicio'] if unit==active else ['telemetria_inicio','telemetria_fim']
    assert sorted(values)==sorted(expected), {unit: values, 'active': active}
state=(r/'estado.md').read_text(encoding='utf-8')
assert 'EM_CURSO' not in state and '`pga-project@0.4.0`' in state and '- 1–33.' in state
a=m['auxiliar_construcao_conciliacao']
assert a['habilitado'] is True
assert a['natureza']=='politica_operacional_pos_release' and a['preserva_release_v1_0_0'] is True
assert a['papel']=='auxiliar' and a['ordem']==2 and a['protocolo']=='PGA'
assert a['participa_em']==['construcao','conciliacao_incremental']
dep=a['dependencia_previa']
assert dep['protocolo']=='PGD' and dep['gate']=='PGD_AUXILIAR_RECONCILIATION=PASS'
assert dep['head']=='366388d8c52f696d81b7277075b87e8fc144ca1b'
assert dep['gate_identidade']=='PGD_IDENTITY_H01_R2=PASS'
assert dep['repositorio_protocolo']=='debianlima/pgd'
assert dep['repositorio_implementacao_canonica']=='debianlima/pgh-distributed-session-control-plane'
assert a['gate_saida']=='PGA_AUXILIAR_RECONCILIATION=PASS'
assert 'nao_substitui_decisao_humana' in a['limites'] and 'nao_faz_mutacao_normativa_silenciosa' in a['limites']
t=(r/'docs/U-PGA-01-msgcd-u20-handoff.md').read_text(encoding='utf-8')
assert 'Protocolo de Autogovernança' in t
s=json.loads((r/'contratos/pga-1.0/release.schema.json').read_text(encoding='utf-8'))
e=yaml.safe_load((r/'dados/pga-1.0/U-PGA-02-release-evidence.yaml').read_text(encoding='utf-8'))
jsonschema.validate(e,s)
print('PGA_PROJECT_VERIFY=PASS VERSION=1.0.0')
