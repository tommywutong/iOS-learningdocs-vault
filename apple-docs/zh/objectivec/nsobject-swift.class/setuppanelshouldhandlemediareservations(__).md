---
title: 'setupPanelShouldHandleMediaReservations(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/setuppanelshouldhandlemediareservations(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setuppanelshouldhandlemediareservations(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/setuppanelshouldhandlemediareservations%28_%3A%29.json'
content_hash: 'sha256:1ff2c3950d35f9a6'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# setupPanelShouldHandleMediaReservations(_:)

<sub>实例方法</sub>

此委托方法允许委托控制如何处理媒体预留。

<sub>macOS</sub>

```swift
func setupPanelShouldHandleMediaReservations(_ aPanel: DRSetupPanel!) -> Bool
```

## 参数

- `aPanel` — 发送消息的设置面板。

## 返回值

## 讨论

返回 `NO` 表示委托将处理媒体预留。返回 `YES` 表示 setupPanel 应自行处理媒体预留。
