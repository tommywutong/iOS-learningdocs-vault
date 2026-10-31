---
title: accessInstanceVariablesDirectly
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessinstancevariablesdirectly
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessinstancevariablesdirectly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessinstancevariablesdirectly.json'
content_hash: 'sha256:0a0387d7bcd5671b'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessInstanceVariablesDirectly

<sub>类型属性</sub>

返回一个布尔值，指示在找不到属性的访问器方法时，键值编码方法是否应直接访问对应的实例变量。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var accessInstanceVariablesDirectly: Bool { get }
```

## 返回值

如果在找不到属性的访问器方法时键值编码方法应直接访问对应实例变量，则为 [YES](../yes.md)；否则为 [NO](../no.md)。

## 讨论

默认返回 [YES](../yes.md)。子类可重写以返回 [NO](../no.md)，此时键值编码方法将不会访问实例变量。
