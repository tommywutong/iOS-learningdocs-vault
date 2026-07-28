---
title: 滚动视图
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scroll-views
source_url: 'https://developer.apple.com/documentation/swiftui/scroll-views'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scroll-views.json'
content_hash: 'sha256:baad9b7528489a95'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md)

# 滚动视图

<sub>API 集合</sub>

使用户能够滚动查看在当前显示区域中无法完全显示的内容。

## 概述

当视图的内容无法在显示区域内完全展示时，你可以将该视图包装在一个 [ScrollView](scrollview.md) 中，以使用户能够在一个或多个轴向上进行滚动。通过视图修饰符来配置滚动视图。例如，你可以设置滚动指示器的可见性，或在某个维度上是否可以滚动。

![](../../../attachments/fc9311e17b13443bf22043d6155e0e7f/scroll-views-hero@2x.png)

你可以在滚动视图中放入任何类型的视图，但最常使用的场景是，某个布局容器中的元素过多，导致无法在显示区域内完全展示。对于放入滚动视图中的某些容器视图（例如惰性叠放 (lazy stacks)），容器只有在子视图即将可见或接近可见时才会加载它们。而对于其他容器（如常规叠放和网格），无论滚动状态如何，容器都会一次性加载所有内容。

[列表](lists.md)和[表格](tables.md)隐式地包含了滚动视图，因此你无需为这些容器类型额外添加滚动功能。不过，你可以使用适用于显式滚动视图的相同视图修饰符来配置它们隐式的滚动视图。

有关设计指导，请参阅《人机界面指南》中的[滚动视图](../design/human-interface-guidelines/scroll-views.md)。

## 主题

### 创建滚动视图

- [ScrollView](scrollview.md) — 一个可滚动的视图。
- [ScrollViewReader](scrollviewreader.md) — 一个通过与代理协同工作来滚动到已知子视图，从而提供编程式滚动的视图。
- [ScrollViewProxy](scrollviewproxy.md) — 一个代理值，用于支持对视图层级结构 (view hierarchy) 中的可滚动视图进行编程式滚动。

### 管理滚动位置

- [scrollPosition(_:anchor:)](<view/scrollposition(__anchor_).md>) — 将一个滚动位置的绑定 (binding) 与此视图内的滚动视图关联起来。
- [scrollPosition(id:anchor:)](<view/scrollposition(id_anchor_).md>) — 关联一个绑定，当此视图内的滚动视图滚动时更新该绑定。
- [defaultScrollAnchor(_:)](<view/defaultscrollanchor(__).md>) — 关联一个锚点，以控制默认情况下应渲染滚动视图内容的哪个部分。
- [defaultScrollAnchor(_:for:)](<view/defaultscrollanchor(__for_).md>) — 关联一个锚点，以控制在特定情境下滚动视图的位置。
- [ScrollAnchorRole](scrollanchorrole.md) — 定义滚动锚点角色的类型。
- [ScrollPosition](scrollposition.md) — 定义滚动视图在其内容中滚动到的语义化位置 (semantic position) 的类型。

### 定义滚动目标

- [scrollTargetBehavior(_:)](<view/scrolltargetbehavior(__).md>) — 设置在提供的轴向上可滚动视图的滚动行为。
- [scrollTargetLayout(isEnabled:)](<view/scrolltargetlayout(isenabled_).md>) — 将最外层的布局配置为滚动目标布局。
- [ScrollTarget](scrolltarget.md) — 一种类型，定义滚动视图应尝试滚动到的目标。
- [ScrollTargetBehavior](scrolltargetbehavior.md) — 一种定义可滚动视图滚动行为的类型。
- [ScrollTargetBehaviorContext](scrolltargetbehaviorcontext.md) — 滚动目标行为更新其滚动目标时的上下文。
- [PagingScrollTargetBehavior](pagingscrolltargetbehavior.md) — 将滚动目标对齐到基于容器的几何形状的滚动行为。
- [ViewAlignedScrollTargetBehavior](viewalignedscrolltargetbehavior.md) — 将滚动目标对齐到基于视图的几何形状的滚动行为。
- [AnyScrollTargetBehavior](anyscrolltargetbehavior.md) — 一个类型擦除的滚动目标行为。
- [ScrollTargetBehaviorProperties](scrolltargetbehaviorproperties.md) — 影响滚动目标行为所应用到的滚动视图的属性。
- [ScrollTargetBehaviorPropertiesContext](scrolltargetbehaviorpropertiescontext.md) — 滚动目标行为决定其属性时的上下文。

