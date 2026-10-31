---
title: objc_super
framework: Objective-C Runtime
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objc_super-swift.struct
source_url: 'https://developer.apple.com/documentation/objectivec/objc_super-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_super-swift.struct.json'
content_hash: 'sha256:e714df29a72dd3b6'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_super

<sub>结构体</sub>

Specifies the superclass of an instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct objc_super
```

## 讨论

当编译器遇到 `super` 关键字作为消息接收者时，会生成 `objc_super` 数据结构。它指定应接收消息的特定超类的类定义。

## 关系

- **符合**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## 主题

### 字段

- [receiver](objc_super-swift.struct/receiver.md) — 类型为 [objc_object](objc_object.md) 的指针。指定类的一个实例。
- [super_class](objc_super-swift.struct/super_class.md) — 指向 [Class](class.md) 数据结构的指针。指定要向其发送消息的实例的特定超类。

### 实例属性

- [receiver](objc_super-swift.struct/receiver.md) — 类型为 [objc_object](objc_object.md) 的指针。指定类的一个实例。
- [super_class](objc_super-swift.struct/super_class.md) — 指向 [Class](class.md) 数据结构的指针。指定要向其发送消息的实例的特定超类。

### 初始化方法

- [init(receiver:super_class:)](<objc_super-swift.struct/init(receiver_super_class_).md>)

## 另请参阅

### 实例数据类型

- [objc_object](objc_object.md) — 表示一个类的实例。
