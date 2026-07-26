---
title: hasAction
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（10.0 起废弃）, iPadOS 4.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, watchOS 2.0+（3.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilocalnotification/hasaction
source_url: 'https://developer.apple.com/documentation/uikit/uilocalnotification/hasaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilocalnotification/hasaction.json'
content_hash: 'sha256:c115535f6784e3a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILocalNotification](../uilocalnotification.md)

# hasAction

<sub>Instance Property</sub>

A Boolean value that controls whether the notification shows or hides the alert action.

> [!warning] Deprecated
> For more information, see [UILocalNotification](../uilocalnotification.md).

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
var hasAction: Bool { get set }
```

## Discussion

Assign [false](../../swift/false.md) to this property to hide the alert button or slider. (This effect requires [alertBody](alertbody.md) to be non-`nil`.) The default value is [true](../../swift/true.md).

## See Also

### Composing the alert

- [alertBody](alertbody.md) — The message displayed in the notification alert. _(deprecated)_
- [alertAction](alertaction.md) — The title of the action button or slider. _(deprecated)_
- [alertTitle](alerttitle.md) — A short description of the reason for the alert. _(deprecated)_
- [alertLaunchImage](alertlaunchimage.md) — Identifies the image used as the launch image when the user taps (or slides) the action button (or slider). _(deprecated)_
- [category](category.md) — The name of a group of actions to display in the alert. _(deprecated)_
