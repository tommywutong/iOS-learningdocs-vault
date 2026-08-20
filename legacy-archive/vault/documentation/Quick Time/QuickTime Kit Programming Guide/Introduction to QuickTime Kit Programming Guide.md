---
title: QuickTime Kit Programming Guide
apple_id: TP40001245
resource_type: Guide
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QTKit
published: '2009-10-19'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/Conceptual/QTKitProgrammingGuide/Chapter01/Introduction.html
archived_at: '2026-07-18T01:58:39.591033Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](The%20QuickTime%20Kit%20API.md)

# Introduction to QuickTime Kit Programming Guide

The QuickTime Kit is a new framework (`QTKit.framework`) developed by Apple for working with QuickTime movies in Cocoa applications on Mac OS X. The QuickTime Kit framework, which offers a rich API for manipulating time-based media, is designed as an alternative to and eventual replacement for the existing Cocoa Application Kit classes NSMovie and NSMovieView. Using this new API provides developers with more extensive coverage of QuickTime functions and data types than is offered by those Application Kit classes and achieves this in a way that minimizes the requirement for Cocoa programmers to be conversant with Carbon data types such as handles, aliases, file-system specifications, and the like.

The QuickTime Kit also comes with a new QuickTime palette, which lets you drag a QuickTime movie object into your project window, and display, control, and edit that movie without writing a single line of code.

To work with this new framework, you don’t need to know anything about the existing NSMovie and NSMovieView classes, but you should be familiar with developing Cocoa applications using Xcode and Interface Builder. Because the framework is flexible and relatively easy to use in Cocoa, you won’t need to have a comprehensive understanding of the QuickTime C API in order to build your application or extend its functionality.

The QuickTime Kit framework is available in Mac OS X v10.4 and later. The framework also supports applications running in Mac OS X v10.3, but requires QuickTime 7 or later.

If you are a Cocoa developer who wants to integrate QuickTime movies in your application, you should read the material presented in this document. The various QuickTime and Cocoa mailing lists provide a useful developer forum for raising issues and answering questions that are posted.

If you are new to Cocoa or QuickTime, you should read these webpages, which are intended to get you up to speed with both Apple technologies: _Getting Started with Cocoa_ and _[Getting Started with QuickTime](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_QuickTime/_index.html#//apple_ref/doc/uid/TP30001099)_.

This document follows a progressive, learn-as-you-go structure. Each chapter depends, to a certain extent, on understanding the material in any previous chapters.

- [The QuickTime Kit API](The%20QuickTime%20Kit%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenbvfvbuqmrqgmwviucykjcummjqge) describes the various classes and functions in the QuickTime Kit and some of their possible uses.
- [Building a Simple QTKitPlayer Application](Building%20a%20Simple%20QTKitPlayer%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenbvfvbuqmrqgqwviucykjcummjqge) explains how you can build a simple QTKitPlayer application.
- [Extending the QTKitPlayer Application](Extending%20the%20QTKitPlayer%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenbvfvbuqmrqhewviucykjcummjqge) discusses how you can extend the functionality of the QTKitPlayer application by adding Cocoa code to your Xcode project.
- [Adding New Capabilities to the QTKitPlayer Application](Adding%20New%20Capabilities%20to%20the%20QTKitPlayer%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenbvfvbuqmrqg4wviucykjcummjqge) discusses how you can add a simple Cocoa drawer with a timer to your QTKitPlayer application and how you can take advantage of the QuickTime C API.
- [Extending the QTKitPlayer To Stream Audio and Video](Extending%20the%20QTKitPlayer%20To%20Stream%20Audio%20and%20Video.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenbvfvbuqmrqhawviucykjcummjqge) describes how you can add the streaming of audio and video to your QTKitPlayer application.
- [Adding Multimedia Playback Capability](Adding%20Multimedia%20Playback%20Capability.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenbvfvbuqmrsgmwviucykjcummjqge) explains in detail how you can extend your QTKitPlayer application to add multimedia playback capabilities.

This introductory and tutorial document is designed as companion text to the reference material in _[QuickTime Kit Framework Reference](https://developer.apple.com/documentation/qtkit)_. The various classes and methods in the QuickTime Kit framework are described in detail therein. Have that document handy as you learn the API and work through the various steps you need to follow in building a QuickTime application.

[Next](The%20QuickTime%20Kit%20API.md)

