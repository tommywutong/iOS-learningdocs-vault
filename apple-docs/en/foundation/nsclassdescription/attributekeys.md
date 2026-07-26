---
title: attributeKeys
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsclassdescription/attributekeys
source_url: 'https://developer.apple.com/documentation/foundation/nsclassdescription/attributekeys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsclassdescription/attributekeys.json'
content_hash: 'sha256:e7c306c2b73298d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSClassDescription](../nsclassdescription.md)

# attributeKeys

<sub>Instance Property</sub>

Overridden by subclasses to return the names of attributes of instances of the described class.

<sub>Mac Catalyst, macOS</sub>

```swift
var attributeKeys: [String] { get }
```

## Return Value

An array of `NSString` objects containing the names of attributes of instances of the described class.

## Discussion

For example, a class description that describes Movie objects could return the attribute keys `title`, `dateReleased`, and `rating`.

If you have an instance of the class the receiver describes, you can use the `NSObject` instance method [attributeKeys](../../objectivec/nsobject-swift.class/attributekeys.md) instead.

## See Also

### Related Documentation

- [toManyRelationshipKeys](tomanyrelationshipkeys.md) — Overridden by subclasses to return the keys for the to-many relationship properties of instances of the described class.
- [toOneRelationshipKeys](toonerelationshipkeys.md) — Overridden by subclasses to return the keys for the to-one relationship properties of instances of the described class.
