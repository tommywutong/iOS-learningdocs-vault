---
title: NSPersistentCloudKitContainer.EventType
framework: Core Data
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentcloudkitcontainer/eventtype
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/eventtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcloudkitcontainer/eventtype.json'
content_hash: 'sha256:da55b2e530e65c75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentCloudKitContainer](../nspersistentcloudkitcontainer.md)

# NSPersistentCloudKitContainer.EventType

<sub>Enumeration</sub>

The type of event in a persistent CloudKit container, either setup, import, or export.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum EventType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Event Types

- [NSPersistentCloudKitContainerEventTypeSetup](eventtype/setup.md) — An event the persistent CloudKit container generates when setting up a store.
- [NSPersistentCloudKitContainerEventTypeImport](eventtype/import.md) — An event the persistent CloudKit container generates when importing records into a store.
- [NSPersistentCloudKitContainerEventTypeExport](eventtype/export.md) — An event the persistent CloudKit container generates when exporting managed objects from a store.

### Initializers

- [init(rawValue:)](<eventtype/init(rawvalue_).md>)

## See Also

### Monitoring Container Events

- [Event](event.md) — An object that represents activity in a persistent CloudKit container.
- [NSPersistentCloudKitContainerEventRequest](../nspersistentcloudkitcontainereventrequest.md) — A request to fetch setup, import, or export events in a persistent CloudKit container.
- [NSPersistentCloudKitContainerEventResult](../nspersistentcloudkitcontainereventresult.md) — The result of a request to fetch persistent CloudKit container events.
- [NSPersistentCloudKitContainerEventChangedNotification](eventchangednotification.md) — A notification that contains details about an event in a persistent CloudKit container.
- [NSPersistentCloudKitContainerEventUserInfoKey](eventnotificationuserinfokey.md) — The user info dictionary key for the persistent CloudKit container event.
