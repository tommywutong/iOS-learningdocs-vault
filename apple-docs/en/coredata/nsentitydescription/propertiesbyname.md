---
title: propertiesByName
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitydescription/propertiesbyname
source_url: 'https://developer.apple.com/documentation/coredata/nsentitydescription/propertiesbyname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitydescription/propertiesbyname.json'
content_hash: 'sha256:150651798cfc2390'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityDescription](../nsentitydescription.md)

# propertiesByName

<sub>Instance Property</sub>

A dictionary containing the properties of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var propertiesByName: [String : NSPropertyDescription] { get }
```

## Discussion

The keys in the dictionary are the property names and the values are instances of [NSAttributeDescription](../nsattributedescription.md) and/or [NSRelationshipDescription](../nsrelationshipdescription.md).

## See Also

### Working with properties

- [properties](properties.md) — An array containing the properties of the receiver.
- [attributesByName](attributesbyname.md) — The attributes of the receiver in a dictionary.
- [relationshipsByName](relationshipsbyname.md) — The relationships of the receiver in a dictionary.
- [- relationshipsWithDestinationEntity:](<relationships(fordestination_).md>) — Returns an array containing the relationships of the receiver where the entity description of the relationship is a given entity.
