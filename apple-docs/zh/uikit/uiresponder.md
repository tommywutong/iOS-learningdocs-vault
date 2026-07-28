---
title: UIResponder
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresponder
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder.json'
content_hash: 'sha256:e0669f851fb6a3ba'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md)

# UIResponder

<sub>类</sub>

一个用于响应和处理事件的抽象接口。

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIResponder
```

## 概述

响应者对象——即 [UIResponder](uiresponder.md) 的实例——构成了 UIKit App 的事件处理骨干。许多关键对象也是响应者，包括 [UIApplication](uiapplication.md) 对象、[UIViewController](uiviewcontroller.md) 对象以及所有 [UIView](uiview.md) 对象（其中包含 [UIWindow](uiwindow.md)）。当事件发生时，UIKit 将它们分发到你的 App 的响应者对象进行处理。

事件有几种类型，包括触摸事件、运动事件、远程控制事件和按压事件。要处理特定类型的事件，响应者必须重写相应的方法。例如，要处理触摸事件，响应者需要实现 [- touchesBegan:withEvent:](<uiresponder/touchesbegan(__with_).md>)、[- touchesMoved:withEvent:](<uiresponder/touchesmoved(__with_).md>)、[- touchesEnded:withEvent:](<uiresponder/touchesended(__with_).md>) 和 [- touchesCancelled:withEvent:](<uiresponder/touchescancelled(__with_).md>) 方法。在处理触摸时，响应者使用 UIKit 提供的事件信息来跟踪这些触摸的变化并相应地更新 App 的界面。

除了处理事件，UIKit 响应者还负责将未处理的事件转发到 App 的其他部分。如果某个响应者不处理一个事件，它会将该事件转发给响应者链（responder chain）中的下一个事件处理者。UIKit 使用预定义的规则动态管理响应者链，以确定哪个对象应该接收下一个事件。例如，一个视图将事件转发给它的父视图，而层级结构中的根视图将事件转发给它的视图控制器。

响应者处理 [UIEvent](uievent.md) 对象，但也可以通过输入视图接受自定义输入。系统键盘是输入视图最明显的例子。当用户在屏幕上点击 [UITextField](uitextfield.md) 或 [UITextView](uitextview.md) 对象时，该视图成为第一响应者并显示其输入视图，也就是系统键盘。类似地，你可以创建自定义输入视图并在其他响应者变为活跃时显示它们。要将自定义输入视图与响应者关联，请将该视图分配给响应者的 [inputView](uiresponder/inputview.md) 属性。

有关响应者和响应者链的更多信息，请参阅[使用响应者和响应者链处理事件](using-responders-and-the-responder-chain-to-handle-events.md)。

## 关系

- **继承自**：[NSObject](../objectivec/nsobject-swift.class.md)

- **被继承于**：[UIAccessibilityElement](uiaccessibilityelement.md)、[UIApplication](uiapplication.md)、[UIScene](uiscene.md)、[UIView](uiview.md)、[UIViewController](uiviewcontroller.md)

- **遵循**：[CVarArg](../swift/cvararg.md)、[Copyable](../swift/copyable.md)、[CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)、[CustomStringConvertible](../swift/customstringconvertible.md)、[Equatable](../swift/equatable.md)、[Escapable](../swift/escapable.md)、[Hashable](../swift/hashable.md)、[NSObjectProtocol](../objectivec/nsobjectprotocol.md)、[NSTouchBarProvider](../appkit/nstouchbarprovider.md)、[Sendable](../swift/sendable.md)、[UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)、[UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)、[UIResponderStandardEditActions](uiresponderstandardeditactions.md)、[UIUserActivityRestoring](uiuseractivityrestoring.md)

## 主题

### 管理响应者链

- [nextResponder](uiresponder/next.md) — 返回响应者链中的下一个响应者，如果没有下一个响应者则返回 `nil`。
- [isFirstResponder](uiresponder/isfirstresponder.md) — 返回一个布尔值，指示此对象是否为第一响应者。
- [canBecomeFirstResponder](uiresponder/canbecomefirstresponder.md) — 返回一个布尔值，指示此对象是否可以成为第一响应者。
- [- becomeFirstResponder](<uiresponder/becomefirstresponder().md>) — 请求 UIKit 将此对象设为其窗口中的第一响应者。
- [canResignFirstResponder](uiresponder/canresignfirstresponder.md) — 返回一个布尔值，指示响应者是否愿意放弃第一响应者状态。
- [- resignFirstResponder](<uiresponder/resignfirstresponder().md>) — 通知此对象它已被要求放弃其窗口中的第一响应者状态。

### 响应触摸事件

- [- touchesBegan:withEvent:](<uiresponder/touchesbegan(__with_).md>) — 告知此对象在视图或窗口中发生了一个或多个新触摸。
- [- touchesMoved:withEvent:](<uiresponder/touchesmoved(__with_).md>) — 当与事件关联的一个或多个触摸发生变化时，通知响应者。
- [- touchesEnded:withEvent:](<uiresponder/touchesended(__with_).md>) — 当一个或多个手指从视图或窗口抬起时，通知响应者。
- [- touchesCancelled:withEvent:](<uiresponder/touchescancelled(__with_).md>) — 当系统事件（例如系统警报）取消触摸序列时，通知响应者。
- [- touchesEstimatedPropertiesUpdated:](<uiresponder/touchesestimatedpropertiesupdated(__).md>) — 告知响应者收到了之前估计属性的更新值，或不再期望进行更新。

### 响应运动事件

- [- motionBegan:withEvent:](<uiresponder/motionbegan(__with_).md>) — 告知响应者运动事件已开始。
- [- motionEnded:withEvent:](<uiresponder/motionended(__with_).md>) — 告知响应者运动事件已结束。
- [- motionCancelled:withEvent:](<uiresponder/motioncancelled(__with_).md>) — 告知响应者运动事件已被取消。

### 响应按压事件

- [- pressesBegan:withEvent:](<uiresponder/pressesbegan(__with_).md>) — 当物理按钮首次被按下时，告知此对象。
- [- pressesChanged:withEvent:](<uiresponder/presseschanged(__with_).md>) — 当与按压关联的值发生变化时，告知此对象。
- [- pressesEnded:withEvent:](<uiresponder/pressesended(__with_).md>) — 当按钮被释放时，告知此对象。
- [- pressesCancelled:withEvent:](<uiresponder/pressescancelled(__with_).md>) — 当系统事件（例如内存不足警告）取消按压事件时，告知此对象。

### 响应远程控制事件

- [- remoteControlReceivedWithEvent:](<uiresponder/remotecontrolreceived(with_).md>) — 当接收到远程控制事件时，告知此对象。

### 管理输入视图

- [inputView](uiresponder/inputview.md) — 当响应者成为第一响应者时要显示的自定义输入视图。
- [inputViewController](uiresponder/inputviewcontroller.md) — 当响应者成为第一响应者时要使用的自定义输入视图控制器。
- [inputAccessoryView](uiresponder/inputaccessoryview.md) — 当响应者成为第一响应者时要显示的自定义输入辅助视图。
- [inputAccessoryViewController](uiresponder/inputaccessoryviewcontroller.md) — 当响应者成为第一响应者时要显示的自定义输入辅助视图控制器。
- [- reloadInputViews](<uiresponder/reloadinputviews().md>) — 当对象是第一响应者时，更新自定义输入和辅助视图。

### 获取撤销管理器

- [undoManager](uiresponder/undomanager.md) — 返回响应者链中最近的共享撤销管理器。

### 构建和验证命令

- [- buildMenuWithBuilder:](<uiresponder/buildmenu(with_).md>) — 要求接收响应者向菜单系统添加和移除项目。
- [- validateCommand:](<uiresponder/validate(__).md>) — 要求接收响应者验证命令。
- [- canPerformAction:withSender:](<uiresponder/canperformaction(__withsender_).md>) — 请求接收响应者在用户界面中启用或禁用指定的命令。
- [- targetForAction:withSender:](<uiresponder/target(foraction_withsender_).md>) — 返回响应操作的目标对象。

### 访问可用的按键命令

- [keyCommands](uiresponder/keycommands.md) — 在此响应者上触发操作的按键命令。

### 管理文本输入模式

- [textInputMode](uiresponder/textinputmode.md) — 此响应者对象的文本输入模式。
- [textInputContextIdentifier](uiresponder/textinputcontextidentifier.md) — 指示响应者应保留其文本输入模式信息的标识符。
- [+ clearTextInputContextIdentifier:](<uiresponder/cleartextinputcontextidentifier(__).md>) — 从 App 的用户默认设置中清除文本输入模式信息。
- [inputAssistantItem](uiresponder/inputassistantitem.md) — 配置键盘快捷键栏时使用的输入辅助项。

### 支持用户活动

- [userActivity](uiresponder/useractivity.md) — 封装此响应者支持的用户活动的对象。
- [- restoreUserActivityState:](<uiresponder/restoreuseractivitystate(__).md>) — 恢复继续给定用户活动所需的状态。
- [- updateUserActivityState:](<uiresponder/updateuseractivitystate(__).md>) — 更新给定用户活动的状态。

### 管理活动项目

- [activityItemsConfiguration](uiresponder/activityitemsconfiguration.md)

### 访问编辑交互

- [editingInteractionConfiguration](uiresponder/editinginteractionconfiguration.md)
- [UIEditingInteractionConfiguration](uieditinginteractionconfiguration.md)

### 从相机捕获文本

- [- captureTextFromCamera:](<uiresponder/capturetextfromcamera(__).md>) — 使用设备相机开始扫描文本。

### 管理触控栏

- [- makeTouchBar](<uiresponder/maketouchbar().md>) — 要求接收响应者创建并配置一个触控栏对象。
- [touchBar](uiresponder/touchbar.md) — 响应者的触控栏对象。

### 常量

- [UIKeyboardAnimationCurveUserInfoKey](uiresponder/keyboardanimationcurveuserinfokey.md) — 一个用户信息键，用于获取系统用来将键盘动画移入或移出屏幕的动画曲线。
- [UIKeyboardAnimationDurationUserInfoKey](uiresponder/keyboardanimationdurationuserinfokey.md) — 一个用户信息键，用于获取键盘动画的持续时间（以秒为单位）。
- [UIKeyboardDidChangeFrameNotification](uiresponder/keyboarddidchangeframenotification.md) — 在键盘 frame 发生变化后立即发布的通知。
- [UIKeyboardDidHideNotification](uiresponder/keyboarddidhidenotification.md) — 在关闭键盘后立即发布的通知。
- [UIKeyboardDidShowNotification](uiresponder/keyboarddidshownotification.md) — 在显示键盘后立即发布的通知。
- [UIKeyboardFrameBeginUserInfoKey](uiresponder/keyboardframebeginuserinfokey.md) — 一个用户信息键，用于获取键盘在其动画开始时的 frame。
- [UIKeyboardFrameEndUserInfoKey](uiresponder/keyboardframeenduserinfokey.md) — 一个用户信息键，用于获取键盘在其动画结束时的 frame。
- [UIKeyboardIsLocalUserInfoKey](uiresponder/keyboardislocaluserinfokey.md) — 一个用户信息键，用于获取一个布尔值，指示键盘是否属于当前 App。
- [UIKeyboardWillChangeFrameNotification](uiresponder/keyboardwillchangeframenotification.md) — 在键盘 frame 将要改变之前立即发布的通知。
- [UIKeyboardWillHideNotification](uiresponder/keyboardwillhidenotification.md) — 在即将关闭键盘之前立即发布的通知。
- [UIKeyboardWillShowNotification](uiresponder/keyboardwillshownotification.md) — 在即将显示键盘之前立即发布的通知。

### 结构体

- [KeyboardDidChangeFrameMessage](uiresponder/keyboarddidchangeframemessage.md)
- [KeyboardDidHideMessage](uiresponder/keyboarddidhidemessage.md)
- [KeyboardDidShowMessage](uiresponder/keyboarddidshowmessage.md)
- [KeyboardWillChangeFrameMessage](uiresponder/keyboardwillchangeframemessage.md)
- [KeyboardWillHideMessage](uiresponder/keyboardwillhidemessage.md)
- [KeyboardWillShowMessage](uiresponder/keyboardwillshowmessage.md)

### 实例属性

- [pencilKitResponderState](uiresponder/pencilkitresponderstate.md) — 与响应者对象关联的 PencilKit 状态。

### 实例方法

- [- providerForDeferredMenuElement:](<uiresponder/provider(for_).md>) — 要求响应者为给定的基于焦点的延迟元素提供一个元素提供者。检查延迟元素的 `identifier` 以识别这是哪个延迟元素。默认情况下，此方法返回 nil。返回一个非 nil 的 `provider` 以使此响应者负责为此次延迟元素提供元素。

## 另请参阅

### 基础

- [使用响应者和响应者链处理事件](using-responders-and-the-responder-chain-to-handle-events.md) — 了解如何处理在你的 App 中传播的事件。
- [UIEvent](uievent.md) — 描述与你的 App 的单个用户交互的对象。
