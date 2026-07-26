---
title: result
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsbatchupdateresult/result
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchupdateresult/result'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchupdateresult/result.json'
content_hash: 'sha256:8c002ffcef23aadf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSBatchUpdateResult](../nsbatchupdateresult.md)

# result

<sub>Instance Property</sub>

The result of a batch-update request, either the number of updated objects, the identifiers of the updated objects, or a status value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var result: Any? { get }
```

## See Also

### Accessing Results

- [resultType](resulttype.md) — The type of result that Core Data returns from the request.
- [NSBatchUpdateRequestResultType](../nsbatchupdaterequestresulttype.md) — Result types for a batch-update request.
