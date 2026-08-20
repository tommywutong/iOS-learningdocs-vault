---
title: View Programming Guide
apple_id: TP40002978
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaViewsGuide/Introduction/Introduction.html
archived_at: '2026-07-15T07:13:23.414113Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](What%20Are%20Views.md)

# Introduction to View Programming Guide for Cocoa

A view instance is responsible for drawing and responding to user actions in a rectangular region of a window. This document describes the role of views in a Cocoa application, how to manipulate views in a window, and how to create a custom view subclass for an application.

You should read this document to gain an understanding of working with views in a Cocoa application. You are expected to be familiar with Cocoa development, including the Objective-C language and memory management. The [Creating a Custom View](Creating%20a%20Custom%20View.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzyfvbuqnznknlti) article expects that a developer is familiar with the Cocoa event model described in _[Cocoa Event Handling Guide](../Cocoa%20Event%20Handling%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2i)_ as well as the graphics drawing environment described in _[Cocoa Drawing Guide](../Cocoa%20Drawing%20Guide/Introduction%20to%20Cocoa%20Drawing%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojq)_.

_View Programming Guide for Cocoa_ consists of the following chapters:

- [What Are Views?](What%20Are%20Views.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzyfvbuqnjnknltc) describes the role of the view in Cocoa applications and an overview of the views provided by Cocoa.
- [View Geometry](View%20Geometry.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzyfvbuqmjqfvjvomi) describes how views establish their base coordinate system.
- [Working with the View Hierarchy](Working%20with%20the%20View%20Hierarchy.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzyfvbuqnbnknltc) describes how an application inserts and removes views from the view hierarchy.
- [Creating a Custom View](Creating%20a%20Custom%20View.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzyfvbuqnznknlti) describes the various aspects of `NSView` that an application can subclass, and provides a dissection of a custom `NSView` subclass.
- [Advanced Custom View Tasks](Advanced%20Custom%20View%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzyfvbuqmjsfvjvona) describes the advanced view subclass drawing tasks.
- [Optimizing View Drawing](Optimizing%20View%20Drawing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzyfvbuqmjrfvjvomi) describes techniques to optimize view drawing.

There are other technologies, not fully covered in this document, that are fundamental to using views in your application. Refer to these documents for more details:

- _[Cocoa Event Handling Guide](../Cocoa%20Event%20Handling%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2i)_ describes the event model used by Cocoa applications and explains how your objects can handle events and participate in the responder chain.
- _[Cocoa Drawing Guide](../Cocoa%20Drawing%20Guide/Introduction%20to%20Cocoa%20Drawing%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojq)_ describes the basic methods used to draw curves, fill shapes, and modify the coordinate system.
- _[Drag and Drop Programming Topics](../Drag%20and%20Drop%20Programming%20Topics/Introduction%20to%20Drag%20and%20Drop.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3ds2i)_ describes how to implement drag and drop in a view subclass.

There is also sample code available that provides detailed examples of view usage. The following sample code is installed in `/Developer/Examples/Appkit`:

- DotView is a simple application that implements a basic `NSView` subclass.
- Sketch is a scriptable graphics application. It provides a look at a complex view subclass than handles many types of events.
- Worm provides three several different `NSView` implementations that demonstrate techniques for improving a view's performance.

Additional sample code is available through Apple Developer Connection:

- [Bindings Joystick](https://developer.apple.com/samplecode/BindingsJoystick/index.html) implements a “joystick” user interface item that illustrates a bindings-enabled subclass of `NSView`.
- [ColorSampler](https://developer.apple.com/samplecode/Color_Sampler/index.html) demonstrates using `lockFocus` to read pixel colors from a view.
- [Reducer](https://developer.apple.com/samplecode/Reducer/index.html) demonstrates use of Core Image, the `NSAnimation` class, and view drawing redirection. Includes a collapsible `NSView` subclass that is Cocoa bindings-enabled.
[Next](What%20Are%20Views.md)

