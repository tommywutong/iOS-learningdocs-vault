---
title: 下载并安装其他 Xcode 组件
framework: updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/downloading-and-installing-additional-xcode-components
source_url: 'https://developer.apple.com/documentation/xcode/downloading-and-installing-additional-xcode-components'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/downloading-and-installing-additional-xcode-components.json'
content_hash: 'sha256:a12d6988acf9eeff'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [项目与工作区](projects-and-workspaces.md)

# 下载并安装其他 Xcode 组件

<sub>文章</sub>

添加更多模拟设备、可选功能和对其他平台的支持。

## 概述

Xcode 允许你自行管理可选组件，只安装使用的组件，并移除不使用的组件。例如，为 App 运行所用的设备和操作系统安装模拟器运行时，或添加对目标平台的支持。你可以在 Xcode 设置中或使用命令行下载并安装 Xcode 组件。

> [!note] 注意
> 为 visionOS 开发需要配备 Apple 芯片的 Mac。

### 在设置中管理 Xcode 组件

若要管理组件，请选择 Xcode \> Settings，然后在边栏中点按 Components。Xcode 会显示已安装和已启用的组件，以及移除它们后可收回的存储空间。

组件分为三种类型：

- **Platform Support** — 可用于开发 App 的平台。
- **Other Components** — 可以启用和停用的可选 Xcode 功能。
- **Other Installed Platforms** — 不同设备和操作系统版本的模拟器运行时，可用于运行 App。

若要下载并安装这些部分中的组件，请点按组件旁边的 Get 按钮。

若要移除或停用不再使用的组件并收回其存储空间，请点按组件旁边的信息按钮。在出现的对话框中，根据组件点按 Delete 或 Turn Off。

创建项目时，也可以通过选择模板并为未安装的平台点按出现的 Get 按钮来安装平台支持。有关更多信息，请参阅[为 App 创建 Xcode 项目](creating-an-xcode-project-for-an-app.md)。

> [!note] 注意
> 你可以在 Xcode 正在安装的平台上创建新的 Xcode 项目或处理现有项目，但在 Xcode 完成文件下载和安装前，无法运行或构建项目。

### 在设置中安装以前发布的模拟器运行时

你可以在 Components 设置中获取以前发布的模拟器运行时。在 Other Installed Platforms 下，点按 Add Platforms 按钮。若要筛选出现的对话框中的列表，请选择平台，并在工具栏的筛选字段中输入词语。然后在下方列表中选择一个或多个版本，并点按 Download & Install。

### 从 Xcode 运行目标安装模拟器运行时

打开某个平台的 Xcode 项目，而该平台尚未安装任何模拟器运行时时，Xcode 会在运行目标旁边和画布中显示 Get 按钮。点按 Get 按钮，下载并安装该平台最新的模拟器运行时。

Xcode 下载模拟器运行时时，Xcode 项目中的运行目标会指示这一状态。Xcode 完成下载和安装后，你可以选择运行目标。

### 从命令行下载 Xcode 组件

你也可以在“终端”中使用 `xcodebuild` 命令下载组件。例如，使用命令行下载一次 Xcode 组件，然后将它们安装到多台 Mac 电脑上。

若要下载特定平台的模拟器运行时，请使用以下语法：

```
xcodebuild -downloadPlatform <iOS|watchOS|tvOS|visionOS>  [-exportPath <destinationpath> -buildVersion <osversion> -architectureVariant <universal|arm64>]
```

例如：

```
xcodebuild -downloadPlatform iOS -exportPath ~/Downloads
```

若要指定操作系统版本，请添加 `-buildVersion` 选项：

```
xcodebuild -downloadPlatform iOS -exportPath ~/Downloads -buildVersion 18.0 
```

若要下载所选 Xcode 版本支持的所有平台，请使用以下带 `-downloadAllPlatforms` 选项的语法：

```
xcodebuild -downloadAllPlatforms [-exportPath <path>]
```

默认情况下，Xcode 会根据 Mac 电脑的架构以及是否使用 Rosetta 运行目标来下载变体。对于基于 Intel 的 Mac 电脑和使用 Rosetta 运行目标的情况，Xcode 会下载通用变体。否则，Xcode 会下载 Apple 芯片变体，以节省所指定平台占用的磁盘空间。

若要下载可同时用于 Apple 芯片和基于 Intel 的 Mac 电脑的通用变体，请使用 `-architectureVariant` 选项：

```
xcodebuild -downloadPlatform iOS -architectureVariant universal
```

### 从命令行安装已下载的软件包

下载组件包后，可以在“终端”中使用 `xcodebuild` 命令进行安装。

首先，使用 `xcode-select -s <path-to-Xcode>` 命令选择要使用的 Xcode 版本。接下来，运行 `xcodebuild -runFirstLaunch` 安装所有必需的系统组件，包括 `simctl` 实用工具。然后，使用带 `-importPlatform <simruntime.dmg>` 选项的 `xcodebuild` 安装组件。

```
xcode-select -s /Applications/Xcode-beta.app
xcodebuild -runFirstLaunch
xcodebuild -importPlatform "~/Downloads/watchOS 9 beta Simulator Runtime.dmg"
```

### 在 Xcode 发布版本之间下载并安装新硬件支持

若要在 Xcode 发布版本之间下载并安装硬件支持更新，请使用带 `-runFirstLaunch` 和 `-checkForNewerComponents` 选项的 `xcodebuild`。运行此命令前，请使用 `xcode-select -s <path-to-Xcode>` 命令选择要使用的 Xcode 版本。

```
xcode-select -s /Applications/Xcode.app
xcodebuild -runFirstLaunch -checkForNewerComponents
```

如果存在新组件，`-checkForNewerComponents` 选项会将文件存储在 `~/Library/Developer/Packages/` 目录中，并为你选择的 Xcode 版本安装组件。

### 下载并安装 Metal Toolchain

若要构建 Metal App，请为 App 的目标平台下载并安装可选的 Metal Toolchain。

首次启动 Xcode 时，如果出现允许选择组件的表单，请选择 App 的平台，在 Additional Components 下选择 Metal Toolchain，然后点按 Install。

否则，你可以使用 Xcode 中的 Components 设置管理所有下载，包括 Metal Toolchain。选择 Xcode \> Settings，在边栏中点按 Components，然后在右侧 Other Components 下点按 Metal Toolchain 旁边的 Get 按钮。

如果在下载 Metal Toolchain 之前尝试构建需要该工具链的 App，会出现一个对话框。点按 Download 下载 Metal Toolchain。

或者，若要从命令行下载并安装该工具链，请在“终端”中运行以下命令：

```
xcodebuild -downloadComponent metalToolchain
```

若要分别下载和安装工具链，请先下载并将其导出到文件：

```
xcodebuild -downloadComponent metalToolchain -exportPath ~/Downloads
```

然后，将工具链安装到 Xcode：

```
xcodebuild -importComponent metalToolchain ~/Downloads/metalToolchain.dmg
```

## 另请参阅

### 文件和工作区

- [管理 Xcode 项目中的文件和文件夹](managing-files-and-folders-in-your-xcode-project.md) — 向项目添加新文件或现有文件，并使用组整理 Project navigator 中的文件和文件夹。
- [管理多个项目及其依赖项](managing-multiple-projects-and-their-dependencies.md) — 使用工作区在一处管理相关项目，或使用跨项目引用配置不同 Xcode 项目之间的构建时依赖关系。
