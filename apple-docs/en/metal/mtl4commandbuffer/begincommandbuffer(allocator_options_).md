---
title: 'beginCommandBuffer(allocator:options:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandbuffer/begincommandbuffer(allocator:options:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandbuffer/begincommandbuffer(allocator:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandbuffer/begincommandbuffer%28allocator%3Aoptions%3A%29.json'
content_hash: 'sha256:990a20a8705d78c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandBuffer](../mtl4commandbuffer.md)

# beginCommandBuffer(allocator:options:)

<sub>Instance Method</sub>

Prepares a command buffer for encoding with additional options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func beginCommandBuffer(allocator: any MTL4CommandAllocator, options: MTL4CommandBufferOptions)
```

## Parameters

- `allocator` — [MTL4CommandAllocator](../mtl4commandallocator.md) to attach to.

- `options` — [MTL4CommandBufferOptions](../mtl4commandbufferoptions.md) to configure the command buffer.

## Discussion

Attaches the command buffer to the specified [MTL4CommandAllocator](../mtl4commandallocator.md) and declares that the application is ready to encode commands into the command buffer.

Command allocators only service a single command buffer at a time. If you need to issue multiple calls to this method simultaneously, for example, in a multi-threaded command encoding scenario, create multiple instances of `MTLCommandAllocator` and use one for each call.

You can safely reuse command allocators after ending the command buffer using it by calling [- endCommandBuffer](<endcommandbuffer().md>).

After calling this method, any prior calls to [- useResidencySet:](<useresidencyset(__).md>) and [useResidencySets:count:](useresidencysets_count_.md) on this command buffer instance no longer apply. Make sure to call these methods again to signal your residency requirements to Metal.

The options you provide configure the command buffer only until the command buffer ends, in the next call to [- endCommandBuffer](<endcommandbuffer().md>).
