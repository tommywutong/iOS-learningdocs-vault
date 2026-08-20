---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WebScript12.html
archived_at: '2026-07-15T08:06:27.677540Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](The%20WebScript%20Language.md) [!Previous Section](WebScript11.md)

## Statements and Operators

WebScript supports most of the same statements and operators that C supports, and they work in much the same way. This section describes only the differences between statements and operators in C and statements and operators in WebScript.

### Control Flow Statements

WebScript supports the following control-flow statements:

```
if
else
for
while
break
continue
return
```


### Arithmetic Operators

WebScript supports the arithmetic operators +, - , /, \*, and %. The rules of precedence in WebScript are the same as those for the C language. You can use these operators in compound statements such as:

```
b = (1.0 + 3.23546) + (((1.0 * 2.3445) + 0.45 + 0.65) -
3.2);
```


### Logical Operators

WebScript supports the negation (!), AND (&&), and OR (||) logical operators. For the most part, you can use these operators as you would in the C language, for example:

```
if ( !(!a || a && !i) || (a && b) && (c || !a && (b+3)) )
i = 0;
```


As in C, Boolean expressions _short-circuit_. For example, in this statement:

```
(!a || (a && !i))
```


The expression is only evaluated up to the point where the outcome can be surmised. That is, if __!a__ is true, the other side of the || expression is not evaluated because the || operator only requires one side of the statement to be true. Likewise, if the && statement is evaluated and __a__ is false, the second half of the && expression is not evaluated because the && operator does require both sides to be true.

### Relational Operators

WebScript supports the relational operators <, <=, >, >=, ==, and !=. In WebScript these operators behave as they do in C.
In WebScript, relational operators are only reliable on NSNumbers. If you try to use them on any other class of object, you may not receive the results you expect.
For example, the following statement compares the addresses stored in the two string variables. If both point to the same address, the strings are equal. If they point to different addresses, even if the strings have identical contents, the statement will be false.

```
NSString *string1, *string2;
if (string1 == string2) // compares pointer values.
```


To compare two strings, or two of any other type of object, use the __isEqual:__ method.

```
NSString *string1, *string2;
if ([string1 isEqual:string2]) // compares values of
objects
```


__Note:__  The == operator may fool you at times by appearing to test equality of objects other than NSNumbers. This is because constant values are uniqued within a script file. That is, if you do the following, WebScript stores the constant string objects in one location and has both variables point to the same string constant.

```
NSString *string1 = @"This is a string";
NSString *string2 = @"This is a string";
```


If you compare these two variables, it may appear that WebScript compares the values they point at, but in reality, it is testing the pointer addresses.

```
NSString *string1 = @"This is a string";
NSString *string2 = @"This is a string";

if (string1 == string2) {
    //This code gets executed because string1 and string2
    //point to the same memory address.

if ([string1 isEqual:string2])
    //This code gets executed because string1 and string2
    //have the same contents.
```


### Increment and Decrement Operators

WebScript supports the preincrement (++) and predecrement (--) operators. These operators behave as they do in the C language, for example:

```
// Increment myVar and then use its value
// as the value of the expression
++myVar;
```


The postincrement and postdecrement operators are not supported. They behave like the preincrement and predecrement operators. For example:

```
// WATCH OUT!! Probably not what you want.
i = 0;
while (i++ < 1) {
    //this loop never gets executed because i++ is a
preincrement.
}
```

[!Table of Contents](The%20WebScript%20Language.md) [!Next Section](WebScript13.md)
