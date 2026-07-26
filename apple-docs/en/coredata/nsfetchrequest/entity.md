---
title: entity
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchrequest/entity
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequest/entity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequest/entity.json'
content_hash: 'sha256:81e6bf7c9d6657ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchRequest](../nsfetchrequest.md)

# entity

<sub>Instance Property</sub>

The entity specified for the fetch request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var entity: NSEntityDescription? { get set }
```

## Discussion

When an [NSFetchRequest](../nsfetchrequest.md) instance is created with `init()`, it is expected that the [entity](../nspropertydescription/entity.md) property will be set.  If this property is not set, the fetch request fails upon execution.

## See Also

### Managing the Fetch Request’s Entity

- [+ fetchRequestWithEntityName:](<init(entityname_)-5anoo.md>) — Returns a fetch request configured with a given entity name.
- [- init](<init().md>) — Creates a new fetch request.
- [entityName](entityname.md) — The name of the entity the request is configured to fetch.
- [includesSubentities](includessubentities.md) — A Boolean value that indicates whether the fetch request includes subentities in the results.
- [NSFetchRequestResultType](../nsfetchrequestresulttype.md) — Constants that specify the possible result types a fetch request can return.
