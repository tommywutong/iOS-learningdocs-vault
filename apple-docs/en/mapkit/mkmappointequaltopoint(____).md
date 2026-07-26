---
title: 'MKMapPointEqualToPoint(_:_:)'
framework: MapKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmappointequaltopoint(_:_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmappointequaltopoint(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmappointequaltopoint%28_%3A_%3A%29.json'
content_hash: 'sha256:5ef5f184a015b509'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMapPointEqualToPoint(_:_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether two map points are equal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func MKMapPointEqualToPoint(_ point1: MKMapPoint, _ point2: MKMapPoint) -> Bool
```

## Parameters

- `point1` — The first map point.

- `point2` — The second point.

## Return Value

[true](../swift/true.md) if the `x` and `y` values in both points are exactly the same, or [false](../swift/false.md) if one or both values are different.
