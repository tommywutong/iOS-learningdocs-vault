---
title: 'ivar_getOffset(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/ivar_getoffset(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/ivar_getoffset(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/ivar_getoffset%28_%3A%29.json'
content_hash: 'sha256:7721a32aafc6e319'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# ivar_getOffset(_:)

<sub>函数</sub>

返回一个实例变量的偏移量。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func ivar_getOffset(_ v: Ivar) -> Int
```

## 讨论

对于类型为 `id` 或其他对象类型的实例变量，应调用 [object_getIvar](<object_getivar(____).md>) 和 [object_setIvar](<object_setivar(______).md>)，而不是使用此偏移量直接访问实例变量数据。

## 另请参阅

### 使用实例变量

- [ivar_getName](<ivar_getname(__).md>) — 返回一个实例变量的名称。
- [ivar_getTypeEncoding](<ivar_gettypeencoding(__).md>) — 返回一个实例变量的类型字符串。
