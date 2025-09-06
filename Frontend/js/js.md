# JS Quick Recall Sheet


## 1 Basics
- `console.log(``)`: displays the text in the console
- `window.alert(`message`)`: displays an alert
- `window.prompt()` gets input
- `typeconversion`: x = Number/String/Boolean(x)
- `document.getElementById("id").textContent`: changes some ID's text content
- `function`: function <name>(<parameters>){<code>} in function declaration;
    we can also define a function as a value or variable by function expression which can be shortened with arrow function
    ```js
    function hello1(){
        console.log("hello")
    }
    hello2 = function(){
        console.log("hello")
    }
    hello3 = () => console.log("hello");
    ```
- `objects`: const name = {key:value, function}
    "this" keyword reference the immediate object, doesnt work with arrow functions
    ```js
    const person1 = {
        firstname: "Spongebob",
        lastname: "Squarepants",
        sayhi: function(){console.log(`hi im ${this.firstname}!`)}
    }
    ```
- `comments`
    - by // comment
    - by /*
    multi line comment
    */
- `other`
    - template literals require backticks along with ${value}
    - 'typeof' is used to find variable type
    - semicolon is after every statement optional to put yourself but recommended for clarity
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
    Math.random() : gives a random number between 0(inclusive) and 1(exclusive)


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
            console.log("Tuesday");
            break;
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
    for/for-in/for-of: in = iterate keys/indexes, of = iterates values


## 9 Arrays
- `theory`
    - A data structure that stores ordered collection of values
- `example`
    ```js
    let fruits = ["apple", "banana", "mango"];
    fruits.push("item"); // adds to end and returns length
    a = fruits.pop(); //removes from end and returns removed element
    b = fruits.shift(); //removes from start and returns removed element
    fruits.unshift("item"); // adds to start and returns length
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
    - accepts a callback then executes function once for each array element
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
- `map`
    - accepts a callback then applies that function (which transforms) to each element of the array, then returns a new array
    ```js
    const dates = ["9-5-2025","10-2-2025", "3-30-2021"];
    const formatteddates = dates.map(format);

    function format(element){
        const parts = element.split("-")
        return `${parts[0]}/${parts[1]}/${parts[2]}`
    }
    ```
- `filter`
    -  accepts a callback then applies that function (which checks) to each element of the array, then returns a new array
    ```js
    const fruits = ["apple", "banana", "cocomelon"]
    const smallwords = fruits.filter(issmall)

    function issmall(element){
        return element.length < 6;
    }
    ```
- `reduce`
    - accepts a callback then applies that function (which reduces the elements to a single value) to each element of the array, then returns the single value
    - has two parameters: accumulator and element
    ```js
    const marks = [76, 89, 30, 68]
    const max = marks.reduce(getMax)

    function getMax(accumulator, element){
        return Math.max(accumulator, element)
    }
    ```
- `sort`
    - sorts the elements of an array as strings in a lexicographic order,
    lexicographic = (alphabet + number + symbols) as strings
    ```js
    // Sorting strings (alphabetical)
    const characters = ["SpongeBob", "Patrick", "Squidward", "Mr. Krabs", "Plankton"];
    characters.sort();
    console.log(characters);
    // ["Mr. Krabs", "Patrick", "Plankton", "SpongeBob", "Squidward"]

    // Sorting numbers (needs compare function)
    const scores = [40, 100, 1, 5, 25, 10];
    scores.sort((a, b) => a - b); 
    console.log(scores);
    // [1, 5, 10, 25, 40, 100]

    // Sorting objects by a property
    const employees = [
    { name: "SpongeBob", age: 20 },
    { name: "Squidward", age: 32 },
    { name: "Patrick", age: 22 }
    ];
    employees.sort((a, b) => a.age - b.age);
    console.log(employees);
    /*
    [
    { name: "SpongeBob", age: 20 },
    { name: "Patrick", age: 22 },
    { name: "Squidward", age: 32 }
    ]
    */
    ```
    
    - `shuffling`
    shuffling using the Fisher-Yates algorithm
    ```js
    function shuffleArray(array) {
    // Copy array to avoid modifying original
    const arr = [...array];

    for (let i = arr.length - 1; i > 0; i--) {
    // Pick a random index from 0 to i
    const j = Math.floor(Math.random() * (i + 1));

    // Swap arr[i] with arr[j]
    [arr[i], arr[j]] = [arr[j], arr[i]];
    }

    return arr;
    }

    // Example usage
    const fruits = ["apple", "banana", "mango", "grapes", "orange"];
    const shuffledFruits = shuffleArray(fruits);

    console.log(shuffledFruits);
    ```


## 14 Constructor
- special method for defining attributes and methods of an object
```js
function Car(brand, model, year, color){
    this.brand = brand,
    this.model = model,
    this.year = year,
    this.color = color
    this.drive = function(){console.log(`You're driving ${this.model}`)}
    }
