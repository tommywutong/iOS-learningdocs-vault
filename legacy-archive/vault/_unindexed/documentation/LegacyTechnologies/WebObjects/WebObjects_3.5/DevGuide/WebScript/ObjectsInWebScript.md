---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/WebScript/ObjectsInWebScript.html
archived_at: '2026-07-15T07:52:33.247994Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.md) [!Previous Section](WebScript.md)

# Objects in WebScript

In WebScript, you work entirely with _objects_. An object is composed of data (called _instance variables_) and a set of actions that act upon that data (called _methods_). All variables that you declare are objects, and all values that a method returns are objects. There are no simple data types like __int__ or
__char__ in C.
Each file that you write in WebScript defines an object. The definition of an object is called a _class_. A class specifies the instance variables that will be created for each object and the methods that the object will be able to perform. To create an object, you create an _instance_ of a class (or _instantiate_ a class).
For example, the following is a typical WebScript file. (This is actually the script file for the Visitors example's Main component. You can look at the entire Visitors example in <DocRoot>__/WebObjects/Examples/WebScript/Visitors.woa__.)

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


Instance variables are declared at the top of the script file. In the example above, __number__ and __aName__ are instance variables. An object's behavior is defined by its _methods_. __awake__ and __recordMe__ are examples of methods.
When you define a new class, you _subclass_ an existing class. Subclassing gives you access not only to the variables and methods that you explicitly define but also to the variables and methods defined for the existing class (called the _superclass_). As you learned in the chapter ["What Is a WebObjects Application?"](../WhatIsWOApp/WhatIsWOApp.md#apple-giydioa), WebObjects applications can contain three kinds of script files: a component script inside a __.wo__ directory, an application script, and a session script. These three kinds of scripts create subclasses of the WebObjects classes WOComponent, WOApplication, and WOSession, respectively. As you'll learn later, you can also subclass other classes in WebScript, but doing so is rare.

[!Table of Contents](WebScript.md) [!Next Section](WebScriptLanguage.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
