---
title: 'NSPointInRect(_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nspointinrect(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nspointinrect(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointinrect%28_%3A_%3A%29.json'
content_hash: 'sha256:8102d2650a237886'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSPointInRect(_:_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether a given point is in a given rectangle.

<sub>Mac Catalyst, macOS</sub>

```swift
func NSPointInRect(_ aPoint: NSPoint, _ aRect: NSRect) -> Bool
```

## Return Value

[true](../swift/true.md) if `aPoint` is located within the rectangle represented by `aRect`, otherwise [false](../swift/false.md).

## Discussion

Point-in-rectangle functions generally assume that the “upper” and “left” edges of a rectangle are inside  the rectangle boundaries, while the “lower” and “right” edges are outside the boundaries. This method treats the “upper” and “left” edges of the rectangle as the ones containing the origin of the rectangle.

### Special Considerations

The meanings of “upper” and “lower” (and “left” and “right”) are relative to the current coordinate system and the location of the rectangle. For a rectangle of positive height located in positive x and y coordinates:

- In the default macOS desktop coordinate system—where the origin is at the bottom left—the rectangle edge closest to the bottom of the screen is the “upper” edge (and is considered inside the rectangle).
- On iOS and in a flipped coordinate system in macOS desktop—where the origin is at the top left—the rectangle edge closest to the bottom of the screen is the “lower” edge (and is considered outside the rectangle).

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
