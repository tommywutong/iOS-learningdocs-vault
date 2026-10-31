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
translated: true
---
> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# OBJC_ROOT_CLASS

<sub>宏</sub>

如果你定义 Objective-C 根类，会收到编译器错误，指出该类在未指定基类的情况下被定义。你可以通过在根类定义之前（即在 `@interface` 指令之前）加上 `OBJC_ROOT_CLASS` 来避免此编译器错误。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define OBJC_ROOT_CLASS
```
