---
title: layerCount
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrasterizationratemapdescriptor/layercount
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratemapdescriptor/layercount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratemapdescriptor/layercount.json'
content_hash: 'sha256:7c1b7ad0e39d0c82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateMapDescriptor](../mtlrasterizationratemapdescriptor.md)

# layerCount

<sub>Instance Property</sub>

The number of layers in the rate map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var layerCount: Int { get }
```

## Discussion

The value of this property is dynamically determined based on how many layers you’ve added to the descriptor. To add a new layer, call [- setLayer:atIndex:](<setlayer(__at_).md>) or use the subscripting operator to assign a layer.

## See Also

### Configuring the rate map layers

- [- layerAtIndex:](<layer(at_).md>) — Returns the layer description for a layer in the rate map.
- [- setLayer:atIndex:](<setlayer(__at_).md>) — Sets a configuration for a layer rate map.
- [layers](layers.md) — The rasterization rates for one or more layers in the rate map.
- [MTLRasterizationRateLayerArray](../mtlrasterizationratelayerarray.md) — Descriptions for the rasterization rates to apply to the set of layers in a rate map.
