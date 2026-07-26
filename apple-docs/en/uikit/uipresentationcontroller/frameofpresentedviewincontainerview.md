---
title: frameOfPresentedViewInContainerView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipresentationcontroller/frameofpresentedviewincontainerview
source_url: 'https://developer.apple.com/documentation/uikit/uipresentationcontroller/frameofpresentedviewincontainerview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipresentationcontroller/frameofpresentedviewincontainerview.json'
content_hash: 'sha256:9d2248d20ff0b51e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPresentationController](../uipresentationcontroller.md)

# frameOfPresentedViewInContainerView

<sub>Instance Property</sub>

The frame rectangle to assign to the presented view at the end of the animations.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var frameOfPresentedViewInContainerView: CGRect { get }
```

## Return Value

The rectangle of the presented view controller’s view, specified in the container view’s coordinate system.

## Discussion

The default implementation of this method returns the frame rectangle of the container view, which results in the presented view controller’s content occupying the entire presentation space. You can override this method and return a different frame rectangle as needed. For example, you might specify a smaller frame rectangle if you want some of the underlying content to show around the edges of the presented view.

UIKit calls this method multiple times during the course of a presentation, so your implementation should return the same frame rectangle each time. Do not use this method to make changes to your view hierarchy or perform other one-time tasks.

## See Also

### Adjusting the size and layout of the presentation

- [- containerViewWillLayoutSubviews](<containerviewwilllayoutsubviews().md>) — Notifies the presentation controller that layout is about to begin on the views of the container view.
- [- containerViewDidLayoutSubviews](<containerviewdidlayoutsubviews().md>) — Notifies the presentation controller when layout ends on the views of the container view.
