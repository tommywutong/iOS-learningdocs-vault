---
title: 管理多个项目及其依赖关系
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/managing-multiple-projects-and-their-dependencies
source_url: 'https://developer.apple.com/documentation/xcode/managing-multiple-projects-and-their-dependencies'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/managing-multiple-projects-and-their-dependencies.json'
content_hash: 'sha256:badf3ed66c7bbf53'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [项目与工作区](projects-and-workspaces.md)

# 管理多个项目及其依赖关系

<sub>文章</sub>

使用工作区（workspace）在一个位置管理相关项目，或使用跨项目引用（cross-project reference）在不同 Xcode 项目之间配置构建时依赖关系。

## 概述

Xcode 项目管理你公司软件产品对应的代码和相关资源。大多数项目围绕单一产品来组织，但你也可以用一个项目来管理多个产品。例如，一个项目可以构建 App、App 扩展以及与 App 相关的框架。项目的组织方式会影响你的团队在这些项目上的协作方式，也可能影响构建性能。

虽然你可以用一个项目来管理公司的全部内容，但将内容分散到多个项目中也有好处：

- 多个较小的项目更容易导览。项目中的文件、目标和产品更少，让你更容易导览项目内容并看清其中的结构。
- 多个项目让分工更容易。如果你有多个团队，给每个团队一个独立的项目可以让他们更独立地工作。
- 多个独立项目可以实现更快的构建时间。将内容分离到多个独立项目中，会促使你消除或最小化这些项目之间的依赖关系。当你限制依赖关系时，Xcode 就能更灵活地并行构建项目，而不是串行构建。

当你将内容分离到独立项目时，它们之间可能仍然存在依赖关系。例如，如果 App 团队和框架团队同时开发各自的内容，他们都需要访问两个项目的最新更改。工作区和跨项目引用可帮助你管理这些项目之间的依赖关系。

### 使用工作区管理多个相关项目

工作区是多个相关项目的容器。使用工作区来组织具有显式或隐式依赖关系的多个项目。例如，你可以使用工作区来组织一个或多个 App 以及它们链接到的共享框架。

创建工作区并向其中添加项目：

1. 在 Xcode 中，选取“文件”>“新建”>“工作区”。
2. 为工作区指定名称并将其保存到文件系统。
3. 在项目导航器（Project navigator）中，按住 Control 键点按空白区域，然后选取“将文件添加到_工作区名称_”。
4. 在出现的表单（sheet）中，选择一个 Xcode 项目（扩展名为 `.xcodeproj` 的文件）。
5. 点按“添加”将项目添加到工作区。

> [!note] 注意
> 你也可以通过将项目从访达（Finder）拖到工作区窗口的项目导航器来将项目添加到工作区。确保将每个项目添加到工作区的根层级，而不是作为另一个项目的子项目。

当你在工作区中添加项目时，Xcode 会自动检测这些项目中目标之间的依赖关系，并按正确顺序构建它们。例如，当你构建一个隐式依赖于另一个项目中框架的 App 时，Xcode 会在构建 App 之前自动构建该框架。当你更改项目时，Xcode 会自动更新所有依赖关系，因此你无需手动更改。

### 显式引用另一个项目中的目标、文件和产品

默认情况下，工作区中的项目无法引用另一个项目中的目标、文件或产品。如果你需要引用另一个项目中的项，必须创建跨项目引用：

1. 在 Xcode 项目中打开项目导航器。
2. 点按项目导航器底部的添加按钮 (+)。
3. 选取“将文件添加到_项目名称_”。
4. 在文件对话框中选择另一个 Xcode 项目（扩展名为 `.xcodeproj`）。
5. 点按“添加”。

添加跨项目引用后，你可以在原始项目的“依赖项（Dependencies）”、“拷贝文件（Copy Files）”和“链接二进制文件与库（Link Binary with Library）”构建阶段中引用其他项目的目标、文件和产品。如果 Xcode 在构建时找不到其他项目，构建系统仍会尝试构建产品，但会产生缺少依赖项的警告。

> [!note] 注意
> 使用工作区来管理多个项目是好的做法。但是，你无法在同一工作区中的两个项目之间创建显式依赖关系。

## 另请参阅

### 文件与工作区

- [管理 Xcode 项目中的文件与文件夹](managing-files-and-folders-in-your-xcode-project.md) — 向项目添加新文件或现有文件，并使用组来组织项目导航器中的文件和文件夹。
- [下载并安装其他 Xcode 组件](downloading-and-installing-additional-xcode-components.md) — 添加更多模拟设备、可选功能以及对其他平台的支持。
