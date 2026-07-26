---
title: maxCount
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsrelationshipdescription/maxcount
source_url: 'https://developer.apple.com/documentation/coredata/nsrelationshipdescription/maxcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsrelationshipdescription/maxcount.json'
content_hash: 'sha256:68acdf2d3568e7d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSRelationshipDescription](../nsrelationshipdescription.md)

# maxCount

<sub>Instance Property</sub>

The maximum number of managed objects the relationship can reference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var maxCount: Int { get set }
```

## Discussion

If you declare a relationship attribute as optional when defining your entities, the framework only enforces [minCount](mincount.md) and [maxCount](maxcount.md) when that attribute is not `nil`.

The default value is `0`.

## See Also

### Configuring Cardinality

- [toMany](istomany.md) — Returns a Boolean value that indicates whether the relationship can contain many managed objects.
- [minCount](mincount.md) — The minimum number of managed objects the relationship can reference.
