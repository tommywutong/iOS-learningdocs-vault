---
title: 'inverse(forRelationshipKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsclassdescription/inverse(forrelationshipkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsclassdescription/inverse(forrelationshipkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsclassdescription/inverse%28forrelationshipkey%3A%29.json'
content_hash: 'sha256:7b2559314ed359c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSClassDescription](../nsclassdescription.md)

# inverse(forRelationshipKey:)

<sub>Instance Method</sub>

Overridden by subclasses to return the name of the inverse relationship from a relationship specified by a given key.

<sub>Mac Catalyst, macOS</sub>

```swift
func inverse(forRelationshipKey relationshipKey: String) -> String?
```

## Return Value

The name of the inverse relationship from the relationship specified by `relationshipKey`.

## Discussion

For a given key that defines the name of the relationship from the receiver’s class to another class, returns the name of the relationship from the other class to the receiver’s class. For example, suppose an Employee class has a relationship named `department` to a Department class, and that Department has a relationship named `employees` to Employee. The statement:

```objc
[employee inverseForRelationshipKey:@"department"];
```

returns the string `employees`.

If you have an instance of the class the receiver describes, you can use the `NSObject` instance method [inverse(forRelationshipKey:)](<../../objectivec/nsobject-swift.class/inverse(forrelationshipkey_).md>) instead.

## See Also

### Relationship keys

- [toManyRelationshipKeys](tomanyrelationshipkeys.md) — Overridden by subclasses to return the keys for the to-many relationship properties of instances of the described class.
- [toOneRelationshipKeys](toonerelationshipkeys.md) — Overridden by subclasses to return the keys for the to-one relationship properties of instances of the described class.
