---
title: 'ivar_getName(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/ivar_getname(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/ivar_getname(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/ivar_getname%28_%3A%29.json'
content_hash: 'sha256:a30f8e985fd44460'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# ivar_getName(_:)

<sub>函数</sub>

返回一个实例变量的名称。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func ivar_getName(_ v: Ivar) -> UnsafePointer<CChar>?
```

## 返回值

包含该实例变量名称的 C 字符串。

## 另请参阅

### 使用实例变量

- [ivar_getTypeEncoding](<ivar_gettypeencoding(__).md>) — 返回一个实例变量的类型字符串。
- [ivar_getOffset](<ivar_getoffset(__).md>) — 返回一个实例变量的偏移量。
