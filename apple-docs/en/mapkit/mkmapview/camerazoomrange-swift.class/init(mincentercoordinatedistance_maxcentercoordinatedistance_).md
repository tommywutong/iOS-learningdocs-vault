---
title: 'init(minCenterCoordinateDistance:maxCenterCoordinateDistance:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/camerazoomrange-swift.class/init(mincentercoordinatedistance:maxcentercoordinatedistance:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/camerazoomrange-swift.class/init(mincentercoordinatedistance:maxcentercoordinatedistance:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/camerazoomrange-swift.class/init%28mincentercoordinatedistance%3Amaxcentercoordinatedistance%3A%29.json'
content_hash: 'sha256:707ef7bd6e76789a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKMapView](../../mkmapview.md) · [CameraZoomRange](../camerazoomrange-swift.class.md)

# init(minCenterCoordinateDistance:maxCenterCoordinateDistance:)

<sub>Initializer</sub>

Create a camera zoom range by specifying a minimum and maximum distance from your map view’s center coordinates, measured in meters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init?(minCenterCoordinateDistance minDistance: CLLocationDistance, maxCenterCoordinateDistance maxDistance: CLLocationDistance)
```

## Parameters

- `minDistance` — The minimum distance the user can zoom in on a map based on its center point, measured in meters. To increase how far in the user can zoom, use a shorter distance value. To decrease how far in the user can zoom, use a larger distance value.

- `maxDistance` — The maximum distance the user can zoom out on a map based on its center point, measured in meters. To increase how far out the user can zoom, use a larger distance value. To decrease how far out the user can zoom, use a smaller distance value.

## Discussion

Specify the camera zoom range by providing the minimum and maximum distance values, in meters, from the center coordinate to constrain your map view’s zoom range.

To specify MapKit’s default minimum or maximum center coordinate distance, use the [MKMapCameraZoomDefault](../../mkmapcamerazoomdefault.md) constant, that allows the user to zoom to any level that MapKit supports.

The following example creates a zoom range that allows the map to zoom from 1000 – 3000 meters:

```swift
MKMapView.CameraZoomRange(
    minCenterCoordinateDistance: 1000,
    maxCenterCoordinateDistance: 3000
)
```

## See Also

### Creating a camera zoom range

- [- initWithMinCenterCoordinateDistance:](<init(mincentercoordinatedistance_).md>) — Create a camera zoom range by specifying the minimum distance from your map view’s center coordinate, measured in meters.
- [- initWithMaxCenterCoordinateDistance:](<init(maxcentercoordinatedistance_).md>) — Create a camera zoom range by specifying the maximum distance from your map view’s center coordinate, measured in meters.
- [MKMapCameraZoomDefault](../../mkmapcamerazoomdefault.md) — A constant value used to represent the default value for zooming in or out on a map.
