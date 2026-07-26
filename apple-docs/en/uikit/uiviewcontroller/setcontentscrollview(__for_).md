---
title: 'setContentScrollView(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/setcontentscrollview(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/setcontentscrollview(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/setcontentscrollview%28_%3Afor%3A%29.json'
content_hash: 'sha256:5dc2dc5572e386ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# setContentScrollView(_:for:)

<sub>Instance Method</sub>

Sets the scroll view that bars observe for the specified edge.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setContentScrollView(_ scrollView: UIScrollView?, for edge: NSDirectionalRectEdge)
```

## Parameters

- `scrollView` — The scroll view to observe. If `nil`, the view controller determines a scroll view automatically.

- `edge` — The edge to observe for scroll view content alignment. Pass [NSDirectionalRectEdgeTop](../nsdirectionalrectedge/top.md) or [NSDirectionalRectEdgeBottom](../nsdirectionalrectedge/bottom.md) to set the scroll view for a specific edge, or pass [NSDirectionalRectEdgeAll](../nsdirectionalrectedge/all.md) to set the scroll view for all edges.

## Discussion

Toolbars, navigation bars, and tab bars adjust their appearance when the edge of a scroll view’s content aligns with the edge of the bar. The view controller identifies a scroll view to observe by analyzing the view hierarchy to select a scroll view. If the view hierarchy is complex, the view controller might not select the appropriate scroll view to observe. Use this method to indicate a specific scroll view for the view controller to observe.

To disable the scroll edge appearance for one or more edges, override [- contentScrollViewForEdge:](<contentscrollview(for_).md>).

## See Also

### Working with scrolling content

- [setContentScrollView(_:)](<setcontentscrollview(__).md>) — Sets the scroll view that bars observe for all edges of the view.
- [- contentScrollViewForEdge:](<contentscrollview(for_).md>) — Returns the scroll view the view controller observes for the specified edge.
