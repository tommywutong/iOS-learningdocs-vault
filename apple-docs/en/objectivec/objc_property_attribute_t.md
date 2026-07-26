---
title: objc_property_attribute_t
framework: Objective-C Runtime
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objc_property_attribute_t
source_url: 'https://developer.apple.com/documentation/objectivec/objc_property_attribute_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_property_attribute_t.json'
content_hash: 'sha256:62c8447209c63e6c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_property_attribute_t

<sub>Structure</sub>

Defines a property attribute.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct objc_property_attribute_t
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Initializers

- [init(name:value:)](<objc_property_attribute_t/init(name_value_).md>)

### Instance Properties

- [name](objc_property_attribute_t/name.md) — The name of the attribute.
- [value](objc_property_attribute_t/value.md) — The value of the attribute (usually empty).

## See Also

### Class-Definition Data Structures

- [Method](method.md) — An opaque type that represents a method in a class definition.
- [Ivar](ivar.md) — An opaque type that represents an instance variable.
- [Category](category.md) — An opaque type that represents a category.
- [objc_property_t](objc_property_t.md) — An opaque type that represents an Objective-C declared property.
- [IMP](imp.md) — A pointer to the start of a method implementation.
- [objc_method_description](objc_method_description.md) — Defines an Objective-C method.
- [objc_cache](objc_cache.md) — Performance optimization for method calls. Contains pointers to recently used methods.
