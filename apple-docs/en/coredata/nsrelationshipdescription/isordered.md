---
title: isOrdered
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsrelationshipdescription/isordered
source_url: 'https://developer.apple.com/documentation/coredata/nsrelationshipdescription/isordered'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsrelationshipdescription/isordered.json'
content_hash: 'sha256:cd655c7b3e079b62'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSRelationshipDescription](../nsrelationshipdescription.md)

# isOrdered

<sub>Instance Property</sub>

A Boolean value that determines whether the relationship preserves the order of the referenced managed objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isOrdered: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md).

## See Also

### Configuring the Destination

- [inverseRelationship](inverserelationship.md) — The relationship that represents the inverse of the current relationship.
- [destinationEntity](destinationentity.md) — The type of object the relationship contains.
