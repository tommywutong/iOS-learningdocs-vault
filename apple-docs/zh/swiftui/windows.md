---
title: 窗口
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/windows
source_url: 'https://developer.apple.com/documentation/swiftui/windows'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windows.json'
content_hash: 'sha256:498639ff73f730f6'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md)

# 窗口

<sub>API 集合</sub>

在一个窗口或一组窗口中显示用户界面内容。

## 概述

在 App 界面中呈现视图层级结构的最常见方式是使用 [WindowGroup](windowgroup.md)，它会产生特定平台的行为和外观。

![](../../../attachments/9522b0ac981c7a46c7a0319092d0212b/windows-hero@2x.png)

在支持此功能的平台上，用户可以从该组同时打开多个窗口。每个窗口都依赖同一个根视图定义，但保留各自的视图状态。在某些平台上，你还可以使用 [Window](window.md) 场景类型，以单实例窗口来补充 App 的用户界面。

使用添加到窗口声明中的场景修饰符来配置窗口，例如 [windowStyle(_:)](<scene/windowstyle(__).md>) 或 [defaultPosition(_:)](<scene/defaultposition(__).md>)。你还可以通过在视图层级结构中的视图上添加 [presentedWindowStyle(_:)](<view/presentedwindowstyle(__).md>) 视图修饰符，来指示如何配置从视图层级结构呈现的新窗口。

有关设计指引，请参阅《人机界面指南》中的 [Windows](../design/human-interface-guidelines/windows.md)。

## 主题

### 基础

- [在 macOS 中自定窗口样式与状态恢复行为](customizing-window-styles-and-state-restoration-behavior-in-macos.md) — 配置 App 的窗口在 macOS 中的外观和功能，以提供引人入胜且更连贯的体验。
- [为 SwiftUI App 带来多窗口](bringing-multiple-windows-to-your-swiftui-app.md) — 通过响应状态变化来组合丰富的视图，并在 iPadOS 和 macOS 上自定 App 的场景呈现和行为。

### 创建窗口

- [WindowGroup](windowgroup.md) — 一种呈现一组结构完全相同的窗口的场景。
- [Window](window.md) — 一种在单一唯一窗口中呈现其内容的场景。
- [UtilityWindow](utilitywindow.md) — 一种专用的窗口场景，为应用程序主要场景的内容提供辅助功能。
- [WindowStyle](windowstyle.md) — 窗口外观和交互的一种规范。
- [windowStyle(_:)](<scene/windowstyle(__).md>) — 为此场景创建的窗口设置样式。

### 设置关联工具栏的样式

- [windowToolbarStyle(_:)](<scene/windowtoolbarstyle(__).md>) — 为此场景内定义的工具栏设置样式。
- [windowToolbarLabelStyle(_:)](<scene/windowtoolbarlabelstyle(__).md>) — 设置工具栏中项目的标签样式，并允许用户自定。
- [windowToolbarLabelStyle(fixed:)](<scene/windowtoolbarlabelstyle(fixed_).md>) — 设置工具栏中项目的标签样式。
- [WindowToolbarStyle](windowtoolbarstyle.md) — 窗口工具栏外观和行为的一种规范。

### 打开窗口

- [呈现窗口和空间](../visionos/presenting-windows-and-spaces.md) — 打开和关闭构成 App 界面的场景。
- [supportsMultipleWindows](environmentvalues/supportsmultiplewindows.md) — 一个布尔值，指示当前平台是否支持打开多个窗口。
- [openWindow](environmentvalues/openwindow.md) — 存储在视图环境中的窗口呈现操作。
- [OpenWindowAction](openwindowaction.md) — 呈现窗口的一种操作。
- [PushWindowAction](pushwindowaction.md) — 一种操作，在调用该操作所在的窗口位置打开请求的窗口。

### 关闭窗口

- [dismissWindow](environmentvalues/dismisswindow.md) — 存储在视图环境中的窗口关闭操作。
- [DismissWindowAction](dismisswindowaction.md) — 一种操作，关闭与特定场景关联的窗口。
- [dismiss](environmentvalues/dismiss.md) — 关闭当前呈现的一种操作。
- [DismissAction](dismissaction.md) — 关闭呈现的一种操作。
- [DismissBehavior](dismissbehavior.md) — 以编程方式关闭窗口的行为。

