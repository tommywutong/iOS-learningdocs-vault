---
title: contentAlignmentPoint
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, tvOS 17.4+, visionOS 1.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/contentalignmentpoint
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/contentalignmentpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/contentalignmentpoint.json'
content_hash: 'sha256:6f657081c5039960'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# contentAlignmentPoint

<sub>Instance Property</sub>

A point where the scroll view anchors content that’s smaller than the scroll view’s frame.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var contentAlignmentPoint: CGPoint { get set }
```

## Discussion

The value for this point is in the unit square, with `(0,0)` representing the top-left corner of the scroll view’s frame, and `(1,1)` representing the bottom-right corner. The default value is `(0,0)`.

If the scroll view’s content is smaller than the scroll view’s frame, the scroll view anchors the content to the specified point relative to its frame. For example, to center smaller content in the scroll view, set its [contentAlignmentPoint](contentalignmentpoint.md) to `(0.5,0.5)`.
