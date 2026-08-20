---
title: Apple JavaScript Coding Guidelines
apple_id: TP40006088
resource_type: Guide
platform: Safari|macOS
topic: Languages & Utilities
technology: null
published: '2011-07-10'
source_url: https://developer.apple.com/library/archive/documentation/ScriptingAutomation/Conceptual/JSCodingGuide/OOJavaScript/OOJavaScript.html
archived_at: '2026-07-18T02:05:35.980978Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Apple JavaScript Coding Guidelines](Introduction%20to%20Apple%20JavaScript%20Coding%20Guidelines.md)


[Next](JavaScript%20Best%20Practices.md)[Previous](JavaScript%20Basics.md)

# Object-Oriented JavaScript

JavaScript code doesn’t necessarily follow object-oriented design patterns. However, the JavaScript language provides support for common object-oriented conventions, like constructors and inheritance, and benefits from using these principles by being easier to maintain and reuse.

Read this chapter if you’re already familiar with object-oriented programming and want to see how to create object-oriented code with JavaScript.

JavaScript provides the ability to create objects that contain member variables and functions. To define a new object, first create a new function with the desired object’s name, like this:

```
function MyObject()
{
    // constructor code goes here
}
```

This function works as the object’s constructor, setting up any variables needed by the object and handling any initializer values passed in as arguments. Within the constructor or any member function, persistent instance variables are created by adding them to the `this` keyword and providing the variable with a value, like this:

```
this.myVariable = 5;
```

To create a new member function, create a new anonymous function and assign it to the prototype property of the object. For example:

```
MyObject.prototype.memberMethod = function()
{
    // code to execute within this method
}
```

After you have created the constructor for your object, you can create new object instances by using the `new` keyword followed by a call to the constructor function. For example:

```
var myObjectVariable = new MyObject();
```

This particular constructor takes no parameters. However, you can also create more complex constructors for classes that allow you to specify commonly used or mandatory initial values. For example:

```
function MyObject(bar)
{
        this.bar = bar;
}

myobj = new MyObject(3);
alert('myobj.bar is '+myobj.bar); // prints 3.
```

One common use of this technique is to create initializers that duplicate the contents of an existing object. This is described further in [Copying an Object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmzzfvjvomy).

Just as you used the `new` operator to create an object, you should delete objects when you are finished with them, like this:

```
delete myObjectVariable;
```

The JavaScript runtime automatically garbage collects objects when their value is set to `null`. However, setting an object to `null` doesn’t remove the variable that references the object from memory. Using `delete` ensures that this memory is reclaimed in addition to the memory used by the object itself.

JavaScript provides arrays for collecting data. Since an array is an object, you need to create a new instance of an array before using it, like this:

```
var myArray = new Array();
```

Alternatively, you can use this simpler syntax:

```
var myArray = [];
```

Once you create an array, you reference elements using integer values inside of brackets, like this:

```
myArray[0] = "first value";
myArray[1] = 5;
```

The previous example shows that arrays, like variables, can hold data of any type.

Generic objects and arrays can be used with associative properties, where strings replace the index number:

```
myObject["indexOne"] = "first value";
myObject["indexTwo"] = 5;
```

When you use a string as an index, you can use a period instead of brackets to access and assign data to that property:

```
myObject.name = "Apple Inc.";
myObject.city = "Cupertino";
```

You can declare an object and its contents inline, as well:

```
myObject = {
    name: "Apple Inc.",
    city: "Cupertino"
}
```

A variation of the `for` loop is available for iterating within the properties of an array or object. Called a `for-in` loop, it looks like this:

```
for ( var index in myArray )
{
    // code to execute within this loop
}
```


Recent WebKit builds (available from webkit.org) contain support for getter and setter functions. These functions behave like a variable but really call a function to change any underlying values that make a property. Declaring a getter looks like this:

```
MyObject.__defineGetter__( "myGetter", function() { return this.myVariable; } );
```

It is essential that a getter function return a value because, when used, the returned value is used in an assignment operation like this:

```
var someVariable = MyObject.myGetter;
```

Like a getter, a setter is defined on an object and provides a keyword and a function:

```
MyObject.__defineSetter__( "mySetter", function(aValue) { this.myVariable = aValue; } );
```

Note that setter functions need to take an argument that’s used in an assignment statement, like this:

```
MyObject.mySetter = someVariable;
```


JavaScript allows an object to inherit from other objects via the `prototype` keyword. To inherit from another object, set your object’s prototype equal to the prototype of the parent object, like this:

```
MyChildObject.prototype = MyParentObject.prototype;
```

This copies all of the parent’s functions and variables to your object. It does _not_, however, copy the default values stored in that object. If your purpose is to subclass an object completely, you must also execute code equivalent to the original constructor or construct an instance of the original type and copy its values as described in [Copying an Object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dkmzzfvjvomy).

Recent WebKit builds also include the ability to extend an existing DOM object via the `prototype` keyword. The advantage of this over inheritance is a smaller memory footprint and easier function overloading.

In object-oriented programming, you often need to make a copy of an object. The most straightforward (but painful) way to do this is to methodically copy each value by hand. For example:

```
function MyObjectCopy(oldobj)
{
        // copy values one at a time
        this.bar = oldobj.bar;
}
```

For very simple objects, explicit copying is fine. However, as objects grow larger, this technique can become unmanageable, particularly if additional variables are added to an object outside the constructor. Fortunately, because a JavaScript object is essentially an associative array, you can manipulate it just as you would an array. For example:

```
function MyObjectCopy(oldobj)
{
        // copy values with an iterator
        for (myvar in oldobj) {
                this[myvar] = oldobj[myvar];
        }
}
```

You should be aware, however, that assigning an object to a variable merely stores a reference to that object, not a copy of that object, and thus any objects stored within this object will not be copied by the above code.

If you need to perform a deep copy of a structured tree of data, you should explicitly call a function to copy the nested objects. The easiest way to do this is to include a `clone` function in each class, test each variable to see if it contains an object with a clone function, and call that function if it exists. For example:

```
// Create an inner object with a variable x whose default
// value is 3.
function InnerObj()
{
        this.x = 3;
}
InnerObj.prototype.clone = function() {
    var temp = new InnerObj();
    for (myvar in this) {
        // this object does not contain any objects, so
        // use the lightweight copy code.
        temp[myvar] = this[myvar];
    }
    return temp;
}

// Create an outer object with a variable y whose default
// value is 77.
function OuterObj()
{
        // The outer object contains an inner object.  Allocate it here.
        this.inner = new InnerObj();
        this.y = 77;
}
OuterObj.prototype.clone = function() {
    var temp = new OuterObj();
    for (myvar in this) {
        if (this[myvar].clone) {
            // This variable contains an object with a
            // clone operator.  Call it to create a copy.
            temp[myvar] = this[myvar].clone();
        } else {
            // This variable contains a scalar value,
            // a string value, or an object with no
            // clone function.  Assign it directly.
            temp[myvar] = this[myvar];
        }
    }
    return temp;
}

// Allocate an outer object and assign non-default values to variables in
// both the outer and inner objects.
outer = new OuterObj;
outer.inner.x = 4;
outer.y = 16;

// Clone the outer object (which, in turn, clones the inner object).
newouter = outer.clone();

// Verify that both values were copied.
alert('inner x is '+newouter.inner.x); // prints 4
alert('y is '+newouter.y); // prints 16
```

[Next](JavaScript%20Best%20Practices.md)[Previous](JavaScript%20Basics.md)

