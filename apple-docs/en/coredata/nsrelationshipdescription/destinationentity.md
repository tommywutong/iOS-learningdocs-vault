---
title: destinationEntity
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsrelationshipdescription/destinationentity
source_url: 'https://developer.apple.com/documentation/coredata/nsrelationshipdescription/destinationentity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsrelationshipdescription/destinationentity.json'
content_hash: 'sha256:435a3e15e40cf1f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSRelationshipDescription](../nsrelationshipdescription.md)

# destinationEntity

<sub>Instance Property</sub>

The type of object the relationship contains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
unowned(unsafe) var destinationEntity: NSEntityDescription? { get set }
```

## See Also

### Configuring the Destination

- [inverseRelationship](inverserelationship.md) — The relationship that represents the inverse of the current relationship.
- [ordered](isordered.md) — A Boolean value that determines whether the relationship preserves the order of the referenced managed objects.
