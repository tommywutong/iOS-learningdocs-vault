---
title: Scroll View Programming Guide for Mac
apple_id: TP40003221
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2010-06-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSScrollViewGuide/Articles/Introduction.html
archived_at: '2026-07-15T07:16:53.400282Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](How%20Scroll%20Views%20Work.md)

# Introduction to Scroll View Programming Guide for Cocoa

A scroll view displays a portion of the contents of a view that’s too large to be displayed in a window and allows the user to move the document view within the scroll view. This document describes the `NSScrollView` class and its use.

You should read this document if your application needs to display content that is too large to fit in a single view. _[View Programming Guide](../View%20Programming%20Guide/Introduction%20to%20View%20Programming%20Guide%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzy)_ should be considered a prerequisite to this document, as is _[Cocoa Event Handling Guide](../Cocoa%20Event%20Handling%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2i)_.

_Scroll View Programming Guide for Cocoa_ consists of the following articles:

- [How Scroll Views Work](How%20Scroll%20Views%20Work.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztinrrfvjvomi) describes the components of scroll views and how they interact.
- [Creating and Configuring a Scroll View](Creating%20and%20Configuring%20a%20Scroll%20View.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztemrwfvjvomi) describes how to create and configure scroll views.
- [Scrolling the Document View](Scrolling%20the%20Document%20View.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztinrtfvjvomi) describes how an application programmatically scrolls the contents of a scroll view.
- [Synchronizing Scroll Views](Synchronizing%20Scroll%20Views.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztkmzxfvjvoni) describes how to synchronize scrolling of two scroll views.

There are other technologies, not fully covered in this document, that are fundamental to using scroll views in your application. Refer to these documents for more details:

- _[Cocoa Event Handling Guide](../Cocoa%20Event%20Handling%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2i)_ describes the event model used by Cocoa applications.
- _[Cocoa Event Handling Guide](../Cocoa%20Event%20Handling%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2i)_ describes how your application objects can handle the events that they receive and explains the responder chain.
- _[View Programming Guide](../View%20Programming%20Guide/Introduction%20to%20View%20Programming%20Guide%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzy)_ describes the view hierarchy and how to implement custom views in your application.
[Next](How%20Scroll%20Views%20Work.md)

