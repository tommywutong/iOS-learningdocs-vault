---
title: MapStyle.Elevation
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapstyle/elevation
source_url: 'https://developer.apple.com/documentation/mapkit/mapstyle/elevation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapstyle/elevation.json'
content_hash: 'sha256:97eb7b2f71615329'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapStyle](../mapstyle.md)

# MapStyle.Elevation

<sub>Structure</sub>

Values you use to determine whether a map renders elevation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Elevation
```

## Topics

### Elevation styles

- [automatic](elevation/automatic.md) — The default elevation style, that renders a flat, 2D map.
- [flat](elevation/flat.md) — A value that renders a flat, 2D map.
- [realistic](elevation/realistic.md) — A value that renders a realistic, 3D map.

## See Also

### Creating map styles

- [hybrid(elevation:pointsOfInterest:showsTraffic:)](<hybrid(elevation_pointsofinterest_showstraffic_).md>) — Creates a hybrid map style that includes the elevation, point of interest, and traffic characteristics you specify.
- [imagery(elevation:)](<imagery(elevation_).md>) — Creates a map style based on satellite imagery with the elevation characteristics you specify.
- [standard(elevation:emphasis:pointsOfInterest:showsTraffic:)](<standard(elevation_emphasis_pointsofinterest_showstraffic_).md>) — Creates a standard map style that includes the elevation, point of interest, and traffic characteristics you specify.
- [StandardEmphasis](standardemphasis.md) — Values that control how the framework emphasizes map features.
