---
title: 'rasterizationRateMapDescriptorWithScreenSize:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrasterizationratemapdescriptor/rasterizationratemapdescriptorwithscreensize:'
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratemapdescriptor/rasterizationratemapdescriptorwithscreensize:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratemapdescriptor/rasterizationratemapdescriptorwithscreensize%3A.json'
content_hash: 'sha256:5d6ba477af079143'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateMapDescriptor](../mtlrasterizationratemapdescriptor.md)

# rasterizationRateMapDescriptorWithScreenSize:

<sub>Type Method</sub>

Creates a rate map descriptor with a given size and identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (MTLRasterizationRateMapDescriptor *) rasterizationRateMapDescriptorWithScreenSize:(MTLSize) screenSize;
```

## Parameters

- `screenSize` — The logical size, in pixels, of the viewport coordinate system.

## Return Value

A descriptor object whose [screenSize](screensize.md) is set to the provided size. You need to add at least one layer rate map to the descriptor.

## See Also

### Creating rate map descriptors

- [rasterizationRateMapDescriptorWithScreenSize:layer:](rasterizationratemapdescriptorwithscreensize_layer_.md) — Creates a rate map descriptor with a single rate layer.
- [rasterizationRateMapDescriptorWithScreenSize:layerCount:layers:](rasterizationratemapdescriptorwithscreensize_layercount_layers_.md) — Creates a rate map descriptor with a set of layer descriptors.
