---
title: containerViewDidLayoutSubviews()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipresentationcontroller/containerviewdidlayoutsubviews()
source_url: 'https://developer.apple.com/documentation/uikit/uipresentationcontroller/containerviewdidlayoutsubviews()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipresentationcontroller/containerviewdidlayoutsubviews%28%29.json'
content_hash: 'sha256:bda3d75283ded61e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPresentationController](../uipresentationcontroller.md)

# containerViewDidLayoutSubviews()

<sub>Instance Method</sub>

Notifies the presentation controller when layout ends on the views of the container view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func containerViewDidLayoutSubviews()
```

## Discussion

UIKit calls this method after adjusting the layout of the views in the container view. Use this method to make any additional changes to the view hierarchy.

In iOS 18 and later, UIKit supports automatic trait tracking inside this method for traits from this presentation controller’s `traitCollection` and the `traitCollection` of its [containerView](containerview.md). For more information, see [Automatic trait tracking](../automatic-trait-tracking.md).

This method supports automatic observation tracking. For more information, see [Updating views automatically with observation tracking in UIKit](../updating-views-automatically-with-observation-tracking-in-uikit.md).

## See Also

### Observing data in presentation controllers

- [- containerViewWillLayoutSubviews](<containerviewwilllayoutsubviews().md>) — Notifies the presentation controller that layout is about to begin on the views of the container view.
