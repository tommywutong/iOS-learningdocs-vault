---
title: Core Foundation Design Concepts
apple_id: 10000122i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: General
technology: CoreFoundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/CFDesignConcepts.html
archived_at: '2026-07-15T07:22:26.702289Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Opaque%20Types.md)

# Introduction to Core Foundation Design Concepts

Core Foundation is a library with a set of programming interfaces conceptually derived from the [Objective-C](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectiveC.html#//apple_ref/doc/uid/TP40008195-CH43)-based Foundation [framework](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56) but implemented in the C language. To do this, Core Foundation implements a limited object model in C. Core Foundation defines opaque types that encapsulate data and functions, hereafter referred to as “objects.”

The programming interfaces of Core Foundation objects have been designed for ease of use and reuse. At a general level, Core Foundation:

- Enables sharing of code and data among various frameworks and libraries
- Makes some degree of operating-system independence possible
- Supports internationalization with Unicode strings
- Provides common API and other useful capabilities, including a plug-in architecture, XML property lists, and preferences

Core Foundation makes it possible for the different frameworks and libraries on OS X to share code and data. Applications, libraries, and frameworks can define C routines that incorporate Core Foundation types in their external interfaces; they can thus communicate data—as Core Foundation objects—to each other through these interfaces.

Core Foundation also provides “toll-free bridging” between certain services and the Cocoa’s Foundation framework. Toll-free bridging enables you to substitute Cocoa objects for Core Foundation objects in function parameters and vice versa.

Some Core Foundation types and functions are abstractions of things that have specific implementations on different operating systems. Code that makes use of these APIs is thus easier to port to different platforms.

Date and number types abstract time utilities and offers facilities for converting between absolute and Gregorian measures of time. It also abstracts numeric values and provides facilities for converting between different internal representations of those values.

One of the major benefits Core Foundation brings to application development is internationalization support. Through its String objects, Core Foundation facilitates easy, robust, and consistent internationalization across all OS X and Cocoa programming interfaces and implementations. The essential part of this support is a type, CFString, instances of which represent an array of 16-bit Unicode characters. A CFString object is flexible enough to hold megabytes worth of characters and yet simple and low-level enough for use in all programming interfaces communicating character data. It accomplishes this with performance not much different than that associated with standard C strings.

You should read this document to learn about the fundamental design principles that underly Core Foundation, and how Core Foundation objects interact with [Cocoa (Touch)](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Cocoa.html#//apple_ref/doc/uid/TP40008195-CH9) objects.

These concepts and tasks discuss the object model used in Core Foundation:

- [Opaque Types](Opaque%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeydmlkdjjbeksscjbea)
- [Object References](Object%20References.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeydolkdjjbeksscjbea)
- [Polymorphic Functions](Polymorphic%20Functions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeydqlkdjjbeksscjbea)
- [Varieties of Objects](Varieties%20of%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeydslkdjjbeksscjbea)
- [Comparing Objects](Comparing%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeytelkdjjbekscbifdq)
- [Inspecting Objects](Inspecting%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeytglkdjjbekscbifdq)

In addition, there are other non-object types, and API conventions that you should be familiar with before using Core Foundation:

- [Naming Conventions](Naming%20Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeytalkdjjbeksscjbea)
- [Other Types](Other%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgeytclkdjjbeksscjbea)
- [Toll-Free Bridged Types](Toll-Free%20Bridged%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzxfvjvomi)

[Next](Opaque%20Types.md)

