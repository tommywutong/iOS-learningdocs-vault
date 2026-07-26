---
title: layers
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrasterizationratemapdescriptor/layers
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratemapdescriptor/layers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratemapdescriptor/layers.json'
content_hash: 'sha256:82f9acf76efcdc1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateMapDescriptor](../mtlrasterizationratemapdescriptor.md)

# layers

<sub>Instance Property</sub>

The rasterization rates for one or more layers in the rate map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var layers: MTLRasterizationRateLayerArray { get }
```

## See Also

### Configuring the rate map layers

- [layerCount](layercount.md) — The number of layers in the rate map.
- [- layerAtIndex:](<layer(at_).md>) — Returns the layer description for a layer in the rate map.
- [- setLayer:atIndex:](<setlayer(__at_).md>) — Sets a configuration for a layer rate map.
- [MTLRasterizationRateLayerArray](../mtlrasterizationratelayerarray.md) — Descriptions for the rasterization rates to apply to the set of layers in a rate map.
