---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/WebScript/LanguageSummary.html
archived_at: '2026-07-15T07:48:01.413710Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.mif.book.md)
[!Previous Section](AccessingAndSharingVars.md)

# WebScript Language Summary

This section summarizes the WebScript language.

### Reserved Words

WebScript includes the following reserved words:

```
if
else
for
while
id
break
continue
nil
YES/NO
```

### Statements

WebScript supports the following statements:

```
if
else
for
while
break
continue
return
```

In WebScript these statements behave as they do in the C language.

### Arithmetic Operators

WebScript supports the arithmetic operators +, - , /, \*, and %. The rules of precedence in WebScript are the same as those for the C language. You can use these operators in compound statements such as:

```
b = (1.0 + 3.23546) + (((1.0 * 2.3445) + 0.45 + 0.65) - 3.2);
```

### Logical Operators

WebScript supports the negation (!), AND (&&), and OR (||) logical operators. You can use these operators as you would in the C language, for example:

```
if ( !(!a || a && !i) || (a && b) && (c || !a && (b+3)) ) i = 0;
```

### Relational Operators

WebScript supports the relational operators <, <=, >, >=, ==, and !=. In WebScript these operators behave as they do in C.

### Increment and Decrement Operators

WebScript supports the ++ and -- operators. These operators behave as they do in the C language, for example:

```
// Use myVar as the value of the expression and then increment myVar
myVar++;
// Increment myVar and then use its value as the value of the expression
++myVar;
```

### id

WebScript supports only one data type: objects (__id__s). The __id__ type is defined as a pointer to an object---in reality, a pointer to the object's data (its instance variables). Like a C function or an array, an object is identified by its address. All objects, regardless of their instance variables or methods, are of type __id__.

### self

In WebScript, __self__ is available in every method. It is a "hidden" variable that refers to the object (the WOApplication object, the WOSession object, or the WOComponent object) associated with a script. When you send a message to __self__, you're telling the object associated with the script to perform a method that's implemented in the script.

### super

As with __self__, __super__ is a "hidden" variable available in every method. By sending a message to __super__, you are invoking the superclass' implementation of the method. An invocation of __super__'s __init__ method should occur at the beginning of an __init__ implementation.

[!Table of Contents](WebScript.mif.book.md)
[!Next Section](NoteToObjCDev.md)