const car1 = new Car("Ford", "Mustang", 2024, "Red")
car1.drive()
```

## 15 Classes
- provides a cleaner and more structured way to defining attributes and methods compared to constructor, e.g. static keywords, encapsulation, inheritance etc.
    - `static`: keyword that defines the properties and methods pertaining to the class itself rather than the object created from that class.(class owns anything static not the objects)
    ```js
    class User{
        static usercount = 0;

        constructor(username){
            this.username = username;
            User.usercount++;
        }
   }
   const user1 = new User("patrick")
   ```
   
   - `inheritance`: allows a new class to inherit the properties and methods of another class (parent => child)
   ```js
   class Animal{
        alive = true;

        sleep(){
            console.log(`this ${this.name} is fast asleep`)
        }
   }
   class Zebra extends Animal{
        name = "zebra";
   }
   const zebra = new Zebra();
   ```
   - `super keyword`: special keyword used within children class to refer to the parent class
   ```js
       class Animal {
      constructor(name) {
        this.name = name;
      }
    }

    class Dog extends Animal {
      constructor(name, breed) {
        super(name); // Calls the Animal constructor
        this.breed = breed;
      }
    }
    ```
    - `getters and setters`: these modify and validate a value when reading/writing a property
        - `getters`: special method that makes a property readable
        - `setters`: special method that makes a property writable
        - `e.g.`
        ```js
        class Rectangle {
        constructor(height, width) {
            this.height = height;
            this._width = width; // use underscore for backing variable
            }

        set width(newWidth) {
            if (newWidth > 0) {
            this._width = newWidth;
            }
        }

        get width() {
            return this._width;
        }
        }

        const rectangle = new Rectangle(10, 5);
        console.log(rectangle.width); // 5
        rectangle.width = 20;
        console.log(rectangle.width); // 20

        ```

## 16 Destructuring 
- extract values from array/objects, then assign them to variables in a convenient way
 [] used to destructure arrays
 {} used to destructure objects
- `arrays`
    ```js
    fruits = ["apple", "banana", "mango", "grapes", "orange"]
    const [fav, nextFav, ...others] = fruits;
    console.log(fav);     // apple
    console.log(nextFav); // banana
    console.log(others);  // ["mango", "grapes", "orange"]
    ```
- `objects`
    ```js
    const spongebob = {
        name: "SpongeBob SquarePants",
        job: "Fry Cook",
        bestFriend: "Patrick Star",
        neighbor: "Squidward Tentacles",
        boss: "Mr. Krabs",
        pet: "Gary"
    };
    const { bestFriend, pet, ...others } = spongebob;
    console.log(bestFriend); // Patrick Star
    console.log(pet);        // Gary
    console.log(others);     // { name: "SpongeBob SquarePants", job: "Fry Cook", neighbor: "Squidward Tentacles", boss: "Mr. Krabs" }

    // --- Nested Object Example ---
    const show = {
        title: "SpongeBob SquarePants",
        characters: {
            main: "SpongeBob",
            sidekick: "Patrick",
            grumpyNeighbor: "Squidward",
            boss: "Mr. Krabs",
            pet: "Gary"
        }
    };
    // Rest inside nested object
    const { characters: { boss, ...restChars } } = show;
    console.log(boss);      // Mr. Krabs
    console.log(restChars); // { main: "SpongeBob", sidekick: "Patrick", grumpyNeighbor: "Squidward", pet: "Gary" }

    ```

## 17 Nested Objects
```js
const spongebob = {
  name: "SpongeBob SquarePants",
  job: "Fry Cook",
  address: {
    street: "124 Conch Street",
    city: "Bikini Bottom",
    ocean: "Pacific Ocean"
  }
};

console.log(spongebob.name);
console.log(spongebob.address.city);
console.log(spongebob.address.street);

spongebob.address.zipcode = "BB100";
console.log(spongebob.address);
```