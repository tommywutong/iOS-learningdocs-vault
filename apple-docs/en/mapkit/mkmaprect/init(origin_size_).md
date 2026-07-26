---
title: 'init(origin:size:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmaprect/init(origin:size:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmaprect/init(origin:size:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmaprect/init%28origin%3Asize%3A%29.json'
content_hash: 'sha256:7e53d81bf1339e72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapRect](../mkmaprect.md)

# init(origin:size:)

<sub>Initializer</sub>

Creates the map rectangle with the specified point and size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(origin: MKMapPoint, size: MKMapSize)
```

## Parameters

- `origin` — The origin of the map rectangle as an [MKMapPoint](../mkmappoint.md).

- `size` — The size of the map rectangle as an [MKMapSize](../mkmapsize.md).

## See Also

### Creating a map rectangle

- [init()](<init().md>) — Creates the rectangle with an empty region.
- [MKMapRectMake](<init(x_y_width_height_).md>) — Creates a new map rectangle structure from the specified values.
- [MKCoordinateRegionForMapRect](<../mkcoordinateregion/init(__).md>) — Returns the region that corresponds to the specified map rectangle.
