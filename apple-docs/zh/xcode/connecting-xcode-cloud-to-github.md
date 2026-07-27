---
title: 将 Xcode Cloud 连接到 GitHub
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/connecting-xcode-cloud-to-github
source_url: 'https://developer.apple.com/documentation/xcode/connecting-xcode-cloud-to-github'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/connecting-xcode-cloud-to-github.json'
content_hash: 'sha256:997f0c0f18f30d34'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md) · [Source code management setup](source-code-management-setup.md)

# 将 Xcode Cloud 连接到 GitHub

<sub>文章</sub>

允许 Xcode Cloud 访问你的 GitHub 仓库。

## 概述

首次配置项目或工作区以使用 Xcode Cloud 时，你需要允许 Xcode Cloud 访问你的 Git 仓库。当你对代码库进行更改时，Xcode Cloud 会用这个访问权限自动构建和测试你的代码。

如果你把代码托管在某个 GitHub 组织下，首次配置项目以使用 Xcode Cloud 的人必须是该_组织的所有者_。如果你没有使用 GitHub 组织，首次配置项目以使用 Xcode Cloud 的人必须拥有 _admin_ 权限。如果你没有所需的角色或权限，请参阅[将 Xcode Cloud 连接到由管理员管理的 Git 仓库](configuring-xcode-cloud-for-your-team.md#Connect-Xcode-Cloud-to-an-admin-managed-Git-repository)。

要允许 Xcode Cloud 访问你在 [GitHub](https://github.com) 上的仓库：

1. 按照[配置你的第一个 Xcode Cloud 工作流](configuring-your-first-xcode-cloud-workflow.md)中所述，配置你的项目或工作区以使用 Xcode Cloud，并创建你的第一个工作流。Xcode 会分析你的项目，识别你使用的 SCM 提供方，然后指明你使用的是 GitHub。
2. 点按“授予访问权限”。Xcode 会打开你的浏览器，将你带到 [App Store Connect](https://appstoreconnect.apple.com) 网站。
3. 点按“在 GitHub 中完成步骤 1”，打开 GitHub 网站，将你的 Apple Account 与你的 GitHub 账户关联起来。
4. 查看 Xcode Cloud 请求的权限，并授权 Xcode Cloud 将你的 GitHub 账户与你的 Apple Account 关联。
5. 在 GitHub 网站上查看 Apple 提供的 GitHub App，并选择只为你项目所在的仓库安装它。不要为每个仓库都安装它。GitHub 会用这个 App 授予 Xcode Cloud 对你仓库的访问权限。
6. 点按“安装”返回 App Store Connect 网站。该网站会指明你已成功将 Xcode Cloud 连接到 GitHub。
7. 返回 Xcode。它会指明 Xcode Cloud 可以访问你的源代码。
8. 点按“下一步”，完成第一个工作流的配置，并开始你的第一次构建。

## 另请参阅

### GitHub 与 GitHub Enterprise

- [将 Xcode Cloud 连接到 GitHub Enterprise](connecting-xcode-cloud-to-github-enterprise.md) — 允许 Xcode Cloud 访问你的 GitHub Enterprise 仓库。
