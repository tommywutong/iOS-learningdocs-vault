---
title: identifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uimutableusernotificationaction/identifier
source_url: 'https://developer.apple.com/documentation/uikit/uimutableusernotificationaction/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimutableusernotificationaction/identifier.json'
content_hash: 'sha256:8f2e2a48ebd97542'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMutableUserNotificationAction](../uimutableusernotificationaction.md)

# identifier

<sub>Instance Property</sub>

The string that you use internally to identify the action.

> [!warning] Deprecated
> For more information, see [UIMutableUserNotificationAction](../uimutableusernotificationaction.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var identifier: String? { get set }
```

## Discussion

The system passes this string to the [- application:handleActionWithIdentifier:forLocalNotification:completionHandler:](<../uiapplicationdelegate/application(__handleactionwithidentifier_for_completionhandler_).md>) or [- application:handleActionWithIdentifier:forRemoteNotification:completionHandler:](<../uiapplicationdelegate/application(__handleactionwithidentifier_forremotenotification_completionhandler_).md>) method of the app delegate when the user chooses the action.

## See Also

### Getting the action information

- [title](title.md) — The localized string to use as the button title for the action. _(deprecated)_
