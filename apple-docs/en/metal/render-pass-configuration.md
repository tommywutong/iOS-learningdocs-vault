---
title: Render pass configuration
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/render-pass-configuration
source_url: 'https://developer.apple.com/documentation/metal/render-pass-configuration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/render-pass-configuration.json'
content_hash: 'sha256:4b3f0d8b81222c19'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [Render passes](render-passes.md) · [MTLRenderCommandEncoder](mtlrendercommandencoder.md)

# Render pass configuration

<sub>API Collection</sub>

Set a render pass’s pipeline state, attachment actions, viewports, and so on, that affect subsequent drawing commands.

## Overview

These methods encode commands that configure the render pass for all subsequent drawing commands. The most important configuration is the pipeline state (see [MTLRenderPipelineState](mtlrenderpipelinestate.md)), which you configure by calling the [- setRenderPipelineState:](<mtlrendercommandencoder/setrenderpipelinestate(__).md>) method.

## Topics

### Configuring pipeline state

- [- setRenderPipelineState:](<mtlrendercommandencoder/setrenderpipelinestate(__).md>) — Configures the encoder with a render or tile pipeline state that applies to your subsequent draw commands.

### Configuring the actions for attachments

- [- setColorStoreAction:atIndex:](<mtlrendercommandencoder/setcolorstoreaction(__index_).md>) — Configures the store action for a color attachment.
- [- setColorStoreActionOptions:atIndex:](<mtlrendercommandencoder/setcolorstoreactionoptions(__index_).md>) — Configures the store action options for a color attachment. _(deprecated)_
- [- setDepthStoreAction:](<mtlrendercommandencoder/setdepthstoreaction(__).md>) — Configures the store action for the depth attachment.
- [- setDepthStoreActionOptions:](<mtlrendercommandencoder/setdepthstoreactionoptions(__).md>) — Configures the store action options for the depth attachment. _(deprecated)_
- [- setStencilStoreAction:](<mtlrendercommandencoder/setstencilstoreaction(__).md>) — Configures the store action for the stencil attachment.
- [- setStencilStoreActionOptions:](<mtlrendercommandencoder/setstencilstoreactionoptions(__).md>) — Configures the store action options for the stencil attachment. _(deprecated)_

### Configuring blend behavior

- [- setBlendColorRed:green:blue:alpha:](<mtlrendercommandencoder/setblendcolor(red_green_blue_alpha_).md>) — Configures each pixel component value, including alpha, for the render pipeline’s constant blend color.
- [- setColorAttachmentMap:](<mtlrendercommandencoder/setcolorattachmentmap(__).md>) — Sets the mapping from logical shader color output to physical render pass color attachments.

### Configuring rendering behavior

- [- setTriangleFillMode:](<mtlrendercommandencoder/settrianglefillmode(__).md>) — Configures how subsequent draw commands rasterize triangle and triangle strip primitives.
- [- setFrontFacingWinding:](<mtlrendercommandencoder/setfrontfacing(__).md>) — Configures which face of a primitive, such as a triangle, is the front.
- [- setCullMode:](<mtlrendercommandencoder/setcullmode(__).md>) — Configures how the render pipeline determines which primitives to remove.

### Configuring depth and stencil behavior

- [- setDepthStencilState:](<mtlrendercommandencoder/setdepthstencilstate(__).md>) — Configures the combined depth and stencil state.
- [- setDepthBias:slopeScale:clamp:](<mtlrendercommandencoder/setdepthbias(__slopescale_clamp_).md>) — Configures the adjustments a render pass applies to depth values from fragment functions by a scaling factor and bias.
- [- setDepthClipMode:](<mtlrendercommandencoder/setdepthclipmode(__).md>) — Configures how the render pipeline handles fragments outside the near and far planes of the view frustum.
- [setDepthTestBounds(_:)](<mtlrendercommandencoder/setdepthtestbounds(__).md>) — Configures the range for depth bounds testing.
- [- setStencilReferenceValue:](<mtlrendercommandencoder/setstencilreferencevalue(__).md>) — Configures the same comparison value for front- and back-facing primitives.
- [- setStencilFrontReferenceValue:backReferenceValue:](<mtlrendercommandencoder/setstencilreferencevalues(front_back_).md>) — Configures different comparison values for front- and back-facing primitives.

### Configuring viewport and scissor behavior

- [- setViewport:](<mtlrendercommandencoder/setviewport(__).md>) — Configures the render pipeline with a viewport that applies a transformation and a clipping rectangle.
- [setViewports(_:)](<mtlrendercommandencoder/setviewports(__).md>) — Configures the render pipeline with multiple viewports that apply transformations and clipping rectangles.
- [- setScissorRect:](<mtlrendercommandencoder/setscissorrect(__).md>) — Configures a rectangle for the fragment scissor test.
- [setScissorRects(_:)](<mtlrendercommandencoder/setscissorrects(__).md>) — Configures multiple rectangles for the fragment scissor test.

### Configuring visibility testing

- [- setVisibilityResultMode:offset:](<mtlrendercommandencoder/setvisibilityresultmode(__offset_).md>) — Configures which visibility test the GPU runs and the destination for any results it generates.

### Configuring vertex amplification

- [- setVertexAmplificationCount:viewMappings:](<mtlrendercommandencoder/setvertexamplificationcount(__viewmappings_).md>) — Configures the number of output vertices the render pipeline produces for each input vertex, optionally with render target and viewport offsets.

### Configuring tessellation factors

- [- setTessellationFactorScale:](<mtlrendercommandencoder/settessellationfactorscale(__).md>) — Configures the scale factor for per-patch tessellation factors.
- [- setTessellationFactorBuffer:offset:instanceStride:](<mtlrendercommandencoder/settessellationfactorbuffer(__offset_instancestride_).md>) — Configures the per-patch tessellation factors for any subsequent patch-drawing commands.

### Configuring persistent threadgroup memory

- [- setObjectThreadgroupMemoryLength:atIndex:](<mtlrendercommandencoder/setobjectthreadgroupmemorylength(__index_).md>) — Configures the size of a threadgroup memory buffer for an entry in the object argument table.
- [- setThreadgroupMemoryLength:offset:atIndex:](<mtlrendercommandencoder/setthreadgroupmemorylength(__offset_index_).md>) — Configures the size of a threadgroup memory buffer for an entry in the fragment or tile shader argument table.
