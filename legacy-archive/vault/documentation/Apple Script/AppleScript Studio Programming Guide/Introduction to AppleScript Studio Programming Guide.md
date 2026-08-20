---
title: AppleScript Studio Programming Guide
apple_id: TP30000889
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2011-01-07'
source_url: https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/StudioBuildingApps/chapter01/studio_intro_book.html
archived_at: '2026-07-15T05:19:37.506566Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](About%20AppleScript%20Studio.md)

# Introduction to AppleScript Studio Programming Guide

_AppleScript Studio Programming Guide_ provides the key information you’ll need to create AppleScript Studio applications.

AppleScript Studio is a powerful tool for quickly creating native Mac OS X applications that support the Aqua user interface guidelines. It combines features from AppleScript, Xcode, Interface Builder, and the Cocoa application framework. With AppleScript Studio, you can work in a full-featured development environment to create applications that use AppleScript scripts to control a broad range of Cocoa user-interface objects.

AppleScript Studio has something to offer both to scripters and to those with Cocoa development experience:

- It provides access to AppleScript’s ability to control multiple applications, including parts of the Mac OS itself.
- Scripters can create applications with a complex user interface, including windows, buttons, menus, text fields, tables, and much more. Scripts have full access to user interface objects.
- Cocoa developers can use AppleScript Studio to speed up prototyping, testing, and deploying of applications.

This document assumes that you have some familiarity with AppleScript and know how to write and execute scripts.

Previous experience building applications with an integrated development environment is also recommended—familiarity with Xcode and Interface Builder is especially useful.

Previous experience with Cocoa is not required, but can be helpful in understanding some of AppleScript Studio’s underlying mechanisms.

For documentation and other resources for these technologies, see [See Also](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2dqlkdjfeeiqkhifda).

For information on whether AppleScript Studio is appropriate to your task, see [Strengths and Limitations](About%20AppleScript%20Studio.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2dslkukbmferkgge3da).

This document contains the following chapters:

- [Introduction to AppleScript Studio Programming Guide](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2dqlkukbmferkggeydc) briefly describes AppleScript Studio, provides a description for each chapter, and lists some related documentation.
- [About AppleScript Studio](About%20AppleScript%20Studio.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2dslkukbmferkggeydc) introduces AppleScript Studio’s key features and shows how to create a simple “Hello World” application.
- [AppleScript Studio Components](AppleScript%20Studio%20Components.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2talkukbmferkggeydc) provides a detailed description of AppleScript Studio, including descriptions of the key features in Xcode and Interface Builder, as well as overviews of the Cocoa and AppleScriptKit frameworks.
- [Programming With AppleScript Studio](Programming%20With%20AppleScript%20Studio.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tclkukbmferkggeydc) describes additional features and issues you’ll want to know more about as you work with AppleScript Studio. It also describes the scripting terminology you need to write scripts and provides tips for programming with AppleScript Studio.
- [AppleScript Studio Cookbook](AppleScript%20Studio%20Cookbook.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2telkukbmferkggeydc) provides step-by-step instructions for performing some common AppleScript Studio tasks.
- [Currency Converter Tutorial](Currency%20Converter%20Tutorial.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tglkukbmferkggeydc) provides a simple tutorial that introduces the tools and processes you’ll use in most AppleScript Studio development.
- [Mail Search Tutorial: Design the Application](Mail%20Search%20Tutorial-%20Design%20the%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tilkukbmferkggeydc) is the first of several chapters that make up a tutorial for a more complex AppleScript Studio application. This chapter describes the process of designing the application.
- [Mail Search Tutorial: Create the Interface](Mail%20Search%20Tutorial-%20Create%20the%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tklkukbmferkggeydc) describes how to create the interface for the Mail Search application.
- [Mail Search Tutorial: Connect the Interface](Mail%20Search%20Tutorial-%20Connect%20the%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tmlkukbmferkggeydc) shows how to connect Mail Search’s interface to event handlers in the application’s scripts.
- [Mail Search Tutorial: Write the Code](Mail%20Search%20Tutorial-%20Write%20the%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tolkukbmferkggeydc) describes the handlers and script statements for the Mail Search application.
- [Mail Search Tutorial: Build and Test the Application](Mail%20Search%20Tutorial-%20Build%20and%20Test%20the%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tqlkukbmferkggeydc) provides information on how to build and test the Mail Search application.
- [Mail Search Tutorial: Customize the Application](Mail%20Search%20Tutorial-%20Customize%20the%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tslkukbmferkggeydc) provides steps for customizing menus, icons, and version and copyright information in the Mail Search application.
- [AppleScript Studio System Requirements and Version Information](AppleScript%20Studio%20System%20Requirements%20and%20Version%20Information.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3dalkukbmferkggeydc) describes the system requirements for building and running AppleScript Studio applications.
- [Mail Search Tutorial, Full Script Listing](Mail%20Search%20Tutorial%2C%20Full%20Script%20Listing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3dclkukbmferkggeydc) contains a complete listing of the Mail Search application’s script file.
- [Document Revision History](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3delkukbmferkggeydc) describes changes made to this document.
- [Glossary](Glossary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi3dglkukayq) defines key terms for working with AppleScript Studio.

You’ll see the AppleScript continuation character (¬, which you create by typing Option-l) in some of the script listings in this document. When a line in a script ends with a continuation character, the next line is considered to be part of that line. You shouldn’t need the continuation character when you actually compile the scripts in AppleScript Studio, because you can use Xcode’s ability to wrap text instead. For more information, see [How Xcode Formats Scripts](Programming%20With%20AppleScript%20Studio.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2tclkdjjbegsciifca).

Some listings in this document may use wrapped text, rather than the continuation character.

You can find getting started and overview documentation for AppleScript, AppleScript Studio, and related technologies, with links to all the available Apple documentation and resources (including mailing lists), here:

- Getting Started With AppleScript
- _[AppleScript Overview](../AppleScript%20Overview/Introduction%20to%20AppleScript%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tm2i)_

Because AppleScript Studio relies heavily on the Cocoa application framework, you may also want to visit the [Cocoa Documentation](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000416) area, particularly these documents:

- _[Application Architecture Overview](../../Cocoa/Application%20Architecture%20Overview/Introduction%20to%20Application%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaydk2i)_
- _[Cocoa Scripting Guide](../../Cocoa/Cocoa%20Scripting%20Guide/Introduction%20to%20Cocoa%20Scripting%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnru)_

You can also use any web search engine to many third-party books, products, and websites for AppleScript and AppleScript Studio.

[Next](About%20AppleScript%20Studio.md)

