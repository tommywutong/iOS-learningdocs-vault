---
title: alwaysBounceVertical
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/alwaysbouncevertical
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/alwaysbouncevertical'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/alwaysbouncevertical.json'
content_hash: 'sha256:045344e7f67ced6b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# alwaysBounceVertical

<sub>Instance Property</sub>

A Boolean value that determines whether bouncing always occurs when vertical scrolling reaches the end of the content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var alwaysBounceVertical: Bool { get set }
```

## Discussion

If the value of this property is [true](../../swift/true.md) and [bouncesVertically](bouncesvertically.md) is [true](../../swift/true.md), the scroll view allows vertical dragging even if the content is smaller than the bounds of the scroll view. The default value is [false](../../swift/false.md).

## See Also

### Configuring the scroll view

- [scrollEnabled](isscrollenabled.md) — A Boolean value that determines whether scrolling is enabled.
- [directionalLockEnabled](isdirectionallockenabled.md) — A Boolean value that determines whether scrolling is disabled in a particular direction.
- [pagingEnabled](ispagingenabled.md) — A Boolean value that determines whether paging is enabled for the scroll view.
- [scrollsToTop](scrollstotop.md) — A Boolean value that controls whether the scroll-to-top gesture is enabled.
- [bounces](bounces.md) — A Boolean value that controls whether the scroll view bounces past the edge of content and back again.
- [bouncesHorizontally](bounceshorizontally.md) — A Boolean value that determines whether the scroll view bounces when it reaches the ends of its horizontal axis.
- [bouncesVertically](bouncesvertically.md) — A Boolean value that determines whether the scroll view bounces when it reaches the ends of its vertical axis.
- [alwaysBounceHorizontal](alwaysbouncehorizontal.md) — A Boolean value that determines whether bouncing always occurs when horizontal scrolling reaches the end of the content view.
