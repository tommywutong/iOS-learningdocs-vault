---
title: Object-Oriented Programming with Objective-C
apple_id: TP40005149
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2010-11-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OOP_ObjC/Introduction/Introduction.html
archived_at: '2026-07-15T07:17:21.858374Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Why%20Objective-C.md)

# Introduction

An object-oriented approach to application development makes programs more intuitive to design, faster to develop, more amenable to modification, and easier to understand. Most object-oriented development environments consist of at least three parts:

- A library of objects
- A set of development tools
- An object-oriented programming language and support library

The Objective-C language is a programming language designed to enable sophisticated object-oriented programming. Objective-C is defined as a small but powerful set of extensions to the standard ANSI C language. Its additions to C are mostly based on Smalltalk, one of the first object-oriented programming languages. Objective-C is designed to give C full object-oriented programming capabilities and to do so in a simple and straightforward way.

Every object-oriented programming language and environment has a different perspective on what _object-oriented_ means, how objects behave, and how programs might be structured. This document offers the Objective-C perspective.

For those who have never used object-oriented programming to create applications, this document is designed to help you become familiar with object-oriented development. It spells out some of the implications of object-oriented design and gives you a flavor of what writing an object-oriented program is really like.

If you have developed applications using an object-oriented environment, this document will help you understand the fundamental concepts that are essential to understanding how to use Objective-C effectively and how to structure a program that uses Objective-C.

Because this isn’t a document about C, it assumes some prior acquaintance with that language. However, it doesn’t have to be an extensive acquaintance. Object-oriented programming in Objective-C is sufficiently different from procedural programming in ANSI C that you won’t be hampered if you’re not an experienced C programmer.

This document is divided into several chapters:

- [Why Objective-C?](Why%20Objective-C.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcnbzfvbuqmznknltc) explains why Objective-C was chosen as the development language for the Cocoa frameworks.
- [Object-Oriented Programming](Object-Oriented%20Programming.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcnbzfvbuqobnknltc) discusses the rationale for object-oriented programming languages and introduces much of the terminology. It develops the ideas behind object-oriented programming techniques. Even if you’re already familiar with object-oriented programming, you are encouraged to read this chapter to gain a sense of the Objective-C perspective on object orientation and its use of terminology.
- [The Object Model](The%20Object%20Model.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcnbzfvbuqnjnknlti) describes how you can think of a program in terms of units that combine state and behavior—objects. It then explains how you characterize these objects as belonging to a particular class, how one class can inherit state and behavior from another class, and how objects can send messages to other objects.
- [Structuring Programs](Structuring%20Programs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcnbzfvbuqnbnknlte) explains how you think about designing an object-oriented program by creating connections between objects. It introduces the techniques of aggregation and decomposition, which divide responsibility between different sorts of object, and the role of frameworks in defining libraries of objects designed to work together.
- [Structuring the Programming Task](Structuring%20the%20Programming%20Task.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcnbzfvbuqnrnknltc) discusses issues of project management related to collaboration among programmers and to code implementation.

_[Programming with Objective-C](../Programming%20with%20Objective-C/About%20Objective-C.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemjq)_ describes the Objective-C programming language.

_[Objective-C Runtime Programming Guide](../Objective-C%20Runtime%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danby)_ describes how you can interact with the Objective-C runtime.

_[Objective-C Runtime Reference](https://developer.apple.com/documentation/objectivec/objective_c_runtime)_ describes the data structures and functions of the Objective-C runtime support library. Your programs can use these interfaces to interact with the Objective-C runtime system. For example, you can add classes or methods, or obtain a list of all class definitions for loaded classes.

[Next](Why%20Objective-C.md)

