---
title: completionBlock
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsasynchronousfetchrequest/completionblock
source_url: 'https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest/completionblock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsasynchronousfetchrequest/completionblock.json'
content_hash: 'sha256:748d99ba76908bcc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAsynchronousFetchRequest](../nsasynchronousfetchrequest.md)

# completionBlock

<sub>Instance Property</sub>

The block that is executed when the fetch request has completed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var completionBlock: NSPersistentStoreAsynchronousFetchResultCompletionBlock? { get }
```

## See Also

### Preparing a Request

- [estimatedResultCount](estimatedresultcount.md) — A configuration parameter that assists Core Data with scheduling the asynchronous fetch request.
- [fetchRequest](fetchrequest.md) — The underlying fetch request that is executed asynchronously.
