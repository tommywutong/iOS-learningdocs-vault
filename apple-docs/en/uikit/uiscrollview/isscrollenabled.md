---
title: isScrollEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/isscrollenabled
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/isscrollenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/isscrollenabled.json'
content_hash: 'sha256:c02d22794bedf5ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# isScrollEnabled

<sub>Instance Property</sub>

A Boolean value that determines whether scrolling is enabled.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isScrollEnabled: Bool { get set }
```

## Discussion

The default value is [true](../../swift/true.md), which indicates that scrolling is enabled. Setting the value to [false](../../swift/false.md) disables scrolling.

When scrolling is disabled, the scroll view doesn’t accept touch events; it forwards them up the responder chain.

## See Also

### Configuring the scroll view

- [directionalLockEnabled](isdirectionallockenabled.md) — A Boolean value that determines whether scrolling is disabled in a particular direction.
- [pagingEnabled](ispagingenabled.md) — A Boolean value that determines whether paging is enabled for the scroll view.
- [scrollsToTop](scrollstotop.md) — A Boolean value that controls whether the scroll-to-top gesture is enabled.
- [bounces](bounces.md) — A Boolean value that controls whether the scroll view bounces past the edge of content and back again.
- [bouncesHorizontally](bounceshorizontally.md) — A Boolean value that determines whether the scroll view bounces when it reaches the ends of its horizontal axis.
- [bouncesVertically](bouncesvertically.md) — A Boolean value that determines whether the scroll view bounces when it reaches the ends of its vertical axis.
- [alwaysBounceVertical](alwaysbouncevertical.md) — A Boolean value that determines whether bouncing always occurs when vertical scrolling reaches the end of the content.
- [alwaysBounceHorizontal](alwaysbouncehorizontal.md) — A Boolean value that determines whether bouncing always occurs when horizontal scrolling reaches the end of the content view.
