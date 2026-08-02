---
title: QTKit Application Tutorial
apple_id: TP40008155
resource_type: Guide
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QTKit
published: '2016-08-26'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/QTKitApplicationTutorial/Introduction/Introduction.html
archived_at: '2026-07-15T07:18:33.666728Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Creating%20a%20Simple%20QTKit%20Media%20Player%20Application.md)

# Introduction

Introduced in OS X v10.4, the QTKit [framework](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56) is a powerful, feature-rich [Objective-C](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectiveC.html#//apple_ref/doc/uid/TP40008195-CH43) API for manipulating and rendering time-based media such as movies and audio files.

This tutorial explains how to build three different applications for playing, editing, and recording audio and video media. You build these applications using the QTKit programming interfaces and Apple’s developer tools, Xcode 3.2 and Interface Builder 3.2. This document describes QTKit for OS X v10.6.

If you are a developer who wants to learn how to integrate playback, editing and recording of media into your application, you should read the material in this document to get started. You don’t necessarily need to be a seasoned Cocoa programmer to take advantage of the capabilities provided in the QTKit framework, although you’ll find prior experience working with Objective-C, Xcode, and Interface Builder helpful to build and compile the different code examples described in this tutorial.

This tutorial follows a progressive, learn-as-you-go structure. To be most successful, work through this tutorial in the order presented.

- [Creating a Simple QTKit Media Player Application](Creating%20a%20Simple%20QTKit%20Media%20Player%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnjvfvbuqmznknltq) describes how to build and compile a simple media player application, using Cocoa bindings and with a minimal number of lines of Objective-C code.
- [Extending the Media Player Application](Extending%20the%20Media%20Player%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnjvfvbuqnjnknltc) explains how you can extend and enhance the functionality of the media player application to support editing of video/audio files.
- [Customizing the Media Player Application](Customizing%20the%20Media%20Player%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnjvfvbuqnznknltc) discusses how you can extend the functionality of the media player application by adding custom controls and selecting attributes to handle the precise display and manipulation of high-definition, H.264-enabled movies. QuickTime X methods for more efficient media playback in your Xcode project are also discussed.
- [Building a Simple QTKit Recorder Application](Building%20a%20Simple%20QTKit%20Recorder%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnjvfvbuqobnknltc) discusses step-by-step how you can build a simple yet powerful QTKit recorder application that lets you capture a video stream and record the media to a QuickTime movie.
- [Adding Audio Input and DV Camera Support](Adding%20Audio%20Input%20and%20DV%20Camera%20Support.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnjvfvbuqojnknltc) describes how you can extend the functionality of your QTKit recorder player application by adding support for audio input and DV cameras with only a few lines of Objective-C code.
- [Creating a QTKit Stop Motion Application](Creating%20a%20QTKit%20Stop%20Motion%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnjvfvbuqmjqfvjvomi) describes how you can construct a simple stop motion recorder application that lets you capture a live video feed, grab frames one at a time with great accuracy, and then record the output of those frames to a QuickTime movie––with less than 100 lines of Objective-C code.

To build your QTKit media player and recorder projects, make sure you are running OS X v10.5 or later and have these Apple developer tools installed on your system:

- __Xcode 3.2 and Interface Builder 3.2__. Apple provides a comprehensive suite of developer tools for creating OS X software. These tools include applications to help you design, create, debug, and optimize your software. The suite also includes header files, sample code, and documentation. You can download the Xcode tools from the [Apple Developer Connection website](https://developer.apple.com/). Registration is required, but free.

The tutorial is based on the following three code samples, which you can download from the [Apple Developer Connection website](https://developer.apple.com/) or view from within Xcode:

- `MyMediaPlayer` (constructed in [Creating a Simple QTKit Media Player Application](Creating%20a%20Simple%20QTKit%20Media%20Player%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnjvfvbuqmznknltq) and [Extending the Media Player Application](Extending%20the%20Media%20Player%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnjvfvbuqnjnknltc)), which demonstrates how you can build, compile and extend a simple yet powerful application for playback of video and audio media.
- `MyRecorder` (constructed in [Building a Simple QTKit Recorder Application](Building%20a%20Simple%20QTKit%20Recorder%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnjvfvbuqobnknltc) and [Adding Audio Input and DV Camera Support](Adding%20Audio%20Input%20and%20DV%20Camera%20Support.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnjvfvbuqojnknltc)), which demonstrates how you can use the QTKit Capture programming interface to create a fully functional application for recording audio/video media.
- `StopMotion` (constructed in [Creating a QTKit Stop Motion Application](Creating%20a%20QTKit%20Stop%20Motion%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnjvfvbuqmjqfvjvomi)) demonstrates how you can build an application for recording single frame images and outputting those images for playback as a QuickTime movie.

For more information on the technologies and tools you use in this tutorial, consult the following Apple documentation:

- _[QTKit Framework Reference](https://developer.apple.com/documentation/qtkit)_ contains the class and protocol reference documentation for the QTKit framework.
- _[Interface Builder User Guide](../../Developer%20Tools/Interface%20Builder%20User%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbu)_ describes the latest version of Interface Builder 3.
- _[A Tour of Xcode](../../Developer%20Tools/A%20Tour%20of%20Xcode/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqojq)_ provides an introduction on how to use the Xcode application.
- _[QTKit Application Programming Guide](../QTKit%20Application%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnjw)_ discusses in-depth the QTKit software architecture, best design practices and coding techniques you can use in developing feature-rich media applications in OS X.

The various QuickTime and Cocoa mailing lists also provide a useful developer forum for raising issues and answering questions that are posted. To subscribe, check out the [QuickTime-API Mailing List](http://www.lists.apple.com/mailman/listinfo/quicktime-api) and the [Cocoa Development list](http://www.lists.apple.com/mailman/listinfo/cocoa-dev).

[Next](Creating%20a%20Simple%20QTKit%20Media%20Player%20Application.md)

