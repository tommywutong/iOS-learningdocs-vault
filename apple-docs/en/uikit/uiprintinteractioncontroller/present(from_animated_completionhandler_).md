---
title: 'present(from:animated:completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintinteractioncontroller/present(from:animated:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/present(from:animated:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontroller/present%28from%3Aanimated%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:5b02c4bd50c068da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionController](../uiprintinteractioncontroller.md)

# present(from:animated:completionHandler:)

<sub>Instance Method</sub>

Presents the iPad printing user interface in a popover view, optionally animating it from a bar-button item.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func present(from item: UIBarButtonItem, animated: Bool, completionHandler completion: UIPrintInteractionController.CompletionHandler? = nil) -> Bool
```

## Parameters

- `item` — The [UIBarButtonItem](../uibarbuttonitem.md) object that the user tapped for printing. You are encouraged to use the constant [UIBarButtonSystemItemAction](../uibarbuttonitem/systemitem/action.md) when creating a bar-button item for this purpose.

- `animated` — [true](../../swift/true.md) to animate the printing popover view from `item`, [false](../../swift/false.md) to display it immediately.

- `completion` — A block of type [CompletionHandler](completionhandler.md) that you implement to handle the conclusion of the print job (for instance, to reset state) and to handle any errors encountered in printing.

## Discussion

It is valid to call this method for applications on iPad devices. Calling this method on an iPhone or iPod touch with `animated` set to [true](../../swift/true.md) causes the printing options view to animate upward from the bottom of the screen.

If you call this method when the printing options are already displayed, `UIPrintInteractionController` hides the printing-options popover view. You must call the method again to display the options.

## See Also

### Presenting the printing user interface

- [- presentAnimated:completionHandler:](<present(animated_completionhandler_).md>) — Presents the iPhone printing user interface in a sheet, optionally animating it to slide up from the bottom of the screen.
- [- presentFromRect:inView:animated:completionHandler:](<present(from_in_animated_completionhandler_).md>) — Presents the iPad printing user interface in a popover view, optionally animating it from any area in a view.
- [- dismissAnimated:](<dismiss(animated_).md>) — Dismisses the printing-options sheet or popover.
