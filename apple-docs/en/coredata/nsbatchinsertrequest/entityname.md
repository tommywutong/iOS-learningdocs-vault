---
title: entityName
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsbatchinsertrequest/entityname
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchinsertrequest/entityname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchinsertrequest/entityname.json'
content_hash: 'sha256:9b33a02a9e3f06c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSBatchInsertRequest](../nsbatchinsertrequest.md)

# entityName

<sub>Instance Property</sub>

The name of the managed entity to insert data into.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var entityName: String { get }
```

## See Also

### Configuring a Request

- [dictionaryHandler](dictionaryhandler.md) — A closure that provides a dictionary for your app to insert data into.
- [entity](entity.md) — The managed entity to insert data into.
- [managedObjectHandler](managedobjecthandler.md) — A closure that provides a managed object for your app to insert data into.
- [objectsToInsert](objectstoinsert.md) — An array of dictionaries that represents the objects to insert with the keys as attribute names and their assigned values.
- [resultType](resulttype.md) — The type of result that Core Data returns from this request.
