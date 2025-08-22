# HTML Quick Recall Sheet

## 1. Basic Structure
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Page Title</title>
</head>
<body>
    <!-- Content goes here -->
</body>
</html>

## 2. Headings & Paragraphs
<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
<p>This is a paragraph.</p>
<br>

## 3. Text Formatting
<b>Bold</b> <strong>Strong</strong> <i>Italic</i> <em>Emphasis</em> <u>Underline</u> <small>Small text</small> <mark>Highlight</mark> <del>Deleted</del> <ins>Inserted</ins> <sub>Subscript</sub> <sup>Superscript</sup>

## 4. Lists
<ul><li>Item 1</li><li>Item 2</li></ul>
<ol><li>First</li><li>Second</li></ol>

## 5. Links
<a href="https://example.com" target="_blank">Visit Example</a> <a href="#section1">Jump to Section</a>

## 6. Images
<img src="image.jpg" alt="Description" width="200" height="150"> <a href="https://example.com"><img src="logo.png" alt="Logo"></a>

## 7. Tables
<table border="1"><thead><tr><th>Name</th><th>Age</th><th>City</th></tr></thead><tbody><tr><td>Alice</td><td>25</td><td>New York</td></tr><tr><td>Bob</td><td>30</td><td>London</td></tr></tbody></table>

## 8. Forms
<form action="/submit" method="post">
<label for="name">Name:</label><input type="text" id="name" name="name" required><br><br>
<label for="email">Email:</label><input type="email" id="email" name="email"><br><br>
<label>Gender:</label><input type="radio" id="male" name="gender" value="male"><label for="male">Male</label>
<input type="radio" id="female" name="gender" value="female"><label for="female">Female</label><br><br>
<label>Hobbies:</label><input type="checkbox" id="reading" name="hobby" value="reading">Reading
<input type="checkbox" id="sports" name="hobby" value="sports">Sports<br><br>
<label for="country">Country:</label>
<select id="country" name="country">
<option value="us">USA</option>
<option value="uk">UK</option>
<option value="in">India</option>
</select><br><br>
<label for="message">Message:</label><br>
<textarea id="message" name="message" rows="4" cols="50"></textarea><br><br>
<input type="submit" value="Submit"><input type="reset" value="Reset">
</form>

## 9. Divs & Spans
<div id="container"><p>This is inside a div.</p></div><span class="highlight">Inline span text</span>

## 10. Semantic Tags
<header>Header content</header><nav>Navigation links</nav><main>Main content</main><article>Article content</article><section>Section content</section><aside>Sidebar</aside><footer>Footer content</footer>

## 11. Multimedia
<audio controls><source src="audio.mp3" type="audio/mpeg">Your browser does not support audio.</audio>
<video width="320" height="240" controls><source src="video.mp4" type="video/mp4">Your browser does not support video.</video>

## 12. Comments
<!-- This is an HTML comment -->

## 13. Miscellaneous
<hr> <pre>Preformatted text</pre> <code>Inline code</code> <blockquote>Quoted text</blockquote> <br>

## 14. Dropdown & Navbar Example
<nav class="navbar"><ul><li><a href="#">Home</a></li><li><a href="#">About</a></li><li><a href="#">Contact</a></li></ul></nav>
<div class="dropdown"><button>Menu</button><div class="content"><a href="#">Option 1</a><a href="#">Option 2</a></div></div>
