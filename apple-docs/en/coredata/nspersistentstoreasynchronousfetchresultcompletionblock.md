---
title: NSPersistentStoreAsynchronousFetchResultCompletionBlock
framework: Core Data
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstoreasynchronousfetchresultcompletionblock
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoreasynchronousfetchresultcompletionblock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoreasynchronousfetchresultcompletionblock.json'
content_hash: 'sha256:380217c4f57872c3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentStoreAsynchronousFetchResultCompletionBlock

<sub>Type Alias</sub>

A completion block that an asynchronous fetch request calls with a result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias NSPersistentStoreAsynchronousFetchResultCompletionBlock = (NSAsynchronousFetchResult<any NSFetchRequestResult>) -> Void
```

## Parameters

- `result` — The result of the fetch request.
