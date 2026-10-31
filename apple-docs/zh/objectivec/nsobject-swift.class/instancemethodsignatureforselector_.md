---
title: 'instanceMethodSignatureForSelector:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/instancemethodsignatureforselector:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/instancemethodsignatureforselector:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/instancemethodsignatureforselector%3A.json'
content_hash: 'sha256:9d40fdd7479d157b'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# instanceMethodSignatureForSelector:

<sub>类型方法</sub>

返回包含由给定选择器标识的实例方法描述的 `NSMethodSignature` 对象。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSMethodSignature *) instanceMethodSignatureForSelector:(SEL) aSelector;
```

## 参数

- `aSelector` — 标识要返回其实现地址的方法的 [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48)。

## 返回值

包含由 `aSelector` 标识的实例方法描述的 `NSMethodSignature` 对象；若找不到该方法则为 `nil`。

## 另请参阅

### 获取方法信息

- [- methodForSelector:](<method(for_).md>) — 定位并返回接收者某个方法实现的地址，以便可将其作为函数调用。
- [+ instanceMethodForSelector:](<instancemethod(for_).md>) — 定位并返回由给定选择器标识的实例方法实现的地址。
- [methodSignatureForSelector:](methodsignatureforselector_.md) — 返回包含由给定选择器标识的方法描述的 `NSMethodSignature` 对象。
