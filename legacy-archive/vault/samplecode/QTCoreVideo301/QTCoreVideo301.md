---
title: QTCoreVideo301
apple_id: DTS40007785
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QuartzCore
published: '2013-07-18'
source_url: https://developer.apple.com/library/archive/samplecode/QTCoreVideo301/Introduction/Intro.html
archived_at: '2026-07-18T03:20:43.914731Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Sources-Application-main.m.md)

# QTCoreVideo301

|  |  |
| --- | --- |
| __Last Revision:__ | Version 2.0, 2013-07-18 Quads use VBOs instead of display lists. GLSL program objects are generated using modern APIs. Shader packages generated using reader/writer objects for serializing/de-serializing directory of shaders. Refactored shader unit classes to use the new classes. Refactored the shaders mediator class to use the new shader units. View animation code refactored from the controller object into self-contained classes. View classes refactored into a more descriptive hierarchy. Now using Xcode 4.6 and the new llvm compiler. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydonzyguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode v4.6 |
| __Runtime Requirements:__ | Mt. Lion v10.8 |

QTCoreVideo301 is a Cocoa application demonstrating how to apply GLSL shader effects to a QuickTime Movie in realtime using GLSL fragment and vertex shaders and the Core Video texture pipeline.

This application is the fifth in a series of applications demonstrating the synergy between QTKit, CoreVideo, and OpenGL. The utility classes in QTCoreVideo301 utilizes the GLSLProgram class and introduces the notion of self-contained GLSL units (representing filters).

This sample also demonstrates, through the use of GLSL units, how to use application controls to interact dynamically with a GLSL fragment shaders. Additionally, this sample makes use of UI view animation techniques; to fade-in or fade-out controls depending on a selected video image filters (or shader).

Usage:

Using Core Video texture pipeline and OpenGL shaders, permits applications to add stunning visual effects to individual frames in realtime.

View Classes:

• AppView - The application main view, derived from QTCVOpenGLView, adding uniform and view control management. • OpenGLView - Allows you to work with OpenGLViews and interact with objects in 3D space. • QTCVOpenGLView - View class for displaying video frame as an opaque texture reference in an OpenGL view. • QTVisualContext - Utility class for managing a QT visual context.

View Animation:

• ViewAnimation - Utility class to animate views. • ViewAnimator - Mediator class for animating grouped views. • ViewEffects - Utility class for creating an effects array.

OpenGL Utiltites:

• CVGLSLUnit - A utility toolkit for managing shaders along with their uniforms for CoreVideo opaque texture references. • CVGLSLUnitMediator - A mediator class for managing all shader units. • GLSLProgram - Utility toolkit for creating a program object from fragment & vertex shaders. • GLShaderListReader - Utility toolkit for reading shaders from a serialized dictionary. • GLShaderListWriter - Utility toolkit for serializing shaders to a XML file. • GLSLUnit - A utility toolkit for managing shaders along with their uniforms. • GLQuad - Utility class for constructing VBOs for quads. • GLUniformDictionary - A utility toolkit for managing dictionary of shader uniforms.

This sample is part of the QTCoreVideo group of samples. Also see QTCoreVideo101, QTCoreVideo102, QTCoreVideo103, QTCoreVideo201, and QTCoreVideo202.

[Next](Sources-Application-main.m.md)

