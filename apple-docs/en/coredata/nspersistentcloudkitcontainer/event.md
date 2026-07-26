---
title: NSPersistentCloudKitContainer.Event
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentcloudkitcontainer/event
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/event'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcloudkitcontainer/event.json'
content_hash: 'sha256:6575220bcf450070'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentCloudKitContainer](../nspersistentcloudkitcontainer.md)

# NSPersistentCloudKitContainer.Event

<sub>Class</sub>

An object that represents activity in a persistent CloudKit container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Event
```

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSCopying](../../foundation/nscopying.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Inspecting Event Properties

- [type](event/type.md) — The type of event, either setup, import, or export.
- [identifier](event/identifier.md) — A unique identifier for the event in a container.
- [storeIdentifier](event/storeidentifier.md) — The associated store identifier in the container for the event.
- [succeeded](event/succeeded.md) — A Boolean value that indicates whether the operation the event represents is successful.
- [startDate](event/startdate.md) — The start date of the operation that the event represents.
- [endDate](event/enddate.md) — The end date of the operation that the event represents.
- [error](event/error.md) — An error that indicates why an operation fails.

## See Also

### Monitoring Container Events

- [EventType](eventtype.md) — The type of event in a persistent CloudKit container, either setup, import, or export.
- [NSPersistentCloudKitContainerEventRequest](../nspersistentcloudkitcontainereventrequest.md) — A request to fetch setup, import, or export events in a persistent CloudKit container.
- [NSPersistentCloudKitContainerEventResult](../nspersistentcloudkitcontainereventresult.md) — The result of a request to fetch persistent CloudKit container events.
- [NSPersistentCloudKitContainerEventChangedNotification](eventchangednotification.md) — A notification that contains details about an event in a persistent CloudKit container.
- [NSPersistentCloudKitContainerEventUserInfoKey](eventnotificationuserinfokey.md) — The user info dictionary key for the persistent CloudKit container event.
