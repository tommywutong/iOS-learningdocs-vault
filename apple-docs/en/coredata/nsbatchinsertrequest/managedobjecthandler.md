---
title: managedObjectHandler
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsbatchinsertrequest/managedobjecthandler
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchinsertrequest/managedobjecthandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchinsertrequest/managedobjecthandler.json'
content_hash: 'sha256:77d0c40e436e389b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSBatchInsertRequest](../nsbatchinsertrequest.md)

# managedObjectHandler

<sub>Instance Property</sub>

A closure that provides a managed object for your app to insert data into.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var managedObjectHandler: ((NSManagedObject) -> Bool)? { get set }
```

## See Also

### Configuring a Request

- [dictionaryHandler](dictionaryhandler.md) — A closure that provides a dictionary for your app to insert data into.
- [entity](entity.md) — The managed entity to insert data into.
- [entityName](entityname.md) — The name of the managed entity to insert data into.
- [objectsToInsert](objectstoinsert.md) — An array of dictionaries that represents the objects to insert with the keys as attribute names and their assigned values.
- [resultType](resulttype.md) — The type of result that Core Data returns from this request.
