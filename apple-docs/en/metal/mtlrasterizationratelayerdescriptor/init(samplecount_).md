---
title: 'init(sampleCount:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrasterizationratelayerdescriptor/init(samplecount:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratelayerdescriptor/init(samplecount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratelayerdescriptor/init%28samplecount%3A%29.json'
content_hash: 'sha256:18f4c0d744f69edc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateLayerDescriptor](../mtlrasterizationratelayerdescriptor.md)

# init(sampleCount:)

<sub>Initializer</sub>

Initializes the layer map with an empty grid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(sampleCount: MTLSize)
```

## Parameters

- `sampleCount` — The size of the grid. Specify the width and height to determine the number of columns and rows in the layer map. The initializer ignores the depth component.

## Return Value

A layer descriptor with a grid of the specified size. All of the rasterization rates are set to `0.0`.

## See Also

### Creating a layer rasterization rate descriptor

- [init(horizontal:vertical:)](<init(horizontal_vertical_).md>) — Initializes a layer rate map with a set of horizontal and vertical rasterization rates.
