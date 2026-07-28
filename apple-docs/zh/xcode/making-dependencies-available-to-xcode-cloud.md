---
title: 让 Xcode Cloud 能够访问依赖项
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/making-dependencies-available-to-xcode-cloud
source_url: 'https://developer.apple.com/documentation/xcode/making-dependencies-available-to-xcode-cloud'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/making-dependencies-available-to-xcode-cloud.json'
content_hash: 'sha256:0d5b9e2f3860fe9e'
translated: true
---

> 导航： [技术](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md)

# 让 Xcode Cloud 能够访问依赖项

<sub>文章</sub>

在配置项目以使用 Xcode Cloud 之前，请先审查依赖项，并确保 Xcode Cloud 能够访问它们。

## 概述

Xcode Cloud 将你用于创建 App 和框架的工具整合在了一起：[Xcode](https://developer.apple.com/xcode/)、[TestFlight](https://developer.apple.com/testflight/) 和 [App Store Connect](https://appstoreconnect.apple.com)。然而，你的 Xcode 项目或工作区可能还需要额外的依赖项或第三方工具才能编译代码。例如，你可能使用了开源社区创建的库，或者使用了 Swift 包依赖项在 App 之间复用和共享代码。

如果 Xcode Cloud 无法访问私有依赖项或第三方工具，它将无法成功构建你的项目。为了避免构建失败，并在开始使用 Xcode Cloud 时节省时间，请在配置项目使用 Xcode Cloud 之前，先审查你的依赖项，并确保 Xcode Cloud 能够访问它们。

> [!note] 注意
> Xcode Cloud 使用的临时构建环境包含了 macOS 和 Xcode 自带的工具 —— 例如 Python —— 并且还额外包含了 [Homebrew](https://brew.sh) 以支持安装第三方依赖项和工具。有关更多信息，请参阅下面的“使用自定义构建脚本安装第三方依赖项或工具”部分。

### 使用 Swift 包依赖项和 Git 子模块

Xcode Cloud 支持通过 Swift 包和 Git 子模块管理的依赖项，如果它们的仓库是公开可访问的，则无需任何单独配置。如果你使用了私有依赖项，Xcode Cloud 会帮助你访问它们。有关使用它们的更多信息，请参阅下文[授予 Xcode Cloud 对私有依赖项的访问权限](making-dependencies-available-to-xcode-cloud.md#Grant-Xcode-Cloud-access-to-private-dependencies)。

遵循在 CI/CD 环境中使用 Swift 包依赖项的最佳实践，Xcode Cloud 不使用自动包解析，而是依赖 `Package.resolved` 文件来解析你的依赖项。如果你的项目中使用了 Swift 包依赖项，请确保将 `Package.resolved` 文件包含在你的 Git 仓库中，并提交对其的所有更改。不要将此文件包含在你的 `.gitignore` 文件中。此外，请确保 `Package.resolved` 文件位于 `$filename.xcodeproj/project.workspace/xcshareddata/swiftpm/Package.resolved`。

> [!note] 注意
> 强制 Xcode Cloud 使用自动包解析 —— 例如，通过在自定义构建脚本中更改设置 —— 可能导致未定义的行为和构建失败。

关于在持续集成和交付环境中构建 Swift 包的一般信息，请参阅[在持续集成工作流中构建 Swift 包或使用它们的 App](building-swift-packages-or-apps-that-use-them-in-continuous-integration-workflows.md)。

### 授予 Xcode Cloud 对私有依赖项的访问权限

当你配置项目或工作区以使用 Xcode Cloud 时，Xcode 会检测你用于托管代码的源代码管理（SCM）提供商。它还会检测每个私有 Git 子模块、Swift 包依赖项或你在自定义脚本中访问的 Git 仓库的 SCM 提供商，并帮助你授予 Xcode Cloud 对其的访问权限。例如，如果你使用 [Bitbucket Server](https://bitbucket.org/product/enterprise) 托管代码，并使用了你通过 [GitLab](https://gitlab.com) 托管的私有依赖项，Xcode 会帮助你同时将你的 Bitbucket Server 和你的 GitLab 帐户连接到 Xcode Cloud。

如果你添加了 Xcode Cloud 无法访问的新的私有包依赖项，下一次构建将会失败。要解决此问题，请导航到失败构建的构建报告，并让 Xcode 或 App Store Connect 帮助你连接 Xcode Cloud 到该依赖项的 SCM 提供商。

> [!note] 注意
> 你需要将你的私有依赖项托管在受支持的 SCM 提供商之一。有关受支持的 SCM 提供商的更多信息，请参阅[源代码管理设置](source-code-management-setup.md)。

构建你的项目可能需要访问你自托管 SCM 提供商的一个以上实例 —— 对于大型团队来说这是常见情况。例如，你可能使用了两个不同的 GitHub Enterprise 实例，一个托管你的 App 代码，另一个托管你的依赖项。如果你的情况符合此场景，请在 Xcode 中完成项目的初始用户引导工作流，并连接托管你 App 代码的实例，然后让第一次构建失败。构建失败后，Xcode 会建议连接另一个实例的修复方法。

### 审查第三方依赖项

如果你使用了像 [CocoaPods](https://cocoapods.org) 或 [Carthage](https://github.com/Carthage/Carthage) 这样的第三方依赖管理器，或者需要额外的工具来成功构建你的项目，你需要在能够使用 Xcode Cloud 之前，对你的项目或工作区进行更改。

由于第三方工具和依赖项需要额外的工作，请在配置项目或工作区使用 Xcode Cloud 之前，审查并简化你的第三方依赖项。例如，你可能能够将一个依赖项替换为 Apple 提供的框架。或者，查看其创建者是否将该依赖项作为 Swift 包提供。如果是这样，你可以使用该包并利用 Swift Package Manager 的支持，而无需配置 Xcode Cloud 来使用第三方工具。

如果切换到 Swift 包依赖项或移除依赖项不现实，请按照以下说明操作，以确保 Xcode Cloud 能够访问依赖项和所需的工具。

### 使用自定义构建脚本安装第三方依赖项或工具

Xcode Cloud 用于执行构建的临时构建环境不包含第三方工具或依赖项。然而，它包含了 [Homebrew](https://brew.sh)，这是一个开源包管理器，你可以使用它来安装额外的软件。例如，你可以使用 Homebrew 来安装像 [CocoaPods](https://cocoapods.org) 或 [Carthage](https://github.com/Carthage/Carthage) 这样的依赖管理器。

要使用 Homebrew 安装工具：

1. 在你的 Xcode 项目或工作区旁边创建一个目录，并将其命名为 `ci_scripts`。
2. 创建一个可执行的 shell 脚本，将其命名为 `ci_post_clone.sh`，并保存在 `ci_scripts` 目录中。例如，在 Xcode 中使用 Shell 脚本模板创建该文件，然后在终端中运行 `chmod +x ci_post_clone.sh` 使其成为可执行文件。
3. 在 Xcode 中打开自定义脚本，并添加必要的命令来使用 Homebrew 安装工具。

> [!note] 注意
> 你可以使用自定义构建脚本来执行各种任务，但不能通过使用 `sudo` 来获取管理员权限。

有关自定义构建脚本的更多信息，请参阅[编写自定义构建脚本](writing-custom-build-scripts.md)。

### 使 CocoaPods 依赖项对 Xcode Cloud 可用

CocoaPods 是 Apple 平台的一个开源依赖管理器。Xcode Cloud 用于执行构建的临时构建环境已预装该工具。如果你使用 CocoaPods，首先确保你同时提交了 `Podfile` 和 `Podfile.lock` 文件。然后，在以下选项中选择一个：

- 通过提交将 `Pods` 目录添加到你的 Git 仓库。
- 通过将 `Pods` 目录添加到你的 `.gitignore` 文件，将其排除在源代码管理之外。

如果你提交了 `Pods` 目录及其内容，你将无需安装由 CocoaPods 管理的依赖项，即可让 Xcode Cloud 构建你的项目或工作区。但需要注意的是，添加 `Pods` 目录会占用你源代码仓库的更多空间。此外，请记住，提交二进制依赖项会影响你的 Git 仓库的性能。这是使用 Git 时的一个普遍问题，并非 Xcode Cloud 所特有。

> [!tip] 提示
> 如果你决定提交 `Pods` 目录，可以考虑使用 [Git LFS](https://git-lfs.github.com)。它已预装在 Xcode Cloud 用于构建你的项目的临时构建环境中。

如果你选择将 `Pods` 目录排除在源代码管理之外，则需要使用自定义构建脚本来安装由 CocoaPods 管理的依赖项。然而，这样做的好处是源代码仓库占用更少的磁盘空间，并且不会拖慢你的 Git 仓库。要使用自定义构建脚本安装 CocoaPods 依赖项：

1. 按照[使用自定义构建脚本安装第三方依赖项或工具](making-dependencies-available-to-xcode-cloud.md#Use-a-custom-build-script-to-install-a-third-party-dependency-or-tool)中的描述创建一个 post-clone 脚本。
2. 向脚本中添加安装 CocoaPods 依赖项的命令。以下代码片段显示了一个实现此目的的基本脚本：

  ```bash
  #!/bin/sh

  # 安装你通过 CocoaPods 管理的依赖项。
  pod install
  ```

### 使 Carthage 依赖项对 Xcode Cloud 可用

Carthage 是 Apple 平台的一个开源依赖管理器。然而，Xcode Cloud 用于构建你的项目的临时构建环境并未预装该工具。为了支持依赖 `carthage copy-frameworks` 命令的项目 —— 大多数项目都如此 —— 请使用自定义构建脚本安装 Carthage：

1. 按照[使用自定义构建脚本安装第三方依赖项或工具](making-dependencies-available-to-xcode-cloud.md#Use-a-custom-build-script-to-install-a-third-party-dependency-or-tool)中的描述创建一个 post-clone 脚本。
2. 向脚本中添加必要的命令，以使用 Homebrew 安装 Carthage 并构建你的 Carthage 依赖项。

## 另请参阅

### 设置与维护

- [为你所在的团队配置 Xcode Cloud](configuring-xcode-cloud-for-your-team.md) — 开始作为一个团队使用 Xcode Cloud 进行持续集成和交付。
- [在 Xcode Cloud 工作流间共享 macOS 和 Xcode 版本](sharing-custom-aliases-across-xcode-cloud-workflows.md) — 使用自定义别名在多个工作流之间共享配置。
- [在 Xcode Cloud 工作流间共享环境变量](sharing-environment-variables-across-xcode-cloud-workflows.md) — 通过使用共享环境变量将通用配置应用于多个工作流。
- [使用 Xcode Cloud 构建 Swift 包和 Swift Playgrounds App 项目](building-swift-packages-or-swift-playground-app-projects-with-xcode-cloud.md) — 将你的 Swift 包或 Swift Playgrounds App 项目添加到 Xcode 项目中，以便在 Xcode Cloud 中构建它。
- [设置 Xcode Cloud 构建的下一个构建编号](setting-the-next-build-number-for-xcode-cloud-builds.md) — 为你现有的 Mac App 从自定义构建编号开始对构建进行编号，以避免版本冲突。
- [在 App 的 Beta 版本中包含给测试人员的备注](including-notes-for-testers-with-a-beta-release-of-your-app.md) — 向你的 Xcode 项目添加文本文件，为 Beta 测试人员提供关于测试内容的备注。
- [从 Xcode Cloud 中移除你的项目](removing-your-project-from-xcode-cloud.md) — 从 Xcode Cloud 中移除你的项目，以删除 App 和工作流数据、断开你的 Git 仓库连接，并移除 Slack 集成。
- [更改 Bundle Identifier](changing-the-bundle-identifier.md) — 修改你 App 的 Bundle Identifier，并在所有出现的地方进行更新。
