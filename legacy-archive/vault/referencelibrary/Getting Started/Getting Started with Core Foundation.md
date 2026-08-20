---
title: Getting Started with Core Foundation
apple_id: TP30001089
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_CoreFoundation/_index.html
archived_at: '2026-07-18T02:39:21.274134Z'
---
> 导航：[总目录](../../README.md) · [referencelibrary](../../_indexes/referencelibrary.md)



## Introduction

### Technology Overview

Core Foundation is a procedural C framework that is conceptually modeled on the object-oriented Foundation framework in [Cocoa](https://developer.apple.com/cocoa/) and that uses the abstraction of the opaque type as a procedural analog to an object. If you use the Mac OS X developer environments ([Carbon](https://developer.apple.com/carbon/) and Cocoa), you can incorporate Core Foundation types in your external interfaces and so share code and data between different frameworks and libraries. Moreover, you can use many Core Foundation data types (such as arrays and strings) interchangeably with the corresponding Cocoa objects. This can help you to transition code from one application environment to another. Utilities such as command-line applications can also benefit from the features Core Foundation provides.

Core Foundation helps you to create various kinds of application by providing:

- Opaque types that encapsulate data such as strings, dates, and locales. These opaque types help you to manipulate Unicode strings, internationalize your application, and deal with time information.
- Opaque types that represent arrays, dictionaries, and XML property lists. These opaque types help you to deal with collections of data and to exchange data between different applications.
- A memory management model that helps you to prevent your code from leaking.
- A suite of utilities to support such features as plug-ins, URL resource access, and user preferences.

You can also use the associated [CFNetwork Programming Guide](../../documentation/Networking/CFNetwork%20Programming%20Guide/Introduction%20to%20CFNetwork%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmzs) framework for networking tasks—in particular, dealing with Bonjour and the processing of HTTP transmissions.

Core Foundation does not provide support for user interface components such as windows and menus. If you want to create applications with a graphical user interface, you should also look at Getting Started with Cocoa and [Getting Started with Carbon](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_Carbon/_index.html#//apple_ref/doc/uid/TP30001086) to become familiar with those frameworks.

### Start Here

To begin development with Core Foundation, read:

- [Mac Technology Overview](../../documentation/Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx) to familiarize yourself with the system architecture of Mac OS X. At a minimum, read the System Architecture chapter, so that you can understand how Core Foundation relates to the major application environments.
- [Core Foundation Design Concepts](../../documentation/Core%20Foundation/Core%20Foundation%20Design%20Concepts/Introduction%20to%20Core%20Foundation%20Design%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezde2i) (Core Foundation) to understand the design concepts that underlie Core Foundation.
- [Core Foundation](https://developer.apple.com/corefoundation/) to become familiar with the latest developments in the Core Foundation APIs, documentation, and Technical Notes, and to learn about other resources related to developing with Core Foundation.

### Choose a Learning Path

Becoming proficient with Core Foundation begins with learning the underlying fundamental concepts—in particular, memory management. You may also benefit from using Apple’s developer tools.

#### Learning the Fundamentals

The first step in learning to use Core Foundation effectively is to understand the basic principles of opaque types. A full appreciation of the memory management model that Core Foundation employs will save you from many common mistakes.

- __To learn about opaque types__, read [Opaque Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/OpaqueTypes.html#//apple_ref/doc/uid/20001106).
- __To learn about memory management__, read [Memory Management Programming Guide for Core Foundation](../../documentation/Core%20Foundation/Memory%20Management%20Programming%20Guide%20for%20Core%20Foundation/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdo2i).

#### Learning About the Development Tools

To start writing Core Foundation utilities quickly, Apple recommends its integrated development environment Xcode, which integrates a number of standard UNIX development tools.

- __To learn more about Apple’s Xcode Tools__, read [Mac Technology Overview](../../documentation/Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx).

#### Migrating from Another Platform

If you are porting code from another environment, the following documents will provide useful information. The article [Carbon-Cocoa Integration Guide](../../documentation/Cocoa/Carbon-Cocoa%20Integration%20Guide/Introduction%20to%20Carbon-Cocoa%20Integration%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqojt) also describes general porting and integration issues relevant to Core Foundation.

- __If you are porting an application from Mac OS 9__, read [Carbon Porting Guide](../../documentation/Carbon/Carbon%20Porting%20Guide/Introduction%20to%20Carbon%20Porting%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojr) to determine how to best make the transition.
- __If you are a UNIX or Linux developer__, read [Porting UNIX/Linux Applications to OS X](../../documentation/Porting/Porting%20UNIX-Linux%20Applications%20to%20OS%20X/Introduction%20to%20Porting%20UNIX-Linux%20Applications%20to%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambt) to learn what makes Mac OS X different from other UNIX implementations and how to port existing UNIX applications to the platform.
- __If you are porting an application from Windows__, read [Porting to Mac OS X from Windows Win32 API](../../documentation/Porting/Porting%20to%20Mac%20OS%20X%20from%20Windows%20Win32%20API/Porting%20to%20Mac%20OS%20X%20from%20Windows%20Win32%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4ta2i) to learn the differences to expect between Windows and Mac OS X and the resources that can be useful in the porting process.

### Next Steps

The [Core Foundation Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000421) includes the following high-level resource pages, which can be bookmarked for easy access:

- [Guides](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000440-TP30000421)

  Conceptual and how-to information for Core Foundation technologies.
- [Reference](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000421)

  Focused, detailed descriptions in reference format for the Core Foundation API.
- [Release Notes](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000872-TP30000421)

  Late-breaking news about new or changed features in the Core Foundation API.
- [Sample Code](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000925-TP30000421)

  Sample applications, some of which demonstrate Core Foundation technologies. If you install the Xcode Tools CD, additional sample projects are provided in `/Developer/Examples/CoreFoundation`.
- [Technical Notes](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000924-TP30000421)

  Late-breaking documents on Core Foundation issues.
- [Technical Q&As](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000926-TP30000421)

  Programming tips, code snippets, and FAQs by Apple’s support engineers.

