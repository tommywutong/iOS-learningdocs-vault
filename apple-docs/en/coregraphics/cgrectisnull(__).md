---
title: 'CGRectIsNull(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgrectisnull(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgrectisnull(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgrectisnull%28_%3A%29.json'
content_hash: 'sha256:d5e071a59dce3e9e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGRectIsNull(_:)

<sub>Function</sub>

Returns whether the rectangle is equal to the null rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGRectIsNull(_ rect: CGRect) -> Bool
```

## Parameters

- `rect` — The rectangle to examine.

## Return Value

[true](../swift/true.md) if the specified rectangle is null; otherwise, [false](../swift/false.md).

## Discussion

A null rectangle is the equivalent of an empty set. For example, the result of intersecting two disjoint rectangles is a null rectangle. A null rectangle cannot be drawn and interacts with other rectangles in special ways.

## See Also

### Checking Rectangle Characteristics

- [CGRectIsEmpty](<cgrectisempty(__).md>) — Returns whether a rectangle has zero width or height, or is a null rectangle.
- [CGRectIsInfinite](<cgrectisinfinite(__).md>) — Returns whether a rectangle is infinite.
