---
title: EKEventStoreChangedNotification
framework: EventKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.8+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/eventkit/ekeventstorechangednotification
source_url: 'https://developer.apple.com/documentation/eventkit/ekeventstorechangednotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/eventkit/ekeventstorechangednotification.json'
content_hash: 'sha256:bece42b0f085f3e3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [EventKit](../eventkit.md)

# EKEventStoreChangedNotification

<sub>Global Variable</sub>

A notification posted when changes are made to the Calendar database.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```objc
extern NSString * const EKEventStoreChangedNotification;
```

## Discussion

This notification is posted whenever changes are made to the Calendar database, including adding, removing, and changing events or reminders. Individual changes are not described. When you receive this notification, you should refetch all [EKEvent](ekevent.md) and [EKReminder](ekreminder.md) objects you have accessed, as they are considered stale.

If you are actively editing an event and do not wish to refetch it unless it is absolutely necessary to do so, you can call the refresh method on it. If the method returns `true`, you do not need to refetch the event.

> [!note] Note
> The system posts this notification on the main actor.
