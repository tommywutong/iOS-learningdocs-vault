---
title: 'batchInsertRequestWithEntityName:objects:'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsbatchinsertrequest/batchinsertrequestwithentityname:objects:'
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchinsertrequest/batchinsertrequestwithentityname:objects:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchinsertrequest/batchinsertrequestwithentityname%3Aobjects%3A.json'
content_hash: 'sha256:ffd5befbf21c35bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSBatchInsertRequest](../nsbatchinsertrequest.md)

# batchInsertRequestWithEntityName:objects:

<sub>Type Method</sub>

Creates a batch-insertion request for a named managed entity, and provides an array of data dictionaries for insertion.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) batchInsertRequestWithEntityName:(NSString *) entityName objects:(NSArray<NSDictionary<NSString *,id> *> *) dictionaries;
```

## Parameters

- `entityName` — The name of a managed entity to insert data into.

- `dictionaries` — An array of dictionaries that represents the objects to insert. Each dictionary contains an attribute name key and a value.

## Return Value

A batch-insertion request.

## See Also

### Creating a Request

- [- initWithEntity:dictionaryHandler:](<init(entity_dictionaryhandler_).md>) — Creates a batch-insertion request for a managed entity, and specifies a closure that provides data dictionaries for insertion.
- [- initWithEntity:managedObjectHandler:](<init(entity_managedobjecthandler_).md>) — Creates a batch-insertion request for a managed entity, and specifies a closure that inserts data into the entity.
- [+ batchInsertRequestWithEntityName:dictionaryHandler:](<init(entityname_dictionaryhandler_)-5l4ps.md>) — Creates a batch-insertion request for a named managed entity, and specifies a closure that provides data dictionaries for insertion.
- [+ batchInsertRequestWithEntityName:managedObjectHandler:](<init(entityname_managedobjecthandler_)-7dr6p.md>) — Creates a batch-insertion request for a named managed entity, and specifies a closure that inserts data into the entity.
- [- initWithEntity:objects:](<init(entity_objects_).md>) — Creates a batch-insertion request for a managed entity, and provides an array of data dictionaries for insertion.
- [- initWithEntityName:objects:](<init(entityname_objects_).md>) — Creates a batch-insertion request for a named managed entity, and provides an array of data dictionaries for insertion.
- [- init](<init().md>) — Creates a Core Data batch-insertion request. _(deprecated)_
