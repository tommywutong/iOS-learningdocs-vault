---
title: 'method(for:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/method(for:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/method(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/method%28for%3A%29.json'
content_hash: 'sha256:36277790a58e0ddc'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# method(for:)

<sub>实例方法</sub>

定位并返回接收者某个方法实现的地址，以便可将其作为函数调用。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func method(for aSelector: Selector!) -> IMP!
```

## 参数

- `aSelector` — 一个 [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48)，标识要返回其实现地址的方法。选择器必须有效且非 `NULL`。若有疑问，请在将选择器传给 [- methodForSelector:](<method(for_).md>) 之前使用 [- respondsToSelector:](<../nsobjectprotocol/responds(to_).md>) 方法进行检查。

## 返回值

接收者对 `aSelector` 实现的地址。

## 讨论

若接收者是实例，`aSelector` 应引用实例方法；若接收者是类，则应引用类方法。

## 另请参阅

### 获取方法信息

- [+ instanceMethodForSelector:](<instancemethod(for_).md>) — 定位并返回由给定选择器标识的实例方法实现的地址。
