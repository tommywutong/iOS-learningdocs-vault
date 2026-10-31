---
title: 'performAction(for:identifier:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/performaction(for:identifier:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/performaction(for:identifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/performaction%28for%3Aidentifier%3A%29.json'
content_hash: 'sha256:515eddfb3e2c9c3c'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# performAction(for:identifier:)

<sub>实例方法</sub>

发送给委托以执行该操作。

<sub>macOS</sub>

```swift
func performAction(for person: ABPerson!, identifier: String!)
```

## 参数

- `person` — 将对其执行操作的联系人。

- `identifier` — 所选值的唯一标识符。

## 讨论

若 [- actionProperty](<actionproperty().md>) 返回的属性是多值属性，则 `identifier` 包含所选值的唯一标识符。当访问翻转菜单时，地址簿应用名片视图中显示的联系人会作为 `person` 传入。
