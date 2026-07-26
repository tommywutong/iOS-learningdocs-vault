---
title: 'CGRectIsInfinite(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgrectisinfinite(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgrectisinfinite(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgrectisinfinite%28_%3A%29.json'
content_hash: 'sha256:9024a60c7caf71be'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGRectIsInfinite(_:)

<sub>Function</sub>

Returns whether a rectangle is infinite.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGRectIsInfinite(_ rect: CGRect) -> Bool
```

## Parameters

- `rect` — The rectangle to examine.

## Return Value

Returns [true](../swift/true.md) if the specified rectangle is infinite; otherwise, [false](../swift/false.md).

## Discussion

An infinite rectangle is one that has no defined bounds. Infinite rectangles can be created as output from a tiling filter. For example, the Core Image framework perspective tile filter creates an image whose extent is described by an infinite rectangle.

## See Also

### Checking Rectangle Characteristics

- [CGRectIsEmpty](<cgrectisempty(__).md>) — Returns whether a rectangle has zero width or height, or is a null rectangle.
- [CGRectIsNull](<cgrectisnull(__).md>) — Returns whether the rectangle is equal to the null rectangle.
