---
title: sourceExpression
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitymapping/sourceexpression
source_url: 'https://developer.apple.com/documentation/coredata/nsentitymapping/sourceexpression'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitymapping/sourceexpression.json'
content_hash: 'sha256:317b852649a364c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityMapping](../nsentitymapping.md)

# sourceExpression

<sub>Instance Property</sub>

The source expression for the entity mapping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sourceExpression: NSExpression? { get set }
```

## Discussion

The source expression is used to obtain the collection of managed objects to process through the mapping. The expression can be a fetch request expression, or any other expression that evaluates to a collection.

## See Also

### Managing Source Information

- [sourceEntityName](sourceentityname.md) — The source entity name for the entity mapping.
- [sourceEntityVersionHash](sourceentityversionhash.md) — The version hash of the source entity for the entity mapping.
