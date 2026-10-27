"use strict";
(() => {
  const notes = Array.from(document.querySelectorAll('.speaker-note'));
  const controls = document.querySelector('.speaker-controls');
  const select = document.getElementById('slide-select');
  const previous = document.getElementById('previous');
  const next = document.getElementById('next');
  const connection = document.getElementById('connection');
  let linked = false;
  let current = 0;
  (window.QS_NOTES || []).forEach((note, i) => {
    const option = document.createElement('option');
    option.value = String(i);
    option.textContent = `${i + 1}. ${note.title}`;
    select.append(option);
  });
  function show(index, notify = false) {
    current = Math.max(0, Math.min(notes.length - 1, Number(index) || 0));
    notes.forEach((note, i) => { note.hidden = i !== current; });
    select.value = String(current);
    previous.disabled = current === 0;
    next.disabled = current === notes.length - 1;
    try { history.replaceState(null, '', `#notiz-${current + 1}`); } catch (_) { /* Optional state only. */ }
    if (notify && linked && window.opener && !window.opener.closed) {
      window.opener.postMessage({type:'qs-navigate',index:current}, '*');
    } else if (notify && linked) {
      linked = false;
      connection.textContent = 'Präsentationsfenster geschlossen. Die Notizen bleiben unabhängig bedienbar.';
    }
    window.scrollTo(0,0);
  }
  previous.addEventListener('click', () => show(current - 1,true));
  next.addEventListener('click', () => show(current + 1,true));
  select.addEventListener('change', () => show(Number(select.value),true));
  window.addEventListener('message', event => {
    if (!window.opener || event.source !== window.opener || !event.data || event.data.type !== 'qs-slide' || !Number.isInteger(event.data.index)) return;
    linked = true;
    connection.textContent = 'Mit der Präsentation verbunden. Die Notizauswahl wechselt auch die Vortragsfolie.';
    show(event.data.index);
  });
  window.addEventListener('keydown', event => {
    if (event.altKey || event.ctrlKey || event.metaKey || event.isComposing || event.defaultPrevented) return;
    if (event.target instanceof Element && event.target.closest('input,textarea,select,[contenteditable="true"]')) return;
    if (['ArrowRight','ArrowDown','PageDown'].includes(event.key)) { event.preventDefault(); show(current + 1,true); }
    if (['ArrowLeft','ArrowUp','PageUp'].includes(event.key)) { event.preventDefault(); show(current - 1,true); }
  });
  controls.hidden = false;
  const match = location.hash.match(/^#notiz-([1-5])$/);
  show(match ? Number(match[1])-1 : 0);
  if (window.opener && !window.opener.closed) window.opener.postMessage({type:'qs-ready'}, '*');
})();
