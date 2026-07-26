---
title: UIActivityViewController.CompletionHandler
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiactivityviewcontroller/completionhandler-swift.typealias
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityviewcontroller/completionhandler-swift.typealias'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityviewcontroller/completionhandler-swift.typealias.json'
content_hash: 'sha256:de9e4caf0551724d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityViewController](../uiactivityviewcontroller.md)

# UIActivityViewController.CompletionHandler

<sub>Type Alias</sub>

A completion handler to execute after the activity view controller is dismissed.

> [!warning] Deprecated
> Use [CompletionWithItemsHandler](completionwithitemshandler-swift.typealias.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
typealias CompletionHandler = (UIActivity.ActivityType?, Bool) -> Void
```

## Discussion

Upon the completion of an activity, or the dismissal of the activity view controller, the view controller’s completion block is executed. You can use this block to execute any final code related to the service. The parameters of this block are as follows:

- **activityType** — The type of the service that was selected by the user. For custom services, this is the value returned by the [activityType](../uiactivity/activitytype-swift.property.md) method of a [UIActivity](../uiactivity.md) object. For system-defined activities, it is one of the strings listed in “Built-in Activity Types” in [UIActivity](../uiactivity.md).
- **completed** — [true](../../swift/true.md) if the service was performed or [false](../../swift/false.md) if it was not. This parameter is also set to [false](../../swift/false.md) when the user dismisses the view controller without selecting a service.

## See Also

### Deprecated

- [completionHandler](completionhandler-swift.property.md) — The completion handler to execute after the activity view controller is dismissed. _(deprecated)_
