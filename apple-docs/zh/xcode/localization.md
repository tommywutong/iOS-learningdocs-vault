---
title: 本地化
framework: xcode
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/localization
source_url: 'https://developer.apple.com/documentation/xcode/localization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/localization.json'
content_hash: 'sha256:059fe656b199792e'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md)

# 本地化

通过支持多种语言和地区来扩大 App 的市场。

## 概述

本地化是将你的 App 翻译并适配为多种语言和地区的过程。请对 App 进行本地化，以便为使用不同语言、并从不同 App Store 地区下载 App 的用户进行适配。

首先，使用可本地化的 API，根据设备的语言和地区设置，正确地格式化并翻译字符串。更多信息，请参阅[在 App 中支持多语言](supporting-multiple-languages-in-your-app.md)。

然后，你可以使用以下几种选项来本地化 App，可以单独使用或组合使用：

- 让编码助手（coding assistant）中的代理（agent）为你添加语言、字符串目录文件和翻译。更多信息，请参阅[使用代理本地化 App](localizing-your-app-using-agents.md)。
- 向 App 中添加字符串目录，并使用字符串目录编辑器管理语言、注释和翻译。更多信息，请参阅[使用字符串目录本地化和变体文本](localizing-and-varying-text-with-a-string-catalog.md)。
- 导出本地化文件并将其发送给*本地化人员（localizer）*，由他们翻译字符串和适配资源。更多信息，请参阅[导出本地化](exporting-localizations.md)和[导入本地化](importing-localizations.md)。

接下来，在 Xcode 预览中以及在模拟设备和物理设备上运行 App，以你支持的语言和地区进行测试。更多信息，请参阅[预览本地化](previewing-localizations.md)和[在运行 App 时测试本地化](testing-localizations-when-running-your-app.md)。

为了获得关于翻译的最佳反馈，将你的 App 分发给以你所支持语言为母语的用户。关于使用 TestFlight 的更多信息，请参阅[分发 App 用于 Beta 测试和发布](distributing-your-app-for-beta-testing-and-releases.md)。

最后，当你发布 App 的本地化版本时，请在 App Store Connect 中为提供 App 的特定地区本地化 App Store 信息。更多信息，请参阅[本地化 App 信息](https://developer.apple.com/help/app-store-connect/manage-app-information/localize-app-information/)。

有关其他本地化技巧、工具和资源，请参阅[将 App 拓展到新市场](https://developer.apple.com/localization/)。

## 主题

### 基础

- [在 App 中支持多语言](supporting-multiple-languages-in-your-app.md) — 对 App 的字符串、图像和其他资源类型进行国际化，为本地化做好准备。
- [使用代理本地化 App](localizing-your-app-using-agents.md) — 使用代理编码工具将 App 中的字符串翻译为多种语言和地区。
- [使用字符串目录本地化和变体文本](localizing-and-varying-text-with-a-string-catalog.md) — 使用字符串目录管理可本地化的字符串、添加语言、翻译文本、处理复数以及按设备对文本进行变体。
- [在代码中使用生成的本地化符号](using-generated-localizable-symbols-in-your-code.md) — 直接将键添加到字符串目录中，以便在代码中使用 Xcode 生成的本地化符号进行引用。
- [本地化 Landmarks](localizing-landmarks.md) — 为 Landmarks 示例代码项目添加本地化。

### 字符串和文本

- [为本地化准备界面](preparing-your-interface-for-localization.md) — 查找 App 中需要翻译的文本，并验证界面是否能适应翻译后的文本。
- [为翻译准备 App 的文本](preparing-your-apps-text-for-translation.md) — 使用可本地化的 API，将 App 中面向用户的文本自动填充到字符串目录中。
- [为翻译准备日期、货币和数字](preparing-dates-numbers-with-formatters.md) — 通过使用格式化工具（formatter），确保日期、货币和数字在多种语言和地区设置下正确显示。

### 布局和视图

- [为本地化准备视图](../swiftui/preparing-views-for-localization.md) — 指定提示并为本地化 SwiftUI 视图添加字符串。
- [在 iOS 中为本地化自动调整视图大小](autosizing-views-for-localization-in-ios.md) — 为 App 添加 Auto Layout 约束以实现可本地化的视图。
- [macOS 中适用于本地化的布局](localization-friendly-layouts-in-macos.md) — 本项目演示了适用于本地化的 Auto Layout 约束。

### 语言和地区

- [添加对语言和地区的支持](adding-support-for-languages-and-regions.md) — 为你支持的每种语言和地区选择要本地化的资源。
- [选择本地化地区和脚本](choosing-localization-regions-and-scripts.md) — 添加仅语言的本地化，或针对特定地区变体和脚本的本地化。

### 资源和素材

- [向本地化添加资源](adding-resources-to-localizations.md) — 在添加到项目中的本地化里包含更多资源。
- [在目录中本地化素材](localizing-assets-in-a-catalog.md) — 使用素材目录本地化颜色、图像、符号、手表复杂功能等。

### 翻译与适配

- [为本地化人员创建 App 截图](creating-screenshots-of-your-app-for-localizers.md) — 与本地化人员共享 App 截图，为翻译提供上下文。
- [导出本地化](exporting-localizations.md) — 将项目中的本地化文件提供给本地化人员。
- [编辑 XLIFF 和字符串目录文件](editing-xliff-and-string-catalog-files.md) — 翻译或适配从项目中导出的、针对特定语言和地区的本地化文件。
- [导入本地化](importing-localizations.md) — 将你为某种语言和地区翻译或适配的文件导入到项目中。
- [在 storyboard 和 XIB 文件中锁定视图](locking-views-in-storyboard-and-xib-files.md) — 在本地化面向用户的字符串时，防止对 Interface Builder 文件进行更改。

### 测试

- [预览本地化](previewing-localizations.md) — 在 SwiftUI 预览或 Interface Builder 预览中测试本地化。
- [在运行 App 时测试本地化](testing-localizations-when-running-your-app.md) — 在你支持的每种语言和地区下运行 App，以进行全面测试。

### 旧版本地化技术

- [本地化包含复数的字符串](localizing-strings-that-contain-plurals.md) — 使用字符串字典文件确保包含语言复数的字符串得到正确本地化。
- [创建字符串的宽度和设备变体](creating-width-and-device-variants-of-strings.md) — 为不同的界面宽度和设备更改本地化字符串。

## 另请参阅

### 界面

- [素材管理](asset-management.md) — 向项目中添加 App 图标、图像、字符串、数据文件、机器学习模型和其他资源，并管理如何在运行时加载它们。
- [Accessibility Inspector](../accessibility/accessibility-inspector.md) — 揭示你的 App 如何向使用辅助功能的用户呈现自身。
