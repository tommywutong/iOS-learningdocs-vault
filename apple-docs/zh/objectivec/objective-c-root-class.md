---
title: Objective-C 根类
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objective-c-root-class
source_url: 'https://developer.apple.com/documentation/objectivec/objective-c-root-class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objective-c-root-class.json'
content_hash: 'sha256:fd970966d2de0f38'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [Objective-C Runtime](objective-c-runtime.md)

# Objective-C 根类

<sub>API 集合</sub>

这个宏将一个类注解为 Objective-C 根类。

## Topics

### Constants

- [OBJC_ROOT_CLASS](objc_root_class.md) — 如果你定义了一个 Objective-C 根类，会收到一个编译器错误，提示该类在未指定基类的情况下被定义。你可以在根类的定义之前（即在 `@interface` 指令之前）加上 `OBJC_ROOT_CLASS` 来避免这个编译器错误。

## See Also

### Constants

- [Boolean Values](boolean-values.md) — 这些宏定义了方便的常量来表示布尔值。
- [Null Values](null-values.md) — 这些宏为类和实例定义了空值。
- [Dispatch Function Prototypes](dispatch-function-prototypes.md) — 这个宏指示 dispatch 函数是否必须转换为合适的函数指针类型。
- [Local Variable Storage Duration](local-variable-storage-duration.md) — 这个宏指示编译器在优化过程中不应对某些局部变量中存储的值进行激进的释放。
