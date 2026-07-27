---
title: 减小你的 App 大小
framework: xcode
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/reducing-your-app-s-size
source_url: 'https://developer.apple.com/documentation/xcode/reducing-your-app-s-size'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/reducing-your-app-s-size.json'
content_hash: 'sha256:2e4cea534a175974'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Performance and metrics](performance-and-metrics.md)

# 减小你的 App 大小

测量你的 App 大小，优化其素材和设置，并采用有助于在移动互联网连接下简化安装过程的技术。

## 概述

即使你的用户所在地区有良好的移动网络覆盖，他们的下载速度也可能有所不同，或者他们的数据流量套餐可能会限制可用高速数据的用量。为了确保 App 下载不会耗时过长或给用户带来额外费用，App Store 会限制用户可以通过移动连接安装的 App 大小。如果一个 App 的大小超出限制，用户就需要连接到 Wi-Fi 网络才能安装它。让你的 App 大小远低于该限制，可以最大化你 App 可能触及的安装用户群，并将安装时间降到最低。

除了这些问题之外，设备可用的存储空间也可能有限，这使得关注你 App 的大小变得更加重要。可以考虑将测量大小作为开发和测试流程的一部分，并在开发过程中计划对其进行优化。

在开始优化你的 App 之前，你首先需要测量它的下载和安装大小。然而，你在 Xcode 内为调试而创建的、或上传到 App Store 的任何二进制文件，都不适合用来测量你 App 的大小。例如，你不能使用以下任何一种二进制文件：

- APP 文件（App 包）
- 归档你的 App 时创建的 XCARCHIVE 包
- 上传到 App Store Connect 的 IPA 文件

这些二进制文件包含的资源和文件，并不是用户从 App Store 下载的那些包的一部分；例如用于崩溃报告的 DSYM 文件。

在开发过程中，获取你 App 准确下载和安装大小的唯一方法，是在你的 Mac 上创建一份 App 大小报告。不过，如果你的 App 可通过 App Store 或 TestFlight App 获取，那么 App Store Connect 会提供最准确的大小信息。它会显示你 App 每个变体的大小，并在超出通过移动互联网连接下载的限制时向你发出警告。

通过 TestFlight 分发用于测试的 App 包含了 App Store 构建版本所没有的额外数据，因此 TestFlight 构建版本会更大。当你在 App Store 上架你的 App 时，这些额外数据不会包含在其中。不过，与你上传的二进制文件相比，你 App 在通过 App Store 审核后的最终大小可能会略大一些。这种大小增加，可能是因为 App Store 会对你 App 的二进制文件执行额外处理，添加 DRM 以防止 App 盗版，然后再重新压缩这些二进制文件。

下图展示了测量你 App 大小并执行优化的常见工作流程。

![概述测量 App 大小以及何时执行优化这一过程的流程图。](../../../attachments/38f7a1fa14b3caf60822d8a97a802dc0/reducing-your-app-s-size-1@2x.png)

要了解更多有关在 App Store Connect 中查看构建版本文件大小的信息，请参阅[查看构建版本和元数据](https://developer.apple.com/help/app-store-connect/manage-builds/view-builds-and-metadata)。

接下来的两个小节将介绍如何使用 Xcode 生成大小报告，以及如何自动创建该报告。

### 创建 App 大小报告

虽然 App Store Connect 提供了对你 App 大小最准确的测量结果，但 Xcode 内置的报告工具也可以为你创建一份 App 大小报告。它能提供你 App 下载和安装大小的近似估算值。要创建 App 大小报告：

1. 在 Xcode 中归档你的 App。
2. 将归档后的 App 导出为 Ad Hoc、Development 或 Enterprise 构建版本。
3. 在设置开发分发选项的表单中，为 App 精简选择「All compatible device variants」。
4. 对你的 App 签名，并将其导出到你的 Mac。

此过程会创建一个包含你 App 制品的文件夹：

- 一个面向旧设备的_通用_ IPA 文件。这个单一的 IPA 文件包含了你 App 所有变体的素材和二进制文件。
- 面向你 App 每个变体的_精简版_ IPA 文件。这些文件只包含单个变体的素材和二进制文件。

导出后 App 所在的输出文件夹中还包含 App 大小报告：一个名为 `App Thinning Size Report.txt` 的文件。此报告列出了你 App 每个 IPA 文件的压缩和未压缩大小。未压缩大小相当于设备上已安装 App 的大小，压缩大小则是你 App 的下载大小。下面展示了一个示例 App 的大小报告开头部分：

```other
App Thinning Size Report for All Variants of ExampleApp

Variant: ExampleApp.ipa
Supported variant descriptors: [device: iPhone11,4, os-version: 12.0], [device: iPhone9,4, os-version: 12.0], [device: iPhone10,3, os-version: 12.0], [device: iPhone11,6, os-version: 12.0], [device: iPhone10,6, os-version: 12.0], [device: iPhone9,2, os-version: 12.0], [device: iPhone10,5, os-version: 12.0], [device: iPhone11,2, os-version: 12.0], and [device: iPhone10,2, os-version: 12.0]
App + On Demand Resources size: 6.7 MB compressed, 18.6 MB uncompressed
App size: 6.7 MB compressed, 18.6 MB uncompressed
On Demand Resources size: Zero KB compressed, Zero KB uncompressed

// Other Variants of Your App.
```

有了你生成的 App 大小报告，你现在就可以执行一些基本优化了，比如检查你的二进制文件中是否有未使用的素材，以减小你 App 的大小。更多信息，请参阅[执行基本优化以减小你的 App 大小](doing-basic-optimization-to-reduce-your-app-s-size.md)。

### 自动生成 App 大小报告

除了使用 Xcode 创建 App 大小报告之外，你可能还想在构建脚本或持续集成工作流程中自动生成该报告。运行以下命令，使用 `xcodebuild` 导出你的 App 用于分发，并创建一份 App 精简大小报告：

```other
xcodebuild -exportArchive -archivePath iOSApp.xcarchive -exportPath Release/MyApp -exportOptionsPlist OptionsPlist.plist
```

根据需要替换所有文件名和路径。要创建 App 大小报告，需要为 `xcodebuild` 提供一份导出选项属性列表。请确保包含 `thinning` 键，并将其值设为 `<thin-for-all-variants>`。

> [!important] 重要
> 请确保对导出选项属性列表中该值里的尖括号进行转义。

要了解更多有关使用 `xcodebuild` 的信息，请参阅[通过命令行使用 Xcode 构建常见问题解答](https://developer.apple.com/library/archive/technotes/tn2339/_index.html#//apple_ref/doc/uid/DTS40014588)。

## 主题

### 大小优化

- [执行基本优化以减小你的 App 大小](doing-basic-optimization-to-reduce-your-app-s-size.md) — 调整你项目的构建设置，并在 App 开发生命周期的早期阶段使用素材目录之类的技术。
- [执行高级优化以进一步减小你的 App 大小](doing-advanced-optimization-to-further-reduce-your-app-s-size.md) — 优化你 App 的素材文件，采用按需资源，并减小 App 更新的大小。

## 另请参阅

### 内存与大小

- [减少你的 App 内存使用量](reducing-your-app-s-memory-use.md) — 通过分析内存使用指标并进行修改以最大化内存效率，提升你 App 的性能。
