---
title: NSPersistentCloudKitContainerEventResult.ResultType
framework: Core Data
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentcloudkitcontainereventresult/resulttype-swift.enum
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainereventresult/resulttype-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcloudkitcontainereventresult/resulttype-swift.enum.json'
content_hash: 'sha256:dbf97242a18c8e86'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentCloudKitContainerEventResult](../nspersistentcloudkitcontainereventresult.md)

# NSPersistentCloudKitContainerEventResult.ResultType

<sub>Enumeration</sub>

The types of results from a persistent CloudKit container event fetch request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum ResultType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Result Types

- [NSPersistentCloudKitContainerEventResultTypeEvents](resulttype-swift.enum/events.md) — The persistent CloudKit container events that match the event request.
- [NSPersistentCloudKitContainerEventResultTypeCountEvents](resulttype-swift.enum/countevents.md) — The number of CloudKit container events that match the event request.

### Initializers

- [init(rawValue:)](<resulttype-swift.enum/init(rawvalue_).md>)

## See Also

### Handling Event Results

- [result](result.md) — The result of the persistent CloudKit container event request, which the result type determines.
- [resultType](resulttype-swift.property.md) — The type of result that the CloudKit container event fetch request returns.
