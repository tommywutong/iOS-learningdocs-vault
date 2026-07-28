---
title: 进行高级优化以进一步减小 App 大小
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/doing-advanced-optimization-to-further-reduce-your-app-s-size
source_url: 'https://developer.apple.com/documentation/xcode/doing-advanced-optimization-to-further-reduce-your-app-s-size'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/doing-advanced-optimization-to-further-reduce-your-app-s-size.json'
content_hash: 'sha256:6f06540908c45429'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [性能与指标](performance-and-metrics.md) · [减小 App 大小](reducing-your-app-s-size.md)

# 进行高级优化以进一步减小 App 大小

<sub>文章</sub>

优化 App 的资源文件、采用按需资源，并减小 App 更新的大小。

## 概述

按照[进行基本优化以减小 App 大小](doing-basic-optimization-to-reduce-your-app-s-size.md)中所述方法进行基本优化，是减小 App 大小的好办法。不过，你还可以进一步优化 App 大小，尽量减少其在设备上的占用空间，并提供快速的下载、安装和更新体验。

![](../../../attachments/3014f056faa37bb8b9c66b5487e8fd1a/doing-advanced-optimization-to-further-reduce-your-app-s-size-1@2x.png)

<sub>展示如何进一步优化 App 大小的流程图。测量 App 大小并进行基本优化。然后再次测量并进行高级优化，包括优化资源文件、减小 App 更新大小、采用按需资源，以及对企业 App 使用 App 瘦身。</sub>

### 优化 App 的资源文件

资源通常占 App 的很大一部分。请考虑以下优化：

**使用尽可能高效的图像和视频格式。** 图像和视频资源通常是 App 体积过大的重要原因。使用效率更高的图像文件格式是减小 App 大小的好办法。例如，考虑对图像使用 HEIF 格式，对视频使用 HEVC 格式。如果使用 PNG 文件，请考虑使用 8 位而不是 32 位 PNG。这样可以将图像大小减至原来的四分之一。

**压缩图像。** 对于 32 位图像，使用 [Adobe Photoshop](https://www.adobe.com/photoshop) 的“Save for Web”功能可以显著减小 JPEG 和 PNG 图像的大小。

**压缩音频文件。** 一般而言，使用 `AAC` 或 `MP3` 编解码器压缩音频，并尝试降低比特率。很多时候并不需要 44.1 kHz 的采样率，较低比特率的片段也不会造成可察觉的质量下降。观看[游戏音频开发](https://developer.apple.com/videos/wwdc/2011/?id=404)，进一步了解如何优化音频资源。

### 减小 App 更新的大小

App 有可用更新时，App Store 不会总是下载整个 App，而是创建一个_更新包_。它会将 App 的一个或多个旧版本与新版本进行比较，并创建经过优化的包。该包仅包含 App 各版本之间发生变化的内容，不包含未变化的内容。

这种比较会检查 _App 捆绑包_中的所有内容，包括 App 可执行文件、storyboard、nib、本地化以及图像等其他资源。

请考虑以下做法来减小 App 更新包的大小：

- 不要对文件进行不必要的修改。使用 `diff` 或其他目录比较工具比较 App 旧版本和新版本的内容，并确认其中不包含任何意外更改。
- 将预计会在更新中发生变化的内容，与预计不会变化的内容分别存储在不同文件中。

> [!note] 注意
> 不要依赖 App 捆绑包中文件的创建日期和修改日期。操作系统使用更新包更新 App，并且仅在文件内容发生变化时更新文件。它不会因为元数据（例如创建日期和修改日期）的变化而更新文件。

### 采用按需资源

分析 App 的所有资源，并确定哪些资源很少使用。将不常用的资源分组为_资源包_。将 App 上传到 App Store Connect 时，资源包不会成为 App 初始下载或 App 更新的一部分。App 可以根据需要单独下载这些资源包。有关更多信息，请参阅[按需资源指南](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/On_Demand_Resources_Guide/index.html#//apple_ref/doc/uid/TP40015083)。

如果无法采用按需资源，请考虑实现一个提供这些资源的 Web 服务，并根据需要使用 [URLSession](../foundation/urlsession.md) 在后台下载。若要进一步了解，请参阅[在后台下载文件](../foundation/downloading-files-in-the-background.md)。

### 利用 App 瘦身

_App 瘦身_是一项确保 App 的 IPA 文件仅包含其在特定设备上运行所需资源和代码的技术。在 App Store 中提供的 App，以及使用 TestFlight 分发给测试员的 App，已经利用了 App 瘦身。但是，如果你分发企业内部 App，或不使用 TestFlight 向测试员分发构建版本，则必须在导出 App 时启用 App 瘦身。要使用 App 瘦身：

1. 在 Xcode 中归档 App。
2. 在 Organizer 窗口中选择已归档的 App，然后点按 Distribute App。
3. 使用 Xcode 导出 App，并在导出表单中为 App 瘦身选择“All compatible device variants”。如果 App 仅支持有限数量的设备，请选择相应设备。

若要进一步了解 App 瘦身，请参阅[分发选项](https://help.apple.com/xcode/mac/11.0/index.html?localePath=en.lproj#/devde46df08a)，并观看 [Xcode 中的 App 瘦身](https://developer.apple.com/videos/play/wwdc2015/404/)。

## 另请参阅

### 大小优化

- [进行基本优化以减小 App 大小](doing-basic-optimization-to-reduce-your-app-s-size.md) — 调整项目构建设置，并在 App 开发生命周期早期采用资源目录等技术。
