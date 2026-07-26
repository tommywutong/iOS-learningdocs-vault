---
title: 'rasterizationRateMapDescriptorWithScreenSize:layerCount:layers:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrasterizationratemapdescriptor/rasterizationratemapdescriptorwithscreensize:layercount:layers:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratemapdescriptor/rasterizationratemapdescriptorwithscreensize:layercount:layers:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratemapdescriptor/rasterizationratemapdescriptorwithscreensize%3Alayercount%3Alayers%3A.json'
content_hash: 'sha256:94c958526670c3f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateMapDescriptor](../mtlrasterizationratemapdescriptor.md)

# rasterizationRateMapDescriptorWithScreenSize:layerCount:layers:

<sub>Type Method</sub>

Creates a rate map descriptor with a set of layer descriptors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (MTLRasterizationRateMapDescriptor *) rasterizationRateMapDescriptorWithScreenSize:(MTLSize) screenSize layerCount:(NSUInteger) layerCount layers:(MTLRasterizationRateLayerDescriptor * const*) layers;
```

## Parameters

- `screenSize` — The logical size, in pixels, of the viewport coordinate system.

- `layerCount` — The number of array elements in `layers`.

- `layers` — An array of rate layer descriptors for the rate map’s layers.

## Return Value

A descriptor object whose [screenSize](screensize.md) is set to the provided size and whose rate map layers are set to the array you provided.

## See Also

### Creating rate map descriptors

- [rasterizationRateMapDescriptorWithScreenSize:](rasterizationratemapdescriptorwithscreensize_.md) — Creates a rate map descriptor with a given size and identifier.
- [rasterizationRateMapDescriptorWithScreenSize:layer:](rasterizationratemapdescriptorwithscreensize_layer_.md) — Creates a rate map descriptor with a single rate layer.
