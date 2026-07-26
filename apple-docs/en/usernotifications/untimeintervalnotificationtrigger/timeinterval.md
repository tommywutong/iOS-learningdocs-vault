---
title: timeInterval
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/untimeintervalnotificationtrigger/timeinterval
source_url: 'https://developer.apple.com/documentation/usernotifications/untimeintervalnotificationtrigger/timeinterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/untimeintervalnotificationtrigger/timeinterval.json'
content_hash: 'sha256:b24a3bf89d3ac441'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNTimeIntervalNotificationTrigger](../untimeintervalnotificationtrigger.md)

# timeInterval

<sub>Instance Property</sub>

The time interval to create the trigger.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var timeInterval: TimeInterval { get }
```

## Discussion

This property contains the original time interval that you specified when creating the trigger object. The value in this property isn’t updated as time counts down. To find out when the trigger will fire next, call the [- nextTriggerDate](<nexttriggerdate().md>) method.

## See Also

### Getting the Trigger Information

- [- nextTriggerDate](<nexttriggerdate().md>) — The next date at which the trigger conditions are met.
