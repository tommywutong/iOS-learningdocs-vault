---
title: UNNotificationPresentationOptionNone
framework: User Notifications
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationpresentationoptionnone
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationpresentationoptionnone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationpresentationoptionnone.json'
content_hash: 'sha256:f47d2ffd0460ec44'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [User Notifications](../usernotifications.md)

# UNNotificationPresentationOptionNone

<sub>Global Variable</sub>

No alert.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
static const UNNotificationPresentationOptions UNNotificationPresentationOptionNone;
```

## Discussion

Specify this constant when you want to silence any user interactions for a notification.

## See Also

### Receiving Notifications

- [- userNotificationCenter:willPresentNotification:withCompletionHandler:](<unusernotificationcenterdelegate/usernotificationcenter(__willpresent_withcompletionhandler_).md>) — Asks the delegate how to handle a notification that arrived while the app was running in the foreground.
- [UNNotificationPresentationOptions](unnotificationpresentationoptions.md) — Constants indicating how to present a notification in a foreground app.
