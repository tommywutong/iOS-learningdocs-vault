---
title: alertTitle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.2+（10.0 起废弃）, iPadOS 8.2+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, watchOS 2.0+（3.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilocalnotification/alerttitle
source_url: 'https://developer.apple.com/documentation/uikit/uilocalnotification/alerttitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilocalnotification/alerttitle.json'
content_hash: 'sha256:87a31f5a36382533'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILocalNotification](../uilocalnotification.md)

# alertTitle

<sub>Instance Property</sub>

A short description of the reason for the alert.

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
var alertTitle: String? { get set }
```

## Discussion

Use this property to provide a short description of the reason for the alert. You may specify a string with the text you want to display or you may specify a string to use as a lookup key in your app’s `Localizable.strings` file. The default value of this property is `nil`.

Title strings should be short, usually only a couple of words describing the reason for the notification. Apple Watch displays the title string as part of the short look notification interface, which has limited space.

## See Also

### Composing the alert

- [alertBody](alertbody.md) — The message displayed in the notification alert. _(deprecated)_
- [alertAction](alertaction.md) — The title of the action button or slider. _(deprecated)_
- [hasAction](hasaction.md) — A Boolean value that controls whether the notification shows or hides the alert action. _(deprecated)_
- [alertLaunchImage](alertlaunchimage.md) — Identifies the image used as the launch image when the user taps (or slides) the action button (or slider). _(deprecated)_
- [category](category.md) — The name of a group of actions to display in the alert. _(deprecated)_
