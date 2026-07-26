---
title: EAAccessoryDidDisconnectNotification
framework: External Accessory
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/externalaccessory/eaaccessorydiddisconnectnotification
source_url: 'https://developer.apple.com/documentation/externalaccessory/eaaccessorydiddisconnectnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/externalaccessory/eaaccessorydiddisconnectnotification.json'
content_hash: 'sha256:e090ec3f2d2b8921'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [External Accessory](../externalaccessory.md)

# EAAccessoryDidDisconnectNotification

<sub>Global Variable</sub>

A notification that is posted when an accessory is disconnected and no longer available for your application to use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
extern NSString * const EAAccessoryDidDisconnectNotification;
```

## Discussion

The notification object is the shared accessory manager. The `userInfo` dictionary contains an [EAAccessoryKey](eaaccessorykey.md), whose value is the [EAAccessory](eaaccessory.md) object representing the accessory that was disconnected. Before delivery of this notification can occur, you must call the [- registerForLocalNotifications](<eaaccessorymanager/registerforlocalnotifications().md>) method to let the system know you are interested in receiving this notification.

If your accessory manager has a delegate, the delegate can use the [- accessoryDidDisconnect:](<eaaccessorydelegate/accessorydiddisconnect(__).md>) method to receive this notification instead.

## See Also

### Managing Connection Status Changes

- [- registerForLocalNotifications](<eaaccessorymanager/registerforlocalnotifications().md>) — Begins the delivery of accessory-related notifications to the current application.
- [- unregisterForLocalNotifications](<eaaccessorymanager/unregisterforlocalnotifications().md>) — Stops the delivery of accessory-related notifications to the current application.
- [EAAccessoryDidConnectNotification](eaaccessorydidconnectnotification.md) — A notification that the system sends when an accessory becomes connected and available for your application to use.
- [EAAccessoryKey](eaaccessorykey.md) — A key that indicates the accessory object whose status changed.
- [EAAccessorySelectedKey](eaaccessoryselectedkey.md) — A key that indicates the accessory object that the user selected.
