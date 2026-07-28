---
title: 使用字符串目录进行本地化与文本变体
framework: updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/localizing-and-varying-text-with-a-string-catalog
source_url: 'https://developer.apple.com/documentation/xcode/localizing-and-varying-text-with-a-string-catalog'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/localizing-and-varying-text-with-a-string-catalog.json'
content_hash: 'sha256:f24477a189d9e27f'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [本地化](localization.md)

# 使用字符串目录进行本地化与文本变体

<sub>文章</sub>

使用字符串目录（String Catalog）来管理可本地化的字符串、添加语言、翻译文本、处理复数形式以及根据设备调整文本。

## 概述

当你的 App 在用户的区域设置（locale）中运行良好并以用户的母语显示内容时，它能提供最佳体验。支持多种语言和地区不仅仅是翻译文本，还包括处理名词和单位的复数形式，以及在特定设备上显示正确的文本形式。

![](../../../attachments/ca1cd2ff0166df7b3fb34dee9d839e39/localizing-and-varying-text-with-a-string-catalog-0-hero@2x.png)

使用字符串目录（String Catalog）可以借助 Xcode 中的可视化编辑器在同一个地方管理你的可本地化字符串。充分利用 Xcode 为你执行的本地化任务，例如从你的 App 中提取可本地化字符串、生成注释和翻译，以及为每种语言添加复数变体。

要开始使用字符串目录：

1. 向你的项目添加字符串目录。
2. 构建你的 App 以填充字符串目录。
3. 向字符串目录添加一种语言。
4. 为该语言生成翻译。

然后，微调你的代码和翻译，根据需要添加复数和设备变体，并在你支持的每种语言和地区中测试你的 App。此外，探索字符串目录的其他功能，例如为本地化人员生成注释，以及在代码中使用可本地化符号（localizable symbols）代替字符串字面量（string literals）。

有关国际化 App 的更多信息，请参阅[在 App 中支持多语言](supporting-multiple-languages-in-your-app.md)；有关测试的信息，请参阅[预览本地化](previewing-localizations.md)和[在运行 App 时测试本地化](testing-localizations-when-running-your-app.md)。

