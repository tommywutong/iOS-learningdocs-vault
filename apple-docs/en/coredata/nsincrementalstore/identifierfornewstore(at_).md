---
title: 'identifierForNewStore(at:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsincrementalstore/identifierfornewstore(at:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsincrementalstore/identifierfornewstore(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsincrementalstore/identifierfornewstore%28at%3A%29.json'
content_hash: 'sha256:9019824b5fb5b635'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSIncrementalStore](../nsincrementalstore.md)

# identifierForNewStore(at:)

<sub>Type Method</sub>

Returns the identifier for the store at a given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func identifierForNewStore(at storeURL: URL) -> Any
```

## Parameters

- `storeURL` — The URL of a persistent store.

## Return Value

The identifier for the store at `storeURL`.

## See Also

### Accessing Metadata

- [- loadMetadata:](<loadmetadata().md>) — Loads the metadata for the store.
