---
title: 'init(center:latitudinalMeters:longitudinalMeters:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS 9.2+, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkcoordinateregion/init(center:latitudinalmeters:longitudinalmeters:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkcoordinateregion/init(center:latitudinalmeters:longitudinalmeters:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkcoordinateregion/init%28center%3Alatitudinalmeters%3Alongitudinalmeters%3A%29.json'
content_hash: 'sha256:da90e30b536820a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKCoordinateRegion](../mkcoordinateregion.md)

# init(center:latitudinalMeters:longitudinalMeters:)

<sub>Initializer</sub>

Creates a new coordinate region from the specified coordinate and distance values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(center centerCoordinate: CLLocationCoordinate2D, latitudinalMeters: CLLocationDistance, longitudinalMeters: CLLocationDistance)
```

## Parameters

- `centerCoordinate` — The center point of the new coordinate region.

- `latitudinalMeters` — The north-to-south span of the region (measured in meters) specified as the distance from the center point to the bounds along the north-to-south axis.

- `longitudinalMeters` — The east-to-west span of the region (measured in meters) specified as the distance from the center point to the bounds along the east-to-west axis.

## Return Value

A region with the specified values.

## See Also

### Creating a region

- [init()](<init().md>) — Creates a coordinate region.
- [MKCoordinateRegionForMapRect](<init(__).md>) — Returns the region that corresponds to the specified map rectangle.
- [init(center:span:)](<init(center_span_).md>) — Creates a coordinate region with a span around the specified center coordinate.
