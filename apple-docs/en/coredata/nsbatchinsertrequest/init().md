---
title: init()
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+（14.0 起废弃）, iPadOS 13.0+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, macOS 10.15+（11.0 起废弃）, tvOS 13.0+（14.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 6.0+（7.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/coredata/nsbatchinsertrequest/init()
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchinsertrequest/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchinsertrequest/init%28%29.json'
content_hash: 'sha256:6fcd9715c65286a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSBatchInsertRequest](../nsbatchinsertrequest.md)

# init()

<sub>Initializer</sub>

Creates a Core Data batch-insertion request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init()
```

## See Also

### Creating a Request

- [- initWithEntity:dictionaryHandler:](<init(entity_dictionaryhandler_).md>) — Creates a batch-insertion request for a managed entity, and specifies a closure that provides data dictionaries for insertion.
- [- initWithEntity:managedObjectHandler:](<init(entity_managedobjecthandler_).md>) — Creates a batch-insertion request for a managed entity, and specifies a closure that inserts data into the entity.
- [+ batchInsertRequestWithEntityName:dictionaryHandler:](<init(entityname_dictionaryhandler_)-5l4ps.md>) — Creates a batch-insertion request for a named managed entity, and specifies a closure that provides data dictionaries for insertion.
- [+ batchInsertRequestWithEntityName:managedObjectHandler:](<init(entityname_managedobjecthandler_)-7dr6p.md>) — Creates a batch-insertion request for a named managed entity, and specifies a closure that inserts data into the entity.
- [- initWithEntity:objects:](<init(entity_objects_).md>) — Creates a batch-insertion request for a managed entity, and provides an array of data dictionaries for insertion.
- [- initWithEntityName:objects:](<init(entityname_objects_).md>) — Creates a batch-insertion request for a named managed entity, and provides an array of data dictionaries for insertion.
