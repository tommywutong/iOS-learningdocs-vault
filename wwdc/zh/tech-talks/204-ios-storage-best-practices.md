---
title: iOS 存储最佳实践
session_id: 204
collection: tech-talks
year: null
duration: '8:53'
topics: [System Services]
group: H · 持久化与文件系统
evergreen: true
source_url: 'https://developer.apple.com/videos/play/tech-talks/204/'
content_hash: 'sha256:adb479220eab9c4a'
translated: true
---

# iOS 存储最佳实践

<sub>技术演讲 · 8:53 · 系统服务</sub>

学习让你的 App 在磁盘上的存储尽可能井井有条、尽可能优化的技巧。了解如何启用对文稿的直接访问……

> [!note] 归档理由
> iOS 存储行为与清理机制

## 相关资源

- [文件系统编程指南](https://developer.apple.com/library/content/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010672)
- [让 App 备份更高效](https://developer.apple.com/library/content/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/PerformanceTips/PerformanceTips.html#//apple_ref/doc/uid/TP40007072-CH7-SW16)
- [防止文件被备份](https://developer.apple.com/library/content/qa/qa1719/_index.html)
- [iOS 数据存储指南](https://developer.apple.com/icloud/documentation/data-storage/index.html)
- [高清视频](https://devstreaming-cdn.apple.com/videos/tutorials/20170912/204a83a4lxlz1/ios_storage_best_practices/ios_storage_best_practices_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/tutorials/20170912/204a83a4lxlz1/ios_storage_best_practices/ios_storage_best_practices_sd.mp4?dl=1)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

作为一名 App 开发者，确切了解你的 App 在磁盘上存储了什么、所有东西存储在哪里、以及为什么需要它们，这一点至关重要。掌握这些细节的最佳方式，是对你的 App 实际存储的内容做一次盘点。

首先，在设备上构建并运行你的 App，然后使用所有会在磁盘上存储内容的功能。完成之后，就该看看实际存储了什么、存储在哪里了。使用 Xcode 中的“设备与模拟器”窗口提取你 App 的容器，以便我们查看其中的内容。在左侧栏中选择你的设备，然后在已安装 App 列表中选择你的 App。

使用齿轮图标，选择 Download Container（下载容器），并把它保存到你的 Mac 上。

在访达中，按住 Control 键点按下载得到的 xcappdata 文件。选择“显示包内容”，进入 App Data 文件夹，开始进行盘点。逐个查看各个目录，了解每个目录里存储了什么。

对于每个文件，确保你能说清它是什么、为什么要存储它。如果你不确定某个东西为什么在那里，也许就可以把它删掉。你要确认自己把正确的文件放在了合适的目录中，同时考虑该文件是否应该包含在 iTunes 和 iCloud 备份中。前两个问题只有你自己能回答，因为它们与你 App 的功能相关。我会重点讲后两个问题，先从文件应该存储在哪里说起。iCloud Drive 是存放文稿的最佳位置，因为文稿会在用户的所有设备上可用。由于你 App 在 iCloud Drive 上的文件夹内容是可见的，重要的是只把人们能够识别并会直接访问的文稿放在那里。你的 App 在本地读写内容，然后操作系统会在网络可用时自动上传这些文件。由于可能有多个设备同时访问 iCloud Drive 中的文件，你确实需要使用文件协调来避免冲突。所以请务必阅读文档了解细节。对于本地存储的文件，你 App 的容器中提供了 Documents 目录。与 iCloud Drive 一样，你应该只在这里存储用户可见的文稿。一旦你确认 Documents 目录中只包含应该公开的文件，“文件” App 就可以在“我的 iPhone”或“我的 iPad”位置显示它们。为此，你的 App 应支持“原地打开”并声明已启用文件共享，这两者都在你的 Info.plist 文件中配置。除了能在“文件” App 中看到他们的文件，人们还可以在聚焦中找到文件，在 iPad 上还可以把它们拖放到其他 App。

公开 Documents 目录的另一个好处是，人们会在“储存空间”设置界面中看到他们的文件，并可以单独移除某些条目。这让磁盘空间的管理容易得多，也能降低空间不足时你的整个 App 被删除的可能性。但请记住，放进 Documents 目录的只应该是对使用你 App 的人有意义的内容。你应该问的关键问题是：“我的用户应该能看到这个文件吗？”如果答案是肯定的，那没问题。如果答案是否定的，就把它移出 Documents 目录，放到下面这些位置之一。Application Support 目录适合存储那些可能会出现在你的 Documents 目录里、但不应该被用户看到的文件。例如，你的 App 需要但用户绝不会手动打开的数据库。

你可以把文件存放在顶层，也可以创建目录来帮助整理。这个目录完全由你控制，而且是持久化的。其中的内容默认包含在备份中，但如果某些文件不需要备份，你可以选择让它们退出备份。最后，Application Support 目录占用的磁盘空间会在“储存空间”设置界面中计入你 App 的“文稿与数据”总量。你的 App 可用的下一个位置是 Caches 目录。你可以把空间不足时可以丢弃的文件存放在这里。对于任何需要时可重新下载的内容，这是一个很好的位置。Caches 目录的内容不包含在备份中。当设备磁盘空间不足时，iOS 可以通过清理缓存来帮忙。只要你的 App 正在运行，系统就绝不会从你的缓存目录中移除文件，而且操作系统会先清理那些一段时间未使用的 App 的缓存。对你来说还有一个好处：缓存目录中的文件不会被计入你 App 的“文稿与数据”总量，尽管它们包含在 App 占用的总空间之中。

最后，你可以把那些较长时间内不需要的文件放进 Temporary 目录。尽管操作系统会在你的 App 未运行时定期移除这些文件，最好还是在你用完它们之后就删掉。

与 Caches 目录一样，Temporary 目录不会被备份，也不会计入你 App 的“文稿与数据”总量。

这些就是你 App 可以存储文件的所有常见位置。iCloud Drive 和 Documents 目录用于应该能在“文件” App 中访问的文件，而 Application Support、缓存和临时目录都是供你的 App 私下使用的。务必检查你的存储位置，并使用正确的目录。最后是几个最佳实践提示。如果你有不需要包含在 iTunes 或 iCloud 备份中的文件，使用 NSFileManager API 设置 “IsExcludedFromBackupKey”。你还要能从容应对从旧版本 App 恢复出来的文件。例如，如果你曾有一个 32 位版本的 App 并且它的文件被备份过，那么对于 64 位版本的 App，这些旧文件可能会被恢复，你需要能够处理这种情况。最好在你的文件上使用版本管理方案，以便在 App 的多个版本之间提供稳健的兼容性。另外，确保只把文件存储在一个位置。例如，如果你把文件放进了本地 Documents 目录，就不要在 iCloud Drive 中再复制一份。选定一个地方并坚持使用。对于用户文稿，我建议优先选择云端存储位置，除非你有特定理由只把文件存储在设备本地。

最后，iOS 11 提供了一些新的卷容量信息，帮助你判断现在是否是让你的 App 占用更多磁盘空间的好时机。

第一个键 Available Capacity For Important Usage（重要用途可用容量），表示可以为用户在你的 App 界面中明确请求的内容腾出的空间大小。例如，用户选择下载一个视频或游戏中的一个新关卡。如果你需要的空间大于可用空间，你应该告诉他们无法满足其请求。第二个键 Available Capacity For Opportunistic Usage（机会性用途可用容量），表示可用于用户可能想要但尚未明确请求的内容的空间大小。这可能是他们正在观看的系列视频的下一集，或者服务器上最近更新、他们可能会打开的文稿。对于这类文件，你可以先把它们存储在 Caches 目录中，等它们真正被使用时，再把它们移到 Application Support 或 Documents 目录。

在完成盘点并确认了你 App 存储的内容之后，如果发现有些东西放错了位置，就更新你的代码，把它放到合适的目录。并且别忘了添加必要的迁移代码，把文件从一个地方移动到另一个地方。如果不这样做，你可能会在无意中留下被遗弃的文件。通过清理你在磁盘上的存储，你可以把 Documents 目录开放给“文件” App 中的人们，让他们用你的 App 更加高效。更多信息请访问 developer.apple.com 或我们的开发者论坛。感谢观看！
