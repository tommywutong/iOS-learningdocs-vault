---
title: 'imagery(elevation:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapstyle/imagery(elevation:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapstyle/imagery(elevation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapstyle/imagery%28elevation%3A%29.json'
content_hash: 'sha256:5c3cbfaf119a379b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapStyle](../mapstyle.md)

# imagery(elevation:)

<sub>Type Method</sub>

Creates a map style based on satellite imagery with the elevation characteristics you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func imagery(elevation: MapStyle.Elevation = .automatic) -> MapStyle
```

## Parameters

- `elevation` — One of the [Elevation](elevation.md) values that determines how the map renders elevation.

## Return Value

A [MapStyle](../mapstyle.md) with the elevation style you specified.

## Discussion

> [!note] Note
> In watchOS, depending on rendering calculations, MapKit may render the map using the Standard map style rather than requested Hybrid or Imagery styles.

## See Also

### Creating map styles

- [hybrid(elevation:pointsOfInterest:showsTraffic:)](<hybrid(elevation_pointsofinterest_showstraffic_).md>) — Creates a hybrid map style that includes the elevation, point of interest, and traffic characteristics you specify.
- [standard(elevation:emphasis:pointsOfInterest:showsTraffic:)](<standard(elevation_emphasis_pointsofinterest_showstraffic_).md>) — Creates a standard map style that includes the elevation, point of interest, and traffic characteristics you specify.
- [Elevation](elevation.md) — Values you use to determine whether a map renders elevation.
- [StandardEmphasis](standardemphasis.md) — Values that control how the framework emphasizes map features.
