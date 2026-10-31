---
title: 呈现修饰符
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-presentation
source_url: 'https://developer.apple.com/documentation/swiftui/view-presentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-presentation.json'
content_hash: 'sha256:802dcf2ae1161b2b'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [视图基础](view-fundamentals.md) · [View](view.md)

# 呈现修饰符

<sub>API 集合</sub>

为视图定义在指定条件下呈现的其他视图。

## 概述

使用呈现修饰符来显示不同类型的模态呈现，例如提醒、弹出窗口、表单和确认对话框。

由于 SwiftUI 是一个声明式框架，你不需要在想要呈现模态的那一刻去调用某个方法。相反，你定义呈现的外观，以及 SwiftUI 应当在什么条件下进行呈现。SwiftUI 会检测条件的变化并代你完成呈现。由于你为触发呈现的条件提供了一个 [Binding](binding.md)，SwiftUI 可以在用户关闭呈现时重置其底层值。

有关如何使用这些修饰符的更多信息，请参阅[模态呈现方式](modal-presentations.md)。

## 主题

### 提醒

- [alert(_:isPresented:actions:)](<view/alert(__ispresented_actions_).md>) — 当给定条件为真时呈现一个提醒，标题使用本地化字符串资源。
- [alert(_:isPresented:presenting:actions:)](<view/alert(__ispresented_presenting_actions_).md>) — 呈现一个提醒，使用给定的数据生成提醒内容，标题使用本地化字符串资源。
- [alert(_:item:actions:)](<view/alert(__item_actions_).md>) — 呈现一个提醒，使用给定的数据生成提醒内容，标题使用一个文本视图。
- [alert(error:actions:)](<view/alert(error_actions_).md>) — 当存在错误时呈现一个提醒。
- [alert(isPresented:error:actions:)](<view/alert(ispresented_error_actions_).md>) — 当存在错误时呈现一个提醒。

### 带消息的提醒

- [alert(_:isPresented:actions:message:)](<view/alert(__ispresented_actions_message_).md>) — 当给定条件为真时呈现一个带消息的提醒，标题使用本地化字符串资源。
- [alert(_:isPresented:presenting:actions:message:)](<view/alert(__ispresented_presenting_actions_message_).md>) — 呈现一个带消息的提醒，使用给定的数据生成提醒内容，标题使用本地化字符串资源。
- [alert(_:item:actions:message:)](<view/alert(__item_actions_message_).md>) — 呈现一个带消息的提醒，使用给定的数据生成提醒内容，标题使用本地化字符串键。
- [alert(error:actions:message:)](<view/alert(error_actions_message_).md>) — 当存在错误时呈现一个带消息的提醒。
- [alert(isPresented:error:actions:message:)](<view/alert(ispresented_error_actions_message_).md>) — 当存在错误时呈现一个带消息的提醒。

### 确认对话框

- [confirmationDialog(_:isPresented:titleVisibility:actions:)](<view/confirmationdialog(__ispresented_titlevisibility_actions_).md>) — 当给定条件为真时呈现一个确认对话框，标题使用本地化字符串资源。
- [confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)](<view/confirmationdialog(__ispresented_titlevisibility_presenting_actions_).md>) — 呈现一个确认对话框，使用数据生成对话框内容，标题使用本地化字符串资源。
- [confirmationDialog(_:item:titleVisibility:actions:)](<view/confirmationdialog(__item_titlevisibility_actions_).md>) — 呈现一个确认对话框，使用数据生成对话框内容，标题使用一个文本视图。
- [dismissalConfirmationDialog(_:shouldPresent:actions:)](<view/dismissalconfirmationdialog(__shouldpresent_actions_).md>) — 在关闭操作被触发时呈现一个确认对话框。

### 带消息的确认对话框

