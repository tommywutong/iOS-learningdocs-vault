---
title: Quartz Display Services Programming Topics
apple_id: TP40004316
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzDisplayServicesConceptual/Introduction/Introduction.html
archived_at: '2026-07-15T07:38:03.988905Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Overview%20of%20Quartz%20Display%20Services.md)

# Introduction to Quartz Display Services Programming Topics

Quartz Display Services is an API that provides direct access to certain low-level features in the OS X window server. Quartz Display Services addresses two important types of functionality: the configuration and control of display hardware.

This document is a collection of short articles that provides an overview of Quartz Display Services and shows how to use this API to accomplish some basic tasks. These articles are recommended reading for software developers working on applications (for example: games and media players) that need advanced control of displays.

This document contains the following articles:

- [Overview of Quartz Display Services](Overview%20of%20Quartz%20Display%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2demrwfvjvomi) gives a brief introduction and defines some important terms.
- [Getting Information About Displays](Getting%20Information%20About%20Displays.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denzsfvjvomi) briefly describes some of the accessor functions and shows how to retrieve display properties from a display mode dictionary.
- [Capturing Displays](Capturing%20Displays.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2demryfvjvomi) shows how to get exclusive use of a display for full screen drawing.
- [Changing Display Modes (OS X v10.6 or later)](Changing%20Display%20Modes%20%28OS%20X%20v10.6%20or%20later%29.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2demzufvjvomi) shows how to switch a display to a different display mode on OS X v10.6 or later.
- [Changing Display Modes (OS X v10.5)](Changing%20Display%20Modes%20%28OS%20X%20v10.5%29.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjsfvjvomi) shows how to switch a display to a different display mode on OS X v10.5.
- [Configuring Displays Using a Transaction](Configuring%20Displays%20Using%20a%20Transaction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2demzqfvjvomi) shows how to reconfigure one or more displays in a single operation.
- [Using Fade Effects](Using%20Fade%20Effects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2demzsfvjvomi) shows how to fade displays during mode transitions or other configuration changes.
- [Notification of Configuration Changes](Notification%20of%20Configuration%20Changes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2demzvfvjvomi) shows how to use a notification callback to learn about display configuration changes.
- [Controlling the Mouse Cursor](Controlling%20the%20Mouse%20Cursor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denrzfvjvomi) shows how to control the visibility and location of the mouse cursor.

These additional resources are available in the ADC Reference Library:

- _[Quartz Display Services Reference](https://developer.apple.com/documentation/coregraphics/quartz_display_services)_ describes the functions, data types, and constants in Quartz Display Services.
- In _[OpenGL Programming Guide for Mac](../OpenGL%20Programming%20Guide%20for%20Mac/About%20OpenGL%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobx)_, the chapter “Drawing to the Full Screen” shows how to use Quartz Display Services to switch to full-screen display mode and change screen resolutions.
- In _[Quartz Composer Programming Guide](../Quartz%20Composer%20Programming%20Guide/Introduction%20to%20Quartz%20Composer%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjx)_, the chapter “Using QCRenderer to Play a Composition” shows how to use Quartz Display Services and Quartz Composer to render a composition to the full screen.
[Next](Overview%20of%20Quartz%20Display%20Services.md)

