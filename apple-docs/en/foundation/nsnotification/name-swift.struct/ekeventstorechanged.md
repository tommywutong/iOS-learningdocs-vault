---
title: EKEventStoreChanged
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.8+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/ekeventstorechanged
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/ekeventstorechanged'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/ekeventstorechanged.json'
content_hash: 'sha256:d0bc66b5df99b3e7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# EKEventStoreChanged

<sub>Type Property</sub>

A notification posted when changes are made to the Calendar database.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
static let EKEventStoreChanged: NSNotification.Name
```

## Discussion

This notification is posted whenever changes are made to the Calendar database, including adding, removing, and changing events or reminders. Individual changes are not described. When you receive this notification, you should refetch all [EKEvent](../../../eventkit/ekevent.md) and [EKReminder](../../../eventkit/ekreminder.md) objects you have accessed, as they are considered stale.

If you are actively editing an event and do not wish to refetch it unless it is absolutely necessary to do so, you can call the refresh method on it. If the method returns `true`, you do not need to refetch the event.

> [!note] Note
> The system posts this notification on the main actor.
