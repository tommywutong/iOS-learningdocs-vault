---
title: MKCircle
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkcircle
source_url: 'https://developer.apple.com/documentation/mapkit/mkcircle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkcircle.json'
content_hash: 'sha256:58a832d7dfc8c2db'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKCircle

<sub>Class</sub>

A circular overlay with a configurable radius that you center on a geographic coordinate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKCircle
```

## Overview

This class defines the portion of the map that the overlay covers. To draw the region, return an [MKCircleRenderer](mkcirclerenderer.md) object from the [- mapView:rendererForOverlay:](<mkmapviewdelegate/mapview(__rendererfor_).md>) method of your map view delegate.

## Relationships

- **Inherits From**: [MKShape](mkshape.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [MKAnnotation](mkannotation.md), [MKOverlay](mkoverlay.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a circle overlay

- [+ circleWithCenterCoordinate:radius:](<mkcircle/init(center_radius_).md>) — Creates and returns a circle object using the specified coordinate and radius.
- [+ circleWithMapRect:](<mkcircle/init(maprect_).md>) — Creates and returns a circle object that derives the circular area from the specified rectangle.

### Accessing the overlay’s attributes

- [coordinate](mkcircle/coordinate.md) — The center point of the circular area, specified as a latitude and longitude.
- [radius](mkcircle/radius.md) — The radius of the circular area, in meters.
- [boundingMapRect](mkcircle/boundingmaprect.md) — The bounding rectangle of the circular area.

### Initializers

- [init(centerCoordinate:radius:)](<mkcircle/init(centercoordinate_radius_).md>)

## See Also

### Circular overlays

- [MKCircleRenderer](mkcirclerenderer.md) — The visual representation of a circular overlay.
