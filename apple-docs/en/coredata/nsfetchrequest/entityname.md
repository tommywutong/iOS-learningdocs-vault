---
title: entityName
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchrequest/entityname
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequest/entityname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequest/entityname.json'
content_hash: 'sha256:f7a3f3cb672c48b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchRequest](../nsfetchrequest.md)

# entityName

<sub>Instance Property</sub>

The name of the entity the request is configured to fetch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var entityName: String? { get }
```

## Discussion

The entity name property is populated whenever the NSFetchRequest is created with `NSFetchRequest/init(entityName:)` or [+ fetchRequestWithEntityName:](<init(entityname_)-5anoo.md>).

## See Also

### Managing the Fetch Request’s Entity

- [+ fetchRequestWithEntityName:](<init(entityname_)-5anoo.md>) — Returns a fetch request configured with a given entity name.
- [- init](<init().md>) — Creates a new fetch request.
- [entity](entity.md) — The entity specified for the fetch request.
- [includesSubentities](includessubentities.md) — A Boolean value that indicates whether the fetch request includes subentities in the results.
- [NSFetchRequestResultType](../nsfetchrequestresulttype.md) — Constants that specify the possible result types a fetch request can return.
