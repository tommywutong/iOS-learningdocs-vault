---
title: MapStyle
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapstyle
source_url: 'https://developer.apple.com/documentation/mapkit/mapstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapstyle.json'
content_hash: 'sha256:db4ad40032bcc211'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapStyle

<sub>Structure</sub>

A style that you can apply to a map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MapStyle
```

## Topics

### Creating map styles

- [hybrid(elevation:pointsOfInterest:showsTraffic:)](<mapstyle/hybrid(elevation_pointsofinterest_showstraffic_).md>) — Creates a hybrid map style that includes the elevation, point of interest, and traffic characteristics you specify.
- [imagery(elevation:)](<mapstyle/imagery(elevation_).md>) — Creates a map style based on satellite imagery with the elevation characteristics you specify.
- [standard(elevation:emphasis:pointsOfInterest:showsTraffic:)](<mapstyle/standard(elevation_emphasis_pointsofinterest_showstraffic_).md>) — Creates a standard map style that includes the elevation, point of interest, and traffic characteristics you specify.
- [Elevation](mapstyle/elevation.md) — Values you use to determine whether a map renders elevation.
- [StandardEmphasis](mapstyle/standardemphasis.md) — Values that control how the framework emphasizes map features.

### Map styles

- [hybrid](mapstyle/hybrid.md) — A map style that represents a satellite image of the area, including the paths of roads with their names layered on top.
- [imagery](mapstyle/imagery.md) — A map style that represents a satellite image of the area the map displays.
- [standard](mapstyle/standard.md) — A map style that represents the default map presentation, which is a street map that shows the position of all roads and some road names, depending upon the zoom level of the map.

## See Also

### Essentials

- [Map](map.md) — A view that displays an embedded map interface.
