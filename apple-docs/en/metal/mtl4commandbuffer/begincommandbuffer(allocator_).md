---
title: 'beginCommandBuffer(allocator:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandbuffer/begincommandbuffer(allocator:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandbuffer/begincommandbuffer(allocator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandbuffer/begincommandbuffer%28allocator%3A%29.json'
content_hash: 'sha256:378a67248ac5b4c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandBuffer](../mtl4commandbuffer.md)

# beginCommandBuffer(allocator:)

<sub>Instance Method</sub>

Prepares a command buffer for encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func beginCommandBuffer(allocator: any MTL4CommandAllocator)
```

## Parameters

- `allocator` — [MTL4CommandAllocator](../mtl4commandallocator.md) to attach to.

## Discussion

Attaches the command buffer to the specified [MTL4CommandAllocator](../mtl4commandallocator.md) and declares that the application is ready to encode commands into the command buffer.

Command allocators only service a single command buffer at a time. If you need to issue multiple calls to this method simultaneously, for example, in a multi-threaded command encoding scenario, create multiple instances of `MTLCommandAllocator` and use one for each call.

You can safely reuse command allocators after ending the command buffer using it by calling [- endCommandBuffer](<endcommandbuffer().md>).

After calling this method, any prior calls to [- useResidencySet:](<useresidencyset(__).md>) and [useResidencySets:count:](useresidencysets_count_.md) on this command buffer instance no longer apply. Make sure to call these methods again to signal your residency requirements to Metal.
