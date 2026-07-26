---
title: 'setLayer(_:at:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrasterizationratemapdescriptor/setlayer(_:at:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratemapdescriptor/setlayer(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratemapdescriptor/setlayer%28_%3Aat%3A%29.json'
content_hash: 'sha256:5de2e9846c6594b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateMapDescriptor](../mtlrasterizationratemapdescriptor.md)

# setLayer(_:at:)

<sub>Instance Method</sub>

Sets a configuration for a layer rate map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setLayer(_ layer: MTLRasterizationRateLayerDescriptor?, at layerIndex: Int)
```

## Parameters

- `layer` — A description of a layer to add to the rate map descriptor. Use `nil` to remove the layer at that index.

- `layerIndex` — The index to put the new layer description in.

## Discussion

Calling this method is equivalent to using array subscript syntax.

## See Also

### Configuring the rate map layers

- [layerCount](layercount.md) — The number of layers in the rate map.
- [- layerAtIndex:](<layer(at_).md>) — Returns the layer description for a layer in the rate map.
- [layers](layers.md) — The rasterization rates for one or more layers in the rate map.
- [MTLRasterizationRateLayerArray](../mtlrasterizationratelayerarray.md) — Descriptions for the rasterization rates to apply to the set of layers in a rate map.
