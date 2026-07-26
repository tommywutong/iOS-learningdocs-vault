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
doc_path: /documentation/coredata/nsbatchdeleterequest/resulttype
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchdeleterequest/resulttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchdeleterequest/resulttype.json'
content_hash: 'sha256:bcc6498c4c992b59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSBatchDeleteRequest](../nsbatchdeleterequest.md)

# resultType

<sub>Instance Property</sub>

The type of result the request provides when it executes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var resultType: NSBatchDeleteRequestResultType { get set }
```

## Discussion

Set this property before you execute the request if you require a result type other than the default of [NSBatchDeleteResultTypeStatusOnly](../nsbatchdeleterequestresulttype/resulttypestatusonly.md).

## See Also

### Configuring the Result Type

- [NSBatchDeleteRequestResultType](../nsbatchdeleterequestresulttype.md) — The types of result a batch delete request can provide when it executes.
