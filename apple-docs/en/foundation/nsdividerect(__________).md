---
title: 'NSDivideRect(_:_:_:_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdividerect(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdividerect(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdividerect%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:df14ea8b0384b0dd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSDivideRect(_:_:_:_:_:)

<sub>Function</sub>

Divides a rectangle into two new rectangles.

<sub>Mac Catalyst, macOS</sub>

```swift
func NSDivideRect(_ inRect: NSRect, _ slice: UnsafeMutablePointer<NSRect>, _ rem: UnsafeMutablePointer<NSRect>, _ amount: Double, _ edge: NSRectEdge)
```

## Discussion

Creates two rectangles—`slice` and `rem`—from `inRect`, by dividing `inRect` with a line that’s parallel to the side of `inRect` specified by `edge`. The size of `slice` is determined by `amount`, which specifies the distance from `edge`.

`slice` and `rem` must not be `NULL`.

For more information, see [NSRectEdge](nsrectedge.md).

## See Also

### Managing Rectangles

- [NSContainsRect](<nscontainsrect(____).md>) — Returns a Boolean value that indicates whether one rectangle completely encloses another.
- [NSEqualRects](<nsequalrects(____).md>) — Returns a Boolean value that indicates whether the two rectangles are equal.
- [NSIsEmptyRect](<nsisemptyrect(__).md>) — Returns a Boolean value that indicates whether a given rectangle is empty.
- [NSHeight](<nsheight(__).md>) — Returns the height of a given rectangle.
- [NSInsetRect](<nsinsetrect(______).md>) — Insets a rectangle by a specified amount.
- [NSIntegralRect](<nsintegralrect(__).md>) — Adjusts the sides of a rectangle to integer values.
- [NSIntegralRectWithOptions](<nsintegralrectwithoptions(____).md>) — Adjusts the sides of a rectangle to integral values using the specified options.
- [NSIntersectionRect](<nsintersectionrect(____).md>) — Calculates the intersection of two rectangles.
- [NSIntersectsRect](<nsintersectsrect(____).md>) — Returns a Boolean value that indicates whether two rectangles intersect.
- [NSMakeRect](<nsmakerect(________).md>) — Creates a new `NSRect` from the specified values.
- [NSMaxX](<nsmaxx(__).md>) — Returns the largest x coordinate of a given rectangle.
- [NSMaxY](<nsmaxy(__).md>) — Returns the largest y coordinate of a given rectangle.
- [NSMidX](<nsmidx(__).md>) — Returns the x coordinate of a given rectangle’s midpoint.
- [NSMidY](<nsmidy(__).md>) — Returns the y coordinate of a given rectangle’s midpoint.
- [NSMinX](<nsminx(__).md>) — Returns the smallest x coordinate of a given rectangle.
