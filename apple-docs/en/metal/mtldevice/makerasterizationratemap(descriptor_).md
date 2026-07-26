---
title: 'makeRasterizationRateMap(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makerasterizationratemap(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makerasterizationratemap(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makerasterizationratemap%28descriptor%3A%29.json'
content_hash: 'sha256:de29bfbc8a34169e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeRasterizationRateMap(descriptor:)

<sub>Instance Method</sub>

Creates a rasterization rate map instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeRasterizationRateMap(descriptor: MTLRasterizationRateMapDescriptor) -> (any MTLRasterizationRateMap)?
```

## Parameters

- `descriptor` — An [MTLRasterizationRateMapDescriptor](../mtlrasterizationratemapdescriptor.md) instance.

## Return Value

A new [MTLRasterizationRateMapDescriptor](../mtlrasterizationratemapdescriptor.md) instance if the method completes successfully; otherwise `nil`.

## See Also

### Creating rasterization rate maps

- [- supportsRasterizationRateMapWithLayerCount:](<supportsrasterizationratemap(layercount_).md>) — Returns a Boolean value that indicates whether the GPU can create a rasterization rate map with a specific number of layers.
