---
title: NSFetchRequestResultType
framework: Core Data
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchrequestresulttype
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchrequestresulttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchrequestresulttype.json'
content_hash: 'sha256:2f654566648248ce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSFetchRequestResultType

<sub>Structure</sub>

Constants that specify the possible result types a fetch request can return.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NSFetchRequestResultType
```

## Overview

These constants are used by [resultType](nsfetchrequest/resulttype.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Result Types

- [NSManagedObjectResultType](nsfetchrequestresulttype/managedobjectresulttype.md) — The request returns managed objects.
- [NSManagedObjectIDResultType](nsfetchrequestresulttype/managedobjectidresulttype.md) — The request returns managed object IDs.
- [NSDictionaryResultType](nsfetchrequestresulttype/dictionaryresulttype.md) — The request returns dictionaries.
- [NSCountResultType](nsfetchrequestresulttype/countresulttype.md) — The request returns the count of the objects that match the request.

### Initializers

- [init(rawValue:)](<nsfetchrequestresulttype/init(rawvalue_).md>) — Creates a fetch request result type using the specified raw value.

## See Also

### Managing the Fetch Request’s Entity

- [+ fetchRequestWithEntityName:](<nsfetchrequest/init(entityname_)-5anoo.md>) — Returns a fetch request configured with a given entity name.
- [- init](<nsfetchrequest/init().md>) — Creates a new fetch request.
- [entityName](nsfetchrequest/entityname.md) — The name of the entity the request is configured to fetch.
- [entity](nsfetchrequest/entity.md) — The entity specified for the fetch request.
- [includesSubentities](nsfetchrequest/includessubentities.md) — A Boolean value that indicates whether the fetch request includes subentities in the results.