### 动画化滚动过渡

- [scrollTransition(_:axis:transition:)](<view/scrolltransition(__axis_transition_).md>) — 应用给定的过渡 (transition)，当此视图在包含它的滚动视图的可见区域内出现和消失时，在过渡的各阶段之间进行动画化。
- [scrollTransition(topLeading:bottomTrailing:axis:transition:)](<view/scrolltransition(topleading_bottomtrailing_axis_transition_).md>) — 应用给定的过渡，当此视图在包含它的滚动视图的可见区域内出现和消失时，在过渡的各阶段之间进行动画化。
- [ScrollTransitionPhase](scrolltransitionphase.md) — 视图在与其他视图一起滚动时经历的各阶段。
- [ScrollTransitionConfiguration](scrolltransitionconfiguration.md) — 滚动过渡的配置，用于控制当视图在包含它的滚动视图或其他容器的可见区域内滚动时，如何应用过渡效果。

### 响应滚动视图的变化

- [onScrollGeometryChange(for:of:action:)](<view/onscrollgeometrychange(for_of_action_).md>) — 添加一个动作，当从滚动几何 (scroll geometry) 创建的值发生变化时执行。
- [onScrollTargetVisibilityChange(idType:threshold:_:)](<view/onscrolltargetvisibilitychange(idtype_threshold___).md>) — 添加一个动作，该动作被调用时会携带关于哪些视图被视为可见的信息。
- [onScrollVisibilityChange(threshold:_:)](<view/onscrollvisibilitychange(threshold___).md>) — 添加一个动作，当视图跨越被视为屏幕上或屏幕外的阈值时被调用。
- [onScrollPhaseChange(_:)](<view/onscrollphasechange(__).md>) — 添加一个动作，当层级结构中的第一个滚动视图的滚动阶段发生变化时执行。
- [ScrollGeometry](scrollgeometry.md) — 定义滚动视图几何形状的类型。
- [ScrollPhase](scrollphase.md) — 一种类型，描述可滚动视图（如滚动视图）的滚动手势的状态。
- [ScrollPhaseChangeContext](scrollphasechangecontext.md) — 一种类型，在滚动视图的阶段发生变化时向你提供更多内容。

### 显示滚动指示器

- [scrollIndicatorsFlash(onAppear:)](<view/scrollindicatorsflash(onappear_).md>) — 在可滚动视图出现时闪烁其滚动指示器。
- [scrollIndicatorsFlash(trigger:)](<view/scrollindicatorsflash(trigger_).md>) — 当某个值发生变化时，闪烁可滚动视图的滚动指示器。
- [scrollIndicators(_:axes:)](<view/scrollindicators(__axes_).md>) — 设置此视图中滚动指示器的可见性。
- [horizontalScrollIndicatorVisibility](environmentvalues/horizontalscrollindicatorvisibility.md) — 应用于任何可水平滚动内容的滚动指示器的可见性。
- [verticalScrollIndicatorVisibility](environmentvalues/verticalscrollindicatorvisibility.md) — 应用于任何可垂直滚动内容的滚动指示器的可见性。
- [ScrollIndicatorVisibility](scrollindicatorvisibility.md) — UI 元素滚动指示器的可见性。

### 管理内容可见性

