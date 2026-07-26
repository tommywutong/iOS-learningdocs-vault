---
title: properties
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitydescription/properties
source_url: 'https://developer.apple.com/documentation/coredata/nsentitydescription/properties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitydescription/properties.json'
content_hash: 'sha256:06c8a2ee16f616b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityDescription](../nsentitydescription.md)

# properties

<sub>Instance Property</sub>

An array containing the properties of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var properties: [NSPropertyDescription] { get set }
```

## Discussion

The elements in the array are instances of [NSAttributeDescription](../nsattributedescription.md), [NSRelationshipDescription](../nsrelationshipdescription.md), and/or [NSFetchedPropertyDescription](../nsfetchedpropertydescription.md).

### Special Considerations

Setting the properties raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

### Working with properties

- [propertiesByName](propertiesbyname.md) — A dictionary containing the properties of the receiver.
- [attributesByName](attributesbyname.md) — The attributes of the receiver in a dictionary.
- [relationshipsByName](relationshipsbyname.md) — The relationships of the receiver in a dictionary.
- [- relationshipsWithDestinationEntity:](<relationships(fordestination_).md>) — Returns an array containing the relationships of the receiver where the entity description of the relationship is a given entity.
