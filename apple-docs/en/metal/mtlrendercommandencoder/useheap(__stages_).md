---
title: 'useHeap(_:stages:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/useheap(_:stages:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/useheap(_:stages:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/useheap%28_%3Astages%3A%29.json'
content_hash: 'sha256:66eca2d0823484ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# useHeap(_:stages:)

<sub>Instance Method</sub>

Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from a heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func useHeap(_ heap: any MTLHeap, stages: MTLRenderStages)
```

## Parameters

- `heap` — An [MTLHeap](../mtlheap.md) instance with resources that subsequent draw commands depend on.

- `stages` — All the render stages that depend on resources within `heap`, including [MTLRenderStageObject](../mtlrenderstages/object.md), [MTLRenderStageMesh](../mtlrenderstages/mesh.md), [MTLRenderStageVertex](../mtlrenderstages/vertex.md), [MTLRenderStageFragment](../mtlrenderstages/fragment.md), and [MTLRenderStageTile](../mtlrenderstages/tile.md).

## Discussion

You can make the resources in `heap` _resident_ (available in GPU memory) for the remaining duration of the render pass by calling this method. Call the method before encoding draw calls that may access resources within `heap` through an argument buffer. The method ensures each resource is in a format that’s compatible with the shaders that depend on it.

The method’s applies the [MTLResourceUsageRead](../mtlresourceusage/read.md) resource usage option to all of the resources within `heap`, except for textures. The method ignores any texture that has [MTLTextureUsageRenderTarget](../mtltextureusage/rendertarget.md), [MTLTextureUsageShaderWrite](../mtltextureusage/shaderwrite.md), or both in its [usage](../mtltexture/usage.md) property. For all other textures in `heap`, the method optimizes each texture’s memory layout for rendering with a sampler. However, your shaders can’t read from those textures by calling this method because the texture needs a different memory layout that’s suitable for reading.

> [!important] Important
> You can instruct Metal to allow a shader to read from texture or write to other resources in heap, by calling [- useResource:usage:stages:](<useresource(__usage_stages_).md>).

Methods that apply a usage option for resources (see [Argument buffer resource preparation commands](../argument-buffer-resource-preparation-commands.md)) override any previous calls that apply to a resource. For example, you can change the usage option for buffer in `heap` to [MTLResourceUsageWrite](../mtlresourceusage/write.md) by passing it to [- useResource:usage:stages:](<useresource(__usage_stages_).md>) after calling this method. However, you can’t reverse the call order because this method resets the usage for all resources within `heap` to [MTLResourceUsageRead](../mtlresourceusage/read.md), overriding previous calls to [- useResource:usage:stages:](<useresource(__usage_stages_).md>).

The method instructs Metal to apply hazard tracking for resources you allocate from a heap that you create with [MTLHazardTrackingModeTracked](../mtlhazardtrackingmode/tracked.md). However, for untracked resources — which come from heaps you create with [MTLHazardTrackingModeUntracked](../mtlhazardtrackingmode/untracked.md) — you need to account for hazards by applying [MTLFence](../mtlfence.md) or [MTLEvent](../mtlevent.md) instances.

> [!note] Note
> The [hazardTrackingMode](../mtlheapdescriptor/hazardtrackingmode.md) property of a new [MTLHeapDescriptor](../mtlheapdescriptor.md) instance is [MTLHazardTrackingModeDefault](../mtlhazardtrackingmode/default.md), which is equivalent to [MTLHazardTrackingModeUntracked](../mtlhazardtrackingmode/untracked.md) because heaps don’t track resources by default.

Apps typically call the method for heaps that have resources in argument buffers for a _bindless_ implementation. For more information about argument buffers and bindless implementations, see [Improving CPU performance by using argument buffers](../improving-cpu-performance-by-using-argument-buffers.md) and [Go bindless with Metal 3](https://developer.apple.com/videos/play/wwdc2022/10101/), respectively.

## See Also

### Loading heaps and the resources they contain for argument buffers

- [useHeaps(_:stages:)](<useheaps(__stages_).md>) — Ensures the shaders in the render pass’s subsequent draw commands have access to the resources you allocate from multiple heaps.
