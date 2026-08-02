---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/CommonMethods/InitializationMethods.html
archived_at: '2026-07-15T07:51:15.559609Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](CommonMethods.md) [!Previous Section](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/CommonMethods/ActionsMethods.html)

# Initialization and Deallocation Methods

Like all objects, WOApplication, WOSession, and WOComponent implement initialization methods (or constructors in Java). Because most subclasses require some unique initialization code, these are the methods that you override most frequently. In WebScript, the initialization methods are __init__ and __awake__. In Java, the initialization methods are the constructor for the class and __awake__.
Both __init__ and __awake__ perform initialization tasks, but they are invoked at different times during an object's life. The __init__ message (or the constructor in Java) is sent once, when the object is first created. In contrast, __awake__ is sent at the beginning of each cycle of the request-response loop that the object is involved in. Thus, it may be sent several times during an object's life.
Complementing __awake__ and __init__ are the __sleep__ and __dealloc__ methods. These methods let objects deallocate their instance variables and perform other clean-up tasks. The __sleep__ method is invoked at the end of each cycle of the request-response loop, whereas the __dealloc__ method is invoked at the end of the object's life.
The __dealloc__ method is used primarily for Objective-C objects. Standard __dealloc__ methods in Objective-C send each instance variable a __release__ message to make sure that the instance variables are freed. WebScript and Java, because they have automatic garbage collection, usually make a deallocation method unnecessary. If you find it necessary, you can implement __dealloc__ in WebScript and __finalize__ in Java.

[!Table of Contents](CommonMethods.md) [!Next Section](StructureOfInitAwake.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
