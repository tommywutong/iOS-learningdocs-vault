---
title: IMP
framework: Objective-C Runtime
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/imp
source_url: 'https://developer.apple.com/documentation/objectivec/imp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/imp.json'
content_hash: 'sha256:55af95ef5e8a0cfd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# IMP

<sub>Type Alias</sub>

A pointer to the start of a method implementation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias IMP = OpaquePointer
```

## Discussion

This data type is a pointer to the start of the function that implements the method. This function uses standard C calling conventions as implemented for the current CPU architecture. The first argument is a pointer to `self` (that is, the memory for the particular instance of this class, or, for a class method, a pointer to the metaclass). The second argument is the method selector. The method arguments follow.

## See Also

### Class-Definition Data Structures

- [Method](method.md) — An opaque type that represents a method in a class definition.
- [Ivar](ivar.md) — An opaque type that represents an instance variable.
- [Category](category.md) — An opaque type that represents a category.
- [objc_property_t](objc_property_t.md) — An opaque type that represents an Objective-C declared property.
- [objc_method_description](objc_method_description.md) — Defines an Objective-C method.
- [objc_cache](objc_cache.md) — Performance optimization for method calls. Contains pointers to recently used methods.
- [objc_property_attribute_t](objc_property_attribute_t.md) — Defines a property attribute.
