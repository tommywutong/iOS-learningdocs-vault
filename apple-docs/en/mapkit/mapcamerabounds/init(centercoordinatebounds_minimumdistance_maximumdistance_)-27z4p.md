---
title: 'init(centerCoordinateBounds:minimumDistance:maximumDistance:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapcamerabounds/init(centercoordinatebounds:minimumdistance:maximumdistance:)-27z4p'
source_url: 'https://developer.apple.com/documentation/mapkit/mapcamerabounds/init(centercoordinatebounds:minimumdistance:maximumdistance:)-27z4p'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcamerabounds/init%28centercoordinatebounds%3Aminimumdistance%3Amaximumdistance%3A%29-27z4p.json'
content_hash: 'sha256:793511a69a6b7c7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapCameraBounds](../mapcamerabounds.md)

# init(centerCoordinateBounds:minimumDistance:maximumDistance:)

<sub>Initializer</sub>

Creates a camera bounds with the specified map rectangle boundary and zoom ranges.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(centerCoordinateBounds: MKMapRect, minimumDistance: Double? = nil, maximumDistance: Double? = nil)
```

## Parameters

- `centerCoordinateBounds` — An [MKMapRect](../mkmaprect.md) that specifies a boundary of an area that the map’s center needs to remain in.

- `minimumDistance` — The minimum distance someone can zoom in on a map based on its center point, measured in meters.

- `maximumDistance` — The maximum distance the user can zoom out on a map based on its center point, measured in meters.

## See Also

### Creating a map camera bounds

- [init(centerCoordinateBounds:minimumDistance:maximumDistance:)](<init(centercoordinatebounds_minimumdistance_maximumdistance_)-97kis.md>) — Creates a camera bounds with the specified region boundary and zoom ranges.
- [init(minimumDistance:maximumDistance:)](<init(minimumdistance_maximumdistance_).md>) — Creates a camera bounds with the zoom ranges you specify.
