---
title: Detecting OpenGL Renderer Changes
apple_id: DTS40010094
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2014-06-25'
source_url: https://developer.apple.com/library/archive/samplecode/BasicMultiGPUSample/Listings/Readme_txt.html
archived_at: '2026-07-18T03:01:49.073893Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Detecting OpenGL Renderer Changes](Detecting%20OpenGL%20Renderer%20Changes.md)


[Next](main.m.md)[Previous](Detecting%20OpenGL%20Renderer%20Changes.md)

# Readme.txt

```
BasicMultiGPUSample

===================================================================================
DESCRIPTION:

This sample demonstrates what an OpenGL application should do to detect possible 
renderer changes. When running on a multi-GPU system, in order to render the OpenGL 
content correctly on all hardware, your application needs to be able to detect 
renderer changes. Whenever the virtual screen changes, the capabilities of the video 
card you are currently rendering to can change, so you must re-query those capabilities
(such as max texture size) and adjust your drawing paths as necessary to support 
the newly active GPU.

This sample demonstrates how to detect and respond to renderer changes in both 
an NSOpenGLView subclass and an NSView subclass. It also demonstrates how to enable 
the usage of offline renderers (renderers that are not connected to a display).

===================================================================================
PACKAGING LIST:

MyNSOpenGLView.h/.m
This is an NSOpenGLView subclass. Demonstrates how to detect and respond to 
renderer changes if you are using an NSOpenGLView subclass.

MyOpenGLView.h/.m
This is an NSView subclass. Demonstrates how to detect and respond to renderer 
changes if you are not using NSOpenGLView.

BoingRenderer.h/.m
This class handles the rendering of a Boing ball using Core Profile. This class 
does not contain code relevant to multi-GPU support.

===================================================================================
BUILD REQUIREMENTS:

OS X v10.9 or later

===================================================================================
RUNTIME REQUIREMENTS:

OS X v10.8 or later

===================================================================================
Copyright (C) 2013~2014 Apple Inc. All rights reserved.
```

[Next](main.m.md)[Previous](Detecting%20OpenGL%20Renderer%20Changes.md)

