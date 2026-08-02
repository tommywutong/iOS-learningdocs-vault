---
title: OpenGL ES Hardware Platform Guide for iOS
apple_id: TP40012935
resource_type: Guide
platform: iOS
topic: null
technology: null
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/OpenGLES/Conceptual/OpenGLESHardwarePlatformGuide_iOS/Introduction/Introduction.html
archived_at: '2026-07-18T01:39:27.953915Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](OpenGL%20ES%20Hardware%20Processors.md)

# Introduction to Hardware for OpenGL ES

iOS devices support a variety of graphics processors with varying capabilities. All currently shipping devices support both OpenGL ES 1.1 and OpenGL ES 2.0. Even devices that support the same version of OpenGL ES may have different capabilities depending on the version of iOS and the underlying graphics hardware. Apple offers many OpenGL ES extensions to provide new capabilities to your apps.

This document describes the details for each device to help you tailor your apps to get the highest performance and quality. The information contained here is current as of iOS 6.1, but is subject to change in future hardware or software releases.

Although this document provides important OpenGL ES hardware information, it is not definitive. If you are unfamiliar with OpenGL ES programming, consult the _[OpenGL ES Programming Guide](../3D%20Drawing/OpenGL%20ES%20Programming%20Guide/About%20OpenGL%20ES.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doojt)_ to learn how to develop OpenGL ES apps on iOS.

To allow your app to run on as many devices as possible and to ensure compatibility with future devices and iOS versions, your app must always test the capabilities of the underlying OpenGL ES implementation at runtime, disabling any features that do not have the required support from iOS. For more information about performing these tests, see Determining OpenGL ES Capabilities in _[OpenGL ES Programming Guide](../3D%20Drawing/OpenGL%20ES%20Programming%20Guide/About%20OpenGL%20ES.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doojt)_.

OpenGL ES is an open standard defined by the Khronos Group. For more information about OpenGL ES 1.1 and 2.0, consult their web page at [http://www.khronos.org/opengles/](http://www.khronos.org/opengles/).

- _[OpenGL ES Programming Guide](../3D%20Drawing/OpenGL%20ES%20Programming%20Guide/About%20OpenGL%20ES.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doojt)_ provides a comprehensive introduction for Apple developers creating OpenGL ES apps.
- [OpenGL ES API Registry](http://www.khronos.org/registry/gles/) is the official repository for the OpenGL ES 1.1 and OpenGL ES 2.0 specifications, the OpenGL ES shading language specification, and documentation for OpenGL ES extensions.
- _[OpenGL ES Framework Reference](https://developer.apple.com/documentation/opengles)_ describes the platform-specific functions and classes provided by Apple to integrate OpenGL ES into iOS.
[Next](OpenGL%20ES%20Hardware%20Processors.md)

