---
title: fetchRequest
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsasynchronousfetchrequest/fetchrequest
source_url: 'https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest/fetchrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsasynchronousfetchrequest/fetchrequest.json'
content_hash: 'sha256:5abc6bb31539d1c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAsynchronousFetchRequest](../nsasynchronousfetchrequest.md)

# fetchRequest

<sub>Instance Property</sub>

The underlying fetch request that is executed asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fetchRequest: NSFetchRequest<ResultType> { get }
```

## See Also

### Preparing a Request

- [completionBlock](completionblock.md) — The block that is executed when the fetch request has completed.
- [estimatedResultCount](estimatedresultcount.md) — A configuration parameter that assists Core Data with scheduling the asynchronous fetch request.
