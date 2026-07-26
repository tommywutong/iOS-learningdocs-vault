---
title: 'useResource(_:usage:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（16.0 起废弃）, iPadOS 11.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.13+（13.0 起废弃）, tvOS 11.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtlrendercommandencoder/useresource(_:usage:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/useresource(_:usage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/useresource%28_%3Ausage%3A%29.json'
content_hash: 'sha256:98f39c6631983e7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# useResource(_:usage:)

<sub>Instance Method</sub>

Ensures the shaders in the render pass’s subsequent draw commands have access to a resource.

> [!warning] Deprecated
> Call [- useResource:usage:stages:](<useresource(__usage_stages_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func useResource(_ resource: any MTLResource, usage: MTLResourceUsage)
```

## Parameters

- `resource` — An [MTLResource](../mtlresource.md) instance that subsequent draw commands depend on.

- `usage` — All the applicable access types the render pass’s shaders use for `resource`, including [MTLResourceUsageRead](../mtlresourceusage/read.md) and [MTLResourceUsageWrite](../mtlresourceusage/write.md). For applicable resources, you may be able to prevent the GPU from unnecessarily decompressing color attachments on some devices by setting `usage` to [MTLResourceUsageRead](../mtlresourceusage/read.md).

## Discussion

You can make a resource _resident_ (available in GPU memory) for the remaining duration of the render pass by calling this method. Call the method before encoding draw calls that may access `resource` through an argument buffer. The method ensures the resource is in a format that’s compatible with the shaders that depend on it.

> [!note] Note
> You don’t need to call this method if you bind a resource to a shader stage.

For example, you can explicitly bind resources for the vertex stage with the methods in the [Vertex shader resource preparation commands](../vertex-shader-resource-preparation-commands.md) collection.

The method also informs Metal when to apply hazard tracking for a resource you create with [MTLHazardTrackingModeTracked](../mtlhazardtrackingmode/tracked.md). For a resource you create with [MTLHazardTrackingModeUntracked](../mtlhazardtrackingmode/untracked.md), you need to apply an [MTLFence](../mtlfence.md) or an [MTLEvent](../mtlevent.md) to account for potential reading and writing hazards.

You can reconfigure an individual resource’s `usage` options for subsequent draw calls in the same render pass by calling this method again.

Apps typically call the method for a resource in an argument buffer as a part of their _bindless_ implementation. For more information about argument buffers and bindless implementations, see [Improving CPU performance by using argument buffers](../improving-cpu-performance-by-using-argument-buffers.md) and [Go bindless with Metal 3](https://developer.apple.com/videos/play/wwdc2022/10101/), respectively.

## See Also

### Deprecated methods

- [use(_:usage:stages:)](<use(__usage_stages_).md>) — Ensures the shaders in the render pass’s subsequent draw commands have access to a resource. _(deprecated)_
- [useResources(_:usage:)](<useresources(__usage_).md>) — Ensures the shaders in the render pass’s subsequent draw commands have access to multiple resources. _(deprecated)_
- [use(_:count:usage:stages:)](<use(__count_usage_stages_).md>) — Ensures the shaders in the render pass’s subsequent draw commands have access to multiple resources. _(deprecated)_
- [- useHeap:](<useheap(__).md>) — Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from a heap. _(deprecated)_
- [use(_:stages:)](<use(__stages_).md>) — Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from a heap. _(deprecated)_
- [useHeaps(_:)](<useheaps(__).md>) — Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from multiple heaps. _(deprecated)_
- [use(_:count:stages:)](<use(__count_stages_).md>) — Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from multiple heaps. _(deprecated)_
- [- textureBarrier](<texturebarrier().md>) — Adds a barrier, which forces any texture read operations to wait until write operations to the same texture finish. _(deprecated)_
