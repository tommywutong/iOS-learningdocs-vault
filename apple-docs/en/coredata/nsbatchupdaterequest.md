---
title: NSBatchUpdateRequest
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsbatchupdaterequest
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchupdaterequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchupdaterequest.json'
content_hash: 'sha256:e9518430f5913d86'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSBatchUpdateRequest

<sub>Class</sub>

A request to Core Data to do a batch update of data in a persistent store without loading any data into memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSBatchUpdateRequest
```

## Relationships

- **Inherits From**: [NSPersistentStoreRequest](nspersistentstorerequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a Request

- [- initWithEntity:](<nsbatchupdaterequest/init(entity_).md>) — Creates a batch-update request for a managed entity.
- [- initWithEntityName:](<nsbatchupdaterequest/init(entityname_).md>) — Creates a batch-update request for a named managed entity.

### Configuring a Request

- [entity](nsbatchupdaterequest/entity.md) — The managed entity to update data for.
- [entityName](nsbatchupdaterequest/entityname.md) — The name of the managed entity to update data for.
- [includesSubentities](nsbatchupdaterequest/includessubentities.md) — A Boolean value that indicates whether to update subentities.
- [predicate](nsbatchupdaterequest/predicate.md) — A predicate that identifies the objects to update.
- [propertiesToUpdate](nsbatchupdaterequest/propertiestoupdate.md) — A dictionary of property description pairs that describe the updates.
- [resultType](nsbatchupdaterequest/resulttype.md) — The type of result that Core Data returns from the request.

## See Also

### Data Updates

- [NSBatchUpdateResult](nsbatchupdateresult.md) — The result returned when executing a batch update request.
