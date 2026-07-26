---
title: MTLRenderPipelineDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinedescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinedescriptor.json'
content_hash: 'sha256:9609def971562dfb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLRenderPipelineDescriptor

<sub>Class</sub>

An argument of options you pass to a GPU device to get a render pipeline state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLRenderPipelineDescriptor
```

## Overview

An [MTLRenderPipelineDescriptor](mtlrenderpipelinedescriptor.md) instance configures the state of the pipeline to use during a rendering pass, including rasterization (such as multisampling), visibility, blending, tessellation, and graphics function state. Use standard allocation and initialization techniques to create an [MTLRenderPipelineDescriptor](mtlrenderpipelinedescriptor.md) object. Then configure and use the descriptor to create an [MTLRenderPipelineState](mtlrenderpipelinestate.md) object.

To specify the vertex or fragment function in the rendering pipeline descriptor, set the [vertexFunction](mtlrenderpipelinedescriptor/vertexfunction.md) or [fragmentFunction](mtlrenderpipelinedescriptor/fragmentfunction.md) property, respectively, to the desired [MTLFunction](mtlfunction.md) object. The system ignores the tessellation stage properties if you don’t set the [vertexFunction](mtlrenderpipelinedescriptor/vertexfunction.md) property to a post-tessellation vertex function. A vertex function is a post-tessellation vertex function if the `[[ patch(patch-type, N) ]]` attribute precedes the function’s signature in your Metal Shading Language source. See the “Post-Tessellation Vertex Functions” section of [Metal Shading Language Specification](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf) for more information.

Setting the [fragmentFunction](mtlrenderpipelinedescriptor/fragmentfunction.md) property to `nil` disables the rasterization of pixels into the color attachment. This action is typically for outputting vertex function data into a buffer object, or for depth-only rendering.

If the vertex shader has an argument with per-vertex input attributes, set the [vertexDescriptor](mtlrenderpipelinedescriptor/vertexdescriptor.md) property to an [MTLVertexDescriptor](mtlvertexdescriptor.md) object that describes the organization of that vertex data.

### Multisampling and the render pipeline

If a color attachment supports multisampling (essentially, the attachment is an [MTLTextureType2DMultisample](mtltexturetype/type2dmultisample.md) type color texture), you can create multiple samples per fragment, and the following rendering pipeline descriptor properties determine coverage:

- [rasterSampleCount](mtlrenderpipelinedescriptor/rastersamplecount.md) is the number of samples for each pixel.
- If [alphaToCoverageEnabled](mtlrenderpipelinedescriptor/isalphatocoverageenabled.md) is [true](../swift/true.md), the GPU uses the alpha channel fragment output for [colorAttachments](mtlrenderpipelinedescriptor/colorattachments.md) to compute a coverage mask that affects the values the GPU writes to all attachments (color, depth, and stencil).
- If [alphaToOneEnabled](mtlrenderpipelinedescriptor/isalphatooneenabled.md) is [true](../swift/true.md), the GPU changes alpha channel fragment values for [colorAttachments](mtlrenderpipelinedescriptor/colorattachments.md) to `1.0`, which is the largest representable value.

If [alphaToCoverageEnabled](mtlrenderpipelinedescriptor/isalphatocoverageenabled.md) is [true](../swift/true.md), an implementation-defined `coverageToMask` function uses the alpha channel fragment output from [colorAttachments](mtlrenderpipelinedescriptor/colorattachments.md) to create an intermediate coverage mask, which sets a number of bits in its output proportionally to the value of the floating-point input. For example, if the input is `0.0f`, the function sets the output to `0x0`. If the input is `1.0f`, the function sets all output bits (in effect, `~0x0`). If the input is `0.5f`, the function sets half of the bits, according to the implementation, which often uses dither patterns.

To determine a final coverage mask, the function performs a logical `AND` on the resulting coverage mask `alphaCoverageMask` with the masks from the rasterizer and fragment shader, as the following code shows:

```objective-c
if (alphaToCoverageEnabled) then
    alphaCoverageMask = coverageToMask(colorAttachment0.alpha);

finalCoverageMask = originalRasterizerCoverageMask
                    & alphaCoverageMask
                    & fragShaderSampleMaskOutput;
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Identifying the render pipeline state object

- [label](mtlrenderpipelinedescriptor/label.md) — A string that identifies the render pipeline descriptor.

### Specifying graphics functions and associated data

