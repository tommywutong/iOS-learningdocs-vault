---
title: attributeKeys
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/attributekeys
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/attributekeys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/attributekeys.json'
content_hash: 'sha256:7726456faf9ef26f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# attributeKeys

<sub>Instance Property</sub>

An array of `NSString` objects containing the names of immutable values that instances of the receiver’s class contain.

<sub>Mac Catalyst, macOS</sub>

```swift
var attributeKeys: [String] { get }
```

## Discussion

`NSObject`’s implementation of `attributeKeys` simply calls `[[self classDescription] attributeKeys]`. To make use of the default implementation, you must therefore implement and register a suitable class description—see [NSClassDescription](../../foundation/nsclassdescription.md).

## See Also

### Working with Class Descriptions

- [classDescription](classdescription.md) — An object containing information about the attributes and relationships of the receiver’s class.
- [- inverseForRelationshipKey:](<inverse(forrelationshipkey_).md>) — For a given key that defines the name of the relationship from the receiver’s class to another class, returns the name of the relationship from the other class to the receiver’s class.
- [toManyRelationshipKeys](tomanyrelationshipkeys.md) — An array containing the keys for the to-many relationship properties of the receiver.
- [toOneRelationshipKeys](toonerelationshipkeys.md) — The keys for the to-one relationship properties of the receiver, if any.
