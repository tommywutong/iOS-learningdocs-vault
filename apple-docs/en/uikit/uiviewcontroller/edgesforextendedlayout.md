---
title: edgesForExtendedLayout
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/edgesforextendedlayout
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/edgesforextendedlayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/edgesforextendedlayout.json'
content_hash: 'sha256:30fbdcb0c74e50fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# edgesForExtendedLayout

<sub>Instance Property</sub>

The edges that you extend for your view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var edgesForExtendedLayout: UIRectEdge { get set }
```

## Discussion

Instead of this property, use the safe area of your view to determine which parts of your interface are occluded by other content. For more information, see the [safeAreaLayoutGuide](../uiview/safearealayoutguide.md) and [safeAreaInsets](../uiview/safeareainsets.md) properties of [UIView](../uiview.md).

In iOS 10 and earlier, use this property to report which edges of your view controller extend underneath navigation bars or other system-provided views. The default value of this property is [UIRectEdgeAll](../uirectedge/all.md), and it is recommended that you do not change that value.

If you remove an edge value from this property, the system does not lay out your content underneath other bars on that same edge. In addition, the system provides a default background so that translucent bars have an appropriate appearance. The window’s root view controller does not react to this property.

## See Also

### Configuring the view’s layout behavior

- [UIRectEdge](../uirectedge.md) — Constants that specify the edges of a rectangle.
- [extendedLayoutIncludesOpaqueBars](extendedlayoutincludesopaquebars.md) — A Boolean value indicating whether or not the extended layout includes opaque bars.
- [- viewWillLayoutSubviews](<viewwilllayoutsubviews().md>) — Notifies the view controller that its view is about to lay out its subviews.
- [- viewDidLayoutSubviews](<viewdidlayoutsubviews().md>) — Notifies the view controller when its view finishes laying out its subviews.
- [- updateViewConstraints](<updateviewconstraints().md>) — Notifies the view controller when its view needs to update its constraints.