- [vertexFunction](mtlrenderpipelinedescriptor/vertexfunction.md) — The vertex function the pipeline calls to process vertices.
- [fragmentFunction](mtlrenderpipelinedescriptor/fragmentfunction.md) — The fragment function the pipeline calls to process fragments.
- [maxVertexCallStackDepth](mtlrenderpipelinedescriptor/maxvertexcallstackdepth.md) — The maximum function call depth from the top-most vertex shader function.
- [maxFragmentCallStackDepth](mtlrenderpipelinedescriptor/maxfragmentcallstackdepth.md) — The maximum function call depth from the top-most fragment shader function.

### Specifying buffer layouts and fetch behavior

- [vertexDescriptor](mtlrenderpipelinedescriptor/vertexdescriptor.md) — The organization of vertex data in an attribute’s argument table.

### Specifying buffer mutability

- [vertexBuffers](mtlrenderpipelinedescriptor/vertexbuffers.md) — An array that contains the buffer mutability options for a render pipeline’s vertex function.
- [fragmentBuffers](mtlrenderpipelinedescriptor/fragmentbuffers.md) — An array that contains the buffer mutability options for a render pipeline’s fragment function.

### Specifying rendering pipeline state

- [- reset](<mtlrenderpipelinedescriptor/reset().md>) — Specifies the default rendering pipeline state values for the descriptor.
- [colorAttachments](mtlrenderpipelinedescriptor/colorattachments.md) — An array of attachments that store color data.
- [depthAttachmentPixelFormat](mtlrenderpipelinedescriptor/depthattachmentpixelformat.md) — The pixel format of the attachment that stores depth data.
- [stencilAttachmentPixelFormat](mtlrenderpipelinedescriptor/stencilattachmentpixelformat.md) — The pixel format of the attachment that stores stencil data.

### Specifying rasterization and visibility state

- [alphaToCoverageEnabled](mtlrenderpipelinedescriptor/isalphatocoverageenabled.md) — A Boolean value that indicates whether to read and use the alpha channel fragment output for color attachments to compute a sample coverage mask.
- [alphaToOneEnabled](mtlrenderpipelinedescriptor/isalphatooneenabled.md) — A Boolean value that indicates whether to force alpha channel values for color attachments to the largest representable value.
- [rasterizationEnabled](mtlrenderpipelinedescriptor/israsterizationenabled.md) — A Boolean value that determines whether the pipeline rasterizes primitives.
- [inputPrimitiveTopology](mtlrenderpipelinedescriptor/inputprimitivetopology.md) — The type of primitive topology the pipeline renders.
- [rasterSampleCount](mtlrenderpipelinedescriptor/rastersamplecount.md) — The number of samples the pipeline applies for each fragment.
- [MTLPrimitiveTopologyClass](mtlprimitivetopologyclass.md) — The primitive topologies available for rendering.
- [sampleCount](mtlrenderpipelinedescriptor/samplecount.md) — The number of samples the pipeline applies for each fragment. _(deprecated)_

### Specifying tessellation state

- [maxTessellationFactor](mtlrenderpipelinedescriptor/maxtessellationfactor.md) — The maximum tessellation factor that the tessellator uses when tessellating patches.
- [tessellationFactorScaleEnabled](mtlrenderpipelinedescriptor/istessellationfactorscaleenabled.md) — A Boolean value that determines whether the pipeline scales the tessellation factor.
- [tessellationFactorFormat](mtlrenderpipelinedescriptor/tessellationfactorformat.md) — The format of the tessellation factors in the tessellation factor buffer.
- [tessellationControlPointIndexType](mtlrenderpipelinedescriptor/tessellationcontrolpointindextype.md) — The size of the control point indices in a control point index buffer.
- [tessellationFactorStepFunction](mtlrenderpipelinedescriptor/tessellationfactorstepfunction.md) — The step function for determining the tessellation factors for a patch from the tessellation factor buffer.
- [tessellationOutputWindingOrder](mtlrenderpipelinedescriptor/tessellationoutputwindingorder.md) — The winding order of triangles from the tessellator.
- [tessellationPartitionMode](mtlrenderpipelinedescriptor/tessellationpartitionmode.md) — The partitioning mode that the tessellator uses to derive the number and spacing of segments for subdividing a corresponding edge.
- [MTLTessellationFactorFormat](mtltessellationfactorformat.md) — Options for specifying the format of the tessellation factors in a tessellation factor buffer.
- [MTLTessellationControlPointIndexType](mtltessellationcontrolpointindextype.md) — Options for specifying the size of the control point indices in a control point index buffer.
- [MTLTessellationFactorStepFunction](mtltessellationfactorstepfunction.md) — Options for specifying the step function that determines the tessellation factors for a patch from the tessellation factor buffer.
- [MTLTessellationPartitionMode](mtltessellationpartitionmode.md) — Options for choosing the partition mode that the tessellator applies when deriving the number and spacing of segments for subdividing a corresponding edge.

