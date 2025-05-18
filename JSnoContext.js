<!DOCTYPE html>
<html>
<head>
  <title>Display User Input</title>
</head>
<body>

  <h2>Enter something:</h2>
  <input type="text" id="userInput" placeholder="Type here...">
  <button onclick="displayInput()">Submit</button>

  <h3>Output:</h3>
  <p id="output"></p>

  <script>
    function displayInput() {
      // Get the value from the input box
      const input = document.getElementById('userInput').value;
      // Display the input inside the paragraph with id 'output'
      document.getElementById('output').textContent = input;
    }
  </script>

</body>
</html>
