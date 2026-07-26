---
title: userInfo
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（10.0 起废弃）, iPadOS 4.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, watchOS 2.0+（3.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uilocalnotification/userinfo
source_url: 'https://developer.apple.com/documentation/uikit/uilocalnotification/userinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilocalnotification/userinfo.json'
content_hash: 'sha256:48ae45c10b9e392d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILocalNotification](../uilocalnotification.md)

# userInfo

<sub>Instance Property</sub>

A dictionary for passing custom information to the notified app.

> [!warning] Deprecated
> For more information, see [UILocalNotification](../uilocalnotification.md).

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
var userInfo: [AnyHashable : Any]? { get set }
```

## Discussion

You may add arbitrary key-value pairs to this dictionary. However, the keys and values must be valid [Property list](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44); if any are not, an exception is raised.

## See Also

### Configuring other parts of the notification

- [applicationIconBadgeNumber](applicationiconbadgenumber.md) — The number to display as the app’s icon badge. _(deprecated)_
- [soundName](soundname.md) — The name of the file containing the sound to play when an alert is displayed. _(deprecated)_
