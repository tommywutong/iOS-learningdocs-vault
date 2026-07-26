---
title: 'present(from:in:animated:completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintinteractioncontroller/present(from:in:animated:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/present(from:in:animated:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontroller/present%28from%3Ain%3Aanimated%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:1cdc473db0632377'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionController](../uiprintinteractioncontroller.md)

# present(from:in:animated:completionHandler:)

<sub>Instance Method</sub>

Presents the iPad printing user interface in a popover view, optionally animating it from any area in a view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func present(from rect: CGRect, in view: UIView, animated: Bool, completionHandler completion: UIPrintInteractionController.CompletionHandler? = nil) -> Bool
```

## Parameters

- `rect` — A rectangle that defines the area from which the printing popover view is animated.

- `view` — The view providing the coordinate system for `rect`.

- `animated` — [true](../../swift/true.md) to animate the printing popover view from `item`, [false](../../swift/false.md) to display it immediately.

- `completion` — A block of type [CompletionHandler](completionhandler.md) that you implement to handle the conclusion of the print job (for instance, to reset state) and to handle any errors encountered in printing.

## Discussion

It is valid to call this method for applications on iPad devices. Calling this method on an iPhone or iPod touch with `animated` set to [true](../../swift/true.md) causes the printing options view to animate upward from the bottom of the screen.

If you call this method when the printing options are already displayed, `UIPrintInteractionController` hides the printing-options popover view. You must call the method again to display the options.

## See Also

### Presenting the printing user interface

- [- presentAnimated:completionHandler:](<present(animated_completionhandler_).md>) — Presents the iPhone printing user interface in a sheet, optionally animating it to slide up from the bottom of the screen.
- [- presentFromBarButtonItem:animated:completionHandler:](<present(from_animated_completionhandler_).md>) — Presents the iPad printing user interface in a popover view, optionally animating it from a bar-button item.
- [- dismissAnimated:](<dismiss(animated_).md>) — Dismisses the printing-options sheet or popover.
