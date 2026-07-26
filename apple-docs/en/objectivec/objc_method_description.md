---
title: objc_method_description
framework: Objective-C Runtime
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objc_method_description
source_url: 'https://developer.apple.com/documentation/objectivec/objc_method_description'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_method_description.json'
content_hash: 'sha256:4d6ab1f4738b600f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_method_description

<sub>Structure</sub>

Defines an Objective-C method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct objc_method_description
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Fields

- [name](objc_method_description/name.md) — The name of the method at runtime.
- [types](objc_method_description/types.md) — The types of the method arguments.

### Initializers

- [init()](<objc_method_description/init().md>)
- [init(name:types:)](<objc_method_description/init(name_types_).md>)

## See Also

### Class-Definition Data Structures

- [Method](method.md) — An opaque type that represents a method in a class definition.
- [Ivar](ivar.md) — An opaque type that represents an instance variable.
- [Category](category.md) — An opaque type that represents a category.
- [objc_property_t](objc_property_t.md) — An opaque type that represents an Objective-C declared property.
- [IMP](imp.md) — A pointer to the start of a method implementation.
- [objc_cache](objc_cache.md) — Performance optimization for method calls. Contains pointers to recently used methods.
- [objc_property_attribute_t](objc_property_attribute_t.md) — Defines a property attribute.
