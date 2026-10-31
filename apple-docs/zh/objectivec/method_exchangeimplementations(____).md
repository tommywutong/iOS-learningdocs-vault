---
title: 'method_exchangeImplementations(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/method_exchangeimplementations(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/method_exchangeimplementations(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/method_exchangeimplementations%28_%3A_%3A%29.json'
content_hash: 'sha256:51763c1fa8fd1f12'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# method_exchangeImplementations(_:_:)

<sub>函数</sub>

交换两个方法的实现。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func method_exchangeImplementations(_ m1: Method, _ m2: Method)
```

## 讨论

这是以下操作的原子版本：

```objc
IMP imp1 = method_getImplementation(m1);
IMP imp2 = method_getImplementation(m2);
method_setImplementation(m1, imp2);
method_setImplementation(m2, imp1);
```

## 另请参阅

### 使用方法

- [method_getName](<method_getname(__).md>) — 返回一个方法的名称。
- [method_getImplementation](<method_getimplementation(__).md>) — 返回一个方法的实现。
- [method_getTypeEncoding](<method_gettypeencoding(__).md>) — 返回一个描述方法参数和返回类型的字符串。
- [method_copyReturnType](<method_copyreturntype(__).md>) — 返回一个描述方法返回类型的字符串。
- [method_copyArgumentType](<method_copyargumenttype(____).md>) — 返回一个描述方法单个参数类型的字符串。
- [method_getReturnType](<method_getreturntype(______).md>) — 通过引用返回一个描述方法返回类型的字符串。
- [method_getNumberOfArguments](<method_getnumberofarguments(__).md>) — 返回一个方法所接受的参数数量。
- [method_getArgumentType](<method_getargumenttype(________).md>) — 通过引用返回一个描述方法单个参数类型的字符串。
- [method_getDescription](<method_getdescription(__).md>) — 返回指定方法的方法描述结构体。 _(已废弃)_
- [method_setImplementation](<method_setimplementation(____).md>) — 设置一个方法的实现。
