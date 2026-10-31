---
title: 模态呈现方式
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/modal-presentations
source_url: 'https://developer.apple.com/documentation/swiftui/modal-presentations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modal-presentations.json'
content_hash: 'sha256:f6c88f816da532b3'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md)

# 模态呈现方式

<sub>API 集合</sub>

在提供专注交互的独立视图中呈现内容。

## 概述

为了引起人们对一个重要的、范围狭窄的任务的注意，你可以显示一个模态呈现，例如提醒、弹出窗口、表单或确认对话框。

![](../../../attachments/669dc3d73261bcf3bda09c163d0c4f64/modal-presentations-hero@2x.png)

在 SwiftUI 中，你使用视图修饰符来创建模态呈现，该修饰符定义呈现的外观以及 SwiftUI 呈现它的条件。SwiftUI 会检测条件的变化并代你完成呈现。由于你为触发呈现的条件提供了一个 [Binding](binding.md)，SwiftUI 可以在用户关闭呈现时重置其底层值。

有关设计指引，请参阅《人机界面指南》中的[模态化](../design/human-interface-guidelines/modality.md)。

## 主题

### 配置对话框

- [DialogSeverity](dialogseverity.md) — 提醒或确认对话框的严重程度。

### 显示表单、覆盖层或弹出窗口

- [sheet(isPresented:onDismiss:content:)](<view/sheet(ispresented_ondismiss_content_).md>) — 当你提供的绑定到布尔值的绑定变为 true 时呈现一个表单。
- [sheet(item:onDismiss:content:)](<view/sheet(item_ondismiss_content_).md>) — 呈现一个表单，使用给定条目作为表单内容的数据源。
- [fullScreenCover(isPresented:onDismiss:content:)](<view/fullscreencover(ispresented_ondismiss_content_).md>) — 当你提供的绑定到布尔值的绑定变为 true 时呈现一个尽可能覆盖整个屏幕的模态视图。
- [fullScreenCover(item:onDismiss:content:)](<view/fullscreencover(item_ondismiss_content_).md>) — 呈现一个尽可能覆盖整个屏幕的模态视图，使用你提供的绑定作为表单内容的数据源。
- [popover(item:attachmentAnchor:arrowEdge:content:)](<view/popover(item_attachmentanchor_arrowedge_content_).md>) — 呈现一个弹出窗口，使用给定条目作为弹出窗口内容的数据源。
- [popover(isPresented:attachmentAnchor:arrowEdge:content:)](<view/popover(ispresented_attachmentanchor_arrowedge_content_).md>) — 当给定条件为真时呈现一个弹出窗口。
- [PopoverAttachmentAnchor](popoverattachmentanchor.md) — 弹出窗口的附加锚点。

### 调整呈现尺寸

- [presentationCompactAdaptation(horizontal:vertical:)](<view/presentationcompactadaptation(horizontal_vertical_).md>) — 指定如何将呈现内容适配到水平和垂直紧凑尺寸类别。
- [presentationCompactAdaptation(_:)](<view/presentationcompactadaptation(__).md>) — 指定如何将呈现内容适配到紧凑尺寸类别。
- [PresentationAdaptation](presentationadaptation.md) — 将呈现内容适配到不同尺寸类别的策略。
- [presentationSizing(_:)](<view/presentationsizing(__).md>) — 设置所包含呈现内容的尺寸调整方式。
- [PresentationSizing](presentationsizing.md) — 一种类型，定义呈现内容的尺寸，以及呈现尺寸如何随其内容尺寸的变化而调整。
- [PresentationSizingRoot](presentationsizingroot.md) — 提供给呈现内容、具有已定义呈现尺寸的视图的代理。
- [PresentationSizingContext](presentationsizingcontext.md) — 关于呈现内容的上下文信息。

### 配置表单高度

- [presentationDetents(_:)](<view/presentationdetents(__).md>) — 设置所包含表单可用的 detent。
- [presentationDetents(_:selection:)](<view/presentationdetents(__selection_).md>) — 设置所包含表单可用的 detent，让你能够以编程方式控制当前选定的 detent。
- [presentationContentInteraction(_:)](<view/presentationcontentinteraction(__).md>) — 配置在呈现内容上的轻扫手势行为。
- [presentationDragIndicator(_:)](<view/presentationdragindicator(__).md>) — 设置表单顶部拖动指示器的可见性。
- [PresentationDetent](presentationdetent.md) — 一种表示表单自然停留位置高度的类型。
- [CustomPresentationDetent](custompresentationdetent.md) — 具有计算高度的自定义 detent 的定义。
- [PresentationContentInteraction](presentationcontentinteraction.md) — 一种行为，可用于影响呈现内容如何响应轻扫手势。

