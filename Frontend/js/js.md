# JS Quick Recall Sheet


## 1 Basics
- `console.log(``)`: displays the text in the console
- `window.alert(`message`)`: displays an alert
- `window.prompt()` gets input
- `typeconversion`: x = Number/String/Boolean(x)
- `document.getElementByID("id").textcontent`: changes some ID's text content
- `function`: function <name>(<parameters>){<code>}
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


## 9 Arrays
- `theory`
    - A data structure that stores ordered collection of values
- `example`
    ```js
    let fruits = ["apple", "banana", "mango"];
    fruits.push("item"); // adds to end and returns length
    a = fruits.pop(); //removes from end and returns removed element
    b = fruits.shift(); //removes from start and returns removed element
    fruits.unshift("item"); // adds to end and returns length
    fruits.length;
    fruits.indexOf("apple");
    fruits.sort().reverse();
    ```

## 10 Spread Operator
- `theory`
    - It separates an array/string into elements
- `example`
    ```js
    name = "username";
    letters = [...name].join("-");
    vegetables = ["potato", "brinjal"];
    fruits = ["apple", "banana", "mango"];

    foods = [...fruits, ... vegetables, "peanut butter", "chocolate"];
    console.log(foods);
    ```


## 11 Rest Parameter
- `theory`
    - Allows a function to work with variable number of arguments by bundling them into an array
- `example`
    ```js
    function openFridge(...food){
        console.log(food);
    }
    const food1 = "pizza";
    const food2 = "milk";
    
    openFridge(food1, food2);
    ```


## 12 Callback
- `theory`
    - A function we pass into another function to be called later
    - Used to handle asychronous operations
    - "Hey, when you're done with this, do this next"
- `example`
    ```js
    Process(Greet);

    function Greet(name){
        console.log("Hi " + name + "!");
    }

    function Process(callbacker){
        let name = window.prompt("Enter your name: ");
        callbacker(name)
    }
    ```


## 13 Array Methods
- `forEach`
    - Method used to iterate over the elements of an array and apply a function(callback) to each element
    - element index array are predefined parameters for these
    ```js
    let fruits = ["apPle", "baNana", "manGo"];

    fruits.forEach(capitalise);
    fruits.forEach(display);

    function capitalise(element, index, arr){
        arr[index] = element.charAt(0).toUpperCase() + element.slice(1).toLowerCase();
        }
    function display(element, index, arr){
        console.log(element, index, arr)
    }
    ```