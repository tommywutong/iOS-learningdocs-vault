---
title: 使用 Core Foundation 类型
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/working-with-core-foundation-types
source_url: 'https://developer.apple.com/documentation/swift/working-with-core-foundation-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/working-with-core-foundation-types.json'
content_hash: 'sha256:669756897a195949'
translated: true
---

> 导航： [Technologies](../technologies.md) · [Swift](../swift.md) · [Imported C and Objective-C APIs](imported-c-and-objective-c-apis.md)

# 使用 Core Foundation 类型

<sub>文章</sub>

在 Swift 代码中直接使用内存管理的 Core Foundation 类型，并按需手动处理 retain 操作。

## 概述

导入 Core Foundation 框架时，它的类型会被导入为 Swift 类。凡是提供了内存管理注解的地方，Swift 都会自动管理 Core Foundation 对象的内存，包括你自己实例化的 Core Foundation 对象。在 Swift 中，每一对免费桥接（toll-free bridged）的 Foundation 与 Core Foundation 类型都可以互换使用。你还可以先把某些免费桥接的 Core Foundation 类型转换为桥接的 Foundation 类型，再把它们桥接为 Swift 标准库类型。更多信息参见[免费桥接（Toll-Free Bridging）](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2)。

### 使用受内存管理的对象

Swift 导入 Core Foundation 类型时，编译器会重新映射这些类型的名称。编译器会去掉每个类型名末尾的 `Ref`，因为所有 Swift 类都是引用类型，这个后缀是多余的。`CFTypeRef` 类型则完全重新映射为 `AnyObject` 类型。

从带有注解的 API 返回的 Core Foundation 对象，在 Swift 中会自动进行内存管理——你无需自己调用 `CFRetain`、`CFRelease` 或 `CFAutorelease` 函数。

如果你在自己的 C 函数和 Objective-C 方法中返回 Core Foundation 对象，可以用 `CF_RETURNS_RETAINED` 或 `CF_RETURNS_NOT_RETAINED` 宏为它们添加注解，从而自动插入内存管理调用。你也可以使用 `CF_IMPLICIT_BRIDGING_ENABLED` 和 `CF_IMPLICIT_BRIDGING_DISABLED` 宏，把遵循 Core Foundation 所有权命名规范的 C 函数声明包裹起来，以便推断内存管理方式。

### 将 Unmanaged 对象转换为受内存管理的对象

Swift 导入未经注解的 API 时，编译器无法自动对返回的 Core Foundation 对象进行内存管理。Swift 会把这些返回的 Core Foundation 对象包装在 [Unmanaged](unmanaged.md) 结构体中。所有间接返回的 Core Foundation 对象同样不受内存管理。例如，下面是一个未经注解的 C 函数：

```occ
CFStringRef StringByAddingTwoStrings(CFStringRef s1, CFStringRef s2)
```

Swift 导入它的方式如下：

```swift
func StringByAddingTwoStrings(_: CFString!, _: CFString!) -> Unmanaged<CFString>! {
    // ...
}
```

当你从未经注解的 API 收到一个不受内存管理的对象时，先立即把它转换成受内存管理的对象，再开始使用。这样 Swift 就能替你处理内存管理。

`Unmanaged` 结构体提供了两个把不受内存管理的对象转换为受内存管理对象的方法——`takeUnretainedValue()` 和 `takeRetainedValue()`。这两个方法都返回对象原始的、未包装的类型。具体选用哪个方法，取决于你调用的 API 返回的是不保留（unretained）还是保留（retained）的对象。

例如，假设上面的 C 函数在返回 `CFString` 对象之前没有保留（retain）它。要开始使用这个对象，你需要调用 `takeUnretainedValue()` 函数。

```swift
let memoryManagedResult = StringByAddingTwoStrings(str1, str2).takeUnretainedValue()
// memoryManagedResult 是一个受内存管理的 CFString
```

你也可以在不受内存管理的对象上调用 `retain()`、`release()` 和 `autorelease()` 方法，但不推荐这样做。

更多信息参见《[Core Foundation 内存管理编程指南](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i)》中的[所有权策略（Ownership Policy）](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148)。

## 另请参阅

### Cocoa 框架

- [使用 Foundation 类型](working-with-foundation-types.md) —— 在 Swift 代码库中使用桥接的 Foundation 类型处理日期、时间及其他值。
