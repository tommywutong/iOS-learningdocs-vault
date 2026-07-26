---
title: 'scrollViewDidEndScrollingAnimation(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscrollviewdelegate/scrollviewdidendscrollinganimation(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/scrollviewdidendscrollinganimation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollviewdelegate/scrollviewdidendscrollinganimation%28_%3A%29.json'
content_hash: 'sha256:60c85fc7c489daa9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollViewDelegate](../uiscrollviewdelegate.md)

# scrollViewDidEndScrollingAnimation(_:)

<sub>Instance Method</sub>

Tells the delegate when a scrolling animation in the scroll view concludes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func scrollViewDidEndScrollingAnimation(_ scrollView: UIScrollView)
```

## Parameters

- `scrollView` — The scroll-view object that’s performing the scrolling animation.

## Discussion

The scroll view calls this method at the end of its implementations of the [- setContentOffset:animated:](<../uiscrollview/setcontentoffset(__animated_).md>) and [- scrollRectToVisible:animated:](<../uiscrollview/scrollrecttovisible(__animated_).md>) methods, but only if animations are requested.
