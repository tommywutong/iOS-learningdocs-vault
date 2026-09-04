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

让你的 UIKit App 对使用 iOS 和 tvOS 的每一个人都可用。

## 概述

让你的 App 可访问，就是让每个人都能使用它。在设计 App 时把辅助功能（accessibility）放在心上，就能让所有人享用你的 App。更多信息参见[辅助功能](../accessibility.md)。

UIKit 的控制和视图自带内建辅助功能，默认即提供可访问的用户体验。通常你无需额外工作就能启用标准辅助功能特性。

某些情况下，你可能想修改默认值，以便更好地呈现你的 App、提供额外上下文，或调整用户在 App 中的流程。UIKit 让这些自定义变得非常直接，只需在定义用户界面时写几行代码或调整 Interface Builder。关于为 UIKit 元素自定义辅助功能的更多信息，参见 [UIAccessibility](uiaccessibility-protocol.md)。

如果你的 App 包含不继承自 [UIView](uiview.md) 或其他自带辅助功能的 UIKit 类的自定义用户界面元素，可以通过子类化 [UIAccessibilityElement](uiaccessibilityelement.md) 让这些元素可访问。

如果你用 SwiftUI 构建 App，参见[辅助功能修饰符](../swiftui/view-accessibility.md)。

## 主题

### 基础

- [UIAccessibility](uiaccessibility-protocol.md) — 一组方法，为 App 用户界面中的视图和控件提供辅助功能信息。
- [UIAccessibilityContainer](uiaccessibilitycontainer.md) — 提供一组方法，供视图子类用来把子组件作为独立元素变得可访问。
- [在你的 App 中支持「旁白」](supporting-voiceover-in-your-app.md) — 添加「旁白」（VoiceOver）支持，让你的 iOS App 对失明或低视力用户更加可用。

### 行为

- [UIAccessibilityFocus](../objectivec/uiaccessibilityfocus.md) — 一个非正式协议，提供判断辅助 App（如「旁白」）是否聚焦于某个可访问元素的方法。
- [UIAccessibilityIdentification](uiaccessibilityidentification.md) — 把唯一标识符与用户界面中的元素关联起来的方法。
- [UIAccessibilityReadingContent](uiaccessibilityreadingcontent.md) — 表示用户阅读的内容（如图书或文章）的对象要实现的方法。
- [UIAccessibilityContentSizeCategoryImageAdjusting](uiaccessibilitycontentsizecategoryimageadjusting.md) — 决定何时为不同内容尺寸类别调整图片的方法。
- [UIAccessibilityTextualContext](uiaccessibilitytextualcontext.md) — 描述具名上下文的常量，帮助识别和分类元素内文本的类型。

### 引导式访问（Guided Access）

- [UIGuidedAccessConfigureAccessibilityFeatures](<uiaccessibility/configureforguidedaccess(features_enabled_completionhandler_).md>) — 在使用引导式访问时启用或禁用指定的辅助功能特性。
- [UIGuidedAccessAccessibilityFeature](uiguidedaccessaccessibilityfeature.md) — 描述引导式访问的辅助功能特性的常量。
- [Code](uiaccessibility/guidedaccesserror/code.md) — 引导式访问的错误码。

### 操作

- [UIAccessibilityAction](../objectivec/uiaccessibilityaction.md) — 辅助功能元素用来支持特定操作的一组方法。
- [UIAccessibilityCustomAction](uiaccessibilitycustomaction.md) — 在可访问对象上执行的自定义操作。
- [Handler](uiaccessibilitycustomaction/handler.md) — 定义要为某个操作执行的处理器（handler）的闭包类型。
- [交付卓越的辅助功能体验](../accessibility/delivering_an_exceptional_accessibility_experience.md) — 改进你的 App 的交互模型，以支持「旁白」等辅助技术。

### 元素

- [UIAccessibilityElement](uiaccessibilityelement.md) — 应当对残障用户可访问、但默认不可访问的元素。
- [UIScrollViewAccessibilityDelegate](uiscrollviewaccessibilitydelegate.md) — 你可以实现的一组方法，为滚动视图提供辅助功能信息。
- [UIPickerViewAccessibilityDelegate](uipickerviewaccessibilitydelegate.md) — 你可以实现的一组方法，为选择器视图（picker view）的各个组件提供辅助功能信息。

