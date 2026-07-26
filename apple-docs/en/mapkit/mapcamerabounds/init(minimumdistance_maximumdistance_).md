---
title: 'init(minimumDistance:maximumDistance:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapcamerabounds/init(minimumdistance:maximumdistance:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapcamerabounds/init(minimumdistance:maximumdistance:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcamerabounds/init%28minimumdistance%3Amaximumdistance%3A%29.json'
content_hash: 'sha256:6d33e11811a6722e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapCameraBounds](../mapcamerabounds.md)

# init(minimumDistance:maximumDistance:)

<sub>Initializer</sub>

Creates a camera bounds with the zoom ranges you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(minimumDistance: Double? = nil, maximumDistance: Double? = nil)
```

## Parameters

- `minimumDistance` — The minimum distance someone can zoom in on a map based on its center point, measured in meters.

- `maximumDistance` — The maximum distance someone can zoom out on a map based on its center point, measured in meters.

## See Also

### Creating a map camera bounds

- [init(centerCoordinateBounds:minimumDistance:maximumDistance:)](<init(centercoordinatebounds_minimumdistance_maximumdistance_)-97kis.md>) — Creates a camera bounds with the specified region boundary and zoom ranges.
- [init(centerCoordinateBounds:minimumDistance:maximumDistance:)](<init(centercoordinatebounds_minimumdistance_maximumdistance_)-27z4p.md>) — Creates a camera bounds with the specified map rectangle boundary and zoom ranges.
