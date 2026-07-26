---
title: completionHandler
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+（8.0 起废弃）, iPadOS 6.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiactivityviewcontroller/completionhandler-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/completionhandler-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityviewcontroller/completionhandler-swift.property.json'
content_hash: 'sha256:eb502693d659d8ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityViewController](../uiactivityviewcontroller.md)

# completionHandler

<sub>Instance Property</sub>

The completion handler to execute after the activity view controller is dismissed.

> [!warning] Deprecated
> Use the [completionWithItemsHandler](completionwithitemshandler-swift.property.md) property instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var completionHandler: UIActivityViewController.CompletionHandler? { get set }
```

## Discussion

When the user-selected service finishes operating on the data, or when the user dismisses the view controller, the view controller executes this completion handler to let your app know the final result of the operation.

## See Also

### Deprecated

- [CompletionHandler](completionhandler-swift.typealias.md) — A completion handler to execute after the activity view controller is dismissed. _(deprecated)_
