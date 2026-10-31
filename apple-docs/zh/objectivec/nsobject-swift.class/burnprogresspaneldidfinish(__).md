---
title: 'burnProgressPanelDidFinish(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/burnprogresspaneldidfinish(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/burnprogresspaneldidfinish(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/burnprogresspaneldidfinish%28_%3A%29.json'
content_hash: 'sha256:4cd35337c1b64121'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# burnProgressPanelDidFinish(_:)

<sub>实例方法</sub>

面板在 order out 之后发送的通知。

<sub>macOS</sub>

```swift
func burnProgressPanelDidFinish(_ aNotification: Notification!)
```

## 参数

- `aNotification` — 始终为 `DRBurnProgressPanelDidFinishNotification`

## 讨论

如果委托实现此方法，会在面板从显示中移除后收到该消息。
