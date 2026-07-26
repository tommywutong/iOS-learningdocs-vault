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
doc_path: '/documentation/mapkit/mapcircle/init(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapcircle/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcircle/init%28_%3A%29.json'
content_hash: 'sha256:2a4f4a021c0da909'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapCircle](../mapcircle.md)

# init(_:)

<sub>Initializer</sub>

Creates a circle overlay from an existing map circle object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ circle: MKCircle)
```

## Parameters

- `circle` — The circle to convert.

## See Also

### Creating a map circle

- [init(center:radius:)](<init(center_radius_).md>) — Creates a circle with the center coordinate and radius you specify.
- [init(mapRect:)](<init(maprect_).md>) — Creates the largest possible circle centered within the given map rectangle.