### 容器

- [UIAccessibilityContainerDataTable](uiaccessibilitycontainerdatatable.md) — 传达表格内容信息的方法。
- [UIAccessibilityContainerDataTableCell](uiaccessibilitycontainerdatatablecell.md) — 提供单元格在表格中位置的方法。
- [UIAccessibilityContainerType](uiaccessibilitycontainertype.md) — 指示基于数据的容器中内容类型的常量。

### 导览

- [UIAccessibilityCustomRotor](uiaccessibilitycustomrotor.md) — 帮助「旁白」用户找到相关元素的下一个实例的上下文相关功能。
- [UIAccessibilityCustomRotorItemResult](uiaccessibilitycustomrotoritemresult.md) — 自定义转子（rotor）所引用的目标元素。
- [UIAccessibilityCustomRotorSearchPredicate](uiaccessibilitycustomrotorsearchpredicate.md) — 帮助确定下一个匹配的自定义转子条目结果的搜索参数。

### 拖放支持

- [UIAccessibilityLocationDescriptor](uiaccessibilitylocationdescriptor.md) — 视图内特定几何关注点的辅助功能描述符，供辅助 App 使用。

### 通知

- [通知名称](notification-names.md) — 辅助功能系统生成的通知的名称。
- [通知字典键](notification-dictionary-keys.md) — 用 user info 字典中的键处理通知。
- [UIAccessibilityPostNotification](<uiaccessibility/post(notification_argument_).md>) — 向辅助 App 发布通知。

### 转换

- [UIAccessibilityConvertFrameToScreenCoordinates](<uiaccessibility/converttoscreencoordinates(__in_)-9ziiu.md>) — 把指定矩形从视图坐标转换为屏幕坐标。
- [UIAccessibilityConvertPathToScreenCoordinates](<uiaccessibility/converttoscreencoordinates(__in_)-6dx4a.md>) — 把指定路径对象转换为屏幕坐标，并返回包含结果的新路径对象。

### 便利函数

- [UIAccessibilityFocusedElement](<uiaccessibility/focusedelement(using_).md>) — 返回指定辅助 App 当前聚焦的辅助功能元素。
- [UIAccessibilityHearingDevicePairedEar](uiaccessibility/hearingdevicepairedear.md) — MFi（Made for iPhone）助听设备的当前配对状态。
- [HearingDeviceEar](uiaccessibility/hearingdeviceear.md) — 指定用户如何使用助听设备的常量。
- [UIAccessibilityRegisterGestureConflictWithZoom](<uiaccessibility/registergestureconflictwithzoom().md>) — 就 App 专属手势与系统定义的缩放辅助手势存在冲突向用户发出警告。
- [UIAccessibilityRequestGuidedAccessSession](<uiaccessibility/requestguidedaccesssession(enabled_completionhandler_).md>) — 异步地把 App 切入或切出单 App 模式（Single App Mode）。
- [UIAccessibilityZoomFocusChanged](<uiaccessibility/zoomfocuschanged(zoomtype_toframe_in_).md>) — 当 App 的焦点变更到新位置时通知系统。

### 能力

