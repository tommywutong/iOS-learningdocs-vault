---
title: 'class_createInstance(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/class_createinstance(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/class_createinstance(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/class_createinstance%28_%3A_%3A%29.json'
content_hash: 'sha256:5eee7bf5fc803677'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# class_createInstance(_:_:)

<sub>函数</sub>

创建一个类的实例，并在默认的 malloc 内存区中为该类分配内存。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func class_createInstance(_ cls: AnyClass?, _ extraBytes: Int) -> Any?
```

## 参数

- `cls` — 你要为其分配实例的类。

- `extraBytes` — 一个整数，表示要额外分配的字节数。这些额外的字节可用于存储类定义中已定义的实例变量之外的额外实例变量。

## 返回值

类 `cls` 的一个实例。
