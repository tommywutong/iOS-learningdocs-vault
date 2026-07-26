---
title: 'hitTest(_:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayer/hittest(_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/hittest(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/hittest%28_%3A%29.json'
content_hash: 'sha256:c29e26b469458980'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# hitTest(_:)

<sub>Instance Method</sub>

Returns the farthest descendant of the receiver in the layer hierarchy (including itself) that contains the specified point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func hitTest(_ p: CGPoint) -> CALayer?
```

## Parameters

- `p` — A point in the coordinate system of the receiver’s superlayer.

## Return Value

The layer that contains `thePoint` or `nil` if the point lies outside the receiver’s bounds rectangle.

## See Also

### Hit testing

- [- containsPoint:](<contains(__).md>) — Returns whether the receiver contains a specified point.
