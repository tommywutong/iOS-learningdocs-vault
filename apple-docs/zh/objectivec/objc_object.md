---
title: objc_object
framework: Objective-C Runtime
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objc_object
source_url: 'https://developer.apple.com/documentation/objectivec/objc_object'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_object.json'
content_hash: 'sha256:970ed665091a62f7'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_object

<sub>结构体</sub>

表示某个类的一个实例。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct objc_object
```

## 关系

- **遵循**： [BitwiseCopyable](../swift/bitwisecopyable.md)、[Sendable](../swift/sendable.md)

## 主题

### 初始化方法

- [init(isa:)](<objc_object/init(isa_).md>)

### 实例属性

- [isa](objc_object/isa.md) — 指向该对象所属类定义的指针。 _(已废弃)_

## 另请参阅

### 实例数据类型

- [objc_super](objc_super-swift.struct.md) — 指定某个实例的超类。
