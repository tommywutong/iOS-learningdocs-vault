---
title: includesSubentities
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchrequest/includessubentities
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequest/includessubentities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequest/includessubentities.json'
content_hash: 'sha256:93772332d9102672'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchRequest](../nsfetchrequest.md)

# includesSubentities

<sub>Instance Property</sub>

A Boolean value that indicates whether the fetch request includes subentities in the results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var includesSubentities: Bool { get set }
```

## Discussion

The value is [true](../../swift/true.md) if the request will include all subentities of the entity for the request; otherwise it is [false](../../swift/false.md). The default is [true](../../swift/true.md).

## See Also

### Managing the Fetch Request’s Entity

- [+ fetchRequestWithEntityName:](<init(entityname_)-5anoo.md>) — Returns a fetch request configured with a given entity name.
- [- init](<init().md>) — Creates a new fetch request.
- [entityName](entityname.md) — The name of the entity the request is configured to fetch.
- [entity](entity.md) — The entity specified for the fetch request.
- [NSFetchRequestResultType](../nsfetchrequestresulttype.md) — Constants that specify the possible result types a fetch request can return.
