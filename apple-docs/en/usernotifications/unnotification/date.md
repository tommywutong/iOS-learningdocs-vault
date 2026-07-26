---
title: date
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotification/date
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotification/date'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotification/date.json'
content_hash: 'sha256:9cdd1af261f2eea7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotification](../unnotification.md)

# date

<sub>Instance Property</sub>

The delivery date of the notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var date: Date { get }
```

## Discussion

The system displays this date to the user in Notification Center.

## See Also

### Getting the Notification Details

- [request](request.md) — The notification request containing the payload and trigger condition for the notification.
