---
title: 在布局外边距内定位内容
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/positioning-content-within-layout-margins
source_url: 'https://developer.apple.com/documentation/uikit/positioning-content-within-layout-margins'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/positioning-content-within-layout-margins.json'
content_hash: 'sha256:9f151ab999a1e9ef'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [View layout](view-layout.md)

# 在布局外边距内定位内容

<sub>文章</sub>

对视图进行定位，使其不被其他内容挤占空间。

## 概述

布局外边距在视图的内容与视图边界之外的任何内容之间提供了一道视觉缓冲。布局外边距由该视图各条边（顶部、底部、前缘和后缘）的边距值组成。这些边距值在视图边界矩形的边缘与视图内部的内容之间创造出一段空间。下图展示了两个具有不同外边距设置的视图。除了在你的内容周围增加的空白之外，外边距没有任何可见的表现形式。

![一张说明视图外边距的示意图。](../../../attachments/8c4cf9ba8dc6a1bc9952e15279e51e90/media-2927043@2x.png)

要设置遵从布局外边距的约束，请在 Xcode 中启用 `Constrain to margins` 选项，如下图所示。（如果你不启用该选项，Xcode 会相对于视图的边界矩形创建约束。）如果父视图的外边距之后发生变化，与这些外边距绑定的元素的位置会相应地更新。

![一张显示 Xcode 中添加约束对话框的截图，其中高亮了 `Constrain to margins` 复选框。](../../../attachments/d811e6e7f9a732099544a5ab4ac28e74/positioning-content-within-layout-margins-1@2x.png)

即使你没有使用约束来定位内容，仍然可以相对于视图的布局外边距手动定位内容。每个视图的 [directionalLayoutMargins](uiview/directionallayoutmargins.md) 属性包含了该视图外边距所使用的边距值。在计算视图中各项目的位置时，请把这些外边距值纳入考量。

### 更改默认的布局外边距

UIKit 为每个视图提供了默认的布局外边距，但你可以把默认值更改为更适合你视图的值。要更改某个视图的外边距值，请更新该视图的 [directionalLayoutMargins](uiview/directionallayoutmargins.md) 属性。（你也可以使用 Size inspector 在设计时设置该属性的值。在 Layout Margins 部分中，选择 Language Directional 选项，并为视图的每条边输入外边距值，如下图所示。）

![一张显示使用 Size inspector 设置外边距的截图。](../../../attachments/2f2896f2d218486530181f446b27dee6/positioning-content-within-layout-margins-2@2x.png)

对于视图控制器的根视图，UIKit 会强制施加一组最小布局外边距，以确保内容能正确显示。当 [directionalLayoutMargins](uiview/directionallayoutmargins.md) 属性中的值小于最小值时，UIKit 会改用这些最小值。你可以从视图控制器的 [systemMinimumLayoutMargins](uiviewcontroller/systemminimumlayoutmargins.md) 属性中获取最小外边距值。要让 UIKit 完全不应用这些最小外边距，请把你视图控制器的 [viewRespectsSystemMinimumLayoutMargins](uiviewcontroller/viewrespectssystemminimumlayoutmargins.md) 属性设为 false。

视图实际的外边距是根据该视图的配置及其 [directionalLayoutMargins](uiview/directionallayoutmargins.md) 属性的值计算得出的。视图的外边距会受到其 [insetsLayoutMarginsFromSafeArea](uiview/insetslayoutmarginsfromsafearea.md) 和 [preservesSuperviewLayoutMargins](uiview/preservessuperviewlayoutmargins.md) 属性设置的影响，这些设置可以增大默认外边距值，以确保你的内容获得恰当的间距。

## 另请参阅

### Constraints

- [Positioning content relative to the safe area](positioning-content-relative-to-the-safe-area.md) — 对视图进行定位，使其不被其他内容遮挡。
- [NSLayoutConstraint](nslayoutconstraint.md) — 两个用户界面对象之间必须由基于约束的布局系统所满足的关系。
- [UILayoutSupport](uilayoutsupport.md) — 一组提供布局支持并可访问布局锚点的方法。
