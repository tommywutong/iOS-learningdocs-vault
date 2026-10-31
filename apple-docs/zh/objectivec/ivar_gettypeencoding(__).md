---
title: 'ivar_getTypeEncoding(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/ivar_gettypeencoding(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/ivar_gettypeencoding(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/ivar_gettypeencoding%28_%3A%29.json'
content_hash: 'sha256:dafeb6f987c76939'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# ivar_getTypeEncoding(_:)

<sub>函数</sub>

返回一个实例变量的类型字符串。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func ivar_getTypeEncoding(_ v: Ivar) -> UnsafePointer<CChar>?
```

## 返回值

包含该实例变量类型编码的 C 字符串。

## 讨论

可能的取值请参阅 [Objective-C Runtime Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008048) \> [Type Encodings](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtTypeEncodings.html#//apple_ref/doc/uid/TP40008048-CH100)。

## 另请参阅

### 使用实例变量

- [ivar_getName](<ivar_getname(__).md>) — 返回一个实例变量的名称。
- [ivar_getOffset](<ivar_getoffset(__).md>) — 返回一个实例变量的偏移量。
