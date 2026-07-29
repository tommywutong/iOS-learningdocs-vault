---
title: 使用预测触控减少延迟
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/minimizing-latency-with-predicted-touches
source_url: 'https://developer.apple.com/documentation/uikit/minimizing-latency-with-predicted-touches'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/minimizing-latency-with-predicted-touches.json'
content_hash: 'sha256:0ea14f98dc8fcbcf'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [触控、按压与手势](touches-presses-and-gestures.md) · [在你的视图中处理触控](handling-touches-in-your-view.md)

# 使用预测触控减少延迟

利用 UIKit 对触控位置的预测，打造流畅且响应灵敏的绘图体验。

## 概述

UIKit 生成触摸事件并将其交付给你的 App 需要时间，你的 App 处理这些事件并渲染结果也需要时间。实际上，这段时间足以让人感知到手指或 Apple Pencil 的移动与渲染结果之间的延迟。为了尽量减少触摸输入与渲染内容之间的感知延迟，你可以在事件处理中加入预测触控（predicted touches）。

预测触控是系统对下一次触摸事件可能发生位置的最佳猜测。下图以绘图 App 为例说明了这一概念。当绘图序列开始时，UIKit 利用手指或 Apple Pencil 先前的触摸位置，预测下一次触摸可能发生的位置。UIKit 会为这些预测位置生成额外的 [UITouch](uitouch.md) 对象，并使它们可供你的 App 使用。

![一张示意图，展示 Apple Pencil 描绘路径，包括实际和预测的触控位置。](../../../attachments/dd9aa41d1e2d957b7b087f4769b37bf7/media-3004386@2x.png)

若要检索预测的触控数据，请调用包含原始 [UITouch](uitouch.md) 对象的 [UIEvent](uievent.md) 对象的 [- predictedTouchesForTouch:](<uievent/predictedtouches(for_).md>) 方法。该方法会返回一个数组，内含预计在最后一次实际触摸之后发生的预测触控。在你的 App 中，始终将预测触控视为临时数据，并在收到每个新的触摸事件时将其丢弃。

## 主题

### 示例

- [在 App 中整合预测触控](incorporating-predicted-touches-into-an-app.md)——了解如何创建一个在其绘图代码中整合了预测触控的简单 App。

## 另请参阅

### 高级触控处理

- [实现 Multi-Touch App](implementing-a-multi-touch-app.md)——了解如何创建一个处理多点触控输入的简单 App。
- [使用合并触控获取高保真输入](getting-high-fidelity-input-with-coalesced-touches.md)——了解如何在你的 App 中支持高精度触控。
