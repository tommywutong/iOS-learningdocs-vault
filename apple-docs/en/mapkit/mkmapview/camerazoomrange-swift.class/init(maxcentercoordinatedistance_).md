---
title: 'init(maxCenterCoordinateDistance:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/camerazoomrange-swift.class/init(maxcentercoordinatedistance:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/camerazoomrange-swift.class/init(maxcentercoordinatedistance:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/camerazoomrange-swift.class/init%28maxcentercoordinatedistance%3A%29.json'
content_hash: 'sha256:31c6c239dc245e02'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKMapView](../../mkmapview.md) · [CameraZoomRange](../camerazoomrange-swift.class.md)

# init(maxCenterCoordinateDistance:)

<sub>Initializer</sub>

Create a camera zoom range by specifying the maximum distance from your map view’s center coordinate, measured in meters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init?(maxCenterCoordinateDistance maxDistance: CLLocationDistance)
```

## Parameters

- `maxDistance` — The maximum distance the user can zoom out on a map based on its center point, measured in meters. To increase how far out the user can zoom, use a larger distance value. To decrease how far out the user can zoom, use a smaller distance value.

## Discussion

The constant, [MKMapCameraZoomDefault](../../mkmapcamerazoomdefault.md), specifies the default distance for [maxCenterCoordinateDistance](maxcentercoordinatedistance.md).

## See Also

### Creating a camera zoom range

- [- initWithMinCenterCoordinateDistance:maxCenterCoordinateDistance:](<init(mincentercoordinatedistance_maxcentercoordinatedistance_).md>) — Create a camera zoom range by specifying a minimum and maximum distance from your map view’s center coordinates, measured in meters.
- [- initWithMinCenterCoordinateDistance:](<init(mincentercoordinatedistance_).md>) — Create a camera zoom range by specifying the minimum distance from your map view’s center coordinate, measured in meters.
- [MKMapCameraZoomDefault](../../mkmapcamerazoomdefault.md) — A constant value used to represent the default value for zooming in or out on a map.