- [confirmationDialog(_:isPresented:titleVisibility:actions:message:)](<view/confirmationdialog(__ispresented_titlevisibility_actions_message_).md>) — 当给定条件为真时呈现一个带消息的确认对话框，标题使用本地化字符串资源。
- [confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)](<view/confirmationdialog(__ispresented_titlevisibility_presenting_actions_message_).md>) — 呈现一个带消息的确认对话框，使用数据生成对话框内容，标题使用本地化字符串资源。
- [confirmationDialog(_:item:titleVisibility:actions:message:)](<view/confirmationdialog(__item_titlevisibility_actions_message_).md>) — 呈现一个带消息的确认对话框，使用数据生成对话框内容，消息使用一个文本视图。
- [dismissalConfirmationDialog(_:shouldPresent:actions:message:)](<view/dismissalconfirmationdialog(__shouldpresent_actions_message_).md>) — 在关闭操作被触发时呈现一个带消息的确认对话框。

### 对话框配置

- [dialogIcon(_:)](<view/dialogicon(__).md>) — 配置此视图内的对话框所使用的图标。
- [dialogSeverity(_:)](<view/dialogseverity(__).md>)
- [dialogSuppressionToggle(isSuppressed:)](<view/dialogsuppressiontoggle(issuppressed_).md>) — 允许用户抑制 `self` 内呈现的对话框和提醒，在 macOS 上使用默认的抑制消息。在其他平台上不使用。
- [dialogSuppressionToggle(_:isSuppressed:)](<view/dialogsuppressiontoggle(__issuppressed_).md>) — 允许用户抑制 `self` 内呈现的对话框和提醒，在 macOS 上使用自定义的抑制消息。在其他平台上不使用。
- [dialogPreventsAppTermination(_:)](<view/dialogpreventsapptermination(__).md>) — 提醒或确认对话框是否阻止 App 被系统或 App 退出菜单项退出/终止。

### 表单

- [sheet(isPresented:onDismiss:content:)](<view/sheet(ispresented_ondismiss_content_).md>) — 当你提供的绑定到布尔值的绑定变为 true 时呈现一个表单。
- [sheet(item:onDismiss:content:)](<view/sheet(item_ondismiss_content_).md>) — 呈现一个表单，使用给定条目作为表单内容的数据源。
- [fullScreenCover(isPresented:onDismiss:content:)](<view/fullscreencover(ispresented_ondismiss_content_).md>) — 当你提供的绑定到布尔值的绑定变为 true 时呈现一个尽可能覆盖整个屏幕的模态视图。
- [fullScreenCover(item:onDismiss:content:)](<view/fullscreencover(item_ondismiss_content_).md>) — 呈现一个尽可能覆盖整个屏幕的模态视图，使用你提供的绑定作为表单内容的数据源。

### 弹出窗口

- [popover(item:attachmentAnchor:arrowEdge:content:)](<view/popover(item_attachmentanchor_arrowedge_content_).md>) — 呈现一个弹出窗口，使用给定条目作为弹出窗口内容的数据源。
- [popover(isPresented:attachmentAnchor:arrowEdge:content:)](<view/popover(ispresented_attachmentanchor_arrowedge_content_).md>) — 当给定条件为真时呈现一个弹出窗口。

### 表单和弹出窗口配置

