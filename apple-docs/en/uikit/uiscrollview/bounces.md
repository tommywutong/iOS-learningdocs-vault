---
title: bounces
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/bounces
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/bounces'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/bounces.json'
content_hash: 'sha256:74194f107ac03f49'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# bounces

<sub>Instance Property</sub>

A Boolean value that controls whether the scroll view bounces past the edge of content and back again.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var bounces: Bool { get set }
```

## Discussion

If the value of this property is [true](../../swift/true.md), the scroll view bounces when it encounters a boundary of the content. Bouncing visually indicates that scrolling has reached an edge of the content. If the value is [false](../../swift/false.md), scrolling stops immediately at the content boundary without bouncing. The default value is [true](../../swift/true.md).

Setting [bounces](bounces.md) is equivalent to setting both [bouncesHorizontally](bounceshorizontally.md) and [bouncesVertically](bouncesvertically.md) to the same value. To set different behavior for the two axes, set those properties to distinct values.

## See Also

### Configuring the scroll view

- [scrollEnabled](isscrollenabled.md) — A Boolean value that determines whether scrolling is enabled.
- [directionalLockEnabled](isdirectionallockenabled.md) — A Boolean value that determines whether scrolling is disabled in a particular direction.
- [pagingEnabled](ispagingenabled.md) — A Boolean value that determines whether paging is enabled for the scroll view.
- [scrollsToTop](scrollstotop.md) — A Boolean value that controls whether the scroll-to-top gesture is enabled.
- [bouncesHorizontally](bounceshorizontally.md) — A Boolean value that determines whether the scroll view bounces when it reaches the ends of its horizontal axis.
- [bouncesVertically](bouncesvertically.md) — A Boolean value that determines whether the scroll view bounces when it reaches the ends of its vertical axis.
- [alwaysBounceVertical](alwaysbouncevertical.md) — A Boolean value that determines whether bouncing always occurs when vertical scrolling reaches the end of the content.
- [alwaysBounceHorizontal](alwaysbouncehorizontal.md) — A Boolean value that determines whether bouncing always occurs when horizontal scrolling reaches the end of the content view.
