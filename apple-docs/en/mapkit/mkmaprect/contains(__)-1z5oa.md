---
title: 'contains(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmaprect/contains(_:)-1z5oa'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmaprect/contains(_:)-1z5oa'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmaprect/contains%28_%3A%29-1z5oa.json'
content_hash: 'sha256:1a4dea3aab70b9fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapRect](../mkmaprect.md)

# contains(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether one rectangle contains another.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(_ rect2: MKMapRect) -> Bool
```

## Parameters

- `rect2` — The rectangle that `rect1` might contain.

## Return Value

[true](../../swift/true.md) if `rect2` is `null` or lies entirely inside `rect1`; otherwise, returns [false](../../swift/false.md) if `rect1` is `null` or doesn’t completely enclose `rect2`.

## See Also

### Intersecting the rectangle

- [MKMapRectContainsPoint](<contains(__)-79tjt.md>) — Returns a Boolean value that indicates whether the specified map point lies within the rectangle.
- [MKMapRectIntersectsRect](<intersects(__).md>) — Returns a Boolean value that indicates whether two rectangles intersect each other.
