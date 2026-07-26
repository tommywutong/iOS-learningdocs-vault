---
title: 'updateContentUnavailableConfiguration(using:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/updatecontentunavailableconfiguration(using:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/updatecontentunavailableconfiguration(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/updatecontentunavailableconfiguration%28using%3A%29.json'
content_hash: 'sha256:a457772afbe312c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# updateContentUnavailableConfiguration(using:)

<sub>Instance Method</sub>

Updates the content-unavailable configuration for the provided state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @objc(_bridgedUpdateContentUnavailableConfigurationUsingState:) @preconcurrency dynamic func updateContentUnavailableConfiguration(using state: UIContentUnavailableConfigurationState)
```

## Parameters

- `state` — The current configuration state for a content-unavailable view.

## Discussion

Override this method to update the value of [contentUnavailableConfiguration](contentunavailableconfiguration-4b95e.md) as appropriate for the given state.

Don’t call this method directly. Instead, call [- setNeedsUpdateContentUnavailableConfiguration](<setneedsupdatecontentunavailableconfiguration().md>) to tell the system to request an update.

In iOS 18 and later, UIKit supports automatic trait tracking inside this method for traits from this view controller’s `traitCollection` and the `traitCollection` of its [view](view.md). For more information, see [Automatic trait tracking](../automatic-trait-tracking.md).

This method supports automatic observation tracking. For more information, see [Updating views automatically with observation tracking in UIKit](../updating-views-automatically-with-observation-tracking-in-uikit.md).

## See Also

### Observing data in view controllers

- [- updateProperties](<updateproperties().md>) — Configures the view controller’s content and styling properties.
- [- viewWillLayoutSubviews](<viewwilllayoutsubviews().md>) — Notifies the view controller that its view is about to lay out its subviews.
- [- viewDidLayoutSubviews](<viewdidlayoutsubviews().md>) — Notifies the view controller when its view finishes laying out its subviews.
- [- updateViewConstraints](<updateviewconstraints().md>) — Notifies the view controller when its view needs to update its constraints.
