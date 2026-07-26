---
title: 'scrollViewDidZoom(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscrollviewdelegate/scrollviewdidzoom(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/scrollviewdidzoom(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollviewdelegate/scrollviewdidzoom%28_%3A%29.json'
content_hash: 'sha256:7ed5b06ef401a88d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollViewDelegate](../uiscrollviewdelegate.md)

# scrollViewDidZoom(_:)

<sub>Instance Method</sub>

Tells the delegate that the scroll view’s zoom factor changed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func scrollViewDidZoom(_ scrollView: UIScrollView)
```

## Parameters

- `scrollView` — The scroll-view object whose zoom factor changed.

## See Also

### Managing zooming

- [- viewForZoomingInScrollView:](<viewforzooming(in_).md>) — Asks the delegate for the view to scale when zooming is about to occur in the scroll view.
- [- scrollViewWillBeginZooming:withView:](<scrollviewwillbeginzooming(__with_).md>) — Tells the delegate that zooming of the content in the scroll view is about to commence.
- [- scrollViewDidEndZooming:withView:atScale:](<scrollviewdidendzooming(__with_atscale_).md>) — Tells the delegate when zooming of the content in the scroll view completed.
