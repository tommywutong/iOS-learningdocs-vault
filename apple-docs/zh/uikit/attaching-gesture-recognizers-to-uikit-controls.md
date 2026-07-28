---
title: 将手势识别器附加到 UIKit 控制
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/attaching-gesture-recognizers-to-uikit-controls
source_url: 'https://developer.apple.com/documentation/uikit/attaching-gesture-recognizers-to-uikit-controls'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/attaching-gesture-recognizers-to-uikit-controls.json'
content_hash: 'sha256:f51058f0cd402f27'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [触摸、按压与手势](touches-presses-and-gestures.md) · [协调多个手势识别器](coordinating-multiple-gesture-recognizers.md)

# 将手势识别器附加到 UIKit 控制

<sub>文章</sub>

了解手势识别器（gesture recognizer）如何与按钮、切换和滑块等 UIKit 控制（control）进行交互。

## 概述

附加到视图的手势识别器不会影响 UIKit 控制处理事件的能力。控制边界内发生的事件会先由该控制处理，让控制有机会调用其操作方法。具体而言，UIKit 控制会在以下情况下调用其操作方法：

- 在 [UIButton](uibutton.md)、[UISwitch](uiswitch.md)、[UIStepper](uistepper.md)、[UISegmentedControl](uisegmentedcontrol.md) 或 [UIPageControl](uipagecontrol.md) 对象上发生单指单次点按。
- 在 [UISlider](uislider.md) 对象的滑块上发生与滑块方向平行的单指轻扫。
- 在 [UISwitch](uiswitch.md) 对象的滑块上发生与切换方向平行的单指平移。

若要在控制调用其操作方法之前处理上述任一手势，请将手势识别器安装到控制本身。手势识别器会先于其所附加的视图处理触摸事件。因此，直接在控制上安装手势识别器会阻止该控制调用其操作方法。

> [!important] 重要
> 更改标准控制的默认行为前，务必查阅特定平台的《人机界面指南》。有关更多信息，请参阅[人机界面指南](https://developer.apple.com/design/human-interface-guidelines/platforms/overview)。

## 另请参阅

### 同时识别手势

- [使一个手势优先于另一个手势](preferring-one-gesture-over-another.md) — 使用手势识别器委托（delegate）对象来确定视图中手势的识别顺序。
- [允许同时识别多个手势](allowing-the-simultaneous-recognition-of-multiple-gestures.md) — 了解如何使用委托对象来允许一次检测多个手势。
