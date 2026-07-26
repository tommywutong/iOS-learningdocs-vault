---
title: 'CGRectIntersectsRect(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgrectintersectsrect(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgrectintersectsrect(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgrectintersectsrect%28_%3A_%3A%29.json'
content_hash: 'sha256:5fff95c902551494'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGRectIntersectsRect(_:_:)

<sub>Function</sub>

Returns whether two rectangles intersect.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGRectIntersectsRect(_ rect1: CGRect, _ rect2: CGRect) -> Bool
```

## Parameters

- `rect1` — The first rectangle to examine.

- `rect2` — The second rectangle to examine.

## Return Value

[true](../swift/true.md) if the two specified rectangles intersect; otherwise, [false](../swift/false.md). The first rectangle intersects the second if the intersection of the rectangles is not equal to the null rectangle.

## See Also

### Comparing Values

- [CGRectEqualToRect](<cgrectequaltorect(____).md>) — Returns whether two rectangles are equal in size and position. _(deprecated)_
