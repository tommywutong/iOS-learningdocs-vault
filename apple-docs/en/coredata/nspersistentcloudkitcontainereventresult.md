---
title: NSPersistentCloudKitContainerEventResult
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentcloudkitcontainereventresult
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainereventresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcloudkitcontainereventresult.json'
content_hash: 'sha256:09b2a020999125f7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentCloudKitContainerEventResult

<sub>Class</sub>

The result of a request to fetch persistent CloudKit container events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSPersistentCloudKitContainerEventResult
```

## Relationships

- **Inherits From**: [NSPersistentStoreResult](nspersistentstoreresult.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Handling Event Results

- [result](nspersistentcloudkitcontainereventresult/result.md) — The result of the persistent CloudKit container event request, which the result type determines.
- [resultType](nspersistentcloudkitcontainereventresult/resulttype-swift.property.md) — The type of result that the CloudKit container event fetch request returns.
- [ResultType](nspersistentcloudkitcontainereventresult/resulttype-swift.enum.md) — The types of results from a persistent CloudKit container event fetch request.

## See Also

### Monitoring Container Events

- [Event](nspersistentcloudkitcontainer/event.md) — An object that represents activity in a persistent CloudKit container.
- [EventType](nspersistentcloudkitcontainer/eventtype.md) — The type of event in a persistent CloudKit container, either setup, import, or export.
- [NSPersistentCloudKitContainerEventRequest](nspersistentcloudkitcontainereventrequest.md) — A request to fetch setup, import, or export events in a persistent CloudKit container.
- [NSPersistentCloudKitContainerEventChangedNotification](nspersistentcloudkitcontainer/eventchangednotification.md) — A notification that contains details about an event in a persistent CloudKit container.
- [NSPersistentCloudKitContainerEventUserInfoKey](nspersistentcloudkitcontainer/eventnotificationuserinfokey.md) — The user info dictionary key for the persistent CloudKit container event.
