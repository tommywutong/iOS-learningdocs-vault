---
title: 'eraseProgressPanelDidFinish(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/eraseprogresspaneldidfinish(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/eraseprogresspaneldidfinish(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/eraseprogresspaneldidfinish%28_%3A%29.json'
content_hash: 'sha256:ab60b3f5e6dc0362'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# eraseProgressPanelDidFinish(_:)

<sub>实例方法</sub>

面板在 order out 之后发送的通知。

<sub>macOS</sub>

```swift
func eraseProgressPanelDidFinish(_ aNotification: Notification!)
```

## 参数

- `aNotification` — 始终为 `DREraseProgressPanelDidFinishNotification`。你可以通过向 `aNotification` 发送 [object](../../foundation/nsnotification/object.md) 来检索相关的 `DREraseProgressPanel` 对象。

## 讨论

如果委托实现此方法，会在面板从显示中移除后收到该消息。
