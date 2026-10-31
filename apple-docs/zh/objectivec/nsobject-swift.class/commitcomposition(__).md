---
title: 'commitComposition(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/commitcomposition(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/commitcomposition(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/commitcomposition%28_%3A%29.json'
content_hash: 'sha256:8a03dc9d11e8f568'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# commitComposition(_:)

<sub>实例方法</sub>

通知控制器应提交组合。

<sub>macOS</sub>

```swift
func commitComposition(_ sender: Any!)
```

## 参数

- `sender` — 请求输入法提交组合的客户端对象。

## 讨论

如果输入法实现此方法，则在客户端希望立即结束组合会话时调用它。典型响应是调用客户端的 `insertText` 方法，并向其传递当前组合字符串。
