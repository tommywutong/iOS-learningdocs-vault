---
title: 在 App 中支持多种语言
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/supporting-multiple-languages-in-your-app
source_url: 'https://developer.apple.com/documentation/xcode/supporting-multiple-languages-in-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/supporting-multiple-languages-in-your-app.json'
content_hash: 'sha256:22cbbb0bacc7b185'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [本地化](localization.md)

# 在 App 中支持多种语言

<sub>文章</sub>

对 App 的字符串、图像及其他资源类型进行国际化，为本地化做好准备。

## 概述

多语言 App 是可以在多种语言和地区环境中运行的 App。让 App 支持多种语言可以拓展受众，并为客户提供更好的整体体验。当文本和资源能够适应设备上的语言与地区设置时，人们会更自在地使用 App。

![包含多种语言“你好”字样的横幅。](../../../attachments/f20b079e42434eb7c69037ff6c920b61/supporting-multiple-languages-in-your-app-hero@2x.png)

要让 App 支持多种语言，首先要对其进行_国际化_，准备好代码和资源，以便翻译成不同语言并适应不同地区。例如，某些地区的日期采用日-月-年格式，而另一些地区则采用月-日-年格式。

完成 App 国际化后，再通过翻译字符串并针对多种语言和地区提供不同资源，对 App 进行_本地化_。有关更多信息，请参阅[使用字符串目录本地化文本并提供变体](localizing-and-varying-text-with-a-string-catalog.md)。

## 对代码进行国际化

编写代码，使 App 自动适应设备的语言和地区设置。请使用专门的可本地化 API，以及以下支持国际化的 Xcode 工具：

- **面向用户的文本**。使用本地化版本的字符串格式化器，为 App 文本的本地化做好准备。有关面向用户文本的更多信息，请参阅[准备 App 文本以供翻译](preparing-your-apps-text-for-translation.md)。
- **日期、货币和数字**。不同地区采用不同的日期、货币和数字格式。有关更多信息，请参阅[准备日期、货币和数字以供翻译](preparing-dates-numbers-with-formatters.md)。
- **语法一致性**。使用 Foundation 中的自动语法一致性 API（例如 [TermOfAddress](../foundation/termofaddress.md)），在本地化文本中正确表示语法性别。有关语法一致性的更多信息，请参阅[释放语法一致性的力量](https://developer.apple.com/videos/play/wwdc2023/10153/)。
- **文本方向**。使用 SwiftUI 和 Xcode 中的布局工具控制文本与 UI 元素的方向，并在从右到左的语言需要时翻转图像方向。有关更多信息，请参阅[正确处理从右到左的布局](https://developer.apple.com/videos/play/wwdc2022/10107/)。
- **纵向空间需求较大的语言**。使用动态字体（Dynamic Type）防止单词和字母被裁剪，并确保文本间距正确，因为有些语言需要显著更多的垂直空间，另一些语言则有特定的换行和连字符使用惯例。有关动态字体的更多信息，请参阅[自动缩放字体](../uikit/scaling-fonts-automatically.md)和[文本与文本交互的新功能](https://developer.apple.com/videos/play/wwdc2023/10058/)。
- **声音、图像和资源**。使用资源目录对 App 中的颜色、图像和声音进行本地化。有关向资源目录添加资源的更多信息，请参阅[向本地化添加资源](adding-resources-to-localizations.md)和[本地化目录中的资源](localizing-assets-in-a-catalog.md)。

## 另请参阅

### 基础

- [使用 agent 本地化 App](localizing-your-app-using-agents.md) — 使用 agent 编码工具，将 App 中的字符串翻译成多种语言并适应多个地区。
- [使用字符串目录本地化文本并提供变体](localizing-and-varying-text-with-a-string-catalog.md) — 使用字符串目录管理可本地化字符串、添加语言、翻译文本、处理复数，并按设备提供文本变体。
- [在代码中使用生成的可本地化符号](using-generated-localizable-symbols-in-your-code.md) — 将键直接添加到字符串目录，以便使用 Xcode 生成的可本地化符号在代码中引用。
- [本地化 Landmarks](localizing-landmarks.md) — 向 Landmarks 示例代码项目添加本地化。
