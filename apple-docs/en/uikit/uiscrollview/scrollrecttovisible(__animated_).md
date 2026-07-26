---
title: 'scrollRectToVisible(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscrollview/scrollrecttovisible(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/scrollrecttovisible(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/scrollrecttovisible%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:e75c32e769f2024c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# scrollRectToVisible(_:animated:)

<sub>Instance Method</sub>

Scrolls a specific area of the content so that it’s visible in the scroll view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func scrollRectToVisible(_ rect: CGRect, animated: Bool)
```

## Parameters

- `rect` — A rectangle defining an area of the content view. The rectangle should be in the coordinate space of the scroll view.

- `animated` — [true](../../swift/true.md) if the scrolling should be animated, [false](../../swift/false.md) if it should be immediate.

## Discussion

This method scrolls the content view so that the area defined by `rect` is just visible inside the scroll view. If the area is already visible, the method does nothing.
