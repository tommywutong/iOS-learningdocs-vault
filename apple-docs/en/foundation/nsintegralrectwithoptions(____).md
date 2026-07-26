---
title: 'NSIntegralRectWithOptions(_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsintegralrectwithoptions(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsintegralrectwithoptions(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsintegralrectwithoptions%28_%3A_%3A%29.json'
content_hash: 'sha256:42915f4db42de929'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSIntegralRectWithOptions(_:_:)

<sub>Function</sub>

Adjusts the sides of a rectangle to integral values using the specified options.

<sub>Mac Catalyst, macOS</sub>

```swift
func NSIntegralRectWithOptions(_ aRect: NSRect, _ opts: AlignmentOptions) -> NSRect
```

## Return Value

A copy of `aRect`, modified based on the options. The options are defined in `NSAlignmentOptions`.

## See Also

### Managing Rectangles

- [NSContainsRect](<nscontainsrect(____).md>) — Returns a Boolean value that indicates whether one rectangle completely encloses another.
- [NSDivideRect](<nsdividerect(__________).md>) — Divides a rectangle into two new rectangles.
- [NSEqualRects](<nsequalrects(____).md>) — Returns a Boolean value that indicates whether the two rectangles are equal.
- [NSIsEmptyRect](<nsisemptyrect(__).md>) — Returns a Boolean value that indicates whether a given rectangle is empty.
- [NSHeight](<nsheight(__).md>) — Returns the height of a given rectangle.
- [NSInsetRect](<nsinsetrect(______).md>) — Insets a rectangle by a specified amount.
- [NSIntegralRect](<nsintegralrect(__).md>) — Adjusts the sides of a rectangle to integer values.
- [NSIntersectionRect](<nsintersectionrect(____).md>) — Calculates the intersection of two rectangles.
- [NSIntersectsRect](<nsintersectsrect(____).md>) — Returns a Boolean value that indicates whether two rectangles intersect.
- [NSMakeRect](<nsmakerect(________).md>) — Creates a new `NSRect` from the specified values.
- [NSMaxX](<nsmaxx(__).md>) — Returns the largest x coordinate of a given rectangle.
- [NSMaxY](<nsmaxy(__).md>) — Returns the largest y coordinate of a given rectangle.
- [NSMidX](<nsmidx(__).md>) — Returns the x coordinate of a given rectangle’s midpoint.
- [NSMidY](<nsmidy(__).md>) — Returns the y coordinate of a given rectangle’s midpoint.
- [NSMinX](<nsminx(__).md>) — Returns the smallest x coordinate of a given rectangle.
