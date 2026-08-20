---
title: Metal Programming Guide
apple_id: TP40014221
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: Metal
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Render-Ctx/Render-Ctx.html
archived_at: '2026-07-15T08:16:51.277551Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Metal Programming Guide](About%20Metal%20and%20This%20Guide.md)


[Next](Data-Parallel%20Compute%20Processing-%20Compute%20Command%20Encoder.md)[Previous](Functions%20and%20Libraries.md)

# Graphics Rendering: Render Command Encoder

This chapter describes how to create and work with [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder) and [MTLParallelRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder) objects, which are used to encode graphics rendering commands into a command buffer. `MTLRenderCommandEncoder` commands describe a graphics rendering pipeline, as seen in Figure 5-1.

__Figure 5-1__  Metal Graphics Rendering Pipeline

!!

A `MTLRenderCommandEncoder` object represents a single rendering command encoder. A `MTLParallelRenderCommandEncoder` object enables a single rendering pass to be broken into a number of separate `MTLRenderCommandEncoder` objects, each of which may be assigned to a different thread. The commands from the different render command encoders are then chained together and executed in a consistent, predictable order, as described in [Multiple Threads for a Rendering Pass](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltcnq).

To create, initialize, and use a single render command encoder:

1. Create a [MTLRenderPassDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor) object to define a collection of attachments that serve as the rendering destination for the graphics commands in the command buffer for that rendering pass. Typically, you create a `MTLRenderPassDescriptor` object once and reuse it each time your app renders a frame. See [Creating a Render Pass Descriptor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltk).
2. Create a `MTLRenderCommandEncoder` object by calling the [renderCommandEncoderWithDescriptor:](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1442999-rendercommandencoderwithdescript) method of [MTLCommandBuffer](https://developer.apple.com/documentation/metal/mtlcommandbuffer) with the specified render pass descriptor. See [Using the Render Pass Descriptor to Create a Render Command Encoder](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltcmi).
3. Create a [MTLRenderPipelineState](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate) object to define the state of the graphics rendering pipeline (including shaders, blending, multisampling, and visibility testing) for one or more draw calls. To use this render pipeline state for drawing primitives, call the [setRenderPipelineState:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515811-setrenderpipelinestate) method of `MTLRenderCommandEncoder`. For details, see [Creating a Render Pipeline State](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltgny).
4. Set textures, buffers, and samplers to be used by the render command encoder, as described in [Specifying Resources for a Render Command Encoder](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltcma).
5. Call `MTLRenderCommandEncoder` methods to specify additional fixed-function state, including the depth and stencil state, as explained in [Fixed-Function State Operations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltgoa).
6. Finally, call `MTLRenderCommandEncoder` methods to draw graphics primitives, as described in [Drawing Geometric Primitives](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltgoi).

A [MTLRenderPassDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor) object represents the destination for the encoded rendering commands, which is a collection of attachments. The properties of a render pass descriptor may include an array of up to four attachments for color pixel data, one attachment for depth pixel data, and one attachment for stencil pixel data. The [renderPassDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/1437979-renderpassdescriptor) convenience method creates a `MTLRenderPassDescriptor` object with color, depth, and stencil attachment properties with default attachment state. The [visibilityResultBuffer](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/1437942-visibilityresultbuffer) property specifies a buffer where the device can update to indicate whether any samples pass the depth and stencil tests—for details, see [Fixed-Function State Operations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltgoa).

Each individual attachment, including the texture that will be written to, is represented by an attachment descriptor. For an attachment descriptor, the pixel format of the associated texture must be chosen appropriately to store color, depth, or stencil data. For a color attachment descriptor, [MTLRenderPassColorAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpasscolorattachmentdescriptor), use a color-renderable pixel format. For a depth attachment descriptor, [MTLRenderPassDepthAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassdepthattachmentdescriptor), use a depth-renderable pixel format, such as [MTLPixelFormatDepth32Float](https://developer.apple.com/documentation/metal/mtlpixelformat/depth32float). For a stencil attachment descriptor, [MTLRenderPassStencilAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassstencilattachmentdescriptor), use a stencil-renderable pixel format, such as [MTLPixelFormatStencil8](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatstencil8).

The amount of memory the texture actually uses per pixel on the device does not always match the size of the texture’s pixel format in the Metal framework code, because the device adds padding for alignment or other purposes. See the [Metal Feature Set Tables](Metal%20Feature%20Set%20Tables.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqmjtfvjvomi) chapter for how much memory is actually used for each pixel format, as well limitations on the size and number of attachments.

The [loadAction](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/1437905-loadaction) and [storeAction](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/1437956-storeaction) properties of an attachment descriptor specify an action that is performed at either the start or end of a rendering pass. (For `MTLParallelRenderCommandEncoder`, the load and store actions occur at the boundaries of the overall command, not for each of its `MTLRenderCommandEncoder` objects. For details, see [Multiple Threads for a Rendering Pass](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltcnq).)

Possible [loadAction](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/1437905-loadaction) values include:

- [MTLLoadActionClear](https://developer.apple.com/documentation/metal/mtlloadaction/clear), which writes the same value to every pixel in the specified attachment descriptor. For more detail about this action, see [Specifying the Clear Load Action](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknlto).
- [MTLLoadActionLoad](https://developer.apple.com/documentation/metal/mtlloadaction/load), which preserves the existing contents of the texture.
- [MTLLoadActionDontCare](https://developer.apple.com/documentation/metal/mtlloadaction/dontcare), which allows each pixel in the attachment to take on any value at the start of the rendering pass.

If your application will render all pixels of the attachment for a given frame, use the default load action [MTLLoadActionDontCare](https://developer.apple.com/documentation/metal/mtlloadaction/dontcare). The `MTLLoadActionDontCare` action allows the GPU to avoid loading the existing contents of the texture, ensuring the best performance. Otherwise, you can use the [MTLLoadActionClear](https://developer.apple.com/documentation/metal/mtlloadaction/clear) action to clear the previous contents of the attachment, or the [MTLLoadActionLoad](https://developer.apple.com/documentation/metal/mtlloadaction/load) action to preserve them. The `MTLLoadActionClear` action also avoids loading the existing texture contents, but it incurs the cost of filling the destination with a solid color.

Possible [storeAction](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/1437956-storeaction) values include:

- [MTLStoreActionStore](https://developer.apple.com/documentation/metal/mtlstoreaction/mtlstoreactionstore), which saves the final results of the rendering pass into the attachment.
- [MTLStoreActionMultisampleResolve](https://developer.apple.com/documentation/metal/mtlstoreaction/mtlstoreactionmultisampleresolve), which resolves the multisample data from the render target into single sample values, stores them in the texture specified by the attachment property `resolveTexture`, and leaves the contents of the attachment undefined. For details, see [Example: Creating a Render Pass Descriptor for Multisampled Rendering](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknlteny).
- [MTLStoreActionDontCare](https://developer.apple.com/documentation/metal/mtlstoreaction/dontcare), which leaves the attachment in an undefined state after the rendering pass is complete. This may improve performance as it enables the implementation to avoid any work necessary to preserve the rendering results.

For color attachments, the [MTLStoreActionStore](https://developer.apple.com/documentation/metal/mtlstoreaction/mtlstoreactionstore) action is the default store action, because applications almost always preserve the final color values in the attachment at the end of rendering pass. For depth and stencil attachments, [MTLStoreActionDontCare](https://developer.apple.com/documentation/metal/mtlstoreaction/dontcare) is the default store action, because those attachments typically do not need to be preserved after the rendering pass is complete.

If the [loadAction](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/1437905-loadaction) property of an attachment descriptor is set to [MTLLoadActionClear](https://developer.apple.com/documentation/metal/mtlloadaction/clear), then a clearing value is written to every pixel in the specified attachment descriptor at the start of a rendering pass. The clearing value property depends upon the type of attachment.

- For [MTLRenderPassColorAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpasscolorattachmentdescriptor), [clearColor](https://developer.apple.com/documentation/metal/mtlrenderpasscolorattachmentdescriptor/1437924-clearcolor) contains a [MTLClearColor](https://developer.apple.com/documentation/metal/mtlclearcolor) value that consists of four double-precision floating-point RGBA components and is used to clear the color attachment. The [MTLClearColorMake](https://developer.apple.com/documentation/metal/1437971-mtlclearcolormake) function creates a clear color value from red, green, blue, and alpha components. The default clear color is (0.0, 0.0, 0.0, 1.0), or opaque black.
- For [MTLRenderPassDepthAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassdepthattachmentdescriptor), [clearDepth](https://developer.apple.com/documentation/metal/mtlrenderpassdepthattachmentdescriptor/1437933-cleardepth) contains one double-precision floating-point clearing value in the range [0.0, 1.0] that is used to clear the depth attachment. The default value is 1.0.
- For [MTLRenderPassStencilAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassstencilattachmentdescriptor), [clearStencil](https://developer.apple.com/documentation/metal/mtlrenderpassstencilattachmentdescriptor/1437931-clearstencil) contains one 32-bit unsigned integer that is used to clear the stencil attachment. The default value is 0.

Listing 5-1 creates a simple render pass descriptor with color and depth attachments. First, two texture objects are created, one with a color-renderable pixel format and the other with a depth pixel format. Next the [renderPassDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/1437979-renderpassdescriptor) convenience method of [MTLRenderPassDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor) creates a default render pass descriptor. Then the color and depth attachments are accessed through the properties of `MTLRenderPassDescriptor`. The textures and actions are set in `colorAttachments[0]`, which represents the first color attachment (at index 0 in the array), and the depth attachment.

__Listing 5-1__  Creating a Render Pass Descriptor with Color and Depth Attachments

```
MTLTextureDescriptor *colorTexDesc = [MTLTextureDescriptor
           texture2DDescriptorWithPixelFormat:MTLPixelFormatRGBA8Unorm
           width:IMAGE_WIDTH height:IMAGE_HEIGHT mipmapped:NO];
id <MTLTexture> colorTex = [device newTextureWithDescriptor:colorTexDesc];

MTLTextureDescriptor *depthTexDesc = [MTLTextureDescriptor
           texture2DDescriptorWithPixelFormat:MTLPixelFormatDepth32Float
           width:IMAGE_WIDTH height:IMAGE_HEIGHT mipmapped:NO];
id <MTLTexture> depthTex = [device newTextureWithDescriptor:depthTexDesc];

MTLRenderPassDescriptor *renderPassDesc = [MTLRenderPassDescriptor renderPassDescriptor];
renderPassDesc.colorAttachments[0].texture = colorTex;
renderPassDesc.colorAttachments[0].loadAction = MTLLoadActionClear;
renderPassDesc.colorAttachments[0].storeAction = MTLStoreActionStore;
renderPassDesc.colorAttachments[0].clearColor = MTLClearColorMake(0.0,1.0,0.0,1.0);

renderPassDesc.depthAttachment.texture = depthTex;
renderPassDesc.depthAttachment.loadAction = MTLLoadActionClear;
renderPassDesc.depthAttachment.storeAction = MTLStoreActionStore;
renderPassDesc.depthAttachment.clearDepth = 1.0;
```


To use the [MTLStoreActionMultisampleResolve](https://developer.apple.com/documentation/metal/mtlstoreaction/mtlstoreactionmultisampleresolve) action, you must set the [texture](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/1437958-texture) property to a multisample-type texture, and the [resolveTexture](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/1437926-resolvetexture) property will contain the result of the multisample resolve operation. (If `texture` does not support multisampling, then the result of a multisample resolve action is undefined.) The [resolveLevel](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/1437918-resolvelevel), [resolveSlice](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/1437966-resolveslice), and [resolveDepthPlane](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/1437960-resolvedepthplane) properties may also be used for the multisample resolve operation to specify the mipmap level, cube slice, and depth plane of the multisample texture, respectively. In most cases, the default values for `resolveLevel`, `resolveSlice`, and `resolveDepthPlane` are usable. In Listing 5-2, an attachment is initially created and then its `loadAction`, `storeAction`, `texture`, and `resolveTexture` properties are set to support multisample resolve.

__Listing 5-2__  Setting Properties for an Attachment with Multisample Resolve

```
MTLTextureDescriptor *colorTexDesc = [MTLTextureDescriptor
           texture2DDescriptorWithPixelFormat:MTLPixelFormatRGBA8Unorm
           width:IMAGE_WIDTH height:IMAGE_HEIGHT mipmapped:NO];
id <MTLTexture> colorTex = [device newTextureWithDescriptor:colorTexDesc];

MTLTextureDescriptor *msaaTexDesc = [MTLTextureDescriptor
           texture2DDescriptorWithPixelFormat:MTLPixelFormatRGBA8Unorm
           width:IMAGE_WIDTH height:IMAGE_HEIGHT mipmapped:NO];
msaaTexDesc.textureType = MTLTextureType2DMultisample;
msaaTexDesc.sampleCount = sampleCount;  //  must be > 1
id <MTLTexture> msaaTex = [device newTextureWithDescriptor:msaaTexDesc];

MTLRenderPassDescriptor *renderPassDesc = [MTLRenderPassDescriptor renderPassDescriptor];
renderPassDesc.colorAttachments[0].texture = msaaTex;
renderPassDesc.colorAttachments[0].resolveTexture = colorTex;
renderPassDesc.colorAttachments[0].loadAction = MTLLoadActionClear;
renderPassDesc.colorAttachments[0].storeAction = MTLStoreActionMultisampleResolve;
renderPassDesc.colorAttachments[0].clearColor = MTLClearColorMake(0.0,1.0,0.0,1.0);
```


After you create a render pass descriptor and specify its properties, use the [renderCommandEncoderWithDescriptor:](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1442999-rendercommandencoderwithdescript) method of a [MTLCommandBuffer](https://developer.apple.com/documentation/metal/mtlcommandbuffer) object to create a render command encoder, as shown in Listing 5-3.

__Listing 5-3__  Creating a Render Command Encoder with the Render Pass Descriptor

```
id <MTLRenderCommandEncoder> renderCE = [commandBuffer
                    renderCommandEncoderWithDescriptor:renderPassDesc];
```


Core Animation defines the [CAMetalLayer](https://developer.apple.com/documentation/quartzcore/cametallayer) class, which is designed for the specialized behavior of a layer-backed view whose content is rendered using Metal. A `CAMetalLayer` object represents information about the geometry of the content (position and size), its visual attributes (background color, border, and shadow), and the resources used by Metal to present the content in a color attachment. It also encapsulates the timing of content presentation so that the content can be displayed as soon as it is available or at a specified time. For more information about Core Animation, see the _[Core Animation Programming Guide](../../Cocoa/Core%20Animation%20Programming%20Guide/About%20Core%20Animation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmju)_.

Core Animation also defines the [CAMetalDrawable](https://developer.apple.com/documentation/quartzcore/cametaldrawable) protocol for objects that are displayable resources. The `CAMetalDrawable` protocol extends `MTLDrawable` and provides an object that conforms to the [MTLTexture](https://developer.apple.com/documentation/metal/mtltexture) protocol, so it can be used as a destination for rendering commands. To render into a `CAMetalLayer` object, you should get a new `CAMetalDrawable` object for each rendering pass, get the `MTLTexture` object that it provides, and use that texture to create the color attachment. Unlike color attachments, creation and destruction of a depth or stencil attachment are costly. If you need either depth or stencil attachments, create them once and then reuse them each time a frame is rendered.

Typically, you use the [layerClass](https://developer.apple.com/documentation/uikit/uiview/1622626-layerclass) method to designate `CAMetalLayer` as the backing layer type for your own custom UIView subclass, as shown in Listing 5-4. Otherwise, you can create a `CAMetalLayer` with its `init` method and include the layer in an existing view.

__Listing 5-4__  Using CAMetalLayer as the backing layer for a UIView subclass

```objc
+ (id) layerClass {
    return [CAMetalLayer class];
}
```

To display content rendered by Metal in the layer, you must obtain a displayable resource (a [CAMetalDrawable](https://developer.apple.com/documentation/quartzcore/cametaldrawable) object) from the `CAMetalLayer` object and then render to the texture in this resource by attaching it to a [MTLRenderPassDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor) object. To do this, you first set properties of the `CAMetalLayer` object that describe the drawable resources it provides, then call its [nextDrawable](https://developer.apple.com/documentation/quartzcore/cametallayer/1478172-nextdrawable) method each time you begin rendering a new frame. If the `CAMetalLayer` properties are not set, the `nextDrawable` method call fails. The following `CAMetalLayer` properties describe the drawable object:

- The [device](https://developer.apple.com/documentation/quartzcore/cametallayer/1478163-device) property declares the [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice) object that the resource is created from.
- The [pixelFormat](https://developer.apple.com/documentation/quartzcore/cametallayer/1478155-pixelformat) property declares the pixel format of the texture. The supported values are [MTLPixelFormatBGRA8Unorm](https://developer.apple.com/documentation/metal/mtlpixelformat/bgra8unorm) (the default) and [MTLPixelFormatBGRA8Unorm_sRGB](https://developer.apple.com/documentation/metal/mtlpixelformat/bgra8unorm_srgb).
- The [drawableSize](https://developer.apple.com/documentation/quartzcore/cametallayer/1478174-drawablesize) property declares the dimensions of the texture in device pixels. To ensure that your app renders content at the precise dimensions of the display (without requiring an additional sampling stage on some devices), take the target screen’s [nativeScale](https://developer.apple.com/documentation/uikit/uiscreen/1617825-nativescale) or [nativeBounds](https://developer.apple.com/documentation/uikit/uiscreen/1617810-nativebounds) property into account when calculating the desired size for your layer.
- The [framebufferOnly](https://developer.apple.com/documentation/quartzcore/cametallayer/1478168-framebufferonly) property declares whether the texture can be used only as an attachment (`YES`) or whether it can also be used for texture sampling and pixel read/write operations (`NO`). If `YES`, the layer object can optimize the texture for display. For most apps, the recommended value is `YES`.
- The [presentsWithTransaction](https://developer.apple.com/documentation/quartzcore/cametallayer/1478157-presentswithtransaction) property declares whether changes to the layer's rendered resource are updated with standard Core Animation transaction mechanisms (`YES`) or are updated asynchronously to normal layer updates (`NO`, the default value).

If the `nextDrawable` method succeeds, it returns a `CAMetalDrawable` object with the following read-only properties:

- The [texture](https://developer.apple.com/documentation/quartzcore/cametaldrawable/1478159-texture) property holds the texture object. You use this as an attachment when creating your rendering pipeline ([MTLRenderPipelineColorAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor) object).
- The [layer](https://developer.apple.com/documentation/quartzcore/cametaldrawable/1478165-layer) property points to the `CAMetalLayer` object that responsible for displaying the drawable.

To display the contents of a drawable object after rendering is complete, you must submit it to Core Animation by calling the drawable object’s [present](https://developer.apple.com/documentation/metal/mtldrawable/1470284-present) method. To synchronize presentation of a drawable with completion of the command buffer responsible for its rendering, you can call either the [presentDrawable:](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443029-present) or [presentDrawable:atTime:](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1442989-present) convenience method on a [MTLCommandBuffer](https://developer.apple.com/documentation/metal/mtlcommandbuffer) object. These methods use the scheduled handler (see [Registering Handler Blocks for Command Buffer Execution](Command%20Organization%20and%20Execution%20Model.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqmznknltema)) to call the drawable’s `present` method, which covers most scenarios. The `presentDrawable:atTime:` method provides further control over when the drawable is presented.

To use a [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder) object to encode rendering commands, you must first specify a [MTLRenderPipelineState](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate) object to define the graphics state for any draw calls. A render pipeline state object is a long-lived persistent object that can be created outside of a render command encoder, cached in advance, and reused across several render command encoders. When describing the same set of graphics state, reusing a previously created render pipeline state object may avoid expensive operations that re-evaluate and translate the specified state to GPU commands.

A render pipeline state is an immutable object. To create a render pipeline state, you first create and configure a mutable [MTLRenderPipelineDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor) object that describes the attributes of a render pipeline state. Then, you use the descriptor to create a [MTLRenderPipelineState](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate) object.

To create a render pipeline state, first create a [MTLRenderPipelineDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor) object, which has properties that describe the graphics rendering pipeline state you want to use during the rendering pass, as depicted in Figure 5-2. The [colorAttachments](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1514712-colorattachments) property of the new `MTLRenderPipelineDescriptor` object contains an array of [MTLRenderPipelineColorAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor) objects, and each descriptor represents a color attachment state that specifies the blend operations and factors for that attachment, as detailed in [Configuring Blending in a Render Pipeline Attachment Descriptor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltemq). The attachment descriptor also specifies the pixel format of the attachment, which must match the pixel format for the texture of the render pipeline descriptor with the corresponding attachment index, or an error occurs.

__Figure 5-2__  Creating a Render Pipeline State from a Descriptor

!

In addition to configuring the color attachments, set these properties for the [MTLRenderPipelineDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor) object:

- Set the [depthAttachmentPixelFormat](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1514608-depthattachmentpixelformat) property to match the pixel format for the texture of [depthAttachment](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/1437973-depthattachment) in [MTLRenderPassDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor).
- Set the [stencilAttachmentPixelFormat](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1514650-stencilattachmentpixelformat) property to match the pixel format for the texture of [stencilAttachment](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/1437950-stencilattachment) in [MTLRenderPassDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor).
- To specify the vertex or fragment shader in the render pipeline state, set the [vertexFunction](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1514679-vertexfunction) or [fragmentFunction](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1514600-fragmentfunction) property, respectively. Setting `fragmentFunction` to `nil` disables the rasterization of pixels into the specified color attachment, which is typically used for depth-only rendering or for outputting data into a buffer object from the vertex shader.
- If the vertex shader has an argument with per-vertex input attributes, set the [vertexDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1514681-vertexdescriptor) property to describe the organization of the vertex data in that argument, as described in [Vertex Descriptor for Data Organization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltina).
- The default value of `YES` for the [rasterizationEnabled](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1514708-rasterizationenabled) property is sufficient for most typical rendering tasks. To use only the vertex stage of the graphics pipeline (for example, to gather data transformed in a vertex shader), set this property to `NO`.
- If the attachment supports multisampling (that is, the attachment is a [MTLTextureType2DMultisample](https://developer.apple.com/documentation/metal/mtltexturetype/mtltexturetype2dmultisample) type texture), then multiple samples can be created per pixel. To determine how fragments combine to provide pixel coverage, use the following `MTLRenderPipelineDescriptor` properties.

  - The [sampleCount](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1514699-samplecount) property determines the number of samples for each pixel. When [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder) is created, the [sampleCount](https://developer.apple.com/documentation/metal/mtltexture/1515443-samplecount) for the textures for all attachments must match this `sampleCount` property. If the attachment cannot support multisampling, then `sampleCount` is 1, which is also the default value.
  - If [alphaToCoverageEnabled](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1514624-alphatocoverageenabled) is set to `YES`, then the alpha channel fragment output for `colorAttachments[0]` is read and used to determine a coverage mask.
  - If [alphaToOneEnabled](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1514697-isalphatooneenabled) is set to `YES`, then alpha channel fragment values for `colorAttachments[0]` are forced to 1.0, which is the largest representable value. (Other attachments are unaffected.)

After creating a render pipeline descriptor and specifying its properties, use it to create the [MTLRenderPipelineState](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate) object. Because creating a render pipeline state can require an expensive evaluation of graphics state and a possible compilation of the specified graphics shaders, you can use either a blocking or an asynchronous method to schedule such work in a way that best fits the design of your app.

- To synchronously create the render pipeline state object, call either the [newRenderPipelineStateWithDescriptor:error:](https://developer.apple.com/documentation/metal/mtldevice/1433369-makerenderpipelinestate) or [newRenderPipelineStateWithDescriptor:options:reflection:error:](https://developer.apple.com/documentation/metal/mtldevice/1433361-newrenderpipelinestatewithdescri) method of a [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice) object. These methods block the current thread while Metal evaluates the descriptor’s graphics state information and compiles shader code to create the pipeline state object.
- To asynchronously create the render pipeline state object, call either the [newRenderPipelineStateWithDescriptor:completionHandler:](https://developer.apple.com/documentation/metal/mtldevice/1433363-makerenderpipelinestate) or [newRenderPipelineStateWithDescriptor:options:completionHandler:](https://developer.apple.com/documentation/metal/mtldevice/1433365-makerenderpipelinestate) method of a [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice) object. These methods return immediately—Metal asynchronously evaluates the descriptor’s graphics state information and compiles shader code to create the pipeline state object, then calls your completion handler to provide the new [MTLRenderPipelineState](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate) object.

When you create a [MTLRenderPipelineState](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate) object you can also choose to create reflection data that reveals details of the pipeline’s shader function and its arguments. The [newRenderPipelineStateWithDescriptor:options:reflection:error:](https://developer.apple.com/documentation/metal/mtldevice/1433361-newrenderpipelinestatewithdescri) and [newRenderPipelineStateWithDescriptor:options:completionHandler:](https://developer.apple.com/documentation/metal/mtldevice/1433365-makerenderpipelinestate) methods provide this data. Avoid obtaining reflection data if it will not be used. For more information on how to analyze reflection data, see [Determining Function Details at Runtime](Functions%20and%20Libraries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnjnknltm).

After you create a [MTLRenderPipelineState](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate) object, call the [setRenderPipelineState:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515811-setrenderpipelinestate) method of `MTLRenderCommandEncoder` to associate the render pipeline state with the command encoder for use in rendering.

Listing 5-5 demonstrates the creation of a render pipeline state object called `pipeline`.

__Listing 5-5__  Creating a Simple Pipeline State

```
MTLRenderPipelineDescriptor *renderPipelineDesc =
                             [[MTLRenderPipelineDescriptor alloc] init];
renderPipelineDesc.vertexFunction = vertFunc;
renderPipelineDesc.fragmentFunction = fragFunc;
renderPipelineDesc.colorAttachments[0].pixelFormat = MTLPixelFormatRGBA8Unorm;

// Create MTLRenderPipelineState from MTLRenderPipelineDescriptor
NSError *errors = nil;
id <MTLRenderPipelineState> pipeline = [device
         newRenderPipelineStateWithDescriptor:renderPipelineDesc error:&errors];
assert(pipeline && !errors);

// Set the pipeline state for MTLRenderCommandEncoder
[renderCE setRenderPipelineState:pipeline];
```

The variables `vertFunc` and `fragFunc` are shader functions that are specified as properties of the render pipeline state descriptor called `renderPipelineDesc`. Calling the [newRenderPipelineStateWithDescriptor:error:](https://developer.apple.com/documentation/metal/mtldevice/1433369-makerenderpipelinestate) method of the [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice) object synchronously uses the pipeline state descriptor to create the render pipeline state object. Calling the [setRenderPipelineState:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515811-setrenderpipelinestate) method of `MTLRenderCommandEncoder` specifies the `MTLRenderPipelineState` object to use with the render command encoder.

Blending uses a highly configurable blend operation to mix the output returned by the fragment function (source) with pixel values in the attachment (destination). Blend operations determine how the source and destination values are combined with blend factors.

To configure blending for a color attachment, set the following [MTLRenderPipelineColorAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor) properties:

- To enable blending, set [blendingEnabled](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/1514642-isblendingenabled) to `YES`. Blending is disabled, by default.
- [writeMask](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/1514619-writemask) identifies which color channels are blended. The default value `MTLColorWriteMaskAll` allows all color channels to be blended.
- [rgbBlendOperation](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/1514659-rgbblendoperation) and [alphaBlendOperation](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/1514666-alphablendoperation) separately assign the blend operations for the RGB and Alpha fragment data with a `MTLBlendOperation` value. The default value for both properties is [MTLBlendOperationAdd](https://developer.apple.com/documentation/metal/mtlblendoperation/add).
- [sourceRGBBlendFactor](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/1514615-sourcergbblendfactor), [sourceAlphaBlendFactor](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/1514660-sourcealphablendfactor), [destinationRGBBlendFactor](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/1514626-destinationrgbblendfactor), and [destinationAlphaBlendFactor](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/1514657-destinationalphablendfactor) assign the source and destination blend factors.

Four blend factors refer to a constant blend color value: `MTLBlendFactorBlendColor`, `MTLBlendFactorOneMinusBlendColor`, `MTLBlendFactorBlendAlpha`, and `MTLBlendFactorOneMinusBlendAlpha`. Call the [setBlendColorRed:green:blue:alpha:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515592-setblendcolorred) method of `MTLRenderCommandEncoder` to specify the constant color and alpha values used with these blend factors, as described in [Fixed-Function State Operations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltgoa).

Some blend operations combine the fragment values by multiplying the source values by a source [MTLBlendFactor](https://developer.apple.com/documentation/metal/mtlblendfactor) value (abbreviated SBF), multiplying the destination values by a destination blend factor (DBF), and combining the results using the arithmetic indicated by the [MTLBlendOperation](https://developer.apple.com/documentation/metal/mtlblendoperation) value. (If the blend operation is either `MTLBlendOperationMin` or `MTLBlendOperationMax`, the SBF and DBF blend factors are ignored.) For example, `MTLBlendOperationAdd` for both `rgbBlendOperation` and `alphaBlendOperation` properties defines the following additive blend operation for RGB and Alpha values:

- RGB = (Source.rgb \* `sourceRGBBlendFactor`) + (Dest.rgb \* `destinationRGBBlendFactor`)
- Alpha = (Source.a \* `sourceAlphaBlendFactor`) + (Dest.a \* `destinationAlphaBlendFactor`)

In the default blend behavior, the source completely overwrites the destination. This behavior is equivalent to setting both the `sourceRGBBlendFactor` and `sourceAlphaBlendFactor` to `MTLBlendFactorOne`, and the `destinationRGBBlendFactor` and `destinationAlphaBlendFactor` to `MTLBlendFactorZero`. This behavior is expressed mathematically as:

- RGB = (Source.rgb \* 1.0) + (Dest.rgb \* 0.0)
- A = (Source.a \* 1.0) + (Dest.a \* 0.0)

Another commonly used blend operation, where the source alpha defines how much of the destination color remains, can be expressed mathematically as:

- RGB = (Source.rgb \* 1.0) + (Dest.rgb \* (1 - Source.a))
- A = (Source.a \* 1.0) + (Dest.a \* (1 - Source.a))

Listing 5-6 shows code for a custom blending configuration, using the blend operation `MTLBlendOperationAdd`, the source blend factor `MTLBlendFactorOne`, and the destination blend factor `MTLBlendFactorOneMinusSourceAlpha`. `colorAttachments[0]` is a [MTLRenderPipelineColorAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor) object with properties that specify the blending configuration.

__Listing 5-6__  Specifying a Custom Blending Configuration

```
MTLRenderPipelineDescriptor *renderPipelineDesc =                               [[MTLRenderPipelineDescriptor alloc] init]; renderPipelineDesc.colorAttachments[0].blendingEnabled = YES;  renderPipelineDesc.colorAttachments[0].rgbBlendOperation = MTLBlendOperationAdd; renderPipelineDesc.colorAttachments[0].alphaBlendOperation = MTLBlendOperationAdd; renderPipelineDesc.colorAttachments[0].sourceRGBBlendFactor = MTLBlendFactorOne; renderPipelineDesc.colorAttachments[0].sourceAlphaBlendFactor = MTLBlendFactorOne; renderPipelineDesc.colorAttachments[0].destinationRGBBlendFactor =         MTLBlendFactorOneMinusSourceAlpha; renderPipelineDesc.colorAttachments[0].destinationAlphaBlendFactor =         MTLBlendFactorOneMinusSourceAlpha;  NSError *errors = nil; id <MTLRenderPipelineState> pipeline = [device           newRenderPipelineStateWithDescriptor:renderPipelineDesc error:&errors];
```


The [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder) methods discussed in this section specify resources that are used as arguments for the vertex and fragment shader functions, which are specified by the `vertexFunction` and `fragmentFunction` properties in a [MTLRenderPipelineState](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate) object. These methods assign a shader resource (buffers, textures, and samplers) to the corresponding argument table index (`atIndex`) in the render command encoder, as shown in Figure 5-3.

__Figure 5-3__  Argument Tables for the Render Command Encoder

!

The following `setVertex*` methods assign one or more resources to corresponding arguments of a vertex shader function.

- [setVertexBuffer:offset:atIndex:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515829-setvertexbuffer)
- [setVertexBuffers:offsets:withRange:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515987-setvertexbuffers)
- [setVertexTexture:atIndex:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515842-setvertextexture)
- [setVertexTextures:withRange:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1516109-setvertextextures)
- [setVertexSamplerState:atIndex:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515537-setvertexsamplerstate)
- [setVertexSamplerState:lodMinClamp:lodMaxClamp:atIndex:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515864-setvertexsamplerstate)
- [setVertexSamplerStates:withRange:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515400-setvertexsamplerstates)
- [setVertexSamplerStates:lodMinClamps:lodMaxClamps:withRange:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1516322-setvertexsamplerstates)

These `setFragment*` methods similarly assign one or more resources to corresponding arguments of a fragment shader function.

- [setFragmentBuffer:offset:atIndex:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515470-setfragmentbuffer)
- [setFragmentBuffers:offsets:withRange:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515724-setfragmentbuffers)
- [setFragmentTexture:atIndex:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515390-setfragmenttexture)
- [setFragmentTextures:withRange:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515878-setfragmenttextures)
- [setFragmentSamplerState:atIndex:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515577-setfragmentsamplerstate)
- [setFragmentSamplerState:lodMinClamp:lodMaxClamp:atIndex:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515485-setfragmentsamplerstate)
- [setFragmentSamplerStates:withRange:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515970-setfragmentsamplerstates)
- [setFragmentSamplerStates:lodMinClamps:lodMaxClamps:withRange:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515463-setfragmentsamplerstates)

There are a maximum of 31 entries in the buffer argument table, 31 entries in the texture argument table, and 16 entries in the sampler state argument table.

The attribute qualifiers that specify resource locations in the Metal shading language source code must match the argument table indices in the Metal framework methods. In Listing 5-7, two buffers (`posBuf` and `texCoordBuf`) with indices 0 and 1, respectively, are defined for the vertex shader.

__Listing 5-7__  Metal Framework: Specifying Resources for a Vertex Function

```
[renderEnc setVertexBuffer:posBuf offset:0 atIndex:0];
[renderEnc setVertexBuffer:texCoordBuf offset:0 atIndex:1];
```

In Listing 5-8, the function signature has corresponding arguments with the attribute qualifiers `buffer(0)` and `buffer(1)`.

__Listing 5-8__  Metal Shading Language: Vertex Function Arguments Match the Framework Argument Table Indices

```
vertex VertexOutput metal_vert(float4 *posData [[ buffer(0) ]],
                               float2 *texCoordData [[ buffer(1) ]])
```

Similarly, in Listing 5-9, a buffer, a texture, and a sampler (`fragmentColorBuf`, `shadeTex`, and `sampler`, respectively), all with index 0, are defined for the fragment shader.

__Listing 5-9__  Metal Framework: Specifying Resources for a Fragment Function

```
[renderEnc setFragmentBuffer:fragmentColorBuf offset:0 atIndex:0];
[renderEnc setFragmentTexture:shadeTex atIndex:0];
[renderEnc setFragmentSamplerState:sampler atIndex:0];
```

In Listing 5-10, the function signature has corresponding arguments with the attribute qualifiers `buffer(0)`, `texture(0)`, and `sampler(0)`, respectively.

__Listing 5-10__  Metal Shading Language: Fragment Function Arguments Match the Framework Argument Table Indices

```
fragment float4 metal_frag(VertexOutput in [[stage_in]],                            float4 *fragColorData [[ buffer(0) ]],                            texture2d<float> shadeTexValues [[ texture(0) ]],                            sampler samplerValues [[ sampler(0) ]] )
```


In Metal framework code, there can be one [MTLVertexDescriptor](https://developer.apple.com/documentation/metal/mtlvertexdescriptor) for every pipeline state that describes the organization of data input to the vertex shader function and shares resource location information between the shading language and framework code.

In Metal shading language code, per-vertex inputs (such as scalars or vectors of integer or floating-point values) can be organized in one struct, which can be passed in one argument that is declared with the `[[ stage_in ]]` attribute qualifier, as seen in the `VertexInput` struct for the example vertex function `vertexMath` in Listing 5-11. Each field of the per-vertex input struct has the `[[ attribute(index) ]]` qualifier, which specifies the index in the vertex attribute argument table.

__Listing 5-11__  Metal Shading Language: Vertex Function Inputs with Attribute Indices

```
struct VertexInput {     float2    position [[ attribute(0) ]];     float4    color    [[ attribute(1) ]];     float2    uv1      [[ attribute(2) ]];     float2    uv2      [[ attribute(3) ]]; };  struct VertexOutput {     float4 pos [[ position ]];     float4 color; };  vertex VertexOutput vertexMath(VertexInput in [[ stage_in ]]) {   VertexOutput out;   out.pos = float4(in.position.x, in.position.y, 0.0, 1.0);    float sum1 = in.uv1.x + in.uv2.x;   float sum2 = in.uv1.y + in.uv2.y;   out.color = in.color + float4(sum1, sum2, 0.0f, 0.0f);   return out; }
```

To refer to the shader function input using the `[[ stage_in ]]` qualifier, describe a [MTLVertexDescriptor](https://developer.apple.com/documentation/metal/mtlvertexdescriptor) object and then set it as the [vertexDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1514681-vertexdescriptor) property of [MTLRenderPipelineState](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate). `MTLVertexDescriptor` has two properties: [attributes](https://developer.apple.com/documentation/metal/mtlvertexdescriptor/1515921-attributes) and [layouts](https://developer.apple.com/documentation/metal/mtlvertexdescriptor/1515480-layouts).

The [attributes](https://developer.apple.com/documentation/metal/mtlvertexdescriptor/1515921-attributes) property of `MTLVertexDescriptor` is a [MTLVertexAttributeDescriptorArray](https://developer.apple.com/documentation/metal/mtlvertexattributedescriptorarray) object that defines how each vertex attribute is organized in a buffer that is mapped to a vertex function argument. The `attributes` property can support access to multiple attributes (such as vertex coordinates, surface normals, and texture coordinates) that are interleaved within the same buffer. The order of the members in the shading language code does not have to be preserved in the buffer in the framework code. Each vertex attribute descriptor in the array has the following properties that provide a vertex shader function information to locate and load the argument data:

- [bufferIndex](https://developer.apple.com/documentation/metal/mtlvertexattributedescriptor/1515502-bufferindex), which is an index to the buffer argument table that specifies which `MTLBuffer` is accessed. The buffer argument table is discussed in [Specifying Resources for a Render Command Encoder](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltcma).
- [format](https://developer.apple.com/documentation/metal/mtlvertexattributedescriptor/1516081-format), which specifies how the data should be interpreted in the framework code. If the data type is not an exact type match, it may be converted or expanded. For example, if the shading language type is `half4` and the framework `format` is [MTLVertexFormatFloat2](https://developer.apple.com/documentation/metal/mtlvertexformat/float2), then when the data is used as an argument to the vertex function, it may be converted from float to half and expanded from two to four elements (with 0.0, 1.0 in the last two elements).
- [offset](https://developer.apple.com/documentation/metal/mtlvertexattributedescriptor/1515785-offset), which specifies where the data can be found from the start of a vertex.

Figure 5-4 illustrates a [MTLVertexAttributeDescriptorArray](https://developer.apple.com/documentation/metal/mtlvertexattributedescriptorarray) in Metal framework code that implements an interleaved buffer that corresponds to the input to the vertex function `vertexMath` in the shading language code in [Listing 5-11](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltimi).

__Figure 5-4__  Buffer Organization with Vertex Attribute Descriptors

!

Listing 5-12 shows the Metal framework code that corresponds to the interleaved buffer shown in Figure 5-4.

__Listing 5-12__  Metal Framework: Using a Vertex Descriptor to Access Interleaved Data

```
id <MTLFunction> vertexFunc = [library newFunctionWithName:@"vertexMath"];             MTLRenderPipelineDescriptor* pipelineDesc =                                    [[MTLRenderPipelineDescriptor alloc] init]; MTLVertexDescriptor* vertexDesc = [[MTLVertexDescriptor alloc] init];  vertexDesc.attributes[0].format = MTLVertexFormatFloat2; vertexDesc.attributes[0].bufferIndex = 0; vertexDesc.attributes[0].offset = 0; vertexDesc.attributes[1].format = MTLVertexFormatFloat4; vertexDesc.attributes[1].bufferIndex = 0; vertexDesc.attributes[1].offset = 2 * sizeof(float);  // 8 bytes vertexDesc.attributes[2].format = MTLVertexFormatFloat2; vertexDesc.attributes[2].bufferIndex = 0; vertexDesc.attributes[2].offset = 8 * sizeof(float);  // 32 bytes vertexDesc.attributes[3].format = MTLVertexFormatFloat2; vertexDesc.attributes[3].bufferIndex = 0; vertexDesc.attributes[3].offset = 6 * sizeof(float);  // 24 bytes vertexDesc.layouts[0].stride = 10 * sizeof(float);    // 40 bytes vertexDesc.layouts[0].stepFunction = MTLVertexStepFunctionPerVertex;  pipelineDesc.vertexDescriptor = vertexDesc; pipelineDesc.vertexFunction = vertFunc;
```

Each [MTLVertexAttributeDescriptor](https://developer.apple.com/documentation/metal/mtlvertexattributedescriptor) object in the [attributes](https://developer.apple.com/documentation/metal/mtlvertexdescriptor/1515921-attributes) array of the [MTLVertexDescriptor](https://developer.apple.com/documentation/metal/mtlvertexdescriptor) object corresponds to the indexed struct member in `VertexInput` in the shader function. `attributes[1].bufferIndex = 0` specifies the use of the buffer at index 0 in the argument table. (In this example, each [MTLVertexAttributeDescriptor](https://developer.apple.com/documentation/metal/mtlvertexattributedescriptor) has the same [bufferIndex](https://developer.apple.com/documentation/metal/mtlvertexattributedescriptor/1515502-bufferindex), so each refers to the same vertex buffer at index 0 in the argument table.) The [offset](https://developer.apple.com/documentation/metal/mtlvertexattributedescriptor/1515785-offset) values specify the location of data within the vertex, so `attributes[1].offset = 2 * sizeof(float)` locates the start of the corresponding data 8 bytes from the start of the buffer. The [format](https://developer.apple.com/documentation/metal/mtlvertexattributedescriptor/1516081-format) values are chosen to match the data type in the shader function, so `attributes[1].format = MTLVertexFormatFloat4` specifies the use of four floating-point values.

The [layouts](https://developer.apple.com/documentation/metal/mtlvertexdescriptor/1515480-layouts) property of `MTLVertexDescriptor` is a [MTLVertexBufferLayoutDescriptorArray](https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptorarray). For each [MTLVertexBufferLayoutDescriptor](https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptor) in [layouts](https://developer.apple.com/documentation/metal/mtlvertexdescriptor/1515480-layouts), the properties specify how vertex and attribute data are fetched from the corresponding [MTLBuffer](https://developer.apple.com/documentation/metal/mtlbuffer) in the argument table when Metal draws primitives. (For more on drawing primitives, see [Drawing Geometric Primitives](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltgoi).) The [stepFunction](https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptor/1515341-stepfunction) property of `MTLVertexBufferLayoutDescriptor` determines whether to fetch attribute data for every vertex, for some number of instances, or just once. If `stepFunction` is set to fetch attribute data for some number of instances, then the [stepRate](https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptor/1516148-steprate) property of `MTLVertexBufferLayoutDescriptor` determines how many instances. The [stride](https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptor/1515441-stride) property specifies the distance between the data of two vertices, in bytes.

Figure 5-5 depicts the [MTLVertexBufferLayoutDescriptor](https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptor) that corresponds to the code in [Listing 5-12](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltimy). `layouts[0]` specifies how vertex data is fetched from corresponding index 0 in the buffer argument table. `layouts[0].stride` specifies a distance of 40 bytes between the data of two vertices. The value of `layouts[0].stepFunction`, [MTLVertexStepFunctionPerVertex](https://developer.apple.com/documentation/metal/mtlvertexstepfunction/pervertex), specifies that attribute data is fetched for every vertex when drawing. If the value of `stepFunction` is [MTLVertexStepFunctionPerInstance](https://developer.apple.com/documentation/metal/mtlvertexstepfunction/perinstance), the `stepRate` property determines how often attribute data is fetched. For example, if `stepRate` is 1, data is fetched for every instance; if `stepRate` is 2, for every two instances, and so on.

__Figure 5-5__  Buffer Organization with Vertex Buffer Layout Descriptors

!

Use these [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder) methods to set fixed-function graphics state values:

- [setViewport:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515527-setviewport) specifies the region, in screen coordinates, which is the destination for the projection of the virtual 3D world. The viewport is 3D, so it includes depth values; for details, see [Working with Viewport and Pixel Coordinate Systems](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltgna).
- [setTriangleFillMode:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1516029-settrianglefillmode) determines whether to rasterize triangle and triangle strip primitives with lines ([MTLTriangleFillModeLines](https://developer.apple.com/documentation/metal/mtltrianglefillmode/lines)) or as filled triangles ([MTLTriangleFillModeFill](https://developer.apple.com/documentation/metal/mtltrianglefillmode/fill)). The default value is `MTLTriangleFillModeFill`.
- [setCullMode:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515975-setcullmode) and [setFrontFacingWinding:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515499-setfrontfacingwinding) are used together to determine if and how culling is applied. You can use culling for hidden surface removal on some geometric models, such as an _orientable_ sphere rendered with filled triangles. (A surface is orientable if its primitives are consistently drawn in either clockwise or counterclockwise order.)

  - The value of [setFrontFacingWinding:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515499-setfrontfacingwinding) indicates whether a front-facing primitive has its vertices drawn in clockwise ([MTLWindingClockwise](https://developer.apple.com/documentation/metal/mtlwinding/mtlwindingclockwise)) or counterclockwise ([MTLWindingCounterClockwise](https://developer.apple.com/documentation/metal/mtlwinding/mtlwindingcounterclockwise)) order. The default value is `MTLWindingClockwise`.
  - The value of [setCullMode:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515975-setcullmode) determines whether to perform culling ([MTLCullModeNone](https://developer.apple.com/documentation/metal/mtlcullmode/mtlcullmodenone), if culling disabled) or which type of primitive to cull ([MTLCullModeFront](https://developer.apple.com/documentation/metal/mtlcullmode/front) or [MTLCullModeBack](https://developer.apple.com/documentation/metal/mtlcullmode/mtlcullmodeback)).

Use the following [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder) methods to encode fixed-function state change commands:

- [setScissorRect:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515583-setscissorrect) specifies a 2D scissor rectangle. Fragments that lie outside the specified scissor rectangle are discarded.
- [setDepthStencilState:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1516119-setdepthstencilstate) sets the depth and stencil test state as described in [Depth and Stencil States](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknlts).
- [setStencilReferenceValue:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515697-setstencilreferencevalue) specifies the stencil reference value.
- [setDepthBias:slopeScale:clamp:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1516269-setdepthbias) specifies an adjustment for comparing shadow maps to the depth values output from fragment shaders.
- [setVisibilityResultMode:offset:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515556-setvisibilityresultmode) determines whether to monitor if any samples pass the depth and stencil tests. If set to [MTLVisibilityResultModeBoolean](https://developer.apple.com/documentation/metal/mtlvisibilityresultmode/boolean), then if any samples pass the depth and stencil tests, a non-zero value is written to a buffer specified by the [visibilityResultBuffer](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/1437942-visibilityresultbuffer) property of [MTLRenderPassDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor), as described in [Creating a Render Pass Descriptor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltk).

  You can use this mode to perform occlusion testing. If you draw a bounding box and no samples pass, then you may conclude that any objects within that bounding box are occluded and thus do not require rendering.
- [setBlendColorRed:green:blue:alpha:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515592-setblendcolorred) specifies the constant blend color and alpha values, as detailed in [Configuring Blending in a Render Pipeline Attachment Descriptor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltemq).

Metal defines its Normalized Device Coordinate (NDC) system as a 2x2x1 cube with its center at (0, 0, 0.5). The left and bottom for x and y, respectively, of the NDC system are specified as -1. The right and top for x and y, respectively, of the NDC system are specified as +1.

The viewport specifies the transformation from NDC to the window coordinates. The Metal viewport is a 3D transformation specified by the [setViewport:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515527-setviewport) method of [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder). The origin of the window coordinates is in the upper-left corner.

In Metal, pixel centers are offset by (0.5, 0.5). For example, the pixel at the origin has its center at (0.5, 0.5); the center of the adjacent pixel to its right is (1.5, 0.5). This is also true for textures.

The depth and stencil operations are fragment operations that you specify as follows:

1. Specify a custom [MTLDepthStencilDescriptor](https://developer.apple.com/documentation/metal/mtldepthstencildescriptor) object that contains settings for the depth/stencil state. Creating a custom `MTLDepthStencilDescriptor` object may require creating one or two [MTLStencilDescriptor](https://developer.apple.com/documentation/metal/mtlstencildescriptor) objects that are applicable to front-facing primitives and back-facing primitives.
2. Create a [MTLDepthStencilState](https://developer.apple.com/documentation/metal/mtldepthstencilstate) object by calling the [newDepthStencilStateWithDescriptor:](https://developer.apple.com/documentation/metal/mtldevice/1433412-makedepthstencilstate) method of `MTLDevice` with a depth/stencil state descriptor.
3. To set the depth/stencil state, call the [setDepthStencilState:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1516119-setdepthstencilstate) method of `MTLRenderCommandEncoder` with the [MTLDepthStencilState](https://developer.apple.com/documentation/metal/mtldepthstencilstate).
4. If the stencil test is in use, call [setStencilReferenceValue:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515697-setstencilreferencevalue) to specify the stencil reference value.

If the depth test is enabled, the render pipeline state must include a depth attachment to support writing the depth value. To perform the stencil test, the render pipeline state must include a stencil attachment. To configure attachments, see [Creating and Configuring a Render Pipeline Descriptor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltima).

If you will be changing the depth/stencil state regularly, then you may want to reuse the state descriptor object, modifying its property values as needed to create more state objects.

Use the properties of a [MTLDepthStencilDescriptor](https://developer.apple.com/documentation/metal/mtldepthstencildescriptor) object as follows to set the depth and stencil state:

- To enable writing the depth value to the depth attachment, set [depthWriteEnabled](https://developer.apple.com/documentation/metal/mtldepthstencildescriptor/1462501-isdepthwriteenabled) to `YES`.
- [depthCompareFunction](https://developer.apple.com/documentation/metal/mtldepthstencildescriptor/1462463-depthcomparefunction) specifies how the depth test is performed. If a fragment’s depth value fails the depth test, the fragment is discarded. For example, the commonly used `MTLCompareFunctionLess` function causes fragment values that are further away from the viewer than the (previously written) pixel depth value to fail the depth test; that is, the fragment is considered occluded by the earlier depth value.
- The [frontFaceStencil](https://developer.apple.com/documentation/metal/mtldepthstencildescriptor/1462476-frontfacestencil) and [backFaceStencil](https://developer.apple.com/documentation/metal/mtldepthstencildescriptor/1462507-backfacestencil) properties each specify a separate [MTLStencilDescriptor](https://developer.apple.com/documentation/metal/mtlstencildescriptor) object for front- and back-facing primitives. To use the same stencil state for both front- and back-facing primitives, you can assign the same [MTLStencilDescriptor](https://developer.apple.com/documentation/metal/mtlstencildescriptor) to both [frontFaceStencil](https://developer.apple.com/documentation/metal/mtldepthstencildescriptor/1462476-frontfacestencil) and [backFaceStencil](https://developer.apple.com/documentation/metal/mtldepthstencildescriptor/1462507-backfacestencil) properties. To explicitly disable the stencil test for one or both faces, set the corresponding property to `nil`, the default value.

Explicit disabling of a stencil state is not necessary. Metal determines whether to enable a stencil test based on whether the stencil descriptor is configured for a valid stencil operation.

[Listing 5-13](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltq) shows an example of creation and use of a [MTLDepthStencilDescriptor](https://developer.apple.com/documentation/metal/mtldepthstencildescriptor) object for the creation of a [MTLDepthStencilState](https://developer.apple.com/documentation/metal/mtldepthstencilstate) object, which is then used with a render command encoder. In this example, the stencil state for the front-facing primitives is accessed from the [frontFaceStencil](https://developer.apple.com/documentation/metal/mtldepthstencildescriptor/1462476-frontfacestencil) property of the depth/stencil state descriptor. The stencil test is explicitly disabled for the back-facing primitives.

__Listing 5-13__  Creating and Using a Depth/Stencil Descriptor

```
MTLDepthStencilDescriptor *dsDesc = [[MTLDepthStencilDescriptor alloc] init];
if (dsDesc == nil)
     exit(1);   //  if the descriptor could not be allocated
dsDesc.depthCompareFunction = MTLCompareFunctionLess;
dsDesc.depthWriteEnabled = YES;

dsDesc.frontFaceStencil.stencilCompareFunction = MTLCompareFunctionEqual;
dsDesc.frontFaceStencil.stencilFailureOperation = MTLStencilOperationKeep;
dsDesc.frontFaceStencil.depthFailureOperation = MTLStencilOperationIncrementClamp;
dsDesc.frontFaceStencil.depthStencilPassOperation =
                          MTLStencilOperationIncrementClamp;
dsDesc.frontFaceStencil.readMask = 0x1;
dsDesc.frontFaceStencil.writeMask = 0x1;
dsDesc.backFaceStencil = nil;
id <MTLDepthStencilState> dsState = [device
                          newDepthStencilStateWithDescriptor:dsDesc];

[renderEnc setDepthStencilState:dsState];
[renderEnc setStencilReferenceValue:0xFF];
```

The following properties define a stencil test in the [MTLStencilDescriptor](https://developer.apple.com/documentation/metal/mtlstencildescriptor):

- [readMask](https://developer.apple.com/documentation/metal/mtlstencildescriptor/1462465-readmask) is a bitmask; the GPU computes the bitwise AND of this mask with both the stencil reference value and the stored stencil value. The stencil test is a comparison between the resulting masked reference value and the masked stored value.
- [writeMask](https://developer.apple.com/documentation/metal/mtlstencildescriptor/1462496-writemask) is a bitmask that restricts which stencil values are written to the stencil attachment by the stencil operations.
- [stencilCompareFunction](https://developer.apple.com/documentation/metal/mtlstencildescriptor/1462455-stencilcomparefunction) specifies how the stencil test is performed for fragments. In Listing 5-13, the stencil comparison function is [MTLCompareFunctionEqual](https://developer.apple.com/documentation/metal/mtlcomparefunction/equal), so the stencil test passes if the masked reference value is equal to masked stencil value already stored at the location of a fragment.
- [stencilFailureOperation](https://developer.apple.com/documentation/metal/mtlstencildescriptor/1462471-stencilfailureoperation), [depthFailureOperation](https://developer.apple.com/documentation/metal/mtlstencildescriptor/1462500-depthfailureoperation), and [depthStencilPassOperation](https://developer.apple.com/documentation/metal/mtlstencildescriptor/1462486-depthstencilpassoperation) specify what to do to a stencil value stored in the stencil attachment for three different test outcomes: if the stencil test fails, if the stencil test passes and the depth test fails, or if both stencil and depth tests succeed, respectively. In the preceding example, the stencil value is unchanged ([MTLStencilOperationKeep](https://developer.apple.com/documentation/metal/mtlstenciloperation/keep)) if the stencil test fails, but it is incremented if the stencil test passes, unless the stencil value is already the maximum possible ([MTLStencilOperationIncrementClamp](https://developer.apple.com/documentation/metal/mtlstenciloperation/incrementclamp)).

After you have established the pipeline state and fixed-function state, you can call the following [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder) methods to draw the geometric primitives. These draw methods reference resources (such as buffers that contain vertex coordinates, texture coordinates, surface normals, and other data) to execute the pipeline with the shader functions and other state you have previously established with `MTLRenderCommandEncoder`.

- [drawPrimitives:vertexStart:vertexCount:instanceCount:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515327-drawprimitives) renders a number of instances (`instanceCount`) of primitives using vertex data in contiguous array elements, starting with the first vertex at the array element at the index `vertexStart` and ending at the array element at the index `vertexStart + vertexCount - 1`.
- [drawPrimitives:vertexStart:vertexCount:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1516326-drawprimitives) is the same as the previous method with an `instanceCount` of 1.
- [drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515699-drawindexedprimitives) renders a number of instances (`instanceCount`) of primitives using an index list specified in the `MTLBuffer` object `indexBuffer`. `indexCount` determines the number of indices. The index list starts at the index that is `indexBufferOffset` byte offset within the data in `indexBuffer`. `indexBufferOffset` must be a multiple of the size of an index, which is determined by `indexType`.
- [drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515542-drawindexedprimitives) is similar to the previous method with an `instanceCount` of 1.

For every primitive rendering method listed above, the first input value determines the primitive type with one of the `MTLPrimitiveType` values. The other input values determine which vertices are used to assemble the primitives. For all these methods, the `instanceStart` input value determines the first instance to draw, and `instanceCount` input value determines how many instances to draw.

As previously discussed, [setTriangleFillMode:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1516029-settrianglefillmode) determines whether the triangles are rendered as filled or wireframe, and the [setCullMode:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515975-setcullmode) and [setFrontFacingWinding:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515499-setfrontfacingwinding) settings determine whether the GPU culls triangles during rendering. For more information, see [Fixed-Function State Operations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltgoa)).

When rendering a point primitive, the shader language code for the vertex function must provide the `[[ point_size ]]` attribute, or the point size is undefined.

When rendering a triangle primitive with flat shading, the attributes of the first vertex (also known as the provoking vertex) are used for the whole triangle. The shader language code for the vertex function must provide the `[[ flat ]]` interpolation qualifier.

For details on all Metal shading language attributes and qualifiers, see _Metal Shading Language Guide_.

To terminate a rendering pass, call [endEncoding](https://developer.apple.com/documentation/metal/mtlcommandencoder/1458038-endencoding) on the render command encoder. After ending the previous command encoder, you can create a new command encoder of any type to encode additional commands into the command buffer.

The following steps, illustrated in [Listing 5-14](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltg), describe a basic procedure for rendering a triangle.

1. Create a [MTLCommandQueue](https://developer.apple.com/documentation/metal/mtlcommandqueue) and use it to create a [MTLCommandBuffer](https://developer.apple.com/documentation/metal/mtlcommandbuffer).
2. Create a [MTLRenderPassDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor) that specifies a collection of attachments that serve as the destination for encoded rendering commands in the command buffer.

   In this example, only the first color attachment is set up and used. (The variable `currentTexture` is assumed to contain a [MTLTexture](https://developer.apple.com/documentation/metal/mtltexture) that is used for a color attachment.) Then the [MTLRenderPassDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor) is used to create a new [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder).
3. Create two [MTLBuffer](https://developer.apple.com/documentation/metal/mtlbuffer) objects, `posBuf` and `colBuf`, and call [newBufferWithBytes:length:options:](https://developer.apple.com/documentation/metal/mtldevice/1433429-newbufferwithbytes) to copy vertex coordinate and vertex color data, `posData` and `colData`, respectively, into the buffer storage.
4. Call the [setVertexBuffer:offset:atIndex:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515829-setvertexbuffer) method of [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder) twice to specify the coordinates and colors.

   The `atIndex` input value of the [setVertexBuffer:offset:atIndex:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515829-setvertexbuffer) method corresponds to the attribute `buffer(atIndex)` in the source code of the vertex function.
5. Create a [MTLRenderPipelineDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor) and establish the vertex and fragment functions in the pipeline descriptor:

   - Create a [MTLLibrary](https://developer.apple.com/documentation/metal/mtllibrary) with source code from `progSrc`, which is assumed to be a string that contains Metal shader source code.
   - Then call the [newFunctionWithName:](https://developer.apple.com/documentation/metal/mtllibrary/1515524-newfunctionwithname) method of [MTLLibrary](https://developer.apple.com/documentation/metal/mtllibrary) to create the [MTLFunction](https://developer.apple.com/documentation/metal/mtlfunction) `vertFunc` that represents the function called `hello_vertex` and to create the [MTLFunction](https://developer.apple.com/documentation/metal/mtlfunction) `fragFunc` that represents the function called `hello_fragment`.
   - Finally, set the [vertexFunction](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1514679-vertexfunction) and [fragmentFunction](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1514600-fragmentfunction) properties of the [MTLRenderPipelineDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor) with these `MTLFunction` objects.
6. Create a [MTLRenderPipelineState](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate) from the [MTLRenderPipelineDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor) by calling [newRenderPipelineStateWithDescriptor:error:](https://developer.apple.com/documentation/metal/mtldevice/1433369-makerenderpipelinestate) or a similar method of [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice). Then the [setRenderPipelineState:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515811-setrenderpipelinestate) method of [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder) uses the created pipeline state for rendering.
7. Call the [drawPrimitives:vertexStart:vertexCount:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1516326-drawprimitives) method of [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder) to append commands to perform the rendering of a filled triangle (type [MTLPrimitiveTypeTriangle](https://developer.apple.com/documentation/metal/mtlprimitivetype/triangle)).
8. Call the [endEncoding](https://developer.apple.com/documentation/metal/mtlcommandencoder/1458038-endencoding) method to end encoding for this rendering pass. And call the [commit](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443003-commit) method of [MTLCommandBuffer](https://developer.apple.com/documentation/metal/mtlcommandbuffer) to execute the commands on the device.

__Listing 5-14__  Metal Code for Drawing a Triangle

```
id <MTLDevice> device = MTLCreateSystemDefaultDevice();

id <MTLCommandQueue> commandQueue = [device newCommandQueue];
id <MTLCommandBuffer> commandBuffer = [commandQueue commandBuffer];

MTLRenderPassDescriptor *renderPassDesc
                               = [MTLRenderPassDescriptor renderPassDescriptor];
renderPassDesc.colorAttachments[0].texture = currentTexture;
renderPassDesc.colorAttachments[0].loadAction = MTLLoadActionClear;
renderPassDesc.colorAttachments[0].clearColor = MTLClearColorMake(0.0,1.0,1.0,1.0);
id <MTLRenderCommandEncoder> renderEncoder =
           [commandBuffer renderCommandEncoderWithDescriptor:renderPassDesc];

static const float posData[] = {
        0.0f, 0.33f, 0.0f, 1.f,
        -0.33f, -0.33f, 0.0f, 1.f,
        0.33f, -0.33f, 0.0f, 1.f,
};
static const float colData[] = {
        1.f, 0.f, 0.f, 1.f,
        0.f, 1.f, 0.f, 1.f,
        0.f, 0.f, 1.f, 1.f,
};
id <MTLBuffer> posBuf = [device newBufferWithBytes:posData
        length:sizeof(posData) options:nil];
id <MTLBuffer> colBuf = [device newBufferWithBytes:colorData
        length:sizeof(colData) options:nil];
[renderEncoder setVertexBuffer:posBuf offset:0 atIndex:0];
[renderEncoder setVertexBuffer:colBuf offset:0 atIndex:1];

NSError *errors;
id <MTLLibrary> library = [device newLibraryWithSource:progSrc options:nil
                           error:&errors];
id <MTLFunction> vertFunc = [library newFunctionWithName:@"hello_vertex"];
id <MTLFunction> fragFunc = [library newFunctionWithName:@"hello_fragment"];
MTLRenderPipelineDescriptor *renderPipelineDesc
                                   = [[MTLRenderPipelineDescriptor alloc] init];
renderPipelineDesc.vertexFunction = vertFunc;
renderPipelineDesc.fragmentFunction = fragFunc;
renderPipelineDesc.colorAttachments[0].pixelFormat = currentTexture.pixelFormat;
id <MTLRenderPipelineState> pipeline = [device
             newRenderPipelineStateWithDescriptor:renderPipelineDesc error:&errors];
[renderEncoder setRenderPipelineState:pipeline];
[renderEncoder drawPrimitives:MTLPrimitiveTypeTriangle
               vertexStart:0 vertexCount:3];
[renderEncoder endEncoding];
[commandBuffer commit];
```

In Listing 5-14, a [MTLFunction](https://developer.apple.com/documentation/metal/mtlfunction) object represents the shader function called `hello_vertex`. The [setVertexBuffer:offset:atIndex:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515829-setvertexbuffer) method of [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder) is used to specify the vertex resources (in this case, two buffer objects) that are passed as arguments into `hello_vertex`. The `atIndex` input value of the [setVertexBuffer:offset:atIndex:](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515829-setvertexbuffer) method corresponds to the attribute `buffer(atIndex)` in the source code of the vertex function, as shown in Listing 5-15.

__Listing 5-15__  Corresponding Shader Function Declaration

```
vertex VertexOutput hello_vertex(
                    const global float4 *pos_data [[ buffer(0) ]],
                    const global float4 *color_data [[ buffer(1) ]])
{
    ...
}
```


In some cases, your app’s performance can be limited by the single-CPU workload of encoding commands for a single rendering pass. However, attempting to circumvent this bottleneck by separating the workload into multiple rendering passes encoded on multiple CPU threads can also adversely impact performance, because each rendering pass requires its own intermediate attachment store and load actions to preserve the render target contents.

Instead, use a [MTLParallelRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder) object, which manages multiple subordinate `MTLRenderCommandEncoder` objects that share the same command buffer and render pass descriptor. The parallel render command encoder ensures that the attachment load and store actions occur only at the start and end of the entire rendering pass, not at the start and end of each subordinate render command encoder’s set of commands. With this architecture, you can assign each `MTLRenderCommandEncoder` object to its own thread in parallel in a safe and highly performant manner.

To create a parallel render command encoder, use the [parallelRenderCommandEncoderWithDescriptor:](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443009-parallelrendercommandencoderwith) method of a `MTLCommandBuffer` object. To create subordinate render command encoders, call the `renderCommandEncoder` method of the `MTLParallelRenderCommandEncoder` object once for each CPU thread from which you want to perform command encoding. All subordinate command encoders created from the same parallel render command encoder encode commands to the same command buffer. Commands are encoded to a command buffer in the order in which the render command encoders are created. To end encoding for a specific render command encoder, call the [endEncoding](https://developer.apple.com/documentation/metal/mtlcommandencoder/1458038-endencoding) method of `MTLRenderCommandEncoder`. After you have ended encoding on all render command encoders created by the parallel render command encoder, call the [endEncoding](https://developer.apple.com/documentation/metal/mtlcommandencoder/1458038-endencoding) method of `MTLParallelRenderCommandEncoder` to end the rendering pass.

Listing 5-16 shows the `MTLParallelRenderCommandEncoder` creating three `MTLRenderCommandEncoder` objects: `rCE1`, `rCE2`, and `rCE3`.

__Listing 5-16__  A Parallel Rendering Encoder with Three Render Command Encoders

```
MTLRenderPassDescriptor *renderPassDesc                       = [MTLRenderPassDescriptor renderPassDescriptor]; renderPassDesc.colorAttachments[0].texture = currentTexture; renderPassDesc.colorAttachments[0].loadAction = MTLLoadActionClear; renderPassDesc.colorAttachments[0].clearColor = MTLClearColorMake(0.0,0.0,0.0,1.0);  id <MTLParallelRenderCommandEncoder> parallelRCE = [commandBuffer                       parallelRenderCommandEncoderWithDescriptor:renderPassDesc]; id <MTLRenderCommandEncoder> rCE1 = [parallelRCE renderCommandEncoder]; id <MTLRenderCommandEncoder> rCE2 = [parallelRCE renderCommandEncoder]; id <MTLRenderCommandEncoder> rCE3 = [parallelRCE renderCommandEncoder];  //  not shown: rCE1, rCE2, and rCE3 call methods to encode graphics commands // //  rCE1 commands are processed first, because it was created first //  even though rCE2 and rCE3 end earlier than rCE1 [rCE2 endEncoding]; [rCE3 endEncoding]; [rCE1 endEncoding];  //  all MTLRenderCommandEncoders must end before MTLParallelRenderCommandEncoder [parallelRCE endEncoding];
```

The order in which the command encoders call [endEncoding](https://developer.apple.com/documentation/metal/mtlcommandencoder/1458038-endencoding) is not relevant to the order in which commands are encoded and appended to the [MTLCommandBuffer](https://developer.apple.com/documentation/metal/mtlcommandbuffer). For [MTLParallelRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder), the [MTLCommandBuffer](https://developer.apple.com/documentation/metal/mtlcommandbuffer) always contains commands in the order that the subordinate render command encoders were created, as seen in Figure 5-6.

__Figure 5-6__  Ordering of Render Command Encoders in a Parallel Rendering Pass

!

[Next](Data-Parallel%20Compute%20Processing-%20Compute%20Command%20Encoder.md)[Previous](Functions%20and%20Libraries.md)

