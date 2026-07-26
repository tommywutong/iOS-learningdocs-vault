---
title: MKMapItemAnnotation
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapitemannotation
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapitemannotation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapitemannotation.json'
content_hash: 'sha256:abcb1889858528bd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMapItemAnnotation

<sub>Class</sub>

An annotation that represents a map item

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MKMapItemAnnotation
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [MKAnnotation](mkannotation.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a map item annotation

- [- initWithMapItem:](<mkmapitemannotation/init(mapitem_).md>) — Creates a map item annotation

### Accessing the annotation’s map item

- [mapItem](mkmapitemannotation/mapitem.md) — The map item represented by this annotation

## See Also

### Location annotations

- [Annotating a Map with Custom Data](annotating-a-map-with-custom-data.md) — Annotate a map with location-specific data using default and customized annotation views and callouts.
- [MKPointAnnotation](mkpointannotation.md) — A string-based piece of location-specific data that you apply to a specific point on a map.
- [MKMarkerAnnotationView](mkmarkerannotationview.md) — An annotation view that displays a balloon-shaped marker at the designated location.
- [MKPinAnnotationView](mkpinannotationview.md) — An annotation view that displays a pin image on the map. _(deprecated)_
