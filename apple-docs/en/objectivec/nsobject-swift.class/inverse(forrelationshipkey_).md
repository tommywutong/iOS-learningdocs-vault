---
title: 'inverse(forRelationshipKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/inverse(forrelationshipkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/inverse(forrelationshipkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/inverse%28forrelationshipkey%3A%29.json'
content_hash: 'sha256:7c27f189e95acd27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# inverse(forRelationshipKey:)

<sub>Instance Method</sub>

For a given key that defines the name of the relationship from the receiver’s class to another class, returns the name of the relationship from the other class to the receiver’s class.

<sub>Mac Catalyst, macOS</sub>

```swift
func inverse(forRelationshipKey relationshipKey: String) -> String?
```

## Parameters

- `relationshipKey` — The name of the relationship from the receiver’s class to another class.

## Return Value

The name of the relationship that is the inverse of the receiver’s relationship named `relationshipKey`.

## Discussion

`NSObject`’s implementation of `inverseForRelationshipKey:` simply invokes `[[self classDescription] inverseForRelationshipKey:relationshipKey]`.  To make use of the default implementation, you must therefore implement and register a suitable class description—see [NSClassDescription](../../foundation/nsclassdescription.md).

For example, suppose an Employee class has a relationship named `department` to a Department class, and that Department has a relationship called `employees` to Employee. The statement:

```objc
employee inverseForRelationshipKey:@"department"];
```

returns the string `employees`.

## See Also

### Working with Class Descriptions

- [attributeKeys](attributekeys.md) — An array of `NSString` objects containing the names of immutable values that instances of the receiver’s class contain.
- [classDescription](classdescription.md) — An object containing information about the attributes and relationships of the receiver’s class.
- [toManyRelationshipKeys](tomanyrelationshipkeys.md) — An array containing the keys for the to-many relationship properties of the receiver.
- [toOneRelationshipKeys](toonerelationshipkeys.md) — The keys for the to-one relationship properties of the receiver, if any.
