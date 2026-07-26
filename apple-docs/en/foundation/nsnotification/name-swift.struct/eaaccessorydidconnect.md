---
title: EAAccessoryDidConnect
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/eaaccessorydidconnect
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/eaaccessorydidconnect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/eaaccessorydidconnect.json'
content_hash: 'sha256:a442f89c7a0f1242'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# EAAccessoryDidConnect

<sub>Type Property</sub>

A notification that the system sends when an accessory becomes connected and available for your application to use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let EAAccessoryDidConnect: NSNotification.Name
```

## Discussion

The notification object is the shared accessory manager. The `userInfo` dictionary contains an [EAAccessoryKey](../../../externalaccessory/eaaccessorykey.md), whose value is an [EAAccessory](../../../externalaccessory/eaaccessory.md) object representing the accessory that is now connected. If a Bluetooth accessory was selected by the user in the Bluetooth picker, this dictionary contains the [EAAccessorySelectedKey](../../../externalaccessory/eaaccessoryselectedkey.md) key. Before delivery of this notification can occur, you must call the [registerForLocalNotifications()](<../../../externalaccessory/eaaccessorymanager/registerforlocalnotifications().md>) method to let the system know you are interested in receiving this notification.

After receiving this notification, always check the [protocolStrings](../../../externalaccessory/eaaccessory/protocolstrings.md) array of the newly connected accessory object to verify that the required protocol is present before trying to open a session. In some cases, the system may send the connection notification before authentication has completed, resulting in an empty [protocolStrings](../../../externalaccessory/eaaccessory/protocolstrings.md) array and a subsequent disconnection message. If this happens, the system sends another connection message later, when authentication succeeds.

> [!important] Important
> iPhone and iPad apps running on Macs with Apple silicon never receive this notification.

## See Also

### External Accessory

- [EAAccessoryDidDisconnect](eaaccessorydiddisconnect.md) — A notification that is posted when an accessory is disconnected and no longer available for your application to use.
