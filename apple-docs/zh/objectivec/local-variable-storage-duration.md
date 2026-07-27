---
title: 局部变量存储期
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/local-variable-storage-duration
source_url: 'https://developer.apple.com/documentation/objectivec/local-variable-storage-duration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/local-variable-storage-duration.json'
content_hash: 'sha256:0f343ff6e3377238'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [Objective-C Runtime](objective-c-runtime.md)

# 局部变量存储期

这个宏指示编译器在优化过程中不应对某些局部变量中存储的值进行激进的释放。

## 主题

### 常量

- [NS_VALID_UNTIL_END_OF_SCOPE](../foundation/ns_valid_until_end_of_scope.md) — 标记类型为 `id` 或指向 ObjC 对象类型指针的局部变量，使得存储到这些局部变量中的值不会被编译器在优化过程中激进地释放。相反，这些值会一直保留，直到该变量被再次赋值，或者该局部变量的作用域（例如复合语句或方法定义）结束为止。

## 另请参阅

### 常量

- [Boolean Values](boolean-values.md) — 这些宏定义了方便的常量来表示布尔值。
- [Null Values](null-values.md) — 这些宏为类和实例定义了空值。
- [Dispatch Function Prototypes](dispatch-function-prototypes.md) — 这个宏指示 dispatch 函数是否必须转换为合适的函数指针类型。
- [Objective-C Root Class](objective-c-root-class.md) — 这个宏将一个类注解为 Objective-C 根类。
