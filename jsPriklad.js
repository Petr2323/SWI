function safeDisplay(input) {
  const div = document.createElement('div');
  div.textContent = input; // automaticke escapovani
  document.body.appendChild(div);
}
