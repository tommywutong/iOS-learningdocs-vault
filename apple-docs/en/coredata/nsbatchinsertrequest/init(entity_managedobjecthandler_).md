---
title: 'init(entity:managedObjectHandler:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsbatchinsertrequest/init(entity:managedobjecthandler:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchinsertrequest/init(entity:managedobjecthandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchinsertrequest/init%28entity%3Amanagedobjecthandler%3A%29.json'
content_hash: 'sha256:3956dbe9eea2ba85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSBatchInsertRequest](../nsbatchinsertrequest.md)

# init(entity:managedObjectHandler:)

<sub>Initializer</sub>

Creates a batch-insertion request for a managed entity, and specifies a closure that inserts data into the entity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(entity: NSEntityDescription, managedObjectHandler handler: @escaping (NSManagedObject) -> Bool)
```

## Parameters

- `entity` — A managed entity to insert data into.

- `handler` — A closure that inserts data into the managed entity.

## Return Value

A batch-insertion request.

## Discussion

Core Data repeatedly calls the provided closure until it returns `true`, then finishes the request and saves the data.

## See Also

### Creating a Request

- [- initWithEntity:dictionaryHandler:](<init(entity_dictionaryhandler_).md>) — Creates a batch-insertion request for a managed entity, and specifies a closure that provides data dictionaries for insertion.
- [+ batchInsertRequestWithEntityName:dictionaryHandler:](<init(entityname_dictionaryhandler_)-5l4ps.md>) — Creates a batch-insertion request for a named managed entity, and specifies a closure that provides data dictionaries for insertion.
- [+ batchInsertRequestWithEntityName:managedObjectHandler:](<init(entityname_managedobjecthandler_)-7dr6p.md>) — Creates a batch-insertion request for a named managed entity, and specifies a closure that inserts data into the entity.
- [- initWithEntity:objects:](<init(entity_objects_).md>) — Creates a batch-insertion request for a managed entity, and provides an array of data dictionaries for insertion.
- [- initWithEntityName:objects:](<init(entityname_objects_).md>) — Creates a batch-insertion request for a named managed entity, and provides an array of data dictionaries for insertion.
- [- init](<init().md>) — Creates a Core Data batch-insertion request. _(deprecated)_
