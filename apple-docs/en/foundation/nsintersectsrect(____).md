---
title: 'NSIntersectsRect(_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsintersectsrect(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsintersectsrect(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsintersectsrect%28_%3A_%3A%29.json'
content_hash: 'sha256:4182ed9774c15980'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSIntersectsRect(_:_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether two rectangles intersect.

<sub>Mac Catalyst, macOS</sub>

```swift
func NSIntersectsRect(_ aRect: NSRect, _ bRect: NSRect) -> Bool
```

## Return Value

[true](../swift/true.md) if `aRect` intersects `bRect`, otherwise [false](../swift/false.md). Returns [false](../swift/false.md) if either `aRect` or `bRect` has a width or height that is 0.

## See Also

### Managing Rectangles

- [NSContainsRect](<nscontainsrect(____).md>) — Returns a Boolean value that indicates whether one rectangle completely encloses another.
- [NSDivideRect](<nsdividerect(__________).md>) — Divides a rectangle into two new rectangles.
- [NSEqualRects](<nsequalrects(____).md>) — Returns a Boolean value that indicates whether the two rectangles are equal.
- [NSIsEmptyRect](<nsisemptyrect(__).md>) — Returns a Boolean value that indicates whether a given rectangle is empty.
- [NSHeight](<nsheight(__).md>) — Returns the height of a given rectangle.
- [NSInsetRect](<nsinsetrect(______).md>) — Insets a rectangle by a specified amount.
- [NSIntegralRect](<nsintegralrect(__).md>) — Adjusts the sides of a rectangle to integer values.
- [NSIntegralRectWithOptions](<nsintegralrectwithoptions(____).md>) — Adjusts the sides of a rectangle to integral values using the specified options.
- [NSIntersectionRect](<nsintersectionrect(____).md>) — Calculates the intersection of two rectangles.
- [NSMakeRect](<nsmakerect(________).md>) — Creates a new `NSRect` from the specified values.
- [NSMaxX](<nsmaxx(__).md>) — Returns the largest x coordinate of a given rectangle.
- [NSMaxY](<nsmaxy(__).md>) — Returns the largest y coordinate of a given rectangle.
- [NSMidX](<nsmidx(__).md>) — Returns the x coordinate of a given rectangle’s midpoint.
- [NSMidY](<nsmidy(__).md>) — Returns the y coordinate of a given rectangle’s midpoint.
- [NSMinX](<nsminx(__).md>) — Returns the smallest x coordinate of a given rectangle.
