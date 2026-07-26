---
title: identifier
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkgeojsonfeature/identifier
source_url: 'https://developer.apple.com/documentation/mapkit/mkgeojsonfeature/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkgeojsonfeature/identifier.json'
content_hash: 'sha256:0b293799998ea134'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKGeoJSONFeature](../mkgeojsonfeature.md)

# identifier

<sub>Instance Property</sub>

An optional identifier the class returns as a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var identifier: String? { get }
```

## Discussion

Note that the GeoJSON specification states that the identifier can be a number or a string. However, this [identifier](identifier.md) returns as a string.

## See Also

### Feature properties

- [geometry](geometry.md) — The shape or shapes associated with the GeoJSON feature.
- [properties](properties.md) — Optional serialized JSON data that corresponds to the properties key.