### 调整窗口大小

- [窗口的定位与调整大小](../visionos/positioning-and-sizing-windows.md) — 影响 App 呈现的窗口的初始几何形状。
- [defaultSize(_:)](<scene/defaultsize(__).md>) — 为窗口设置默认大小。
- [defaultSize(width:height:)](<scene/defaultsize(width_height_).md>) — 为窗口设置默认宽度和高度。
- [defaultSize(width:height:depth:)](<scene/defaultsize(width_height_depth_).md>) — 为 volumetric 窗口设置默认大小。
- [defaultSize(_:in:)](<scene/defaultsize(__in_).md>) — 为 volumetric 窗口设置默认大小。
- [defaultSize(width:height:depth:in:)](<scene/defaultsize(width_height_depth_in_).md>) — 为 volumetric 窗口设置默认大小。
- [windowResizability(_:)](<scene/windowresizability(__).md>) — 设置窗口使用的可调整大小类型。
- [WindowResizability](windowresizability.md) — 窗口的可调整大小性。
- [windowIdealSize(_:)](<scene/windowidealsize(__).md>) — 指定由此场景派生的窗口在缩放时应如何确定其大小。
- [WindowIdealSize](windowidealsize.md) — 一个定义窗口缩放时应使用的大小的类型。

### 定位窗口

- [defaultPosition(_:)](<scene/defaultposition(__).md>) — 为窗口设置默认位置。
- [WindowLevel](windowlevel.md) — 窗口的层级。
- [windowLevel(_:)](<scene/windowlevel(__).md>) — 设置此场景的窗口层级。
- [WindowLayoutRoot](windowlayoutroot.md) — 表示窗口根内容的一个代理。
- [WindowPlacement](windowplacement.md) — 表示窗口首选大小和位置的一个类型。
- [defaultWindowPlacement(_:)](<scene/defaultwindowplacement(__).md>) — 定义用于确定窗口默认放置位置的函数。
- [windowIdealPlacement(_:)](<scene/windowidealplacement(__).md>) — 提供一个函数，用于确定场景的窗口缩放时使用的放置位置。
- [WindowPlacementContext](windowplacementcontext.md) — 表示用于调整窗口大小和定位窗口的上下文信息的一个类型。
- [WindowProxy](windowproxy.md) — App 中已打开窗口的代理。
- [DisplayProxy](displayproxy.md) — 提供显示硬件信息的一个类型。

### 配置窗口可见性

- [WindowVisibilityToggle](windowvisibilitytoggle.md) — 用于切换窗口可见性的专用按钮。
- [defaultLaunchBehavior(_:)](<scene/defaultlaunchbehavior(__).md>) — 设置此场景的默认启动行为。
- [restorationBehavior(_:)](<scene/restorationbehavior(__).md>) — 设置此场景的恢复行为。
- [SceneLaunchBehavior](scenelaunchbehavior.md) — 场景的启动行为。
- [SceneRestorationBehavior](scenerestorationbehavior.md) — 场景的恢复行为。
- [persistentSystemOverlays(_:)](<scene/persistentsystemoverlays(__).md>) — 设置覆盖在 App 上的非临时系统视图的首选可见性。
- [windowToolbarFullScreenVisibility(_:)](<view/windowtoolbarfullscreenvisibility(__).md>) — 配置窗口进入全屏模式时窗口工具栏的可见性。
- [WindowToolbarFullScreenVisibility](windowtoolbarfullscreenvisibility.md) — 窗口工具栏相对于全屏模式的可见性。

### 管理窗口行为

