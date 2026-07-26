---
title: 'init(center:span:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkcoordinateregion/init(center:span:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkcoordinateregion/init(center:span:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkcoordinateregion/init%28center%3Aspan%3A%29.json'
content_hash: 'sha256:acbe39e48d7350ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKCoordinateRegion](../mkcoordinateregion.md)

# init(center:span:)

<sub>Initializer</sub>

Creates a coordinate region with a span around the specified center coordinate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(center: CLLocationCoordinate2D, span: MKCoordinateSpan)
```

## Parameters

- `center` — The center of the coordinate region.

- `span` — The span around the center of the coordinate region.

## See Also

### Creating a region

- [init()](<init().md>) — Creates a coordinate region.
- [MKCoordinateRegionMakeWithDistance](<init(center_latitudinalmeters_longitudinalmeters_).md>) — Creates a new coordinate region from the specified coordinate and distance values.
- [MKCoordinateRegionForMapRect](<init(__).md>) — Returns the region that corresponds to the specified map rectangle.
