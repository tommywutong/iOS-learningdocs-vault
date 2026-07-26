---
title: isDirectionalLockEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/isdirectionallockenabled
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/isdirectionallockenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/isdirectionallockenabled.json'
content_hash: 'sha256:f911ed6b9cfed86d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# isDirectionalLockEnabled

<sub>Instance Property</sub>

A Boolean value that determines whether scrolling is disabled in a particular direction.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isDirectionalLockEnabled: Bool { get set }
```

## Discussion

If this property is [false](../../swift/false.md), scrolling is permitted in both horizontal and vertical directions. If this property is [true](../../swift/true.md) and the user begins dragging in one general direction (horizontally or vertically), the scroll view disables scrolling in the other direction. If the drag direction is diagonal, then scrolling doesn’t lock and the user can drag in any direction until the drag completes. The default value is [false](../../swift/false.md).

## See Also

### Configuring the scroll view

- [scrollEnabled](isscrollenabled.md) — A Boolean value that determines whether scrolling is enabled.
- [pagingEnabled](ispagingenabled.md) — A Boolean value that determines whether paging is enabled for the scroll view.
- [scrollsToTop](scrollstotop.md) — A Boolean value that controls whether the scroll-to-top gesture is enabled.
- [bounces](bounces.md) — A Boolean value that controls whether the scroll view bounces past the edge of content and back again.
- [bouncesHorizontally](bounceshorizontally.md) — A Boolean value that determines whether the scroll view bounces when it reaches the ends of its horizontal axis.
- [bouncesVertically](bouncesvertically.md) — A Boolean value that determines whether the scroll view bounces when it reaches the ends of its vertical axis.
- [alwaysBounceVertical](alwaysbouncevertical.md) — A Boolean value that determines whether bouncing always occurs when vertical scrolling reaches the end of the content.
- [alwaysBounceHorizontal](alwaysbouncehorizontal.md) — A Boolean value that determines whether bouncing always occurs when horizontal scrolling reaches the end of the content view.
