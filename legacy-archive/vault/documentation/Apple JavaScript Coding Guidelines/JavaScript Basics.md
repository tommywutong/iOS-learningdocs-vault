---
title: Apple JavaScript Coding Guidelines
apple_id: TP40006088
resource_type: Guide
platform: Safari|macOS
topic: Languages & Utilities
technology: null
published: '2011-07-10'
source_url: https://developer.apple.com/library/archive/documentation/ScriptingAutomation/Conceptual/JSCodingGuide/JSIntroduction/JSIntroduction.html
archived_at: '2026-07-18T02:05:35.917859Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Apple JavaScript Coding Guidelines](Introduction%20to%20Apple%20JavaScript%20Coding%20Guidelines.md)


[Next](Object-Oriented%20JavaScript.md)[Previous](Introduction%20to%20Apple%20JavaScript%20Coding%20Guidelines.md)

# JavaScript Basics

JavaScript is a programming language used by web browsers to provide scripting access to webpages. It’s also being used more and more by desktop applications to provide an embedded scripting environment. If you’re already familiar with programming, JavaScript is easy to learn and provides many of the conventions you’re already used to.

This chapter introduces JavaScript language basics, including variables, iteration, and functions. Read it if you’re familiar with programming principles and want to learn specifics about the JavaScript language.

The basic building block in JavaScript is the variable. You declare variables using the `var` keyword, like this:

```
var foo;
```

JavaScript variables are type agnostic—they can hold data of any type, like a number or an object. Once you declare a variable, you assign it a value like this:

```
foo = 5;
```

The assignment operator, `=`, gives the variable to its left the value of the expression to its right. As shown, a variable can be given a literal value like a number. It can also be given the value of another variable, like this:

```
var foo, bar;
foo = 5;
bar = foo;
```

Notice that `foo` and `bar` are declared in the same statement. This is a convenience used to declare many variables at once. Also note that each statement ends with a semicolon; JavaScript doesn’t require this behavior but it’s a helpful convention that prevents ambiguity since it clearly marks the end of a statement. As statements get more complex, leaving out a semicolon may cause unintended consequences, so it’s best to include one at the end of each statement.

There are five primitive types in JavaScript, as shown in Table 1.

__Table 1__  Primitive types in JavaScript

| Type | Description |
| `number` | A numerical value, capable of handling integer and floating-point values |
| `boolean` | A logical value, either `true` or `false` |
| `string` | A sequence of characters |
| `null` | No value |
| `undefined` | An unknown value |

JavaScript freely converts between data types as needed. Consider this statement:

```
var x = 1 + "2";
```

JavaScript first promotes the number `1` to the string `"1"` and then assigns the newly concatenated string `"12"` to `x`.

If you want to do a numeric addition, you must use the parseInt function. For example:

```
var x = 1 + parseInt("2", 10);
```

The second parameter is a radix value, and is guessed based on the number if omitted following the same rules as a number in C. (Numbers starting with 0x are hex, other numbers starting with 0 are octal, and all other numbers are base 10.)

Anything that is not a primitive type is an object. Primitive types are promoted to objects as needed, like this:

```
var message = "Hello World";
var firstCharacter = message.charAt(0);
```

JavaScript promotes the string `"Hello World"` to an object in order to call the `charAt` member function.

JavaScript includes conditional statements where enclosed code runs only if its preceding statement evaluates to a Boolean `true` value. A typical conditional statement starts with the `if` keyword and is followed by a statement to test, like this:

```
if ( variable == true)
{
   // code to execute when this statement is true
}
```

As in most C-like languages, `true` is equivalent to the number one (`1`) and `false` is equivalent to the number zero (`0`).

Within the brackets `{ ... }`, you place the code to execute if the preceding statement is true. The statement itself needs to evaluate to a Boolean value, either `true` or `false`. Various operators are used to assemble conditional statements, as shown in Table 2.

__Table 2__  Conditional Operators

| Conditional Operator | Description |
| `==` | Returns `true` if both values are equal. Coerces values of different types before evaluating. |
| `===` | Returns `true` if both values are equal and of the same type. Returns `false` otherwise. |
| `!=` | Returns `true` if values are not equal. Coerces values of different types before evaluating |
| `!==` | Returns `true` if both values are not equal or not of the same type. Returns `false` otherwise. |
| `<` | Returns `true` if the left value is less than the right value. Returns `false` otherwise. |
| `<=` | Returns `true` if the left value is less than or equal to the right value. Returns `false` otherwise. |
| `>` | Returns `true` if the left value is greater than the right value. Returns `false` otherwise. |
| `>=` | Returns `true` if the left value is greater than or equal to the right value. Returns `false` otherwise. |

