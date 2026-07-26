---
title: 'subscript(_:)'
framework: Metal
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrasterizationratelayerarray/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratelayerarray/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratelayerarray/subscript%28_%3A%29.json'
content_hash: 'sha256:7ab9c52672d9fbfb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRasterizationRateLayerArray](../mtlrasterizationratelayerarray.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Retrieves the sample value at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
subscript(layerIndex: Int) -> MTLRasterizationRateLayerDescriptor? { get set }
```

## Parameters

- `layerIndex` — The index of the sample you want to retrieve.

## Return Value

An [NSNumber](../../foundation/nsnumber.md) instance describing the value of the sample at the specified index, or `0` if the index is out of range.

## See Also

### Accessing members of the array

- [MTLRasterizationRateLayerDescriptor](../mtlrasterizationratelayerdescriptor.md) — The minimum rasterization rates to apply to sections of a layer in the render target.
