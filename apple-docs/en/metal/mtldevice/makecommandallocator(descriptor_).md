---
title: 'makeCommandAllocator(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makecommandallocator(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makecommandallocator(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makecommandallocator%28descriptor%3A%29.json'
content_hash: 'sha256:7a96170940ca23ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeCommandAllocator(descriptor:)

<sub>Instance Method</sub>

Creates a new command allocator from a command allocator descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeCommandAllocator(descriptor: MTL4CommandAllocatorDescriptor) throws -> any MTL4CommandAllocator
```

## Parameters

- `descriptor` — A [MTL4CommandAllocatorDescriptor](../mtl4commandallocatordescriptor.md) instance that configures the [MTL4CommandAllocator](../mtl4commandallocator.md) instance.

## Return Value

A [MTL4CommandAllocator](../mtl4commandallocator.md) instance, or `nil` if the function failed.
