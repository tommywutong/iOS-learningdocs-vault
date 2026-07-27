---
title: 在项目中配置新 target
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/configuring-a-new-target-in-your-project
source_url: 'https://developer.apple.com/documentation/xcode/configuring-a-new-target-in-your-project'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/configuring-a-new-target-in-your-project.json'
content_hash: 'sha256:e0b01907c91e9bfc'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [构建系统](build-system.md)

# 在项目中配置新 target

<sub>文章</sub>

配置项目以构建新产品，并添加该产品所需的代码和资源。

## 概述

target 指定要构建的产品，例如 App、框架、App 扩展或单元测试。一个项目可以包含多个 target，分别表示单个产品的相关组成部分。例如，一个项目可以分别包含 App、私有框架、App 扩展和测试套件的 target。

从模板创建新项目时，Xcode 会自动向项目添加一个或多个 target。要查看项目中的 target，请在项目导航器中选择该项目，target 列表便会出现在右侧项目编辑器的边栏中。例如，带测试的多平台 App 模板会分别为 App 和测试创建 target。

![](../../../attachments/04ee97f6359e9ce1650d825476201465/build-targets@2x.png)

<sub>Xcode 项目窗口的截图，其中在项目导航器中选中了项目，在项目编辑器边栏中选中了 App target，右侧显示 General 面板。</sub>

编辑器区域会显示当前项目和 target 的信息。要查看 target 的常规信息，请在项目编辑器工具栏中点按 General 标签页。要查看签名资源和添加到 target 的功能，请点按 Signing & Capabilities 标签页。

要查看项目设置，请在 target 列表上方的边栏中选择项目。对 target 所做的更改只会影响该 target，而对项目所做的更改会影响所有 target。

### 向项目添加新 target

添加新 target 可在项目中创建独立产品、使用 App 扩展增强现有 App，或将代码拆分到私有框架中。你还可以向项目添加新的 App、系统扩展、测试套件和其他类型的 target。

要添加新 target：

1. 选择 File \> New \> Target。
2. 为新 target 选择平台。
3. 从下方选择一个模板。
4. 点按 Next。
5. 在对话框中输入 target 名称，并选择编程语言等其他设置。
6. 点按 Finish。

![Xcode 模板表单（sheet）的截图，展示可用于多平台 target 的模板。](../../../attachments/31fb5f25baae727b93e278d1eff02707/build-target-templates@2x.png)

你可以将某些类型的 target 直接嵌入现有 App 的套装中。对于计划随 App 一起交付的框架、App 扩展和其他产品，此选项可以简化设置过程。嵌入 target 时，Xcode 会配置必要的项目设置来构建该 target，并将其复制到你的 App 中。Xcode 还会创建必要的依赖项，确保各 target 按正确顺序构建。

### 向 target 添加源文件和其他内容

使用文件模板可以帮助你快速开始开发 App。

要创建新文件并将其直接嵌入现有 target，请选择 File \> New \> File from Template。然后选择平台和模板，并在出现的对话框中点按 Next。或者，选择 File \> New \> Empty File。

![Xcode 新文件模板表单的截图，其中选中了 iOS 平台和 Swift File 模板。](../../../attachments/301b60128860a4b4b0aaaa2f44880adf/build-target-new-file-templates@2x.png)

要将现有文件分配给新 target，请在项目导航器中选择该文件，然后在文件检查器中更改 target 成员资格特性（attribute）。在 Target Membership 下点按添加按钮（+）。在 Choose Targets 对话框中，选择要将该文件添加到的 target，然后点按 Save。

![Choose Targets 对话框的截图，其中显示 target 列表。](../../../attachments/815bcd621c2f491a6af1896c741a036d/build-target-membership-settings@2x.png)

有关如何向项目添加文件的更多信息，请参阅[管理 Xcode 项目中的文件和文件夹](managing-files-and-folders-in-your-xcode-project.md)。

### 配置两个 target 之间的依赖关系

依赖关系会告诉 Xcode 应以何种正确顺序构建一组 target。Xcode 会尽可能并行构建 target，但有时必须串行构建。

例如，Xcode 必须先构建自定框架，再构建链接该框架的 App。如果你选中 Find Implicit Dependencies 方案选项，将新 target 嵌入 App 时，Xcode 会在 App 与 target 之间创建依赖关系。如果未选中该选项，则必须自行配置依赖关系。

要查看和添加依赖关系，请在边栏中选择一个 target，然后在项目编辑器工具栏中点按 Build Phases 标签页。Xcode 在构建当前 target 前必须成功构建的 target 会显示在 Target Dependencies 下。如果多个依赖 target 之间不存在相互依赖关系，Xcode 可以同时构建它们。

![](../../../attachments/e4d59340523f1a0f4f31b1a30d31ee1f/build-phase-settings-dependencies@2x.png)

<sub>Xcode 项目编辑器的截图，其中边栏中选中了一个 target，Build Phases 标签页处于选中状态，并展开显示 Target Dependencies 设置。</sub>

如果 target 之间存在 Xcode 无法轻易检测的关系，请手动添加依赖关系。虽然选中 Find Implicit Dependencies 构建方案选项后，Xcode 可以自动添加依赖关系，但它无法检测所有依赖关系。例如，如果一个 target 依赖另一个 target 中自定脚本所构建的数据文件，Xcode 无法检测到这种情况。如果未指定必要的依赖关系，Xcode 可能会报告错误或错误地构建 target。

> [!note] 注意
> 如果你的 target 依赖另一个 Xcode 项目中的内容，请先添加对该项目的引用，再配置任何依赖关系。有关更多信息，请参阅[管理多个项目及其依赖关系](managing-multiple-projects-and-their-dependencies.md)。

有关通过优化 target 来缩短构建时间的更多信息，请参阅[提高增量构建的速度](improving-the-speed-of-incremental-builds.md)。

## 另请参阅

### 基础

- [配置多平台 App](configuring-a-multiplatform-app-target.md) — 在单个 App target 中跨平台共享项目设置和代码。
