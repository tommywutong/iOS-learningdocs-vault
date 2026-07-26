---
title: MKGeoJSONFeature
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkgeojsonfeature
source_url: 'https://developer.apple.com/documentation/mapkit/mkgeojsonfeature'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkgeojsonfeature.json'
content_hash: 'sha256:7bc15239bb6f7901'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKGeoJSONFeature

<sub>Class</sub>

The decoded representation of a GeoJSON feature.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKGeoJSONFeature
```

## Overview

A feature is an object with associated geometry and optional properties in JSON that you define. MapKit exposes these optional properties, but treats them as opaque. [MKGeoJSONFeature](mkgeojsonfeature.md) is one of the classes that the GeoJSON decoder ([MKGeoJSONDecoder](mkgeojsondecoder.md)) can return.

See the GeoJSON standards specification [RFC 7946](https://tools.ietf.org/html/rfc7946#section-3.2) for more information about `Feature` objects.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [MKGeoJSONObject](mkgeojsonobject.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Feature properties

- [geometry](mkgeojsonfeature/geometry.md) — The shape or shapes associated with the GeoJSON feature.
- [identifier](mkgeojsonfeature/identifier.md) — An optional identifier the class returns as a string.
- [properties](mkgeojsonfeature/properties.md) — Optional serialized JSON data that corresponds to the properties key.

## See Also

### Geographical features

- [Displaying an Indoor Map](displaying-an-indoor-map.md) — Use the Indoor Mapping Data Format (IMDF) to show an indoor map with custom overlays and points of interest.
- [MKGeoJSONDecoder](mkgeojsondecoder.md) — An object that decodes GeoJSON objects into MapKit types.
- [MKGeoJSONObject](mkgeojsonobject.md) — Objects that the GeoJSON decoder can return.