- [interactiveDismissDisabled(_:)](<view/interactivedismissdisabled(__).md>) — 有条件地阻止以交互方式关闭弹出窗口、表单和检查器等呈现内容。
- [presentationDetents(_:)](<view/presentationdetents(__).md>) — 设置所包含表单可用的 detent。
- [presentationDetents(_:selection:)](<view/presentationdetents(__selection_).md>) — 设置所包含表单可用的 detent，让你能够以编程方式控制当前选定的 detent。
- [presentationDragIndicator(_:)](<view/presentationdragindicator(__).md>) — 设置表单顶部拖动指示器的可见性。
- [presentationBackground(_:)](<view/presentationbackground(__).md>) — 使用形状样式设置所包含表单的呈现背景。
- [presentationBackground(alignment:content:)](<view/presentationbackground(alignment_content_).md>) — 将所包含表单的呈现背景设置为自定义视图。
- [presentationBackgroundInteraction(_:)](<view/presentationbackgroundinteraction(__).md>) — 控制人们是否可以与呈现内容背后的视图交互。
- [presentationCompactAdaptation(horizontal:vertical:)](<view/presentationcompactadaptation(horizontal_vertical_).md>) — 指定如何让呈现内容适配水平和垂直紧凑尺寸类别。
- [presentationCompactAdaptation(_:)](<view/presentationcompactadaptation(__).md>) — 指定如何让呈现内容适配紧凑尺寸类别。
- [presentationContentInteraction(_:)](<view/presentationcontentinteraction(__).md>) — 配置在呈现内容上的轻扫手势行为。
- [presentationCornerRadius(_:)](<view/presentationcornerradius(__).md>) — 请求呈现内容具有特定的圆角半径。
- [presentationSizing(_:)](<view/presentationsizing(__).md>) — 设置所包含呈现内容的尺寸调整方式。
- [presentationBreakthroughEffect(_:)](<view/presentationbreakthrougheffect(__).md>) — 更改所包含呈现内容穿透遮挡其上的内容的方式。
- [presentationPreventsAppTermination(_:)](<view/presentationpreventsapptermination(__).md>) — 呈现内容是否阻止 App 被系统或 App 退出菜单项终止/退出。

### 文件导出器

- [fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)](<view/fileexporter(ispresented_document_contenttype_defaultfilename_oncompletion_).md>) — 呈现一个系统对话框，用于将储存在值类型（例如结构体）中的文稿导出为磁盘上的文件。 _(已废弃)_
- [fileExporter(isPresented:documents:contentType:onCompletion:)](<view/fileexporter(ispresented_documents_contenttype_oncompletion_).md>) — 呈现一个系统对话框，用于将值类型文稿的集合导出为磁盘上的文件。 _(已废弃)_
- [fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:onCancellation:)](<view/fileexporter(ispresented_document_contenttype_defaultfilename_oncompletion_oncancellation_).md>) — 呈现一个系统对话框，允许用户将 `WritableDocument` 导出为磁盘上的文件。 _(beta)_
- [fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)](<view/fileexporter(ispresented_document_contenttypes_defaultfilename_oncompletion_oncancellation_).md>) — 呈现一个系统对话框，允许用户将 `FileDocument` 导出为磁盘上的文件。 _(已废弃)_
- [fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)](<view/fileexporter(ispresented_documents_contenttypes_oncompletion_oncancellation_).md>) — 呈现一个系统对话框，允许用户将一组符合 `WritableDocument` 的对象导出为磁盘上的文件。 _(beta)_
- [fileExporter(isPresented:item:contentTypes:defaultFilename:onCompletion:onCancellation:)](<view/fileexporter(ispresented_item_contenttypes_defaultfilename_oncompletion_oncancellation_).md>) — 呈现一个系统对话框，允许用户将一个 `Transferable` 条目导出为磁盘上的文件。
- [fileExporter(isPresented:items:contentTypes:onCompletion:onCancellation:)](<view/fileexporter(ispresented_items_contenttypes_oncompletion_oncancellation_).md>) — 呈现一个系统对话框，允许用户将一组 `Transferable` 条目导出为磁盘上的文件。
- [fileExporterFilenameLabel(_:)](<view/fileexporterfilenamelabel(__).md>) — 在 macOS 上，为 `fileExporter` 配置文件名栏位的标签。

### 文件导入器

- [fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:)](<view/fileimporter(ispresented_allowedcontenttypes_allowsmultipleselection_oncompletion_).md>) — 呈现一个系统对话框，允许用户导入多个文件。
- [fileImporter(isPresented:allowedContentTypes:onCompletion:)](<view/fileimporter(ispresented_allowedcontenttypes_oncompletion_).md>) — 呈现一个系统对话框，允许用户导入一个现有文件。
- [fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:onCancellation:)](<view/fileimporter(ispresented_allowedcontenttypes_allowsmultipleselection_oncompletion_oncancellation_).md>) — 呈现一个系统对话框，允许用户导入多个文件。

