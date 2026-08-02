---
title: Image Capture Applications Programming Guide
apple_id: TP40005196
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: ImageCaptureCore
published: '2009-08-29'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ImageCaptureServicesProgrammingGuide/01Introduction/01Introduction.html
archived_at: '2026-07-15T05:23:12.591423Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Image%20Capture%20Overview.md)

# Introduction

OS X, version 10.6 and later, includes Objective-C classes that make it easy to find and control cameras and scanners, whether attached directly via USB or available over the network. You can browse for devices, list and download thumbnails and images, take scans, rotate or delete images and, if the device supports it, take pictures or control the scan parameters.

High-level image capture classes in the `ImageKit` framework allow you to construct applications that control cameras and scanners entirely by dragging and dropping elements in Interface Builder, literally without writing a line of code.

Similar classes in the `ImageCaptureCore` framework provide the equivalent capabilities to quickly find and control cameras and scanners, but without the built-in UI, allowing you to write headless applications or to provide your own custom UI.

If you want to find or control cameras or scanners from within your application, you should read this document.

This document is organized into the following sections:

- "[Image Capture Overview](Image%20Capture%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojwfvbuqmznknltc)”—an overview of the Image Capture API
- "[Creating an Application Using ImageKit](Creating%20an%20Application%20Using%20ImageKit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojwfvbuqnbnknltk)”— a sample camera browser application created using the `ImageKit` API.
- [Creating an Application Using ImageCaptureCore](Creating%20an%20Application%20Using%20ImageCaptureCore.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcojwfvbuqnjnknltc)”— a sample camera browser application created using the `ImageCaptureCore` API.

- _Image Kit Reference Collection_
- _Image Capture Applications Reference_
- _Image Capture Device Modules Reference_
[Next](Image%20Capture%20Overview.md)

