---
title: 'method_getDescription(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（15.0 起废弃）, iPadOS 2.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, macOS 10.5+（11.0 起废弃）, tvOS 9.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（8.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/method_getdescription(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/method_getdescription(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/method_getdescription%28_%3A%29.json'
content_hash: 'sha256:b6d070bad5902e7b'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# method_getDescription(_:)

<sub>函数</sub>

返回指定方法的方法描述结构体。

> [!warning] 已废弃
> Use method_getName and method_getTypeEncoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func method_getDescription(_ m: Method) -> UnsafeMutablePointer<objc_method_description>
```

## 参数

- `m` — 你想查询的方法。

## 返回值

描述由 `m` 指定的方法的 `objc_method_description` 结构体。

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
- [method_setImplementation](<method_setimplementation(____).md>) — 设置一个方法的实现。
- [method_exchangeImplementations](<method_exchangeimplementations(____).md>) — 交换两个方法的实现。
