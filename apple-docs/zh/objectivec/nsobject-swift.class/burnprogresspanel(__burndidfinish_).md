---
title: 'burnProgressPanel(_:burnDidFinish:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/burnprogresspanel(_:burndidfinish:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/burnprogresspanel(_:burndidfinish:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/burnprogresspanel%28_%3Aburndidfinish%3A%29.json'
content_hash: 'sha256:e13166c5ac6cbc9d'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# burnProgressPanel(_:burnDidFinish:)

<sub>实例方法</sub>

允许委托处理刻录结束反馈。

<sub>macOS</sub>

```swift
func burnProgressPanel(_ theBurnPanel: DRBurnProgressPanel!, burnDidFinish burn: DRBurn!) -> Bool
```

## 参数

- `theBurnPanel` — 进度面板

- `burn` — 执行刻录的对象。

## 返回值

一个 `BOOL`，指示是否应发生正常的刻录结束反馈。

## 讨论

此方法允许委托处理或修改进度面板执行的刻录结束反馈。返回 `YES` 表示委托已处理刻录完成，应抑制标准反馈。若此方法返回 `NO`，则执行正常的刻录结束处理（在适当时显示错误、播放“完成”提示音等）。

在进度面板被收起之前会向委托发送消息，以便可在以窗口显示的进度面板上展示表单。
