---
title: Detecting OpenGL Renderer Changes
apple_id: DTS40010094
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2014-06-25'
source_url: https://developer.apple.com/library/archive/samplecode/BasicMultiGPUSample/Introduction/Intro.html
archived_at: '2026-07-18T03:01:48.400190Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Readme.txt.md)

# Detecting OpenGL Renderer Changes

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.3, 2014-06-25 Replaced deprecated calls. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytambzgqwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | OS X v10.9 or later |
| __Runtime Requirements:__ | OS X v10.8 or later |

This sample demonstrates what an OpenGL application should do to detect possible renderer changes. When running on a multi-GPU system, in order to render the OpenGL content correctly on all hardware, your application needs to be able to detect renderer changes. Whenever the virtual screen changes, the capabilities of the video card you are currently rendering to can change, so you must re-query those capabilities (such as max texture size) and adjust your drawing paths as necessary to support the newly active GPU.

This sample demonstrates how to detect and respond to renderer changes in both an NSOpenGLView subclass and an NSView subclass. It also demonstrates how to enable the usage of offline renderers (renderers that are not connected to a display).

[Next](Readme.txt.md)

