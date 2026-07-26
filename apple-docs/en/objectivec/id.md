---
title: id
framework: Objective-C Runtime
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/id
source_url: 'https://developer.apple.com/documentation/objectivec/id'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/id.json'
content_hash: 'sha256:15db739bbfa31006'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# id

<sub>Type Alias</sub>

A pointer to an instance of a class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef struct objc_object * id;
```

## Discussion

When you create an instance of a particular class, the allocated memory contains an `objc_object` data structure, which is directly followed by the data for the instance variables of the class.

The `alloc` and `allocWithZone:` methods of the Foundation framework class NSObject use the function [class_createInstance](<class_createinstance(____).md>) to create `objc_object` data structures.

## See Also

### Instance Data Types

- [objc_object](objc_object.md) — Represents an instance of a class.
- [objc_super](objc_super-swift.struct.md) — Specifies the superclass of an instance.
