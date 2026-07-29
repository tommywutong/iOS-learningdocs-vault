---
title: 自定义绘图
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/customizing-drawings
source_url: 'https://developer.apple.com/documentation/uikit/customizing-drawings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/customizing-drawings.json'
content_hash: 'sha256:664fa51e3ca5b815'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [绘图](drawing.md) · [UIColor](uicolor.md)

# 自定义绘图

<sub>文章</sub>

在你的 App 中创建用于绘图的颜色和图案。

## 概述

你可以自定义 App 中的颜色，包括背景色和色调颜色（tint color），以及 App 用户可用的绘图样式。

### 设置自定义背景色和色调颜色

使用 [UIColor](uicolor.md) 对象最常见的方式是将其与 UIKit 中的其他对象组合使用。将 [UIColor](uicolor.md) 与 UIKit 中的对象结合使用，可以让你创建并自定义 App 的 UI。例如，[UIView](uiview.md) 类（及其子类）包含背景色和色调颜色，以影响它们在屏幕上的绘制方式。以下代码示例设置了一个视图的背景色和色调颜色。

```swift
backgroundView.backgroundColor = UIColor.systemGray
backgroundView.tintColor = UIColor.systemBlue
```

### 创建自定义颜色和绘图样式

在 App 中自定义绘图时，[UIColor](uicolor.md) 对象提供了设置当前图形上下文的填充或描边颜色的方法。这些方法可以设置对象的颜色，并创建各种图案和样式。以下代码展示了一个视图内自定义绘图的简单示例。

```swift
class CircleView: UIView {
    
    override func draw(_ rect: CGRect) {
        let ovalBounds = self.bounds.insetBy(dx: 10, dy: 10)
        let oval = UIBezierPath(ovalIn: ovalBounds)
        let brightRed = UIColor(displayP3Red: 1.0, green: 0.0, blue: 0.0, alpha: 1.0)
        brightRed.setFill()
        oval.fill()
    }
}
```

## 另请参阅

### 将颜色应用于绘图环境

- [- set](<uicolor/set().md>) — 将后续描边和填充操作的颜色设置为接收者所表示的颜色。
- [- setFill](<uicolor/setfill().md>) — 将后续填充操作的颜色设置为接收者所表示的颜色。
- [- setStroke](<uicolor/setstroke().md>) — 将后续描边操作的颜色设置为接收者所表示的颜色。
