---
title: App 扩展
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/app-extensions
source_url: 'https://developer.apple.com/documentation/uikit/app-extensions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/app-extensions.json'
content_hash: 'sha256:6f90ecf2f9279f1d'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md)

# App 扩展

<sub>API 集合</sub>

将 App 的基本功能扩展到系统的其他部分。

## 主题

### 扩展支持

- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md) — App 扩展（extension）用于响应宿主 App 请求的接口。
- [NSExtensionContext](../foundation/nsextensioncontext.md) — 调用 App 扩展的宿主 App 上下文。

### 文稿提供程序

- [NSFileProviderExtension](../fileprovider/nsfileproviderextension.md) — 非复制型文件提供程序扩展的主类。
- [UIDocumentPickerExtensionViewController](uidocumentpickerextensionviewcontroller.md) — 文稿选择器视图控制器（view controller）扩展的主类。 _(已废弃)_

### 自定义键盘

- [UITextDocumentProxy](uitextdocumentproxy.md) — 一个为自定义键盘提供文本上下文的对象。
- [UIInputViewAudioFeedback](uiinputviewaudiofeedback.md) — 一个属性，使自定义输入视图或键盘配件视图能够播放标准键盘输入点击声。
- [UIInputViewController](uiinputviewcontroller.md) — 自定义键盘 App 扩展的主要视图控制器。
- [UILexicon](uilexicon.md) — 一个只读的词条对数组，每个词条对都位于自定义键盘的词典条目对象中。
- [UILexiconEntry](uilexiconentry.md) — 一个只读词条对，可在自定义键盘的词典对象中使用。

## 另请参阅

### App 结构

- [App 与环境](app-and-environment.md) — 管理生命周期事件和 App 的 UI 场景，并获取有关特性（trait）以及 App 运行环境的信息。
- [文稿、数据与粘贴板](documents-data-and-pasteboard.md) — 整理 App 的数据，并在粘贴板上共享这些数据。
- [资源管理](resource-management.md) — 管理用于实现 App 界面的图像、字符串、Storyboard 和 nib 文件。
- [进程间通信](interprocess-communication.md) — 向用户显示基于活动的服务。
- [Mac Catalyst](mac-catalyst.md) — 创建可供用户在 Mac 上运行的 iPad App 版本。
