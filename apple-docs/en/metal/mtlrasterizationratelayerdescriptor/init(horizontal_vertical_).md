---
title: 'init(horizontal:vertical:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrasterizationratelayerdescriptor/init(horizontal:vertical:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratelayerdescriptor/init(horizontal:vertical:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratelayerdescriptor/init%28horizontal%3Avertical%3A%29.json'
content_hash: 'sha256:fc7cd72d479eb904'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateLayerDescriptor](../mtlrasterizationratelayerdescriptor.md)

# init(horizontal:vertical:)

<sub>Initializer</sub>

Initializes a layer rate map with a set of horizontal and vertical rasterization rates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(horizontal: [Float], vertical: [Float])
```

## Parameters

- `horizontal` — An array of the horizontal rates to apply across the grid.

- `vertical` — An array of the vertical rates to apply across the grid.

## Return Value

A layer descriptor whose width is the number of horizontal rates and whose height is the number of vertical rates. The layer descriptor copies the values from the input parameters.

## See Also

### Creating a layer rasterization rate descriptor

- [- initWithSampleCount:](<init(samplecount_).md>) — Initializes the layer map with an empty grid.
