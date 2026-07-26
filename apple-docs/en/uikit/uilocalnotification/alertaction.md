---
title: alertAction
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（10.0 起废弃）, iPadOS 4.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, watchOS 2.0+（3.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilocalnotification/alertaction
source_url: 'https://developer.apple.com/documentation/uikit/uilocalnotification/alertaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilocalnotification/alertaction.json'
content_hash: 'sha256:0ffd04a0dc707086'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILocalNotification](../uilocalnotification.md)

# alertAction

<sub>Instance Property</sub>

The title of the action button or slider.

> [!warning] Deprecated
> For more information, see [UILocalNotification](../uilocalnotification.md).

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
var alertAction: String? { get set }
```

## Discussion

Assign a string or, preferably, a localized-string key (using [NSLocalizedString](../../foundation/nslocalizedstring.md)) as the value. The alert action is the title of the right button of the alert or the value of the unlock slider, where the value replaces “unlock” in “slide to unlock”. If you specify `nil`, and [alertBody](alertbody.md) is non-`nil`, “View” (localized to the preferred language) is used as the default value.

## See Also

### Composing the alert

- [alertBody](alertbody.md) — The message displayed in the notification alert. _(deprecated)_
- [alertTitle](alerttitle.md) — A short description of the reason for the alert. _(deprecated)_
- [hasAction](hasaction.md) — A Boolean value that controls whether the notification shows or hides the alert action. _(deprecated)_
- [alertLaunchImage](alertlaunchimage.md) — Identifies the image used as the launch image when the user taps (or slides) the action button (or slider). _(deprecated)_
- [category](category.md) — The name of a group of actions to display in the alert. _(deprecated)_
