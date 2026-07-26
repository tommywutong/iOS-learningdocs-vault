---
title: 'imageblockMemoryLength(forDimensions:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputepipelinestate/imageblockmemorylength(fordimensions:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/imageblockmemorylength(fordimensions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepipelinestate/imageblockmemorylength%28fordimensions%3A%29.json'
content_hash: 'sha256:29706ab7ed6d23dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePipelineState](../mtlcomputepipelinestate.md)

# imageblockMemoryLength(forDimensions:)

<sub>Instance Method</sub>

Returns the length of reserved memory for an imageblock of a given size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func imageblockMemoryLength(forDimensions imageblockDimensions: MTLSize) -> Int
```

## Parameters

- `imageblockDimensions` — An [MTLSize](../mtlsize.md) instance that represents the dimensions of an imageblock.

## Return Value

The length, in bytes, occupied by the image block in memory.
