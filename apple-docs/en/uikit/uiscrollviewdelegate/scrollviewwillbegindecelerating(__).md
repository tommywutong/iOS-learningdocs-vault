---
title: 'scrollViewWillBeginDecelerating(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscrollviewdelegate/scrollviewwillbegindecelerating(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/scrollviewwillbegindecelerating(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollviewdelegate/scrollviewwillbegindecelerating%28_%3A%29.json'
content_hash: 'sha256:8eb42623e30ad5b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollViewDelegate](../uiscrollviewdelegate.md)

# scrollViewWillBeginDecelerating(_:)

<sub>Instance Method</sub>

Tells the delegate that the scroll view is starting to decelerate the scrolling movement.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func scrollViewWillBeginDecelerating(_ scrollView: UIScrollView)
```

## Parameters

- `scrollView` — The scroll-view object that’s decelerating the scrolling of the content view.

## Discussion

The scroll view calls this method as the user’s finger touches up as it’s moving during a scrolling operation; the scroll view continues to move a short distance afterwards. The [decelerating](../uiscrollview/isdecelerating.md) property of [UIScrollView](../uiscrollview.md) controls deceleration.

## See Also

### Responding to scrolling and dragging

- [- scrollViewDidScroll:](<scrollviewdidscroll(__).md>) — Tells the delegate when the user scrolls the content view within the scroll view.
- [- scrollViewWillBeginDragging:](<scrollviewwillbegindragging(__).md>) — Tells the delegate when the scroll view is about to start scrolling the content.
- [- scrollViewWillEndDragging:withVelocity:targetContentOffset:](<scrollviewwillenddragging(__withvelocity_targetcontentoffset_).md>) — Tells the delegate when the user finishes scrolling the content.
- [- scrollViewDidEndDragging:willDecelerate:](<scrollviewdidenddragging(__willdecelerate_).md>) — Tells the delegate when dragging ended in the scroll view.
- [- scrollViewShouldScrollToTop:](<scrollviewshouldscrolltotop(__).md>) — Asks the delegate if the scroll view should scroll to the top of the content.
- [- scrollViewDidScrollToTop:](<scrollviewdidscrolltotop(__).md>) — Tells the delegate that the scroll view scrolled to the top of the content.
- [- scrollViewDidEndDecelerating:](<scrollviewdidenddecelerating(__).md>) — Tells the delegate that the scroll view ended decelerating the scrolling movement.
