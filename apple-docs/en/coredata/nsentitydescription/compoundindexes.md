---
title: compoundIndexes
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（11.0 起废弃）, iPadOS 3.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.5+（10.13 起废弃）, tvOS 9.0+（11.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（4.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/coredata/nsentitydescription/compoundindexes
source_url: 'https://developer.apple.com/documentation/coredata/nsentitydescription/compoundindexes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitydescription/compoundindexes.json'
content_hash: 'sha256:f683ae48c0f1e385'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityDescription](../nsentitydescription.md)

# compoundIndexes

<sub>Instance Property</sub>

The compound indexes for the entity as an array of arrays.

> [!warning] Deprecated
> Use NSEntityDescription.indexes instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var compoundIndexes: [[Any]] { get set }
```

## Discussion

The arrays contained in the returned array contain instances of `NSAttributeDescription`, `NSRelationshipDescription` that represent properties of the entity, or of `NSString` that match the name of attributes or relationships of the entity.

Compound indexes are only used by stores that natively support compound indices—setting them is only advisory. Indexes apply to the entire inheritance hierarchy.

## See Also

### Configuring indexes and constraints

- [indexes](indexes.md) — An array of fetch index descriptions for the entity.
- [uniquenessConstraints](uniquenessconstraints.md) — An array of arrays that contains one or more attributes with a value that must be unique over the instances of that entity.
