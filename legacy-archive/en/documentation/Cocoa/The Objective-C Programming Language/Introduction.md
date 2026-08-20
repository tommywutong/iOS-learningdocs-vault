---
title: The Objective-C Programming Language
apple_id: TP30001163
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Introduction/introObjectiveC.html
archived_at: '2026-07-15T07:17:31.942122Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Objects%2C%20Classes%2C%20and%20Messaging.md)

# Introduction

The Objective-C language is a simple computer language designed to enable sophisticated object-oriented programming. Objective-C is defined as a small but powerful set of extensions to the standard ANSI C language. Its additions to C are mostly based on Smalltalk, one of the first object-oriented programming languages. Objective-C is designed to give C full object-oriented programming capabilities, and to do so in a simple and straightforward way.

Most object-oriented development environments consist of several parts:

- An object-oriented programming language
- A library of objects
- A suite of development tools
- A runtime environment

This document is about the first component of the development environment—the programming language. This document also provides a foundation for learning about the second component, the Objective-C application [frameworks](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56)—collectively known as _Cocoa_. The runtime environment is described in a separate document, _[Objective-C Runtime Programming Guide](../Objective-C%20Runtime%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danby)_.

The document is intended for readers who might be interested in:

- Programming in Objective-C
- Finding out about the basis for the Cocoa application frameworks

This document both introduces the object-oriented model that Objective-C is based upon and fully documents the language. It concentrates on the Objective-C extensions to C, not on the C language itself.

Because this isn’t a document about C, it assumes some prior acquaintance with that language. Object-oriented programming in Objective-C is, however, sufficiently different from _procedural programming_ in ANSI C that you won’t be hampered if you’re not an experienced C programmer.

The following chapters cover all the features Objective-C adds to standard C.

- [Objects, Classes, and Messaging](Objects%2C%20Classes%2C%20and%20Messaging.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjrfvjvomi)
- [Defining a Class](Defining%20a%20Class.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjsfvjvomi)
- [Protocols](Protocols.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjvfvjvomi)
- [Declared Properties](Declared%20Properties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjxfvjvomi)
- [Categories and Extensions](Categories%20and%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmrqfvjvomi)
- [Associative References](Associative%20References.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmrufvjvomi)
- [Fast Enumeration](Fast%20Enumeration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjyfvjvomi)
- [Enabling Static Behavior](Enabling%20Static%20Behavior.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjwfvjvomi)
- [Selectors](Selectors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmrtfvjvomi)
- [Exception Handling](Exception%20Handling.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjtfvjvomi)
- [Threading](Threading.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjzfvjvomi)

A glossary at the end of this document provides definitions of terms specific to Objective-C and object-oriented programming.

This document makes special use of computer voice and italic fonts. Computer voice denotes words or characters that are to be taken literally (typed as they appear). Italic denotes words that represent something else or can be varied. For example, the syntax:

`@interface`_ClassName_`(`_CategoryName_`)`

means that `@interface` and the two parentheses are required, but that you can choose the class name and category name.

Where example code is shown, ellipsis points indicates the parts, often substantial parts, that have been omitted:

```objc
- (void)encodeWithCoder:(NSCoder *)coder
{
    [super encodeWithCoder:coder];
    ...
}
```


If you have never used object-oriented programming to create applications, you should read _[Object-Oriented Programming with Objective-C](../Object-Oriented%20Programming%20with%20Objective-C/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcnbz)_. You should also consider reading it if you have used other object-oriented development environments such as C++ and Java because they have many expectations and conventions different from those of Objective-C. _[Object-Oriented Programming with Objective-C](../Object-Oriented%20Programming%20with%20Objective-C/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcnbz)_ is designed to help you become familiar with object-oriented development from the perspective of an Objective-C developer. It spells out some of the implications of object-oriented design and gives you a flavor of what writing an object-oriented program is really like.

_[Objective-C Runtime Programming Guide](../Objective-C%20Runtime%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danby)_ describes aspects of the Objective-C runtime and how you can use it.

_[Objective-C Runtime Reference](https://developer.apple.com/documentation/objectivec/objective_c_runtime)_ describes the data structures and functions of the Objective-C runtime support library. Your programs can use these interfaces to interact with the Objective-C runtime system. For example, you can add classes or methods, or obtain a list of all class definitions for loaded classes.

Objective-C supports three mechanisms for memory management: automatic garbage collection and reference counting:

- _Automatic Reference Counting_ (ARC), where the compiler reasons about the lifetimes of objects.
- _Manual Reference Counting_ (MRC, sometimes referred to as MRR for “manual retain/release”), where you are ultimately responsible for determining the lifetime of objects.

  Manual reference counting is described in _[Advanced Memory Management Programming Guide](../Advanced%20Memory%20Management%20Programming%20Guide/About%20Memory%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaytc2i)_.
- _Garbage collection_, where you pass responsibility for determining the lifetime of objects to an automatic “collector.”

  Garbage collection is described in _[Garbage Collection Programming Guide](../Garbage%20Collection%20Programming%20Guide/Introduction%20to%20Garbage%20Collection.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimzr)_. (Not available for iOS—you cannot access this document through the iOS Dev Center.)

[Next](Objects%2C%20Classes%2C%20and%20Messaging.md)

