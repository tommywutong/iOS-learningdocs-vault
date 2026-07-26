---
title: 'CGRectContainsRect(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgrectcontainsrect(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgrectcontainsrect(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgrectcontainsrect%28_%3A_%3A%29.json'
content_hash: 'sha256:5c45fd803f3ab83a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGRectContainsRect(_:_:)

<sub>Function</sub>

Returns whether the first rectangle contains the second rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGRectContainsRect(_ rect1: CGRect, _ rect2: CGRect) -> Bool
```

## Parameters

- `rect1` — The rectangle to examine for containment of the rectangle passed in `rect2`.

- `rect2` — The rectangle to examine for being contained in the rectangle passed in `rect1`.

## Return Value

[true](../swift/true.md) if the rectangle specified by `rect2` is contained in the rectangle passed in `rect1`; otherwise, [false](../swift/false.md). The first rectangle contains the second if the union of the two rectangles is equal to the first rectangle.

## See Also

### Checking for Membership

- [CGRectContainsPoint](<cgrectcontainspoint(____).md>) — Returns whether a rectangle contains a specified point.
