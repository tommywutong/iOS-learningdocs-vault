---
title: region
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unlocationnotificationtrigger/region
source_url: 'https://developer.apple.com/documentation/usernotifications/unlocationnotificationtrigger/region'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unlocationnotificationtrigger/region.json'
content_hash: 'sha256:d9ab6dc05f8111db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNLocationNotificationTrigger](../unlocationnotificationtrigger.md)

# region

<sub>Instance Property</sub>

The region used to determine when the system sends the notification.

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
@NSCopying var region: CLRegion { get }
```

## Discussion

Use the [notifyOnEntry](../../corelocation/clregion/notifyonentry.md) and [notifyOnExit](../../corelocation/clregion/notifyonexit.md) properties of this region to specify whether the system sends notifications when the user enters or exits the specified geographic area.
