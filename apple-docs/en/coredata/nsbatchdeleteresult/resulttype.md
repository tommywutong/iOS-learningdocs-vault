---
title: resultType
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsbatchdeleteresult/resulttype
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchdeleteresult/resulttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchdeleteresult/resulttype.json'
content_hash: 'sha256:551968ada8c350a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSBatchDeleteResult](../nsbatchdeleteresult.md)

# resultType

<sub>Instance Property</sub>

The data type of the request’s result value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var resultType: NSBatchDeleteRequestResultType { get }
```

## Discussion

This property’s value is set to the request’s [resultType](../nsbatchdeleterequest/resulttype.md) property.

## See Also

### Accessing the Result

- [result](result.md) — The value the request returns after it executes.
- [NSBatchDeleteRequestResultType](../nsbatchdeleterequestresulttype.md) — The types of result a batch delete request can provide when it executes.
