---
title: 'intersects(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmaprect/intersects(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmaprect/intersects(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmaprect/intersects%28_%3A%29.json'
content_hash: 'sha256:030783f5e4f60b2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapRect](../mkmaprect.md)

# intersects(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether two rectangles intersect each other.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func intersects(_ rect2: MKMapRect) -> Bool
```

## Parameters

- `rect2` — The second rectangle.

## Return Value

[true](../../swift/true.md) if `rect1` and `rect2` intersect each other, or [false](../../swift/false.md) if they don’t intersect or either rectangle is `null`.

## Discussion

The rectangles aren’t intersecting if the only intersection occurs along an edge. For a true intersection, the rectangles both need to enclose a single rectangular area with a width and height that are both greater than `0`.

## See Also

### Intersecting the rectangle

- [MKMapRectContainsPoint](<contains(__)-79tjt.md>) — Returns a Boolean value that indicates whether the specified map point lies within the rectangle.
- [MKMapRectContainsRect](<contains(__)-1z5oa.md>) — Returns a Boolean value that indicates whether one rectangle contains another.
