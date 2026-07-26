---
title: toOneRelationshipKeys
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsclassdescription/toonerelationshipkeys
source_url: 'https://developer.apple.com/documentation/foundation/nsclassdescription/toonerelationshipkeys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsclassdescription/toonerelationshipkeys.json'
content_hash: 'sha256:a700c32cf0a72443'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSClassDescription](../nsclassdescription.md)

# toOneRelationshipKeys

<sub>Instance Property</sub>

Overridden by subclasses to return the keys for the to-one relationship properties of instances of the described class.

<sub>Mac Catalyst, macOS</sub>

```swift
var toOneRelationshipKeys: [String] { get }
```

## Return Value

An array of `NSString` objects containing the names of the to-one relationship properties of instances of the described class.

## Discussion

To-one relationship properties are single objects.

If you have an instance of the class the receiver describes, you can use the `NSObject` instance method [toOneRelationshipKeys](../../objectivec/nsobject-swift.class/toonerelationshipkeys.md) instead.

## See Also

### Related Documentation

- [attributeKeys](attributekeys.md) — Overridden by subclasses to return the names of attributes of instances of the described class.

### Relationship keys

- [- inverseForRelationshipKey:](<inverse(forrelationshipkey_).md>) — Overridden by subclasses to return the name of the inverse relationship from a relationship specified by a given key.
- [toManyRelationshipKeys](tomanyrelationshipkeys.md) — Overridden by subclasses to return the keys for the to-many relationship properties of instances of the described class.
