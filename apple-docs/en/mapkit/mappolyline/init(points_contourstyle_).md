---
title: 'init(points:contourStyle:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mappolyline/init(points:contourstyle:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mappolyline/init(points:contourstyle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mappolyline/init%28points%3Acontourstyle%3A%29.json'
content_hash: 'sha256:3487039a639dcfe9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapPolyline](../mappolyline.md)

# init(points:contourStyle:)

<sub>Initializer</sub>

Creates a new polyline that traces a path between the provided points using the specifed contour style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(points: [MKMapPoint], contourStyle: MapPolyline.ContourStyle = .straight)
```

## Parameters

- `points` — The points to trace the path between.

- `contourStyle` — The [ContourStyle](contourstyle.md) to use.

## See Also

### Creating a polyline

- [init(_:)](<init(__)-93u7w.md>) — Creates a polyline from polyline you provide.
- [init(_:)](<init(__)-5p2kx.md>) — Creates a polyline that traces the route you provide.
- [init(coordinates:contourStyle:)](<init(coordinates_contourstyle_).md>) — Creates a polyline that traces a path between the given coordinates using the specifed contour style.
