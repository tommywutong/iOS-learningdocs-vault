---
title: 'CGRectEqualToRect(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/coregraphics/cgrectequaltorect(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgrectequaltorect(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgrectequaltorect%28_%3A_%3A%29.json'
content_hash: 'sha256:ce6f26002b396afb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGRectEqualToRect(_:_:)

<sub>Function</sub>

Returns whether two rectangles are equal in size and position.

> [!warning] Deprecated
> The [CGRect](../corefoundation/cgrect.md) type adopts the `Equatable` protocol; use the `==` operator instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGRectEqualToRect(_ rect1: CGRect, _ rect2: CGRect) -> Bool
```

## Parameters

- `rect1` — The first rectangle to examine.

- `rect2` — The second rectangle to examine.

## Return Value

[true](../swift/true.md) if the two specified rectangles have equal size and origin values, or if both rectangles are null rectangles. Otherwise, [false](../swift/false.md).

## See Also

### Comparing Values

- [CGRectIntersectsRect](<cgrectintersectsrect(____).md>) — Returns whether two rectangles intersect.
