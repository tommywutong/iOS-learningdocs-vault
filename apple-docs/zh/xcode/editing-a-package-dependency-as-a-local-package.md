---
title: 将软件包依赖项作为本地软件包进行编辑
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/editing-a-package-dependency-as-a-local-package
source_url: 'https://developer.apple.com/documentation/xcode/editing-a-package-dependency-as-a-local-package'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/editing-a-package-dependency-as-a-local-package.json'
content_hash: 'sha256:e21db160baebdf26'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [Swift 软件包](swift-packages.md)

# 将软件包依赖项作为本地软件包进行编辑

<sub>文章</sub>

通过将软件包依赖项添加为本地软件包来覆盖它并编辑其内容。

## 概述

在 App 中将 Swift 软件包用作软件包依赖项时，你可能需要对其进行编辑。例如，你可能想为开源软件包贡献错误修复。但是，你无法直接编辑软件包依赖项的内容。若要进行更改，请将 Swift 软件包作为本地软件包添加到 App 项目中。不要移除软件包依赖项；添加本地软件包会覆盖同名的软件包依赖项。从项目中移除本地软件包后，Xcode 会再次使用软件包依赖项。

要将 Swift 软件包作为本地软件包添加到项目：

1. 从软件包依赖项的 Git 仓库签出其源代码。
2. 打开 App 的 Xcode 项目或工作区。
3. 选择 File \> Add Package Dependencies。
4. 点按软件包选择窗口底部的 Add Local 按钮。
5. 选择包含软件包的文件夹，然后点按 Add Package 按钮。
6. 为 Xcode 检测到的 Package Products 选择目标。

现在，你可以更改本地软件包，并通过构建和运行 App 来验证更改。完成本地软件包编辑后，将更改推送到其远程 Git 仓库。当这些更改进入软件包的下一个发布版本后，从项目中移除本地软件包，并将软件包依赖项更新到新版本。

## 另请参阅

### 软件包依赖项

- [向 App 添加软件包依赖项](adding-package-dependencies-to-your-app.md) — 集成软件包依赖项，以在项目之间共享代码或利用其他开发者的代码。
- [识别二进制依赖项](identifying-binary-dependencies.md) — 确定软件包依赖项是否引用二进制文件，并验证二进制文件的真实性。
