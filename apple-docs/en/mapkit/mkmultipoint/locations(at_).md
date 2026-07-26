---
title: 'locations(at:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmultipoint/locations(at:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmultipoint/locations(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmultipoint/locations%28at%3A%29.json'
content_hash: 'sha256:94be8d648b30003f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMultiPoint](../mkmultipoint.md)

# locations(at:)

<sub>Instance Method</sub>

Translates a point index set into a unit distance along the shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func locations(at indexes: IndexSet) -> [CGFloat]
```

## Parameters

- `indexes` — The index set of map points associated with the shape.

## Return Value

An array of [CGFloat](../../corefoundation/cgfloat-swift.struct.md) values.

## See Also

### Accessing the points in the shape

- [- points](<points().md>) — Returns an array of map points associated with the shape.
- [pointCount](pointcount.md) — The number of points associated with the shape.
- [- locationAtPointIndex:](<location(atpointindex_).md>) — Translates a point index into a unit distance along the shape.
