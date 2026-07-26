---
title: 'setContentScrollView(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/setcontentscrollview(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/setcontentscrollview(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/setcontentscrollview%28_%3A%29.json'
content_hash: 'sha256:129d0be36a9ea998'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# setContentScrollView(_:)

<sub>Instance Method</sub>

Sets the scroll view that bars observe for all edges of the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func setContentScrollView(_ scrollView: UIScrollView?)
```

## Parameters

- `scrollView` — The scroll view to observe.

## Discussion

Calling this convenience method is identical to calling [- setContentScrollView:forEdge:](<setcontentscrollview(__for_).md>) and passing [NSDirectionalRectEdgeAll](../nsdirectionalrectedge/all.md) for the `edge` parameter.

## See Also

### Working with scrolling content

- [- setContentScrollView:forEdge:](<setcontentscrollview(__for_).md>) — Sets the scroll view that bars observe for the specified edge.
- [- contentScrollViewForEdge:](<contentscrollview(for_).md>) — Returns the scroll view the view controller observes for the specified edge.