- [WindowManagerRole](windowmanagerrole.md) — 定义场景的窗口在受管理窗口上下文（例如全屏模式和舞台管理器）中使用时的行为方式的选项。
- [windowManagerRole(_:)](<scene/windowmanagerrole(__).md>) — 配置由 `self` 派生的窗口在参与受管理窗口上下文（例如全屏或舞台管理器）时的角色。
- [WindowInteractionBehavior](windowinteractionbehavior.md) — 启用和禁用窗口交互行为的选项。
- [windowDismissBehavior(_:)](<view/windowdismissbehavior(__).md>) — 为包围 `self` 的窗口配置关闭功能。
- [windowFullScreenBehavior(_:)](<view/windowfullscreenbehavior(__).md>) — 为包围 `self` 的窗口配置全屏功能。
- [windowMinimizeBehavior(_:)](<view/windowminimizebehavior(__).md>) — 为包围 `self` 的窗口配置最小化功能。
- [windowResizeBehavior(_:)](<view/windowresizebehavior(__).md>) — 为包围 `self` 的窗口配置调整大小功能。
- [windowBackgroundDragBehavior(_:)](<scene/windowbackgrounddragbehavior(__).md>) — 配置通过窗口背景拖动窗口的行为。
- [allowsWindowActivationEvents()](<view/allowswindowactivationevents().md>) — 配置此视图层级结构中的手势来处理激活所属窗口的事件。
- [allowsWindowActivationEvents(_:)](<view/allowswindowactivationevents(__).md>) — 配置此视图层级结构中的手势能否处理激活所属窗口的事件。

### 与 volume 交互

- [onVolumeViewpointChange(updateStrategy:initial:_:)](<view/onvolumeviewpointchange(updatestrategy_initial___).md>) — 添加一个操作，在 volume 的视点变化时执行。
- [supportedVolumeViewpoints(_:)](<view/supportedvolumeviewpoints(__).md>) — 指定 volume 中窗口栏和挂饰支持哪些视点。
- [VolumeViewpointUpdateStrategy](volumeviewpointupdatestrategy.md) — 一个类型，描述提供给 [onVolumeViewpointChange(updateStrategy:initial:_:)](<view/onvolumeviewpointchange(updatestrategy_initial___).md>) 的操作应在何时被调用。
- [Viewpoint3D](viewpoint3d.md) — 一个类型，描述从什么方向观察某物。
- [SquareAzimuth](squareazimuth.md) — 一个类型，描述沿水平平面观察某物的方向，并吸附到 4 个方向。
- [WorldAlignmentBehavior](worldalignmentbehavior.md) — 表示场景的世界对齐行为的一个类型。
- [volumeWorldAlignment(_:)](<scene/volumeworldalignment(__).md>) — 指定 volume 在世界中移动时应如何对齐。
- [WorldScalingBehavior](worldscalingbehavior.md) — 指定窗口在世界中应具有的缩放行为。
- [defaultWorldScaling(_:)](<scene/defaultworldscaling(__).md>) — 指定窗口的世界缩放行为。
- [WorldScalingCompensation](worldscalingcompensation.md) — 指示返回的度量值是否会将动态缩放考虑在内。
- [worldTrackingLimitations](environmentvalues/worldtrackinglimitations.md) — 设备跟踪用户周围环境的当前限制。
- [WorldTrackingLimitation](worldtrackinglimitation.md) — 表示跟踪用户周围环境限制的一个结构体。
- [SurfaceSnappingInfo](surfacesnappinginfo.md) — 表示窗口场景吸附状态信息的一个类型。

### 已废弃类型

- [ControlActiveState](controlactivestate.md) — 窗口中控制预期呈现的活跃外观。_(已废弃)_

## 另请参阅

### App 结构

- [App 组织](app-organization.md) — 定义 App 的入口点和顶层结构。
- [场景](scenes.md) — 声明构成 App 各部分的用户界面分组。
- [沉浸式空间](immersive-spaces.md) — 在用户周围环境中显示无边界的内容。
- [文稿](documents.md) — 让用户能够打开和管理文稿。
- [导览](navigation.md) — 让用户能够在场景内 App 视图层级结构的不同部分之间移动。
- [模态呈现](modal-presentations.md) — 在提供专注交互的独立视图中呈现内容。
- [工具栏](toolbars.md) — 提供对常用命令和控制的即时访问。
- [搜索](search.md) — 让用户能够搜索 App 内的文本或其他内容。
- [App 扩展](app-extensions.md) — 将 App 的基本功能扩展到系统的其他部分，例如添加小组件。
