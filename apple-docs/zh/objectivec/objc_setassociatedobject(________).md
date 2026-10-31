---
title: 'objc_setAssociatedObject(_:_:_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_setassociatedobject(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_setassociatedobject(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_setassociatedobject%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:ec8a92c4a7db7a75'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_setAssociatedObject(_:_:_:_:)

<sub>函数</sub>

使用给定的键和关联策略为给定对象设置一个关联值。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_setAssociatedObject(_ object: Any, _ key: UnsafeRawPointer, _ value: Any?, _ policy: objc_AssociationPolicy)
```

## 参数

- `object` — 关联的源对象。

- `key` — 关联所用的键。

- `value` — 要与 `object` 的键 `key` 关联的值。传入 `nil` 可清除现有关联。

- `policy` — 关联的策略。可能的取值参见 [objc_AssociationPolicy](objc_associationpolicy.md)。

## 另请参阅

### 关联引用

- [objc_getAssociatedObject](<objc_getassociatedobject(____).md>) — 返回给定对象在给定键下关联的值。
- [objc_removeAssociatedObjects](<objc_removeassociatedobjects(__).md>) — 移除给定对象的所有关联。
