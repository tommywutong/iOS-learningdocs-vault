---
title: 'scrollViewDidScroll(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscrollviewdelegate/scrollviewdidscroll(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/scrollviewdidscroll(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollviewdelegate/scrollviewdidscroll%28_%3A%29.json'
content_hash: 'sha256:dd97f4eb995c679f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollViewDelegate](../uiscrollviewdelegate.md)

# scrollViewDidScroll(_:)

<sub>Instance Method</sub>

Tells the delegate when the user scrolls the content view within the scroll view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func scrollViewDidScroll(_ scrollView: UIScrollView)
```

## Parameters

- `scrollView` — The scroll-view object in which the scrolling occurred.

## Discussion

The delegate typically implements this method to obtain the change in content offset from `scrollView` and draw the affected portion of the content view.

## See Also

### Responding to scrolling and dragging

- [- scrollViewWillBeginDragging:](<scrollviewwillbegindragging(__).md>) — Tells the delegate when the scroll view is about to start scrolling the content.
- [- scrollViewWillEndDragging:withVelocity:targetContentOffset:](<scrollviewwillenddragging(__withvelocity_targetcontentoffset_).md>) — Tells the delegate when the user finishes scrolling the content.
- [- scrollViewDidEndDragging:willDecelerate:](<scrollviewdidenddragging(__willdecelerate_).md>) — Tells the delegate when dragging ended in the scroll view.
- [- scrollViewShouldScrollToTop:](<scrollviewshouldscrolltotop(__).md>) — Asks the delegate if the scroll view should scroll to the top of the content.
- [- scrollViewDidScrollToTop:](<scrollviewdidscrolltotop(__).md>) — Tells the delegate that the scroll view scrolled to the top of the content.
- [- scrollViewWillBeginDecelerating:](<scrollviewwillbegindecelerating(__).md>) — Tells the delegate that the scroll view is starting to decelerate the scrolling movement.
- [- scrollViewDidEndDecelerating:](<scrollviewdidenddecelerating(__).md>) — Tells the delegate that the scroll view ended decelerating the scrolling movement.
