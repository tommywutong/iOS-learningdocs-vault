---
title: MTLRasterizationRateMap
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrasterizationratemap
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratemap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratemap.json'
content_hash: 'sha256:230f3f5e1bf8a997'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLRasterizationRateMap

<sub>Protocol</sub>

A compiled read-only instance that determines how to apply variable rasterization rates when rendering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLRasterizationRateMap : NSObjectProtocol, Sendable
```

## Overview

Use a rasterization rate map to reduce rendering quality in less-important or less-sampled regions of the render target, such as areas affected by blur effects or a far-away cascade of a shadow map.

By default, a render pass doesn’t have a rasterization rate map, and the viewport coordinate system maps exactly to physical pixels in the targeted textures. If you apply a rasterization rate map to a render pass, the viewport coordinate system becomes a logical coordinate system, and the rate map describes how to map logical coordinates to physical pixels in the render pass’s targets. You can specify different rasterization rates in different regions of the logical coordinate system. When you do, those logical units map to fewer physical pixels, which means you can use smaller render targets and render fewer pixels, saving both memory and processing time. For more information, see [Rendering at different rasterization rates](rendering-at-different-rasterization-rates.md).

Don’t implement this protocol yourself; instead, create an [MTLRasterizationRateMapDescriptor](mtlrasterizationratemapdescriptor.md) instance, configure it, and then call the [- newRasterizationRateMapWithDescriptor:](<mtldevice/makerasterizationratemap(descriptor_).md>) on a device instance.

To apply a rasterization rate map to a render pass, set the render pass descriptor’s [rasterizationRateMap](mtlrenderpassdescriptor/rasterizationratemap.md) property.

### Configuring the rate map

A rasterization rate map specifies the size of the viewport coordinate space in logical units and one or more _layer maps_. A layer map partitions the viewport coordinate space into a 2D grid of cells and defines the rasterization rate for each cell. If you aren’t using layered rendering, provide a single layer map; otherwise, provide one layer map for each layer. For more information about layered rendering, see [Rendering to multiple texture slices in a draw command](rendering-to-multiple-texture-slices-in-a-draw-command.md).

You can query the physical size requirements for each layer in the render pass by calling the [- physicalSizeForLayer:](<mtlrasterizationratemap/physicalsize(layer_).md>) method. Your render targets need to be at least this large.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Identifying the rate map

- [device](mtlrasterizationratemap/device.md) — The device object that created the rate map.
- [label](mtlrasterizationratemap/label.md) — A string that identifies the rate map.

### Inspecting geometric and rendering properties

- [layerCount](mtlrasterizationratemap/layercount.md) — The number of layers in the rate map.
- [screenSize](mtlrasterizationratemap/screensize.md) — The logical size, in pixels, of the viewport coordinate system.
- [- physicalSizeForLayer:](<mtlrasterizationratemap/physicalsize(layer_).md>) — Returns the dimensions, in pixels, of the area in the render target affected by the rasterization rate map.
- [physicalGranularity](mtlrasterizationratemap/physicalgranularity.md) — The granularity, in physical pixels, at which the rasterization rate varies.

### Converting between viewport and physical coordinates

- [- mapScreenToPhysicalCoordinates:forLayer:](<mtlrasterizationratemap/physicalcoordinates(screencoordinates_layer_).md>) — Converts a point in logical viewport coordinates to the corresponding physical coordinates in a render layer.
- [- mapPhysicalToScreenCoordinates:forLayer:](<mtlrasterizationratemap/screencoordinates(physicalcoordinates_layer_).md>) — Converts a point in physical coordinates inside a layer to its corresponding logical viewport coordinates.

### Obtaining coordinate transformation data

- [parameterBufferSizeAndAlign](mtlrasterizationratemap/parameterdatasizeandalign.md) — The size and alignment requirements to contain the coordinate transformation information in this rate map.
- [- copyParameterDataToBuffer:offset:](<mtlrasterizationratemap/copyparameterdata(buffer_offset_).md>) — Copies the parameter data into the provided buffer.

## See Also

### Rasterization settings

- [Rendering at different rasterization rates](rendering-at-different-rasterization-rates.md) — Configure a rasterization rate map to vary rasterization rates depending on the amount of detail needed.
- [Creating a rasterization rate map](creating-a-rasterization-rate-map.md) — Define the rasterization rates for each part of your render target.
- [Rendering with a rasterization rate map](rendering-with-a-rasterization-rate-map.md) — Create offscreen textures to hold intermediate rasterized data.
- [Scaling variable rasterization rate content](scaling-variable-rasterization-rate-content.md) — Use the rate map data to scale the content to fill your destination texture.
- [MTLRasterizationRateMapDescriptor](mtlrasterizationratemapdescriptor.md) — An object that you use to configure new rasterization rate maps.
- [MTLCoordinate2D](mtlcoordinate2d.md) — A coordinate in the viewport.
- [MTLCoordinate2DMake](<mtlcoordinate2dmake(____).md>) — Returns a new 2D point with the specified coordinates.