### 设置表单及其背景的样式

- [presentationCornerRadius(_:)](<view/presentationcornerradius(__).md>) — 请求呈现内容具有特定的圆角半径。
- [presentationBackground(_:)](<view/presentationbackground(__).md>) — 使用形状样式设置所包含表单的呈现背景。
- [presentationBackground(alignment:content:)](<view/presentationbackground(alignment_content_).md>) — 将所包含表单的呈现背景设置为自定义视图。
- [presentationBackgroundInteraction(_:)](<view/presentationbackgroundinteraction(__).md>) — 控制人们是否可以与呈现内容背后的视图交互。
- [PresentationBackgroundInteraction](presentationbackgroundinteraction.md) — 呈现内容背后的视图可用的交互类型。

### 呈现提醒

- [AlertScene](alertscene.md) — 一种将自己呈现为独立提醒对话框的场景。
- [alert(_:isPresented:actions:)](<view/alert(__ispresented_actions_).md>) — 当给定条件为真时呈现一个提醒，标题使用本地化字符串资源。
- [alert(_:isPresented:presenting:actions:)](<view/alert(__ispresented_presenting_actions_).md>) — 呈现一个提醒，使用给定的数据生成提醒内容，标题使用本地化字符串资源。
- [alert(_:item:actions:)](<view/alert(__item_actions_).md>) — 呈现一个提醒，使用给定的数据生成提醒内容，标题使用一个文本视图。
- [alert(error:actions:)](<view/alert(error_actions_).md>) — 当存在错误时呈现一个提醒。
- [alert(isPresented:error:actions:)](<view/alert(ispresented_error_actions_).md>) — 当存在错误时呈现一个提醒。
- [alert(_:isPresented:actions:message:)](<view/alert(__ispresented_actions_message_).md>) — 当给定条件为真时呈现一个带消息的提醒，标题使用本地化字符串资源。
- [alert(_:isPresented:presenting:actions:message:)](<view/alert(__ispresented_presenting_actions_message_).md>) — 呈现一个带消息的提醒，使用给定的数据生成提醒内容，标题使用本地化字符串资源。
- [alert(_:item:actions:message:)](<view/alert(__item_actions_message_).md>) — 呈现一个带消息的提醒，使用给定的数据生成提醒内容，标题使用本地化字符串键。
- [alert(error:actions:message:)](<view/alert(error_actions_message_).md>) — 当存在错误时呈现一个带消息的提醒。
- [alert(isPresented:error:actions:message:)](<view/alert(ispresented_error_actions_message_).md>) — 当存在错误时呈现一个带消息的提醒。

### 为操作获取确认

- [confirmationDialog(_:isPresented:titleVisibility:actions:)](<view/confirmationdialog(__ispresented_titlevisibility_actions_).md>) — 当给定条件为真时呈现一个确认对话框，标题使用本地化字符串资源。
- [confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)](<view/confirmationdialog(__ispresented_titlevisibility_presenting_actions_).md>) — 呈现一个确认对话框，使用数据生成对话框内容，标题使用本地化字符串资源。
- [dismissalConfirmationDialog(_:shouldPresent:actions:)](<view/dismissalconfirmationdialog(__shouldpresent_actions_).md>) — 在关闭操作被触发时呈现一个确认对话框。

### 显示带消息的确认对话框

- [confirmationDialog(_:isPresented:titleVisibility:actions:message:)](<view/confirmationdialog(__ispresented_titlevisibility_actions_message_).md>) — 当给定条件为真时呈现一个带消息的确认对话框，标题使用本地化字符串资源。
- [confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)](<view/confirmationdialog(__ispresented_titlevisibility_presenting_actions_message_).md>) — 呈现一个带消息的确认对话框，使用数据生成对话框内容，标题使用本地化字符串资源。
- [dismissalConfirmationDialog(_:shouldPresent:actions:message:)](<view/dismissalconfirmationdialog(__shouldpresent_actions_message_).md>) — 在关闭操作被触发时呈现一个带消息的确认对话框。

### 配置对话框

