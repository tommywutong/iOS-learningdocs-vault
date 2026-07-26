---
title: 'MKMapSizeEqualToSize(_:_:)'
framework: MapKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapsizeequaltosize(_:_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapsizeequaltosize(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapsizeequaltosize%28_%3A_%3A%29.json'
content_hash: 'sha256:3f29789cbc691964'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMapSizeEqualToSize(_:_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether two map sizes are equal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func MKMapSizeEqualToSize(_ size1: MKMapSize, _ size2: MKMapSize) -> Bool
```

## Parameters

- `size1` — The first map size.

- `size2` — The second map size.

## Return Value

[true](../swift/true.md) if the `width` and `height` values in both sizes are exactly the same, or [false](../swift/false.md) if one or both values are different.
