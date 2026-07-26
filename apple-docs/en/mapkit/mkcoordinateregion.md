---
title: MKCoordinateRegion
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkcoordinateregion
source_url: 'https://developer.apple.com/documentation/mapkit/mkcoordinateregion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkcoordinateregion.json'
content_hash: 'sha256:3755840c2b20e77e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKCoordinateRegion

<sub>Structure</sub>

A rectangular geographic region that centers around a specific latitude and longitude.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MKCoordinateRegion
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a region

- [init()](<mkcoordinateregion/init().md>) — Creates a coordinate region.
- [MKCoordinateRegionMakeWithDistance](<mkcoordinateregion/init(center_latitudinalmeters_longitudinalmeters_).md>) — Creates a new coordinate region from the specified coordinate and distance values.
- [MKCoordinateRegionForMapRect](<mkcoordinateregion/init(__).md>) — Returns the region that corresponds to the specified map rectangle.
- [init(center:span:)](<mkcoordinateregion/init(center_span_).md>) — Creates a coordinate region with a span around the specified center coordinate.

### Getting the region coordinates

- [center](mkcoordinateregion/center.md) — The center point of the region.
- [span](mkcoordinateregion/span.md) — The horizontal and vertical span representing the amount of map to display.

## See Also

### Map coordinates

- [MKCoordinateSpan](mkcoordinatespan.md) — The width and height of a map region.
- [MKMapRect](mkmaprect.md) — A rectangular area on a two-dimensional map projection.
- [MKMapPoint](mkmappoint.md) — A point on a two-dimensional map projection.
- [MKMapSize](mkmapsize.md) — Width and height information on a two-dimensional map projection.
- [MKDistanceFormatter](mkdistanceformatter.md) — A utility object that converts between a geographic distance and a string-based expression of that distance.