- [UIAccessibilityIsAssistiveTouchRunning](uiaccessibility/isassistivetouchrunning.md) — 表示 AssistiveTouch 是否处于启用状态的布尔值。
- [UIAccessibilityIsVoiceOverRunning](uiaccessibility/isvoiceoverrunning.md) — 表示「旁白」是否处于启用状态的布尔值。
- [UIAccessibilityIsSwitchControlRunning](uiaccessibility/isswitchcontrolrunning.md) — 表示切换控制（Switch Control）设置是否处于启用状态的布尔值。
- [UIAccessibilityIsShakeToUndoEnabled](uiaccessibility/isshaketoundoenabled.md) — 表示摇动以撤销（Shake to Undo）设置是否处于启用状态的布尔值。
- [UIAccessibilityIsClosedCaptioningEnabled](uiaccessibility/isclosedcaptioningenabled.md) — 表示隐藏式字幕 + SDH（Closed Captions + SDH）设置是否处于启用状态的布尔值。
- [UIAccessibilityIsBoldTextEnabled](uiaccessibility/isboldtextenabled.md) — 表示粗体文本（Bold Text）设置是否处于启用状态的布尔值。
- [UIAccessibilityDarkerSystemColorsEnabled](uiaccessibility/isdarkersystemcolorsenabled.md) — 表示增强对比度（Increase Contrast）设置是否处于启用状态的布尔值。
- [UIAccessibilityIsGrayscaleEnabled](uiaccessibility/isgrayscaleenabled.md) — 表示色彩滤镜（Color Filters）与灰度（Grayscale）设置是否处于启用状态的布尔值。
- [UIAccessibilityIsGuidedAccessEnabled](uiaccessibility/isguidedaccessenabled.md) — 表示引导式访问设置是否处于启用状态的布尔值。
- [UIAccessibilityIsInvertColorsEnabled](uiaccessibility/isinvertcolorsenabled.md) — 表示经典反色（Classic Invert）设置是否处于启用状态的布尔值。
- [UIAccessibilityIsMonoAudioEnabled](uiaccessibility/ismonoaudioenabled.md) — 表示单声道音频（Mono Audio）设置是否处于启用状态的布尔值。
- [UIAccessibilityIsReduceMotionEnabled](uiaccessibility/isreducemotionenabled.md) — 表示减弱动态效果（Reduce Motion）设置是否处于启用状态的布尔值。
- [UIAccessibilityIsReduceTransparencyEnabled](uiaccessibility/isreducetransparencyenabled.md) — 表示降低透明度（Reduce Transparency）设置是否处于启用状态的布尔值。
- [UIAccessibilityIsSpeakScreenEnabled](uiaccessibility/isspeakscreenenabled.md) — 表示朗读屏幕（Speak Screen）设置是否处于启用状态的布尔值。
- [UIAccessibilityIsSpeakSelectionEnabled](uiaccessibility/isspeakselectionenabled.md) — 表示朗读所选项（Speak Selection）设置是否处于启用状态的布尔值。
- [UIAccessibilityIsOnOffSwitchLabelsEnabled](uiaccessibility/isonoffswitchlabelsenabled.md) — 表示开/关标签（On/Off Labels）设置是否处于启用状态的布尔值。
- [UIAccessibilityIsVideoAutoplayEnabled](uiaccessibility/isvideoautoplayenabled.md) — 表示自动播放视频预览（Auto-Play Video Previews）设置是否处于启用状态的布尔值。
- [UIAccessibilityButtonShapesEnabled](uiaccessibility/buttonshapesenabled.md) — 表示按钮形状（Button Shapes）设置是否处于启用状态的布尔值。_(已废弃)_
- [UIAccessibilityPrefersCrossFadeTransitions](uiaccessibility/preferscrossfadetransitions.md) — 表示减弱动态效果与首选交叉淡入淡出过渡（Prefer Cross-Fade Transitions）设置是否处于启用状态的布尔值。
- [UIAccessibilityShouldDifferentiateWithoutColor](uiaccessibility/shoulddifferentiatewithoutcolor.md) — 表示不依赖颜色区分（Differentiate Without Color）设置是否处于启用状态的布尔值。

## 另请参阅

### 用户交互

- [触摸、按压和手势](touches-presses-and-gestures.md) — 把你的 App 的事件处理逻辑封装在手势识别器中，让这些代码在整个 App 里可以复用。
- [菜单与快捷键](menus-and-shortcuts.md) — 使用菜单系统、上下文菜单、主屏幕快速操作和键盘快捷键，简化与你 App 的交互。
- [拖放](drag-and-drop.md) — 通过在视图中使用交互 API，为你的 App 带来拖放功能。
- [指针交互](pointer-interactions.md) — 在你的自定义控制和视图中支持指针交互。
- [Apple Pencil 交互](apple-pencil-interactions.md) — 处理 Apple Pencil 上的双击、挤压等用户交互。
- [基于焦点的导览](focus-based-navigation.md) — 使用遥控器、游戏控制器或键盘导览你的 UIKit App 的界面。
