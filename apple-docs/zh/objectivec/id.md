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
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# id

<sub>类型别名</sub>

指向某个类实例的指针。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef struct objc_object * id;
```

## 讨论

当你创建某个特定类的实例时，所分配的内存包含一个 `objc_object` 数据结构，其后紧跟着该类实例变量的数据。

Foundation 框架类 NSObject 的 `alloc` 和 `allocWithZone:` 方法使用函数 [class_createInstance](<class_createinstance(____).md>) 来创建 `objc_object` 数据结构。

## 另请参阅

### 实例数据类型

- [objc_object](objc_object.md) — 表示一个类的实例。
- [objc_super](objc_super-swift.struct.md) — 指定一个实例的超类。
