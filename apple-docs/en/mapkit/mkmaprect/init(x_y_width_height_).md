---
title: 'init(x:y:width:height:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmaprect/init(x:y:width:height:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmaprect/init(x:y:width:height:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmaprect/init%28x%3Ay%3Awidth%3Aheight%3A%29.json'
content_hash: 'sha256:d594eb836afb0375'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapRect](../mkmaprect.md)

# init(x:y:width:height:)

<sub>Initializer</sub>

Creates a new map rectangle structure from the specified values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(x: Double, y: Double, width: Double, height: Double)
```

## Parameters

- `x` — The point along the east-west axis of the map projection to use for the origin.

- `y` — The point along the north-south axis of the map projection to use for the origin.

- `width` — The width of the rectangle (measured using map points).

- `height` — The height of the rectangle (measured using map points).

## Return Value

A map rectangle with the specified values.

## See Also

### Creating a map rectangle

- [init()](<init().md>) — Creates the rectangle with an empty region.
- [init(origin:size:)](<init(origin_size_).md>) — Creates the map rectangle with the specified point and size.
- [MKCoordinateRegionForMapRect](<../mkcoordinateregion/init(__).md>) — Returns the region that corresponds to the specified map rectangle.
