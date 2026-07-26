---
title: 'init(objectIDs:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsbatchdeleterequest/init(objectids:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchdeleterequest/init(objectids:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchdeleterequest/init%28objectids%3A%29.json'
content_hash: 'sha256:973ee9b42858eb09'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSBatchDeleteRequest](../nsbatchdeleterequest.md)

# init(objectIDs:)

<sub>Initializer</sub>

Creates a request that deletes the managed objects with the specified identifiers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(objectIDs objects: [NSManagedObjectID])
```

## Parameters

- `objects` — The array that contains the identifiers of the managed objects to delete.

## Discussion

> [!important] Important
> The identifiers your provide must be from managed objects of the same entity type; mixing entity types results in an error when you execute the request.

## See Also

### Creating a Request

- [- initWithFetchRequest:](<init(fetchrequest_).md>) — Creates a request that deletes the results of the specified fetch request.
