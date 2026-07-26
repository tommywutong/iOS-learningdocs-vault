---
title: 'init(fetchRequest:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsbatchdeleterequest/init(fetchrequest:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchdeleterequest/init(fetchrequest:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchdeleterequest/init%28fetchrequest%3A%29.json'
content_hash: 'sha256:20a2f84cb39aca01'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSBatchDeleteRequest](../nsbatchdeleterequest.md)

# init(fetchRequest:)

<sub>Initializer</sub>

Creates a request that deletes the results of the specified fetch request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(fetchRequest fetch: NSFetchRequest<any NSFetchRequestResult>)
```

## Parameters

- `fetch` — The fetch request that identifies the managed objects to delete.

## See Also

### Creating a Request

- [- initWithObjectIDs:](<init(objectids_).md>) — Creates a request that deletes the managed objects with the specified identifiers.
