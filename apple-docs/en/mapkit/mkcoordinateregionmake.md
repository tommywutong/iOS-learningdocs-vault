---
title: MKCoordinateRegionMake
framework: MapKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkcoordinateregionmake
source_url: 'https://developer.apple.com/documentation/mapkit/mkcoordinateregionmake'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkcoordinateregionmake.json'
content_hash: 'sha256:05a87c9b08f3656e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKCoordinateRegionMake

<sub>Function</sub>

Creates a new coordinate region from the specified coordinate and span values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
static MKCoordinateRegion MKCoordinateRegionMake(CLLocationCoordinate2D centerCoordinate, MKCoordinateSpan span);
```

## Parameters

- `centerCoordinate` — The center point of the region.

- `span` — The horizontal and vertical span representing the amount of map to display. The size of the span also reflects the current zoom level.

## Return Value

A region with the specified values.

## See Also

### Functions

- [MKCoordinateRegionMakeWithDistance](<mkcoordinateregion/init(center_latitudinalmeters_longitudinalmeters_).md>) — Creates a new coordinate region from the specified coordinate and distance values.
- [MKCoordinateSpanMake](mkcoordinatespanmake.md) — Creates a new [MKCoordinateSpan](mkcoordinatespan.md) from the specified values.
- [MKMapPointForCoordinate](<mkmappoint/init(__).md>) — Creates the map point data structure that corresponds to the specified coordinate.
- [MKMapPointMake](mkmappointmake.md) — Creates a new map point structure from the specified values.
- [MKMapSizeMake](mkmapsizemake.md) — Creates a new map size structure from the specified values.
