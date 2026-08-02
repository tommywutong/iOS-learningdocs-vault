---
title: Metal Programming Guide
apple_id: TP40014221
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: Metal
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html
archived_at: '2026-07-15T08:16:51.232042Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Fundamental%20Metal%20Concepts.md)

# About Metal and This Guide

The Metal framework supports GPU-accelerated advanced 3D graphics rendering and data-parallel computation workloads. Metal provides a modern and streamlined API for fine-grained, low-level control of the organization, processing, and submission of graphics and computation commands, as well as the management of the associated data and resources for these commands. A primary goal of Metal is to minimize the CPU overhead incurred by executing GPU workloads.

This document describes the fundamental concepts of Metal: the command submission model, the memory management model, and the use of independently compiled code for graphics shader and data-parallel computation functions. The document then details how to use the Metal API to write an app.

You can find more details in the following chapters:

- [Fundamental Metal Concepts](Fundamental%20Metal%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqmrnknltc) briefly describes the main features of Metal.
- [Command Organization and Execution Model](Command%20Organization%20and%20Execution%20Model.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqmznknltc) explains how to create and submit commands to the GPU for execution.
- [Resource Objects: Buffers and Textures](Resource%20Objects-%20Buffers%20and%20Textures.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnbnknltc) discusses the management of device memory, including buffer and texture objects that represent GPU memory allocations.
- [Functions and Libraries](Functions%20and%20Libraries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnjnknltc) describes how Metal shading language code can be represented in a Metal app, and how Metal shading language code is loaded onto and executed by the GPU.
- [Graphics Rendering: Render Command Encoder](Graphics%20Rendering-%20Render%20Command%20Encoder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltc) describes how to render 3D graphics, including how to distribute graphics operations across multiple threads.
- [Data-Parallel Compute Processing: Compute Command Encoder](Data-Parallel%20Compute%20Processing-%20Compute%20Command%20Encoder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnrnknltc) explains how to perform data-parallel processing.
- [Buffer and Texture Operations: Blit Command Encoder](Buffer%20and%20Texture%20Operations-%20Blit%20Command%20Encoder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqojnknltg) describes how to copy data between textures and buffers.
- [Metal Tools](Metal%20Tools.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqobnknltc) lists the tools available to help you customize and improve your development workflow.
- [Metal Feature Set Tables](Metal%20Feature%20Set%20Tables.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqmjtfvjvomi) lists the feature availability, implementation limits, and pixel format capabilities of each Metal feature set.
- [What's New in iOS 9 and OS X 10.11](What%27s%20New%20in%20iOS%209%20and%20OS%20X%2010.11.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqmjsfvjvomjr) summarizes the new features introduced in iOS 9 and OS X 10.11.
- [What’s New in iOS 10, tvOS 10, and OS X 10.12](What%E2%80%99s%20New%20in%20iOS%2010%2C%20tvOS%2010%2C%20and%20macOS%2010.12.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqmjufvjvomi) summarizes the new features introduced in iOS 10, tvOS 10, and OS X 10.12.
- [Tessellation](Tessellation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqmjvfvjvomi) describes the Metal tessellation pipeline used to tessellate a patch, including the use of a compute kernel, tessellator, and post-tessellation vertex function.
- [Resource Heaps](Resource%20Heaps.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqmjwfvjvomi) describes how to sub-allocate resources from a heap, alias between them, and track them with a fence.

You should be familiar with the Objective-C language and experienced in programming with OpenGL, OpenCL, or similar APIs.

The _[Metal Framework Reference](https://developer.apple.com/documentation/metal)_ is a collection of documents that describes the interfaces in the Metal framework.

The [Metal Shading Language Specification](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf) is a document that specifies the Metal shading language, which is used to write a graphics shader or a compute function that is used by a Metal app.

In addition, several sample code projects using Metal are available in the Apple Developer Library.

[Next](Fundamental%20Metal%20Concepts.md)

