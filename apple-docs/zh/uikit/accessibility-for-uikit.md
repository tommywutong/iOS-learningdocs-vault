---
title: UIKit 的辅助功能
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/accessibility-for-uikit
source_url: 'https://developer.apple.com/documentation/uikit/accessibility-for-uikit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/accessibility-for-uikit.json'
content_hash: 'sha256:9599fcb5ed21f76c'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md)

# UIKit 的辅助功能

<sub>API 集合</sub>

让你的 UIKit App 对使用 iOS 和 tvOS 的所有人都无障碍可用。

## 概述

让你的 App 无障碍可用，意味着让所有人都能使用它。在设计 App 时顾及辅助功能，就能让所有人都能享用你的 App。更多信息，请参阅[辅助功能](../accessibility.md)。

UIKit 的控制和视图自带内置辅助功能，默认提供无障碍的用户体验。通常，你无需做额外工作即可启用这些标准辅助功能特性。

在某些情况下，你可能希望修改默认值，以便更好地呈现你的 App、提供额外的上下文，或调整用户在 App 中的流程。UIKit 让这些自定变得非常直接，只需在定义用户界面时修改几行代码或在 Interface Builder 中做些调整即可。有关为 UIKit 元素自定辅助功能的更多信息，请参阅 [UIAccessibility](uiaccessibility-protocol.md)。

如果你的 App 包含不继承自 [UIView](uiview.md) 或其他自带内置辅助功能的 UIKit 类的自定用户界面元素，请通过派生 [UIAccessibilityElement](uiaccessibilityelement.md) 的子类使这些元素可被辅助功能访问。

如果你使用 SwiftUI 构建 App，请参阅[辅助功能修饰符](../swiftui/view-accessibility.md)。

## 主题

### 基础

- [UIAccessibility](uiaccessibility-protocol.md) — 一组方法，提供关于 App 用户界面中视图和控制的辅助功能信息。
- [UIAccessibilityContainer](uiaccessibilitycontainer.md) — 提供一组方法，供视图子类用来将子组件作为独立元素开放给辅助功能。
- [在 App 中支持旁白](supporting-voiceover-in-your-app.md) — 添加旁白（VoiceOver）支持，让你的 iOS App 对盲人或低视力用户更加无障碍。

### 行为

- [UIAccessibilityFocus](../objectivec/uiaccessibilityfocus.md) — 一个非正式协议，提供一种方法来判断辅助 App（如旁白）是否将焦点置于某个辅助功能元素上。
- [UIAccessibilityIdentification](uiaccessibilityidentification.md) — 将唯一标识符与用户界面中的元素关联的方法。
- [UIAccessibilityReadingContent](uiaccessibilityreadingcontent.md) — 为表示用户阅读内容（如图书或文章）的对象而需实现的方法。
- [UIAccessibilityContentSizeCategoryImageAdjusting](uiaccessibilitycontentsizecategoryimageadjusting.md) — 用于确定何时针对不同内容尺寸类别调整图像的方法。
- [UIAccessibilityTextualContext](uiaccessibilitytextualcontext.md) — 描述命名上下文的常量，有助于识别和分类元素内文本的类型。

### 引导式访问

- [UIGuidedAccessConfigureAccessibilityFeatures](<uiaccessibility/configureforguidedaccess(features_enabled_completionhandler_).md>) — 在使用引导式访问时启用或禁用指定的辅助功能特性。
- [UIGuidedAccessAccessibilityFeature](uiguidedaccessaccessibilityfeature.md) — 描述引导式访问辅助功能特性的常量。
- [Code](uiaccessibility/guidedaccesserror/code.md) — 引导式访问的错误码。

### 操作

- [UIAccessibilityAction](../objectivec/uiaccessibilityaction.md) — 一组方法，辅助功能元素可用它来支持特定操作。
- [UIAccessibilityCustomAction](uiaccessibilitycustomaction.md) — 在可辅助访问的对象上执行的自定操作。
- [Handler](uiaccessibilitycustomaction/handler.md) — 定义为某个操作执行的处理程序的闭包类型。
- [交付卓越的辅助功能体验](../accessibility/delivering_an_exceptional_accessibility_experience.md) — 改进 App 的交互模型，以支持旁白等辅助技术。

