// Utility function to escape HTML special characters to prevent XSS
function escapeHTML(str) {
  return str.replace(/[&<>"'`=\/]/g, function(s) {
    return ({
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      '"': '&quot;',
      "'": '&#39;',
      '`': '&#96;',
      '=': '&#61;',
      '/': '&#47;'
    })[s];
  });
}

// Function to validate and display user input safely
function displayUserInput(input) {
  // Basic validation example: input must be a string, 1-100 chars, alphanumeric + space + some punctuation
  const isValid = typeof input === 'string' &&
                  input.length > 0 &&
                  input.length <= 100 &&
                  /^[a-zA-Z0-9 .,!?'-]*$/.test(input);

  if (!isValid) {
    console.error('Invalid input');
    return;
  }

  // Escape HTML to prevent XSS
  const safeInput = escapeHTML(input);

  // Display safely in a div with id 'output'
  const outputDiv = document.getElementById('output');
  if (outputDiv) {
    outputDiv.textContent = safeInput;  // textContent sets text without parsing HTML
  }
}
