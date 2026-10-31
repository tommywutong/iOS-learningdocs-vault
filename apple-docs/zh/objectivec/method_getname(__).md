---
title: 'method_getName(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/method_getname(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/method_getname(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/method_getname%28_%3A%29.json'
content_hash: 'sha256:bb7af84630c39d6b'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# method_getName(_:)

<sub>函数</sub>

返回一个方法的名称。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func method_getName(_ m: Method) -> Selector
```

## 参数

- `m` — 要检查的方法。

## 返回值

类型为 SEL 的指针。

## 讨论

若要以 C 字符串形式获取方法名称，请调用 `sel_getName(method_getName(method))`。

## 另请参阅

### 使用方法

- [method_getImplementation](<method_getimplementation(__).md>) — 返回一个方法的实现。
- [method_getTypeEncoding](<method_gettypeencoding(__).md>) — 返回一个描述方法参数和返回类型的字符串。
- [method_copyReturnType](<method_copyreturntype(__).md>) — 返回一个描述方法返回类型的字符串。
- [method_copyArgumentType](<method_copyargumenttype(____).md>) — 返回一个描述方法单个参数类型的字符串。
- [method_getReturnType](<method_getreturntype(______).md>) — 通过引用返回一个描述方法返回类型的字符串。
- [method_getNumberOfArguments](<method_getnumberofarguments(__).md>) — 返回一个方法所接受的参数数量。
- [method_getArgumentType](<method_getargumenttype(________).md>) — 通过引用返回一个描述方法单个参数类型的字符串。
- [method_getDescription](<method_getdescription(__).md>) — 返回指定方法的方法描述结构体。 _(已废弃)_
- [method_setImplementation](<method_setimplementation(____).md>) — 设置一个方法的实现。
- [method_exchangeImplementations](<method_exchangeimplementations(____).md>) — 交换两个方法的实现。
