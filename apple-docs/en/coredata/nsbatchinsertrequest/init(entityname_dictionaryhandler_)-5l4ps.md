---
title: 'init(entityName:dictionaryHandler:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsbatchinsertrequest/init(entityname:dictionaryhandler:)-5l4ps'
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchinsertrequest/init(entityname:dictionaryhandler:)-5l4ps'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchinsertrequest/init%28entityname%3Adictionaryhandler%3A%29-5l4ps.json'
content_hash: 'sha256:c5e4741c5196c4af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSBatchInsertRequest](../nsbatchinsertrequest.md)

# init(entityName:dictionaryHandler:)

<sub>Initializer</sub>

Creates a batch-insertion request for a named managed entity, and specifies a closure that provides data dictionaries for insertion.

<sub>visionOS</sub>

```swift
convenience init(entityName: String, dictionaryHandler handler: @escaping (NSMutableDictionary) -> Bool)
```

## Parameters

- `entityName` — The name of the managed entity to insert data into.

- `handler` — A closure that provides a dictionary that represents an object to insert. The dictionary contains an attribute name key and a value.

## Return Value

A batch-insertion request.

## Discussion

Core Data repeatedly calls the provided closure until it returns `true`, then finishes the request and saves the data.

## See Also

### Creating a Request

- [- initWithEntity:dictionaryHandler:](<init(entity_dictionaryhandler_).md>) — Creates a batch-insertion request for a managed entity, and specifies a closure that provides data dictionaries for insertion.
- [- initWithEntity:managedObjectHandler:](<init(entity_managedobjecthandler_).md>) — Creates a batch-insertion request for a managed entity, and specifies a closure that inserts data into the entity.
- [+ batchInsertRequestWithEntityName:managedObjectHandler:](<init(entityname_managedobjecthandler_)-7dr6p.md>) — Creates a batch-insertion request for a named managed entity, and specifies a closure that inserts data into the entity.
- [- initWithEntity:objects:](<init(entity_objects_).md>) — Creates a batch-insertion request for a managed entity, and provides an array of data dictionaries for insertion.
- [- initWithEntityName:objects:](<init(entityname_objects_).md>) — Creates a batch-insertion request for a named managed entity, and provides an array of data dictionaries for insertion.
- [- init](<init().md>) — Creates a Core Data batch-insertion request. _(deprecated)_
