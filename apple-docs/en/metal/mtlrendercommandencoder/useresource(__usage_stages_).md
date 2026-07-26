---
title: 'useResource(_:usage:stages:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/useresource(_:usage:stages:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/useresource(_:usage:stages:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/useresource%28_%3Ausage%3Astages%3A%29.json'
content_hash: 'sha256:fcbdd9c1de109a56'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# useResource(_:usage:stages:)

<sub>Instance Method</sub>

Ensures the shaders in the render pass’s subsequent draw commands have access to a resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func useResource(_ resource: any MTLResource, usage: MTLResourceUsage, stages: MTLRenderStages)
```

## Parameters

- `resource` — An [MTLResource](../mtlresource.md) instance that subsequent draw commands depend on.

- `usage` — All the applicable access types the render pass’s shaders use for the resource, including [MTLResourceUsageRead](../mtlresourceusage/read.md) and [MTLResourceUsageWrite](../mtlresourceusage/write.md). For applicable resources, you may be able to prevent the GPU from unnecessarily decompressing color attachments on some devices by setting `usage` to [MTLResourceUsageRead](../mtlresourceusage/read.md).

- `stages` — All the render stages that depend on `resource`, including [MTLRenderStageObject](../mtlrenderstages/object.md), [MTLRenderStageMesh](../mtlrenderstages/mesh.md), [MTLRenderStageVertex](../mtlrenderstages/vertex.md), [MTLRenderStageFragment](../mtlrenderstages/fragment.md), and [MTLRenderStageTile](../mtlrenderstages/tile.md).

## Discussion

You can make a resource _resident_ (available in GPU memory) for the remaining duration of the render pass by calling this method. Call the method before encoding draw calls that may access `resource` through an argument buffer. The method ensures the resource is in a format that’s compatible with the shaders that depend on it.

> [!note] Note
> You don’t need to call this method if you bind a resource to a shader stage.

For example, you can explicitly bind resources for the vertex stage with the methods in the [Vertex shader resource preparation commands](../vertex-shader-resource-preparation-commands.md) collection.

The method also informs Metal when to apply hazard tracking for a resource you create with [MTLHazardTrackingModeTracked](../mtlhazardtrackingmode/tracked.md). For a resource you create with [MTLHazardTrackingModeUntracked](../mtlhazardtrackingmode/untracked.md), you need to apply an [MTLFence](../mtlfence.md) or an [MTLEvent](../mtlevent.md) to account for potential reading and writing hazards.

You can reconfigure an individual resource’s `usage` options for subsequent draw calls in the same render pass by calling this method again.

Apps typically call the method for a resource in an argument buffer as a part of their _bindless_ implementation. For more information about argument buffers and bindless implementations, see [Improving CPU performance by using argument buffers](../improving-cpu-performance-by-using-argument-buffers.md) and [Go bindless with Metal 3](https://developer.apple.com/videos/play/wwdc2022/10101/), respectively.

## See Also

### Loading individual resources for argument buffers

- [useResources(_:usage:stages:)](<useresources(__usage_stages_).md>) — Ensures the shaders in the render pass’s subsequent draw commands have access to multiple resources.
