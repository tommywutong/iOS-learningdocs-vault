---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WebScript3.html
archived_at: '2026-07-15T08:06:34.719771Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](The%20WebScript%20Language.md) [!Previous Section](WebScript%20Language%20Elements.md)

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
NSString *myString2, *myString3;
```


For more information on specifying class names in variable declarations, see the section ["Data Types"](WebScript11.md#apple-gy3dsmi).

In WebScript, there are two basic kinds of variables: local variables and instance variables. You declare instance variables at the top of the file, and you declare local variables at the beginning of a method or at the beginning of a block construct (such as a __while__ loop). The following shows where variables can be declared:

```
id instanceVariable; // An instance variable for this
class.

- aMethod {
    id localVariable1; // A local variable for this method.

    while (1) {
        NSString *localVariable2; // A local variable for
this block.
    }
}
```

[!Table of Contents](The%20WebScript%20Language.md) [!Next Section](WebScript4.md)
