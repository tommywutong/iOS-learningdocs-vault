---
title: MTLRasterizationRateLayerDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrasterizationratelayerdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratelayerdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratelayerdescriptor.json'
content_hash: 'sha256:cba7a8c24b099b5e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLRasterizationRateLayerDescriptor

<sub>Class</sub>

The minimum rasterization rates to apply to sections of a layer in the render target.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLRasterizationRateLayerDescriptor
```

## Overview

Use a layer map to divide the logical viewport coordinate system into a 2D grid of equal-sized rectangles, and choose different rasterization rates for each cell.

Specify rasterization rates using floating-point numbers between `0.0` and `1.0`, inclusive. A rate of `1.0` represents the normal rasterization rate, where each logical unit is equal to a physical pixel; a rate of `0.5` means that two logical units equate to one physical pixel, and so on. A value of `0.0` means that the GPU renders at its lowest quality level. When you create the map, the device object chooses the nearest rasterization rate supported by the GPU that meets or exceeds the rate you specified.

In the layer map, you provide separate rasterization rates for the grid’s rows and columns. The horizontal rates specify a horizontal rasterization rate for each column, and the vertical rates specify a vertical rasterization rate for each row. Each cell calculates its physical size in pixels by using the logical size of cells in the map, the horizontal rate from the cell’s column, and the vertical rate from its row.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a layer rasterization rate descriptor

- [- initWithSampleCount:](<mtlrasterizationratelayerdescriptor/init(samplecount_).md>) — Initializes the layer map with an empty grid.
- [init(horizontal:vertical:)](<mtlrasterizationratelayerdescriptor/init(horizontal_vertical_).md>) — Initializes a layer rate map with a set of horizontal and vertical rasterization rates.

### Inspecting the layer rate function parameters

- [sampleCount](mtlrasterizationratelayerdescriptor/samplecount.md) — The number of rows and columns in the layer map.
- [maxSampleCount](mtlrasterizationratelayerdescriptor/maxsamplecount.md) — The maximum number of rows and columns in the layer map.
- [horizontal](mtlrasterizationratelayerdescriptor/horizontal.md) — The horizontal rasterization rates for the layer map’s rows.
- [vertical](mtlrasterizationratelayerdescriptor/vertical.md) — The vertical rasterization rates for the layer map’s rows.
- [MTLRasterizationRateSampleArray](mtlrasterizationratesamplearray.md) — An array instance that contains rasterization rates.

## See Also

### Accessing members of the array

- [- objectAtIndexedSubscript:](<mtlrasterizationratelayerarray/subscript(__).md>) — Retrieves the sample value at the specified index.
