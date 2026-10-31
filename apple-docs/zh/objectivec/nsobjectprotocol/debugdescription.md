---
title: debugDescription
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobjectprotocol/debugdescription
source_url: 'https://developer.apple.com/documentation/objectivec/nsobjectprotocol/debugdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobjectprotocol/debugdescription.json'
content_hash: 'sha256:1173fd24ab1e6d0a'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# debugDescription

<sub>实例属性</sub>

供调试器使用的接收者文本表示。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional var debugDescription: String { get }
```

## 返回值

出于调试目的描述该对象的字符串。

## 讨论

调试器的 `po` 命令使用此属性创建适合在调试器中显示的对象文本表示。默认实现返回与 [description](description.md) 相同的值。重写任一属性以提供自定义对象描述。

## 另请参阅

### 描述对象

- [description](description.md) — 接收者的文本表示。
