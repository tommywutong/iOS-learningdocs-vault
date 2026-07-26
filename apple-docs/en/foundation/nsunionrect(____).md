---
title: 'NSUnionRect(_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsunionrect(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsunionrect(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsunionrect%28_%3A_%3A%29.json'
content_hash: 'sha256:14ef6810ac493bd1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSUnionRect(_:_:)

<sub>Function</sub>

Calculates the union of two rectangles.

<sub>Mac Catalyst, macOS</sub>

```swift
func NSUnionRect(_ aRect: NSRect, _ bRect: NSRect) -> NSRect
```

## Discussion

Returns the smallest rectangle that completely encloses both `aRect` and `bRect`. If one of the rectangles has 0 (or negative) width or height, a copy of the other rectangle is returned; but if both have 0 (or negative) width or height, the returned rectangle has its origin at (0.0, 0.0) and has 0 width and height.

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
- [NSIntersectsRect](<nsintersectsrect(____).md>) — Returns a Boolean value that indicates whether two rectangles intersect.
- [NSMakeRect](<nsmakerect(________).md>) — Creates a new `NSRect` from the specified values.
- [NSMaxX](<nsmaxx(__).md>) — Returns the largest x coordinate of a given rectangle.
- [NSMaxY](<nsmaxy(__).md>) — Returns the largest y coordinate of a given rectangle.
- [NSMidX](<nsmidx(__).md>) — Returns the x coordinate of a given rectangle’s midpoint.
- [NSMidY](<nsmidy(__).md>) — Returns the y coordinate of a given rectangle’s midpoint.
