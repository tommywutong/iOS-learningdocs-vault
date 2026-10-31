---
title: 键盘与输入
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/keyboards-and-input
source_url: 'https://developer.apple.com/documentation/uikit/keyboards-and-input'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/keyboards-and-input.json'
content_hash: 'sha256:6e95ab33740b26ed'
translated: true
---

> 导航： [Technologies](../technologies.md) · [UIKit](../uikit.md)

# 键盘与输入

<sub>API 集合</sub>

配置系统键盘、创建你自己的键盘来处理输入，或检测物理键盘上的按键。

## 主题

### 文本输入

- [UITextInput](uitextinput.md) — 一组用于与文本输入系统交互并在文档中启用功能的方法。
- [UITextInputDelegate](uitextinputdelegate.md) — 文档与文本输入系统之间的中介。
- [UIKeyInput](uikeyinput.md) — 响应者用于实现简单文本输入的一组方法。
- [UITextInputTraits](uitextinputtraits.md) — 一组定义文本对象键盘输入特性的方法。
- [UITextInputContext](uitextinputcontext.md) — 一个报告 App 接收的输入类型的对象。
- [UITextInputMode](uitextinputmode.md) — 当前的文本输入模式。
- [UITextInputAssistantItem](uitextinputassistantitem.md) — 一个管理你添加到 iPad 键盘上方快捷栏的自定栏按钮项目的对象。
- [UIDictationPhrase](uidictationphrase.md) — 一个表示用户听写短语的文本解释的对象。

### 文本交互

- [UITextInteraction](uitextinteraction.md) — 一个为自定文本视图提供文本选择手势与 UI 的交互。
- [UITextInteractionDelegate](uitextinteractiondelegate.md) — 一个对象实现的接口，用于接收文本交互事件相关信息。
- [UITextInteractionMode](uitextinteractionmode.md) — 决定文本交互提供的选择行为的模式。

### 自定文本选择

- [Adopting system selection UI in custom text views](adopting-system-selection-ui-in-custom-text-views.md) — 在 UIKit 的自定文本 UI 中融入系统文本选择体验。
- [UITextSelectionDisplayInteraction](uitextselectiondisplayinteraction.md) — 一个提供用于显示文本选择的系统 UI 的对象。
- [UITextSelectionHighlightView](uitextselectionhighlightview.md) — 一个用于为选中文本提供自定高亮 UI 的接口。
- [UITextSelectionHandleView](uitextselectionhandleview.md) — 一个用于绘制文本范围自定选择手柄的接口。
- [UITextCursorView](uitextcursorview.md) — 一个用于在一段文本中绘制插入点的接口。
- [UIStandardTextCursorView](uistandardtextcursorview.md) — 一个在一段文本中绘制标准系统插入点的视图。
- [UITextCursorDropPositionAnimator](uitextcursordroppositionanimator.md)
- [UITextLoupeSession](uitextloupesession.md) — 一个管理在你指定位置呈现系统放大镜的对象。

### 文本操作与菜单

- [UITextItem](uitextitem.md) — 一个用于将自定操作与菜单附加到链接、文本附件或其他特定文本的对象。
- [MenuConfiguration](uitextitem/menuconfiguration.md) — 一个描述为文本项目显示何种菜单与预览的对象。
- [UITextViewDelegate](uitextviewdelegate.md) — 用于接收文本视图对象编辑相关消息的方法。

### 消息的 Smart Reply

- [Adopting Smart Reply in your messaging or email app](adopting-smart-reply-in-your-messaging-or-email-app.md) — 使用 Apple Intelligence 生成回复建议，并将所选文本放入你的文本 UI。
- [UIConversationContext](uiconversationcontext.md) — 一个表示参与者之间对话的基类，例如邮件或消息 App 中的对话。
- [Entry](uiconversationcontext/entry.md) — 一个表示对话中一条消息的基类。
- [UIMailConversationContext](uimailconversationcontext.md) — 一个表示邮件对话的类。
- [MailEntry](uimailconversationcontext/mailentry.md) — 一个表示邮件线程中特定邮件的类。
- [UIMessageConversationContext](uimessageconversationcontext.md) — 一个表示消息对话的类。
- [MessageEntry](uimessageconversationcontext/messageentry.md) — 一个表示消息对话中一条消息的类。
- [UIInputSuggestion](uiinputsuggestion.md) — 一个用于处理来自键盘或系统的建议的基类。
- [UIPhotoSearchSuggestion](uiphotosearchsuggestion.md) — 一个携带人物、主题、位置与时间段照片搜索元数据的输入建议。 _(beta)_
- [UISmartReplySuggestion](uismartreplysuggestion.md) — 一个用于处理 Smart Reply 建议的类。

### 文本分词器

- [UITextInputTokenizer](uitextinputtokenizer.md) — 一个分词器，即允许文本输入系统评估不同粒度文本单位的对象。
- [UITextInputStringTokenizer](uitextinputstringtokenizer.md) — 文本输入分词器协议的基础实现。

### 键盘布局

- [Adjusting your layout with keyboard layout guide](adjusting-your-layout-with-keyboard-layout-guide.md) — 使用键盘布局指南的跟踪功能动态响应键盘移动。
- [UIKeyboardLayoutGuide](uikeyboardlayoutguide.md) — 一个表示键盘在 App 布局中所占空间的布局指南。
- [UITrackingLayoutGuide](uitrackinglayoutguide.md) — 一个根据与边缘的接近程度自动激活与停用布局约束的布局指南。

### 自定键盘

- [Creating a custom keyboard](creating-a-custom-keyboard.md) — 向 Xcode 项目添加扩展，以提供系统级自定文本输入。
- [UIInputViewController](uiinputviewcontroller.md) — 自定键盘 App 扩展的主视图控制器。
- [UIInputView](uiinputview.md) — 一个在视图成为第一响应者时显示并管理该视图自定输入的对象。
- [UILexicon](uilexicon.md) — 一个只读的术语对数组，每个术语对都在词典条目对象中，供自定键盘使用。
- [UILexiconEntry](uilexiconentry.md) — 一个只读的术语对，可在词典对象中供自定键盘使用。
- [UITextDocumentProxy](uitextdocumentproxy.md) — 一个向自定键盘提供文本上下文的对象。

### 物理键盘

- [Handling key presses made on a physical keyboard](handling-key-presses-made-on-a-physical-keyboard.md) — 检测某人何时在物理键盘上按下与释放按键。
- [Navigating an app’s user interface using a keyboard](navigating-an-app-s-user-interface-using-a-keyboard.md) — 在 iPad App 与使用 Mac Catalyst 构建的 App 中，使用键盘与可聚焦 UI 元素在用户界面元素间导航。
- [Adding hardware keyboard support to your app](adding-hardware-keyboard-support-to-your-app.md) — 通过处理原始键盘事件、编写自定键盘快捷键以及使用手势识别器来增强与 App 的交互。
- [UIKey](uikey.md) — 一个提供键盘按键状态信息的对象。
- [UIKeyboardHIDUsage](uikeyboardhidusage.md) — 一组标识 USB 键盘按键的 HID 使用码。

## 另请参阅

### 文本

- [Text display and fonts](text-display-and-fonts.md) — 显示文本、管理字体并检查拼写。
- [TextKit](textkit.md) — 管理文本存储，并对 App 视图中的文本内容执行自定布局。
- [Writing Tools](writing-tools.md) — 为 App 的文本视图添加写作工具支持。
- [Handwriting recognition](handwriting-recognition.md) — 配置接受文本的文本栏与自定视图，以处理来自 Apple Pencil 的输入。