### 文件移动器

- [fileMover(isPresented:file:onCompletion:)](<view/filemover(ispresented_file_oncompletion_).md>) — 呈现一个系统对话框，允许用户将一个现有文件移动到新位置。
- [fileMover(isPresented:files:onCompletion:)](<view/filemover(ispresented_files_oncompletion_).md>) — 呈现一个系统对话框，允许用户将一组现有文件移动到新位置。
- [fileMover(isPresented:file:onCompletion:onCancellation:)](<view/filemover(ispresented_file_oncompletion_oncancellation_).md>) — 呈现一个系统对话框，允许用户将一个现有文件移动到新位置。
- [fileMover(isPresented:files:onCompletion:onCancellation:)](<view/filemover(ispresented_files_oncompletion_oncancellation_).md>) — 呈现一个系统对话框，允许用户将一组现有文件移动到新位置。

### 文件对话框配置

- [fileDialogBrowserOptions(_:)](<view/filedialogbrowseroptions(__).md>) — 在 macOS 上，配置 `fileExporter`、`fileImporter` 或 `fileMover` 以提供精细的 URL 搜索体验：包含或排除隐藏文件、允许按标签搜索等。
- [fileDialogConfirmationLabel(_:)](<view/filedialogconfirmationlabel(__).md>) — 在 macOS 上，为 `fileExporter`、`fileImporter` 或 `fileMover` 配置自定义的确认按钮标签。
- [fileDialogCustomizationID(_:)](<view/filedialogcustomizationid(__).md>) — 在 macOS 上，配置 `fileExporter`、`fileImporter` 或 `fileMover` 以持久化和恢复文件对话框配置。
- [fileDialogDefaultDirectory(_:)](<view/filedialogdefaultdirectory(__).md>) — 配置 `fileExporter`、`fileImporter` 或 `fileMover` 以指定的默认目录打开。
- [fileDialogImportsUnresolvedAliases(_:)](<view/filedialogimportsunresolvedaliases(__).md>) — 在 macOS 上，配置用户选择替身时 `fileExporter`、`fileImporter` 或 `fileMover` 的行为。
- [fileDialogMessage(_:)](<view/filedialogmessage(__).md>) — 在 macOS 上，为 `fileExporter`、`fileImporter` 或 `fileMover` 配置呈现给用户的自定义消息，类似于标题。
- [fileDialogURLEnabled(_:)](<view/filedialogurlenabled(__).md>) — 在 macOS 上，配置 `fileImporter` 或 `fileMover` 以有条件地停用所呈现的 URL。

### 注视流式传输

- [foveatedStreamingPauseSheet(session:)](<view/foveatedstreamingpausesheet(session_).md>) — 告知系统在注视流式传输会话暂停时呈现一个带有恢复或结束该会话控制的表单。

### 屏幕捕捉

- [recordingEditor(_:)](<view/recordingeditor(__).md>) — 为给定的录制 URL 呈现录制编辑器。 _(beta)_
- [recordingEditor(_:mode:)](<view/recordingeditor(__mode_).md>) — 以特定模式为给定的录制 URL 呈现录制编辑器。 _(beta)_

### 文稿浏览器

- [documentLaunchTitle(_:)](<view/documentlaunchtitle(__).md>) — 设置文稿启动卡片上显示的标题。 _(beta)_
- [documentLaunchSubtitle(_:)](<view/documentlaunchsubtitle(__).md>) — 设置文稿启动卡片上标题下方显示的副标题。 _(beta)_
- [documentBrowserContextMenu(_:)](<view/documentbrowsercontextmenu(__).md>) — 向 `DocumentLaunchView` 添加接受所选文件列表作为参数的操作。

### 检查器

