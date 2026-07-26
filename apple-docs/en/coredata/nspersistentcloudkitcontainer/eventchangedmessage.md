---
title: NSPersistentCloudKitContainer.EventChangedMessage
framework: Core Data
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/coredata/nspersistentcloudkitcontainer/eventchangedmessage
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/eventchangedmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcloudkitcontainer/eventchangedmessage.json'
content_hash: 'sha256:768e15bad28a00aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentCloudKitContainer](../nspersistentcloudkitcontainer.md)

# NSPersistentCloudKitContainer.EventChangedMessage

<sub>Structure</sub>

Posted when a CloudKit event occurs on the CloudKit private serial queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct EventChangedMessage
```

## Relationships

- **Conforms To**: [NotificationCenter.AsyncMessage](../../foundation/notificationcenter/asyncmessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [event](eventchangedmessage/event.md) — The CloudKit event that triggered this notification.
