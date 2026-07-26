---
title: eventChangedNotification
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentcloudkitcontainer/eventchangednotification
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/eventchangednotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcloudkitcontainer/eventchangednotification.json'
content_hash: 'sha256:573859404e8d4087'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentCloudKitContainer](../nspersistentcloudkitcontainer.md)

# eventChangedNotification

<sub>Type Property</sub>

A notification that contains details about an event in a persistent CloudKit container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let eventChangedNotification: NSNotification.Name
```

## See Also

### Monitoring Container Events

- [Event](event.md) — An object that represents activity in a persistent CloudKit container.
- [EventType](eventtype.md) — The type of event in a persistent CloudKit container, either setup, import, or export.
- [NSPersistentCloudKitContainerEventRequest](../nspersistentcloudkitcontainereventrequest.md) — A request to fetch setup, import, or export events in a persistent CloudKit container.
- [NSPersistentCloudKitContainerEventResult](../nspersistentcloudkitcontainereventresult.md) — The result of a request to fetch persistent CloudKit container events.
- [NSPersistentCloudKitContainerEventUserInfoKey](eventnotificationuserinfokey.md) — The user info dictionary key for the persistent CloudKit container event.