- [dialogIcon(_:)](<view/dialogicon(__).md>) — 配置此视图内的对话框所使用的图标。
- [dialogIcon(_:)](<scene/dialogicon(__).md>) — 配置提醒所使用的图标。
- [dialogSeverity(_:)](<view/dialogseverity(__).md>)
- [dialogSeverity(_:)](<scene/dialogseverity(__).md>) — 设置提醒的严重程度。
- [dialogSuppressionToggle(isSuppressed:)](<view/dialogsuppressiontoggle(issuppressed_).md>) — 允许用户抑制 `self` 内呈现的对话框和提醒，在 macOS 上使用默认的抑制消息。在其他平台上不使用。
- [dialogSuppressionToggle(isSuppressed:)](<scene/dialogsuppressiontoggle(issuppressed_).md>) — 允许用户使用自定义的抑制消息来抑制提醒。
- [dialogSuppressionToggle(_:isSuppressed:)](<view/dialogsuppressiontoggle(__issuppressed_).md>) — 允许用户抑制 `self` 内呈现的对话框和提醒，在 macOS 上使用自定义的抑制消息。在其他平台上不使用。
- [dialogSuppressionToggle(_:isSuppressed:)](<scene/dialogsuppressiontoggle(__issuppressed_).md>) — 允许用户使用自定义的抑制消息来抑制提醒。
- [dialogPreventsAppTermination(_:)](<view/dialogpreventsapptermination(__).md>) — 提醒或确认对话框是否阻止 App 被系统或 App 终止菜单项退出/终止。

### 导出到文件

- [fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)](<view/fileexporter(ispresented_document_contenttype_defaultfilename_oncompletion_).md>) — 呈现一个系统对话框，用于将储存在值类型（例如结构体）中的文稿导出为磁盘上的文件。 _(已废弃)_
- [fileExporter(isPresented:documents:contentType:onCompletion:)](<view/fileexporter(ispresented_documents_contenttype_oncompletion_).md>) — 呈现一个系统对话框，用于将值类型文稿的集合导出为磁盘上的文件。 _(已废弃)_
- [fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:onCancellation:)](<view/fileexporter(ispresented_document_contenttype_defaultfilename_oncompletion_oncancellation_).md>) — 呈现一个系统对话框，允许用户将 `WritableDocument` 导出为磁盘上的文件。 _(beta)_
- [fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)](<view/fileexporter(ispresented_document_contenttypes_defaultfilename_oncompletion_oncancellation_).md>) — 呈现一个系统对话框，允许用户将 `FileDocument` 导出为磁盘上的文件。 _(已废弃)_
- [fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)](<view/fileexporter(ispresented_documents_contenttypes_oncompletion_oncancellation_).md>) — 呈现一个系统对话框，允许用户将一组符合 `WritableDocument` 的对象导出为磁盘上的文件。 _(beta)_
- [fileExporter(isPresented:item:contentTypes:defaultFilename:onCompletion:onCancellation:)](<view/fileexporter(ispresented_item_contenttypes_defaultfilename_oncompletion_oncancellation_).md>) — 呈现一个系统对话框，允许用户将一个 `Transferable` 条目导出为磁盘上的文件。
- [fileExporter(isPresented:items:contentTypes:onCompletion:onCancellation:)](<view/fileexporter(ispresented_items_contenttypes_oncompletion_oncancellation_).md>) — 呈现一个系统对话框，允许用户将一组 `Transferable` 条目导出为磁盘上的文件。
- [fileExporterFilenameLabel(_:)](<view/fileexporterfilenamelabel(__).md>) — 在 macOS 上，为 `fileExporter` 配置文件名栏位的标签。

### 从文件导入

- [fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:)](<view/fileimporter(ispresented_allowedcontenttypes_allowsmultipleselection_oncompletion_).md>) — 呈现一个系统对话框，允许用户导入多个文件。
- [fileImporter(isPresented:allowedContentTypes:onCompletion:)](<view/fileimporter(ispresented_allowedcontenttypes_oncompletion_).md>) — 呈现一个系统对话框，允许用户导入一个现有文件。
- [fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:onCancellation:)](<view/fileimporter(ispresented_allowedcontenttypes_allowsmultipleselection_oncompletion_oncancellation_).md>) — 呈现一个系统对话框，允许用户导入多个文件。

### 移动文件

