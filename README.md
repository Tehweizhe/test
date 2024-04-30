<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Title Aggregator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #000;
            color: #fff;
            padding: 20px;
        }
        a {
            color: #fff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Title Aggregator</h1>
    <ul id="headlines">
        <!-- Headlines will be inserted here dynamically -->
    </ul>

    <script>
        // Fetch headlines from the server and display them
        fetch('/headlines')
            .then(response => response.json())
            .then(data => {
                const headlinesList = document.getElementById('headlines');
                data.forEach(headline => {
                    const listItem = document.createElement('li');
                    const link = document.createElement('a');
                    link.href = headline.link;
                    link.textContent = headline.title;
                    link.target = '_blank';
                    listItem.appendChild(link);
                    headlinesList.appendChild(listItem);
                });
            });
    </script>
</body>
</html>
