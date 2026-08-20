---
title: Metal Best Practices Guide
apple_id: TP40016642
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: Metal
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/3DDrawing/Conceptual/MTLBestPracticesGuide/FunctionsandLibraries.html
archived_at: '2026-07-15T03:48:49.322195Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Metal Best Practices Guide](index.md)



## Functions and Libraries

__Best Practice:__ Compile your functions and build your library at build time.

Compiling Metal shading language source code is one of the most expensive stages in the lifetime of a Metal app. Metal minimizes this cost by allowing you to compile graphics and compute functions at build time, then load them as a library at runtime.

### Build Your Library at Build Time

When you build your app, Xcode automatically compiles your `.metal` source files and builds them into a single default library. To obtain the resulting [MTLLibrary](https://developer.apple.com/documentation/metal/mtllibrary) object, call the [newDefaultLibrary](https://developer.apple.com/documentation/metal/mtldevice/1433380-newdefaultlibrary) method once during your initial Metal setup.

> [!NOTE]
> 

Building your library at runtime incurs a significant performance cost. Do so _only_ if your graphics and compute functions are created dynamically at runtime. In all other situations, always build your library at build time.

> [!IMPORTANT]
> 

### Group Your Functions into a Single Library

Using Xcode to build a single default library is the fastest and most efficient build option. If you must use Metal’s command line utilities or runtime methods to build your library, coalesce your Metal shading language source code and group all your functions into a single library. Avoid creating multiple libraries, if possible.

[Indirect Buffers](IndirectBuffers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbsfvbuqmzrfvjvomi)

[Pipelines](Pipelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbsfvbuqmrvfvjvomq)
