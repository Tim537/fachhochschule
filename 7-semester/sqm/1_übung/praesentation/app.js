"use strict";
(() => {
  const slides = Array.from(document.querySelectorAll('.slide'));
  const status = document.getElementById('status');
  const dialogs = Array.from(document.querySelectorAll('dialog'));
  let current = 0;
  let presenter = null;
  let lastFocus = null;
  const readHash = () => {
    const match = location.hash.match(/^#folie-([1-5])$/);
    return match ? Number(match[1]) - 1 : 0;
  };
  function syncPresenter() {
    if (presenter && !presenter.closed) {
      presenter.postMessage({type:'qs-slide', index:current}, '*');
    }
  }
  function show(index, focus = false) {
    current = Math.max(0, Math.min(slides.length - 1, Number(index) || 0));
    slides.forEach((slide, i) => { slide.hidden = i !== current; });
    document.title = `${current + 1}/5 · ${slides[current].querySelector('h2').textContent}`;
    try { history.replaceState(null, '', `#folie-${current + 1}`); } catch (_) { /* Files can restrict history APIs. */ }
    document.querySelectorAll('[data-slide]').forEach(button => {
      if (Number(button.dataset.slide) === current) button.setAttribute('aria-current', 'page');
      else button.removeAttribute('aria-current');
    });
    status.textContent = `Folie ${current + 1} von ${slides.length}: ${slides[current].querySelector('h2').textContent}`;
    window.scrollTo(0, 0);
    if (focus) slides[current].querySelector('h2').focus({preventScroll:true});
    syncPresenter();
  }
  function openDialog(id) {
    const dialog = document.getElementById(id);
    if (!dialog || typeof dialog.showModal !== 'function') {
      location.href = id === 'chapters' ? 'statisch.html' : 'README.md';
      return;
    }
    if (dialog.open) { dialog.close(); return; }
    dialogs.filter(other => other.open).forEach(other => other.close());
    lastFocus = document.activeElement;
    dialog.showModal();
  }
  dialogs.forEach(dialog => dialog.addEventListener('close', () => {
    if (lastFocus && lastFocus.isConnected) lastFocus.focus({preventScroll:true});
  }));
  document.querySelectorAll('[data-close]').forEach(button => button.addEventListener('click', () => {
    document.getElementById(button.dataset.close).close();
  }));
  document.querySelectorAll('[data-slide]').forEach(button => button.addEventListener('click', () => {
    document.getElementById('chapters').close();
    show(Number(button.dataset.slide), true);
  }));
  function openPresenter() {
    presenter = window.open(`sprecher.html#notiz-${current + 1}`, 'qs-private-speaker', 'popup,width=1000,height=850');
    if (presenter) { presenter.focus(); syncPresenter(); }
    else { openDialog('help'); }
  }
  async function fullscreen() {
    try {
      if (document.fullscreenElement && document.exitFullscreen) await document.exitFullscreen();
      else if (document.documentElement.requestFullscreen) await document.documentElement.requestFullscreen();
      else openDialog('help');
    } catch (_) { openDialog('help'); }
  }
  window.addEventListener('keydown', event => {
    if (event.altKey || event.ctrlKey || event.metaKey || event.isComposing || event.defaultPrevented) return;
    if (event.target instanceof Element && event.target.closest('input,textarea,select,[contenteditable="true"]')) return;
    const key = event.key.toLowerCase();
    if (dialogs.some(dialog => dialog.open)) return;
    if (['arrowright','arrowdown','pagedown'].includes(key)) { event.preventDefault(); show(current + 1); }
    else if (['arrowleft','arrowup','pageup'].includes(key)) { event.preventDefault(); show(current - 1); }
    else if (key === 'q') { event.preventDefault(); openDialog('chapters'); }
    else if (key === 'h') { event.preventDefault(); openDialog('help'); }
    else if (key === 'n') { event.preventDefault(); openPresenter(); }
    else if (key === 'f') { event.preventDefault(); fullscreen(); }
  });
  window.addEventListener('hashchange', () => show(readHash()));
  window.addEventListener('message', event => {
    if (event.source !== presenter || !event.data) return;
    if (event.data.type === 'qs-ready') syncPresenter();
    if (event.data.type === 'qs-navigate' && Number.isInteger(event.data.index)) show(event.data.index);
  });
  show(readHash());
})();
