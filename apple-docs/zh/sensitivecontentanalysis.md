---
title: Sensitive Content Analysis
framework: Sensitive Content Analysis
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/sensitivecontentanalysis
source_url: 'https://developer.apple.com/documentation/sensitivecontentanalysis'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/sensitivecontentanalysis.json'
content_hash: 'sha256:eba53b21cacbc5f2'
translated: true
---

> 导航：[Technologies](technologies.md)

# Sensitive Content Analysis

<sub>框架</sub>

通过在显示图像和视频之前检测其中的敏感内容并提醒用户，在你的 App 中提供更安全的体验。

## 概述

Sensitive Content Analysis 框架使 App 能够检查内容中是否含有裸露画面及其他敏感素材。在 iOS 和 macOS 中，「敏感内容警告」用户偏好设置或屏幕使用时间中的「通信安全」家长控制功能，可让用户选择防范意外或不希望看到的敏感内容图像。通过使用 Sensitive Content Analysis 在显示内容之前检查其是否敏感，为用户在这些设置中提供他们所期望的体验。

请考虑你的 App 会获取来自外部来源的图像或视频的场景，并使用此框架来检查媒体是否敏感。例如，一个消息类 App 可以检查它从联系人处收到的每一张图像。一个课堂类 App 可以对上传到共享位置的个人设备内容（用于课堂作业提交或其他课堂活动）进行评估。而一个视频会议 App 则可以实时分析通话中所有参与者的视频流。

![](../../attachments/4cbaecea0bbe206c2ac1f4afb2406bdb/sensitivecontentanalysis-1@2x.png)

<sub>一张从左到右推进的流程图。该图表分为三个区域。左侧区域包含标签「第三方 App」，其文字表明该 App 通过网络接收一张图像。有一个箭头从该区域向右流向一个位于中央的方框，其标签为「敏感度分析器」。流程图的整个中央区域标记为「Sensitive Content Analysis」。有一个箭头从「敏感度分析器」方框流向中央区域内另外两个分别标有「是」和「否」的方框。箭头本身的文字写着「是否敏感」，代表图表流程分支所依据的条件。有一个箭头从「是」方框向右流向图表的右侧部分，该部分包含两个方框。上方的方框内文字写道：该 App 会避免显示敏感内容。第二个箭头从「否」方框向右流向另一个方框，其内容写道：该 App 会显示不敏感的内容。</sub>

### 在内容敏感时进行干预

如果框架判定某些媒体内容含有敏感内容，请提醒用户注意此问题，并在用户决定如何处理之前避免显示该媒体。例如，下图描绘了在 iOS 17 中的信息 App 收到一张可能露骨的图像时的情形。用户界面会将图像模糊处理，并且：

- 如果用户选择查看，则显示被标记的内容。
- 提供一个附加操作菜单，例如屏蔽该联系人。

![](../../attachments/8f61ec0f4dde803c8f7a0e9c6e87bcbd/sensitivecontentanalysis-2@2x.png)

<sub>两台并排放置的 iPhone 图像，均显示信息 App。左侧的手机呈现了用户在对话中收到的一张图像的视图。一个标注指向该图像，内容为「模糊视图」。指代该模糊图像的文字写道：这可能是敏感内容。该视图包含一个文字为「显示」的按钮，以及一个标注，内容为：显示内容的界面。右侧的手机在信息中显示同一对话，视图中呈现的是一张清晰的图像。一个标注从这张清晰的图像延伸出来，内容为：已显示的内容。该视图包含一个带有警告三角形的按钮，从中延伸出一个标注，内容为：备选／附加选项。</sub>

## 主题

### 设置

- [Detecting sensitive content in media and providing intervention options](sensitivecontentanalysis/detecting-nudity-in-media-and-providing-intervention-options.md) — 在显示可能敏感的图像或视频之前提醒用户。

### 授权

- [com.apple.developer.sensitivecontentanalysis.client](bundleresources/entitlements/com.apple.developer.sensitivecontentanalysis.client.md) — 一种代码签名 entitlement，使 App 能够检测图像和视频中的裸露画面。

### 图像和视频文件分析

- [SCSensitivityAnalyzer](sensitivecontentanalysis/scsensitivityanalyzer.md) — 一个用于分析媒体中敏感内容的对象。
- [SCSensitivityAnalysisPolicy](sensitivecontentanalysis/scsensitivityanalysispolicy.md) — 表示框架检查敏感内容的方式以及 App 响应方式的配置。

### 视频流分析

- [SCVideoStreamAnalyzer](sensitivecontentanalysis/scvideostreamanalyzer.md) — 一个通过分析帧来监控视频流中敏感内容的对象。

### 分析结果

- [SCSensitivityAnalysis](sensitivecontentanalysis/scsensitivityanalysis.md) — 一个用于指示是否存在敏感内容并提供干预指导的对象。

### 测试

- [Testing your app’s response to sensitive media](sensitivecontentanalysis/testing-your-app-s-response-to-sensitive-media.md) — 使用 Apple 提供的用于测试的特殊二维码和描述文件，来触发你的 App 的干预流程。
