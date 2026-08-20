---
title: Getting Started with Carbon
apple_id: TP30001086
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-05-23'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_Carbon/_index.html
archived_at: '2026-07-18T02:39:21.211076Z'
---
> 导航：[总目录](../../README.md) · [referencelibrary](../../_indexes/referencelibrary.md)



## Introduction

### Technology Overview

Carbon is a procedural C interface for Mac OS X. Whether you are writing a new application or porting one from another platform, Carbon is an excellent framework for developing on Mac OS X. If you're developing new applications and prefer an object-oriented interface, be sure to consider [Cocoa](https://developer.apple.com/cocoa/).

If you are familiar with C programming but not with Carbon or Mac OS X, you want to learn how to design and implement a basic user interface and then learn how to build a Carbon application using Mac OS X development tools. After that, you’ll want to explore the various Carbon "managers" and "services" for APIs specific to your needs.

### Start Here

Before you begin development, you should familiarize yourself with the system architecture and user interface of Mac OS X. You should read:

- [Mac Technology Overview](../../documentation/Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx) to learn about the major application environments available (Carbon, Cocoa, and Java).
- [Carbon Overview](../../documentation/Carbon/Carbon%20Overview/Introduction%20to%20Carbon%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojq) to familiarize yourself with the Carbon technologies available for application development.
- Apple Human Interface Guidelines to learn what standard user interface elements are available in Mac OS X and to understand how to design your application's look and feel.

### Choose a Learning Path

If you’re just beginning to develop Carbon applications, you may want to know how developing for Mac OS X differs from developing for other platforms. If you’re ready to develop for Mac OS X, you’ll want to learn how to use the Xcode development environment. If you’re familiar with Xcode, you’ll want to begin creating a simple user interface for Mac OS X.

#### Migrating from Another Platform

Before you begin development for Mac OS X, you may need to move your existing code from another platform.

- __If you’re a Windows developer__, read [Porting to Mac OS X from Windows Win32 API](../../documentation/Porting/Porting%20to%20Mac%20OS%20X%20from%20Windows%20Win32%20API/Porting%20to%20Mac%20OS%20X%20from%20Windows%20Win32%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4ta2i), which highlights differences to expect between Windows and Mac OS X and provides pointers to resources that can be useful in the porting process.
- __If you’re a UNIX or Linux developer__, read [Porting UNIX/Linux Applications to OS X](../../documentation/Porting/Porting%20UNIX-Linux%20Applications%20to%20OS%20X/Introduction%20to%20Porting%20UNIX-Linux%20Applications%20to%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambt) to learn what makes Mac OS X different from other UNIX implementations and to learn how to port existing UNIX applications to the platform.
- __If you’re a Mac OS 9 developer__, read [Carbon Porting Guide](../../documentation/Carbon/Carbon%20Porting%20Guide/Introduction%20to%20Carbon%20Porting%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojr) and Technical Note TN2003, [Moving Your Code to Mac OS X](https://developer.apple.com/technotes/tn/tn2003.html), to learn how to best make the transition to Mac OS X.

#### Developing with Xcode

To develop Carbon applications, Apple recommends using Xcode, which is included in the Developer Tools package included with Mac OS X v10.3 (Panther) and later. You should read:

- Xcode 2.1 User Guide to learn about the tools used to design a user interface as well as build and debug applications.
- [A Tour of Xcode](../../documentation/Developer%20Tools/A%20Tour%20of%20Xcode/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqojq) to learn how to use Xcode tools to build a simple Carbon application.

Once you’re familiar with Xcode, you’re ready to build a user interface for a Carbon application.

#### Building a User Interface

To build a user interface for your Carbon application, you should read:

- [Carbon Event Manager Programming Guide](../../documentation/Carbon/Carbon%20Event%20Manager%20Programming%20Guide/Introduction%20to%20Carbon%20Event%20Manager%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobz) to understand the event-handling model for Carbon applications. Carbon events are the primary messaging mechanism between your application and system software, handling user interactions as well as low-level events.
- [Handling Carbon Windows and Controls](../../documentation/Carbon/Handling%20Carbon%20Windows%20and%20Controls/Introduction%20to%20Handling%20Carbon%20Windows%20and%20Controls.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambu) to learn how to create and manipulate windows and controls in Carbon applications.
- [Creating Carbon Menus](../../documentation/Carbon/Creating%20Carbon%20Menus/Carbon%20Menus%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrv) to learn how to implement menus in your Carbon application.
- [HIView Programming Guide](../../documentation/Carbon/HIView%20Programming%20Guide/Introduction%20to%20HIView%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrt) to familiarize yourself with the object-oriented approach to implementing Carbon user interface objects. If you are planning to run your application on Mac OS X v10.2 (Jaguar) or later, you should adopt HIViews.
- [Unarchiving Interface Objects With Interface Builder Services](../../documentation/Carbon/Unarchiving%20Interface%20Objects%20With%20Interface%20Builder%20Services/Introduction%20to%20Unarchiving%20Interface%20Objects%20With%20Interface%20Builder%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambv) to learn how to access Carbon user interface elements created using the Interface Builder tool, included with Xcode. Although you can create windows, controls, and menus programmatically, in most cases the preferred method is to create them in Interface Builder and store them as special "nib" files.
- [Learning Carbon](http://oreilly.com/catalog/learncarbon/index.html) from O'Reilly & Associates, which provides a book-length tutorial for building Carbon applications, including topics such as building the user interface, manipulating text, and printing. Even though this book uses an older development environment (Project Builder), much of the information is still useful for developers wanting to learn about Carbon.

Note that the Carbon user interface APIs are often referred to as the Human Interface Toolbox, High Level Toolbox, or, if you are using object-oriented HIViews, the HIToolbox.

### Next Steps

The [Carbon Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000420) includes the following high-level Carbon resource pages, which you can bookmark for easy access:

- [Guides](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000440-TP30000420)

  Conceptual and how-to information about Carbon technologies.
- [Reference](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000420)

  Focused, detailed descriptions in reference format for Carbon.
- [Release Notes](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000872-TP30000420)

  Late-breaking news about new or changed features in the Carbon API.
- [Sample Code](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000925-TP30000420)

  Sample applications demonstrating a wide variety of Carbon technologies. If you have installed the developer tools or Xcode CD, you may also want to check out the sample applications in Developer/Examples/Carbon.
- [Technical Notes](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000924-TP30000420)

  Late-breaking documents on Carbon-related issues.
- [Technical Q&As](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000926-TP30000420)

  Programming tips, code samples, and FAQs by Apple’s support engineers.
- Mailing Lists

  The Carbon development mailing list ([carbon-dev](http://lists.apple.com/mailman/listinfo/carbon-dev)) is an excellent place to discuss programming issues or topics with fellow Carbon developers.

These additional resource pages may also be helpful:

- [Tips and Tricks](https://developer.apple.com/carbon/tipsandtricks.html)

  A site containing useful information for developing, porting, and debugging Carbon applications.