### 元素

- [UIAccessibilityElement](uiaccessibilityelement.md) — 一个应当对残障用户无障碍可用、但默认情况下不可访问的元素。
- [UIScrollViewAccessibilityDelegate](uiscrollviewaccessibilitydelegate.md) — 一组你可实现的方法，用于为滚动视图提供辅助功能信息。
- [UIPickerViewAccessibilityDelegate](uipickerviewaccessibilitydelegate.md) — 一组你可实现的方法，用于为选择器视图的各个组件提供辅助功能信息。

### 容器

- [UIAccessibilityContainerDataTable](uiaccessibilitycontainerdatatable.md) — 传达表格内容信息的方法。
- [UIAccessibilityContainerDataTableCell](uiaccessibilitycontainerdatatablecell.md) — 提供单元格在表格中位置的方法。
- [UIAccessibilityContainerType](uiaccessibilitycontainertype.md) — 指示基于数据的容器中内容类型的常量。

### 导览

- [UIAccessibilityCustomRotor](uiaccessibilitycustomrotor.md) — 一种上下文敏感的功能，帮助旁白用户找到相关元素的下一个实例。
- [UIAccessibilityCustomRotorItemResult](uiaccessibilitycustomrotoritemresult.md) — 自定转子所引用的目标元素。
- [UIAccessibilityCustomRotorSearchPredicate](uiaccessibilitycustomrotorsearchpredicate.md) — 帮助确定下一个匹配的自定转子条目结果的搜索参数。

### 拖放支持

- [UIAccessibilityLocationDescriptor](uiaccessibilitylocationdescriptor.md) — 视图内特定几何关注点的辅助功能描述符，供辅助 App 使用。

### 通知

- [通知名称](notification-names.md) — 辅助功能系统生成的通知的名称。
- [通知字典键](notification-dictionary-keys.md) — 使用 user info 字典中的键处理通知。
- [UIAccessibilityPostNotification](<uiaccessibility/post(notification_argument_).md>) — 向辅助 App 发布通知。

### 转换

- [UIAccessibilityConvertFrameToScreenCoordinates](<uiaccessibility/converttoscreencoordinates(__in_)-9ziiu.md>) — 将指定矩形从视图坐标转换为屏幕坐标。
- [UIAccessibilityConvertPathToScreenCoordinates](<uiaccessibility/converttoscreencoordinates(__in_)-6dx4a.md>) — 将指定路径对象转换为屏幕坐标，并返回包含结果的新路径对象。

### 便捷函数

- [UIAccessibilityFocusedElement](<uiaccessibility/focusedelement(using_).md>) — 返回指定辅助 App 当前聚焦的辅助功能元素。
- [UIAccessibilityHearingDevicePairedEar](uiaccessibility/hearingdevicepairedear.md) — 「专为 iPhone 而设」助听设备的当前配对状态。
- [HearingDeviceEar](uiaccessibility/hearingdeviceear.md) — 指定人如何使用助听设备的常量。
- [UIAccessibilityRegisterGestureConflictWithZoom](<uiaccessibility/registergestureconflictwithzoom().md>) — 提醒用户：App 专属手势与系统定义的缩放辅助功能手势存在冲突。
- [UIAccessibilityRequestGuidedAccessSession](<uiaccessibility/requestguidedaccesssession(enabled_completionhandler_).md>) — 异步地将 App 进入或退出单 App 模式。
- [UIAccessibilityZoomFocusChanged](<uiaccessibility/zoomfocuschanged(zoomtype_toframe_in_).md>) — 当 App 的焦点变更到新位置时通知系统。

### 功能状态

