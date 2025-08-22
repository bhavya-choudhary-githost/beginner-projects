# HTML Cheatsheet

## Structure
``` html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title</title>
  </head>
  <body>
    <!-- content here -->
  </body>
</html>
```

## Common Tags
- `<h1>`–`<h6>` : headings
- `<p>` : paragraph
- `<a href="url">` : link
- `<img src="path" alt="desc">` : image
- `<div>` : block container  
- `<span>` : inline container

## Lists
```html
<ul>
  <li>Item</li>
</ul>
<ol>
  <li>Numbered item</li>
</ol>
```

## Forms
```html
<form action="" method="">
  <input type="text" placeholder="Name">
  <input type="email">
  <input type="checkbox">
  <button type="submit">Send</button>
</form>
```
- `<textarea>` : multi-line text
- `<select><option></option></select>` : dropdown

## Semantic
<header> <nav> <main> <section> <article> <aside> <footer>

## Media
```html
<video controls>
  <source src="video.mp4" type="video/mp4">
</video>

<audio controls>
  <source src="audio.mp3" type="audio/mpeg">
</audio>
```

## Meta & Linking
```html
<meta charset="UTF-8">
<meta name="description" content="...">
<link rel="stylesheet" href="styles.css">
<script src="script.js" defer></script>
```

## Comments
```html
<!-- This is a comment -->
```
