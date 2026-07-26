---
title: 'lineIntersection(_:eoFill:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shape/lineintersection(_:eofill:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shape/lineintersection(_:eofill:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/lineintersection%28_%3Aeofill%3A%29.json'
content_hash: 'sha256:298b072a38f1212f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# lineIntersection(_:eoFill:)

<sub>Instance Method</sub>

Returns a new shape with a line from this shape that overlaps the filled regions of the given shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func lineIntersection<T>(_ other: T, eoFill: Bool = false) -> some Shape where T : Shape

```

## Parameters

- `other` — The shape to intersect.

- `eoFill` — Whether to use the even-odd rule for determining which areas to treat as the interior of the shapes (if true), or the non-zero rule (if false).

## Return Value

A new shape.

## Discussion

The line of the resulting shape is the line of this shape that overlaps the filled region of `other`.

Intersected subpaths that are clipped create open subpaths. Closed subpaths that do not intersect `other` remain closed.

## See Also

### Performing operations on a shape

- [intersection(_:eoFill:)](<intersection(__eofill_).md>) — Returns a new shape with filled regions common to both shapes.
- [lineSubtraction(_:eoFill:)](<linesubtraction(__eofill_).md>) — Returns a new shape with a line from this shape that does not overlap the filled region of the given shape.
- [subtracting(_:eoFill:)](<subtracting(__eofill_).md>) — Returns a new shape with filled regions from this shape that are not in the given shape.
- [symmetricDifference(_:eoFill:)](<symmetricdifference(__eofill_).md>) — Returns a new shape with filled regions either from this shape or the given shape, but not in both.
- [union(_:eoFill:)](<union(__eofill_).md>) — Returns a new shape with filled regions in either this shape or the given shape.
