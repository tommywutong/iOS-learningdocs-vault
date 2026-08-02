---
title: Metal Programming Guide
apple_id: TP40014221
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: Metal
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Device/Device.html
archived_at: '2026-07-15T08:16:51.223419Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Metal Programming Guide](About%20Metal%20and%20This%20Guide.md)


[Next](Command%20Organization%20and%20Execution%20Model.md)[Previous](About%20Metal%20and%20This%20Guide.md)

# Fundamental Metal Concepts

Metal provides a single, unified programming interface and language for both graphics and data-parallel computation workloads. Metal enables you to integrate graphics and computation tasks much more efficiently without needing to use separate APIs and shader languages.

The Metal framework provides the following:

- __Low-overhead interface.__ Metal is designed to eliminate “hidden” performance bottlenecks such as implicit state validation. You get control over the asynchronous behavior of the GPU for efficient multithreading used to create and commit command buffers in parallel.

  For details on Metal command submission, see [Command Organization and Execution Model](Command%20Organization%20and%20Execution%20Model.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqmznknltc).
- __Memory and resource management.__ The Metal framework describes buffer and texture objects that represent allocations of GPU memory. Texture objects have specific pixel formats and may be used for texture images or attachments.

  For details on Metal memory objects, see [Resource Objects: Buffers and Textures](Resource%20Objects-%20Buffers%20and%20Textures.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnbnknltc).
- __Integrated support for both graphics and compute operations.__ Metal uses the same data structures and resources (such as buffers, textures, and command queues) for both graphics and compute operations. In addition, the Metal shading language supports both graphics and compute functions. The Metal framework enables resources to be shared between the runtime interface, graphics shaders, and compute functions.

  For details on writing apps that use Metal for graphics rendering or data-parallel compute operations, see [Graphics Rendering: Render Command Encoder](Graphics%20Rendering-%20Render%20Command%20Encoder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltc) or [Data-Parallel Compute Processing: Compute Command Encoder](Data-Parallel%20Compute%20Processing-%20Compute%20Command%20Encoder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnrnknltc).
- __Precompiled shaders.__ Metal shaders can be compiled at build time along with your app code and then loaded at runtime. This workflow provides better code generation as well as easier debugging of shader code. (Metal also supports runtime compilation of shader code.)

  For details on working with Metal shaders from your Metal framework code, see [Functions and Libraries](Functions%20and%20Libraries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnjnknltc). For details on the Metal shading language itself, see _Metal Shading Language Guide_.

A Metal app cannot execute Metal commands in the background, and a Metal app that attempts this is terminated.

[Next](Command%20Organization%20and%20Execution%20Model.md)[Previous](About%20Metal%20and%20This%20Guide.md)

