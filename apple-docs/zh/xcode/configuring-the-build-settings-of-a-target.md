---
title: 配置目标的构建设置
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/configuring-the-build-settings-of-a-target
source_url: 'https://developer.apple.com/documentation/xcode/configuring-the-build-settings-of-a-target'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/configuring-the-build-settings-of-a-target.json'
content_hash: 'sha256:40adafd2392dcb15'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [构建系统](build-system.md)

# 配置目标的构建设置

<sub>文章</sub>

指定用于编译、链接和从目标生成产品的选项，并识别从项目或系统继承的设置。

## 概述

Xcode 构建过程高度可配置，你可以更改单个目标或项目中所有目标的构建设置（Build Settings）。构建设置控制构建过程的每个方面，包括 Xcode 如何编译你的源文件、如何链接你的可执行文件、是否生成调试信息，以及如何打包和分发你的代码。Xcode 有数百个构建设置，以支持与构建过程相关的工具和步骤。

你可以从“Build Settings”（构建设置）标签页或使用构建配置文件对项目或目标的设置进行更改。下图显示了一个项目的“Build Settings”（构建设置）标签页。

![](../../../attachments/af7a7a11967dfd4ab70af3f67339364e/build-settings-editor@2x.png)

<sub>一个 Xcode 窗口显示了所选目标的构建设置，以及用于筛选和搜索设置列表的控制。</sub>

> [!note] 注意
> 你也可以将设置存储在格式特殊的纯文本文件中，这些文件称为构建配置文件（Build Configuration File）。这些文件便于你连同设置一起，将源文件保存在源代码管理系统中。有关构建配置文件的信息，请参阅[向项目中添加构建配置文件](adding-a-build-configuration-file-to-your-project.md)。

有关构建设置的完整列表，请参阅[构建设置参考](build-settings-reference.md)。

### 搜索和筛选构建设置列表

要快速找到特定的构建设置，可以使用“Build Settings”（构建设置）标签页顶部的筛选器和搜索字段。

- 选择一个筛选器以显示所有设置或仅显示已修改的设置。
- 在搜索字段中输入文本，以显示包含指定字符串的设置。默认情况下，Xcode 会搜索所有设置特性。
- 若要细化搜索，请单击放大镜图标并选择要匹配的单个特性。

### 配置构建设置的值

每个构建设置都包含以下特性。

| 特性 | 描述 | 示例 |
|---|---|---|
| 标题 | 构建设置的人类可读名称。 | `Build Active Architecture Only` |
| 名称 | 构建设置的程序化名称。该名称出现在 Quick Help（快速帮助）检查器、构建配置（`xcconfig`）文件和 `xcodebuild` 命令行工具中。 | `ONLY_ACTIVE_ARCH` |
| 值类型 | 常见类型包括布尔值、字符串、枚举、字符串列表、路径字符串和路径字符串列表。 | `Boolean` |
| 值 | 设置的当前值。 | `YES` |

“Build Settings”（构建设置）标签页会显示设置的标题或名称，但不会同时显示两者。当标题可见时，选择 Editor \> Show Setting Names 以显示名称。当名称可见时，选择 Editor \> Show Setting Titles 以显示标题。

当你找到要修改的设置后，单击值特性并输入新值。Xcode 会对已修改的设置应用粗体字体，以便你稍后能轻松找到它们。若要恢复设置的原始值，请选中该设置并按 Delete 键。如果你是在“Levels”（层级）视图中修改的设置，请在你覆盖值的层级删除该设置。例如，如果你在项目中覆盖了该设置，则在那里删除该设置，而不是在属于该项目的目标中删除。

要为调试和发布构建配置不同的值，请单击设置项的展开三角形以显示特定于配置的值，并在那里进行更改。如果你在设置项的展开三角形处于关闭状态时修改了设置，Xcode 会将更改应用于两种配置。

某些设置的值是参考其他设置来定义的。例如，某个值是指向文件路径的特性可能使用 `BUILD_DIR` 设置来指定路径的一部分。当设置的定义可见时，选择 Editor \> Show Values 以查看计算后的最终值——即不带环境变量的值。当最终值可见时，选择 Editor \> Show Definitions 以查看定义。

### 评估项目如何继承设置

每个目标都从其父项目和平台 SDK 继承设置。这种继承模型确保目标一开始就拥有有效的基线设置。当你创建目标时，Xcode 会根据目标类型更改某些设置，你也可以根据自身需要自由进行其他更改。

为了帮助你查明设置值的来源，请打开项目或目标的构建设置，然后选择“Levels”（层级）筛选器。Xcode 会在构建设置编辑器中显示当前的设置层级。此层级包括默认的 SDK 值以及任何其他处于活动状态的项目或目标值。“Resolved”（已解析）列显示 Xcode 用于构建项最终解析的值。

![](../../../attachments/6f1f0ea843065c4fd5bceb5188cf354a/build-setting-inheritance-hierarchy@2x.png)

<sub>构建设置编辑器中的“Levels”（层级）选项显示默认系统设置、项目设置和目标设置的继承关系。</sub>

显示层级时，高亮的值表示具有更高优先级的值。Xcode 在引用你为项目定义的构建设置之前，会优先使用目标的构建设置。在每个层级，Xcode 优先使用你在项目中提供的设置，然后才是你在构建配置文件中提供的设置。Xcode 将最低优先级分配给系统默认值。优先级层级如下：

1. 目标层级的值。
2. 映射到目标的配置设置文件的值。
3. 项目层级的值。
4. 映射到项目的配置设置文件。
5. 系统默认值。

> [!note] 注意
> 使用 `xcodebuild` 命令行工具时，该工具会为你传递给它的任何设置赋予最高优先级。

### 获取构建设置的更多详细信息

要查看特定设置的详细信息，请选择该设置，然后选择 View \> Inspectors \> Quick Help。Xcode 会显示该设置的描述，以及其名称和值类型。

![Quick Help（快速帮助）检查器显示了所选构建设置的详细信息。](../../../attachments/c40047e4289f3d112b8f553c3e70d542/build-setting-quick-help@2x.png)

## 另请参阅

### 构建设置

- [向项目中添加构建配置文件](adding-a-build-configuration-file-to-your-project.md) — 在纯文本文件中指定项目的构建设置，并为调试和发布构建提供不同的设置。
- [构建设置参考](build-settings-reference.md) — 控制或更改目标构建方式的各个 Xcode 构建设置的详细列表。
- [识别和解决框架模块问题](identifying-and-addressing-framework-module-issues.md) — 使用模块验证器检测并修复框架模块中的常见问题。
- [理解 Xcode 构建产物布局的变化](understanding-build-product-layout-changes.md)
