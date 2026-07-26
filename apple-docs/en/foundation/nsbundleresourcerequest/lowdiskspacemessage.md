---
title: NSBundleResourceRequest.LowDiskSpaceMessage
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+（27.0 起废弃）, iPadOS 26.0+（27.0 起废弃）, Mac Catalyst 26.0+（27.0 起废弃）, tvOS 26.0+（27.0 起废弃）, visionOS 26.0+（27.0 起废弃）, watchOS 26.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsbundleresourcerequest/lowdiskspacemessage
source_url: 'https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/lowdiskspacemessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbundleresourcerequest/lowdiskspacemessage.json'
content_hash: 'sha256:4e4d7b13e0ceb6f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSBundleResourceRequest](../nsbundleresourcerequest.md)

# NSBundleResourceRequest.LowDiskSpaceMessage

<sub>Structure</sub>

A message the system sends when it detects the amount of available disk space getting low.

> [!warning] Deprecated
> Use Background Assets instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct LowDiskSpaceMessage
```

## Overview

After receiving this notification, your app should release any on-demand resources that aren’t required. Call [- endAccessingResources](<endaccessingresources().md>) to release the managed resources. If the app is in the background and the app doesn’t free up enough space, the system may terminate the app.

Observe this message with the identifier [lowDiskSpace](../notificationcenter/messageidentifier/lowdiskspace.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [Subject](../notificationcenter/mainactormessage/subject.md) of this message type is [NSBundleResourceRequest](../nsbundleresourcerequest.md).

This message interoperates with the notification [NSBundleResourceRequestLowDiskSpaceNotification](../nsnotification/name-swift.struct/nsbundleresourcerequestlowdiskspace.md). The system notifies observers of the message when the [NotificationCenter](../notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Relationships

- **Conforms To**: [AsyncMessage](../notificationcenter/asyncmessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a message

- [init()](<lowdiskspacemessage/init().md>) — Creates a message about the available disk space getting low. _(deprecated)_