Each if statement can also have a corresponding else statement, where the enclosed code is executed when the if statement evaluates to false, like this:

```
if ( variable == true)
{
    // code to execute when this statement is true
}
else {
    // code to execute when this statement is false
}
```

When you want to check a value versus a number of values, a `switch` statement is useful. In a `switch` statement, you provide a conditional statement or variable and cases to match the statement’s outcome or variable’s value, like this:

```
switch ( variable ){
    case 1: // code to execute when variable equals 1
            break;
    case 2: // code to execute when variable equals 2
            break;
    default: // code to execute when variable equals something other than the cases
             break;
}
```

Note that each case ends with a break statement and that the `default` case, if provided, is called if none of the cases are matched.

JavaScript provides structures for looping code while a condition is true. The most basic looping structure is the `while` loop, which executes code while a conditional statement equals `true`:

```
while ( variable == true )
{
     // code to execute while variable is true
}
```

A variation on the while loop is the `do-while` loop, which executes its code at least once before checking its conditional statement, like this:

```
do
{
    // code to execute while variable is true
}
while ( variable == true );
```

The final loop type is the `for` loop. It uses three statements: an initialization statement, a conditional statement, and a iterative statement, called every time the loop completes. The most common pattern of use calls for the first statement to initialize a counter variable, the second to check the counter’s values, and the third to increment it, like this:

```
for ( var i = 0; i < variable; ++i )
{
    // code to execute within this loop
}
```


JavaScript allows you to wrap code into a function that you can reuse anywhere. To create a function, use the `function` keyword, provide a name, and include a list of any variables you want to pass in:

```
function myFunction ( variableOne, variableTwo )
{
    // code to execute within this function
}
```

Functions can be declared and used anywhere within a block of JavaScript code. Variables that contain primitive values are passed into a function by value, whereas objects are passed in by reference. Functions can optionally return a value using the `return` keyword:

```
function myFunction ( variableOne )
{
    // code to execute within this function
    return variableOne;
}
```

Functions implicitly return `undefined` if you don’t supply a return value.

Functions can also be assigned to a variable, like this:

```
var myFunctionVariable = function ( variable )
{
    // code to execute within this function
}
```

Once a function is defined within a variable, it can be passed as an argument into any other function. Within the receiving function, you can call that function by placing parentheses after the variable’s name and optionally including arguments, like this:

```
function myFunction ( myFunctionVariable )
{
    myFunctionVariable( "aString" );
}
```


As in most C-like languages, JavaScript has various characters that allow you to connect multiple statements in useful ways. This section describes a few of them.

The question mark and colon can be used in a comparison or calculation in the same way you would use an if-then-else statement in code. For example, suppose you want to increment or decrement the value of variable `Q`, depending on whether the value of the variable `increment` is true or false. You could write that code in either of two ways:

```
if (increment) { Q++; } else { Q--; }
// or
Q=increment ? Q+1 : Q-1;
```

These two statements are equivalent in every way. Overuse of this syntax can make code less readable, but moderate use can sometimes significantly clean up what would otherwise be deeply nested control statements or unnecessary duplication of large amounts of code.

For example, this syntax is often used for very simple conversion of numerical values to strings for output. The snippet below prints “yes” or “no” depending on whether the `increment` variable is set or not:

```
alert('Increment: '+(increment ? "yes" : "no"));
```


The comma separator is used to separate items in lists, such as function parameters, items in an array, and so on, and under some circumstances, can also be used to separate expressions.

When used to separate expressions, the comma separator instructs the interpreter to execute them in sequence. The result of the expression is the rightmost expression. This use of the comma is generally reserved for locations in your code where a semicolon has special meaning beyond separating statements.

For example, you use a semicolon to separate the parts of a C-style `for` loop as shown in this snippet:

```
for ( var i = 0; i < variable; ++i )
{
    // code to execute within this loop
}
```

If you need to increment multiple values at each stage of the loop, you could make your code harder to read by indexing one value off of the other (maybe) or by placing additional assignment statements prior to the start of the loop and as the last statement in the loop. However, this practice tends to make it harder to spot the loop iterator variables and thus makes the code harder to follow.

Instead, you should write the `for` loop as shown in this snippet, which displays an alert with five characters each, taken from different places in two strings:

```
var string = "The quick brown fox jumped over the lazy dog.";
var stringb = "This is a test.  This is only a test.";

for (var i=0, j=4; i<5; i++, j++) {
        alert('string['+i+'] = '+string[i]);
        alert('stringb['+j+'] = '+stringb[j]);
}
```

[Next](Object-Oriented%20JavaScript.md)[Previous](Introduction%20to%20Apple%20JavaScript%20Coding%20Guidelines.md)

