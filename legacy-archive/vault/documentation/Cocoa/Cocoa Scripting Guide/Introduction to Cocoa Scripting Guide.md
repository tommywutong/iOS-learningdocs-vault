---
title: Cocoa Scripting Guide
apple_id: TP40002164
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: null
published: '2008-03-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html
archived_at: '2026-07-15T07:18:50.852993Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Overview%20of%20Cocoa%20Support%20for%20Scriptable%20Applications.md)

# Introduction to Cocoa Scripting Guide

This document describes how to create scriptable applications using the support provided by the Cocoa application framework. That support, which is referred to as _Cocoa scripting_, includes classes, categories, and scriptability information.

A scriptable application is one that can be controlled by AppleScript scripts. Users write scripts to automate tasks and combine the use of multiple applications. As a developer, you can also use scripts to speed up prototyping or testing of your scriptable applications.

When a script that targets an application is executed, commands are sent to the application in the form of Apple events, a kind of interprocess message. Cocoa scripting helps you create scriptable applications by doing much of the work of receiving these Apple events, extracting information from them, and invoking methods in your scriptable classes.

This document provides conceptual information and examples that are based primarily on the scripting support available in OS X versions 10.4 and 10.3.

Although some information may be accurate for versions of the Mac OS prior to v10.3, this document has not been reviewed for accuracy on those versions, nor does it attempt to provide details for working with those versions.

This document is intended for developers who want to make their Cocoa applications scriptable or who need to know more about how Cocoa applications interact with AppleScript and Apple events. It assumes you have some familiarity with Cocoa, Objective-C, and AppleScript. However, if you are unfamiliar with AppleScript, you should start by reading _Getting Started with AppleScript_ and _[AppleScript Overview](../../Apple%20Script/AppleScript%20Overview/Introduction%20to%20AppleScript%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tm2i)_. Many of the terms scripters use are defined in _[AppleScript Language Guide](../../Apple%20Script/AppleScript%20Language%20Guide/Introduction%20to%20AppleScript%20Language%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobt)_.

The following chapters describe how to design, implement, and debug a scriptable Cocoa application:

- [Overview of Cocoa Support for Scriptable Applications](Overview%20of%20Cocoa%20Support%20for%20Scriptable%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsnzwfvbeeq2cineuuri) provides a brief overview of AppleScript and scriptable applications, and describes the scripting support provided by the Cocoa application framework. This chapter is a prerequisite for the chapters that follow.
- [Designing for Scriptability](Designing%20for%20Scriptability.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsnzyfvbeeq2cineuuri) provides high-level checklists for designing a new scriptable Cocoa application and making an existing application scriptable.
- [Implementing a Scriptable Application](Implementing%20a%20Scriptable%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgaztolkcijbuurkfivbq) lists the key steps for implementing a scriptable Cocoa application, with links to more detailed information where necessary.
- [Preparing a Scripting Definition File](Preparing%20a%20Scripting%20Definition%20File.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsnzzfvbeeq2cineuuri) describes the structure of scripting definition, or sdef, files. It also shows how to create an sdef for a scriptable Cocoa application and how to add scriptability information to it.
- [Getting and Setting Properties and Elements](Getting%20and%20Setting%20Properties%20and%20Elements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmjyfvjvomi) describes how to work with Cocoa scripting to get and set the values of properties and elements in your scriptable application. It also provides examples of basic, KVC-compliant accessor methods.
- [Object Specifiers](Object%20Specifiers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmznknltc) explains the mechanism for locating a scriptable object in the context of its container and provides sample object specifier methods.
- [Script Commands](Script%20Commands.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2delkcijbueq2jjjcq) provides additional detail about the script command mechanism Cocoa uses to respond to Apple events and describes how to implement script commands.
- [Testing, Debugging, and Performance](Testing%2C%20Debugging%2C%20and%20Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobrfvbeeq2kivcukqy) provides tips for building up your test plan debugging the scriptability in your Cocoa application, and spotting possible performance issues.

The following chapters provide additional information about Cocoa scripting support:

- [How Cocoa Applications Handle Apple Events](How%20Cocoa%20Applications%20Handle%20Apple%20Events.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgiztslkcijbueq2jjjcq) describes the default support for handling Apple events in Cocoa applications and how your application interacts with it.
- [Cocoa Scripting Classes and Categories](Cocoa%20Scripting%20Classes%20and%20Categories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgaztilkcijbuer2diveq) provides brief descriptions of the main classes that make up Cocoa scripting support, including those that you use in creating scriptable applications.
- [Evolution of Cocoa Scriptability Information](Evolution%20of%20Cocoa%20Scriptability%20Information.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnrufvbuqmjzfvjvomi) describes changes to Cocoa scriptability information over time. It includes information about when to use various types of scriptability information and how to convert between them.

The following chapter describes how to specify scriptability information using an earlier format:

- [Script Suite and Script Terminology Files](Script%20Suite%20and%20Script%20Terminology%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi2dclkcijbueq2jjjcq) describes another way to provide terminology information and describes the structure of script suite and script terminology files.

For more information on the basic design patterns used by Cocoa scripting support, see _[Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)_.

[Next](Overview%20of%20Cocoa%20Support%20for%20Scriptable%20Applications.md)

