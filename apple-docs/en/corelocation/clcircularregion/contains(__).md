---
title: 'contains(_:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+（27.0 起废弃）, iPadOS 7.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corelocation/clcircularregion/contains(_:)'
source_url: 'https://developer.apple.com/documentation/corelocation/clcircularregion/contains(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clcircularregion/contains%28_%3A%29.json'
content_hash: 'sha256:fd3383b9318bd64b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLCircularRegion](../clcircularregion.md)

# contains(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the geographic area contains the specified coordinate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
func contains(_ coordinate: CLLocationCoordinate2D) -> Bool
```

## Parameters

- `coordinate` — The coordinate to test against the region.

## Return Value

Returns [true](../../swift/true.md) if the coordinate lies within the region’s boundaries, or [false](../../swift/false.md) if it doesn’t.
