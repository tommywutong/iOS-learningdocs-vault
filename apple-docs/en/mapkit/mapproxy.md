---
title: MapProxy
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapproxy
source_url: 'https://developer.apple.com/documentation/mapkit/mapproxy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapproxy.json'
content_hash: 'sha256:c5ced836878e5690'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapProxy

<sub>Structure</sub>

A proxy for accessing sizing information about a given map view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MapProxy
```

## Topics

### Creating a camera proxy

- [camera(framing:)](<mapproxy/camera(framing_)-1asl2.md>) — Creates a camera in the context of the map that frames the given coordinate region.
- [camera(framing:)](<mapproxy/camera(framing_)-uxov.md>) — Creates a camera in the context of the map that frames the given map rectangle.
- [camera(framing:allowPitch:)](<mapproxy/camera(framing_allowpitch_).md>) — Creates a camera in the context of the map that frames the given map item.

### Converting between coordinate spaces

- [convert(_:to:)](<mapproxy/convert(__to_).md>) — Converts a map coordinate to a point in the specified coordinate space.
- [convert(_:from:)](<mapproxy/convert(__from_).md>) — Converts a point in the specified coordinate space to a map coordinate.

## See Also

### Structures

- [DefaultUserAnnotationContent](defaultuserannotationcontent.md) — A structure that represents the view to show at the user’s location on the map.
- [EmptyMapContent](emptymapcontent.md) — A map content element that doesn’t contain any content.
- [MapReader](mapreader.md) — A container view that defines its contents as a function of information about the first contained map.
- [TupleMapContent](tuplemapcontent.md) — A view created from a Swift tuple of map content values.
- [MapSelectableContentView](mapselectablecontentview.md)
