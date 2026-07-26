---
title: scrollsToTop
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/scrollstotop
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/scrollstotop'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/scrollstotop.json'
content_hash: 'sha256:660c9629753980a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# scrollsToTop

<sub>Instance Property</sub>

A Boolean value that controls whether the scroll-to-top gesture is enabled.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var scrollsToTop: Bool { get set }
```

## Discussion

The scroll-to-top gesture is a tap on the status bar. When a user makes this gesture, the system asks the scroll view closest to the status bar to scroll to the top. If that scroll view has [scrollsToTop](scrollstotop.md) set to [false](../../swift/false.md), its delegate returns [false](../../swift/false.md) from [- scrollViewShouldScrollToTop:](<../uiscrollviewdelegate/scrollviewshouldscrolltotop(__).md>), or the content is already at the top, nothing happens.

After the scroll view scrolls to the top of the content view, it sends the delegate a [- scrollViewDidScrollToTop:](<../uiscrollviewdelegate/scrollviewdidscrolltotop(__).md>) message.

The default value of this property is [true](../../swift/true.md).

### Special considerations

On iPhone, the scroll-to-top gesture has no effect if there’s more than one scroll view onscreen that has [scrollsToTop](scrollstotop.md) set to [true](../../swift/true.md).

## See Also

### Configuring the scroll view

- [scrollEnabled](isscrollenabled.md) — A Boolean value that determines whether scrolling is enabled.
- [directionalLockEnabled](isdirectionallockenabled.md) — A Boolean value that determines whether scrolling is disabled in a particular direction.
- [pagingEnabled](ispagingenabled.md) — A Boolean value that determines whether paging is enabled for the scroll view.
- [bounces](bounces.md) — A Boolean value that controls whether the scroll view bounces past the edge of content and back again.
- [bouncesHorizontally](bounceshorizontally.md) — A Boolean value that determines whether the scroll view bounces when it reaches the ends of its horizontal axis.
- [bouncesVertically](bouncesvertically.md) — A Boolean value that determines whether the scroll view bounces when it reaches the ends of its vertical axis.
- [alwaysBounceVertical](alwaysbouncevertical.md) — A Boolean value that determines whether bouncing always occurs when vertical scrolling reaches the end of the content.
- [alwaysBounceHorizontal](alwaysbouncehorizontal.md) — A Boolean value that determines whether bouncing always occurs when horizontal scrolling reaches the end of the content view.
