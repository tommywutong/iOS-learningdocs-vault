---
title: Using the Java Bridge
apple_id: TP40001404
resource_type: Guide
platform: Java
topic: Cross Platform
technology: null
published: '2007-04-03'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Legacy/JavaBridge/JavaBridge.1.html
archived_at: '2026-07-15T07:16:23.728596Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Using the Java Bridge](Legacy%20Documentclose%20button.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/index.html)  __>__  [Cocoa](https://developer.apple.com/library/archive/documentation/Cocoa/index.html) __>__
Using the Java Bridge

---

# Legacy Documentclose button

__Important:__
The information in this document is obsolete and should not be used for new development.

[Previous](Legacy%20Documentclose%20button.md) | [Next](Legacy%20Documentclose%20button-3.md) | [PDF](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Legacy/JavaBridge/JavaBridge.pdf)

[Using the Java Bridge](Legacy%20Documentclose%20button.md)

#  Introduction

The original OpenStep system developed by NeXT Software contained a number of object-oriented frameworks written in the Objective-C language. Most developers who used these frameworks wrote their code in Objective-C.

In recent years, the number of developers writing Java code has increased dramatically. For the benefit of these programmers, Apple Computer has provided Java APIs for these frameworks: Foundation Kit, AppKit, WebObjects, and Enterprise Objects. They were made possible by using techniques described later in this document. You can use these same techniques to expose your own Objective-C frameworks to Java code.

Java and Objective-C are both object-oriented languages, and they have enough similarities that communication between the two is possible. However, there are some differences between the two languages that you need to be aware of in order to use the bridge effectively. In general, using Objective-C from Java requires a bit more work on the part of the programmer than the reverse process.

Once the proper setup has been done, you can:

- Instantiate and use classes from one language in the other.
- 

  Pass objects as arguments and receive objects as return values from one language to the other.
- 

  Directly subclass Objective-C classes in Java.
- 

  See Objective-C protocols as Java interfaces.

---

[Previous](Legacy%20Documentclose%20button.md) | [Next](Legacy%20Documentclose%20button-3.md) | [PDF](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Legacy/JavaBridge/JavaBridge.pdf)
\xA9 1998 Apple Computer, Inc.
