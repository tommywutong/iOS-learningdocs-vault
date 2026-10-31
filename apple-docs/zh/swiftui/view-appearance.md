---
title: 外观修饰符
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-appearance
source_url: 'https://developer.apple.com/documentation/swiftui/view-appearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-appearance.json'
content_hash: 'sha256:36f7ec08c414d447'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [视图基础](view-fundamentals.md) · [View](view.md)

# 外观修饰符

<sub>API 集合</sub>

配置视图的前景和背景样式、控制以及可见性。

## 概述

使用这些修饰符来配置视图的外观，包括颜色和色调的使用，以及叠加层和背景元素的应用。控制视图以及视图内特定元素的可见性。管理各种控制的形状和大小。

有关配置视图的信息，请参阅[视图配置](view-configuration.md)。

## 主题

### 颜色与图案

- [backgroundStyle(_:)](<view/backgroundstyle(__).md>) — 设置用于在此视图内渲染背景的指定样式。
- [foregroundStyle(_:)](<view/foregroundstyle(__).md>) — 设置视图的前景元素使用给定样式。
- [foregroundStyle(_:_:)](<view/foregroundstyle(____).md>) — 设置子视图中前景样式的主要和次要层级。
- [foregroundStyle(_:_:_:)](<view/foregroundstyle(______).md>) — 设置前景样式的主要、次要和第三层级。
- [allowedDynamicRange(_:)](<view/alloweddynamicrange(__).md>) — 返回一个配置了指定允许动态范围的新视图。

### 色调

- [tint(_:)](<view/tint(__).md>) — 设置此视图内的色调颜色。
- [listRowSeparatorTint(_:edges:)](<view/listrowseparatortint(__edges_).md>) — 设置与某一行关联的色调颜色。
- [listSectionSeparatorTint(_:edges:)](<view/listsectionseparatortint(__edges_).md>) — 设置与某个分区关联的色调颜色。
- [listItemTint(_:)](<view/listitemtint(__).md>) — 为列表中的内容设置固定的色调颜色。

### 浅色与深色外观

- [preferredColorScheme(_:)](<view/preferredcolorscheme(__).md>) — 设置此呈现内容的首选配色方案。
- [preferredSurroundingsEffect(_:)](<view/preferredsurroundingseffect(__).md>) — 对透视视频应用一种效果。

### 前景元素

- [border(_:width:)](<view/border(__width_).md>) — 使用指定的样式和宽度为此视图添加边框。
- [overlay(alignment:content:)](<view/overlay(alignment_content_).md>) — 将你指定的视图叠加在此视图前面。
- [overlay(_:ignoresSafeAreaEdges:)](<view/overlay(__ignoressafeareaedges_).md>) — 将指定的样式叠加在此视图前面。
- [overlay(_:in:fillStyle:)](<view/overlay(__in_fillstyle_).md>) — 将你指定的形状叠加在此视图前面。
- [spatialOverlay(alignment:content:)](<view/spatialoverlay(alignment_content_).md>) — 在此视图的 3D 边界内添加次要视图。
- [spatialOverlayPreferenceValue(_:alignment:_:)](<view/spatialoverlaypreferencevalue(__alignment___).md>) — 使用视图中指定的偏好值生成另一个视图，占用与第一个视图相同的 3D 空间。

### 背景元素

- [background(alignment:content:)](<view/background(alignment_content_).md>) — 将你指定的视图叠加在此视图后面。
- [background(_:ignoresSafeAreaEdges:)](<view/background(__ignoressafeareaedges_).md>) — 将视图的背景设置为一种样式。
- [background(ignoresSafeAreaEdges:)](<view/background(ignoressafeareaedges_).md>) — 将视图的背景设置为默认背景样式。
- [background(_:in:fillStyle:)](<view/background(__in_fillstyle_).md>) — 将视图的背景设置为填充某种样式的可内嵌形状。
- [background(in:fillStyle:)](<view/background(in_fillstyle_).md>) — 将视图的背景设置为填充默认背景样式的可内嵌形状。
- [alternatingRowBackgrounds(_:)](<view/alternatingrowbackgrounds(__).md>) — 覆盖此视图中的列表和表格是否具有交替行背景。
- [listRowBackground(_:)](<view/listrowbackground(__).md>) — 在列表行条目后面放置自定义背景视图。
- [scrollContentBackground(_:)](<view/scrollcontentbackground(__).md>) — 指定此视图内可滚动视图背景的可见性。
- [containerBackground(_:for:)](<view/containerbackground(__for_).md>) — 使用视图设置所包含容器的容器背景。
- [containerBackground(for:alignment:content:)](<view/containerbackground(for_alignment_content_).md>) — 使用视图设置所包含容器的容器背景。
- [glassBackgroundEffect(displayMode:)](<view/glassbackgroundeffect(displaymode_).md>) — 使用自动玻璃背景效果和相对容器的圆角矩形形状填充视图背景。
- [glassBackgroundEffect(_:displayMode:)](<view/glassbackgroundeffect(__displaymode_).md>) — 使用自定义玻璃背景效果和相对容器的圆角矩形形状填充视图背景。
- [glassBackgroundEffect(in:displayMode:)](<view/glassbackgroundeffect(in_displaymode_).md>) — 使用自动玻璃背景效果和你指定的形状填充视图背景。
- [glassBackgroundEffect(_:in:displayMode:)](<view/glassbackgroundeffect(__in_displaymode_).md>) — 使用自定义玻璃背景效果和你指定的形状填充视图背景。
- [backgroundExtensionEffect()](<view/backgroundextensioneffect().md>) — 为视图添加背景扩展效果。视图将被复制为镜像副本，这些副本将放置在视图周围任何具有可用安全区的边缘上。此外，还会在其上应用模糊效果以模糊化这些副本。
- [backgroundExtensionEffect(isEnabled:)](<view/backgroundextensioneffect(isenabled_).md>) — 为视图添加背景扩展效果。视图将被复制为镜像副本，这些副本将放置在视图周围任何具有可用安全区的边缘上。此外，还会在其上应用模糊效果以模糊化这些副本。