- [fileMover(isPresented:file:onCompletion:)](<view/filemover(ispresented_file_oncompletion_).md>) — 呈现一个系统对话框，允许用户将一个现有文件移动到新位置。
- [fileMover(isPresented:files:onCompletion:)](<view/filemover(ispresented_files_oncompletion_).md>) — 呈现一个系统对话框，允许用户将一组现有文件移动到新位置。
- [fileMover(isPresented:file:onCompletion:onCancellation:)](<view/filemover(ispresented_file_oncompletion_oncancellation_).md>) — 呈现一个系统对话框，允许用户将一个现有文件移动到新位置。
- [fileMover(isPresented:files:onCompletion:onCancellation:)](<view/filemover(ispresented_files_oncompletion_oncancellation_).md>) — 呈现一个系统对话框，允许用户将一组现有文件移动到新位置。

### 配置文件对话框

- [fileDialogBrowserOptions(_:)](<view/filedialogbrowseroptions(__).md>) — 在 macOS 上，配置 `fileExporter`、`fileImporter` 或 `fileMover` 以提供精细的 URL 搜索体验：包含或排除隐藏文件、允许按标签搜索等。
- [fileDialogConfirmationLabel(_:)](<view/filedialogconfirmationlabel(__).md>) — 在 macOS 上，为 `fileExporter`、`fileImporter` 或 `fileMover` 配置自定义的确认按钮标签。
- [fileDialogCustomizationID(_:)](<view/filedialogcustomizationid(__).md>) — 在 macOS 上，配置 `fileExporter`、`fileImporter` 或 `fileMover` 以持久化和恢复文件对话框配置。
- [fileDialogDefaultDirectory(_:)](<view/filedialogdefaultdirectory(__).md>) — 配置 `fileExporter`、`fileImporter` 或 `fileMover` 以指定的默认目录打开。
- [fileDialogImportsUnresolvedAliases(_:)](<view/filedialogimportsunresolvedaliases(__).md>) — 在 macOS 上，配置用户选择替身时 `fileExporter`、`fileImporter` 或 `fileMover` 的行为。
- [fileDialogMessage(_:)](<view/filedialogmessage(__).md>) — 在 macOS 上，为 `fileExporter`、`fileImporter` 或 `fileMover` 配置呈现给用户的自定义消息，类似于标题。
- [fileDialogURLEnabled(_:)](<view/filedialogurlenabled(__).md>) — 在 macOS 上，配置 `fileImporter` 或 `fileMover` 以有条件地停用所呈现的 URL。
- [FileDialogBrowserOptions](filedialogbrowseroptions.md) — 文件对话框呈现文件系统的方式。

### 呈现检查器

- [inspector(isPresented:content:)](<view/inspector(ispresented_content_).md>) — 在视图层级结构中的应用位置插入一个检查器。
- [inspectorColumnWidth(_:)](<view/inspectorcolumnwidth(__).md>) — 为包含此视图的检查器设置固定的首选宽度，该检查器以尾栏形式呈现。
- [inspectorColumnWidth(min:ideal:max:)](<view/inspectorcolumnwidth(min_ideal_max_).md>) — 为以尾栏形式呈现的检查器设置灵活的首选宽度。

### 关闭呈现内容

- [isPresented](environmentvalues/ispresented.md) — 一个布尔值，指示与此环境关联的视图当前是否被呈现。
- [dismiss](environmentvalues/dismiss.md) — 一个关闭当前呈现内容的动作。
- [DismissAction](dismissaction.md) — 一个关闭呈现内容的动作。
- [interactiveDismissDisabled(_:)](<view/interactivedismissdisabled(__).md>) — 有条件地阻止以交互方式关闭弹出窗口、表单和检查器等呈现内容。

### 已废弃的模态呈现方式

- [Alert](alert.md) — 一种提醒呈现的表示。 _(已废弃)_
- [ActionSheet](actionsheet.md) — 一种操作表单呈现的表示。 _(已废弃)_

## 另请参阅

### App 结构

- [App 组织](app-organization.md) — 定义 App 的入口点和顶层结构。
- [场景](scenes.md) — 声明构成 App 各个部分的用户界面分组。
- [窗口](windows.md) — 在一个窗口或一组窗口中显示用户界面内容。
- [沉浸式空间](immersive-spaces.md) — 在用户周围显示无边界的内容。
- [文稿](documents.md) — 让人们能够打开和管理文稿。
- [导航](navigation.md) — 使用户能够在场景内你的 App 视图层级结构的不同部分之间移动。
- [工具栏](toolbars.md) — 提供对常用命令和控制的即时访问。
- [搜索](search.md) — 让人们能够搜索你的 App 内的文本或其他内容。
- [App 扩展](app-extensions.md) — 将你的 App 的基本功能扩展到系统的其他部分，例如添加小组件。
