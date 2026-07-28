---
title: 计算 Apple Pencil 的垂直作用力
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/computing-the-perpendicular-force-of-apple-pencil
source_url: 'https://developer.apple.com/documentation/uikit/computing-the-perpendicular-force-of-apple-pencil'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/computing-the-perpendicular-force-of-apple-pencil.json'
content_hash: 'sha256:08ef8013b6adb06d'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [Apple Pencil 交互](apple-pencil-interactions.md) · [处理来自 Apple Pencil 的输入](handling-input-from-apple-pencil.md)

# 计算 Apple Pencil 的垂直作用力

<sub>文章</sub>

调整 Apple Pencil 报告的作用力值，使其与 3D Touch 的作用力值一致。

## 概述

在 3D Touch 设备上，系统测量的是人手指垂直作用于屏幕表面的力。但 Apple Pencil 报告的作用力是沿其长轴测量的，而长轴通常并不垂直于屏幕。你可能不想直接使用 Apple Pencil 的作用力值，而是只计算其中垂直于屏幕的分量，这样便可用同一套代码处理来自人手指或 Apple Pencil 的触摸。

以下代码展示了如何为 [UITouch](uitouch.md) 类添加 `perpendicularForce` 属性，以报告 Apple Pencil 施加的垂直作用力。对于涉及 Apple Pencil 的触摸，此方法将报告的作用力值除以 Apple Pencil 高度角的正弦值。对于其他触摸，它会报告现有的作用力值。

```swift
extension UITouch {
    var perpendicularForce: CGFloat {
        if type == .pencil {
            return force / sin(altitudeAngle)
        } else {
            return force
        }
    }
}

```
