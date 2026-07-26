---
title: EAAccessoryDidDisconnect
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/eaaccessorydiddisconnect
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/eaaccessorydiddisconnect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/eaaccessorydiddisconnect.json'
content_hash: 'sha256:4944078441e7c5a3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# EAAccessoryDidDisconnect

<sub>Type Property</sub>

A notification that is posted when an accessory is disconnected and no longer available for your application to use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let EAAccessoryDidDisconnect: NSNotification.Name
```

## Discussion

The notification object is the shared accessory manager. The `userInfo` dictionary contains an [EAAccessoryKey](../../../externalaccessory/eaaccessorykey.md), whose value is the [EAAccessory](../../../externalaccessory/eaaccessory.md) object representing the accessory that was disconnected. Before delivery of this notification can occur, you must call the [registerForLocalNotifications()](<../../../externalaccessory/eaaccessorymanager/registerforlocalnotifications().md>) method to let the system know you are interested in receiving this notification.

If your accessory manager has a delegate, the delegate can use the [accessoryDidDisconnect(_:)](<../../../externalaccessory/eaaccessorydelegate/accessorydiddisconnect(__).md>) method to receive this notification instead.

## See Also

### External Accessory

- [EAAccessoryDidConnect](eaaccessorydidconnect.md) — A notification that the system sends when an accessory becomes connected and available for your application to use.
