---
title: isToMany
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsrelationshipdescription/istomany
source_url: 'https://developer.apple.com/documentation/coredata/nsrelationshipdescription/istomany'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsrelationshipdescription/istomany.json'
content_hash: 'sha256:d00d3bda49f7db9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSRelationshipDescription](../nsrelationshipdescription.md)

# isToMany

<sub>Instance Property</sub>

Returns a Boolean value that indicates whether the relationship can contain many managed objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isToMany: Bool { get }
```

## Discussion

If [maxCount](maxcount.md) is equal to `1`, implying a to-one relationship, this property returns [false](../../swift/false.md); otherwise, it returns [true](../../swift/true.md).

## See Also

### Configuring Cardinality

- [minCount](mincount.md) — The minimum number of managed objects the relationship can reference.
- [maxCount](maxcount.md) — The maximum number of managed objects the relationship can reference.
