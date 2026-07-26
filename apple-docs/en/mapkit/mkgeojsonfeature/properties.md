---
title: properties
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkgeojsonfeature/properties
source_url: 'https://developer.apple.com/documentation/mapkit/mkgeojsonfeature/properties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkgeojsonfeature/properties.json'
content_hash: 'sha256:e02bed8428a01ccb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKGeoJSONFeature](../mkgeojsonfeature.md)

# properties

<sub>Instance Property</sub>

Optional serialized JSON data that corresponds to the properties key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var properties: Data? { get }
```

## Discussion

MapKit exposes these optional properties but treats them as opaque.

## See Also

### Feature properties

- [geometry](geometry.md) — The shape or shapes associated with the GeoJSON feature.
- [identifier](identifier.md) — An optional identifier the class returns as a string.
