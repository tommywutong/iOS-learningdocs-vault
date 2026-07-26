---
title: result
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsbatchdeleteresult/result
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchdeleteresult/result'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchdeleteresult/result.json'
content_hash: 'sha256:ce739012ad759afc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSBatchDeleteResult](../nsbatchdeleteresult.md)

# result

<sub>Instance Property</sub>

The value the request returns after it executes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var result: Any? { get }
```

## Discussion

Use [resultType](resulttype.md) to determine the kind of value this property contains, and then cast to the appropriate type as the following example shows:

```swift
// resultType is .resultTypeCount.
guard let count = batchDeleteResult.result as? Int else { return }
            
// resultType is .resultTypeObjectIDs.
guard let objectIDs = batchDeleteResult.result as? [NSManagedObjectID] 
    else { return }
            
// resultType is .resultTypeStatusOnly.
guard let status = batchDeleteResult.result as? Bool else { return }
```

## See Also

### Accessing the Result

- [resultType](resulttype.md) — The data type of the request’s result value.
- [NSBatchDeleteRequestResultType](../nsbatchdeleterequestresulttype.md) — The types of result a batch delete request can provide when it executes.
