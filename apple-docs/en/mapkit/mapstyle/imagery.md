---
title: imagery
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapstyle/imagery
source_url: 'https://developer.apple.com/documentation/mapkit/mapstyle/imagery'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapstyle/imagery.json'
content_hash: 'sha256:cbee9043a4686bb5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapStyle](../mapstyle.md)

# imagery

<sub>Type Property</sub>

A map style that represents a satellite image of the area the map displays.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var imagery: MapStyle { get }
```

## Discussion

> [!note] Note
> In watchOS, depending on rendering calculations, MapKit may render the map using the Standard map style rather than requested Hybrid or Imagery styles.

## See Also

### Map styles

- [hybrid](hybrid.md) — A map style that represents a satellite image of the area, including the paths of roads with their names layered on top.
- [standard](standard.md) — A map style that represents the default map presentation, which is a street map that shows the position of all roads and some road names, depending upon the zoom level of the map.
