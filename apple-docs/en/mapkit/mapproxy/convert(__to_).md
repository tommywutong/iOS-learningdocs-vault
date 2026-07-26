---
title: 'convert(_:to:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapproxy/convert(_:to:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapproxy/convert(_:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapproxy/convert%28_%3Ato%3A%29.json'
content_hash: 'sha256:2d9f3d7795602e35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapProxy](../mapproxy.md)

# convert(_:to:)

<sub>Instance Method</sub>

Converts a map coordinate to a point in the specified coordinate space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func convert(_ coordinate: CLLocationCoordinate2D, to space: some CoordinateSpaceProtocol) -> CGPoint?
```

## Parameters

- `coordinate` — The map coordinate to find the corresponding point for.

- `space` — The reference coordinate space for the returned point.

## Return Value

Returns a [CGPoint](../../corefoundation/cgpoint.md); otherwise `nil`, if `coordinate` isn’t represented by a point in the [MapReader](../mapreader.md) associated with a [Map](../map.md).

## See Also

### Converting between coordinate spaces

- [convert(_:from:)](<convert(__from_).md>) — Converts a point in the specified coordinate space to a map coordinate.
