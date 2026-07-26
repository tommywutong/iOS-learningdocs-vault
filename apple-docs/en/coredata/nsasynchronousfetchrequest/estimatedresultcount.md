---
title: estimatedResultCount
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsasynchronousfetchrequest/estimatedresultcount
source_url: 'https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest/estimatedresultcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsasynchronousfetchrequest/estimatedresultcount.json'
content_hash: 'sha256:f679a163e8d309a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAsynchronousFetchRequest](../nsasynchronousfetchrequest.md)

# estimatedResultCount

<sub>Instance Property</sub>

A configuration parameter that assists Core Data with scheduling the asynchronous fetch request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var estimatedResultCount: Int { get set }
```

## See Also

### Preparing a Request

- [completionBlock](completionblock.md) — The block that is executed when the fetch request has completed.
- [fetchRequest](fetchrequest.md) — The underlying fetch request that is executed asynchronously.
