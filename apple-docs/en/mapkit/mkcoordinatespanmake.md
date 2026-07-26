---
title: MKCoordinateSpanMake
framework: MapKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkcoordinatespanmake
source_url: 'https://developer.apple.com/documentation/mapkit/mkcoordinatespanmake'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkcoordinatespanmake.json'
content_hash: 'sha256:e1d09e0e4e023ea7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKCoordinateSpanMake

<sub>Function</sub>

Creates a new [MKCoordinateSpan](mkcoordinatespan.md) from the specified values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
static MKCoordinateSpan MKCoordinateSpanMake(CLLocationDegrees latitudeDelta, CLLocationDegrees longitudeDelta);
```

## Parameters

- `latitudeDelta` — The amount of north-to-south distance (measured in degrees) to use for the span. Unlike longitudinal distances, which vary based on the latitude, one degree of latitude is approximately 111 kilometers (69 miles) at all times.

- `longitudeDelta` — The amount of east-to-west distance (measured in degrees) to use for the span. The number of kilometers spanned by a longitude range varies based on the current latitude. For example, one degree of longitude spans a distance of approximately 111 kilometers (69 miles) at the equator but shrinks to 0 kilometers at the poles.

## Return Value

A span with the specified delta values.

## See Also

### Functions

- [MKCoordinateRegionMake](mkcoordinateregionmake.md) — Creates a new coordinate region from the specified coordinate and span values.
- [MKCoordinateRegionMakeWithDistance](<mkcoordinateregion/init(center_latitudinalmeters_longitudinalmeters_).md>) — Creates a new coordinate region from the specified coordinate and distance values.
- [MKMapPointForCoordinate](<mkmappoint/init(__).md>) — Creates the map point data structure that corresponds to the specified coordinate.
- [MKMapPointMake](mkmappointmake.md) — Creates a new map point structure from the specified values.
- [MKMapSizeMake](mkmapsizemake.md) — Creates a new map size structure from the specified values.