- [scrollContentBackground(_:)](<view/scrollcontentbackground(__).md>) — 指定此视图内可滚动视图的背景可见性。
- [scrollClipDisabled(_:)](<view/scrollclipdisabled(__).md>) — 设置滚动视图是否将其内容裁剪到其边界内。
- [ScrollContentOffsetAdjustmentBehavior](scrollcontentoffsetadjustmentbehavior.md) — 一种类型，定义了滚动视图可以拥有的不同内容偏移量调整行为。

### 禁用滚动

- [scrollDisabled(_:)](<view/scrolldisabled(__).md>) — 在可滚动视图中禁用或启用滚动。
- [isScrollEnabled](environmentvalues/isscrollenabled.md) — 一个布尔值，指示与此环境关联的任何滚动视图是否允许发生滚动。

### 配置滚动弹跳行为

- [scrollBounceBehavior(_:axes:)](<view/scrollbouncebehavior(__axes_).md>) — 配置可滚动视图沿指定轴向上的弹跳行为。
- [horizontalScrollBounceBehavior](environmentvalues/horizontalscrollbouncebehavior.md) — 可滚动视图水平轴向上的滚动弹跳模式。
- [verticalScrollBounceBehavior](environmentvalues/verticalscrollbouncebehavior.md) — 可滚动视图垂直轴向上的滚动弹跳模式。
- [ScrollBounceBehavior](scrollbouncebehavior.md) — 可滚动视图在到达内容末尾时可以弹跳的方式。

### 配置滚动边缘效果

- [scrollEdgeEffectStyle(_:for:)](<view/scrolledgeeffectstyle(__for_).md>) — 为此层级结构内的滚动视图配置滚动边缘效果的样式。
- [scrollEdgeEffectHidden(_:for:)](<view/scrolledgeeffecthidden(__for_).md>) — 隐藏此层级结构内滚动视图的任何滚动边缘效果。
- [ScrollEdgeEffectStyle](scrolledgeeffectstyle.md) — 一种结构，用于指定滚动内容与包含控制 (controls)（如工具栏）的区域之间的模糊 (blur) 过渡。
- [safeAreaBar(edge:alignment:spacing:content:)](<view/safeareabar(edge_alignment_spacing_content_).md>) — 在被修饰视图旁边，将指定内容显示为自定义栏。

### 与软件键盘交互

- [scrollDismissesKeyboard(_:)](<view/scrolldismisseskeyboard(__).md>) — 配置可滚动内容与软件键盘的交互行为。
- [scrollDismissesKeyboardMode](environmentvalues/scrolldismisseskeyboardmode.md) — 可滚动内容与软件键盘交互的方式。
- [ScrollDismissesKeyboardMode](scrolldismisseskeyboardmode.md) — 可滚动内容可以与软件键盘交互的各种方式。

### 管理针对不同输入的滚动

- [scrollInputBehavior(_:for:)](<view/scrollinputbehavior(__for_).md>) — 当使用特定输入时，在可滚动视图中启用或禁用滚动。
- [ScrollInputKind](scrollinputkind.md) — 用于滚动视图的输入。
- [ScrollInputBehavior](scrollinputbehavior.md) — 一种定义输入是否应滚动视图的类型。

## 另请参阅

### 视图布局

- [布局基础](layout-fundamentals.md) — 在内置布局容器（如叠放和网格）内排列视图。
- [布局调整](layout-adjustments.md) — 微调对齐、间距、内边距 (padding) 和其他布局参数。
- [自定义布局](custom-layout.md) — 将视图放置到自定义排列中，并在布局类型之间创建动画化过渡。
- [列表](lists.md) — 显示结构化的、可滚动的信息列。
- [表格](tables.md) — 显示可选中、可排序的、以行和列排列的数据。
- [视图分组](view-groupings.md) — 在不同类型的、用途驱动的容器（如表单 (forms) 或控制组）中呈现视图。
