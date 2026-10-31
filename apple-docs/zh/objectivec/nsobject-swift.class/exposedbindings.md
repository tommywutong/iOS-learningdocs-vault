---
title: exposedBindings
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/exposedbindings
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/exposedbindings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/exposedbindings.json'
content_hash: 'sha256:654db8417a60320f'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# exposedBindings

<sub>实例属性</sub>

返回包含接收者所暴露绑定的数组。

<sub>macOS</sub>

```swift
var exposedBindings: [NSBindingName] { get }
```

## 返回值

包含接收者所暴露绑定的数组。

## 讨论

子类可以重写此方法，以移除超类暴露但不适合子类的绑定。

## 另请参阅

### 暴露绑定

- [+ exposeBinding:](<exposebinding(__).md>) — 暴露指定的 `binding`，公布其可用性。
