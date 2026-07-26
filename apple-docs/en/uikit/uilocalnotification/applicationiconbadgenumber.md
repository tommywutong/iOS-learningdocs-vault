---
title: applicationIconBadgeNumber
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（10.0 起废弃）, iPadOS 4.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, watchOS 2.0+（3.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilocalnotification/applicationiconbadgenumber
source_url: 'https://developer.apple.com/documentation/uikit/uilocalnotification/applicationiconbadgenumber'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilocalnotification/applicationiconbadgenumber.json'
content_hash: 'sha256:9ff4195e480da78b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILocalNotification](../uilocalnotification.md)

# applicationIconBadgeNumber

<sub>Instance Property</sub>

The number to display as the app’s icon badge.

> [!warning] Deprecated
> For more information, see [UILocalNotification](../uilocalnotification.md).

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
var applicationIconBadgeNumber: Int { get set }
```

## Discussion

The default value of this property is 0, which means that no badge is displayed.

## See Also

### Configuring other parts of the notification

- [soundName](soundname.md) — The name of the file containing the sound to play when an alert is displayed. _(deprecated)_
- [userInfo](userinfo.md) — A dictionary for passing custom information to the notified app. _(deprecated)_
