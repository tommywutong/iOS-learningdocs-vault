---
title: MapCircle
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapcircle
source_url: 'https://developer.apple.com/documentation/mapkit/mapcircle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcircle.json'
content_hash: 'sha256:df7b059ab700369c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapCircle

<sub>Structure</sub>

A circular overlay with a configurable radius that you center on a geographic coordinate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MapCircle
```

## Overview

Use this view to create circular overlays in the closure you provide to the `content` parameter in [Map](map.md) initializers.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [MapContent](mapcontent.md)

## Topics

### Creating a map circle

- [init(_:)](<mapcircle/init(__).md>) — Creates a circle overlay from an existing map circle object.
- [init(center:radius:)](<mapcircle/init(center_radius_).md>) — Creates a circle with the center coordinate and radius you specify.
- [init(mapRect:)](<mapcircle/init(maprect_).md>) — Creates the largest possible circle centered within the given map rectangle.

## See Also

### Annotations and overlays

- [Annotation](annotation.md) — A customizable annotation used to indicate a location on a map.
- [MapPolygon](mappolygon.md) — A closed polygon overlay.
- [MapPolyline](mappolyline.md) — An open polygon overlay consisting of one or more connected line segments.
- [Marker](marker.md) — A balloon-shaped annotation that marks a map location.
- [UserAnnotation](userannotation.md) — Displays the person’s current location on the map.
