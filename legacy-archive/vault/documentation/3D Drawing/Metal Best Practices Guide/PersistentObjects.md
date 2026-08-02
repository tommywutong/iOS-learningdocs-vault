---
title: Metal Best Practices Guide
apple_id: TP40016642
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: Metal
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/3DDrawing/Conceptual/MTLBestPracticesGuide/PersistentObjects.html
archived_at: '2026-07-15T03:48:56.130022Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Metal Best Practices Guide](index.md)



## Persistent Objects

__Best Practice:__ Create persistent objects early and reuse them often.

The Metal framework provides protocols to manage persistent objects throughout the lifetime of your app. These objects are expensive to create but are usually initialized once and reused often. You do not need to create these objects at the beginning of every render or compute loop.

### Initialize Your Device and Command Queue First

Call the [MTLCreateSystemDefaultDevice](https://developer.apple.com/documentation/metal/1433401-mtlcreatesystemdefaultdevice) function at the start of your app to obtain the default system device. Next, call the [newCommandQueue](https://developer.apple.com/documentation/metal/mtldevice/1433388-newcommandqueue) or [newCommandQueueWithMaxCommandBufferCount:](https://developer.apple.com/documentation/metal/mtldevice/1433433-makecommandqueue) method to create a command queue for executing GPU instructions on that device.

All apps should create only one [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice) object per GPU and reuse it for all your Metal work on that GPU. Most apps should create only one [MTLCommandQueue](https://developer.apple.com/documentation/metal/mtlcommandqueue) object per GPU, though you may want more if each command queue represents different Metal work (for example, non-real-time compute processing and real-time graphics rendering).

> [!NOTE]
> 

### Compile Your Functions and Build Your Library at Build Time

For an overview of compiling your functions and building your library at build time, see the [Functions and Libraries](FunctionsandLibraries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbsfvbuqmrufvjvomi) best practices.

At runtime, use the [MTLLibrary](https://developer.apple.com/documentation/metal/mtllibrary) and [MTLFunction](https://developer.apple.com/documentation/metal/mtlfunction) objects to access your library of graphics and compute functions. Avoid building your library at runtime or fetching functions during a render or compute loop.

If you need to configure multiple render or compute pipelines, reuse [MTLFunction](https://developer.apple.com/documentation/metal/mtlfunction) objects whenever possible. You can release [MTLLibrary](https://developer.apple.com/documentation/metal/mtllibrary) and [MTLFunction](https://developer.apple.com/documentation/metal/mtlfunction) objects after building all render and compute pipelines that depend on them.

### Build Your Pipelines Once and Reuse Them Often

Building a programmable pipeline involves an expensive evaluation of GPU state. You should build [MTLRenderPipelineState](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate) and [MTLComputePipelineState](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate) objects only once, then reuse them for every new render or compute command encoder you create. Do not build new pipelines for new command encoders. For an overview of building multiple pipelines asynchronously, see the [Pipelines](Pipelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbsfvbuqmrvfvjvomq) best practices.

> [!NOTE]
> 

### Allocate Resource Storage Up Front

Resource data may be static or dynamic and accessed at various stages throughout the lifetime of your app. However, the [MTLBuffer](https://developer.apple.com/documentation/metal/mtlbuffer) and [MTLTexture](https://developer.apple.com/documentation/metal/mtltexture) objects that allocate memory for this data should be created as early as possible. After these objects are created, the resource properties and storage allocation are immutable, but the data itself is not; you can update the data whenever necessary.

Reuse [MTLBuffer](https://developer.apple.com/documentation/metal/mtlbuffer) and [MTLTexture](https://developer.apple.com/documentation/metal/mtltexture) objects as much as possible, particularly for static data. Avoid creating new resources during a render or compute loop, even for dynamic data. For further information about buffers and textures, see the [Resource Management](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbsfvbuqmznknltc) and [Triple Buffering](TripleBuffering.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbsfvbuqnjnknltc) best practices.

[Fundamental Concepts](index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbsfvbuqmrxfvjvomi)

[Resource Options](ResourceOptions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbsfvbuqmjxfvjvomi)
