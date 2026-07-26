---
title: 'present(animated:completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintinteractioncontroller/present(animated:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/present(animated:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontroller/present%28animated%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:725e20877eedfb16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionController](../uiprintinteractioncontroller.md)

# present(animated:completionHandler:)

<sub>Instance Method</sub>

Presents the iPhone printing user interface in a sheet, optionally animating it to slide up from the bottom of the screen.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func present(animated: Bool, completionHandler completion: UIPrintInteractionController.CompletionHandler? = nil) -> Bool
```

## Parameters

- `animated` — [true](../../swift/true.md) to animate the display of the sheet, [false](../../swift/false.md) to display the sheet immediately.

- `completion` — A block of type [CompletionHandler](completionhandler.md) that you implement to handle the conclusion of the print job (for instance, to reset state) and to handle any errors encountered in printing.

## Discussion

It is valid to call this method for applications on iPhone and iPod touch devices. Calling this method on an iPad with `animated` set to [true](../../swift/true.md) causes the printing options view to animate from the window frame.

If you call this method when the printing options are already displayed, `UIPrintInteractionController` hides the printing-options sheet. You must call the method again to display the options.

## See Also

### Presenting the printing user interface

- [- presentFromBarButtonItem:animated:completionHandler:](<present(from_animated_completionhandler_).md>) — Presents the iPad printing user interface in a popover view, optionally animating it from a bar-button item.
- [- presentFromRect:inView:animated:completionHandler:](<present(from_in_animated_completionhandler_).md>) — Presents the iPad printing user interface in a popover view, optionally animating it from any area in a view.
- [- dismissAnimated:](<dismiss(animated_).md>) — Dismisses the printing-options sheet or popover.
