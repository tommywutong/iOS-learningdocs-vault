---
title: 'useResources:count:usage:stages:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/useresources:count:usage:stages:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/useresources:count:usage:stages:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/useresources%3Acount%3Ausage%3Astages%3A.json'
content_hash: 'sha256:a46ea9ebd2a9b415'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# useResources:count:usage:stages:

<sub>Instance Method</sub>

Ensures the shaders in the render pass’s subsequent draw commands have access to multiple resources.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) useResources:(id<MTLResource> const[]) resources count:(NSUInteger) count usage:(MTLResourceUsage) usage stages:(MTLRenderStages) stages;
```

## Parameters

- `resources` — A pointer to a C array of [MTLResource](../mtlresource.md) instances that subsequent draw commands depend on.

- `count` — The number of elements in `resources`.

- `usage` — All the applicable access types the render pass’s shaders use for `resource`, including [MTLResourceUsageRead](../mtlresourceusage/read.md) and [MTLResourceUsageWrite](../mtlresourceusage/write.md). For applicable resources, you may be able to prevent the GPU from unnecessarily decompressing color attachments on some devices by setting `usage` to [MTLResourceUsageRead](../mtlresourceusage/read.md).

- `stages` — All the render stages that depend on elements in `resources`, including [MTLRenderStageObject](../mtlrenderstages/object.md), [MTLRenderStageMesh](../mtlrenderstages/mesh.md), [MTLRenderStageVertex](../mtlrenderstages/vertex.md), [MTLRenderStageFragment](../mtlrenderstages/fragment.md), and [MTLRenderStageTile](../mtlrenderstages/tile.md).

## Discussion

You can make multiple resources _resident_ (available in GPU memory) for the remaining duration of the render pass by calling this method. Call the method before encoding draw calls that may access the elements of `resources` through an argument buffer. The method ensures each resource is in a format that’s compatible with the shaders that depend on it.

> [!note] Note
> You don’t need to call this method if you bind a resource to a shader stage.

For example, you can explicitly bind resources for the vertex stage with the methods in the [Vertex shader resource preparation commands](../vertex-shader-resource-preparation-commands.md) collection.

The method also informs Metal when to apply hazard tracking for the resources you create with [MTLHazardTrackingModeTracked](../mtlhazardtrackingmode/tracked.md). For resources you create with [MTLHazardTrackingModeUntracked](../mtlhazardtrackingmode/untracked.md), you need to apply an [MTLFence](../mtlfence.md) or an [MTLEvent](../mtlevent.md) to account for potential reading and writing hazards.

You can reconfigure an individual resource’s `usage` options for subsequent draw calls in the same render pass by calling this method again.

Apps typically call the method for resources in an argument buffer as a part of their _bindless_ implementation. For more information about argument buffers and bindless implementations, see [Improving CPU performance by using argument buffers](../improving-cpu-performance-by-using-argument-buffers.md) and [Go bindless with Metal 3](https://developer.apple.com/videos/play/wwdc2022/10101/), respectively.

## See Also

### Loading individual resources for argument buffers

- [- useResource:usage:stages:](<useresource(__usage_stages_).md>) — Ensures the shaders in the render pass’s subsequent draw commands have access to a resource.
