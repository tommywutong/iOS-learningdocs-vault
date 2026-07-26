---
title: 'dismiss(animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintinteractioncontroller/dismiss(animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/dismiss(animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontroller/dismiss%28animated%3A%29.json'
content_hash: 'sha256:7ef1902688801f96'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionController](../uiprintinteractioncontroller.md)

# dismiss(animated:)

<sub>Instance Method</sub>

Dismisses the printing-options sheet or popover.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func dismiss(animated: Bool)
```

## Parameters

- `animated` — [true](../../swift/true.md) to animate the dismissal, otherwise [false](../../swift/false.md).

## Discussion

You should dismiss the printing options when they are presented in a sheet or animated from a rectangle _and_ the user changes the orientation of the device. (This, of course, assumes your application responds to orientation changes.) You should then present the printing options again once the new orientation takes effect. You can observe the [UIApplicationWillChangeStatusBarOrientationNotification](../uiapplication/willchangestatusbarorientationnotification.md) notification to find out when the device orientation is about to change.

## See Also

### Presenting the printing user interface

- [- presentAnimated:completionHandler:](<present(animated_completionhandler_).md>) — Presents the iPhone printing user interface in a sheet, optionally animating it to slide up from the bottom of the screen.
- [- presentFromBarButtonItem:animated:completionHandler:](<present(from_animated_completionhandler_).md>) — Presents the iPad printing user interface in a popover view, optionally animating it from a bar-button item.
- [- presentFromRect:inView:animated:completionHandler:](<present(from_in_animated_completionhandler_).md>) — Presents the iPad printing user interface in a popover view, optionally animating it from any area in a view.
