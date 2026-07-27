---
title: 在 App 的 Beta 版本中包含供测试人员参考的说明
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/including-notes-for-testers-with-a-beta-release-of-your-app
source_url: 'https://developer.apple.com/documentation/xcode/including-notes-for-testers-with-a-beta-release-of-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/including-notes-for-testers-with-a-beta-release-of-your-app.json'
content_hash: 'sha256:2b8aa9a898fcad78'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md)

# 在 App 的 Beta 版本中包含供测试人员参考的说明

<sub>文章</sub>

向 Xcode 项目添加文本文件，为 Beta 测试人员提供有关测试内容的说明。

## 概述

通过 TestFlight 从 Xcode Cloud 分发 App 的 Beta 版本时，你可以包含说明，向测试人员介绍更新中包含的更改，并指导他们应测试 App 的哪些区域。使用这些说明将测试重点放在 App 中需要关注的区域。说明会显示在 TestFlight App 的“测试内容”字段中。你提供的信息可以针对特定语言和区域设置。

有关分发 App Beta 版本的更多信息，请参阅[创建用于构建 App 以供分发的工作流程](creating-a-workflow-that-builds-your-app-for-distribution.md)。

> [!note] WWDC23 相关场次
> 第 10224 场：[简化 Xcode 和 Xcode Cloud 中的分发](https://developer.apple.com/videos/play/wwdc2023/10224)

### 创建 TestFlight 文件夹

Xcode Cloud 使用你添加到 Xcode 项目中的文本文件来创建供测试人员参考的说明。文本文件位于名为 TestFlight 的文件夹中，该文件夹与 Xcode 项目或工作区位于同一文件夹。

要创建 TestFlight 文件夹：

- 在 Xcode 中打开项目或工作区。
- 在 Project navigator 中，按住 Control 键点按项目，然后选取 New Group，以创建组及其对应的文件夹。
- 将新组命名为 TestFlight。

### 向文件夹添加文本文件以包含说明

向 TestFlight 文件夹添加文本文件，为测试人员提供说明。若要提供多种语言的说明，请为每种语言创建一个文件。有关 TestFlight 支持的区域设置列表，请参阅 [BetaBuildLocalizationCreateRequest.Data.Attributes](../appstoreconnectapi/betabuildlocalizationcreaterequest/data-data.dictionary/attributes-data.dictionary.md)。有关语言和区域代码的一般信息，请参阅[选择本地化区域和文字](choosing-localization-regions-and-scripts.md)。

要向项目添加文本文件：

- 向 TestFlight 文件夹添加一个新的 Empty 文件。有关说明，请参阅[管理 Xcode 项目中的文件和文件夹](managing-files-and-folders-in-your-xcode-project.md)。
- 使用 `WhatToTest.<LOCALE>.txt` 格式为文件命名。将 `LOCALE` 替换为文件内容所用的语言和区域代码。例如，美国英语使用 `WhatToTest.en-US.txt`。
- 提交文件并将其推送到远程仓库。

Xcode Cloud 下次构建 App 并将其上传到 TestFlight 时，会自动找到此文件，并将其中的文本加入 TestFlight 中 App 的“测试内容”字段。

### 提供实用且恰当的内容

请包含对测试人员有用且与当前版本相关的信息，例如：

- 添加到 App 的功能。
- 在代码中解决的问题。
- 触发构建的提交所对应的提交信息，或最近几条提交信息。

> [!note] 注意
> Xcode Cloud 部署 App 后，你提供的信息会对有权访问该构建版本的所有组中的所有测试人员可见。

### 编写脚本以动态生成内容

你可以使用自定义构建脚本，在 Xcode Cloud 构建期间生成说明。以下示例将 GIT 日志中的最后三条提交信息用作测试人员说明：

```
#!/bin/zsh
#  ci_post_xcodebuild.sh

if [[ -d "$CI_APP_STORE_SIGNED_APP_PATH" ]]; then
  TESTFLIGHT_DIR_PATH=../TestFlight
  mkdir $TESTFLIGHT_DIR_PATH
  git fetch --deepen 3 && git log -3 --pretty=format:"%s" >! $TESTFLIGHT_DIR_PATH/WhatToTest.en-US.txt
fi
```

有关更多信息，请参阅[编写自定义构建脚本](writing-custom-build-scripts.md)。

## 另请参阅

### 设置和维护

- [使依赖项可供 Xcode Cloud 使用](making-dependencies-available-to-xcode-cloud.md) — 在配置项目使用 Xcode Cloud 前，检查依赖项并使其可供 Xcode Cloud 使用。
- [为团队配置 Xcode Cloud](configuring-xcode-cloud-for-your-team.md) — 以团队形式开始使用 Xcode Cloud 进行持续集成和交付。
- [在 Xcode Cloud 工作流程之间共享 macOS 和 Xcode 版本](sharing-custom-aliases-across-xcode-cloud-workflows.md) — 使用自定义别名与多个工作流程共享配置。
- [在 Xcode Cloud 工作流程之间共享环境变量](sharing-environment-variables-across-xcode-cloud-workflows.md) — 使用共享环境变量将通用配置应用于多个工作流程。
- [使用 Xcode Cloud 构建 Swift 包和 Swift Playgrounds App 项目](building-swift-packages-or-swift-playground-app-projects-with-xcode-cloud.md) — 将 Swift 包或 Swift Playgrounds App 项目添加到 Xcode 项目，以便在 Xcode Cloud 中构建。
- [设置 Xcode Cloud 构建的下一个构建编号](setting-the-next-build-number-for-xcode-cloud-builds.md) — 让现有 Mac App 从自定义构建编号开始编号，避免版本冲突。
- [从 Xcode Cloud 移除项目](removing-your-project-from-xcode-cloud.md) — 从 Xcode Cloud 移除项目，以删除 App 和工作流程数据、断开 Git 仓库连接，并移除 Slack 集成。
- [更改 bundle 标识符](changing-the-bundle-identifier.md) — 修改 App 的 bundle 标识符，并更新它出现的所有位置。
