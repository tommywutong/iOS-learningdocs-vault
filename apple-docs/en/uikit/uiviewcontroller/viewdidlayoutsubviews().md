---
title: viewDidLayoutSubviews()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/viewdidlayoutsubviews()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/viewdidlayoutsubviews()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/viewdidlayoutsubviews%28%29.json'
content_hash: 'sha256:01a32863637adcd8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# viewDidLayoutSubviews()

<sub>Instance Method</sub>

Notifies the view controller when its view finishes laying out its subviews.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func viewDidLayoutSubviews()
```

## Discussion

When the bounds change for a view controller’s view, the view adjusts the positions of its subviews and then the system calls this method. However, this method being called _does not_ indicate that the individual layouts of the view’s subviews have been adjusted. Each subview is responsible for adjusting its own layout.

Your view controller can override this method to make changes after the view lays out its subviews. The default implementation of this method does nothing.

In iOS 18 and later, UIKit supports automatic trait tracking inside this method for traits from this view controller’s `traitCollection` and the `traitCollection` of its [view](view.md). For more information, see [Automatic trait tracking](../automatic-trait-tracking.md).

This method supports automatic observation tracking. For more information, see [Updating views automatically with observation tracking in UIKit](../updating-views-automatically-with-observation-tracking-in-uikit.md).

## See Also

### Observing data in view controllers

- [- updateProperties](<updateproperties().md>) — Configures the view controller’s content and styling properties.
- [- viewWillLayoutSubviews](<viewwilllayoutsubviews().md>) — Notifies the view controller that its view is about to lay out its subviews.
- [- updateViewConstraints](<updateviewconstraints().md>) — Notifies the view controller when its view needs to update its constraints.
- [updateContentUnavailableConfiguration(using:)](<updatecontentunavailableconfiguration(using_).md>) — Updates the content-unavailable configuration for the provided state.
