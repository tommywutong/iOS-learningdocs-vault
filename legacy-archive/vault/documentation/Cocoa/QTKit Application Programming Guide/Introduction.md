---
title: QTKit Application Programming Guide
apple_id: TP40008156
resource_type: Guide
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QTKit
published: '2016-08-26'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/QTKitApplicationProgrammingGuide/Introduction/Introduction.html
archived_at: '2026-07-15T07:18:09.538726Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](QTKit%20Architecture.md)

# Introduction

QTKit is a Cocoa-based, Objective-C [framework](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56) (`QTKit.framework`) with a rich and evolving API for manipulating time-based media. Introduced in OS X v10.4, QTKit provides a set of Objective-C classes and methods specifically designed to handle the basic chores of playback, editing, export, audio/video capture and recording, in addition to a number of other multimedia capabilities. Each iteration of the framework from Apple, accompanying the latest release of OS X, has extended the power and reach of the API.

Toward that end, OS X v10.6 introduces QuickTime X, a new media architecture for efficient, high-performance playback of audio/video media, with optimized support for modern codecs. As an [Objective-C](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectiveC.html#//apple_ref/doc/uid/TP40008195-CH43) API, QTKit provides a great deal of functionality in a relatively small package, with methods and classes that support a wide range of media-related tasks, such as playback, editing, and capture.

The goal of this programming guide is to show you how to take advantage of the QTKit classes and methods in your application, through code examples and step-by-step procedures that illustrate various coding techniques and best practices. In addition, the guide provides you with a class hierarchy and architectural overview of the framework itself, grouping some of the most frequently used playback and capture methods to accomplish particular tasks.

If you are a media developer who wants to integrate movies in your Cocoa application, you should read the material in this document. You don’t necessarily need to be a seasoned Cocoa programmer to take advantage of the capabilities provided in the QTKit framework, although you’ll need some prior experience working with [Objective-C](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectiveC.html#//apple_ref/doc/uid/TP40008195-CH43), Xcode, and Interface Builder to build and compile the code examples described in this guide. The document describes QTKit for OS X v10.6 and later.

A prerequisite for working with the QTKit framework is a basic understanding of Cocoa and the [Objective-C](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectiveC.html#//apple_ref/doc/uid/TP40008195-CH43) programming language. The basics of Cocoa and Objective-C are discussed in detail in the _[Cocoa Fundamentals Guide](../Cocoa%20Fundamentals%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzu)_ and _[The Objective-C Programming Language](../The%20Objective-C%20Programming%20Language/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrt)_ guide. It may also be helpful to have an understanding of the OS X graphics and imaging technologies which are described in _[Mac Technology Overview](../../Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx)_. If you need to learn the basics of how to build and compile a media playback or recorder application, refer to the _[QTKit Application Tutorial](../QTKit%20Application%20Tutorial/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnjv)_. The tutorial is intended to get you rapidly up to speed with QTKit by working step by step through a set of code samples that let you accomplish playback and recording tasks.

This guide is organized into an overview chapter that discusses the fundamentals of the QTKit architecture, followed by a chapter describing the QTKit classes and methods designed for audio/video capture and recording. The last chapter deals with how to modify your existing QTKit code to take advantage of the improved playback performance and modern codec optimizations available in Mac OS v10.6 and the new media architecture of QuickTime X.

- [QTKit Architecture](QTKit%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnjwfvbuqmjqhewvgvzrgu) describes the QTKit software architecture, class hierarchy, design and object model, and various programming tasks you can perform, such as opening and playing movies. It also discusses thread-safety issues that you need to understand in order to work with the API.
- [QTKit Capture](QTKit%20Capture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnjwfvbuqmjqhawvgvzz) describes the portion of the QTKit API that deals with capture and recording of media and provides a set of use cases and code samples for dealing with various capture programming tasks.
- [Adopting QuickTime X for Playback](Adopting%20QuickTime%20X%20for%20Playback.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnjwfvbuqmjrgewvgvzr) discusses how your application can opt into the new, more efficient media playback capabilities available in QuickTime X and Mac OS v10.6.

For more information on the technologies and tools you use in this programming guide, consult the following Apple documentation:

- _[QTKit Framework Reference](https://developer.apple.com/documentation/qtkit)_ contains the class and protocol reference documentation for the QTKit framework.
- _[Interface Builder User Guide](../../Developer%20Tools/Interface%20Builder%20User%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbu)_ describes Interface Builder, Apple interface creation tool.
- _[A Tour of Xcode](../../Developer%20Tools/A%20Tour%20of%20Xcode/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqojq)_ provides an introduction on how to use the Xcode IDE.
- _[QTKit Application Tutorial](../QTKit%20Application%20Tutorial/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnjv)_ explains how to build three different Cocoa applications for playing, editing, and recording audio/video media, using QTKit.
[Next](QTKit%20Architecture.md)

