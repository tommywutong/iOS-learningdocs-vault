---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Methods6.html
archived_at: '2026-07-15T08:05:57.618324Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Common%20Methods.md) [!Previous Section](Methods5.md)

# Initialization and Deallocation Methods

Like all objects, WOApplication, WOSession, and WOComponent implement initialization methods (or constructors in Java). Because most subclasses require some unique initialization code, these are the methods that you override most frequently. In WebScript, the initialization method is named __init__. In Java, the initialization method is the constructor for the class.
Complementing __init__ is the __dealloc__ method. This method lets objects deallocate their instance variables and perform other clean-up tasks. The __dealloc__ method is used primarily for Objective-C objects. Standard __dealloc__ methods in Objective-C send each instance variable a __release__ message to make sure that the instance variables are freed. WebScript and Java, because they have automatic garbage collection, usually make a deallocation method unnecessary. If you find it necessary, you can implement __dealloc__ in WebScript and __finalize__ in Java.

[!Table of Contents](Common%20Methods.md) [!Next Section](Methods7.md)
