---
title: allocatedSize()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4commandallocator/allocatedsize()
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandallocator/allocatedsize()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandallocator/allocatedsize%28%29.json'
content_hash: 'sha256:568c95c3f6db2826'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandAllocator](../mtl4commandallocator.md)

# allocatedSize()

<sub>Instance Method</sub>

Queries the size of the internal memory heaps of this command allocator that support encoding commands into command buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func allocatedSize() -> UInt64
```

## Return Value

A size in bytes.
