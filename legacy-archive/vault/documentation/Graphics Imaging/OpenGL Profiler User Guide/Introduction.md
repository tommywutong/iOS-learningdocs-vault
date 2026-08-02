---
title: OpenGL Profiler User Guide
apple_id: TP40006475
resource_type: Guide
platform: Xcode Developer Tools
topic: Languages & Utilities
technology: OpenGL
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGLProfilerUserGuide/Introduction/Introduction.html
archived_at: '2026-07-15T07:37:04.497474Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Getting%20Started.md)

# Introduction

OpenGL Profiler is an application that’s useful for debugging and assessing performance. It lets you look inside a running application and observe how the application uses OpenGL. It can track the OpenGL functions used by an application, how often each is used, and the execution time of each function. Using this data, you can determine how efficiently an OpenGL application uses the GPU. You can then use the data to guide application development, modifying those parts of the code that slow performance or appear to use resources inefficiently.

OpenGL Profiler has a variety of interactive features. After setting breakpoints, developers can investigate application resources (textures, programs, shaders, and so on), examine the values of OpenGL context parameters, look at buffer contents, and check other aspects of the OpenGL state.

You’ll want to read this document if you develop applications that use OpenGL on OS X. By reading it, you’ll learn how to set up OpenGL Profiler, collect data, set breakpoints, and use the results to track down problems.

This document is organized into the following chapters:

- [Getting Started](Getting%20Started.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinzvfvbuqmrqfvjvomi) shows how to get OpenGL Profiler running and how to start a profiling session.
- [Using Breakpoints](Using%20Breakpoints.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinzvfvbuqmzqfvjvomi) provides details on setting breakpoints and describes the tasks you can accomplish when your application pauses.
- [Identifying and Solving Performance Issues](Identifying%20and%20Solving%20Performance%20Issues.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinzvfvbuqnbqfvjvomi) gives advice on how to use OpenGL Profiler to track down and analyze performance issues in your application.
- [Controlling Profiling Programmatically](Controlling%20Profiling%20Programmatically.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinzvfvbuqnjqfvjvooi) describes how to add code to your application that will control various aspects of OpenGL Profiler during a profiling session.

These documents contain information that can help you analyze and optimize your OpenGL code:

- _[OpenGL Programming Guide for Mac](../OpenGL%20Programming%20Guide%20for%20Mac/About%20OpenGL%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobx)_ shows how to program using OpenGL on OS X. You’ll want to read the chapter “Improving Performance” to get an overview of the best programming practices to use as well as how to use Apple’s tools for identifying bottlenecks, and gathering and analyzing performance data.
- _[OpenGL Driver Monitor User Guide](../OpenGL%20Driver%20Monitor%20User%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinzu)_ which is a developer tool that lets you investigate how the graphics processing unit (GPU) works on a system-wide basis.
- _[Instruments User Guide](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/index.html#//apple_ref/doc/uid/TP40004652)_ describes how to use Instruments to profile your application.
[Next](Getting%20Started.md)

