---
title: Quartz Composer Programming Guide
apple_id: TP40001357
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzComposer/qc_intro/qc_intro.html
archived_at: '2026-07-15T07:37:14.788970Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Using%20QCView%20to%20Create%20a%20Standalone%20Composition.md)

# Introduction to Quartz Composer Programming Guide

The Quartz Composer framework defines classes and protocols that work with compositions built using the Quartz Composer development tool. This book describes how to use the [QCView](https://developer.apple.com/documentation/quartz/qcview) and [QCRenderer](https://developer.apple.com/documentation/quartz/qcrenderer) classes, and how to include compositions in webpages and widgets.

You should read this document if you are a developer who wants to load, play, and control compositions programmatically from a Cocoa application. This document assumes that you are familiar with the Quartz Composer development tool and the information in _[Quartz Composer User Guide](../Quartz%20Composer%20User%20Guide/Introduction%20to%20Quartz%20Composer%20User%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgobr)_. If you want to learn how to use the [QCPlugIn](https://developer.apple.com/documentation/quartz/qcplugin) class to create custom patches that you can use from within the Quartz Composer development tool, see _[Quartz Composer Custom Patch Programming Guide](../Quartz%20Composer%20Custom%20Patch%20Programming%20Guide/Introduction%20to%20Quartz%20Composer%20Custom%20Patch%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2doobx)_.

This document is organized as follows:

- [Using QCView to Create a Standalone Composition](Using%20QCView%20to%20Create%20a%20Standalone%20Composition.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjxfvbuqmrqg4wviucykjcummjqge) discusses how to render a composition to a [QCView](https://developer.apple.com/documentation/quartz/qcview) object using Interface Builder but no code.
- [Publishing Ports and Binding Them to Controls](Publishing%20Ports%20and%20Binding%20Them%20to%20Controls.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjxfvbuqmrqhawviucykjcummjqge) shows how to add controls to the user interface that are bound to one or more published ports in a composition.
- [Using the QCRenderer Class to Play a Composition](Using%20the%20QCRenderer%20Class%20to%20Play%20a%20Composition.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjxfvbuqmrqhewviucykjcummjqge) describes the [QCRenderer](https://developer.apple.com/documentation/quartz/qcrenderer) class and shows how to use it to load and play a composition programmatically.
- [Adding Compositions to Webpages and Widgets](Adding%20Compositions%20to%20Webpages%20and%20Widgets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjxfvbuqmznknltm) describes how to include a composition in a webpage or Dashboard widget.

These resources are essential for anyone wanting to program using the Quartz Composer framework:

- _Quartz Composer Reference Collection_ provides documentation for the Objective-C programming interface for Quartz Composer.
- `/Developer/Examples/Quartz Composer Sample Code` contains a variety of Quartz Composer compositions.
- The Quartz Composer development mailing list ([quartzcomposer-dev](http://lists.apple.com/mailman/listinfo/quartzcomposer-dev)) is an excellent place to discuss programming issues or topics with other developers.
[Next](Using%20QCView%20to%20Create%20a%20Standalone%20Composition.md)

