---
title: UIScrollViewDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollviewdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollviewdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollviewdelegate.json'
content_hash: 'sha256:54a0a34029de41cc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIScrollViewDelegate

<sub>Protocol</sub>

The interface for the delegate of a scroll view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIScrollViewDelegate : NSObjectProtocol
```

## Overview

The methods that the [UIScrollViewDelegate](uiscrollviewdelegate.md) protocol declares allow the adopting delegate to respond to messages from the [UIScrollView](uiscrollview.md) class. The delegate responds to and affects operations like scrolling, zooming, deceleration of scrolled content, and scrolling animations.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [UICollectionViewDelegate](uicollectionviewdelegate.md), [UICollectionViewDelegateFlowLayout](uicollectionviewdelegateflowlayout.md), [UIScrollViewAccessibilityDelegate](uiscrollviewaccessibilitydelegate.md), [UITableViewDelegate](uitableviewdelegate.md), [UITextViewDelegate](uitextviewdelegate.md)

- **Conforming Types**: [UICollectionViewController](uicollectionviewcontroller.md), [UITableViewController](uitableviewcontroller.md), [UIWebView](uiwebview.md)

## Topics

### Responding to scrolling and dragging

- [- scrollViewDidScroll:](<uiscrollviewdelegate/scrollviewdidscroll(__).md>) — Tells the delegate when the user scrolls the content view within the scroll view.
- [- scrollViewWillBeginDragging:](<uiscrollviewdelegate/scrollviewwillbegindragging(__).md>) — Tells the delegate when the scroll view is about to start scrolling the content.
- [- scrollViewWillEndDragging:withVelocity:targetContentOffset:](<uiscrollviewdelegate/scrollviewwillenddragging(__withvelocity_targetcontentoffset_).md>) — Tells the delegate when the user finishes scrolling the content.
- [- scrollViewDidEndDragging:willDecelerate:](<uiscrollviewdelegate/scrollviewdidenddragging(__willdecelerate_).md>) — Tells the delegate when dragging ended in the scroll view.
- [- scrollViewShouldScrollToTop:](<uiscrollviewdelegate/scrollviewshouldscrolltotop(__).md>) — Asks the delegate if the scroll view should scroll to the top of the content.
- [- scrollViewDidScrollToTop:](<uiscrollviewdelegate/scrollviewdidscrolltotop(__).md>) — Tells the delegate that the scroll view scrolled to the top of the content.
- [- scrollViewWillBeginDecelerating:](<uiscrollviewdelegate/scrollviewwillbegindecelerating(__).md>) — Tells the delegate that the scroll view is starting to decelerate the scrolling movement.
- [- scrollViewDidEndDecelerating:](<uiscrollviewdelegate/scrollviewdidenddecelerating(__).md>) — Tells the delegate that the scroll view ended decelerating the scrolling movement.

### Managing zooming

- [- viewForZoomingInScrollView:](<uiscrollviewdelegate/viewforzooming(in_).md>) — Asks the delegate for the view to scale when zooming is about to occur in the scroll view.
- [- scrollViewWillBeginZooming:withView:](<uiscrollviewdelegate/scrollviewwillbeginzooming(__with_).md>) — Tells the delegate that zooming of the content in the scroll view is about to commence.
- [- scrollViewDidEndZooming:withView:atScale:](<uiscrollviewdelegate/scrollviewdidendzooming(__with_atscale_).md>) — Tells the delegate when zooming of the content in the scroll view completed.
- [- scrollViewDidZoom:](<uiscrollviewdelegate/scrollviewdidzoom(__).md>) — Tells the delegate that the scroll view’s zoom factor changed.

### Responding to scrolling animations

- [- scrollViewDidEndScrollingAnimation:](<uiscrollviewdelegate/scrollviewdidendscrollinganimation(__).md>) — Tells the delegate when a scrolling animation in the scroll view concludes.

### Responding to inset changes

- [- scrollViewDidChangeAdjustedContentInset:](<uiscrollviewdelegate/scrollviewdidchangeadjustedcontentinset(__).md>) — Tells the delegate when the scroll view’s inset values change.

## See Also

### Responding to scroll view interactions

- [delegate](uiscrollview/delegate.md) — The delegate of the scroll view.
