---
title: OpenGL Driver Monitor User Guide
apple_id: TP40006474
resource_type: Guide
platform: Xcode Developer Tools
topic: Languages & Utilities
technology: OpenGL
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGLDriverMonitorUserGuide/Introduction/Introduction.html
archived_at: '2026-07-15T07:36:51.921467Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Using%20OpenGL%20Driver%20Monitor.md)

# Introduction

OpenGL Driver Monitor is a developer tool that has two purposes. It is:

- An application that lets developers see how OpenGL works on a specific system and look at the capabilities of a driver
- An advanced diagnostic tool that OpenGL driver developers and experts can use to track down thorny performance issues

Most OpenGL developers should not use the driver monitor application to analyze performance issues; they should instead use Instruments and OpenGL Profiler.

You’ll want to read this document if you:

- Develop applications that use OpenGL on OS X and you are curious as to how the GPU and CPU interact
- Want to look at the capabilities of a particular OpenGL driver
- Are an OpenGL driver developer who needs to investigate a driver bug
- Are an advanced OpenGL developer or consultant trying to track down a performance issue that you’ve been unable to analyze using Instruments and OpenGL Profiler

This document is organized into the following chapters:

- [Using OpenGL Driver Monitor](Using%20OpenGL%20Driver%20Monitor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinzufvbuqmrnknltk) describes how to set preferences, collect real-time parameter values locally or remotely, and view renderer information.
- [Identifying and Solving Performance Issues](Identifying%20and%20Solving%20Performance%20Issues.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinzufvbuqmznknltc) provides strategies for using OpenGL Driver Monitor to analyze performance issues.
- [OpenGL Driver Monitor Parameters](OpenGL%20Driver%20Monitor%20Parameters.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinzufvbuqnbnknltkny) describes, by symbolic and descriptive names, the parameters that you can monitor.

These documents contain information that can help you analyze and optimize your OpenGL code:

- _[OpenGL Programming Guide for Mac](../OpenGL%20Programming%20Guide%20for%20Mac/About%20OpenGL%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobx)_ discusses best practices for getting optimal performance.
- _[OpenGL Profiler User Guide](../OpenGL%20Profiler%20User%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinzv)_ explains how to collect and analyze data that can help you tune your OpenGL application.
- _[Instruments User Guide](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/index.html#//apple_ref/doc/uid/TP40004652)_ describes how to optimize application performance using this tool.
[Next](Using%20OpenGL%20Driver%20Monitor.md)

