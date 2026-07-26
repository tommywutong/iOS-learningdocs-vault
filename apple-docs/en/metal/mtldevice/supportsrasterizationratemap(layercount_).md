---
title: 'supportsRasterizationRateMap(layerCount:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/supportsrasterizationratemap(layercount:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/supportsrasterizationratemap(layercount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/supportsrasterizationratemap%28layercount%3A%29.json'
content_hash: 'sha256:04767a4c7e88e9e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# supportsRasterizationRateMap(layerCount:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the GPU can create a rasterization rate map with a specific number of layers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func supportsRasterizationRateMap(layerCount: Int) -> Bool
```

## Parameters

- `layerCount` — The number of layers for a rasterization rate map.

## See Also

### Creating rasterization rate maps

- [- newRasterizationRateMapWithDescriptor:](<makerasterizationratemap(descriptor_).md>) — Creates a rasterization rate map instance.
