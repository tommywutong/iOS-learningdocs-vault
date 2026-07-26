---
title: NSBatchInsertRequest
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsbatchinsertrequest
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchinsertrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchinsertrequest.json'
content_hash: 'sha256:8812ff995ec186ef'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSBatchInsertRequest

<sub>Class</sub>

A request to insert a batch of data in a persistent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSBatchInsertRequest
```

## Relationships

- **Inherits From**: [NSPersistentStoreRequest](nspersistentstorerequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a Request

- [- initWithEntity:dictionaryHandler:](<nsbatchinsertrequest/init(entity_dictionaryhandler_).md>) — Creates a batch-insertion request for a managed entity, and specifies a closure that provides data dictionaries for insertion.
- [- initWithEntity:managedObjectHandler:](<nsbatchinsertrequest/init(entity_managedobjecthandler_).md>) — Creates a batch-insertion request for a managed entity, and specifies a closure that inserts data into the entity.
- [+ batchInsertRequestWithEntityName:dictionaryHandler:](<nsbatchinsertrequest/init(entityname_dictionaryhandler_)-5l4ps.md>) — Creates a batch-insertion request for a named managed entity, and specifies a closure that provides data dictionaries for insertion.
- [+ batchInsertRequestWithEntityName:managedObjectHandler:](<nsbatchinsertrequest/init(entityname_managedobjecthandler_)-7dr6p.md>) — Creates a batch-insertion request for a named managed entity, and specifies a closure that inserts data into the entity.
- [- initWithEntity:objects:](<nsbatchinsertrequest/init(entity_objects_).md>) — Creates a batch-insertion request for a managed entity, and provides an array of data dictionaries for insertion.
- [- initWithEntityName:objects:](<nsbatchinsertrequest/init(entityname_objects_).md>) — Creates a batch-insertion request for a named managed entity, and provides an array of data dictionaries for insertion.
- [- init](<nsbatchinsertrequest/init().md>) — Creates a Core Data batch-insertion request. _(deprecated)_

### Configuring a Request

- [dictionaryHandler](nsbatchinsertrequest/dictionaryhandler.md) — A closure that provides a dictionary for your app to insert data into.
- [entity](nsbatchinsertrequest/entity.md) — The managed entity to insert data into.
- [entityName](nsbatchinsertrequest/entityname.md) — The name of the managed entity to insert data into.
- [managedObjectHandler](nsbatchinsertrequest/managedobjecthandler.md) — A closure that provides a managed object for your app to insert data into.
- [objectsToInsert](nsbatchinsertrequest/objectstoinsert.md) — An array of dictionaries that represents the objects to insert with the keys as attribute names and their assigned values.
- [resultType](nsbatchinsertrequest/resulttype.md) — The type of result that Core Data returns from this request.

### Initializers

- [- initWithEntityName:dictionaryHandler:](<nsbatchinsertrequest/init(entityname_dictionaryhandler_)-74gtn.md>)
- [- initWithEntityName:managedObjectHandler:](<nsbatchinsertrequest/init(entityname_managedobjecthandler_)-2dgkw.md>)

## See Also

### Data Inserts

- [NSBatchInsertResult](nsbatchinsertresult.md) — The result that Core Data returns when executing a batch-insertion request.