- [inspector(isPresented:content:)](<view/inspector(ispresented_content_).md>) — 在视图层级结构中的应用位置插入一个检查器。
- [inspectorColumnWidth(_:)](<view/inspectorcolumnwidth(__).md>) — 为包含此视图的检查器设置固定的首选宽度，该检查器以尾栏形式呈现。
- [inspectorColumnWidth(min:ideal:max:)](<view/inspectorcolumnwidth(min_ideal_max_).md>) — 为以尾栏形式呈现的检查器设置灵活的首选宽度。

### 快速查看预览

- [quickLookPreview(_:)](<view/quicklookpreview(__).md>) — 呈现单个 URL 内容的快速查看预览。
- [quickLookPreview(_:in:)](<view/quicklookpreview(__in_).md>) — 呈现你提供的 URL 的快速查看预览。

### 同播共享

- [familyActivityPicker(isPresented:selection:)](<view/familyactivitypicker(ispresented_selection_).md>) — 以表单形式呈现一个活动选择器视图。
- [familyActivityPicker(headerText:footerText:isPresented:selection:)](<view/familyactivitypicker(headertext_footertext_ispresented_selection_).md>) — 以表单形式呈现一个活动选择器视图。
- [familyActivityPicker(title:headerText:footerText:isPresented:selection:)](<view/familyactivitypicker(title_headertext_footertext_ispresented_selection_).md>) — 呈现一个活动选择器表单，用于选择要管理的 App 和网站。

### 实时活动

- [activitySystemActionForegroundColor(_:)](<view/activitysystemactionforegroundcolor(__).md>) — 系统在锁定屏幕上的实时活动旁边显示的辅助操作按钮的文本颜色。
- [activityBackgroundTint(_:)](<view/activitybackgroundtint(__).md>) — 为出现在锁定屏幕上的实时活动的背景设置色调颜色。

### 游戏保存

- [gameSaveSyncingAlert(directory:finishedLoading:)](<view/gamesavesyncingalert(directory_finishedloading_).md>) — 在游戏同步目录加载期间呈现一个模态视图。

### Apple Music

- [musicSubscriptionOffer(isPresented:options:onLoadCompletion:)](<view/musicsubscriptionoffer(ispresented_options_onloadcompletion_).md>) — 当 `isPresented` 绑定为 `true` 时，启动呈现一个包含 Apple Music 订阅优惠的表单的流程。

### 通讯录

- [contactAccessButtonCaption(_:)](<view/contactaccessbuttoncaption(__).md>)
- [contactAccessButtonStyle(_:)](<view/contactaccessbuttonstyle(__).md>)
- [contactAccessPicker(isPresented:completionHandler:)](<view/contactaccesspicker(ispresented_completionhandler_).md>) — 以模态方式呈现一个界面，允许用户选择你的 App 可以访问哪些联系人。

### StoreKit

- [appStoreOverlay(isPresented:configuration:)](<view/appstoreoverlay(ispresented_configuration_).md>) — 当给定条件为真时呈现一个 StoreKit 覆盖层。
- [appStoreMerchandising(isPresented:kind:onDismiss:)](<view/appstoremerchandising(ispresented_kind_ondismiss_).md>) — 显示一个商品推广视图。
- [manageSubscriptionsSheet(isPresented:)](<view/managesubscriptionssheet(ispresented_).md>)
- [refundRequestSheet(for:isPresented:onDismiss:)](<view/refundrequestsheet(for_ispresented_ondismiss_).md>) — 为给定的交易显示退款请求表单。
- [offerCodeRedemption(options:isPresented:onCompletion:)](<view/offercoderedemption(options_ispresented_oncompletion_).md>) — 呈现一个表单，让顾客可以兑换你在 App Store Connect 中配置的优惠代码。 _(beta)_

### PhotoKit

