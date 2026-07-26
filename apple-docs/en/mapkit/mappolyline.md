---
title: MapPolyline
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mappolyline
source_url: 'https://developer.apple.com/documentation/mapkit/mappolyline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mappolyline.json'
content_hash: 'sha256:d50807023378ebf4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapPolyline

<sub>Structure</sub>

An open polygon overlay consisting of one or more connected line segments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MapPolyline
```

## Overview

Use this view to create map polylines instances in the closure you provide to the `content` parameter in the [Map](map.md) initializers.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [MapContent](mapcontent.md)

## Topics

### Creating a polyline

- [init(_:)](<mappolyline/init(__)-93u7w.md>) — Creates a polyline from polyline you provide.
- [init(_:)](<mappolyline/init(__)-5p2kx.md>) — Creates a polyline that traces the route you provide.
- [init(coordinates:contourStyle:)](<mappolyline/init(coordinates_contourstyle_).md>) — Creates a polyline that traces a path between the given coordinates using the specifed contour style.
- [init(points:contourStyle:)](<mappolyline/init(points_contourstyle_).md>) — Creates a new polyline that traces a path between the provided points using the specifed contour style.

### Styling the polyline

- [ContourStyle](mappolyline/contourstyle.md) — Values that define how MapKit styles lines to represent the contour of the Earth.

## See Also

### Annotations and overlays

- [Annotation](annotation.md) — A customizable annotation used to indicate a location on a map.
- [MapCircle](mapcircle.md) — A circular overlay with a configurable radius that you center on a geographic coordinate.
- [MapPolygon](mappolygon.md) — A closed polygon overlay.
- [Marker](marker.md) — A balloon-shaped annotation that marks a map location.
- [UserAnnotation](userannotation.md) — Displays the person’s current location on the map.
