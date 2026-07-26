---
title: alertBody
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（10.0 起废弃）, iPadOS 4.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, watchOS 2.0+（3.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilocalnotification/alertbody
source_url: 'https://developer.apple.com/documentation/uikit/uilocalnotification/alertbody'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilocalnotification/alertbody.json'
content_hash: 'sha256:d7c4361e8556ebd2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILocalNotification](../uilocalnotification.md)

# alertBody

<sub>Instance Property</sub>

The message displayed in the notification alert.

> [!warning] Deprecated
> For more information, see [UILocalNotification](../uilocalnotification.md).

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
var alertBody: String? { get set }
```

## Discussion

Assign a string or, preferably, a localized-string key (using [NSLocalizedString](../../foundation/nslocalizedstring.md)) as the value of the message. If the value of this property is non-`nil`, an alert is displayed. The default value is `nil` (no alert). Printf style escape characters are stripped from the string prior to display; to include a percent symbol (%) in the message, use two percent symbols (%%).

## See Also

### Composing the alert

- [alertAction](alertaction.md) — The title of the action button or slider. _(deprecated)_
- [alertTitle](alerttitle.md) — A short description of the reason for the alert. _(deprecated)_
- [hasAction](hasaction.md) — A Boolean value that controls whether the notification shows or hides the alert action. _(deprecated)_
- [alertLaunchImage](alertlaunchimage.md) — Identifies the image used as the launch image when the user taps (or slides) the action button (or slider). _(deprecated)_
- [category](category.md) — The name of a group of actions to display in the alert. _(deprecated)_