- [photosPicker(isPresented:selection:matching:preferredItemEncoding:)](<view/photospicker(ispresented_selection_matching_preferreditemencoding_).md>) — 呈现一个可选择 `PhotosPickerItem` 的照片选择器。
- [photosPicker(isPresented:selection:matching:preferredItemEncoding:photoLibrary:)](<view/photospicker(ispresented_selection_matching_preferreditemencoding_photolibrary_).md>) — 呈现一个照片选择器，从给定的照片图库中选择 `PhotosPickerItem`。
- [photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:)](<view/photospicker(ispresented_selection_maxselectioncount_selectionbehavior_matching_preferreditemencoding_).md>) — 呈现一个可选择一组 `PhotosPickerItem` 的照片选择器。
- [photosPicker(isPresented:selection:maxSelectionCount:selectionBehavior:matching:preferredItemEncoding:photoLibrary:)](<view/photospicker(ispresented_selection_maxselectioncount_selectionbehavior_matching_preferreditemencoding_photolibrary_).md>) — 呈现一个照片选择器，从给定的照片图库中选择一组 `PhotosPickerItem`。
- [photosPickerAccessoryVisibility(_:edges:)](<view/photospickeraccessoryvisibility(__edges_).md>) — 设置照片选择器的附件可见性。附件包括内容与边缘之间的任何内容，例如导航栏或边栏。
- [photosPickerDisabledCapabilities(_:)](<view/photospickerdisabledcapabilities(__).md>) — 停用照片选择器的某些功能。
- [photosPickerSearchText(_:)](<view/photospickersearchtext(__).md>) — 设置照片选择器的搜索文本。 _(beta)_
- [photosPickerStyle(_:)](<view/photospickerstyle(__).md>) — 设置照片选择器的模式。
- [photosSharedAlbumCreationSheet(isPresented:defaultTitle:defaultSharingPolicy:photoLibrary:onCompletion:)](<view/photossharedalbumcreationsheet(ispresented_defaulttitle_defaultsharingpolicy_photolibrary_oncompletion_).md>) — 呈现一个视图，允许用户创建新的共享相簿。 _(beta)_
- [photosSharedAlbumCustomizationSheet(isPresented:albumIdentifier:photoLibrary:onCompletion:)](<view/photossharedalbumcustomizationsheet(ispresented_albumidentifier_photolibrary_oncompletion_).md>) — 呈现一个视图，允许用户自定指定的共享相簿。 _(beta)_
- [photosSharedAlbumPostingSheet(isPresented:items:defaultAlbumIdentifier:photoLibrary:completion:)](<view/photossharedalbumpostingsheet(ispresented_items_defaultalbumidentifier_photolibrary_completion_).md>) — 呈现一个「添加到共享相簿」表单，允许用户将给定条目发布到共享相簿。 _(beta)_

### 翻译

- [translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:)](<view/translationpresentation(ispresented_text_attachmentanchor_arrowedge_replacementaction_).md>) — 当给定条件为真时呈现一个翻译弹出窗口。
- [translationTask(_:action:)](<view/translationtask(__action_).md>) — 添加一个任务，在此视图出现之前或翻译配置更改时执行。
- [translationTask(source:target:action:)](<view/translationtask(source_target_action_).md>) — 添加一个任务，在此视图出现之前或指定的源语言或目标语言更改时执行。
- [translationTask(source:target:preferredStrategy:action:)](<view/translationtask(source_target_preferredstrategy_action_).md>) — 添加一个任务，在此视图出现之前或指定的源语言或目标语言更改时执行。

### 安全性

- [certificateSheet(trust:title:message:help:)](<view/certificatesheet(trust_title_message_help_).md>) — 使用提供的证书信任显示一个证书表单。

## 另请参阅

### 提供交互性

- [输入与事件修饰符](view-input-and-events.md) — 为视图提供响应于用户输入和系统事件而执行的操作。
- [搜索修饰符](view-search.md) — 让人们能够在你的 App 中搜索内容。
- [状态修饰符](view-state.md) — 访问存储，并为子视图提供配置数据。
