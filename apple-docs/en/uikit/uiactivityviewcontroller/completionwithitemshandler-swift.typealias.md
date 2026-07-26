---
title: UIActivityViewController.CompletionWithItemsHandler
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivityviewcontroller/completionwithitemshandler-swift.typealias
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/completionwithitemshandler-swift.typealias'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityviewcontroller/completionwithitemshandler-swift.typealias.json'
content_hash: 'sha256:9f99b8e7ff517ae5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityViewController](../uiactivityviewcontroller.md)

# UIActivityViewController.CompletionWithItemsHandler

<sub>Type Alias</sub>

A completion handler to execute after the activity view controller is dismissed.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
typealias CompletionWithItemsHandler = (UIActivity.ActivityType?, Bool, [Any]?, (any Error)?) -> Void
```

## Discussion

Upon the completion of an activity, or the dismissal of the activity view controller, the view controller’s completion block is executed. You can use this block to execute any final code related to the service. The parameters of this block are as follows:

- **activityType** — The type of the service that was selected by the user. For custom services, this is the value returned by the [activityType](../uiactivity/activitytype-swift.property.md) method of a [UIActivity](../uiactivity.md) object. For system-defined activities, it is one of the strings listed in “Built-in Activity Types” in [UIActivity](../uiactivity.md).
- **completed** — [true](../../swift/true.md) if the service was performed or [false](../../swift/false.md) if it was not. This parameter is also set to [false](../../swift/false.md) when the user dismisses the view controller without selecting a service.
- **returnedItems** — An array of [NSExtensionItem](../../foundation/nsextensionitem.md) objects containing any modified data. Use the items in this array to get any changes made to the original data by an extension. If no items were modified, the value of this parameter is `nil`.
- **activityError** — An error object if the activity failed to complete, or `nil` if the the activity completed normally.

## See Also

### Accessing the completion handler

- [completionWithItemsHandler](completionwithitemshandler-swift.property.md) — The completion handler to execute after the activity view controller is dismissed.
