---
title: 'originalString(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/originalstring(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/originalstring(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/originalstring%28_%3A%29.json'
content_hash: 'sha256:9918d810489a5129'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# originalString(_:)

<sub>实例方法</sub>

返回由预组合 Unicode 字符组成的字符串。

<sub>macOS</sub>

```swift
func originalString(_ sender: Any!) -> NSAttributedString!
```

## 参数

- `sender` — 请求原始字符串的客户端对象。

## 返回值

预组合 Unicode 字符的原始字符串。如果输入法存储了原始输入文本，则返回该文本。返回值是归因字符串，以便输入法在需要时可以附加自定义属性。
