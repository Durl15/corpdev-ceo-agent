import os

os.makedirs('C:/Projects/CorpDevCEOAgent/static', exist_ok=True)

content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CorpDev CEO Agent</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@300;400;500;600;700&display=swap');
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{--bg:#f4f6f9;--surface:#fff;--card:#fff;--border:#e2e8f0;--border-bright:#cbd5e1;--accent:#d97706;--accent-dim:#fef3c7;--green:#059669;--red:#dc2626;--text:#1e293b;--text-dim:#94a3b8;--text-mid:#475569;--mono:'IBM Plex Mono',monospace;--sans:'IBM Plex Sans',sans-serif}
body{background:var(--bg);font-family:var(--sans);color:var(--text);min-height:100vh}
.header{background:var(--surface);border-bottom:1px solid var(--border);padding:16px 24px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:100;box-shadow:0 1px 4px rgba(0,0,0,.05)}
.brand{display:flex;align-items:center;gap:12px}
.brand-icon{width:36px;height:36px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;font-family:var(--mono);font-weight:700;font-size:13px;color:#fff}
.brand-name{font-size:13px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;line-height:1}
.brand-sub{font-family:var(--mono);font-size:10px;color:var(--accent);margin-top:2px;letter-spacing:.08em}
.header-right{display:flex;align-items:center;gap:10px}
.status-dot{width:8px;height:8px;border-radius:50%;background:var(--green);box-shadow:0 0 6px var(--green);animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}
.status-label{font-family:var(--mono);font-size:10px;color:var(--green);text-transform:uppercase;letter-spacing:.1em}
.main{display:grid;grid-template-columns:330px 1fr;height:calc(100vh - 61px)}
.left-panel{background:var(--surface);border-right:1px solid var(--border);display:flex;flex-direction:column;overflow:hidden}
.panel-header{padding:16px 20px;border-bottom:1px solid var(--border)}
.panel-title{font-family:var(--mono);font-size:10px;text-transform:uppercase;letter-spacing:.12em;color:var(--text-dim);margin-bottom:12px}
.mode-toggle{display:flex;background:var(--bg);border:1px solid var(--border);border-radius:8px;padding:3px;margin-bottom:12px}
.mode-btn{flex:1;padding:7px 10px;border:none;background:none;color:var(--text-mid);font-family:var(--mono);font-size:11px;cursor:pointer;border-radius:6px;transition:all .2s}
.mode-btn.active{background:var(--accent);color:#fff;font-weight:600}
.search-box{position:relative}
.search-input{width:100%;background:var(--bg);border:1px solid var(--border);border-radius:8px;padding:11px 44px 11px 14px;color:var(--text);font-family:var(--sans);font-size:14px;outline:none;transition:border-color .2s}
.search-input:focus{border-color:var(--accent);background:#fff}
.search-input::placeholder{color:var(--text-dim)}
.search-btn{position:absolute;right:8px;top:50%;transform:translateY(-50%);background:var(--accent);border:none;border-radius:6px;width:30px;height:30px;display:flex;align-items:center;justify-content:center;cursor:pointer;color:#fff;transition:all .2s}
.search-btn:hover{background:#b45309}
.search-btn:disabled{opacity:.4;cursor:not-allowed}
.filters{padding:12px 20px;border-bottom:1px solid var(--border);display:flex;flex-direction:column;gap:8px}
.filter-label{font-family:var(--mono);font-size:10px;text-transform:uppercase;letter-spacing:.1em;color:var(--text-dim)}
.filter-chips{display:flex;flex-wrap:wrap;gap:6px}
.chip{padding:4px 10px;border-radius:20px;border:1px solid var(--border);background:none;color:var(--text-dim);font-family:var(--mono);font-size:10px;cursor:pointer;transition:all .15s}
.chip.active{border-color:var(--accent);color:var(--accent);background:var(--accent-dim)}
.history-section{flex:1;overflow-y:auto;padding:12px 0}
.history-section::-webkit-scrollbar{width:4px}
.history-section::-webkit-scrollbar-thumb{background:var(--border);border-radius:2px}
.section-label{font-family:var(--mono);font-size:9px;text-transform:uppercase;letter-spacing:.12em;color:var(--text-dim);padding:0 20px 8px}
.history-item{padding:10px 20px;cursor:pointer;transition:background .15s;border-left:2px solid transparent}
.history-item:hover{background:var(--bg);border-left-color:var(--border-bright)}
.history-item.active{background:var(--accent-dim);border-left-color:var(--accent)}
.h-company{font-size:13px;font-weight:500;margin-bottom:3px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.h-meta{font-family:var(--mono);font-size:10px;color:var(--text-dim);display:flex;gap:8px}
.h-type{color:var(--accent)}
.saved-panel{border-top:1px solid var(--border);padding:12px 20px;max-height:200px;overflow-y:auto;background:#fafbfc}
.saved-title{font-family:var(--mono);font-size:9px;text-transform:uppercase;letter-spacing:.1em;color:var(--text-dim);margin-bottom:8px;display:flex;justify-content:space-between}
.saved-item{display:flex;align-items:center;justify-content:space-between;padding:7px 0;border-bottom:1px solid var(--border)}
.saved-item:last-child{border-bottom:none}
.saved-name{font-size:12px;font-weight:500}
.saved-co{font-family:var(--mono);font-size:10px;color:var(--text-dim);margin-top:1px}
.saved-rm{background:none;border:none;color:var(--text-dim);cursor:pointer;font-size:16px;padding:2px 6px;border-radius:4px;line-height:1}
.saved-rm:hover{color:var(--red)}
.right-panel{display:flex;flex-direction:column;overflow:hidden;background:var(--bg)}
.empty-state{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;padding:40px;text-align:center}
.empty-icon{font-size:40px;opacity:.25}
.empty-title{font-size:16px;font-weight:600;color:var(--text-mid)}
.empty-sub{font-family:var(--mono);font-size:11px;color:var(--text-dim);line-height:1.7;max-width:320px}
.loading-state{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:20px}
.loading-ring{width:44px;height:44px;border:2px solid var(--border);border-top-color:var(--accent);border-radius:50%;animation:spin .8s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.loading-text{font-family:var(--mono);font-size:12px;color:var(--text-dim);letter-spacing:.08em}
.query-bar{display:flex;align-items:center;justify-content:space-between;padding:14px 24px;background:var(--surface);border-bottom:1px solid var(--border);box-shadow:0 1px 3px rgba(0,0,0,.04)}
.query-info{display:flex;align-items:center;gap:12px}
.query-tag{font-family:var(--mono);font-size:10px;letter-spacing:.08em;color:#fff;background:var(--accent);padding:3px 8px;border-radius:4px;font-weight:600}
.query-text{font-size:14px;font-weight:600}
.query-count{font-family:var(--mono);font-size:11px;color:var(--text-dim)}
.results-panel{flex:1;overflow-y:auto;padding:20px 24px}
.results-panel::-webkit-scrollbar{width:4px}
.results-panel::-webkit-scrollbar-thumb{background:var(--border);border-radius:2px}
.contact-card{background:var(--card);border:1px solid var(--border);border-radius:12px;margin-bottom:16px;overflow:hidden;box-shadow:0 1px 6px rgba(0,0,0,.05);animation:slide-in .3s ease}
@keyframes slide-in{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
.card-header{padding:18px 20px 14px;border-bottom:1px solid var(--border);display:flex;align-items:flex-start;justify-content:space-between}
.card-avatar{width:44px;height:44px;border-radius:10px;background:linear-gradient(135deg,#fde68a,var(--accent));display:flex;align-items:center;justify-content:center;font-weight:700;font-size:15px;color:#fff;flex-shrink:0}
.card-identity{flex:1;padding:0 14px}
.card-name{font-size:17px;font-weight:600;margin-bottom:2px}
.card-title{font-size:13px;color:var(--text-mid);margin-bottom:4px}
.card-company{font-family:var(--mono);font-size:11px;color:var(--accent);letter-spacing:.04em}
.confidence-badge{display:flex;flex-direction:column;align-items:flex-end;gap:4px;flex-shrink:0}
.conf-label{font-family:var(--mono);font-size:9px;text-transform:uppercase;letter-spacing:.1em;color:var(--text-dim)}
.conf-bar{width:80px;height:4px;background:var(--border);border-radius:2px;overflow:hidden}
.conf-fill{height:100%;border-radius:2px}
.conf-fill.high{background:var(--green)}
.conf-fill.med{background:var(--accent)}
.conf-fill.low{background:var(--red)}
.conf-pct{font-family:var(--mono);font-size:11px;color:var(--text-mid)}
.contact-grid{display:grid;grid-template-columns:1fr 1fr}
.contact-field{padding:12px 20px;border-right:1px solid var(--border);border-bottom:1px solid var(--border)}
.contact-field:nth-child(even){border-right:none}
.contact-field:nth-last-child(-n+2){border-bottom:none}
.field-label{font-family:var(--mono);font-size:9px;text-transform:uppercase;letter-spacing:.1em;color:var(--text-dim);margin-bottom:5px}
.field-value{font-size:13px}
.field-value.mono{font-family:var(--mono);font-size:12px}
.field-value.link{color:var(--accent);text-decoration:none}
.field-value.link:hover{text-decoration:underline}
.field-value.na{color:var(--text-dim);font-style:italic;font-size:12px}
.intel-row{padding:12px 20px;border-top:1px solid var(--border);background:#fafbfc}
.intel-row p{font-size:13px;color:var(--text-mid);line-height:1.6;margin-top:4px}
.card-footer{padding:12px 20px;display:flex;align-items:center;justify-content:space-between;background:#f8fafc;border-top:1px solid var(--border)}
.source-tag{font-family:var(--mono);font-size:10px;color:var(--text-dim)}
.card-actions{display:flex;gap:8px}
.act-btn{padding:5px 12px;border-radius:6px;border:1px solid var(--border);background:#fff;color:var(--text-mid);font-family:var(--mono);font-size:10px;cursor:pointer;transition:all .15s;text-transform:uppercase}
.act-btn:hover{border-color:var(--accent);color:var(--accent);background:var(--accent-dim)}
.act-btn.primary{background:var(--accent);border-color:var(--accent);color:#fff;font-weight:600}
.act-btn.primary:hover{background:#b45309}
.error-block{background:#fef2f2;border:1px solid #fecaca;border-radius:10px;padding:16px 20px;color:var(--red);font-size:13px;font-family:var(--mono)}
</style>
</head>
<body>
<div class="header">
  <div class="brand">
    <div class="brand-icon">DJ</div>
    <div><div class="brand-name">CorpDev CEO Agent</div><div class="brand-sub">Contact Intelligence // DJ AI</div></div>
  </div>
  <div class="header-right"><div class="status-dot"></div><div class="status-label">Live Intelligence</div></div>
</div>
<div class="main">
  <div class="left-panel">
    <div class="panel-header">
      <div class="panel-title">Search Mode</div>
      <div class="mode-toggle">
        <button class="mode-btn active" id="mode-company" onclick="setMode('company')">&#127970; Company</button>
        <button class="mode-btn" id="mode-ceo" onclick="setMode('ceo')">&#128100; CEO / Exec</button>
      </div>
      <div class="search-box">
        <input class="search-input" id="search-input" placeholder="e.g. Salesforce, Marc Benioff..." onkeydown="if(event.key==='Enter') runSearch()">
        <button class="search-btn" id="search-btn" onclick="runSearch()">
          <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
        </button>
      </div>
    </div>
    <div class="filters">
      <div class="filter-label">Industry Filter</div>
      <div class="filter-chips">
        <button class="chip active" onclick="toggleChip(this)">All</button>
        <button class="chip" onclick="toggleChip(this)">Healthcare</button>
        <button class="chip" onclick="toggleChip(this)">Construction</button>
        <button class="chip" onclick="toggleChip(this)">Finance</button>
        <button class="chip" onclick="toggleChip(this)">Tech</button>
        <button class="chip" onclick="toggleChip(this)">Nonprofit</button>
        <button class="chip" onclick="toggleChip(this)">Gov/Muni</button>
      </div>
    </div>
    <div class="history-section"><div class="section-label">Recent Searches</div><div id="history-list"></div></div>
    <div class="saved-panel">
      <div class="saved-title"><span>Saved Contacts</span><span id="saved-count">0</span></div>
      <div id="saved-list"><div style="font-family:var(--mono);font-size:10px;color:var(--text-dim);">No saved contacts yet</div></div>
    </div>
  </div>
  <div class="right-panel" id="right-panel">
    <div class="empty-state">
      <div class="empty-icon">&#9889;</div>
      <div class="empty-title">CorpDev CEO Agent</div>
      <div class="empty-sub">Search by company or executive name to surface contact intelligence.</div>
    </div>
  </div>
</div>
<script>
let searchMode='company',searchHistory=[],savedContacts=[],currentQuery='',selectedIndustry='All';
function setMode(m){searchMode=m;document.getElementById('mode-company').classList.toggle('active',m==='company');document.getElementById('mode-ceo').classList.toggle('active',m==='ceo');document.getElementById('search-input').placeholder=m==='company'?'e.g. Salesforce, Home HeadQuarters...':'e.g. Marc Benioff, Hope Knight...';}
function toggleChip(el){document.querySelectorAll('.chip').forEach(c=>c.classList.remove('active'));el.classList.add('active');selectedIndustry=el.textContent;}
async function runSearch(){const q=document.getElementById('search-input').value.trim();if(!q)return;currentQuery=q;setLoading(true);searchHistory.unshift({query:q,mode:searchMode,ts:Date.now()});if(searchHistory.length>12)searchHistory.pop();renderHistory();try{const r=await fetch('/api/search',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({query:q,mode:searchMode,industry:selectedIndustry})});if(!r.ok){const e=await r.json();throw new Error(e.detail||'Search failed');}const d=await r.json();renderResults(d.contacts,q,d.raw);}catch(e){renderError(e.message);}finally{setLoading(false);}}
function esc(s){return String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
function val(v){return v&&v!=='Not found';}
function timeAgo(ts){const s=Math.floor((Date.now()-ts)/1000);if(s<60)return 'just now';if(s<3600)return Math.floor(s/60)+'m ago';return Math.floor(s/3600)+'h ago';}
function renderResults(contacts,query,raw){const panel=document.getElementById('right-panel');let html='<div class="query-bar"><div class="query-info"><span class="query-tag">'+searchMode.toUpperCase()+'</span><span class="query-text">'+esc(query)+'</span></div><div class="query-count">'+contacts.length+' result'+(contacts.length!==1?'s':'')+'</div></div><div class="results-panel">';if(!contacts.length&&raw){html+='<div style="background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:16px 20px;margin-bottom:16px;"><div style="font-family:var(--mono);font-size:10px;text-transform:uppercase;color:var(--accent);margin-bottom:8px;">Intelligence Report</div><div style="font-size:13px;color:var(--text-mid);line-height:1.7;">'+esc(raw)+'</div></div>';}
contacts.forEach(function(c,i){var ini=(c.name||'??').split(' ').map(function(w){return w[0];}).join('').toUpperCase().slice(0,2);var cl=c.confidence>=75?'high':c.confidence>=50?'med':'low';var conf=c.confidence||0;var eH=val(c.email)?'<a class="field-value mono link" href="mailto:'+esc(c.email)+'">'+esc(c.email)+'</a>'+(c.email_confidence?'<div style="font-family:var(--mono);font-size:9px;color:var(--text-dim);margin-top:3px;">'+esc(c.email_confidence)+'</div>':''):'<span class="field-value na">Not found</span>';var pH=val(c.phone)?'<span class="field-value mono">'+esc(c.phone)+'</span>':'<span class="field-value na">Not found</span>';var lH=val(c.linkedin)?'<a class="field-value link" href="'+esc(c.linkedin)+'" target="_blank">View Profile &rarr;</a>':'<span class="field-value na">Not found</span>';var wH=val(c.website)?'<a class="field-value link" href="'+esc(c.website)+'" target="_blank">'+esc(c.website.replace(/https?:\\/\\//,''))+'</a>':'<span class="field-value na">Not found</span>';
html+='<div class="contact-card" style="animation-delay:'+( i*0.08)+'s"><div class="card-header"><div class="card-avatar">'+ini+'</div><div class="card-identity"><div class="card-name">'+esc(c.name||'Unknown')+'</div><div class="card-title">'+esc(c.title||'Title unknown')+'</div><div class="card-company">'+esc(c.company||'')+'</div></div><div class="confidence-badge"><div class="conf-label">Confidence</div><div class="conf-bar"><div class="conf-fill '+cl+'" style="width:'+conf+'%"></div></div><div class="conf-pct">'+conf+'%</div></div></div><div class="contact-grid"><div class="contact-field"><div class="field-label">Email</div>'+eH+'</div><div class="contact-field"><div class="field-label">Phone</div>'+pH+'</div><div class="contact-field"><div class="field-label">LinkedIn</div>'+lH+'</div><div class="contact-field"><div class="field-label">Website</div>'+wH+'</div><div class="contact-field"><div class="field-label">HQ Location</div><span class="field-value">'+esc(c.hq||'Unknown')+'</span></div><div class="contact-field"><div class="field-label">Employees</div><span class="field-value mono">'+esc(c.employees||'Unknown')+'</span></div></div>'+(val(c.intel)?'<div class="intel-row"><div class="field-label">&#9889; Intel</div><p>'+esc(c.intel)+'</p></div>':'')+'<div class="card-footer"><span class="source-tag">Web Intelligence &middot; '+new Date().toLocaleDateString()+'</span><div class="card-actions"><button class="act-btn" onclick="copyCard('+i+')">Copy</button><button class="act-btn primary" onclick="saveCard('+i+')">Save</button></div></div></div>';});
html+='</div>';panel.innerHTML=html;window._last=contacts;}
function copyCard(i){var c=(window._last||[])[i];if(!c)return;navigator.clipboard.writeText('Name: '+c.name+'\\nTitle: '+c.title+'\\nCompany: '+c.company+'\\nEmail: '+c.email+'\\nPhone: '+c.phone+'\\nLinkedIn: '+c.linkedin+'\\nWebsite: '+c.website+'\\nHQ: '+c.hq).catch(function(){});}
function saveCard(i){var c=(window._last||[])[i];if(!c)return;if(!savedContacts.find(function(s){return s.name===c.name&&s.company===c.company;})){savedContacts.push(c);renderSaved();}}
function renderSaved(){document.getElementById('saved-count').textContent=savedContacts.length;var l=document.getElementById('saved-list');if(!savedContacts.length){l.innerHTML='<div style="font-family:var(--mono);font-size:10px;color:var(--text-dim);">No saved contacts yet</div>';return;}l.innerHTML=savedContacts.map(function(c,i){return '<div class="saved-item"><div><div class="saved-name">'+esc(c.name||'Unknown')+'</div><div class="saved-co">'+esc(c.company||'')+' &middot; '+esc(c.title||'')+'</div></div><button class="saved-rm" onclick="removeSaved('+i+')">&times;</button></div>';}).join('');}
function removeSaved(i){savedContacts.splice(i,1);renderSaved();}
function renderHistory(){document.getElementById('history-list').innerHTML=searchHistory.map(function(h){return '<div class="history-item'+(h.query===currentQuery?' active':'')+'" onclick="rerun(this)" data-q="'+esc(h.query)+'" data-m="'+h.mode+'"><div class="h-company">'+esc(h.query)+'</div><div class="h-meta"><span class="h-type">'+h.mode+'</span><span>'+timeAgo(h.ts)+'</span></div></div>';}).join('');}
function rerun(el){var q=el.getAttribute('data-q');var m=el.getAttribute('data-m');searchMode=m;document.getElementById('mode-company').classList.toggle('active',m==='company');document.getElementById('mode-ceo').classList.toggle('active',m==='ceo');document.getElementById('search-input').value=q;runSearch();}
function setLoading(on){document.getElementById('search-btn').disabled=on;if(on)document.getElementById('right-panel').innerHTML='<div class="loading-state"><div class="loading-ring"></div><div class="loading-text">Searching web intelligence...</div></div>';}
function renderError(msg){document.getElementById('right-panel').innerHTML='<div style="padding:24px"><div class="error-block">&#9888; '+esc(msg)+'</div></div>';}
</script>
</body>
</html>"""

with open('C:/Projects/CorpDevCEOAgent/static/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('index.html written successfully.')