### 透视

- [breakthroughEffect(_:)](<view/breakthrougheffect(__).md>) — 确保视图始终对用户可见，即使其他内容（如 3D 模型）遮挡了它。

### 控制配置

- [defaultWheelPickerItemHeight(_:)](<view/defaultwheelpickeritemheight(__).md>) — 设置默认的滚轮式选择器条目高度。
- [horizontalRadioGroupLayout()](<view/horizontalradiogrouplayout().md>) — 将此视图内单选组样式选择器的样式设置为水平排布，单选按钮位于布局内部。
- [controlSize(_:)](<view/controlsize(__).md>) — 设置此视图内控制的尺寸。
- [buttonBorderShape(_:)](<view/buttonbordershape(__).md>) — 设置此视图内按钮的边框形状。
- [buttonRepeatBehavior(_:)](<view/buttonrepeatbehavior(__).md>) — 设置此视图内的按钮在长时间交互时是否应重复触发其操作。
- [headerProminence(_:)](<view/headerprominence(__).md>) — 设置此视图的标头突出程度。
- [scrollDisabled(_:)](<view/scrolldisabled(__).md>) — 在可滚动视图中禁用或启用滚动。
- [scrollBounceBehavior(_:axes:)](<view/scrollbouncebehavior(__axes_).md>) — 配置可滚动视图沿指定轴向上的弹跳行为。
- [scrollIndicatorsFlash(onAppear:)](<view/scrollindicatorsflash(onappear_).md>) — 在可滚动视图出现时闪烁其滚动指示器。
- [scrollIndicatorsFlash(trigger:)](<view/scrollindicatorsflash(trigger_).md>) — 当某个值发生变化时，闪烁可滚动视图的滚动指示器。
- [menuOrder(_:)](<view/menuorder(__).md>) — 设置从此视图呈现的菜单中条目的首选顺序。
- [menuActionDismissBehavior(_:)](<view/menuactiondismissbehavior(__).md>) — 告知菜单在执行操作后是否关闭。
- [paletteSelectionEffect(_:)](<view/paletteselectioneffect(__).md>) — 指定要应用于调色板条目的选择效果。
- [typeSelectEquivalent(_:)](<view/typeselectequivalent(__).md>) — 在集合（如列表或表格）中设置显式的键入选择等效文本。

### 符号效果

- [symbolEffect(_:options:isActive:)](<view/symboleffect(__options_isactive_).md>) — 返回一个添加了符号效果的新视图。
- [symbolEffect(_:options:value:)](<view/symboleffect(__options_value_).md>) — 返回一个添加了符号效果的新视图。
- [symbolEffectsRemoved(_:)](<view/symboleffectsremoved(__).md>) — 返回一个新视图，其继承的符号图像效果被移除或保持不变。

### 隐私与涂黑

- [privacySensitive(_:)](<view/privacysensitive(__).md>) — 将视图标记为包含敏感的用户隐私数据。
- [redacted(reason:)](<view/redacted(reason_).md>) — 添加一个对此视图层级结构应用涂黑处理的原因。
- [unredacted()](<view/unredacted().md>) — 移除任何对此视图层级结构应用涂黑处理的原因。
- [invalidatableContent(_:)](<view/invalidatablecontent(__).md>) — 将接收者标记为其内容可能会失效。
- [contentCaptureProtected(_:)](<view/contentcaptureprotected(__).md>)

### 可见性

