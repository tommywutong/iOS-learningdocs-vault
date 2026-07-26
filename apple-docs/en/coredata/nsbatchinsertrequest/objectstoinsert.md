---
title: objectsToInsert
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsbatchinsertrequest/objectstoinsert
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchinsertrequest/objectstoinsert'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchinsertrequest/objectstoinsert.json'
content_hash: 'sha256:7bd1911f5e65b318'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSBatchInsertRequest](../nsbatchinsertrequest.md)

# objectsToInsert

<sub>Instance Property</sub>

An array of dictionaries that represents the objects to insert with the keys as attribute names and their assigned values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var objectsToInsert: [[String : Any]]? { get set }
```

## See Also

### Configuring a Request

- [dictionaryHandler](dictionaryhandler.md) — A closure that provides a dictionary for your app to insert data into.
- [entity](entity.md) — The managed entity to insert data into.
- [entityName](entityname.md) — The name of the managed entity to insert data into.
- [managedObjectHandler](managedobjecthandler.md) — A closure that provides a managed object for your app to insert data into.
- [resultType](resulttype.md) — The type of result that Core Data returns from this request.
