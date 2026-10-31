---
title: 'resolveClassMethod(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/resolveclassmethod(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/resolveclassmethod(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/resolveclassmethod%28_%3A%29.json'
content_hash: 'sha256:3c6f7cec39a2eea1'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# resolveClassMethod(_:)

<sub>类型方法</sub>

为类方法的给定选择器动态提供实现。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func resolveClassMethod(_ sel: Selector!) -> Bool
```

## 参数

- `sel` — 要解析的选择器的名称。

## 返回值

若找到该方法并将其添加到接收者则为 [YES](../yes.md)，否则为 [NO](../no.md)。

## 讨论

此方法允许你为给定选择器动态提供实现。进一步讨论请参阅 [+ resolveInstanceMethod:](<resolveinstancemethod(__).md>)。

## 另请参阅

### 动态解析方法

- [+ resolveInstanceMethod:](<resolveinstancemethod(__).md>) — 为实例方法的给定选择器动态提供实现。
