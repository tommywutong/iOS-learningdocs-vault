---
title: makeCommandAllocator()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/makecommandallocator()
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makecommandallocator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makecommandallocator%28%29.json'
content_hash: 'sha256:fa5d3013449f2eae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeCommandAllocator()

<sub>Instance Method</sub>

Creates a new command allocator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeCommandAllocator() -> (any MTL4CommandAllocator)?
```

## Return Value

A [MTL4CommandAllocator](../mtl4commandallocator.md) instance, or `nil` if the function failed.
