---
title: 'NSIntersectionRect(_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsintersectionrect(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsintersectionrect(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsintersectionrect%28_%3A_%3A%29.json'
content_hash: 'sha256:c26da31a5b6b41c6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSIntersectionRect(_:_:)

<sub>Function</sub>

Calculates the intersection of two rectangles.

<sub>Mac Catalyst, macOS</sub>

```swift
func NSIntersectionRect(_ aRect: NSRect, _ bRect: NSRect) -> NSRect
```

## Return Value

The graphic intersection of `aRect` and `bRect`. If the two rectangles don’t overlap, the returned rectangle has its origin at (0.0, 0.0) and zero width and height (including situations where the intersection is a point or a line segment).

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
- [NSIntersectsRect](<nsintersectsrect(____).md>) — Returns a Boolean value that indicates whether two rectangles intersect.
- [NSMakeRect](<nsmakerect(________).md>) — Creates a new `NSRect` from the specified values.
- [NSMaxX](<nsmaxx(__).md>) — Returns the largest x coordinate of a given rectangle.
- [NSMaxY](<nsmaxy(__).md>) — Returns the largest y coordinate of a given rectangle.
- [NSMidX](<nsmidx(__).md>) — Returns the x coordinate of a given rectangle’s midpoint.
- [NSMidY](<nsmidy(__).md>) — Returns the y coordinate of a given rectangle’s midpoint.
- [NSMinX](<nsminx(__).md>) — Returns the smallest x coordinate of a given rectangle.
