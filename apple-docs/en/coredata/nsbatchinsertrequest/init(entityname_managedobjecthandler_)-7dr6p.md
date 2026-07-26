---
title: 'init(entityName:managedObjectHandler:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsbatchinsertrequest/init(entityname:managedobjecthandler:)-7dr6p'
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchinsertrequest/init(entityname:managedobjecthandler:)-7dr6p'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchinsertrequest/init%28entityname%3Amanagedobjecthandler%3A%29-7dr6p.json'
content_hash: 'sha256:901f774aa241921a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSBatchInsertRequest](../nsbatchinsertrequest.md)

# init(entityName:managedObjectHandler:)

<sub>Initializer</sub>

Creates a batch-insertion request for a named managed entity, and specifies a closure that inserts data into the entity.

<sub>visionOS</sub>

```swift
convenience init(entityName: String, managedObjectHandler handler: @escaping (NSManagedObject) -> Bool)
```

## Parameters

- `entityName` — The name of the managed entity that defines the object to create.

- `handler` — A closure that inserts data into the managed entity.

## Return Value

A batch-insertion request.

## Discussion

Core Data repeatedly calls the provided closure until it returns `true`, then finishes the request and saves the data.

## See Also

### Creating a Request

- [- initWithEntity:dictionaryHandler:](<init(entity_dictionaryhandler_).md>) — Creates a batch-insertion request for a managed entity, and specifies a closure that provides data dictionaries for insertion.
- [- initWithEntity:managedObjectHandler:](<init(entity_managedobjecthandler_).md>) — Creates a batch-insertion request for a managed entity, and specifies a closure that inserts data into the entity.
- [+ batchInsertRequestWithEntityName:dictionaryHandler:](<init(entityname_dictionaryhandler_)-5l4ps.md>) — Creates a batch-insertion request for a named managed entity, and specifies a closure that provides data dictionaries for insertion.
- [- initWithEntity:objects:](<init(entity_objects_).md>) — Creates a batch-insertion request for a managed entity, and provides an array of data dictionaries for insertion.
- [- initWithEntityName:objects:](<init(entityname_objects_).md>) — Creates a batch-insertion request for a named managed entity, and provides an array of data dictionaries for insertion.
- [- init](<init().md>) — Creates a Core Data batch-insertion request. _(deprecated)_
