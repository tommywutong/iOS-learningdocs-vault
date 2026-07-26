---
title: property
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchindexelementdescription/property
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchindexelementdescription/property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchindexelementdescription/property.json'
content_hash: 'sha256:d9811133ff1b847b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSFetchIndexElementDescription](../nsfetchindexelementdescription.md)

# property

<sub>Instance Property</sub>

A property description.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var property: NSPropertyDescription? { get }
```

## Discussion

This property may also be an [NSExpressionDescription](../nsexpressiondescription.md) that expresses a function.

## See Also

### Inspecting an Index Element Description

- [collationType](collationtype.md) — The type of collation that the index element uses, either binary or R-tree.
- [indexDescription](indexdescription.md)
- [ascending](isascending.md) — A Boolean value that controls whether an index that supports direction is an ascending or descending index.
- [propertyName](propertyname.md) — The specified name in the property description.
