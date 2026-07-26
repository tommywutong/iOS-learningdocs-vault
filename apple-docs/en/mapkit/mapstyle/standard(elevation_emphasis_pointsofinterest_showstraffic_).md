---
title: 'standard(elevation:emphasis:pointsOfInterest:showsTraffic:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapstyle/standard(elevation:emphasis:pointsofinterest:showstraffic:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapstyle/standard(elevation:emphasis:pointsofinterest:showstraffic:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapstyle/standard%28elevation%3Aemphasis%3Apointsofinterest%3Ashowstraffic%3A%29.json'
content_hash: 'sha256:9cb2ef1e8ddf1d73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapStyle](../mapstyle.md)

# standard(elevation:emphasis:pointsOfInterest:showsTraffic:)

<sub>Type Method</sub>

Creates a standard map style that includes the elevation, point of interest, and traffic characteristics you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func standard(elevation: MapStyle.Elevation = .automatic, emphasis: MapStyle.StandardEmphasis = .automatic, pointsOfInterest: PointOfInterestCategories = .all, showsTraffic: Bool = false) -> MapStyle
```

## Parameters

- `elevation` — One of the [Elevation](elevation.md) values that determines whether the framework renders map elevation.

- `emphasis` — One of the [StandardEmphasis](standardemphasis.md) values that controls how the framework emphasizes map features.

- `pointsOfInterest` — A collection of [PointOfInterestCategories](../pointofinterestcategories.md) displayed on the map.

- `showsTraffic` — A Boolean value that indicates whether the map displays traffic.

## Return Value

A [MapStyle](../mapstyle.md) with the configuration you specified.

## See Also

### Creating map styles

- [hybrid(elevation:pointsOfInterest:showsTraffic:)](<hybrid(elevation_pointsofinterest_showstraffic_).md>) — Creates a hybrid map style that includes the elevation, point of interest, and traffic characteristics you specify.
- [imagery(elevation:)](<imagery(elevation_).md>) — Creates a map style based on satellite imagery with the elevation characteristics you specify.
- [Elevation](elevation.md) — Values you use to determine whether a map renders elevation.
- [StandardEmphasis](standardemphasis.md) — Values that control how the framework emphasizes map features.
