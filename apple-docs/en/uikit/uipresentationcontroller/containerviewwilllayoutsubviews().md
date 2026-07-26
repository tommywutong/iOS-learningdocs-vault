---
title: containerViewWillLayoutSubviews()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipresentationcontroller/containerviewwilllayoutsubviews()
source_url: 'https://developer.apple.com/documentation/uikit/uipresentationcontroller/containerviewwilllayoutsubviews()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipresentationcontroller/containerviewwilllayoutsubviews%28%29.json'
content_hash: 'sha256:b4c5923c7cd16d8f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPresentationController](../uipresentationcontroller.md)

# containerViewWillLayoutSubviews()

<sub>Instance Method</sub>

Notifies the presentation controller that layout is about to begin on the views of the container view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func containerViewWillLayoutSubviews()
```

## Discussion

UIKit calls this method before adjusting the layout of the views in the container view. Use this method and the [- containerViewDidLayoutSubviews](<containerviewdidlayoutsubviews().md>) method to update any custom views managed by your presentation controller.

In iOS 18 and later, UIKit supports automatic trait tracking inside this method for traits from this presentation controller’s `traitCollection` and the `traitCollection` of its [containerView](containerview.md). For more information, see [Automatic trait tracking](../automatic-trait-tracking.md).

This method supports automatic observation tracking. For more information, see [Updating views automatically with observation tracking in UIKit](../updating-views-automatically-with-observation-tracking-in-uikit.md).

## See Also

### Observing data in presentation controllers

- [- containerViewDidLayoutSubviews](<containerviewdidlayoutsubviews().md>) — Notifies the presentation controller when layout ends on the views of the container view.