- [hidden()](<view/hidden().md>) — 无条件隐藏此视图。
- [labelsHidden()](<view/labelshidden().md>) — 隐藏此视图内包含的任何控制的标签。
- [labelsVisibility(_:)](<view/labelsvisibility(__).md>) — 控制此视图内包含的任何控制的标签的可见性。
- [menuIndicator(_:)](<view/menuindicator(__).md>) — 设置此视图内控制的菜单指示器可见性。
- [listRowSeparator(_:edges:)](<view/listrowseparator(__edges_).md>) — 设置与此特定行关联的分隔线的显示模式。
- [listSectionSeparator(_:edges:)](<view/listsectionseparator(__edges_).md>) — 设置是否隐藏与列表分区关联的分隔线。
- [listSectionIndexVisibility(_:)](<view/listsectionindexvisibility(__).md>) — 更改列表分区索引的可见性。
- [persistentSystemOverlays(_:)](<view/persistentsystemoverlays(__).md>) — 设置叠加在 App 上的非临时系统视图的首选可见性。
- [scrollIndicators(_:axes:)](<view/scrollindicators(__axes_).md>) — 设置此视图内滚动指示器的可见性。
- [scrollClipDisabled(_:)](<view/scrollclipdisabled(__).md>) — 设置滚动视图是否将其内容裁剪到其边界内。
- [sliderThumbVisibility(_:)](<view/sliderthumbvisibility(__).md>) — 设置此视图内 `Slider` 的滑块可见性。
- [tableColumnHeaders(_:)](<view/tablecolumnheaders(__).md>) — 控制 `Table` 的列标头视图的可见性。
- [upperLimbVisibility(_:)](<view/upperlimbvisibility(__).md>) — 在呈现 [ImmersiveSpace](immersivespace.md) 场景时，设置用户上肢的首选可见性。
- [volumeBaseplateVisibility(_:)](<view/volumebaseplatevisibility(__).md>) — 设置 volume 基座的可见性，当用户看向 volume 的「地面」时以及在调整大小时会显示该基座。`automatic` 和 `visible` 都会显示基座，`hidden` 则永远不会显示。

### 触感反馈

- [sensoryFeedback(_:trigger:)](<view/sensoryfeedback(__trigger_).md>) — 在提供的 `trigger` 值发生变化时播放指定的 `feedback`。
- [sensoryFeedback(trigger:_:)](<view/sensoryfeedback(trigger___).md>) — 在提供的 `trigger` 值发生变化后，播放 `feedback` 闭包返回的反馈。
- [sensoryFeedback(_:trigger:condition:)](<view/sensoryfeedback(__trigger_condition_).md>) — 在提供的 `trigger` 值发生变化且 `condition` 闭包返回 `true` 时播放指定的 `feedback`。

### 小组件配置

- [widgetAccentable(_:)](<view/widgetaccentable(__).md>) — 将视图及其所有子视图添加到强调组。
- [widgetCurvesContent(_:)](<view/widgetcurvescontent(__).md>) — 在上下文允许的情况下沿曲线显示小组件的内容。
- [widgetLabel(_:)](<view/widgetlabel(__).md>) — 返回一个本地化文本标签，在附件系列小组件的主 SwiftUI 视图之外显示额外内容。
- [widgetLabel(label:)](<view/widgetlabel(label_).md>) — 创建一个标签，用于在附件系列小组件的主 SwiftUI 视图之外显示额外内容。
- [dynamicIsland(verticalPlacement:)](<view/dynamicisland(verticalplacement_).md>) — 指定出现在灵动岛中的展开实时活动视图的垂直放置位置。
- [accessoryWidgetGroupStyle(_:)](<view/accessorywidgetgroupstyle(__).md>) — 可应用于 `AccessoryWidgetGroup` 的视图修饰符，用于指定三个内容视图将被遮罩成的形状。`style` 的值被设置为 `.automatic`，默认为 `.circular`。
- [controlWidgetActionHint(_:)](<view/controlwidgetactionhint(__).md>) — 被修饰的标签所描述的控制的操作提示。
- [controlWidgetStatus(_:)](<view/controlwidgetstatus(__).md>) — 被修饰的标签所描述的控制的状态。

### 窗口行为

- [windowDismissBehavior(_:)](<view/windowdismissbehavior(__).md>) — 为包含 `self` 的窗口配置关闭功能。
- [windowFullScreenBehavior(_:)](<view/windowfullscreenbehavior(__).md>) — 为包含 `self` 的窗口配置全屏功能。
- [windowToolbarFullScreenVisibility(_:)](<view/windowtoolbarfullscreenvisibility(__).md>) — 配置窗口进入全屏模式时窗口工具栏的可见性。
- [windowMinimizeBehavior(_:)](<view/windowminimizebehavior(__).md>) — 为包含 `self` 的窗口配置最小化功能。
- [windowResizeAnchor(_:)](<view/windowresizeanchor(__).md>) — 设置当视图大小发生变化导致窗口必须调整大小时所使用的窗口锚点。
- [windowResizeBehavior(_:)](<view/windowresizebehavior(__).md>) — 为包含 `self` 的窗口配置调整大小功能。
- [preferredWindowClippingMargins(_:_:)](<view/preferredwindowclippingmargins(____).md>) — 请求在窗口边界之外绘制的额外外边距。

## 另请参阅

### 配置视图元素

- [辅助功能修饰符](view-accessibility.md) — 让你的 SwiftUI App 对每个人都易于访问，包括残障人士。
- [文本和符号修饰符](view-text-and-symbols.md) — 管理视图中文本的渲染、选择和输入。
- [辅助视图修饰符](view-auxiliary-views.md) — 添加并配置支持视图，例如工具栏和上下文菜单。
- [图表视图修饰符](view-chart-view.md) — 配置你用 Swift Charts 声明的图表。