- [UIAccessibilityIsAssistiveTouchRunning](uiaccessibility/isassistivetouchrunning.md) — 一个布尔值，指示「辅助触控」是否处于启用状态。
- [UIAccessibilityIsVoiceOverRunning](uiaccessibility/isvoiceoverrunning.md) — 一个布尔值，指示旁白是否处于启用状态。
- [UIAccessibilityIsSwitchControlRunning](uiaccessibility/isswitchcontrolrunning.md) — 一个布尔值，指示「切换控制」设置是否处于启用状态。
- [UIAccessibilityIsShakeToUndoEnabled](uiaccessibility/isshaketoundoenabled.md) — 一个布尔值，指示「摇动以撤销」设置是否处于启用状态。
- [UIAccessibilityIsClosedCaptioningEnabled](uiaccessibility/isclosedcaptioningenabled.md) — 一个布尔值，指示「隐藏式字幕与 SDH」设置是否处于启用状态。
- [UIAccessibilityIsBoldTextEnabled](uiaccessibility/isboldtextenabled.md) — 一个布尔值，指示「粗体文本」设置是否处于启用状态。
- [UIAccessibilityDarkerSystemColorsEnabled](uiaccessibility/isdarkersystemcolorsenabled.md) — 一个布尔值，指示「增强对比度」设置是否处于启用状态。
- [UIAccessibilityIsGrayscaleEnabled](uiaccessibility/isgrayscaleenabled.md) — 一个布尔值，指示「色彩滤镜」和「灰度」设置是否处于启用状态。
- [UIAccessibilityIsGuidedAccessEnabled](uiaccessibility/isguidedaccessenabled.md) — 一个布尔值，指示「引导式访问」设置是否处于启用状态。
- [UIAccessibilityIsInvertColorsEnabled](uiaccessibility/isinvertcolorsenabled.md) — 一个布尔值，指示「经典反转」设置是否处于启用状态。
- [UIAccessibilityIsMonoAudioEnabled](uiaccessibility/ismonoaudioenabled.md) — 一个布尔值，指示「单声道音频」设置是否处于启用状态。
- [UIAccessibilityIsReduceMotionEnabled](uiaccessibility/isreducemotionenabled.md) — 一个布尔值，指示「减弱动态效果」设置是否处于启用状态。
- [UIAccessibilityIsReduceTransparencyEnabled](uiaccessibility/isreducetransparencyenabled.md) — 一个布尔值，指示「降低透明度」设置是否处于启用状态。
- [UIAccessibilityIsSpeakScreenEnabled](uiaccessibility/isspeakscreenenabled.md) — 一个布尔值，指示「朗读屏幕」设置是否处于启用状态。
- [UIAccessibilityIsSpeakSelectionEnabled](uiaccessibility/isspeakselectionenabled.md) — 一个布尔值，指示「朗读所选项」设置是否处于启用状态。
- [UIAccessibilityIsOnOffSwitchLabelsEnabled](uiaccessibility/isonoffswitchlabelsenabled.md) — 一个布尔值，指示「开／关标签」设置是否处于启用状态。
- [UIAccessibilityIsVideoAutoplayEnabled](uiaccessibility/isvideoautoplayenabled.md) — 一个布尔值，指示「自动播放视频预览」设置是否处于启用状态。
- [UIAccessibilityButtonShapesEnabled](uiaccessibility/buttonshapesenabled.md) — 一个布尔值，指示「按钮形状」设置是否处于启用状态。_(已废弃)_
- [UIAccessibilityPrefersCrossFadeTransitions](uiaccessibility/preferscrossfadetransitions.md) — 一个布尔值，指示「减弱动态效果」和「偏好交叉淡入淡出过渡」设置是否处于启用状态。
- [UIAccessibilityShouldDifferentiateWithoutColor](uiaccessibility/shoulddifferentiatewithoutcolor.md) — 一个布尔值，指示「不用颜色区分」设置是否处于启用状态。

## 另请参阅

### 用户交互

- [触摸、按压与手势](touches-presses-and-gestures.md) — 将 App 的事件处理逻辑封装在手势识别器中，以便在整个 App 中重用这些代码。
- [菜单与快捷键](menus-and-shortcuts.md) — 使用菜单系统、上下文菜单、主屏幕快速操作和键盘快捷键简化与你的 App 的交互。
- [拖放](drag-and-drop.md) — 通过在视图上使用交互 API，为你的 App 带来拖放功能。
- [指针交互](pointer-interactions.md) — 在你的自定控制和视图中支持指针交互。
- [Apple Pencil 交互](apple-pencil-interactions.md) — 处理 Apple Pencil 上的双击和挤压等用户交互。
- [基于焦点的导览](focus-based-navigation.md) — 使用遥控器、游戏控制器或键盘导览你的 UIKit App 的界面。
