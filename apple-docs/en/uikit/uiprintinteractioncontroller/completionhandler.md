---
title: UIPrintInteractionController.CompletionHandler
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintinteractioncontroller/completionhandler
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller/completionhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontroller/completionhandler.json'
content_hash: 'sha256:c3f51f7285c7cc31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionController](../uiprintinteractioncontroller.md)

# UIPrintInteractionController.CompletionHandler

<sub>Type Alias</sub>

A completion handler for responding to the completion of a print job or for handling printing errors.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
typealias CompletionHandler = (UIPrintInteractionController, Bool, (any Error)?) -> Void
```

## Discussion

You implement this block as the final argument of [- presentAnimated:completionHandler:](<present(animated_completionhandler_).md>), [- presentFromBarButtonItem:animated:completionHandler:](<present(from_animated_completionhandler_).md>), or [- presentFromRect:inView:animated:completionHandler:](<present(from_in_animated_completionhandler_).md>). When a print job concludes, you can reset any state set up for printing and do related housekeeping tasks. If the print job encountered an error, it is likely to be a programming error, so you might want to log the error for debugging purposes.

- **`printInteractionController`** — The shared instance of `UIPrintInteractionController` that is managing the print job.
- **`completed`** — A Boolean value that indicates whether the print job completed successfully.
- **`error`** — An instance of the [NSError](../../foundation/nserror.md) that contains information about the printing error. The printing domain is [UIPrintErrorDomain](../uiprinterrordomain.md). The printing error codes are described in `UIKit Printing Error Codes`. If the print job completes successfully, this parameter is `nil`.

## See Also

### Printing directly to a printer

- [- printToPrinter:completionHandler:](<print(to_completionhandler_).md>) — Prints directly to the specified printer.
