# CSS Quick Recall Sheet



## 1 Style Sheet Types
- `theory`
    - `Inline`  → In the individual tags
    - `Internal`→ style tags that include the individual  tags with curly brackets
    - `External`→ 
        - most common method
        - external .css file linked with <link rel="stylesheet">
        - individual tags with curly brackets
        - tags can also be given unique <id=""> : selected by #<idname>{<properties>} and/or reusable <class=""> attribute : selected by .<classname>{<properties>}
- `examples`
    ```html
    <p style="color:blue; background-color:red"></p>
    <style>
        p{
            color: blue;
            background-color:red
        }
    </style>
    ```

## 2 Colors
- `ways of writing colors`
    - `named colors`
    - `rgb`
    - `hsl`
- `attributes`
    ```css
    h1{
        background-color: value;
        color: value;
    }
    ```

## 3 Fonts
- `using external fonts`
    - using link on fonts.google.com and pasting it in the html header
    - download from fonts.google.com, then use this in the external css file:
        ```css
        @font-face{
            src: url(fonts/font_name.ttf);
            font-family: personalised_font_name;
        }
        ```
- `attributes`
    ```css
    p{
        font-family: "font a",fallbackfont;
        font-size: 16px = 1em;
        font-weight: bold/normal;
        font-style: italic/normal;
        text-decoration: underline;
    }
~ do you remember what sans serif fonts are

## 4 Borders
- `attributes`
    ```css
    p{
        border-width: 3px;
        border-style: solid/dashed/dotted/double/groove/ridge/inset/outset;
        border color: red;
        border radius: 2px;
    }
    ```
- `shorthand syntax`
    ```css
    p{
        border: 3px outset white;
        border-top/bottom/left/right: 5px inset black;
        border-radius: 2px
    }
    ```

## 5 Shadows
- `theory`
    - when using div/span give them ids/classes then use those to style
    ~ also div needs height and width property
    - text-shadow: 'horizontal-offset(rightside)' 'vertical-offset' 'blur' 'color', an separate shadow's attributes
- `attributes`
    ```css
    p{
        text-shadow: 3px 3px 5px red, -3px -3px 5px blue;
    }
    ```

## 6 Margins
- `theory`
    - margin is the space around any element not just the page
- `attributes`
    ```css
    body{
        margin: 0px;
        margin-top/bottom/left/right: 5px/auto;
    }
    ```

## 7 Float
- `theory`
    - float property allows other elements to flow around the parent element, flowroot tells the block to contain all floating elements within it
    - clear both tells the element to not float and start from a new line
- `attributes`
    ```css
    body{
        border: 3px inset;
        display: flow-root
    }
    #img1{
        float: left/right;
        margin-right/left: 6px;
    }
    #p1{
        clear: both;
    }
    ```

## 8 Overflow
- `theory`
    - it sets the behaviour for a parent element when the content doesnt fit
- `attributes`
    ```css
    div{
        border: 2px, groove;
        height: 75px;
        overflow: visible/hidden/scroll/auto;
        overflow: clip;
        overflow-clip-margin: 13px;
    }
    ```

## 9 Display
- `attributes`
    ```css
    div{
        background-color: blue;
        diplay: inline;
        visibility: hidden;
    }
    span{
        background-color: red;
        display: block;
    }
     div{
        background-color: blue;
        width: 100px;
        height: 100px;
        diplay: inline-block;
        visibility: hidden;
    }
    ```

## 10 Height and Width
- `theory`
    - *{ } is the universal selector, applies to all of the tags
    - we use min/max height of the box because the box size will vary according to how much text is inside
    - border-box includes border and padding in when accounting for the size
- `attributes`
    ```css
    * {
        box-sizing: border-box;
    }

    #box{
        background-color: grey;
        border: 3px solid black;
        padding: 10px
        height: 10vh/10px/10%/auto;
        min-height: 10%;
        max-height: 10%;
        text-align: center;
    }
    ```

## 11 Positions
- `theory`
    - types
        - `relative`: the position changes are taken relative to where it normally is 
        - `fixed`: the position is fixed relative to viewport
        - `absolute`: the position is fixed relative to its nearest ancestor
        - `sticky`: position is static until you scroll past when it becomes fixed
        - `static`: predefined default position of an element
- `attributes`
    ```css
        #box1{
            height: 200px;
            width: 200px;
            position: relative;
            top: 100px
            left: 10px
        }
        #box2{
            height: 100px;
            width: 100px;
            position: relative;
            top: 50px
            left: 50px
        }
    ```

## 12 Background-Images
- `attributes`
    ```css
        body{
            background-image: url();
            background-repeat: none;
            background-position: center;
            background-attachment: fixed;
            background-size: cover;
        }
    ```

## 13 Combinators
- `theory`
    - they explain the relationship between listed selectors, check brocode for examples
    - these include
          = descendant
        > = children
        ~ = siblings
        + = adjacent siblings


## 14 Pseudo-Classes
- `theory`: these add behaviours that are triggered under certain conditions to the selectors
- `attribues`
    ### a
    ```css
    a:link{
        color: yellow;
    }
    a:hover{
        color: blue;
        font-size: 1.1em;
    }
    a:active{
        color: red;
        font-size: 1.1em
    }
    a:visited{
        color: purple
    }
    ```

    ### li
    ```css
    li:not(:hover){
        color: grey;
    }
    li:nth-child(1/odd/2n+3){
        background-color: yellow
    }
    ```

    ### hiding in block
    ```css
    #box1 p{
        background-color: green;
        display: none;
    }
    #box1 p:hover{
        display: block;
    }
    ```

## 15 Pseudo-Elements
- `theory`
    - pseudo elements are keywords added after a selector to style parts of the elements
- `attributes`
    ```css
    h1::first-letter{
        font-size: 1.1em;
        font-style: italic
    }
    p::first-line{
        background-color: yellow;
    }
    p::selection{
        color: purple;
        background-color: black
    }
    #list-of-fruits li::before{
        content: "a";
    }
    #list-of-fruits li::after{
        content: "b";
    }
    #list-of-fruits li::marker{
        content: "✅";
        color: red;
    }
    ```

## 16 Pagination
- `theory`
    - Make simple paged with anchor tags and hyperlinks

## 17 Dropdown-Menus
- `attributes`
    ```html
        <div class="dropdown">
            <button>content</button>
            <div class="fruits">
                <a href="">apple</a>
                <a href="">mango</a>
                <a href="">banana</a>
            </div>
        </div>
    ```
    ```css
        .dropdown{
            display: inline-block;
        }
        .dropdown button{
            color: white;
            background-color: grey;
            padding: 10px 15px;
            border: none;
            cursor: pointer;
        }
        .dropdown a{
            display: block;
            color: block;
            text-decoration: none;
            padding: 10px 15px;
        }
        .dropdown .content{
            display: none;
            position: absolute;
            background-color: grey;
            min-width: 100px;
            box-shadow: 3px 2px 1px black;
        }
        .dropdown:hover .content{
            display: block;
        }
    ```

## 18 Navigation-Bar
- `attributes`
    ```html
    <body>
        <nav class="navbar">
            <ul>
                <li><a href="">Home</a></li>
                <li><a href="">About</a></li>
                <li><a href="">Contact</a></li>
            </ul>
        </nav>
        <main>
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Debitis totam omnis unde, nostrum beatae ab at! Odio iure nemo obcaecati perspiciatis quia, assumenda nulla ex ducimus at deleniti, eum vero!   
        </main>
    </body>
    ```
    ```css
    .navbar ul{
        list-style-type: none;
        background-color: grey;
    }
    .navbar a{
        color: white;
        text-decoration: none;
        padding: 50px;
        display: block;
        text-align: center;
    }
    ```

## 19 Icons
- `theory`
    - choose on fontawesome.com and copy past the i element along with src on html
    it looks like <i class="fa ..."></i>
    - use their classes to give them color