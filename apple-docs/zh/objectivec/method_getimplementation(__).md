---
title: 'method_getImplementation(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/method_getimplementation(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/method_getimplementation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/method_getimplementation%28_%3A%29.json'
content_hash: 'sha256:c71215b2f63db88f'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# method_getImplementation(_:)

<sub>函数</sub>

返回一个方法的实现。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func method_getImplementation(_ m: Method) -> IMP
```

## 参数

- `m` — 要检查的方法。

## 返回值

类型为 `IMP` 的函数指针。

## 另请参阅

### 使用方法

- [method_getName](<method_getname(__).md>) — 返回一个方法的名称。
- [method_getTypeEncoding](<method_gettypeencoding(__).md>) — 返回一个描述方法参数和返回类型的字符串。
- [method_copyReturnType](<method_copyreturntype(__).md>) — 返回一个描述方法返回类型的字符串。
- [method_copyArgumentType](<method_copyargumenttype(____).md>) — 返回一个描述方法单个参数类型的字符串。
- [method_getReturnType](<method_getreturntype(______).md>) — 通过引用返回一个描述方法返回类型的字符串。
- [method_getNumberOfArguments](<method_getnumberofarguments(__).md>) — 返回一个方法所接受的参数数量。
- [method_getArgumentType](<method_getargumenttype(________).md>) — 通过引用返回一个描述方法单个参数类型的字符串。
- [method_getDescription](<method_getdescription(__).md>) — 返回指定方法的方法描述结构体。 _(已废弃)_
- [method_setImplementation](<method_setimplementation(____).md>) — 设置一个方法的实现。
- [method_exchangeImplementations](<method_exchangeimplementations(____).md>) — 交换两个方法的实现。
