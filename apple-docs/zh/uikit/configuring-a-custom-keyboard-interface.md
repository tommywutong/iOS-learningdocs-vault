---
title: 配置自定键盘界面
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/configuring-a-custom-keyboard-interface
source_url: 'https://developer.apple.com/documentation/uikit/configuring-a-custom-keyboard-interface'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/configuring-a-custom-keyboard-interface.json'
content_hash: 'sha256:f94b02dc8d40075b'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [键盘与输入](keyboards-and-input.md) · [创建自定键盘](creating-a-custom-keyboard.md)

# 配置自定键盘界面

<sub>文章</sub>

为文本编辑设计灵活、实用且响应迅速的界面。

## 概述

你可以创建自定键盘，为操控文本输入提供系统级界面。由于你需要将键盘与系统提供的服务集成，因此必须满足特定要求，并符合用户的常见预期。

除其他事项外，你的键盘必须：

- 处理电子邮件地址、电话号码和 URL 等不同类型的输入。
- 适应可用空间。例如，iPadOS 可以显示停靠在屏幕底部的键盘，也可以显示宽度紧凑的浮动键盘。
- 允许用户切换到其他键盘。

### 支持不同的输入类型

使用 [textDocumentProxy](uiinputviewcontroller/textdocumentproxy.md) 确定当前文本输入视图的键盘输入类型。针对你的 App 支持的每一种键盘类型，相应地配置界面。一种做法是在视图控制器中实现 [- textWillChange:](<uitextinputdelegate/textwillchange(__).md>)，然后将 [textDocumentProxy](uiinputviewcontroller/textdocumentproxy.md) 的 [keyboardType](uitextinputtraits/keyboardtype.md) 与键盘当前显示进行比较。如果两者不同，请相应地更新界面。

```swift
let keyboardType = textDocumentProxy.keyboardType

switch(keyboardType) {
case .asciiCapable: …
case .emailAddress: …
case .numberPad: …
…
}
```

某些文本输入视图不允许使用自定键盘：

- 当用户开始在安全文本字段中输入文本时，安全文本字段条目始终显示系统键盘，并暂时移除当前有效的自定键盘。当用户开始在非安全文本字段中输入文本时，系统会再次显示你的键盘。
- 键盘类型配置为 [UIKeyboardTypePhonePad](uikeyboardtype/phonepad.md) 或 [UIKeyboardTypeNamePhonePad](uikeyboardtype/namephonepad.md) 的文本输入字段会显示系统键盘。

App 可以通过实现 [- application:shouldAllowExtensionPointIdentifier:](<uiapplicationdelegate/application(__shouldallowextensionpointidentifier_).md>)，并在收到 `com.apple.keyboard-service` 标识符时返回 [false](../swift/false.md)，来完全禁止使用第三方键盘。如果某个 App 禁止使用第三方键盘，你的键盘就不会在该 App 中显示。

### 适应不同布局

默认情况下，iOS 会根据屏幕大小和设备方向调整自定键盘的大小，使其与系统键盘匹配。自定键盘的宽度始终由系统设置，通常与屏幕宽度一致。你可以使用 Auto Layout 调整自定键盘主视图的高度。要更改键盘高度，请调整 UIInputViewController 视图的高度约束，使界面达到所需高度。

有关排布视图的更多信息，请参阅[视图布局](view-layout.md)。

### 处理常见键盘行为

用户期望键盘具备各种行为。自动大写就是一个例子：在标准文本字段中，区分大小写的语言会自动将句子的首字母大写。

用户通常期望任何键盘都具备以下功能：

- 根据键盘类型特性（trait）提供适当的布局和功能，例如编辑电子邮件地址或电话号码时自动显示相关按键
- 自动更正和建议
- 自动大写
- 连按两次空格时自动输入句点
- 智能引号
- 大写锁定支持
- 为使用表意字符和符号的语言提供多阶段输入，例如日文汉字和中文汉字

UIInputViewController 遵循 [UITextInputTraits](uitextinputtraits.md) 协议，以提供与这些常见行为相关的多种属性。这些属性指示当前有效的设置，例如自动补全类型、自动大写类型、启用 Return 键、智能引号和破折号等。完整列表请参阅 [UITextInputTraits](uitextinputtraits.md)。

另一种常见行为是能够收起键盘。用户可以通过收起键盘结束在当前文本输入视图中的编辑。你可以实现一个收起键盘的按钮，并调用 [- dismissKeyboard](<uiinputviewcontroller/dismisskeyboard().md>)：

```swift
@IBAction func dismissButtonTapped(_ sender: Any) {
    dismissKeyboard()
}
```

自定键盘还必须为用户提供切换键盘的方式。有关实现键盘切换按钮的更多信息，请参阅[添加自定用户界面](creating-a-custom-keyboard.md#Add-your-custom-user-interface)。

### 支持自动补全

为支持自动补全功能，你的键盘可以访问 [UILexicon](uilexicon.md)。结合使用此类和你自行设计的词典，在用户输入文本时提供建议和自动更正。[UILexicon](uilexicon.md) 对象包含来自多种来源的词语，包括：

- 用户「通讯录」数据库中未配对的名字和姓氏。
- 在「设置 \> 通用 \> 键盘 \> 快捷键」列表中定义的文本快捷键。
- 常用词词典。

### 指示听写支持

如果你的键盘提供使用听写输入文本的方式，请将 UIInputViewController 子类的 [hasDictationKey](uiinputviewcontroller/hasdictationkey.md) 属性设为 [true](../swift/true.md)。在某些情况下，iOS 可能会自动显示听写按钮（例如在配备面容 ID 的 iPhone 设备上）。将 [hasDictationKey](uiinputviewcontroller/hasdictationkey.md) 设为 [true](../swift/true.md) 后，iOS 不会显示系统按钮，因为两个执行听写的按钮会让用户感到困惑。

### 利用容器 App

设计自定键盘时，请记住可以利用容器 App 实现某些功能。例如，教程最适合放在父 App 中。你还可以在容器 App 中配置设置或选项，然后将这些设置存储到键盘能够读取的共享组容器中。如果容器 App 的唯一用途是交付自定键盘，它也必须提供某种实用功能，即使该功能仅用于提供信息。

有关更多设计指导，请参阅[人机界面指南](https://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards)。

## 另请参阅

### 键盘配置

- [为自定键盘配置开放访问权限](configuring-open-access-for-a-custom-keyboard.md) — 启用网络访问权限以及对共享组容器的写入权限。
