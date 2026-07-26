---
title: lowDiskSpace
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+（27.0 起废弃）, iPadOS 26.0+（27.0 起废弃）, Mac Catalyst 26.0+（27.0 起废弃）, tvOS 26.0+（27.0 起废弃）, visionOS 26.0+（27.0 起废弃）, watchOS 26.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/notificationcenter/messageidentifier/lowdiskspace
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/lowdiskspace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/messageidentifier/lowdiskspace.json'
content_hash: 'sha256:37f28f2d3ef6a16a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NotificationCenter](../../notificationcenter.md) · [MessageIdentifier](../messageidentifier.md)

# lowDiskSpace

<sub>Type Property</sub>

An identifier for a message about the available disk space getting low.

> [!warning] Deprecated
> Use Background Assets instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static var lowDiskSpace: NotificationCenter.BaseMessageIdentifier<NSBundleResourceRequest.LowDiskSpaceMessage> { get }
```

## Discussion

Use this identifier with [NotificationCenter](../../notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [LowDiskSpaceMessage](../../nsbundleresourcerequest/lowdiskspacemessage.md).
