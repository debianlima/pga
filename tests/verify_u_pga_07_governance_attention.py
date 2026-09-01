#!/usr/bin/env python3
from pathlib import Path
import json
import yaml
import jsonschema

ROOT=Path(__file__).resolve().parents[1]
SCHEMA=ROOT/'contratos/pga-1.0/governance-attention.schema.json'
DATA=ROOT/'dados/pga-1.0/U-PGA-07-governance-attention.yaml'
DOC=ROOT/'docs/U-PGA-07-governance-attention.md'
SOURCE_COMMIT='f5047f72914c6634982df30c8ce0f8747af5cfb3'
SOURCE_PATH='config/3.0/governance-decisions.yaml'
SOURCE_SHA256='cc79afcd94345752c0e0b5cf9883c48a5956f09a91bcde990fccb941f4ff903b'
EXPECTED_IDS=[
 'Q1-WORK34-KEY-AUTH','Q2-DESKTOP-ARCH','Q3-NETWORK-SHARING-DEFAULT',
 'Q4-H09-PROVENANCE','Q5-T069-MITIGATION','Q6-OTEL-SIGNOZ-PROJECT-SKILLS',
 'Q7-ATU-PHYSICAL-PROMOTION']

def fail(reason):
    print('PGA_GOVERNANCE_ATTENTION_U07=FAIL',reason)
    raise SystemExit(2)

def main():
    for p in (SCHEMA,DATA,DOC):
        if not p.exists(): fail('missing:'+str(p.relative_to(ROOT)))
    schema=json.loads(SCHEMA.read_text(encoding='utf-8'))
    data=yaml.safe_load(DATA.read_text(encoding='utf-8'))
    jsonschema.validate(data,schema)
    if data.get('unit')!='U-PGA-07-GOVERNANCE-ATTENTION-PROJECTION': fail('unit')
    src=data.get('source') or {}
    if src.get('repository')!='debianlima/pgh-distributed-session-control-plane': fail('source-repo')
    if src.get('commit')!=SOURCE_COMMIT or src.get('path')!=SOURCE_PATH or src.get('sha256')!=SOURCE_SHA256: fail('source-pin')
    if src.get('schema')!='pgh-governance-human-decisions/1': fail('source-schema')
    queue=data.get('human_attention_queue') or []
    if queue: fail('resolved-decisions-must-not-remain-in-human-queue')
    resolved=data.get('resolved_decisions') or []
    if [x.get('decision_id') for x in resolved] != EXPECTED_IDS: fail('resolved-id-order')
    allowed_status={'RESOLVED','RESOLVED_PROVENANCE'}
    if any(x.get('source_status') not in allowed_status for x in resolved): fail('source-status')
    if any(x.get('queue_disposition')!='REMOVED_RESOLVED' for x in resolved): fail('queue-disposition')
    if any(x.get('authority')!='human-operator' for x in resolved): fail('authority-preserved')
    follow=data.get('technical_followups') or []
    if [x.get('decision_id') for x in follow] != EXPECTED_IDS: fail('followup-coverage')
    if len({x.get('follow_up_id') for x in follow}) != 7: fail('followup-unique')
    if any(x.get('human_decision_required') is not False for x in follow): fail('resolved-followup-requeued-human')
    if any(not x.get('action') or not x.get('evidence_refs') for x in follow): fail('followup-auditability')
    model=data.get('governance_attention_model') or {}
    req=set(model.get('required_fields') or [])
    expected={'decision_id','project_ref','task_ref','evidence_refs','category','options','impact','reversibility','dependencies','deadline','required_authority','actions'}
    if req != expected: fail('attention-model-fields')
    if model.get('allowed_actions') != ['more_info','approve','reject','modify']: fail('attention-actions')
    if model.get('repository_divergence_creates_attention_item') is not True: fail('reconciliation-attention')
    boundary=data.get('authority_boundary') or {}
    for k in ('creates_scheduler','creates_worker','creates_lease','creates_runtime_state','creates_grant','changes_human_decision'):
        if boundary.get(k) is not False: fail('authority-boundary:'+k)
    if boundary.get('PGA')!='policy_authority_priority_gates_governed_evolution': fail('pga-boundary')
    gates=data.get('gates') or {}
    required=['DELTA_INVENTORY','LEARNING_PRESERVED','SOURCE_PIN','ATTENTION_SCHEMA','RESOLVED_QUEUE_DRAIN','FOLLOWUP_COVERAGE','AUTHORITY_BOUNDARY','NO_PGA_RUNTIME','RELEASE_IMMUTABILITY','RECONCILIATION_CLOSURE','DEPENDENCY_REFERENCES']
    # pre-closure artifacts may mark only final closure gates PENDING; all others must PASS.
    for k in required[:-2]:
        if gates.get(k)!='PASS': fail('gate:'+k)
    if gates.get('RECONCILIATION_CLOSURE') not in ('PENDING','PASS'): fail('gate:RECONCILIATION_CLOSURE')
    if gates.get('DEPENDENCY_REFERENCES') not in ('PENDING','PASS'): fail('gate:DEPENDENCY_REFERENCES')
    if (ROOT/'VERSION').read_text().strip()!='1.0.0': fail('release-version')
    text=DOC.read_text(encoding='utf-8')
    for marker in ('GovernanceAttentionItem','Q1–Q7','REMOVED_RESOLVED','follow-up técnico','não cria scheduler','v1.0.0'):
        if marker not in text: fail('doc:'+marker)
    print('PGA_GOVERNANCE_ATTENTION_U07=PASS QUEUE=0 RESOLVED=7 FOLLOWUPS=7 NO_PGA_RUNTIME=PASS')

if __name__=='__main__': main()
