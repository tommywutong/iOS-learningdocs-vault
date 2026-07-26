---
title: 'hybrid(elevation:pointsOfInterest:showsTraffic:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapstyle/hybrid(elevation:pointsofinterest:showstraffic:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapstyle/hybrid(elevation:pointsofinterest:showstraffic:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapstyle/hybrid%28elevation%3Apointsofinterest%3Ashowstraffic%3A%29.json'
content_hash: 'sha256:441af09fea3fcd1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapStyle](../mapstyle.md)

# hybrid(elevation:pointsOfInterest:showsTraffic:)

<sub>Type Method</sub>

Creates a hybrid map style that includes the elevation, point of interest, and traffic characteristics you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func hybrid(elevation: MapStyle.Elevation = .automatic, pointsOfInterest: PointOfInterestCategories = .all, showsTraffic: Bool = false) -> MapStyle
```

## Parameters

- `elevation` — One of the [Elevation](elevation.md) values that determines whether the map renders elevation.

- `pointsOfInterest` — A collection of [PointOfInterestCategories](../pointofinterestcategories.md) that the map displays.

- `showsTraffic` — A Boolean value that indicates whether the map displays traffic.

## Return Value

A [MapStyle](../mapstyle.md) with the configuration you specified.

## Discussion

> [!note] Note
> In watchOS, depending on rendering calculations, MapKit may render the map using the Standard map style rather than requested Hybrid or Imagery styles.

## See Also

### Creating map styles

- [imagery(elevation:)](<imagery(elevation_).md>) — Creates a map style based on satellite imagery with the elevation characteristics you specify.
- [standard(elevation:emphasis:pointsOfInterest:showsTraffic:)](<standard(elevation_emphasis_pointsofinterest_showstraffic_).md>) — Creates a standard map style that includes the elevation, point of interest, and traffic characteristics you specify.
- [Elevation](elevation.md) — Values you use to determine whether a map renders elevation.
- [StandardEmphasis](standardemphasis.md) — Values that control how the framework emphasizes map features.
