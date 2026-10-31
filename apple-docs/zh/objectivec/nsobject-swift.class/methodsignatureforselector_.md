---
title: 'methodSignatureForSelector:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/methodsignatureforselector:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/methodsignatureforselector:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/methodsignatureforselector%3A.json'
content_hash: 'sha256:a67811a18c39f1be'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# methodSignatureForSelector:

<sub>实例方法</sub>

返回一个包含由给定选择器标识的方法描述的 `NSMethodSignature` 对象。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSMethodSignature *) methodSignatureForSelector:(SEL) aSelector;
```

## 参数

- `aSelector` — 标识要返回其实现地址的方法的 [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48)。当接收者是实例时，`aSelector` 应标识实例方法；当接收者是类时，应标识类方法。

## 返回值

包含由 `aSelector` 标识的方法描述的 `NSMethodSignature` 对象；若找不到该方法则为 `nil`。

## 讨论

此方法用于协议的实现。此方法也用于必须创建 `NSInvocation` 对象的情况，例如在消息转发期间。若你的对象维护委托，或能够处理其未直接实现的消息，则应重写此方法以返回适当的方法签名。

## 另请参阅

### 相关文档

- [forwardInvocation:](forwardinvocation_.md) — 由子类重写，以便将消息转发给其他对象。

### 获取方法信息

- [- methodForSelector:](<method(for_).md>) — 定位并返回接收者某个方法实现的地址，以便可将其作为函数调用。
- [+ instanceMethodForSelector:](<instancemethod(for_).md>) — 定位并返回由给定选择器标识的实例方法实现的地址。
- [instanceMethodSignatureForSelector:](instancemethodsignatureforselector_.md) — 返回包含由给定选择器标识的实例方法描述的 `NSMethodSignature` 对象。