> [!note] WWDC25 相关讲座
> 讲座 225：[编码实践：使用 Xcode 探索本地化](https://developer.apple.com/videos/play/wwdc2025/225)

### 向项目添加字符串目录

向你的项目添加一个或多个字符串目录文件。你可以从默认的 `Localizable.xcstrings` 文件开始，之后根据代码的复杂程度，再添加更多文件。

要添加字符串目录到项目：

1. 选取“文件”>“新建”>“从模板中创建文件”。
2. 在出现的表单（sheet）中，选择平台，在过滤字段中输入 `string`，在“资源”下选择“字符串目录”，然后点按“下一步”。
3. 在出现的对话框中，接受默认名称 `Localizable` 或输入其他名称，在项目中选择一个文件夹作为位置，然后点按“创建”。

如果添加了多个字符串目录，可以通过在代码中将字符串目录的名称传递给本地化 API 来为每个可本地化字符串选择要使用的字符串目录。有关更多信息，请参阅[将可本地化字符串组织到表格中](preparing-your-apps-text-for-translation.md#Organize-localizable-strings-into-tables)。

### 向字符串目录添加可本地化文本

要将 App 中的可本地化文本填充到字符串目录，选取“产品”>“构建”。Xcode 会自动发现 App 中的可本地化字符串，并将其添加到项目的字符串目录中。每次构建项目时，Xcode 都会根据你对代码中可本地化字符串所做的更改来更新字符串目录。

视图（View）中的大多数 SwiftUI 字符串都是自动可本地化的，并会出现在字符串目录文件中。如果某些字符串缺失，请验证你正在代码中使用可本地化的 API，以便 Xcode 能找到所有面向用户的文本。有关更多信息，请参阅[准备 App 文本以进行翻译](preparing-your-apps-text-for-translation.md)和[准备日期、货币和数字以进行翻译](preparing-dates-numbers-with-formatters.md)。

### 在助理中检查可本地化文本的来源

填充字符串目录后，你可以在添加语言和翻译之前，检查 App 中可本地化文本的位置。

在项目导航器中选择字符串目录文件，然后选取“编辑器”>“助理”。然后，在目录中选择一个键（key），即可在助理中看到可本地化文本的来源。

如有必要，在源代码编辑器中编辑可本地化文本，然后选取“产品”>“构建”以更新字符串目录。

要跳转到源代码编辑器中的文本，请点按将鼠标悬停在字符串目录中的键上方时出现的箭头按钮。你也可以跳转到代码，并在某个键的属性检查器（Attributes inspector）中查看示例用法。

### 为包含复数的字符串添加变体

如果在可本地化字符串中使用了字符串插值（string interpolation），Xcode 可以为字符串目录自动添加复数变体。

不同语言处理名词和单位复数形式的语法规则各不相同。例如，在英文中，当 `%lld` 的值为 `1` 时，你可以返回 `1 item`；而对于其他所有情况，你可以返回 `%lld items`。其他语言可能根据其地区和区域设置，拥有更少或更多的复数变体。

| 复数形式 | 文本 |
|---|---|
| 单数（One） | `%lld item` |
| 其他（Other） | `%lld items` |

首先，将包含插值变量的字符串传递给本地化 API，以便 Xcode 发现它并将其添加到字符串目录中。

```swift
Text("\(collection.landmarks.count) items")
```

在字符串目录编辑器中，按住 Control 键点按包含变量的键，然后从上下文菜单中选择“按复数变体（Vary by Plural）”。Xcode 会为源本地化添加复数变体。

然后，在源本地化中输入不同复数形式的翻译。点按边栏中的语言，点按该字符串键的每种变体在“语言”列中的文本字段，然后输入系统在该复数形式显示时要使用的翻译。

之后，当你向字符串目录添加其他语言时，Xcode 也会自动为这些语言添加特定于语言的变体。例如，当英语是源本地化时，Xcode 会为英语添加“单数（One）”和“其他（Other）”变体；当你添加俄语时，则会为俄语添加“单数（One）”、“少量（Few）”、“许多（Many）”和“其他（Other）”变体。

当选择“按复数变体”时，Xcode 会：

- 将该语言的所有复数形式添加到字符串目录编辑器。
- 确定用于插值字符串的说明符（specifier）（本例中 `%lld` 表示一个 64 位整数）。
- 使用该键的值预填充变体字段。

你可以在添加语言之前或之后，为源本地化添加复数变体，Xcode 会保持所有复数变体同步。如果你为源本地化之外的语言添加复数变体，则该更改仅影响该语言。

### 按设备变体文字

当你需要根据设备上的可用空间或由于设备具有不同的交互方式而更改显示的文本时，请在字符串目录编辑器中使用“按设备变体（Vary by Device）”选项。

例如，假设你想要根据你的 App 是在 iPhone 还是 Mac 上运行，显示两条不同的消息。

| 操作系统 | 消息 |
|---|---|
| iOS | 轻点了解更多 |
| macOS | 点按了解更多 |

要根据设备变体文字字符串，请选择字符串目录文件以及代表你想要变体的消息的语言和键。按住 Control 键点按该键，选择“按设备变体”，然后选择你想要为其添加特定消息的设备。

为你选择的设备输入想要显示的文本，同时为所有其他设备保留现有文本。如果需要更多变体，可以添加更多设备。

当 App 在所选设备上运行时，系统会为该设备显示新消息。

### 自动生成注释

你可以让 Xcode 为可本地化字符串自动创建注释，从而为本地化人员提供更多上下文。这些注释描述了接口元素、周围的界面、占位符内容以及字符串中的变量。

要为特定键生成注释：

1. 在字符串目录编辑器中，按住 Control 键点按要添加注释的键。
2. 从上下文菜单中选择“生成注释”。

你也可以为所有项目启用自动注释生成。在 Xcode >“设置”>“编辑”中，开启“本地化字符串”下的“自动生成字符串目录注释”。

之后，当你导出本地化文件时，任何自动生成的注释旁边都会出现一个“自动生成”注释，以便与人工编写的注释区分开。

或者，将注释传递给代码中的本地化 API。有关更多信息，请参阅[为可本地化字符串添加注释](preparing-your-apps-text-for-translation.md#Add-comments-to-your-localizable-strings)。

### 向项目添加本地化

将你想要支持的语言和地区组合添加到你的字符串目录中。

对于每个本地化，在项目导航器中选择字符串目录，点按字符串目录编辑器底部边栏中的添加按钮（+），然后从弹出菜单中选择一种语言，并可选地选择一个地区。

例如，选择一种语言和地区，例如葡萄牙语（巴西）（pt-BR）或葡萄牙语（葡萄牙）（pt-PT），或者只选择一种语言，例如法语（fr）或希腊语（el）。有关语言和地区的更多信息，请参阅[选择本地化地区和文字](choosing-localization-regions-and-scripts.md)。

你还可以使用项目编辑器中的“信息”窗格来添加和移除语言。在“本地化”下，点按添加按钮，或选择一个本地化然后点按移除按钮（-）。

### 向字符串目录添加翻译

如果你知道所添加语言的翻译，可以直接在字符串目录编辑器中输入它们。要输入翻译，请在边栏中选择要添加翻译的语言。然后，点按该语言列中每个键的文本字段，并输入该键的翻译。

新添加的、需要翻译的字符串会在“状态”列中显示“新建（New）”图标。当你添加翻译时，状态会从“新建”变为“已翻译”，并用绿色对勾表示。随着你添加翻译，语言旁边的百分比符号会更新，显示该语言的翻译百分比。当字符串目录语言达到完全翻译时，百分比符号会变为绿色对勾。

## 另请参阅

### 相关文档

- [使用代理本地化你的 App](localizing-your-app-using-agents.md)——使用代理编码工具将 App 中的字符串翻译成多种语言和地区。

### 基础

- [在 App 中支持多语言](supporting-multiple-languages-in-your-app.md)——国际化 App 的字符串、图像和其他资源类型，为本地化做准备。
- [使用代理本地化你的 App](localizing-your-app-using-agents.md)——使用代理编码工具将 App 中的字符串翻译成多种语言和地区。
- [在代码中使用生成的可本地化符号](using-generated-localizable-symbols-in-your-code.md)——直接向字符串目录添加键，你可以使用 Xcode 生成的可本地化符号在代码中引用这些键。
- [本地化 Landmarks](localizing-landmarks.md)——向 Landmarks 示例代码项目添加本地化。
