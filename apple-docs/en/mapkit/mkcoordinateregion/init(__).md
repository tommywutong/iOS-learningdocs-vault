---
title: 'init(_:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkcoordinateregion/init(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkcoordinateregion/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkcoordinateregion/init%28_%3A%29.json'
content_hash: 'sha256:cde13f4c725c5eff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKCoordinateRegion](../mkcoordinateregion.md)

# init(_:)

<sub>Initializer</sub>

Returns the region that corresponds to the specified map rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ rect: MKMapRect)
```

## Parameters

- `rect` — The map rectangle that corresponds to the desired region on a two-dimensional map projection.

## Return Value

The region structure specifying the latitude, longitude, and span values for the specified rectangle.

## See Also

### Creating a region

- [init()](<init().md>) — Creates a coordinate region.
- [MKCoordinateRegionMakeWithDistance](<init(center_latitudinalmeters_longitudinalmeters_).md>) — Creates a new coordinate region from the specified coordinate and distance values.
- [init(center:span:)](<init(center_span_).md>) — Creates a coordinate region with a span around the specified center coordinate.
