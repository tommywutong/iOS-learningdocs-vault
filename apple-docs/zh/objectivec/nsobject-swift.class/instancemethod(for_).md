---
title: 'instanceMethod(for:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/instancemethod(for:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/instancemethod(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/instancemethod%28for%3A%29.json'
content_hash: 'sha256:ca4bb10643b08de2'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# instanceMethod(for:)

<sub>类型方法</sub>

定位并返回由给定选择器标识的实例方法实现的地址。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func instanceMethod(for aSelector: Selector!) -> IMP!
```

## 参数

- `aSelector` — 标识要返回其实现地址的方法的 [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48)。选择器必须非 `NULL` 且对接收者有效。若有疑问，请在将选择器传给 [- methodForSelector:](<method(for_).md>) 之前使用 [- respondsToSelector:](<../nsobjectprotocol/responds(to_).md>) 方法进行检查。

## 返回值

`aSelector` 实例方法实现的地址。

## 讨论

若接收者的实例无法响应 `aSelector` 消息，则会生成错误。

使用此方法仅向类对象查询实例方法的实现。若要查询类方法的实现，请改为向该类发送 [- methodForSelector:](<method(for_).md>) 实例方法。

## 另请参阅

### 获取方法信息

- [- methodForSelector:](<method(for_).md>) — 定位并返回接收者某个方法实现的地址，以便可将其作为函数调用。
