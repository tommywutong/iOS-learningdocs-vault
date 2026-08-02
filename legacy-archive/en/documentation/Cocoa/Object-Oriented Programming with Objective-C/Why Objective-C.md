---
title: Object-Oriented Programming with Objective-C
apple_id: TP40005149
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2010-11-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OOP_ObjC/Articles/ooWhy.html
archived_at: '2026-07-15T07:17:21.852618Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Object-Oriented Programming with Objective-C](Introduction.md)


[Next](Object-Oriented%20Programming.md)[Previous](Introduction.md)

# Why Objective-C?

The Objective-C language was chosen for a variety of reasons. First and foremost, it’s an object-oriented language. The kind of functionality that’s packaged in the Cocoa frameworks can only be delivered through object-oriented techniques. Second, because Objective-C is an extension of standard ANSI C, existing C programs can be adapted to use the software frameworks without losing any of the work that went into their original development. Because Objective-C incorporates C, you get all the benefits of C when working within Objective-C. You can choose when to do something in an object-oriented way (define a new class, for example) and when to stick to procedural programming techniques (define a structure and some functions instead of a class).

Moreover, Objective-C is a fundamentally simple language. Its syntax is small, unambiguous, and easy to learn. Object-oriented programming, with its self-conscious terminology and emphasis on abstract design, often presents a steep learning curve to new recruits. A well-organized language like Objective-C can make becoming a proficient object-oriented programmer that much less difficult.

Compared to other object-oriented languages based on C, Objective-C is very dynamic. The compiler preserves a great deal of information about the objects themselves for use at runtime. Decisions that otherwise might be made at compile time can be postponed until the program is running. Dynamism gives Objective-C programs unusual flexibility and power. For example, it yields two big benefits that are hard to get with other nominally object-oriented languages:

- Objective-C supports an open style of dynamic binding, a style that can accommodate a simple architecture for interactive user interfaces. Messages are not necessarily constrained by either the class of the receiver or even the method name, so a software framework can allow for user choices at runtime and permit developers freedom of expression in their design. (Terminology such as _dynamic binding_, _message_, _class_, and _receiver_ are explained in due course in this document.)
- Dynamism enables the construction of sophisticated development tools. An interface to the runtime system provides access to information about running applications, so it’s possible to develop tools that monitor, intervene, and reveal the underlying structure and activity of Objective-C applications.

[Next](Object-Oriented%20Programming.md)[Previous](Introduction.md)

