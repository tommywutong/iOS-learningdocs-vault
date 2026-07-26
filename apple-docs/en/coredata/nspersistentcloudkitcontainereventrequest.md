---
title: NSPersistentCloudKitContainerEventRequest
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentcloudkitcontainereventrequest
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainereventrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcloudkitcontainereventrequest.json'
content_hash: 'sha256:5198976838df14b6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentCloudKitContainerEventRequest

<sub>Class</sub>

A request to fetch setup, import, or export events in a persistent CloudKit container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSPersistentCloudKitContainerEventRequest
```

## Relationships

- **Inherits From**: [NSPersistentStoreRequest](nspersistentstorerequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Fetching Events

- [+ fetchEventsAfterDate:](<nspersistentcloudkitcontainereventrequest/fetchevents(after_)-5izg7.md>) — Creates a fetch request for events after a specified date from a persistent CloudKit container.
- [+ fetchEventsAfterEvent:](<nspersistentcloudkitcontainereventrequest/fetchevents(after_)-3yfp.md>) — Creates a fetch request for events that occur after a specified event from a persistent CloudKit container.
- [+ fetchEventsMatchingFetchRequest:](<nspersistentcloudkitcontainereventrequest/fetchevents(matchingfetch_).md>) — Creates a fetch request for events that match a specified fetch request from a persistent CloudKit container.
- [+ fetchRequestForEvents](<nspersistentcloudkitcontainereventrequest/fetchforevents().md>) — Creates a fetch request for all events in a persistent CloudKit container.
- [resultType](nspersistentcloudkitcontainereventrequest/resulttype.md) — The type of result that the request returns.

## See Also

### Monitoring Container Events

- [Event](nspersistentcloudkitcontainer/event.md) — An object that represents activity in a persistent CloudKit container.
- [EventType](nspersistentcloudkitcontainer/eventtype.md) — The type of event in a persistent CloudKit container, either setup, import, or export.
- [NSPersistentCloudKitContainerEventResult](nspersistentcloudkitcontainereventresult.md) — The result of a request to fetch persistent CloudKit container events.
- [NSPersistentCloudKitContainerEventChangedNotification](nspersistentcloudkitcontainer/eventchangednotification.md) — A notification that contains details about an event in a persistent CloudKit container.
- [NSPersistentCloudKitContainerEventUserInfoKey](nspersistentcloudkitcontainer/eventnotificationuserinfokey.md) — The user info dictionary key for the persistent CloudKit container event.
