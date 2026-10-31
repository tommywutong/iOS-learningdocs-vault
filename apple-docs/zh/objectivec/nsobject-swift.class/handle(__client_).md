---
title: 'handle(_:client:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/handle(_:client:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/handle(_:client:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/handle%28_%3Aclient%3A%29.json'
content_hash: 'sha256:874e19919e88ba6e'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# handle(_:client:)

<sub>实例方法</sub>

处理按键按下和鼠标事件。

<sub>macOS</sub>

```swift
func handle(_ event: NSEvent!, client sender: Any!) -> Bool
```

## 参数

- `event` — 要处理的事件。

- `sender` — 发送该事件的客户端对象。

## 返回值

若事件已处理则为 [YES](../yes.md)；否则为 [NO](../no.md)。
