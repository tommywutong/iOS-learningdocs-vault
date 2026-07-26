---
title: extendedLayoutIncludesOpaqueBars
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/extendedlayoutincludesopaquebars
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/extendedlayoutincludesopaquebars'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/extendedlayoutincludesopaquebars.json'
content_hash: 'sha256:eb6533123ec7bd52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# extendedLayoutIncludesOpaqueBars

<sub>Instance Property</sub>

A Boolean value indicating whether or not the extended layout includes opaque bars.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var extendedLayoutIncludesOpaqueBars: Bool { get set }
```

## Discussion

The default value of this property is [false](../../swift/false.md).

> [!note] Note
> Bars are translucent by default in iOS 7.0

## See Also

### Configuring the view’s layout behavior

- [edgesForExtendedLayout](edgesforextendedlayout.md) — The edges that you extend for your view controller.
- [UIRectEdge](../uirectedge.md) — Constants that specify the edges of a rectangle.
- [- viewWillLayoutSubviews](<viewwilllayoutsubviews().md>) — Notifies the view controller that its view is about to lay out its subviews.
- [- viewDidLayoutSubviews](<viewdidlayoutsubviews().md>) — Notifies the view controller when its view finishes laying out its subviews.
- [- updateViewConstraints](<updateviewconstraints().md>) — Notifies the view controller when its view needs to update its constraints.
