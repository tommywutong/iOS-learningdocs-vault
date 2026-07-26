---
title: init()
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmaprect/init()
source_url: 'https://developer.apple.com/documentation/mapkit/mkmaprect/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmaprect/init%28%29.json'
content_hash: 'sha256:21d6ee5f973cff35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapRect](../mkmaprect.md)

# init()

<sub>Initializer</sub>

Creates the rectangle with an empty region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## Discussion

This method sets the origin point to `(0, 0)` and the size to `(0, 0)`.

## See Also

### Creating a map rectangle

- [init(origin:size:)](<init(origin_size_).md>) — Creates the map rectangle with the specified point and size.
- [MKMapRectMake](<init(x_y_width_height_).md>) — Creates a new map rectangle structure from the specified values.
- [MKCoordinateRegionForMapRect](<../mkcoordinateregion/init(__).md>) — Returns the region that corresponds to the specified map rectangle.
