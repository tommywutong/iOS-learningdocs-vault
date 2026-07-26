---
title: 'viewForZooming(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscrollviewdelegate/viewforzooming(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollviewdelegate/viewforzooming(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollviewdelegate/viewforzooming%28in%3A%29.json'
content_hash: 'sha256:239675517aecf80c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollViewDelegate](../uiscrollviewdelegate.md)

# viewForZooming(in:)

<sub>Instance Method</sub>

Asks the delegate for the view to scale when zooming is about to occur in the scroll view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func viewForZooming(in scrollView: UIScrollView) -> UIView?
```

## Parameters

- `scrollView` — The scroll-view object displaying the content view.

## Return Value

A [UIView](../uiview.md) object that will be scaled as a result of the zooming gesture. Return `nil` if you don’t want zooming to occur.

## See Also

### Managing zooming

- [- scrollViewWillBeginZooming:withView:](<scrollviewwillbeginzooming(__with_).md>) — Tells the delegate that zooming of the content in the scroll view is about to commence.
- [- scrollViewDidEndZooming:withView:atScale:](<scrollviewdidendzooming(__with_atscale_).md>) — Tells the delegate when zooming of the content in the scroll view completed.
- [- scrollViewDidZoom:](<scrollviewdidzoom(__).md>) — Tells the delegate that the scroll view’s zoom factor changed.
