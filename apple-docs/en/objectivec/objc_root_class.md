---
title: OBJC_ROOT_CLASS
framework: Objective-C Runtime
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objc_root_class
source_url: 'https://developer.apple.com/documentation/objectivec/objc_root_class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_root_class.json'
content_hash: 'sha256:4e6d18a1d17000bc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# OBJC_ROOT_CLASS

<sub>Macro</sub>

If you define an Objective-C root class, you receive a compiler error indicating that the class is defined without specifying a base class. You can avoid this compiler error by preceding the definition of the root class (that is, before the `@interface` directive) with `OBJC_ROOT_CLASS`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define OBJC_ROOT_CLASS
```
