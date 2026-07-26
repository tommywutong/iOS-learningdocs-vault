---
title: 'init(points:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mappolygon/init(points:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mappolygon/init(points:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mappolygon/init%28points%3A%29.json'
content_hash: 'sha256:91644d317ae2e9e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapPolygon](../mappolygon.md)

# init(points:)

<sub>Initializer</sub>

Creates a polygon from a list of map points.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(points: [MKMapPoint])
```

## Parameters

- `points` — An array of [MKMapPoint](../mkmappoint.md) points that make up the vertices of the polygon.

## See Also

### Creating a map polygon

- [init(coordinates:)](<init(coordinates_).md>) — Creates a polygon from a list of coordinates you provide.
- [init(_:)](<init(__).md>) — Creates a polygon from the polygon you provide.
