---
title: 'intersection(_:eoFill:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shape/intersection(_:eofill:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shape/intersection(_:eofill:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/intersection%28_%3Aeofill%3A%29.json'
content_hash: 'sha256:443046cd713ca011'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# intersection(_:eoFill:)

<sub>Instance Method</sub>

Returns a new shape with filled regions common to both shapes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func intersection<T>(_ other: T, eoFill: Bool = false) -> some Shape where T : Shape

```

## Parameters

- `other` — The shape to intersect.

- `eoFill` — Whether to use the even-odd rule for determining which areas to treat as the interior of the shapes (if true), or the non-zero rule (if false).

## Return Value

A new shape.

## Discussion

The filled region of the resulting shape is the overlapping area of the filled region of both shapes.  This can be used to clip the fill of a shape to a mask.

Any unclosed subpaths in either shape are assumed to be closed. The result of filling this shape using either even-odd or non-zero fill rules is identical.

## See Also

### Performing operations on a shape

- [lineIntersection(_:eoFill:)](<lineintersection(__eofill_).md>) — Returns a new shape with a line from this shape that overlaps the filled regions of the given shape.
- [lineSubtraction(_:eoFill:)](<linesubtraction(__eofill_).md>) — Returns a new shape with a line from this shape that does not overlap the filled region of the given shape.
- [subtracting(_:eoFill:)](<subtracting(__eofill_).md>) — Returns a new shape with filled regions from this shape that are not in the given shape.
- [symmetricDifference(_:eoFill:)](<symmetricdifference(__eofill_).md>) — Returns a new shape with filled regions either from this shape or the given shape, but not in both.
- [union(_:eoFill:)](<union(__eofill_).md>) — Returns a new shape with filled regions in either this shape or the given shape.
