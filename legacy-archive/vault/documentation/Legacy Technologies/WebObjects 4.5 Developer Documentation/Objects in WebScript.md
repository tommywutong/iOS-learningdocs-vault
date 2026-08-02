---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WebScript1.html
archived_at: '2026-07-15T08:06:26.145044Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](The%20WebScript%20Language.md) [!Previous Section](The%20WebScript%20Language.md)

# Objects in WebScript

In WebScript, you work entirely with _objects_. An object is composed of data (called _instance variables_) and a set of actions that act upon that data (called _methods_). All variables that you declare are objects, and all values that a method returns are objects. There are no simple data types like __int__ or __char__ in C.
Each file that you write in WebScript defines an object. The definition of an object is called a _class_. A class specifies the instance variables that will be created for each object and the methods that the object will be able to perform. To create an object, you create an _instance_ of a class (or _instantiate_ a class).
For example, the following is a typical WebScript file.

```
id number, aName;

- awake {
     if (!number) {
        number = [[self application] visitorNum];
        number++;
        [[self application] setVisitorNum:number];
    }
    return self;
}

- recordMe {
    if ([aName length]) {
        [[self application] setLastVisitor:aName];
        [self setAName:@""]; // clear the text field
    }
}
```


Instance variables are declared at the top of the script file. In the example above, __number__ and __aName__ are instance variables of type __id__. An object's behavior is defined by its _methods_. __awake__ and __recordMe__ are examples of methods.
When you define a new class, you _subclass_ an existing class. Subclassing gives you access not only to the variables and methods that you explicitly define but also to the variables and methods defined for the existing class (called the _superclass_). As you learned in the chapter [""](What%20Is%20a%20WebObjects%20Application.md#apple-gezdmmjt), WebObjects applications can contain four kinds of script files: a component script inside a __.wo__ directory, an application script, a session script, and a direct action script. These four kinds of scripts create subclasses of the WebObjects classes WOComponent, WOApplication, WOSession, and WODirectAction, respectively. As you'll learn later, you can also subclass other classes in WebScript, but doing so is rare.

[!Table of Contents](The%20WebScript%20Language.md) [!Next Section](WebScript%20Language%20Elements.md)