### Specifying indirect command buffers usage

- [supportIndirectCommandBuffers](mtlrenderpipelinedescriptor/supportindirectcommandbuffers.md) — A Boolean value that determines whether you can encode commands into an indirect command buffer using the render pipeline.

### Specifying the maximum vertex amplification count

- [maxVertexAmplificationCount](mtlrenderpipelinedescriptor/maxvertexamplificationcount.md) — The maximum vertex amplification count you can set when encoding render commands.

### Specifying precompiled shader binaries

- [supportAddingVertexBinaryFunctions](mtlrenderpipelinedescriptor/supportaddingvertexbinaryfunctions.md) — A Boolean value that indicates whether you can use the pipeline to create new pipelines by adding binary functions to the vertex shader’s callable functions list.
- [supportAddingFragmentBinaryFunctions](mtlrenderpipelinedescriptor/supportaddingfragmentbinaryfunctions.md) — A Boolean value that indicates whether you can use the pipeline to create new pipelines by adding binary functions to the fragment shader’s callable functions list.
- [binaryArchives](mtlrenderpipelinedescriptor/binaryarchives.md) — An array of binary archives to search for precompiled versions of the shader.

### Specifying callable functions for the pipeline

- [vertexLinkedFunctions](mtlrenderpipelinedescriptor/vertexlinkedfunctions.md) — Functions that you can specify as function arguments for the vertex shader when encoding commands that use the pipeline.
- [fragmentLinkedFunctions](mtlrenderpipelinedescriptor/fragmentlinkedfunctions.md) — Functions that you can specify as function arguments for the fragment shader when encoding commands that use the pipeline.

### Specifying shader validation

- [shaderValidation](mtlrenderpipelinedescriptor/shadervalidation.md) — A value that enables or disables shader validation for the pipeline.

### Instance Properties

- [fragmentPreloadedLibraries](mtlrenderpipelinedescriptor/fragmentpreloadedlibraries.md)
- [vertexPreloadedLibraries](mtlrenderpipelinedescriptor/vertexpreloadedlibraries.md)

## See Also

### Render pipeline states

- [MTLRenderPipelineState](mtlrenderpipelinestate.md) — An interface that represents a graphics pipeline configuration for a render pass, which the pass applies to the draw commands you encode.
- [MTL4RenderPipelineDescriptor](mtl4renderpipelinedescriptor.md) — Groups together properties to create a render pipeline state object.
- [MTLRenderPipelineFunctionsDescriptor](mtlrenderpipelinefunctionsdescriptor.md) — A collection of functions for updating a render pipeline.
- [MTL4MeshRenderPipelineDescriptor](mtl4meshrenderpipelinedescriptor.md) — Groups together properties you use to create a mesh render pipeline state object.
- [MTLMeshRenderPipelineDescriptor](mtlmeshrenderpipelinedescriptor.md) — An object that configures new render pipeline state objects for mesh shading.
- [MTLPipelineBufferDescriptor](mtlpipelinebufferdescriptor.md) — The mutability options for a buffer that a render or compute pipeline uses.
- [MTLPipelineBufferDescriptorArray](mtlpipelinebufferdescriptorarray.md) — An array of pipeline buffer descriptors.
- [MTL4RenderPipelineColorAttachmentDescriptor](mtl4renderpipelinecolorattachmentdescriptor.md)
- [MTLRenderPipelineColorAttachmentDescriptor](mtlrenderpipelinecolorattachmentdescriptor.md) — A color render target that specifies the color configuration and color operations for a render pipeline.
- [MTLRenderPipelineColorAttachmentDescriptorArray](mtlrenderpipelinecolorattachmentdescriptorarray.md) — An array of render pipeline color attachment descriptor objects.
- [MTL4TileRenderPipelineDescriptor](mtl4tilerenderpipelinedescriptor.md) — Groups together properties you use to create a tile render pipeline state object.
- [MTLTileRenderPipelineDescriptor](mtltilerenderpipelinedescriptor.md) — An object that configures new render pipeline state objects for tile shading.
- [MTLTileRenderPipelineColorAttachmentDescriptor](mtltilerenderpipelinecolorattachmentdescriptor.md) — A description of a tile-shading render pipeline’s color render target.
- [MTLPipelineOption](mtlpipelineoption.md) — Options that determine how Metal prepares the pipeline.
- [MTL4RenderPipelineBinaryFunctionsDescriptor](mtl4renderpipelinebinaryfunctionsdescriptor.md) — Allows you to specify additional binary functions to link to each stage of a render pipeline.
