---
title: FxPlug SDK Overview
apple_id: TP40002180
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/FXPlug_overview/FXPlugSDKOverview/FXPlugSDKOverview.html
archived_at: '2026-07-15T05:17:57.054199Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](What%E2%80%99s%20New%20in%20FxPlug%203.1.1.md)

# About the FxPlug SDK

The FxPlug SDK is a compact yet powerful image processing plug-in architecture that lets you create new effects for Final Cut Pro and Motion. Download the FxPlug SDK from [https://developer.apple.com/download/more/?=FXPlug](https://developer.apple.com/download/more/?=FXPlug).

Leveraging technologies such as OpenGL, OpenCL, Quartz, Quartz Composer, and Core Image, you can develop unique plug-ins that include onscreen controls and custom UI elements—all running seamlessly in the host application. FxPlug supports both hardware-accelerated and CPU-based effects.

You can write various types of plug-ins with the FxPlug SDK:

- Video filters that operate on an input video image to produce an output video image.
- Video generators that do not require an input image.

In each case, the video images can be traditional RAM-based bitmaps or hardware-accelerated OpenGL buffers.

A single plug-in can support software rendering, hardware rendering, or both. Implementing a software path is always recommended to provide compatibility with older machines that may not have Quartz Extreme–compatible video hardware.

[Next](What%E2%80%99s%20New%20in%20FxPlug%203.1.1.md)

