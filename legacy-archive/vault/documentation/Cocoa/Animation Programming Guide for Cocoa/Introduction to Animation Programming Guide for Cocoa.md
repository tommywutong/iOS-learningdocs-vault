---
title: Animation Programming Guide for Cocoa
apple_id: TP40003592
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: AppKit
published: '2006-05-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AnimationGuide/Introduction/Introduction.html
archived_at: '2026-07-15T05:25:26.408066Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Using%20an%20NSAnimation%20Object.md)

# Introduction to Animation Programming Guide for Cocoa

Cocoa provides facilities for animating certain types of operations over a finite or indefinite amount of time. The basic animation support provided by the `NSAnimation` class focuses on providing you with a source for animation timing and management. Although the word "animation" may make you think of cartoons or other forms of movies, animation objects are more designed for animating portions of your program's user interface. For example, you can use the `NSViewAnimation` class (a subclass of `NSAnimation`) to create smooth transitions in the size, position, or opacity of a view or window. This animated appearance lets you create a user interface with a more fluid appearance.

This document describes the fundamental concepts involved in using Cocoa animation objects and also provides examples of how to use them in your own applications.

This document contains the following articles:

- [Using an NSAnimation Object](Using%20an%20NSAnimation%20Object.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztkobrfvjvomi) describes the basic features of animation objects and how you customize them.
- [Animating Views and Windows](Animating%20Views%20and%20Windows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztkojtfvjvomi) describes the use of view animation objects, which provide a high-level interface for smoothly resizing, repositioning, and changing the opacity of view and window objects.

Sample code is available that provides examples for using the Cocoa animation classes:

- _[Reducer](../../../samplecode/Reducer/Reducer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnrsgy)_ implements a reusable collapsible view (using `NSViewAnimation`) and an animated tab view class subclass of `NSAnimation`.
- _[iSpend](../../../samplecode/iSpend/iSpend.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnrsgu)_ implements an expanding view using `NSViewAnimation`.
[Next](Using%20an%20NSAnimation%20Object.md)

