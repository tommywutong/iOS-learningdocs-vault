---
title: MTLRasterizationRateMapDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrasterizationratemapdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratemapdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratemapdescriptor.json'
content_hash: 'sha256:7436164b6b6eec9b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLRasterizationRateMapDescriptor

<sub>Class</sub>

An object that you use to configure new rasterization rate maps.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLRasterizationRateMapDescriptor
```

## Overview

To create a new rate map, first create an [MTLRasterizationRateMapDescriptor](mtlrasterizationratemapdescriptor.md) instance and set its property values. Then, create a new rasterization rate-map by calling an [MTLDevice](mtldevice.md) instance’s
[- newRasterizationRateMapWithDescriptor:](<mtldevice/makerasterizationratemap(descriptor_).md>) method.

When creating a rate map, Metal copies into it property values from the descriptor. You can reuse a descrptor by modifying its property values, which doesn’t affect the other rate-map instances that already exist.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating rate map descriptors

- [init(screenSize:label:)](<mtlrasterizationratemapdescriptor/init(screensize_label_).md>) — A convenience initializer that creates a rate map descriptor with a given size and identifier.
- [init(screenSize:layer:label:)](<mtlrasterizationratemapdescriptor/init(screensize_layer_label_).md>) — A convenience initializer that creates a rate map descriptor with a single rate layer.
- [init(screenSize:layers:label:)](<mtlrasterizationratemapdescriptor/init(screensize_layers_label_).md>) — A convenience initializer that creates a rate map descriptor with a set of layer descriptors.

### Identifying the rate map

- [label](mtlrasterizationratemapdescriptor/label.md) — A string used to identify the rate map you create with the descriptor.

### Configuring the viewport size

- [screenSize](mtlrasterizationratemapdescriptor/screensize.md) — The size of the viewport coordinate system, in logical pixels.

### Configuring the rate map layers

- [layerCount](mtlrasterizationratemapdescriptor/layercount.md) — The number of layers in the rate map.
- [- layerAtIndex:](<mtlrasterizationratemapdescriptor/layer(at_).md>) — Returns the layer description for a layer in the rate map.
- [- setLayer:atIndex:](<mtlrasterizationratemapdescriptor/setlayer(__at_).md>) — Sets a configuration for a layer rate map.
- [layers](mtlrasterizationratemapdescriptor/layers.md) — The rasterization rates for one or more layers in the rate map.
- [MTLRasterizationRateLayerArray](mtlrasterizationratelayerarray.md) — Descriptions for the rasterization rates to apply to the set of layers in a rate map.

## See Also

### Rasterization settings

- [Rendering at different rasterization rates](rendering-at-different-rasterization-rates.md) — Configure a rasterization rate map to vary rasterization rates depending on the amount of detail needed.
- [Creating a rasterization rate map](creating-a-rasterization-rate-map.md) — Define the rasterization rates for each part of your render target.
- [Rendering with a rasterization rate map](rendering-with-a-rasterization-rate-map.md) — Create offscreen textures to hold intermediate rasterized data.
- [Scaling variable rasterization rate content](scaling-variable-rasterization-rate-content.md) — Use the rate map data to scale the content to fill your destination texture.
- [MTLRasterizationRateMap](mtlrasterizationratemap.md) — A compiled read-only instance that determines how to apply variable rasterization rates when rendering.
- [MTLCoordinate2D](mtlcoordinate2d.md) — A coordinate in the viewport.
- [MTLCoordinate2DMake](<mtlcoordinate2dmake(____).md>) — Returns a new 2D point with the specified coordinates.
