---
title: 'location(atPointIndex:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmultipoint/location(atpointindex:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmultipoint/location(atpointindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmultipoint/location%28atpointindex%3A%29.json'
content_hash: 'sha256:54b32a820ad893b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMultiPoint](../mkmultipoint.md)

# location(atPointIndex:)

<sub>Instance Method</sub>

Translates a point index into a unit distance along the shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func location(atPointIndex index: Int) -> CGFloat
```

## Parameters

- `index` — The index of the map point associated with the shape.

## Return Value

A [CGFloat](../../corefoundation/cgfloat-swift.struct.md) value that indicates the unit distance along the shape.

## See Also

### Accessing the points in the shape

- [- points](<points().md>) — Returns an array of map points associated with the shape.
- [pointCount](pointcount.md) — The number of points associated with the shape.
- [locations(at:)](<locations(at_).md>) — Translates a point index set into a unit distance along the shape.
