---
title: 'contentScrollView(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/contentscrollview(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/contentscrollview(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/contentscrollview%28for%3A%29.json'
content_hash: 'sha256:94c05d1eed9197e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# contentScrollView(for:)

<sub>Instance Method</sub>

Returns the scroll view the view controller observes for the specified edge.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func contentScrollView(for edge: NSDirectionalRectEdge) -> UIScrollView?
```

## Parameters

- `edge` — The edge the scroll view observes for alignment, [NSDirectionalRectEdgeTop](../nsdirectionalrectedge/top.md) or [NSDirectionalRectEdgeBottom](../nsdirectionalrectedge/bottom.md). Passing any other value raises an exception.

## Return Value

The scroll view the view controller observes for the edge.

## Discussion

Toolbars, navigation bars, and tab bars adjust their appearance when the edge of a scroll view’s content aligns with the edge of the bar. If you want to disable this behavior for one or more edges, override this method and return `nil` for the appropriate edge. If you don’t set a scroll view with [- setContentScrollView:forEdge:](<setcontentscrollview(__for_).md>) or [setContentScrollView(_:)](<setcontentscrollview(__).md>), the default implementation of this method returns `nil`.

The following example disables the scroll edge view for the top edge only. This example disables the appearance changes of the navigation bar at the top edge, but not the toolbar at the bottom edge.

```swift
override func contentScrollView(for edge: NSDirectionalRectEdge) -> UIScrollView? {
    if edge == .top {
        return nil
    } else {
        return super.contentScrollView(for: edge)
    }
}
```

## See Also

### Working with scrolling content

- [- setContentScrollView:forEdge:](<setcontentscrollview(__for_).md>) — Sets the scroll view that bars observe for the specified edge.
- [setContentScrollView(_:)](<setcontentscrollview(__).md>) — Sets the scroll view that bars observe for all edges of the view.
