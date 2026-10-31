---
title: 'title(for:identifier:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/title(for:identifier:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/title(for:identifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/title%28for%3Aidentifier%3A%29.json'
content_hash: 'sha256:569d1738de213386'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# title(for:identifier:)

<sub>实例方法</sub>

发送给委托以请求该操作的菜单项标题。

<sub>macOS</sub>

```swift
func title(for person: ABPerson!, identifier: String!) -> String!
```

## 参数

- `person` — 将对其执行操作的联系人。

- `identifier` — 将为其显示菜单项的值的唯一标识符。

## 返回值

该操作的菜单项标题。

## 讨论

若 [- actionProperty](<actionproperty().md>) 返回的属性是多值属性，则 `identifier` 包含所选值的唯一标识符。
