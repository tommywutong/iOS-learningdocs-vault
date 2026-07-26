---
title: 'NSMouseInRect(_:_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmouseinrect(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmouseinrect(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmouseinrect%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:c7080c16bbdf0c30'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMouseInRect(_:_:_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether the point is in the specified rectangle.

<sub>Mac Catalyst, macOS</sub>

```swift
func NSMouseInRect(_ aPoint: NSPoint, _ aRect: NSRect, _ flipped: Bool) -> Bool
```

## Return Value

[true](../swift/true.md) if the hot spot of the cursor lies inside a given rectangle, otherwise [false](../swift/false.md).

## Discussion

This method assumes an unscaled and unrotated coordinate system. Specify [true](../swift/true.md) for `flipped` if the underlying view uses a flipped coordinate system.

Point-in-rectangle functions generally assume that the bottom edge of a rectangle is outside of the rectangle boundaries, while the upper edge is inside the boundaries. This method views `aRect` from the point of view of the user—that is, this method always treats the bottom edge of the rectangle as the one closest to the bottom edge of the user’s screen. By making this adjustment, this function ensures consistent mouse-detection behavior from the user’s perspective.

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
