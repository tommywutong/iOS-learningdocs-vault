---
title: 'relationships(forDestination:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsentitydescription/relationships(fordestination:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsentitydescription/relationships(fordestination:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitydescription/relationships%28fordestination%3A%29.json'
content_hash: 'sha256:341b21ffdb21a1cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityDescription](../nsentitydescription.md)

# relationships(forDestination:)

<sub>Instance Method</sub>

Returns an array containing the relationships of the receiver where the entity description of the relationship is a given entity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func relationships(forDestination entity: NSEntityDescription) -> [NSRelationshipDescription]
```

## Parameters

- `entity` — An entity description.

## Return Value

An array containing the relationships of the receiver where the entity description of the relationship is `entity`. Elements in the array are instances of [NSRelationshipDescription](../nsrelationshipdescription.md).

## See Also

### Working with properties

- [propertiesByName](propertiesbyname.md) — A dictionary containing the properties of the receiver.
- [properties](properties.md) — An array containing the properties of the receiver.
- [attributesByName](attributesbyname.md) — The attributes of the receiver in a dictionary.
- [relationshipsByName](relationshipsbyname.md) — The relationships of the receiver in a dictionary.
