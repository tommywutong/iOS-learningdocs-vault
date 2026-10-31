---
title: 'inputText(_:client:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/inputtext(_:client:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/inputtext(_:client:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/inputtext%28_%3Aclient%3A%29.json'
content_hash: 'sha256:a318365861469724'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# inputText(_:client:)

<sub>实例方法</sub>

处理未映射到操作方法的按键按下事件。

<sub>macOS</sub>

```swift
func inputText(_ string: String!, client sender: Any!) -> Bool
```

## 参数

- `string` — 按键按下事件，即客户端输入的文本。

- `sender` — 发送按键按下事件的客户端对象。

## 返回值

若输入被接受则为 [YES](../yes.md)；否则为 [NO](../no.md)。

## 讨论

使用键绑定（即实现 [- didCommandBySelector:client:](<didcommand(by_client_).md>)）时，输入法应实现此方法。
