---
title: Core Video Programming Guide
apple_id: TP40001536
resource_type: Guide
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QuartzCore
published: '2007-04-03'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreVideo/CVProg_Intro/CVProg_Intro.html
archived_at: '2026-07-15T07:35:40.018963Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Core%20Video%20Concepts.md)

# Introduction to Core Video Programming Guide

This document explains Core Video concepts and describes how to obtain and manipulate video frames using the Core Video programming interface.

Core Video is a new pipeline model for digital video in OS X. Partitioning the processing into discrete steps makes it simpler for developers to access and manipulate individual frames without having to worry about translating between data types (QuickTime, OpenGL, and so on) or display synchronization issues.

Core Video is comparable to the Core Image and Core Audio technologies.

Core Video is available in:

- OS X v10.4 and later
- OS X v10.3 when QuickTime 7.0 or later is installed

For best results, you should use Core Video functionality only on computers that support hardware graphics acceleration (that is, Quartz Extreme).

The audience for this document is any Carbon or Cocoa developer who wants a greater degree of control in manipulating video images. Developers should be familiar with digital video and OpenGL as well as multithreaded programming.

Core Video is necessary only if you want to manipulate individual video frames. For example, the following types of video processing would require Core Video:

- Color correction or other filtering, such as provided by Core Image filters
- Physical transforms of the video images (such as warping, or mapping onto a surface)
- Adding video to an OpenGL scene
- Adding additional information to frames, such as a visible timecode
- Compositing multiple video streams

If you don’t need this level of sophistication (for example, if you only want to display video in your applications), you should use the simplified movie players such as HIMovieView (in Carbon) or QTKit (in Cocoa) to display video. You can also apply effects to video using Quartz Composer.

This document is organized into the following chapters:

- [Core Video Concepts](Core%20Video%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmzwfvbuqmrqgiwueqkcjjcemsck) describes the Core Video pipeline model and explains the key concepts necessary to use the Core Video API.
- [Core Video Tasks](Core%20Video%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmzwfvbuqmrqgmwugskiinduqr2h) shows how to use Core Video to obtain and manipulate individual video frames.

Apple offers the following additional resources in the ADC Reference library that complement the _Core Video Programming Guide_:

- _Core Video Reference_ provides a detailed description of the Core Video API.
- _[OpenGL Programming Guide for Mac](../OpenGL%20Programming%20Guide%20for%20Mac/About%20OpenGL%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobx)_ provides information on GL textures and CGL graphics contexts.
- _Cocoa OpenGL_ contains information about the OpenGL classes available in Cocoa (such as NSOpenGLView).
- _[Core Image Programming Guide](../Core%20Image%20Programming%20Guide/About%20Core%20Image.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobv)_ contains information about how to create Core Image filters, which you can apply to video frames.

In addition, the OpenGL website ([http://www.opengl.org](http://www.opengl.org/)) is the primary source for information about the OpenGL API.

[Next](Core%20Video%20Concepts.md)

