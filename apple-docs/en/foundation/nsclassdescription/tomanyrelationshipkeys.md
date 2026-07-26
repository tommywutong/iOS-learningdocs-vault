---
title: toManyRelationshipKeys
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsclassdescription/tomanyrelationshipkeys
source_url: 'https://developer.apple.com/documentation/foundation/nsclassdescription/tomanyrelationshipkeys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsclassdescription/tomanyrelationshipkeys.json'
content_hash: 'sha256:18c396bf9c93894f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSClassDescription](../nsclassdescription.md)

# toManyRelationshipKeys

<sub>Instance Property</sub>

Overridden by subclasses to return the keys for the to-many relationship properties of instances of the described class.

<sub>Mac Catalyst, macOS</sub>

```swift
var toManyRelationshipKeys: [String] { get }
```

## Return Value

An array of `NSString` objects containing the names of the to-many relationship properties of instances of the described class.

## Discussion

To-many relationship properties are arrays of objects.

If you have an instance of the class the receiver describes, you can use the `NSObject` instance method [toManyRelationshipKeys](../../objectivec/nsobject-swift.class/tomanyrelationshipkeys.md) instead.

## See Also

### Related Documentation

- [attributeKeys](attributekeys.md) — Overridden by subclasses to return the names of attributes of instances of the described class.

### Relationship keys

- [- inverseForRelationshipKey:](<inverse(forrelationshipkey_).md>) — Overridden by subclasses to return the name of the inverse relationship from a relationship specified by a given key.
- [toOneRelationshipKeys](toonerelationshipkeys.md) — Overridden by subclasses to return the keys for the to-one relationship properties of instances of the described class.
