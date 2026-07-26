---
title: 'scrollViewDidEndZooming(_:with:atScale:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscrollviewdelegate/scrollviewdidendzooming(_:with:atscale:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/scrollviewdidendzooming(_:with:atscale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollviewdelegate/scrollviewdidendzooming%28_%3Awith%3Aatscale%3A%29.json'
content_hash: 'sha256:c6ae21469269b817'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollViewDelegate](../uiscrollviewdelegate.md)

# scrollViewDidEndZooming(_:with:atScale:)

<sub>Instance Method</sub>

Tells the delegate when zooming of the content in the scroll view completed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func scrollViewDidEndZooming(_ scrollView: UIScrollView, with view: UIView?, atScale scale: CGFloat)
```

## Parameters

- `scrollView` — The scroll-view object displaying the content view.

- `view` — The view object representing that part of the content view that needs to be scaled.

- `scale` — The scale factor to use for scaling; this value must be between the limits established by the `UIScrollView` properties [maximumZoomScale](../uiscrollview/maximumzoomscale.md) and [minimumZoomScale](../uiscrollview/minimumzoomscale.md).

## Discussion

The scroll view also calls this method after any “bounce” animations. It also calls this method after animated changes to the zoom level and after a zoom-related gesture ends (regardless of whether the gesture resulted in a change to the zoom level).

## See Also

### Managing zooming

- [- viewForZoomingInScrollView:](<viewforzooming(in_).md>) — Asks the delegate for the view to scale when zooming is about to occur in the scroll view.
- [- scrollViewWillBeginZooming:withView:](<scrollviewwillbeginzooming(__with_).md>) — Tells the delegate that zooming of the content in the scroll view is about to commence.
- [- scrollViewDidZoom:](<scrollviewdidzoom(__).md>) — Tells the delegate that the scroll view’s zoom factor changed.
