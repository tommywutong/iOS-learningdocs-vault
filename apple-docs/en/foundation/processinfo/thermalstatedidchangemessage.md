---
title: ProcessInfo.ThermalStateDidChangeMessage
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/thermalstatedidchangemessage
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/thermalstatedidchangemessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/thermalstatedidchangemessage.json'
content_hash: 'sha256:e4b074309c7ac709'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# ProcessInfo.ThermalStateDidChangeMessage

<sub>Structure</sub>

A message the system sends when the device’s thermal state changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ThermalStateDidChangeMessage
```

## Overview

To observe this message, access the [thermalState](thermalstate-swift.property.md) property prior to adding your observer.

Observe this message with the identifier [thermalStateDidChange](../notificationcenter/messageidentifier/thermalstatedidchange.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [Subject](../notificationcenter/mainactormessage/subject.md) of this message type is [ProcessInfo](../processinfo.md).

This message interoperates with the notification [NSProcessInfoThermalStateDidChangeNotification](thermalstatedidchangenotification.md). The system notifies observers of the message when the [NotificationCenter](../notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Relationships

- **Conforms To**: [AsyncMessage](../notificationcenter/asyncmessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a message

- [init()](<thermalstatedidchangemessage/init().md>) — Creates a message about a thermal state change.

## See Also

### Working with notification messsages

- [PowerStateDidChangeMessage](powerstatedidchangemessage.md) — A message the system sends when the device’s power state changes.
