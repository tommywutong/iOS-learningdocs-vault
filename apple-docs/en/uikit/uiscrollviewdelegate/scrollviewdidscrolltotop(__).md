---
title: 'scrollViewDidScrollToTop(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscrollviewdelegate/scrollviewdidscrolltotop(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/scrollviewdidscrolltotop(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollviewdelegate/scrollviewdidscrolltotop%28_%3A%29.json'
content_hash: 'sha256:506c697a153c40aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollViewDelegate](../uiscrollviewdelegate.md)

# scrollViewDidScrollToTop(_:)

<sub>Instance Method</sub>

Tells the delegate that the scroll view scrolled to the top of the content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func scrollViewDidScrollToTop(_ scrollView: UIScrollView)
```

## Parameters

- `scrollView` — The scroll-view object that perform the scrolling operation.

## Discussion

The scroll view sends this message when it finishes scrolling to the top of the content. It might call it immediately if the top of the content is already shown. For the scroll-to-top gesture (a tap on the status bar) to be effective, the [scrollsToTop](../uiscrollview/scrollstotop.md) property of the [UIScrollView](../uiscrollview.md) must be set to [true](../../swift/true.md).

## See Also

### Responding to scrolling and dragging

- [- scrollViewDidScroll:](<scrollviewdidscroll(__).md>) — Tells the delegate when the user scrolls the content view within the scroll view.
- [- scrollViewWillBeginDragging:](<scrollviewwillbegindragging(__).md>) — Tells the delegate when the scroll view is about to start scrolling the content.
- [- scrollViewWillEndDragging:withVelocity:targetContentOffset:](<scrollviewwillenddragging(__withvelocity_targetcontentoffset_).md>) — Tells the delegate when the user finishes scrolling the content.
- [- scrollViewDidEndDragging:willDecelerate:](<scrollviewdidenddragging(__willdecelerate_).md>) — Tells the delegate when dragging ended in the scroll view.
- [- scrollViewShouldScrollToTop:](<scrollviewshouldscrolltotop(__).md>) — Asks the delegate if the scroll view should scroll to the top of the content.
- [- scrollViewWillBeginDecelerating:](<scrollviewwillbegindecelerating(__).md>) — Tells the delegate that the scroll view is starting to decelerate the scrolling movement.
- [- scrollViewDidEndDecelerating:](<scrollviewdidenddecelerating(__).md>) — Tells the delegate that the scroll view ended decelerating the scrolling movement.
