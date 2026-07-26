---
title: 'init(x:y:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmappoint/init(x:y:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmappoint/init(x:y:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmappoint/init%28x%3Ay%3A%29.json'
content_hash: 'sha256:aa823ad50ff38cce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapPoint](../mkmappoint.md)

# init(x:y:)

<sub>Initializer</sub>

Creates a new map point structure from the specified values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(x: Double, y: Double)
```

## Parameters

- `x` — The point along the east-west axis of the map projection.

- `y` — The point along the north-south axis of the map projection.

## Return Value

A map point with the specified values.

## See Also

### Creating a map point

- [init()](<init().md>) — Creates a map point at an unspecified point.
- [MKMapPointForCoordinate](<init(__).md>) — Creates the map point data structure that corresponds to the specified coordinate.
