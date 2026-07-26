---
title: isPagingEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/ispagingenabled
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/ispagingenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/ispagingenabled.json'
content_hash: 'sha256:0fbc4bd6cc0129c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# isPagingEnabled

<sub>Instance Property</sub>

A Boolean value that determines whether paging is enabled for the scroll view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isPagingEnabled: Bool { get set }
```

## Discussion

If the value of this property is [true](../../swift/true.md), the scroll view stops on multiples of the scroll view’s bounds when the user scrolls. The default value is [false](../../swift/false.md).

## See Also

### Configuring the scroll view

- [scrollEnabled](isscrollenabled.md) — A Boolean value that determines whether scrolling is enabled.
- [directionalLockEnabled](isdirectionallockenabled.md) — A Boolean value that determines whether scrolling is disabled in a particular direction.
- [scrollsToTop](scrollstotop.md) — A Boolean value that controls whether the scroll-to-top gesture is enabled.
- [bounces](bounces.md) — A Boolean value that controls whether the scroll view bounces past the edge of content and back again.
- [bouncesHorizontally](bounceshorizontally.md) — A Boolean value that determines whether the scroll view bounces when it reaches the ends of its horizontal axis.
- [bouncesVertically](bouncesvertically.md) — A Boolean value that determines whether the scroll view bounces when it reaches the ends of its vertical axis.
- [alwaysBounceVertical](alwaysbouncevertical.md) — A Boolean value that determines whether bouncing always occurs when vertical scrolling reaches the end of the content.
- [alwaysBounceHorizontal](alwaysbouncehorizontal.md) — A Boolean value that determines whether bouncing always occurs when horizontal scrolling reaches the end of the content view.
