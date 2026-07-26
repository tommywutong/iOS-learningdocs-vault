---
title: NSCoreDataCoreSpotlightDelegate.IndexDidUpdateMessage
framework: Core Data
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/coredata/nscoredatacorespotlightdelegate/indexdidupdatemessage
source_url: 'https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/indexdidupdatemessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nscoredatacorespotlightdelegate/indexdidupdatemessage.json'
content_hash: 'sha256:b39999fc2781469d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSCoreDataCoreSpotlightDelegate](../nscoredatacorespotlightdelegate.md)

# NSCoreDataCoreSpotlightDelegate.IndexDidUpdateMessage

<sub>Structure</sub>

Posted when the Core Spotlight index is updated on a private queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct IndexDidUpdateMessage
```

## Relationships

- **Conforms To**: [NotificationCenter.AsyncMessage](../../foundation/notificationcenter/asyncmessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [historyToken](indexdidupdatemessage/historytoken.md) — The persistent history token representing the index state.
- [storeUUID](indexdidupdatemessage/storeuuid.md) — The UUID of the store that was indexed.
