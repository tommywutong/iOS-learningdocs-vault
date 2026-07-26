---
title: Tracking the resource residency of argument buffers
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/tracking-the-resource-residency-of-argument-buffers
source_url: 'https://developer.apple.com/documentation/metal/tracking-the-resource-residency-of-argument-buffers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/tracking-the-resource-residency-of-argument-buffers.json'
content_hash: 'sha256:8f2a0efd7e2eacb2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [Buffers](buffers.md)

# Tracking the resource residency of argument buffers

<sub>Article</sub>

Optimize resource performance within an argument buffer.

## Overview

The Metal driver can’t automatically track the residency of argument buffer resources, but you can track it manually.

### Track argument buffer resource residency manually

Call an [MTLRenderCommandEncoder](mtlrendercommandencoder.md) or [MTLComputeCommandEncoder](mtlcomputecommandencoder.md) method:

- For individual resources, call [- useResource:usage:stages:](<mtlrendercommandencoder/useresource(__usage_stages_).md>) or [- useResource:usage:](<mtlcomputecommandencoder/useresource(__usage_).md>).
- For all resources in a heap, call [- useHeap:stages:](<mtlrendercommandencoder/useheap(__stages_).md>) or [- useHeap:](<mtlcomputecommandencoder/useheap(__).md>).

These methods perform two important functions:

- They add argument buffer resources to the set of resources that the render or compute pass needs resident.
- They ensure that argument buffer resources are in a format that’s compatible with the required function operation, as an [MTLResourceUsage](mtlresourceusage.md) value specifies.

The methods with a `stages` parameter also insert dependency hazards, similar to [MTLFence](mtlfence.md) instances for that stage.

Call these methods before issuing any draw or dispatch calls that may access the specified resources.

> [!note] Note
> To track resource access and dependency hazards, use [MTLFence](mtlfence.md) instances.
>
> If all the required resources aren’t resident when executing a render or compute pass, the associated [MTLCommandBuffer](mtlcommandbuffer.md) instance fails.

## See Also

### Argument buffers

- [Improving CPU performance by using argument buffers](improving-cpu-performance-by-using-argument-buffers.md) — Optimize your app’s performance by grouping your resources into argument buffers.
- [Managing groups of resources with argument buffers](managing-groups-of-resources-with-argument-buffers.md) — Create argument buffers to organize related resources.
- [Indexing argument buffers](indexing-argument-buffers.md) — Assign resource indices within an argument buffer.
- [Rendering terrain dynamically with argument buffers](rendering-terrain-dynamically-with-argument-buffers.md) — Use argument buffers to render terrain in real time with a GPU-driven pipeline.
- [Encoding argument buffers on the GPU](encoding-argument-buffers-on-the-gpu.md) — Use a compute pass to encode an argument buffer and access its arguments in a subsequent render pass.
- [Using argument buffers with resource heaps](using-argument-buffers-with-resource-heaps.md) — Reduce CPU overhead by using arrays inside argument buffers and combining them with resource heaps.
- [MTLArgumentDescriptor](mtlargumentdescriptor.md) — A representation of an argument within an argument buffer.
- [MTLArgumentEncoder](mtlargumentencoder.md) — An interface you can use to encode argument data into an argument buffer.
- [MTLAttributeStrideStatic](mtlattributestridestatic.md)
