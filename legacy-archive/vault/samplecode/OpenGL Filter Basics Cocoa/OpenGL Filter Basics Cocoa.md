---
title: OpenGL Filter Basics Cocoa
apple_id: DTS10004586
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2008-02-06'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGLFilterBasicsCocoa/Introduction/Intro.html
archived_at: '2026-07-18T03:18:01.691443Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Sources-Main-Classes-OpenGLBasicView.m.md)

# OpenGL Filter Basics Cocoa

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2008-02-06 How to use Objective-C and MVC design patterns in installing and utilizing filters in an OpenGL rendering pipeline |
| __Build Requirements:__ | Mac OS X 10.5 and Xcode 3.0 |
| __Runtime Requirements:__ | Mac OS X 10.5 |

This application demonstrates how to install a filter in an OpenGL pipeline using Objective-C and MVC design pattern. Here our model in the MVC design pattern is the filter object that encapsulates the OpenGL algorithmic workflows of loading, compiling, linking and binding of a fragment shader to a program object; texture initialization; framebuffer object instantiation and binding to a texture. The data generation for the filter is encapsulated in the object that produces the rotating 3D models. The controller here acts as a request broker between the filter and the view, and thus feeds the data into the filter and visualizes the results of the computation by updating an OpenGL view. This application further takes advantage of dictionaries to encapsulate the process of initialization of OpenGL viewâ€™s pixel format attributes. Dictionaries are also used to abstract the process of initializing GLSL fragment shader uniforms. Furthermore, this application also makes use of the multithreaded OpenGL engine.

[Next](Sources-Main-Classes-OpenGLBasicView.m.md)

