---
title: NSRect
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsrect
source_url: 'https://developer.apple.com/documentation/foundation/nsrect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsrect.json'
content_hash: 'sha256:98e3c3301d2fa5bd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSRect

<sub>Type Alias</sub>

A rectangle.

<sub>Mac Catalyst, macOS</sub>

```swift
typealias NSRect = CGRect
```

## Discussion

When building for 64 bit systems, or building 32 bit like 64 bit, `NSRect` is typedef’d to `CGRect`.

## Topics

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
- [NSMinX](<nsminx(__).md>) — Returns the smallest x coordinate of a given rectangle.
- [NSMinY](<nsminy(__).md>) — Returns the smallest y coordinate of a given rectangle.
- [NSMouseInRect](<nsmouseinrect(______).md>) — Returns a Boolean value that indicates whether the point is in the specified rectangle.
- [NSOffsetRect](<nsoffsetrect(______).md>) — Offsets the rectangle by the specified amount.
- [NSPointInRect](<nspointinrect(____).md>) — Returns a Boolean value that indicates whether a given point is in a given rectangle.
- [NSRectFromString](<nsrectfromstring(__).md>) — Returns a rectangle from a text-based representation.
- [NSStringFromRect](<nsstringfromrect(__).md>) — Returns a string representation of a rectangle.
- [NSRectFromCGRect](<nsrectfromcgrect(__).md>) — Returns an `NSRect` typecast from a `CGRect`.
- [NSRectToCGRect](<nsrecttocgrect(__).md>) — Returns a `CGRect` typecast from an `NSRect`.
- [NSUnionRect](<nsunionrect(____).md>) — Calculates the union of two rectangles.
- [NSWidth](<nswidth(__).md>) — Returns the width of the specified rectangle.

### Zero Constant

- [NSZeroRect](nszerorect.md) — An `NSRect` structure set to `0` in width and height.

### Related Types

- [NSRectEdge](nsrectedge.md)
- [AlignmentOptions](alignmentoptions.md) — Values representing alignment operations.
- [NSRectArray](nsrectarray.md) — Type indicating a parameter is array of `NSRect` structures.
- [NSRectPointer](nsrectpointer.md) — Type indicating a parameter is a pointer to an `NSRect` structure.

## See Also

### Geometry

- [CGFloat](../corefoundation/cgfloat-swift.struct.md) — The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [NSPoint](nspoint.md) — A point in a Cartesian coordinate system.
- [NSSize](nssize.md) — A two-dimensional size.
- [AffineTransform](affinetransform.md) — A graphics coordinate transformation.
- [NSEdgeInsets](nsedgeinsets.md) — A description of the distance between the edges of two rectangles.
