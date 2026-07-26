---
title: geometry
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkgeojsonfeature/geometry
source_url: 'https://developer.apple.com/documentation/mapkit/mkgeojsonfeature/geometry'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkgeojsonfeature/geometry.json'
content_hash: 'sha256:91c9c1be88f9311c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKGeoJSONFeature](../mkgeojsonfeature.md)

# geometry

<sub>Instance Property</sub>

The shape or shapes associated with the GeoJSON feature.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var geometry: [any MKShape & MKGeoJSONObject] { get }
```

## See Also

### Feature properties

- [identifier](identifier.md) — An optional identifier the class returns as a string.
- [properties](properties.md) — Optional serialized JSON data that corresponds to the properties key.
