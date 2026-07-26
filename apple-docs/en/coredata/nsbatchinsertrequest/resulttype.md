---
title: resultType
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsbatchinsertrequest/resulttype
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchinsertrequest/resulttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchinsertrequest/resulttype.json'
content_hash: 'sha256:3fcc417b38f1caa3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSBatchInsertRequest](../nsbatchinsertrequest.md)

# resultType

<sub>Instance Property</sub>

The type of result that Core Data returns from this request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var resultType: NSBatchInsertRequestResultType { get set }
```

## Discussion

The default is [NSBatchInsertRequestResultTypeStatusOnly](../nsbatchinsertrequestresulttype/statusonly.md).

## See Also

### Configuring a Request

- [dictionaryHandler](dictionaryhandler.md) — A closure that provides a dictionary for your app to insert data into.
- [entity](entity.md) — The managed entity to insert data into.
- [entityName](entityname.md) — The name of the managed entity to insert data into.
- [managedObjectHandler](managedobjecthandler.md) — A closure that provides a managed object for your app to insert data into.
- [objectsToInsert](objectstoinsert.md) — An array of dictionaries that represents the objects to insert with the keys as attribute names and their assigned values.
