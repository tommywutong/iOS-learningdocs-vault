---
title: completionWithItemsHandler
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivityviewcontroller/completionwithitemshandler-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/completionwithitemshandler-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityviewcontroller/completionwithitemshandler-swift.property.json'
content_hash: 'sha256:3fddac5f51f5f716'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityViewController](../uiactivityviewcontroller.md)

# completionWithItemsHandler

<sub>Instance Property</sub>

The completion handler to execute after the activity view controller is dismissed.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var completionWithItemsHandler: UIActivityViewController.CompletionWithItemsHandler? { get set }
```

## Discussion

When the user-selected service finishes operating on the data, or when the user dismisses the view controller, the view controller executes this completion handler to let your app know the final result of the operation.

## See Also

### Accessing the completion handler

- [CompletionWithItemsHandler](completionwithitemshandler-swift.typealias.md) — A completion handler to execute after the activity view controller is dismissed.
