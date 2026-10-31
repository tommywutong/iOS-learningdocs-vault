---
title: 'eraseProgressPanel(_:eraseDidFinish:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/eraseprogresspanel(_:erasedidfinish:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/eraseprogresspanel(_:erasedidfinish:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/eraseprogresspanel%28_%3Aerasedidfinish%3A%29.json'
content_hash: 'sha256:fadc1e63aae91d11'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# eraseProgressPanel(_:eraseDidFinish:)

<sub>实例方法</sub>

面板在显示前发送的通知。

<sub>macOS</sub>

```swift
func eraseProgressPanel(_ theErasePanel: DREraseProgressPanel!, eraseDidFinish erase: DRErase!) -> Bool
```

## 参数

- `theErasePanel` — 进度面板

- `erase` — 执行擦除的对象。

## 讨论

此方法允许委托处理或修改进度面板执行的刻录结束反馈。返回 `YES` 表示委托已处理刻录完成，应抑制标准反馈。若此方法返回 `NO`，则执行正常的刻录结束处理（在适当时显示错误、播放“完成”提示音等）。

在进度面板被收起之前会向委托发送消息，以便可在以窗口显示的进度面板上展示表单。
