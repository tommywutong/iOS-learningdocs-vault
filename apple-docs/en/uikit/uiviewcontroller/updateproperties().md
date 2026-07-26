---
title: updateProperties()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/updateproperties()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/updateproperties()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/updateproperties%28%29.json'
content_hash: 'sha256:2b12712d5bc7b171'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# updateProperties()

<sub>Instance Method</sub>

Configures the view controller’s content and styling properties.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func updateProperties()
```

## Overview

Override this method to configure the view’s content and styling in your view controller subclass. Don’t call this method directly; instead, call [- setNeedsUpdateProperties](<setneedsupdateproperties().md>) to schedule an update.

This method supports automatic observation tracking. For more information, see [Updating views automatically with observation tracking in UIKit](../updating-views-automatically-with-observation-tracking-in-uikit.md).

## See Also

### Observing data in view controllers

- [- viewWillLayoutSubviews](<viewwilllayoutsubviews().md>) — Notifies the view controller that its view is about to lay out its subviews.
- [- viewDidLayoutSubviews](<viewdidlayoutsubviews().md>) — Notifies the view controller when its view finishes laying out its subviews.
- [- updateViewConstraints](<updateviewconstraints().md>) — Notifies the view controller when its view needs to update its constraints.
- [updateContentUnavailableConfiguration(using:)](<updatecontentunavailableconfiguration(using_).md>) — Updates the content-unavailable configuration for the provided state.
