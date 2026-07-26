---
title: 'scrollViewDidEndDecelerating(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscrollviewdelegate/scrollviewdidenddecelerating(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/scrollviewdidenddecelerating(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollviewdelegate/scrollviewdidenddecelerating%28_%3A%29.json'
content_hash: 'sha256:e1005bb1659c391d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollViewDelegate](../uiscrollviewdelegate.md)

# scrollViewDidEndDecelerating(_:)

<sub>Instance Method</sub>

Tells the delegate that the scroll view ended decelerating the scrolling movement.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func scrollViewDidEndDecelerating(_ scrollView: UIScrollView)
```

## Parameters

- `scrollView` — The scroll-view object that’s decelerating the scrolling of the content view.

## Discussion

The scroll view calls this method when the scrolling movement comes to a halt. The [decelerating](../uiscrollview/isdecelerating.md) property of `UIScrollView` controls deceleration.

## See Also

### Responding to scrolling and dragging

- [- scrollViewDidScroll:](<scrollviewdidscroll(__).md>) — Tells the delegate when the user scrolls the content view within the scroll view.
- [- scrollViewWillBeginDragging:](<scrollviewwillbegindragging(__).md>) — Tells the delegate when the scroll view is about to start scrolling the content.
- [- scrollViewWillEndDragging:withVelocity:targetContentOffset:](<scrollviewwillenddragging(__withvelocity_targetcontentoffset_).md>) — Tells the delegate when the user finishes scrolling the content.
- [- scrollViewDidEndDragging:willDecelerate:](<scrollviewdidenddragging(__willdecelerate_).md>) — Tells the delegate when dragging ended in the scroll view.
- [- scrollViewShouldScrollToTop:](<scrollviewshouldscrolltotop(__).md>) — Asks the delegate if the scroll view should scroll to the top of the content.
- [- scrollViewDidScrollToTop:](<scrollviewdidscrolltotop(__).md>) — Tells the delegate that the scroll view scrolled to the top of the content.
- [- scrollViewWillBeginDecelerating:](<scrollviewwillbegindecelerating(__).md>) — Tells the delegate that the scroll view is starting to decelerate the scrolling movement.
