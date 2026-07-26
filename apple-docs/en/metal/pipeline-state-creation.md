---
title: Pipeline state creation
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/pipeline-state-creation
source_url: 'https://developer.apple.com/documentation/metal/pipeline-state-creation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/pipeline-state-creation.json'
content_hash: 'sha256:54606c64b031e693'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [GPU devices and work submission](gpu-devices-and-work-submission.md) · [MTLDevice](mtldevice.md)

# Pipeline state creation

<sub>API Collection</sub>

Create pipeline states for render and compute passes, samplers, depth and stencil states, and indirect command buffers.

## Overview

Use these methods to create instances of various state types for a render or compute pass (see [Render passes](render-passes.md) and [Compute passes](compute-passes.md), respectively).

You can create multiple [MTLRenderPipelineState](mtlrenderpipelinestate.md) instances for a single render pass encoder ([MTLRenderCommandEncoder](mtlrendercommandencoder.md)) that each apply to different types of render commands. For example, a single render pass can render primitives with vertices, then meshes, and finish with a tile shader command, each with a different pipeline. To create these pipelines, configure instances of [MTLRenderPipelineDescriptor](mtlrenderpipelinedescriptor.md), [MTLMeshRenderPipelineDescriptor](mtlmeshrenderpipelinedescriptor.md), and [MTLTileRenderPipelineDescriptor](mtltilerenderpipelinedescriptor.md). Then pass those descriptors to the [- newRenderPipelineStateWithDescriptor:completionHandler:](<mtldevice/makerenderpipelinestate(descriptor_completionhandler_).md>), [- newRenderPipelineStateWithMeshDescriptor:options:completionHandler:](<mtldevice/makerenderpipelinestate(descriptor_options_completionhandler_)-1wvya.md>) and [- newRenderPipelineStateWithTileDescriptor:options:completionHandler:](<mtldevice/makerenderpipelinestate(tiledescriptor_options_completionhandler_).md>) methods (or a counterpart method), respectively.

> [!important] Important
> Only create reflection (see [MTLRenderPipelineReflection](mtlrenderpipelinereflection.md)) instances if you need them, because each one can require a significant amount of memory.

## Topics

### Creating render pipeline states with vertex shaders

- [- newRenderPipelineStateWithDescriptor:error:](<mtldevice/makerenderpipelinestate(descriptor_).md>) — Synchronously creates a render pipeline state.
- [- newRenderPipelineStateWithDescriptor:completionHandler:](<mtldevice/makerenderpipelinestate(descriptor_completionhandler_).md>) — Asynchronously creates a render pipeline state.
- [makeRenderPipelineState(descriptor:options:)](<mtldevice/makerenderpipelinestate(descriptor_options_)-89vxc.md>) — Synchronously creates a render pipeline state and reflection information in a tuple.
- [- newRenderPipelineStateWithDescriptor:options:reflection:error:](<mtldevice/makerenderpipelinestate(descriptor_options_reflection_).md>) — Synchronously creates a render pipeline state and reflection information.
- [- newRenderPipelineStateWithDescriptor:options:completionHandler:](<mtldevice/makerenderpipelinestate(descriptor_options_completionhandler_)-5gdww.md>) — Asynchronously creates a render pipeline state and reflection information.

### Creating render pipeline states with mesh shaders

- [makeRenderPipelineState(descriptor:options:)](<mtldevice/makerenderpipelinestate(descriptor_options_)-yrak.md>) — Synchronously creates a mesh render pipeline state and reflection information in a tuple.
- [- newRenderPipelineStateWithMeshDescriptor:options:completionHandler:](<mtldevice/makerenderpipelinestate(descriptor_options_completionhandler_)-1wvya.md>) — Asynchronously creates a mesh render pipeline state and reflection information.

### Creating tile render pipeline states

- [makeRenderPipelineState(tileDescriptor:options:)](<mtldevice/makerenderpipelinestate(tiledescriptor_options_).md>) — Synchronously creates a tile shader’s render pipeline state and reflection information in a tuple.
- [- newRenderPipelineStateWithTileDescriptor:options:reflection:error:](<mtldevice/makerenderpipelinestate(tiledescriptor_options_reflection_).md>) — Synchronously creates a tile shader’s render pipeline state and reflection information.
- [- newRenderPipelineStateWithTileDescriptor:options:completionHandler:](<mtldevice/makerenderpipelinestate(tiledescriptor_options_completionhandler_).md>) — Asynchronously creates a tile shader’s render pipeline state and reflection information.

### Creating compute pipeline states

- [- newComputePipelineStateWithDescriptor:options:reflection:error:](<mtldevice/makecomputepipelinestate(descriptor_options_reflection_).md>) — Synchronously creates a compute pipeline state and reflection information.
- [- newComputePipelineStateWithDescriptor:options:completionHandler:](<mtldevice/makecomputepipelinestate(descriptor_options_completionhandler_).md>) — Asynchronously creates a compute pipeline state and reflection information.
- [- newComputePipelineStateWithFunction:error:](<mtldevice/makecomputepipelinestate(function_).md>) — Synchronously creates a compute pipeline state with a function instance.
- [- newComputePipelineStateWithFunction:completionHandler:](<mtldevice/makecomputepipelinestate(function_completionhandler_).md>) — Asynchronously creates a compute pipeline state with a function instance.
- [- newComputePipelineStateWithFunction:options:reflection:error:](<mtldevice/makecomputepipelinestate(function_options_reflection_).md>) — Synchronously creates a compute pipeline state and reflection with a function instance.
- [- newComputePipelineStateWithFunction:options:completionHandler:](<mtldevice/makecomputepipelinestate(function_options_completionhandler_).md>) — Asynchronously creates a compute pipeline state and reflection with a function instance.

### Creating depth and stencil states

- [- newDepthStencilStateWithDescriptor:](<mtldevice/makedepthstencilstate(descriptor_).md>) — Creates a depth-stencil state instance.

### Supporting types

- [MTLNewRenderPipelineStateCompletionHandler](mtlnewrenderpipelinestatecompletionhandler.md) — A completion handler signature a method calls when it finishes creating a render pipeline.
- [MTLNewRenderPipelineStateWithReflectionCompletionHandler](mtlnewrenderpipelinestatewithreflectioncompletionhandler.md) — A completion handler signature a method calls when it finishes creating a render pipeline and reflection information.
- [MTLNewComputePipelineStateCompletionHandler](mtlnewcomputepipelinestatecompletionhandler.md) — A completion handler signature a method calls when it finishes creating a compute pipeline.
- [MTLNewComputePipelineStateWithReflectionCompletionHandler](mtlnewcomputepipelinestatewithreflectioncompletionhandler.md) — A completion handler signature a method calls when it finishes creating a compute pipeline and reflection information.

## See Also

### Working with GPU devices

- [Device inspection](device-inspection.md) — Locate and identify a GPU and the features it supports, and sample its counters.
- [Work submission](work-submission.md) — Create queues that submit work to the GPU or load assets into GPU resources, and indirect command buffers that group your frequent commands together.
- [Resource creation](resource-creation.md) — Load assets with input/output queues and make various resource instances, such as buffers, textures, acceleration structures, and memory heaps.
- [Shader library and archive creation](shader-library-and-archive-creation.md) — Create static and dynamic shader libraries, and binary shader archives.
