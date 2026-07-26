---
title: MKGeoJSONDecoder
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkgeojsondecoder
source_url: 'https://developer.apple.com/documentation/mapkit/mkgeojsondecoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkgeojsondecoder.json'
content_hash: 'sha256:180a7f22b5082082'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKGeoJSONDecoder

<sub>Class</sub>

An object that decodes GeoJSON objects into MapKit types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKGeoJSONDecoder
```

## Overview

The GeoJSON decoder returns objects that conform to the [MKGeoJSONObject](mkgeojsonobject.md) protocol.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Decoding GeoJSON objects

- [- geoJSONObjectsWithData:error:](<mkgeojsondecoder/decode(__).md>) — Decodes the provided data into native MapKit types that a map can display.

## See Also

### Geographical features

- [Displaying an Indoor Map](displaying-an-indoor-map.md) — Use the Indoor Mapping Data Format (IMDF) to show an indoor map with custom overlays and points of interest.
- [MKGeoJSONFeature](mkgeojsonfeature.md) — The decoded representation of a GeoJSON feature.
- [MKGeoJSONObject](mkgeojsonobject.md) — Objects that the GeoJSON decoder can return.
