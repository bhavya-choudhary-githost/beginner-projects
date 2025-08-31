# JS Quick Recall Sheet


## 1 Basics
- `console.log(``)`: displays the text in the console
- `window.alert(`message`)`: displays an alert
- `window.prompt()` gets input
- `typeconversion`: x = Number/String/Boolean(x)
- `document.getElementByID("id").textcontent`: changes some ID's text content
- `comments`
    - by // comment
    - by /*
    multi line comment
    */
- `other`
    - template literals require backticks along with ${value}
    - 'typeof' is used to find variable type
    - semicolon is used after every statement
    - const used instead of let for variables that dont change
    - .checked property


## 2 Global Objects
- `Math`
    - `simple maths`
        Math.PI, Math.E
        Math.round()
        Math.floor()
        Math.ceil()
        Math.trunc()
        Math.pow(a, b)
        Math.sqrt()
        Math.log()
        Math.sin()
        Math.cos()
        Math.tan()
        Math.abs()
        Math.sign()
        Math.min(a, b, c)
        Math.max(a, b, c)
    - `other`
    Math.random() : gives a random number between 1 and 0


## 3 Ternary Operator
- `theory`
    - let a = condition ? codeIfTrue : codeIfFalse
- `example`
```js
 let message = age >= 18 ? "You can enter" : "You can not enter"
 console.log(message)
```


## 4 Switch 
- `theory`
    - good replacement to using a lot of similar if else statements
    - switch(condition resut or variable){
        case condition:
        changes;}
- `example`
    ```js
    // ex-1
    let score = 92;
    let Grade;

    switch(true){
        case score >= 90:
            Grade = "A";
            break;
        case score >= 80:
            Grade = "B";
            break;
        default:
            Grade = "F"
    }
    console.log(Grade)
    // ex-2

    let day =  1

    switch(day){
        case 1:
            console.log("Monday");
            break;
        case 2:
            break;
            console.log("Tuesday");
    }
    ```


## 5 String Methods
- `theory`
    - `common methods`
        string.charAt(index)
        string.indexOf("a")
        string.lastIndexOf("a")
        string.length
        string.trim()
        string.slice(start, end)
        string.toUpperCase()
        string.toLowerCase()
        string.repeat(no of times)
        string.startsWith(" ")
        string.endsWith("a")
        string.includes(" ")

        string.replaceAll("to be replaced","replacing element")
        string.padStart(no of characters to be reached, "what to pad with")
        string.padEnd(no of characters to be reached, "what to pad with")
        

## 6 Method Chaining
- `example`
    ```js
    const username = window.prompt("Enter your name: ");

    // without Chaining
    let name = username.trim();
    let firstletter = name.charAt(0);
    let one = firstletter.toUpperCase();

    let otherletters = name.slice(1);
    let two = otherletters.toLowerCase();

    let three = one + two;
    console.log(three);

    // with Chaining
    let properName = username.trim().charAt(0).toUpperCase() + username.trim().slice(1).toLowerCase();
    console.log(properName);
    ```


## 7 Operators
- `theory`
    - `Boolean`
        AND = &&
        OR = ||
        NOT = !
    - `Other`
        = assignment operator
        == comparison operator
        === strict equality operator(also checks if datatype is equal)
        != inequality operator
        !== strict inequality operator


## 8 Conditionals
- `theory`
    if/else/else if

    break/continue

    while/do-while
    for/for-in/for-of: in iterate keys/indexes, of iterates values






