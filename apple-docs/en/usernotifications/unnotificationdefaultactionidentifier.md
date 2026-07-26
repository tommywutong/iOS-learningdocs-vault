---
title: UNNotificationDefaultActionIdentifier
framework: User Notifications
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationdefaultactionidentifier
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationdefaultactionidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationdefaultactionidentifier.json'
content_hash: 'sha256:2d88a68267bb8e45'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNNotificationDefaultActionIdentifier

<sub>Global Variable</sub>

An action that indicates the user opened the app from the notification interface.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
let UNNotificationDefaultActionIdentifier: String
```

## Discussion

The delivery of this action doesn’t require any special configuration of notification categories. Use the [- userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:](<unusernotificationcenterdelegate/usernotificationcenter(__didreceive_withcompletionhandler_).md>) method of your delegate object to receive this action.

## See Also

### Getting the Response Information

- [actionIdentifier](unnotificationresponse/actionidentifier.md) — The identifier string of the action that the user selected.
- [notification](unnotificationresponse/notification.md) — The notification to which the user responded.
- [targetScene](unnotificationresponse/targetscene.md) — The scene where the system reflects the user’s response to a notification.
- [UNNotificationDismissActionIdentifier](unnotificationdismissactionidentifier.md) — The action that indicates the user explicitly dismissed the notification interface.
