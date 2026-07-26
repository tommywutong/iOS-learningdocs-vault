---
title: reset()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4commandallocator/reset()
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandallocator/reset()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandallocator/reset%28%29.json'
content_hash: 'sha256:3d66b14d89db9946'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandAllocator](../mtl4commandallocator.md)

# reset()

<sub>Instance Method</sub>

Marks the command allocator’s heaps for reuse.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func reset()
```

## Discussion

Calling this method allows new [MTL4CommandBuffer](../mtl4commandbuffer.md) to reuse its existing internal memory heaps to encode new GPU commands.

You are responsible to ensure that all command buffers with memory originating from this allocator instance are complete before calling resetting it.
