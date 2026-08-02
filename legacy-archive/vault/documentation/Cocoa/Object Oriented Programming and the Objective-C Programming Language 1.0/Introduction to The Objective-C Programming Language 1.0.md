---
title: Object Oriented Programming and the Objective-C Programming Language 1.0
apple_id: TP40005191
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-06-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OOPandObjC1/Introduction/introObjectiveC.html
archived_at: '2026-07-15T07:17:28.407897Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](The%20Language.md)

# Introduction to The Objective-C Programming Language 1.0

An object-oriented approach to application development makes programs more intuitive to design, faster to develop, more amenable to modification, and easier to understand. Most object-oriented development environments consist of at least three parts:

- An object-oriented programming language and support library
- A library of objects
- A set of development tools

This document is about the first component of the development environment—the programming language and its runtime environment. It fully describes the Objective-C language, and provides a foundation for learning about the second component, the Mac OS X Objective-C application frameworks—collectively known as Cocoa. You can start to learn more about Cocoa by reading _Getting Started with Cocoa_. The two main development tools you use are Xcode and Interface Builder, described in _[Xcode 2.0 User Guide](../../Developer%20Tools/Xcode%202.0%20User%20Guide/Introduction%20to%20Xcode%202.0%20User%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbq)_ and _[Interface Builder](../../Developer%20Tools/Interface%20Builder/Introduction%20to%20Interface%20Builder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3ts2i)_ respectively.

The Objective-C language is a simple computer language designed to enable sophisticated object-oriented programming. Objective-C is defined as small but powerful set of extensions to the standard ANSI C language. Its additions to C are mostly based on Smalltalk, one of the first object-oriented programming languages. Objective-C is designed to give C full object-oriented programming capabilities, and to do so in a simple and straightforward way.

For those who have never used object-oriented programming to create applications before, this document is also designed to help you become familiar with object-oriented development. It spells out some of the implications of object-oriented design and gives you a flavor of what writing an object-oriented program is really like.

The document is intended for readers who might be interested in:

- Learning about object-oriented programming
- Finding out about the basis for the Cocoa application framework
- Programming in Objective-C

This document both introduces the object-oriented model that Objective-C is based upon and fully documents the language. It concentrates on the Objective-C extensions to C, not on the C language itself.

Because this isn’t a document about C, it assumes some prior acquaintance with that language. However, it doesn’t have to be an extensive acquaintance. Object-oriented programming in Objective-C is sufficiently different from procedural programming in ANSI C that you won’t be hampered if you’re not an experienced C programmer.

This document is divided into four chapters and two appendixes. The chapters are:

- [The Language](The%20Language.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnznijauuq2kifbei) describes the basic concepts and syntax of Objective-C. It covers many of the same topics as Object-Oriented Programming, but looks at them from the standpoint of the Objective-C language. It reintroduces the terminology of object-oriented programming, but in the context of Objective-C.
- [The Runtime System](The%20Runtime%20System.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqojninfeeqscineeo) looks at the NSObject class and how Objective-C programs interact with the runtime system. In particular, it examines the paradigms for managing object allocations, dynamically loading new classes at runtime, and forwarding messages to other objects.

The appendixes contain reference material that might be useful for understanding the language. They are:

- [Language Summary](Language%20Summary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqmznknltc) lists and briefly comments on all of the Objective-C extensions to the C language.
- [Grammar](Grammar.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojrfvbuqnbnijbusq2gi5eui) presents, without comment, a formal grammar of the Objective-C extensions to the C language. This reference manual is meant to be read as a companion to the reference manual for C presented in _The C Programming Language_ by Brian W. Kernighan and Dennis M. Ritchie, published by Prentice Hall.

Where this document discusses functions, methods, and other programming elements, it makes special use of computer voice and italic fonts. Computer voice denotes words or characters that are to be taken literally (typed as they appear). Italic denotes words that represent something else or can be varied. For example, the syntax:

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

The conventions used in the reference appendix are described in that appendix.

_[Objective-C 2.0 Runtime Reference](https://developer.apple.com/documentation/objectivec/objective_c_runtime)_ describes the data structures and functions of the Objective-C runtime support library. Your programs can use these interfaces to interact with the Objective-C runtime system. For example, you can add classes or methods, or obtain a list of all class definitions for loaded classes.

[Next](The%20Language.md)

