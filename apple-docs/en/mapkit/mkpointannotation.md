---
title: MKPointAnnotation
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkpointannotation
source_url: 'https://developer.apple.com/documentation/mapkit/mkpointannotation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpointannotation.json'
content_hash: 'sha256:0ef5137fb83dc143'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKPointAnnotation

<sub>Class</sub>

A string-based piece of location-specific data that you apply to a specific point on a map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKPointAnnotation
```

## Overview

You use this class, rather than define a custom annotation object, in situations where all you want to do is display a title string at the specified point on the map.

## Relationships

- **Inherits From**: [MKShape](mkshape.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [MKAnnotation](mkannotation.md), [MKGeoJSONObject](mkgeojsonobject.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a Point Annotation

- [- init](<mkpointannotation/init().md>) — Creates a map annotation that shows a title string at a point on a map.
- [- initWithCoordinate:](<mkpointannotation/init(coordinate_).md>) — Creates a point annotation at the specified coordinate on the map.
- [- initWithCoordinate:title:subtitle:](<mkpointannotation/init(coordinate_title_subtitle_).md>) — Creates a point annotation displaying a title and subtitle string at the specified coordinate on the map.

### Accessing the Annotation’s Location

- [coordinate](mkpointannotation/coordinate.md) — The coordinate point of the annotation.

## See Also

### Location annotations

- [Annotating a Map with Custom Data](annotating-a-map-with-custom-data.md) — Annotate a map with location-specific data using default and customized annotation views and callouts.
- [MKMapItemAnnotation](mkmapitemannotation.md) — An annotation that represents a map item
- [MKMarkerAnnotationView](mkmarkerannotationview.md) — An annotation view that displays a balloon-shaped marker at the designated location.
- [MKPinAnnotationView](mkpinannotationview.md) — An annotation view that displays a pin image on the map. _(deprecated)_
