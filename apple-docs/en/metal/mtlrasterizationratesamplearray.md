---
title: MTLRasterizationRateSampleArray
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrasterizationratesamplearray
source_url: 'https://developer.apple.com/documentation/metal/mtlrasterizationratesamplearray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrasterizationratesamplearray.json'
content_hash: 'sha256:9fac8f50e6f45aa5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLRasterizationRateSampleArray

<sub>Class</sub>

An array instance that contains rasterization rates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLRasterizationRateSampleArray
```

## Overview

The [horizontal](mtlrasterizationratelayerdescriptor/horizontal.md) and [vertical](mtlrasterizationratelayerdescriptor/vertical.md) properties of an [MTLRasterizationRateLayerDescriptor](mtlrasterizationratelayerdescriptor.md) point to [MTLRasterizationRateSampleArray](mtlrasterizationratesamplearray.md) instances that contains rasterization rates for the layer map. You can use array subscript syntax to access the samples. [MTLRasterizationRateSampleArray](mtlrasterizationratesamplearray.md) instances perform bounds checking on any memory operations you make to their sample data.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing the array

- [subscript(_:)](<mtlrasterizationratesamplearray/subscript(__).md>) — Retrieves the sample value at the specified index.

## See Also

### Inspecting the layer rate function parameters

- [sampleCount](mtlrasterizationratelayerdescriptor/samplecount.md) — The number of rows and columns in the layer map.
- [maxSampleCount](mtlrasterizationratelayerdescriptor/maxsamplecount.md) — The maximum number of rows and columns in the layer map.
- [horizontal](mtlrasterizationratelayerdescriptor/horizontal.md) — The horizontal rasterization rates for the layer map’s rows.
- [vertical](mtlrasterizationratelayerdescriptor/vertical.md) — The vertical rasterization rates for the layer map’s rows.
