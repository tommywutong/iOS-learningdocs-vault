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
doc_path: '/documentation/mapkit/mkmaprect/contains(_:)-79tjt'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmaprect/contains(_:)-79tjt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmaprect/contains%28_%3A%29-79tjt.json'
content_hash: 'sha256:2fd5c763bda590cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapRect](../mkmaprect.md)

# contains(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the specified map point lies within the rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(_ point: MKMapPoint) -> Bool
```

## Parameters

- `point` — The point to check.

## Return Value

[true](../../swift/true.md) if the rectangle isn’t `null` or empty and the point is inside the rectangle; otherwise, [false](../../swift/false.md).

## Discussion

For this method, a point is inside the rectangle if its coordinates lie inside the rectangle or on the minimum X or minimum Y edge.

## See Also

### Intersecting the rectangle

- [MKMapRectContainsRect](<contains(__)-1z5oa.md>) — Returns a Boolean value that indicates whether one rectangle contains another.
- [MKMapRectIntersectsRect](<intersects(__).md>) — Returns a Boolean value that indicates whether two rectangles intersect each other.
