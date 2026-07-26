---
title: classDescription
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/classdescription
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/classdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/classdescription.json'
content_hash: 'sha256:4b3c51d4bfc1dd6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# classDescription

<sub>Instance Property</sub>

An object containing information about the attributes and relationships of the receiver’s class.

<sub>Mac Catalyst, macOS</sub>

```swift
@NSCopying var classDescription: NSClassDescription { get }
```

## See Also

### Working with Class Descriptions

- [attributeKeys](attributekeys.md) — An array of `NSString` objects containing the names of immutable values that instances of the receiver’s class contain.
- [- inverseForRelationshipKey:](<inverse(forrelationshipkey_).md>) — For a given key that defines the name of the relationship from the receiver’s class to another class, returns the name of the relationship from the other class to the receiver’s class.
- [toManyRelationshipKeys](tomanyrelationshipkeys.md) — An array containing the keys for the to-many relationship properties of the receiver.
- [toOneRelationshipKeys](toonerelationshipkeys.md) — The keys for the to-one relationship properties of the receiver, if any.
