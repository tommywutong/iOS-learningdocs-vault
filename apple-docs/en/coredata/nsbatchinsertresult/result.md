---
title: result
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsbatchinsertresult/result
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchinsertresult/result'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchinsertresult/result.json'
content_hash: 'sha256:f4f598f43f6bcaa8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSBatchInsertResult](../nsbatchinsertresult.md)

# result

<sub>Instance Property</sub>

The result of a batch-insertion request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var result: Any? { get }
```

## Discussion

Cast the result to the type corresponding to [resultType](resulttype.md) to inspect it. The following example shows how to inspect a result type of [NSBatchInsertRequestResultTypeStatusOnly](../nsbatchinsertrequestresulttype/statusonly.md).

```swift
let success = batchInsertResult.result as? Bool
```

## See Also

### Accessing Results

- [resultType](resulttype.md) — The type of result that Core Data returns from this request.
- [NSBatchInsertRequestResultType](../nsbatchinsertrequestresulttype.md) — Result types for a batch-insertion request.
