---
title: 'shouldEnableAction(for:identifier:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/shouldenableaction(for:identifier:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/shouldenableaction(for:identifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/shouldenableaction%28for%3Aidentifier%3A%29.json'
content_hash: 'sha256:6e953bdea527102e'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# shouldEnableAction(for:identifier:)

<sub>实例方法</sub>

发送给委托以确定是否应启用该操作。

<sub>macOS</sub>

```swift
func shouldEnableAction(for person: ABPerson!, identifier: String!) -> Bool
```

## 参数

- `person` — 将对其执行操作的联系人。

- `identifier` — 所选值的唯一标识符。

## 返回值

若该操作适用则为 [YES](../yes.md)；否则为 [NO](../no.md)。

## 讨论

若 [- actionProperty](<actionproperty().md>) 返回的属性是多值属性，则 `identifier` 包含所选值的唯一标识符。
