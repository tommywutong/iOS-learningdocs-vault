---
title: 'inputText(_:key:modifiers:client:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/inputtext(_:key:modifiers:client:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/inputtext(_:key:modifiers:client:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/inputtext%28_%3Akey%3Amodifiers%3Aclient%3A%29.json'
content_hash: 'sha256:dd9e0eb752d3df20'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# inputText(_:key:modifiers:client:)

<sub>实例方法</sub>

接收 Unicode、生成它的键码以及任何修饰键标志。

<sub>macOS</sub>

```swift
func inputText(_ string: String!, key keyCode: Int, modifiers flags: Int, client sender: Any!) -> Bool
```

## 参数

- `string` — 客户端输入的文本。

- `keyCode` — 关联 Unicode 的键码。

- `flags` — 修饰键标志。

- `sender` — 客户端对象。

## 返回值

若输入被接受则为 [YES](../yes.md)；否则为 [NO](../no.md)。
