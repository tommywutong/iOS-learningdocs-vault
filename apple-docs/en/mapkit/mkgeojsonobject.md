---
title: MKGeoJSONObject
framework: MapKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkgeojsonobject
source_url: 'https://developer.apple.com/documentation/mapkit/mkgeojsonobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkgeojsonobject.json'
content_hash: 'sha256:65002f99277cba79'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKGeoJSONObject

<sub>Protocol</sub>

Objects that the GeoJSON decoder can return.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol MKGeoJSONObject : NSObjectProtocol
```

## Overview

Classes that conform to this protocol represent the types that the GeoJSON decoder can return.

There’s no reason to create your own classes that conform to this protocol; only MapKit can define classes that the GeoJSON decoder uses.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [MKGeoJSONFeature](mkgeojsonfeature.md), [MKGeodesicPolyline](mkgeodesicpolyline.md), [MKMultiPoint](mkmultipoint.md), [MKMultiPolygon](mkmultipolygon.md), [MKMultiPolyline](mkmultipolyline.md), [MKPointAnnotation](mkpointannotation.md), [MKPolygon](mkpolygon.md), [MKPolyline](mkpolyline.md)

## See Also

### Geographical features

- [Displaying an Indoor Map](displaying-an-indoor-map.md) — Use the Indoor Mapping Data Format (IMDF) to show an indoor map with custom overlays and points of interest.
- [MKGeoJSONDecoder](mkgeojsondecoder.md) — An object that decodes GeoJSON objects into MapKit types.
- [MKGeoJSONFeature](mkgeojsonfeature.md) — The decoded representation of a GeoJSON feature.
