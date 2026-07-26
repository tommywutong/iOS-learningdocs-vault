---
title: 'init(entityName:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsfetchrequest/init(entityname:)-5anoo'
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequest/init(entityname:)-5anoo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequest/init%28entityname%3A%29-5anoo.json'
content_hash: 'sha256:753c6d66c9a860ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchRequest](../nsfetchrequest.md)

# init(entityName:)

<sub>Initializer</sub>

Returns a fetch request configured with a given entity name.

<sub>visionOS</sub>

```swift
convenience init(entityName: String)
```

## Parameters

- `entityName` — The name of the entity to fetch.

## Return Value

A fetch request configured to fetch the entity named `entityName`.

## Discussion

This method provides a convenient way to configure the entity for a fetch request without having to retrieve an [NSEntityDescription](../nsentitydescription.md) object. When the fetch is executed, the request uses the managed object context to find the entity with the given name. The model associated with the context’s persistent store coordinator must contain an entity named `entityName`.

## See Also

### Related Documentation

- [Predicate Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html#//apple_ref/doc/uid/TP40001789)
- [Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)

### Managing the Fetch Request’s Entity

- [- init](<init().md>) — Creates a new fetch request.
- [entityName](entityname.md) — The name of the entity the request is configured to fetch.
- [entity](entity.md) — The entity specified for the fetch request.
- [includesSubentities](includessubentities.md) — A Boolean value that indicates whether the fetch request includes subentities in the results.
- [NSFetchRequestResultType](../nsfetchrequestresulttype.md) — Constants that specify the possible result types a fetch request can return.
