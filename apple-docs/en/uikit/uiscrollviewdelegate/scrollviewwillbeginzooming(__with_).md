---
title: 'scrollViewWillBeginZooming(_:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscrollviewdelegate/scrollviewwillbeginzooming(_:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/scrollviewwillbeginzooming(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollviewdelegate/scrollviewwillbeginzooming%28_%3Awith%3A%29.json'
content_hash: 'sha256:702f04320ecea7b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollViewDelegate](../uiscrollviewdelegate.md)

# scrollViewWillBeginZooming(_:with:)

<sub>Instance Method</sub>

Tells the delegate that zooming of the content in the scroll view is about to commence.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func scrollViewWillBeginZooming(_ scrollView: UIScrollView, with view: UIView?)
```

## Parameters

- `scrollView` — The scroll-view object displaying the content view.

- `view` — The view object whose content is about to be zoomed.

## Discussion

This method is called at the beginning of zoom gestures and in cases where a change in zoom level is to be animated. You can use this method to store state information or perform any additional actions prior to zooming the view’s content.

## See Also

### Managing zooming

- [- viewForZoomingInScrollView:](<viewforzooming(in_).md>) — Asks the delegate for the view to scale when zooming is about to occur in the scroll view.
- [- scrollViewDidEndZooming:withView:atScale:](<scrollviewdidendzooming(__with_atscale_).md>) — Tells the delegate when zooming of the content in the scroll view completed.
- [- scrollViewDidZoom:](<scrollviewdidzoom(__).md>) — Tells the delegate that the scroll view’s zoom factor changed.
