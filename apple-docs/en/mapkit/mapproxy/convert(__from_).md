---
title: 'convert(_:from:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapproxy/convert(_:from:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapproxy/convert(_:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapproxy/convert%28_%3Afrom%3A%29.json'
content_hash: 'sha256:a61e26f8283113d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapProxy](../mapproxy.md)

# convert(_:from:)

<sub>Instance Method</sub>

Converts a point in the specified coordinate space to a map coordinate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func convert(_ point: CGPoint, from space: some CoordinateSpaceProtocol) -> CLLocationCoordinate2D?
```

## Parameters

- `point` — The point to convert.

- `space` — The reference coordinate space for `point`.

## Return Value

Returns a [CLLocationCoordinate2D](../../corelocation/cllocationcoordinate2d.md); or `nil,` if the specified `point` isn’t represented by a point in the [MapReader](../mapreader.md) associated with a [Map](../map.md).

## See Also

### Converting between coordinate spaces

- [convert(_:to:)](<convert(__to_).md>) — Converts a map coordinate to a point in the specified coordinate space.
