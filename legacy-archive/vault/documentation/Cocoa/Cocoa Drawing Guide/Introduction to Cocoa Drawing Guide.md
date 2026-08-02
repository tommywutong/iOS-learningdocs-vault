---
title: Cocoa Drawing Guide
apple_id: TP40003290
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: null
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Introduction/Introduction.html
archived_at: '2026-07-15T07:12:29.566533Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Overview%20of%20Cocoa%20Drawing.md)

# Introduction to Cocoa Drawing Guide

High-quality graphics are an important part of a well-designed application. In fact, high-quality graphics is one of the things that sets OS X apart from many other operating systems. While some operating systems rely on flat colors and rectangular objects, OS X uses color, transparency, and its advanced compositing system to give programs a more fluid and inviting appearance.

This document is intended for developers who are new to drawing custom content using Cocoa. More advanced Cocoa developers may also want to read this book for tips on how to perform specific tasks.

Before you begin reading this document, you should be familiar with the basic concepts of how to create a Cocoa application. This includes how to create new projects in Xcode, how to create a simple nib file, and how to manipulate Cocoa objects. You do not need any understanding of graphics programming in general, although such knowledge definitely helps.

This document assumes that you are familiar with the basic concepts for creating a Cocoa application. This book also assumes that you have a basic understanding of the Objective-C programming language.

This document has the following chapters:

- [Overview of Cocoa Drawing](Overview%20of%20Cocoa%20Drawing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrqgiwueqsdjjceosck) introduces drawing-related concepts and the Cocoa support for drawing.
- [Graphics Contexts](Graphics%20Contexts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrqgmwueq2jjjdeessk) describes the drawing environment and provides examples of how you configure the environment to suit your needs.
- [Coordinate Systems and Transforms](Coordinate%20Systems%20and%20Transforms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrqgqwueq2jirfeuqsj) describes the coordinate systems used for drawing and provides examples of how you manipulate your content using transforms.
- [Color and Transparency](Color%20and%20Transparency.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrqguwueqkkirdesrsf) provides basic information about color and shows you how to use the color-related Cocoa objects.
- [Paths](Paths.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrqgywueqsdjbdeussh) describes the basic drawing tools found in Cocoa and provides detailed information about how to create and manipulate everything from simple shapes to Bezier paths.
- [Images](Images.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrqhawueq2jijbemr2k) describes the image classes found in Cocoa and provides examples of how to create and manipulate images in your application.
- [Text](Text.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrqhewueq2jivcusr2d) provides an overview of text and its relationship to the Cocoa drawing environment.
- [Advanced Drawing Techniques](Advanced%20Drawing%20Techniques.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrqg4wugsscizcukssb) demonstrates some advanced drawing-related techniques, including full-screen drawing, animation, gradients, and performance tuning.
- [Incorporating Other Drawing Technologies](Incorporating%20Other%20Drawing%20Technologies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojqfvbuqmrrgewueqkbireesqkg) provides information and examples on how to integrate advanced technologies, such as Quartz, OpenGL, and QuickTime, into your Cocoa application.

Drawing is only one step in the process of creating a fully functional Cocoa view. Understanding view hierarchies and how events interact with views are two other critical steps. For information about these other subjects, consult the following documents:

- _[View Programming Guide](../View%20Programming%20Guide/Introduction%20to%20View%20Programming%20Guide%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzy)_—for information about creating and managing views
- _[Cocoa Event Handling Guide](../Cocoa%20Event%20Handling%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2i)_—for information about event handling

To ensure the drawing in your app looks great on a Retina display, consult this document:

- _[High Resolution Guidelines for OS X](../../Graphics%20Animation/High%20Resolution%20Guidelines%20for%20OS%20X/About%20High%20Resolution%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmbs)_

Because Cocoa drawing is based on Quartz, many Quartz behaviors (though not all) are also relevant to Cocoa. This document describes the different behaviors provided by Cocoa, but for additional information about Quartz behavior, consult the following documents:

- _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_—for conceptual information related to Quartz.
[Next](Overview%20of%20Cocoa%20Drawing.md)

