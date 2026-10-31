---
title: method_invoke_stret
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/method_invoke_stret
source_url: 'https://developer.apple.com/documentation/objectivec/method_invoke_stret'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/method_invoke_stret.json'
content_hash: 'sha256:459b8abc8ea6a7d5'
translated: true
---


> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# method_invoke_stret

<sub>函数</sub>

调用返回数据结构的指定方法的实现。

<sub>macOS</sub>

```objc
extern void method_invoke_stret();
```

## 参数

- **`receiver`** — 指向你要在其上调用方法的类实例的指针。此值不得为 `nil`。
- **`method`** — 你要调用其实现的方法。
- **`...`** — 包含该方法参数的可变参数列表。

## 讨论

使用此函数调用方法实现，比调用 [method_getImplementation](<method_getimplementation(__).md>) 和 [method_getName](<method_getname(__).md>) 更快。

## 另请参阅

### 使用方法

- [method_invoke](method_invoke.md) — Calls the implementation of a specified method.
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
- [method_exchangeImplementations](<method_exchangeimplementations(____).md>) — 交换两个方法的实现。
