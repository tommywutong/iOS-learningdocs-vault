---
title: 'init(minCenterCoordinateDistance:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/camerazoomrange-swift.class/init(mincentercoordinatedistance:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/camerazoomrange-swift.class/init(mincentercoordinatedistance:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/camerazoomrange-swift.class/init%28mincentercoordinatedistance%3A%29.json'
content_hash: 'sha256:3aadd9fac774c86e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKMapView](../../mkmapview.md) · [CameraZoomRange](../camerazoomrange-swift.class.md)

# init(minCenterCoordinateDistance:)

<sub>Initializer</sub>

Create a camera zoom range by specifying the minimum distance from your map view’s center coordinate, measured in meters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init?(minCenterCoordinateDistance minDistance: CLLocationDistance)
```

## Parameters

- `minDistance` — The minimum distance the user can zoom in on a map based on its center point, measured in meters. To increase how far in the user can zoom, use a shorter distance value. To decrease how far in the user can zoom, use a larger distance value.

## Discussion

To specify MapKit’s default minimum distance from the center coordinate, use the [MKMapCameraZoomDefault](../../mkmapcamerazoomdefault.md) constant, that allows the user to zoom to any level that MapKit supports.

The following example prevents the user from zooming closer than 1000 meters from the map’s center coordinate:

```swift
MKMapView.CameraZoomRange(
    minCenterCoordinateDistance: 1000
)
```

## See Also

### Creating a camera zoom range

- [- initWithMinCenterCoordinateDistance:maxCenterCoordinateDistance:](<init(mincentercoordinatedistance_maxcentercoordinatedistance_).md>) — Create a camera zoom range by specifying a minimum and maximum distance from your map view’s center coordinates, measured in meters.
- [- initWithMaxCenterCoordinateDistance:](<init(maxcentercoordinatedistance_).md>) — Create a camera zoom range by specifying the maximum distance from your map view’s center coordinate, measured in meters.
- [MKMapCameraZoomDefault](../../mkmapcamerazoomdefault.md) — A constant value used to represent the default value for zooming in or out on a map.
