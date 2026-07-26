---
title: 'init(_:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mappolyline/init(_:)-5p2kx'
source_url: 'https://developer.apple.com/documentation/mapkit/mappolyline/init(_:)-5p2kx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mappolyline/init%28_%3A%29-5p2kx.json'
content_hash: 'sha256:a98acadc8ec8ac40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapPolyline](../mappolyline.md)

# init(_:)

<sub>Initializer</sub>

Creates a polyline that traces the route you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ route: MKRoute)
```

## Parameters

- `route` — The [MKRoute](../mkroute.md) to trace.

## See Also

### Creating a polyline

- [init(_:)](<init(__)-93u7w.md>) — Creates a polyline from polyline you provide.
- [init(coordinates:contourStyle:)](<init(coordinates_contourstyle_).md>) — Creates a polyline that traces a path between the given coordinates using the specifed contour style.
- [init(points:contourStyle:)](<init(points_contourstyle_).md>) — Creates a new polyline that traces a path between the provided points using the specifed contour style.
