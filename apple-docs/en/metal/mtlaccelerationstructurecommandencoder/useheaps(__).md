---
title: 'useHeaps(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlaccelerationstructurecommandencoder/useheaps(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/useheaps(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlaccelerationstructurecommandencoder/useheaps%28_%3A%29.json'
content_hash: 'sha256:7db46d63a1905224'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAccelerationStructureCommandEncoder](../mtlaccelerationstructurecommandencoder.md)

# useHeaps(_:)

<sub>Instance Method</sub>

Makes the resources contained in the specified heaps available to the acceleration structure pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func useHeaps(_ heaps: [any MTLHeap])
```

## Parameters

- `heaps` — The sets of heap that contain resources to mark as used.

## Discussion

This method makes all the resources in multiple heaps resident for the duration of a compute pass and ensures that they’re in a format compatible with the compute function.

Call this method before issuing any dispatch calls that may access the resources in the heap.

You can only read or sample resources in the specified heap. This method ignores render targets (textures that specify a [MTLTextureUsageRenderTarget](../mtltextureusage/rendertarget.md) usage option) and writable textures (textures that specify a [MTLTextureUsageShaderWrite](../mtltextureusage/shaderwrite.md) usage option) within the heap. To use these resources, you need to call the [- useResource:usage:](<../mtlcomputecommandencoder/useresource(__usage_).md>) method instead.

> [!note] Note
> You can synchronize memory operations to address dependency hazards with [MTLFence](../mtlfence.md) instances.

## See Also

### Making indirect resources resident

- [- useHeap:](<useheap(__).md>) — Makes the resources contained in the specified heap available to the acceleration structure pass.
- [- useResource:usage:](<useresource(__usage_).md>) — Makes a resource available to the acceleration structure pass.
- [useResources(_:usage:)](<useresources(__usage_).md>) — Makes multiple resources available to the acceleration structure pass.
- [MTLResourceUsage](../mtlresourceusage.md) — Options that describe how a graphics or compute function uses an argument buffer’s resource.
