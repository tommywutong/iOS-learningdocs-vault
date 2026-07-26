---
title: objc_constructInstance
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objc_constructinstance
source_url: 'https://developer.apple.com/documentation/objectivec/objc_constructinstance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_constructinstance.json'
content_hash: 'sha256:b756e704601299f0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_constructInstance

<sub>Function</sub>

Creates an instance of a class at the specified location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern idobjc_constructInstance(Class cls, void *bytes);
```

## Parameters

- `cls` — The class that you want to allocate an instance of.

- `bytes` — The location at which to allocate an instance of the `cls` class. `bytes` must point to at least `class_getInstanceSize(cls)` bytes of well-aligned, zero-filled memory.

## Return Value

An instance of the class `cls` at `bytes`, if successful; otherwise `nil` (for example, if `cls` or `bytes` are themselves `nil`).

## See Also

### Instantiating Classes

- [class_createInstance](<class_createinstance(____).md>) — Creates an instance of a class, allocating memory for the class in the default malloc memory zone.
- [objc_destructInstance](objc_destructinstance.md) — Destroys an instance of a class without freeing memory and removes any of its associated references.
