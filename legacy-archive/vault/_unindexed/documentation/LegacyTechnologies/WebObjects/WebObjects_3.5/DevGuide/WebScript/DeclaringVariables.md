---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/WebScript/DeclaringVariables.html
archived_at: '2026-07-15T07:52:30.833813Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.md) [!Previous Section](WebScriptLanguage.md)

## Variables

To declare a variable in WebScript, use the syntax:

```
    id myVar;
    id myVar1, myVar2;
```


In these declarations, __id__ is a data type. The __id__ type is a reference to any object-in reality, a pointer to the object's data (its instance variables). Like a C function or an array, an object is identified by its address; thus, all variables declared in WebScript are pointers to objects. In the examples above, __myVar1__ and __myVar2__ could be any object: a string, an array, or a custom object from your application.
__Note:__  Unlike C, no pointer manipulation is allowed in WebScript.
Instead of using __id__, you can specifically refer to the class you want to instantiate using this syntax:

```
    className *variableName;
```


For example, you could specify that a variable is an NSString object using this syntax:

```
    NSString *myString1;
    NSString *myString1, *myString2;
```


For more information on specifying class names in variable declarations, see the section ["Data Types"](DataTypes.md#apple-gy3dsmi).

In WebScript, there are two basic kinds of variables: local variables and instance variables. You declare instance variables at the top of the file, and you declare local variables at the beginning of a method or at the beginning of a block construct (such as a __while__ loop). The following shows where variables can be declared:

```
    id instanceVariable; // An instance variable for this class.

    - aMethod {
        id localVariable1; // A local variable for this method.

        while (1) {
            NSString *localVariable2; // A local variable for this block.
        }
    }
```


### Variables and Scope

Each kind of variable has a different scope and a different lifetime. Local variables are only visible inside the block of text in which they are declared. In the example above, __localVariable1__ is declared at the top of a method. It is accessible within the entire body of that method, including the __while__ loop. It is created upon entry into the method and released upon exit. __localVariable2__, on the other hand, is declared in the __while__ loop construct. You can only access it within the curly braces for the __while__ loop, not within the rest of the method.
The scope of an instance variable is object-wide. That means that any method in the object can access any instance variable. You can't directly access an instance variable outside of the object that owns it; you must use an accessor method instead. See ["Accessor Methods"](AccessorMethods.md#apple-gyztmny).

The lifetime of an instance variable is the same as the lifetime of the object. When the object is created, all of its instance variables are created as well and their values persist throughout the life of the object. Instance variables are not freed until the object is freed.
As you learned in the chapter ["Common Methods"](../CommonMethods/CommonMethods.md#apple-gyytknq), a WOApplication is created when you started a WebObjects application, a WOSession is created each time a different user accesses that application, and a WOComponent is created the first time a user accesses that page in the application. Thus, the variables you declare at the top of the application script (__Application.wos__) exist as long as the application is running. The variables you declare at the top of the session script (__Session.wos__) exist for the length of one session. As new users access your application, new sessions are created, so new copies of the session's instance variables are created too. These copies of instance variables are private to each session; one session does not know about the instance variables of another session. As sessions expire, their instance variables are freed. Finally, the variables you declare at the top of a component script are created and released as that component is created and released.

__Note:__  Just how often a particular component object is created depends on whether the application object is caching pages. For more information, see ["WebObjects Viewed Through Its Classes"](../HowWOWorks/HowWOWorks.md#apple-gy3a).

### Assigning Values to Variables

You assign values to variables using the following syntax:

```
    myVar = aValue;
```


A value can be assigned to a variable at the time it is declared or after it is declared. For example:

```
    NSNumber *myVar1;
    id myVar2 = 77;

    myVar1 = 76;
```


The value you assign to a variable can be either a constant or another variable. For example:

```
    // assign another variable to a variable
    myVar = anotherVar;
    // assign a string constant to a variable
    myString = @"This is my string.";
```


__Note:__  The // syntax denotes a comment.
You can assign constant values to objects of four of the most commonly used classes in WebScript: NSNumber, NSString, NSArray, and NSDictionary. These classes are defined in the Foundation framework. To learn how to initialize objects of all other classes, see ["Creating Instances of Classes"](CreatingObjects.md#apple-gq4dgni) in this chapter.

NSNumber is the easiest class to initialize. You just assign a number to the variable, like this:

```
    NSNumber *myNumber = 77;
```


For the remaining three classes, WebScript provides a convenient syntax for initializing constant objects. In such an assignment statement, the value you're assigning to the constant object is preceded by an at sign (@). You use parentheses to enclose the elements of an NSArray and curly braces to enclose the key-value pairs of an NSDictionary. The following are examples of how you use this syntax to assign values to constant NSString, NSArray, and NSDictionary objects in WebScript:

```
    myString = @"hello world";
    myArray = @("hello", "goodbye");
    myDictionary = @{"key" = 16};
    anotherArray = @(1, 2, 3, "hello");
    aDict = @{ "a" = 1; "b" = "hello world"; "c" = (1,2,3);
            "d" = { "x" = 1; "r" = 2 }};
```


The following rules apply when you use this syntax to create constant objects:

- The value you assign must be a constant (that is, it can't include variables). For example, the following is not allowed:

```
    // This is not allowed!!
    myArray = @("hello", aVariable);
```

- You shouldn't use @ to identify an NSString, NSArray, or NSDictionary inside the value being assigned. For example:

```
    // This is not allowed!!
    myDictionary = @(@"value" = 3);

    // Do this instead
    myDictionary = @("value" = 3);
```


For more information on NSNumber, NSString, NSDictionary, and NSArray, see the chapter ["WebScript Programmer's Quick Reference to Foundation Classes"](../Foundation/FoundationTOC.md#apple-gq4to).

[!Table of Contents](WebScript.md) [!Next Section](WritingOwnMethods.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
