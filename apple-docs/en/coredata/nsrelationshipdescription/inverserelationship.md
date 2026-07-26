---
title: inverseRelationship
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsrelationshipdescription/inverserelationship
source_url: 'https://developer.apple.com/documentation/coredata/nsrelationshipdescription/inverserelationship'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsrelationshipdescription/inverserelationship.json'
content_hash: 'sha256:44a0a75a3c4f3a78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSRelationshipDescription](../nsrelationshipdescription.md)

# inverseRelationship

<sub>Instance Property</sub>

The relationship that represents the inverse of the current relationship.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
unowned(unsafe) var inverseRelationship: NSRelationshipDescription? { get set }
```

## Discussion

The inverse relationship is the description of the current relationship from the destination entity’s perspective. For example, the inverse of a department’s relationship to an employee (a to-many relationship) is the employees’ relationship to the department (a to-one relationship).

## See Also

### Configuring the Destination

- [destinationEntity](destinationentity.md) — The type of object the relationship contains.
- [ordered](isordered.md) — A Boolean value that determines whether the relationship preserves the order of the referenced managed objects.
