---
title: 文件管理与 Quick Look 的新变化
session_id: 719
collection: wwdc2019
year: 2019
duration: '23:55'
topics: ['SwiftUI & UI Frameworks', System Services]
group: H · 持久化与文件系统
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2019/719/'
content_hash: 'sha256:88839891498a7771'
translated: true
---

# 文件管理与 Quick Look 的新变化

<sub>WWDC2019 · 23:55 · SwiftUI & UI Frameworks、System Services</sub>

你的 iOS App 现在可以通过 USB 和 SMB 访问存储在外部设备上的文件。了解创建基于文稿的 App 的最佳实践……

> [!note] 归档理由
> 文件管理与 Quick Look

## 相关资源

- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2019/719dyb631z49zpjzk/719/719_hd_whats_new_in_file_management_and_quick_look.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2019/719dyb631z49zpjzk/719/719_sd_whats_new_in_file_management_and_quick_look.mp4?dl=1)
- [Presentation Slides (PDF)](https://devstreaming-cdn.apple.com/videos/wwdc/2019/719dyb631z49zpjzk/719/719_whats_new_in_file_management_and_quick_look.pdf?dl=1)
- [Advances in Foundation](https://developer.apple.com/videos/play/wwdc2019/723)
- [What's New in Apple File Systems](https://developer.apple.com/videos/play/wwdc2019/710)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

欢迎观看"文件管理与 Quick Look 的新变化"。今天我们要与你分享大量用于管理文稿和文件预览的新 API。

这里是本场次将涵盖的领域。首先，我们将展示 App 如何使用文稿选取器访问目录及其内容。我们还将展示 App 如何正确支持存储在外部 USB 驱动器或 SMB 服务器上的文件。

然后，了解 App 如何获取并显示丰富的缩略图。

你还将看到 App 如何通过 Quick Look 提供图像、PDF 和视频的快速编辑支持。Quick Look 扩展 API 现在跨平台，我们让把 iOS App 移植到 macOS 变得容易。最后，我们将讨论支持 Mac 上的 iPad App。

那么本场次面向谁？如果你正在编写新 App 或已有呈现文稿或执行文件操作的 App，你就在正确的场次。你想学习支持存储在可移除驱动器（如 USB 和 SMB）上的文件的最佳实践。你可能还需要 App 递归访问文件夹内的多个文稿并执行批量文件操作。

如果你想了解显示文件缩略图或在 App 中提供简单图像和视频编辑，继续留步。

顺便说一句，如果你还没看过，你绝对应该看看 WWDC 2018 中的"在 iOS App 中管理文稿"场次，我们在其中逐步详细介绍了如何使用 UIDocumentBrowserViewController 和 UIDocumentPickerViewController。

还有 WWDC 2018 的"从零开始的 Quick Look 预览"场次，如果你有兴趣在 iOS 乃至 macOS 上呈现文件预览，我们强烈建议你观看。最常被请求的功能之一是访问整个目录及其内容。我们真的很高兴 iOS 13 现在可以做到。你 App 的功能可能需要读取、写入或创建文稿而访问目录内容。例如，需要对一批图像应用相同更改的图像编辑器会读取每张图像、应用修改并把新图像保存在原始图像旁边。iOS 13 之前，App 可以通过 UIDocumentPickerViewController 访问其应用容器之外的文件，但用户必须一次选一个文件。iOS 13 新增，你的 App 可以呈现 UIDocumentPickerViewController 让用户选择文件夹。验证后，你的 App 将被授予对该目录及其所有内容的递归访问。此外，你现在可以设置文档选取器呈现时显示的默认目录。

现在让我们通过几个配置 UIDocumentPickerViewController 的示例看看如何做到。要允许文件夹选择，创建仅包含 kUTTypeFolder 类型的数组初始化的实例，然后呈现它。

要设置 UIDocumentPickerViewController 实例的默认目录，设置其 directoryURL 属性然后呈现。现在看看这个例子。我们向你展示如何枚举文件夹内容，但你可以用相同示例用标准 File Manager API 在这里写入文件。

另外，确保使用 URL 的 start/stopAccessingSecurityScopedResource 调用，并为读写操作使用 NSFileCoordinator API，如示例所示。

在 iOS 13 中，用户控制哪些应用可以访问文件夹。这种访问列在"隐私"窗格的"文件和文件夹"部分，可以撤销。注意因为用户随时可以撤销访问，你需要确保代码在尝试打开文稿或枚举文件夹时优雅地处理错误。在这个例子中，你可以看到如何通过存储书签数据，然后用 URL resolvingBookmarkData 选项重新创建 URL，来跨 App 启动维持对文件夹的持久访问。

iOS 13 新增支持外部 USB 驱动器、闪存驱动器和 SMB 服务器。

支持 APFS、HFS+、FAT 和 ExFAT 格式化的驱动器。

驱动器可以插到 iPad Pro 的 USB-C 连接器上，或通过 SD 卡读卡器附件。

它们会自动列在"文件"App 的边栏，或在你的 App 中通过 UIDocumentPickerViewController 或 document browser。

用户也可以使用 Connect to Server 操作连接到 SMB 服务器，使用与 Finder 相同的键盘快捷键或边栏菜单。

任何 UIDocumentBrowserViewController API 或 UIDocumentPickerViewController API 的客户端都能免费获得相同支持，只要 App 是用 iOS 13 SDK 或更高版本构建的。然而，有几件事需要检查，以确保 App 对 USB 和 SMB 有良好支持。

有几个假设不再成立。文件访问不再局限于单个卷，因为它们现在可以存储在外部卷（如 USB 驱动器或 SMB 服务器）上。如果 USB 驱动器被拔掉或与 SMB 服务器卷的网络连接丢失，卷可能会消失。

磁盘访问可能比过去慢。你过去认为瞬间完成的操作现在可能需要几秒甚至几分钟，取决于网络条件或 USB 设备速度。另外，不要假设底层文件系统总是 APFS 或 HFS+。

这如何影响你的 App？如果你需要把文件从一个位置移动到另一个位置，使用 FileManager.moveItem(at:) API，它会为你处理跨卷移动文件。

过去，移动和克隆操作总是快速的。跨卷移动时，操作可能变成较慢的复制和删除。如果你使用 NSTemporaryDirectory 保存文件的临时版本，应该更新代码，根据写入其中文件的最终目的地选择临时文件夹的位置。

你可以用以下 File Manager 调用做到：File Manager URL for itemReplacementDirectory in userDomainMask appropriateFor URL。这总是给你写入文件的正确临时目录。过去，你的 App 可能假设文件在打开时不会消失，这不再成立，因为 USB 驱动器可能被拔掉，SMB 服务器连接可能中断。这可能导致 App 在读写文件内容时失败。你的 App 应检查错误并优雅地失败。一个建议是：如果你 App 写入文件失败，可以呈现 UIDocumentPickerViewController 让用户选择保存文件的替代位置。读写存储在 USB 驱动器或远程 SMB 服务器上的文件可能很慢，因此需要确保 App 在执行文件操作时不会挂起。始终在后台队列执行文件系统操作。

我们还建议添加 UI，如活动指示器，让用户知道有事情在发生，提供让用户取消操作的方式也是个好主意。

否则用户可能感觉应用无响应。当文稿存储在 USB 驱动器或远程 SMB 服务器上时，报告的是 LIFS 而非媒体格式化的文件系统。你的 App 很可能不必担心底层文件系统。相反，你应该检查文件系统能力以了解支持哪些文件系统操作。LIFS 是文件系统抽象，不要直接查找其存在。要了解更多 LIFS，请查看"What's New in File Systems"场次。

iOS 13 新增 UIDocumentBrowserViewController 中额外的自定义支持。现在看看这个。现在你可以通过把 shouldShowFileExtensions 属性设为 true 来始终显示文件扩展名。创建文稿按钮现在也可以自定义，通过设置 defaultDocumentAspectRatio 属性调整按钮图标的宽高比。按钮标题文本现在可以通过设置 localizedCreateDocumentActionTitle 属性更改。现在 Lyn 将讨论 Quick Look 的新变化。

在 App 中获取文件缩略图。这是为那些想通过显示丰富文件缩略图来增强应用外观的人准备的。

所以不是这样，你可以是这样。

Quick Look thumbnailing 是一个新的跨平台框架，用于检索文件 URL 的缩略图图像。这是 iOS 上的新功能，取代 macOS 上的 QLThumbnail C API。它还取代了 NSURLThumbnailDictionaryKey。

iOS 和 macOS 为几种文件类型（如图像、PDF、文本文件、视频等）提供内置支持。你还可以通过缩略图扩展为自己的文件类型提供支持。

Quick Look thumbnailing 是非 UI 框架。默认不导入 UIKit 或 AppKit。我们可以在不导入两者的情况下获取缩略图的 CGImage，但你也可以通过显式链接 UIKit 或 AppKit 分别在 iOS 上获得 UIImage 或在 macOS 上获得 NSImage。

它是异步的，因此检索缩略图时不会阻塞，如果决定最终不需要那个缩略图，还支持取消。

让我们从大局概述开始。要获取缩略图，你先创建 QLThumbnailGenerator.Request，然后把它传给 QLThumbnailGenerator，指定你是否希望每次有新的缩略图表示可用时收到通知，还是只在你请求的最佳表示完成时收到通知。你可以请求缩略图的不同表示，它们会有不同的质量与性能成本。

图标是与该文件类型关联的通用图像。同一类型的文件都相同。低质量缩略图是更快的缩略图，可能不完全是你指定的大小。这通常来自缩略图的缓存版本或可能嵌入文件本身的缩略图。

最后的表示类型 thumbnail 是完全质量的缩略图，精确匹配请求。生成它耗时最长。

为方便起见，你也可以指定 all 以获取任何可用类型的缩略图。创建 QLThumbnail generation request 时，你指定想要的大小、缩放和表示类型。你可能只关心全质量缩略图，或接受图标或低质量版本。最好指定所有对你有效的表示类型，因为并非所有三种类型都可用于给定缩略图。

你将得到 QLThumbnailRepresentation，它指定缩略图类型（图标、低质量或缩略图）和图像，可以作为 CGImage 访问，或如果你在 iOS 链接了 UIKit、在 macOS 链接了 AppKit，分别获得 UIImage 或 NSImage。要获取该 QLThumbnailRepresentation，把缩略图请求传给 QLThumbnailGenerator。如果你只想要最佳质量的可用缩略图，使用 generateBestRepresentation。它会用能创建的缩略图请求最佳版本调用你的完成处理程序。或者你可能更喜欢提供 updateHandler 的 generateRepresentations 来获取增量更新，每次表示可用时被调用。你可以用这个，例如，快速更新 UI，然后随着更好缩略图到达而改善显示质量。关于缩略图检索就说这么多。谈谈用 Quick Look 编辑图像、PDF 和视频。

Quick Look 提供在 iOS 上预览各种类型文件文稿的 API。它还允许你通过扩展为自己的文稿提供自定义预览。

现在在 iOS 13 中，我们还添加了用 QLPreviewController 快速编辑图像、PDF 和视频的支持。QLPreviewController 是你用来预览文件的。使用它只需分配 QLPreviewController 实例，并在呈现前设置数据源和委托。要了解更多 Quick Look 和 QLPreviewController，请查看我们 2018 年的 WWDC 场次"从零开始的 Quick Look 预览"。iOS 13 新增，QLPreviewController 还提供访问 Markup——预览文稿时或在 Mail 中编辑附件时可用的编辑工具。这适用于图像和 PDF。QLPreviewController 还支持修剪和旋转视频。要使用这些功能，你只需启用编辑模式。只需实现可选的委托方法 editingModeForPreviewItem。默认编辑被禁用，但可以按项目启用。这个委托方法允许你指定是否需要编辑能力以及如何处理生成的文件。你可以让 QLPreviewController 用用户编辑后的版本覆盖原始文件。为此，从 editingModeForPreviewItem 返回 updateContents。

如果你需要在编辑成功保存时做出反应，也可以实现可选的 didUpdateContentsOfPreviewItem 方法。或者你可能更喜欢用 QLPreviewController 为被预览的文件创建编辑后的副本并自己管理。为此从 editingModeForPreviewItem 返回 createCopy 并实现委托方法 savedEditedCopyOfPreviewItemAtModifiedContentsURL。

macOS 上的 Quick Look 扩展 API。

我们刚谈了获取和使用文件的缩略图与预览。现在谈谈如何为自己的文件类型提供缩略图和预览。在 iOS 上，App 已经可以实现 Quick Look 缩略图和预览扩展，为自己的文稿提供系统级缩略图和预览支持。现在相同的 Quick Look 扩展 API 在 macOS 上可用。

缩略图在 macOS 和 iOS 中被广泛使用，让用户快速识别文件。例如，你可以看到截图中 macOS 如何在 Finder 中使用它们。macOS 可以为许多常见文件类型生成缩略图，但实现缩略图扩展允许你也为自己的文件类型提供缩略图，以便它们在 Finder 和可能显示缩略图的其他地方有丰富表示。扩展 API 取代了基于 CF 插件的旧生成器系统。如果你有 Quick Look 生成器，考虑尽快迁移。我这里泛指 Quick Look 扩展，因为缩略图扩展点来自 Quick Look thumbnailing。这之前在 iOS 上由 Quick Look 框架提供，但如果你不需要 UIKit，可以考虑从 Quick Look thumbnailing 导入，这会让你的扩展更轻量。

要创建缩略图扩展，在 Xcode 项目中用缩略图扩展模板添加新 target。

设置扩展 target 后，你就可以开始实现 QLThumbnailProvider 子类。你可以用 CG context、AppKit context 绘制缩略图，或提供指向图像的文件 URL。

这里是快速示例，我们覆盖 provideThumbnailForRequest 处理程序方法。我们在 WWDC 2017 "在 iOS 11 中构建出色的基于文稿的 App"场次中广泛涵盖了 Quick Look API 的这一部分。我们强烈建议你查看。简而言之，你将得到 QLFileThumbnailRequest，包含文件的 URL、缩略图的最大和最小尺寸及其缩放。用这些创建匹配这些规格的缩略图。

对于每个缩略图请求，API 期望你创建 QLThumbnailReply，用于生成缩略图。把 QLThumbnailReply 传给上面的完成处理程序。

要在 macOS 上调试缩略图扩展，你可以使用 QLManage。如果你过去写过 Quick Look 生成器，你可能认识这个工具。在 Xcode 中构建并运行扩展 target 以向系统注册你的扩展。然后用 QLManage 生成你的文件类型的缩略图，并在 Xcode 中附加到扩展。

文件的预览扩展。今年新功能，macOS 上的 Quick Look 也允许你通过实现预览扩展为自己的文件类型提供预览。

Quick Look 预览扩展已经存在以支持 Core Spotlight 预览。见 WWDC 2017 "iOS 与 macOS Core Spotlight 的新变化"。今年我们还添加了文件预览支持。通过扩展，你现在可以直接提供视图来显示你的预览。这与旧 Quick Look 生成器不同，后者提供数据或 URL 供系统呈现。新的扩展 API 让你对预览外观有更大控制。我们建议你迁移离旧 Quick Look 生成器，它们将在未来版本中被废弃。

要创建预览扩展，在项目中添加新 target 并选择预览扩展模板。

API 与 iOS 预览扩展相同。见 WWDC 2018 "从零开始的 Quick Look 预览"。作为快速总结，你希望在 Info.plist 的 QLSupportedContentTypes 中声明支持的 UTI 列表。

这必须精确匹配你要预览的文件 UTI。不支持按父 UTI 匹配。模板会提供一个视图控制器，你将在其中准备预览。这里是视图控制器模板的快速示例。实现 preparePreviewOfFile(at:) 来准备你的视图控制器。一旦就绪，调用完成处理程序。呈现你预览的 QLPreviewView 会显示旋转轮，直到调用这个完成处理程序。因此尽快准备好预览。

请记住，你的预览可能显示在任何 QLPreviewView 中，可能是预览面板、栏视图边栏、聚焦或任何 QLPreviewView 的客户端。

要调试，用 Xcode 启动扩展 target。注意 Xcode 默认会启动 Quick Look 模拟器。这是为了辅助调试 Core Spotlight 预览，扩展也可以提供支持。要调试常规文件预览，可以忽略模拟器并用 Finder 或 QLManage 调用预览。只要你的预览扩展通过 Xcode 启动，Xcode 会自动附加到它。

谈谈支持 Mac 上的 iPad App。我们的文稿处理 API 在 Mac 上的 iPad App 中支持，因此你可以把基于文稿的 iOS App 带到 macOS。

对于 UIDocumentPickerViewController，像在 iOS 上一样使用它，用户会自动获得感觉像 macOS 原生的体验。具体来说，.import 和 .open 模式显示 NSOpenPanel，.exportToService 和 .moveToService 模式显示 NSSavePanel。

类似地，对于 UIDocumentBrowserViewController，用户会获得感觉像 macOS 上基于文稿的 App 的体验。用户会像 TextEdit 一样在单独窗口中获得 NSOpenPanel。由于 iOS 和 macOS 接口之间的差异，存在一些细微的运行时差异。一个很好的例子是 UIDocumentBrowserViewController 的导航栏，在 macOS 上不存在。查看文档了解这些特定情况该怎么做。在某些情况下，你可以使用新 API（如菜单栏 API）来帮助处理这些 UI 差异。

Quick Look 也在 Mac 上的 iPad App 中可用。呈现 QLPreviewController 会在 macOS 上启动 QLPreviewPanel，提供更原生的 Mac 体验。因为 QLPreviewPanel 是单独窗口，你呈现的视图控制器内容会可见，但会被灰化且不可交互。

测试你的 iPad App 在 Mac 上，确保它看起来很棒。

QLPreviewController 在 Mac 上的 iPad App 中的一个限制是嵌入 QLPreviewController 的视图不完全支持，在这种情况下我们会提供缩略图而非实时预览。

今天我们学到了什么？首先，我们向你展示了如何利用 iOS 13 的新功能，如访问目录中的多个文件、支持 USB 驱动器和 SMB 服务器。然后我们看了如何用 Quick Look 显示与"文件"App 相同的丰富缩略图，为图像和视频提供 Quick Look 编辑支持，以及用现代扩展 API 在 Mac 上提供预览和缩略图。感谢观看。
