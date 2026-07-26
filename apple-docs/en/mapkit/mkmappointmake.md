---
title: MKMapPointMake
framework: MapKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmappointmake
source_url: 'https://developer.apple.com/documentation/mapkit/mkmappointmake'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmappointmake.json'
content_hash: 'sha256:790034efc9fd4763'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMapPointMake

<sub>Function</sub>

Creates a new map point structure from the specified values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
static MKMapPoint MKMapPointMake(double x, double y);
```

## Parameters

- `x` — The point along the east-west axis of the map projection.

- `y` — The point along the north-south axis of the map projection.

## Return Value

A map point with the specified values.

## See Also

### Functions

- [MKCoordinateRegionMake](mkcoordinateregionmake.md) — Creates a new coordinate region from the specified coordinate and span values.
- [MKCoordinateRegionMakeWithDistance](<mkcoordinateregion/init(center_latitudinalmeters_longitudinalmeters_).md>) — Creates a new coordinate region from the specified coordinate and distance values.
- [MKCoordinateSpanMake](mkcoordinatespanmake.md) — Creates a new [MKCoordinateSpan](mkcoordinatespan.md) from the specified values.
- [MKMapPointForCoordinate](<mkmappoint/init(__).md>) — Creates the map point data structure that corresponds to the specified coordinate.
- [MKMapSizeMake](mkmapsizemake.md) — Creates a new map size structure from the specified values.
