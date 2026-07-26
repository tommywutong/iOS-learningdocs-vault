---
title: Method
framework: Objective-C Runtime
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/method
source_url: 'https://developer.apple.com/documentation/objectivec/method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/method.json'
content_hash: 'sha256:ded944b7126dd20b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# Method

<sub>Type Alias</sub>

An opaque type that represents a method in a class definition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Method = OpaquePointer
```

## See Also

### Class-Definition Data Structures

- [Ivar](ivar.md) — An opaque type that represents an instance variable.
- [Category](category.md) — An opaque type that represents a category.
- [objc_property_t](objc_property_t.md) — An opaque type that represents an Objective-C declared property.
- [IMP](imp.md) — A pointer to the start of a method implementation.
- [objc_method_description](objc_method_description.md) — Defines an Objective-C method.
- [objc_cache](objc_cache.md) — Performance optimization for method calls. Contains pointers to recently used methods.
- [objc_property_attribute_t](objc_property_attribute_t.md) — Defines a property attribute.
