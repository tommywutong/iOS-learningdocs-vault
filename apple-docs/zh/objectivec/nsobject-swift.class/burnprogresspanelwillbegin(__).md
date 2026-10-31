---
title: 'burnProgressPanelWillBegin(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/burnprogresspanelwillbegin(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/burnprogresspanelwillbegin(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/burnprogresspanelwillbegin%28_%3A%29.json'
content_hash: 'sha256:ab8f0c7e78e7e1f3'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# burnProgressPanelWillBegin(_:)

<sub>实例方法</sub>

面板在显示之前发送的通知。

<sub>macOS</sub>

```swift
func burnProgressPanelWillBegin(_ aNotification: Notification!)
```

## 参数

- `aNotification` — 始终为 `DRBurnProgressPanelDidFinishNotification`

## 讨论

如果委托实现此方法，会在面板即将显示之前收到该消息。
