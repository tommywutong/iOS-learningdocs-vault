---
title: 'CGRectIsEmpty(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgrectisempty(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgrectisempty(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgrectisempty%28_%3A%29.json'
content_hash: 'sha256:c380f82f872493cc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGRectIsEmpty(_:)

<sub>Function</sub>

Returns whether a rectangle has zero width or height, or is a null rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGRectIsEmpty(_ rect: CGRect) -> Bool
```

## Parameters

- `rect` — The rectangle to examine.

## Return Value

[true](../swift/true.md) if the specified rectangle is empty; otherwise, [false](../swift/false.md).

## Discussion

An empty rectangle is either a null rectangle or a valid rectangle with zero height or width.

## See Also

### Checking Rectangle Characteristics

- [CGRectIsNull](<cgrectisnull(__).md>) — Returns whether the rectangle is equal to the null rectangle.
- [CGRectIsInfinite](<cgrectisinfinite(__).md>) — Returns whether a rectangle is infinite.
