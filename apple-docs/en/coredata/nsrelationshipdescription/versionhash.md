---
title: versionHash
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsrelationshipdescription/versionhash
source_url: 'https://developer.apple.com/documentation/coredata/nsrelationshipdescription/versionhash'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsrelationshipdescription/versionhash.json'
content_hash: 'sha256:324ab181865feedc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSRelationshipDescription](../nsrelationshipdescription.md)

# versionHash

<sub>Instance Property</sub>

The relationship’s unique identity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var versionHash: Data { get }
```

## Discussion

To calculate its version hash, the relationship combines its superclass’s [versionHash](../nspropertydescription/versionhash.md) property with the values of [inverseRelationship](inverserelationship.md), [destinationEntity](destinationentity.md), [minCount](mincount.md), and [maxCount](maxcount.md).
