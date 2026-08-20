---
title: Quartz Composer Custom Patch Programming Guide
apple_id: TP40004787
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2010-03-24'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzComposer_Patch_PlugIn_ProgGuide/Introduction/Introduction.html
archived_at: '2026-07-15T07:37:51.842019Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](The%20Basics%20of%20Custom%20Patches.md)

# Introduction to Quartz Composer Custom Patch Programming Guide

A patch is one of the basic elements of the Quartz Composer development tool. Similar to routines in traditional programming languages, patches are base processing units. They execute and produce a result. In OS X v10.4, all patches were built-in to Quartz Composer. Starting in OS X v10.5, you can create custom patches and package them as a Quartz Composer plug-in. After a plug-in is installed in the appropriate directory, the patches contained in it are available to use in the Quartz Composer workspace and by most Quartz Composer clients, and can be used in the same manner that you use built-in patches.

This document shows how to create custom patches and package them as Quartz Composer plug-ins. You’ll see how to code a variety of patches from a simple string-processing patch to one that renders using OpenGL.

Anyone who uses the Quartz Composer development tool and wants to create a custom patch should read this document. To get the most out of this document, you’ll need to be familiar with _[Quartz Composer User Guide](../Quartz%20Composer%20User%20Guide/Introduction%20to%20Quartz%20Composer%20User%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgobr)_. You’ll also need to know how to use Xcode to create an Objective-C project. Although Quartz Composer uses OpenGL when it renders, you don’t need to know OpenGL to write a custom patch unless you want to create a custom patch that renders on the GPU. This document shows how to write both non-rendering and rendering custom patches.

You can use the properties feature of Objective-C 2.0 when creating a custom patch. If you are unfamiliar with properties, you’ll want to read about them before you start writing custom patches. This feature is a time saver that eliminates the need to write accessor methods. All the examples in this document use properties. See _[The Objective-C Programming Language](../../Cocoa/The%20Objective-C%20Programming%20Language/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrt)_.

This document is organized into the following chapters:

- [The Basics of Custom Patches](The%20Basics%20of%20Custom%20Patches.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2doobxfvbuqmznknltc) describes how the patches that appear in Quartz Composer relate to the code that generates a custom patch. It provides an overview of the tasks needed to create a custom patch and package it as a plug-in. It also describes the Xcode templates that you can use to write custom patches.
- [Writing Processor Patches](Writing%20Processor%20Patches.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2doobxfvbuqnbnknltc) shows how to write three patches that process data—one that processes a string, another that converts a numeric value to a color, and another that shows how to configure a parameter that can’t be represented by one of the standard port data types.
- [Writing Image Processing Patches](Writing%20Image%20Processing%20Patches.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2doobxfvbuqnznknltc) describes how to use input and output image protocols to create a patch that produces an image by operating on two input images.
- [Writing Consumer Patches](Writing%20Consumer%20Patches.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2doobxfvbuqnjnknltc) discusses how to use OpenGL in a custom patch and provides instructions for writing a patch that renders a quad that you can animate.

The following resources are valuable to anyone writing a custom patch and packaging it as a Quartz Composer plug-in:

- Several of the sample code projects in `/Developer/Examples/Quartz Composer/Plugins` are custom patch projects.
- _[Quartz Composer User Guide](../Quartz%20Composer%20User%20Guide/Introduction%20to%20Quartz%20Composer%20User%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgobr)_ describes the development tool and how to use it to create compositions.
- _[Quartz Composer Programming Guide](../Quartz%20Composer%20Programming%20Guide/Introduction%20to%20Quartz%20Composer%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjx)_ shows how to perform programming tasks using the Quartz Composer framework.
- _Quartz Composer Reference Collection_ describes all the classes and protocols in the Quartz Composer API. You’ll need to refer to this documentation as you write Quartz Composer custom patches.
- _[Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)_ contains valuable information for anyone who is unfamiliar this mechanism for getting and setting values.
[Next](The%20Basics%20of%20Custom%20Patches.md)

