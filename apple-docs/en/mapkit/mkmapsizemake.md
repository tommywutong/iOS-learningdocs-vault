---
title: MKMapSizeMake
framework: MapKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapsizemake
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapsizemake'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapsizemake.json'
content_hash: 'sha256:ed74131222ee1920'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMapSizeMake

<sub>Function</sub>

Creates a new map size structure from the specified values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
static MKMapSize MKMapSizeMake(double width, double height);
```

## Parameters

- `width` — The distance (measured using map points) along the east-west axis of the map projection.

- `height` — The distance (measured using map points) along the north-south axis of the map projection.

## Return Value

A map size with the specified values.

## See Also

### Functions

- [MKCoordinateRegionMake](mkcoordinateregionmake.md) — Creates a new coordinate region from the specified coordinate and span values.
- [MKCoordinateRegionMakeWithDistance](<mkcoordinateregion/init(center_latitudinalmeters_longitudinalmeters_).md>) — Creates a new coordinate region from the specified coordinate and distance values.
- [MKCoordinateSpanMake](mkcoordinatespanmake.md) — Creates a new [MKCoordinateSpan](mkcoordinatespan.md) from the specified values.
- [MKMapPointForCoordinate](<mkmappoint/init(__).md>) — Creates the map point data structure that corresponds to the specified coordinate.
- [MKMapPointMake](mkmappointmake.md) — Creates a new map point structure from the specified values.
