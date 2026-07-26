---
title: MapPolygon
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mappolygon
source_url: 'https://developer.apple.com/documentation/mapkit/mappolygon'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mappolygon.json'
content_hash: 'sha256:ccacb3fd0d583f63'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapPolygon

<sub>Structure</sub>

A closed polygon overlay.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MapPolygon
```

## Overview

Use this view to create map polygons instances in the closure you provide to the `content` parameter in the [Map](map.md) initializers.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [MapContent](mapcontent.md)

## Topics

### Creating a map polygon

- [init(coordinates:)](<mappolygon/init(coordinates_).md>) — Creates a polygon from a list of coordinates you provide.
- [init(points:)](<mappolygon/init(points_).md>) — Creates a polygon from a list of map points.
- [init(_:)](<mappolygon/init(__).md>) — Creates a polygon from the polygon you provide.

## See Also

### Annotations and overlays

- [Annotation](annotation.md) — A customizable annotation used to indicate a location on a map.
- [MapCircle](mapcircle.md) — A circular overlay with a configurable radius that you center on a geographic coordinate.
- [MapPolyline](mappolyline.md) — An open polygon overlay consisting of one or more connected line segments.
- [Marker](marker.md) — A balloon-shaped annotation that marks a map location.
- [UserAnnotation](userannotation.md) — Displays the person’s current location on the map.
