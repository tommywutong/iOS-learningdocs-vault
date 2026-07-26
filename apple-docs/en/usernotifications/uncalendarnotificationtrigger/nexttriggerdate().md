---
title: nextTriggerDate()
framework: User Notifications
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/uncalendarnotificationtrigger/nexttriggerdate()
source_url: 'https://developer.apple.com/documentation/usernotifications/uncalendarnotificationtrigger/nexttriggerdate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/uncalendarnotificationtrigger/nexttriggerdate%28%29.json'
content_hash: 'sha256:7918904becfcaca6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNCalendarNotificationTrigger](../uncalendarnotificationtrigger.md)

# nextTriggerDate()

<sub>Instance Method</sub>

The next date at which the trigger conditions are met.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nextTriggerDate() -> Date?
```

## Return Value

The next trigger date.

## Discussion

Use this property to find out when the system will deliver a notification associated with this trigger.

## See Also

### Getting the Trigger Information

- [dateComponents](datecomponents.md) — The date components to construct this object.
