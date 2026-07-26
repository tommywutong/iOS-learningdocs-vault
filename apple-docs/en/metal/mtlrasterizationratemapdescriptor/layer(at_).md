---
title: 'layer(at:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrasterizationratemapdescriptor/layer(at:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratemapdescriptor/layer(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratemapdescriptor/layer%28at%3A%29.json'
content_hash: 'sha256:e5095df357a16497'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateMapDescriptor](../mtlrasterizationratemapdescriptor.md)

# layer(at:)

<sub>Instance Method</sub>

Returns the layer description for a layer in the rate map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func layer(at layerIndex: Int) -> MTLRasterizationRateLayerDescriptor?
```

## Parameters

- `layerIndex` — The entry to return.

## Return Value

The [MTLRasterizationRateLayerDescriptor](../mtlrasterizationratelayerdescriptor.md) instance for the given index, or `nil` if you haven’t set an instance for this index.

## Discussion

Calling this method is equivalent to using array subscript syntax.

## See Also

### Configuring the rate map layers

- [layerCount](layercount.md) — The number of layers in the rate map.
- [- setLayer:atIndex:](<setlayer(__at_).md>) — Sets a configuration for a layer rate map.
- [layers](layers.md) — The rasterization rates for one or more layers in the rate map.
- [MTLRasterizationRateLayerArray](../mtlrasterizationratelayerarray.md) — Descriptions for the rasterization rates to apply to the set of layers in a rate map.
