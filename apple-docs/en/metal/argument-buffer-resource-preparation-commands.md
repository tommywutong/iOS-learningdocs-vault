---
title: Argument buffer resource preparation commands
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/argument-buffer-resource-preparation-commands
source_url: 'https://developer.apple.com/documentation/metal/argument-buffer-resource-preparation-commands'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/argument-buffer-resource-preparation-commands.json'
content_hash: 'sha256:a8c3dbee440b41e9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [Render passes](render-passes.md) · [MTLRenderCommandEncoder](mtlrendercommandencoder.md)

# Argument buffer resource preparation commands

<sub>API Collection</sub>

Load individual resources and multiple resources within a heap into GPU memory so that they’re available to shaders through argument buffers.

## Overview

These methods encode commands that load resources into GPU memory, making them accessible to your shaders through argument buffers. To load an individual resource, call the [- useResource:usage:stages:](<mtlrendercommandencoder/useresource(__usage_stages_).md>) method, or another resource-based method. Alternatively, you can load all the resources within a heap by calling the [- useHeap:stages:](<mtlrendercommandencoder/useheap(__stages_).md>) method or another heap-based method.

> [!important] Important
> The heap-based methods don’t provide a `usage` parameter (see [MTLResourceUsage](mtlresourceusage.md)) and set the usage for the resources within each heap to [MTLResourceUsageRead](mtlresourceusage/read.md).

To give shaders write or read/write access to specific resources within a heap, call a resource-based method after the heap-based method. Metal combines usage modes you set for a resource through both heap and resource methods.

For more information, see [Improving CPU performance by using argument buffers](improving-cpu-performance-by-using-argument-buffers.md).

## Topics

### Loading individual resources for argument buffers

- [- useResource:usage:stages:](<mtlrendercommandencoder/useresource(__usage_stages_).md>) — Ensures the shaders in the render pass’s subsequent draw commands have access to a resource.
- [useResources(_:usage:stages:)](<mtlrendercommandencoder/useresources(__usage_stages_).md>) — Ensures the shaders in the render pass’s subsequent draw commands have access to multiple resources.

### Loading heaps and the resources they contain for argument buffers

- [- useHeap:stages:](<mtlrendercommandencoder/useheap(__stages_).md>) — Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from a heap.
- [useHeaps(_:stages:)](<mtlrendercommandencoder/useheaps(__stages_).md>) — Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from multiple heaps.

## See Also

### Resource preparation commands

- [Mesh and object shader resource preparation commands](mesh-and-object-shader-resource-preparation-commands.md) — Assign resources to mesh and object shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Vertex shader resource preparation commands](vertex-shader-resource-preparation-commands.md) — Assign resources to vertex shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Fragment shader resource preparation commands](fragment-shader-resource-preparation-commands.md) — Assign resources to fragment shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Tile shaders resource preparation commands](tile-shaders-resource-preparation-commands.md) — Assign resources to tile shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
