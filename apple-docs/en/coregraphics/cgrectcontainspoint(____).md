---
title: 'CGRectContainsPoint(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgrectcontainspoint(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgrectcontainspoint(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgrectcontainspoint%28_%3A_%3A%29.json'
content_hash: 'sha256:4df5194c9094d595'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGRectContainsPoint(_:_:)

<sub>Function</sub>

Returns whether a rectangle contains a specified point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGRectContainsPoint(_ rect: CGRect, _ point: CGPoint) -> Bool
```

## Parameters

- `rect` — The rectangle to examine.

- `point` — The point to examine.

## Return Value

[true](../swift/true.md) if the rectangle is not null or empty and the point is located within the rectangle; otherwise, [false](../swift/false.md).

## Discussion

A point is considered inside the rectangle if its coordinates lie inside the rectangle or on the minimum X or minimum Y edge.

## See Also

### Checking for Membership

- [CGRectContainsRect](<cgrectcontainsrect(____).md>) — Returns whether the first rectangle contains the second rectangle.
