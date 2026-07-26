---
title: ProcessInfo.PowerStateDidChangeMessage
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/powerstatedidchangemessage
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/powerstatedidchangemessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/powerstatedidchangemessage.json'
content_hash: 'sha256:830d43fc335a7d5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# ProcessInfo.PowerStateDidChangeMessage

<sub>Structure</sub>

A message the system sends when the device’s power state changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PowerStateDidChangeMessage
```

## Overview

After your observer receives this notification, query the [lowPowerModeEnabled](islowpowermodeenabled.md) property to determine the current power state of the device. If Low Power Mode is active, take appropriate steps to reduce activity in your app. Otherwise, your app can resume normal operations.

Observe this message with the identifier [powerStateDidChange](../notificationcenter/messageidentifier/powerstatedidchange.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [Subject](../notificationcenter/mainactormessage/subject.md) of this message type is [ProcessInfo](../processinfo.md).

This message interoperates with the notification [NSProcessInfoPowerStateDidChangeNotification](../nsnotification/name-swift.struct/nsprocessinfopowerstatedidchange.md). The system notifies observers of the message when the [NotificationCenter](../notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Relationships

- **Conforms To**: [AsyncMessage](../notificationcenter/asyncmessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a message

- [init()](<powerstatedidchangemessage/init().md>) — Creates a message about a power state change.

## See Also

### Working with notification messsages

- [ThermalStateDidChangeMessage](thermalstatedidchangemessage.md) — A message the system sends when the device’s thermal state changes.
