---
title: 'intersects(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkoverlay/intersects(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlay/intersects(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlay/intersects%28_%3A%29.json'
content_hash: 'sha256:70d9fc88ae8001bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlay](../mkoverlay.md)

# intersects(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the specified rectangle intersects the overlay’s shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func intersects(_ mapRect: MKMapRect) -> Bool
```

## Parameters

- `mapRect` — The rectangle to intersect with the overlay’s area.

## Return Value

[true](../../swift/true.md) if any part of the map rectangle intersects the receiver’s shape, or [false](../../swift/false.md) if it doesn’t.

## Discussion

You can implement this method to provide more specific bounds-checking for an overlay. If you don’t implement it, the method uses the bounding rectangle to detect intersections.
