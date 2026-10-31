---
title: 'objc_removeAssociatedObjects(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_removeassociatedobjects(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_removeassociatedobjects(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_removeassociatedobjects%28_%3A%29.json'
content_hash: 'sha256:91c881c40de788ec'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_removeAssociatedObjects(_:)

<sub>函数</sub>

移除给定对象的所有关联。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_removeAssociatedObjects(_ object: Any)
```

## 参数

- `object` — 维护着关联对象的对象。

## 讨论

此函数的主要目的是便于将对象恢复到「原始状态」。你不应使用此函数从对象中一般性地移除关联，因为它也会移除其他客户端可能已添加到该对象上的关联。通常，你应使用 [objc_setAssociatedObject](<objc_setassociatedobject(________).md>) 并传入 `nil` 值来清除某个关联。

## 另请参阅

### 关联引用

- [objc_setAssociatedObject](<objc_setassociatedobject(________).md>) — 使用给定的键和关联策略为给定对象设置一个关联值。
- [objc_getAssociatedObject](<objc_getassociatedobject(____).md>) — 返回给定对象在给定键下关联的值。
