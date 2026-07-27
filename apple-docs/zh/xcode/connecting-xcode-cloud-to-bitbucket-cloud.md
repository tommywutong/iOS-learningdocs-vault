---
title: 将 Xcode Cloud 连接到 Bitbucket Cloud
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/connecting-xcode-cloud-to-bitbucket-cloud
source_url: 'https://developer.apple.com/documentation/xcode/connecting-xcode-cloud-to-bitbucket-cloud'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/connecting-xcode-cloud-to-bitbucket-cloud.json'
content_hash: 'sha256:0277a4a183a16865'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md) · [Source code management setup](source-code-management-setup.md)

# 将 Xcode Cloud 连接到 Bitbucket Cloud

<sub>文章</sub>

允许 Xcode Cloud 访问你的 Bitbucket Cloud 仓库。

## 概述

首次配置项目或工作区以使用 Xcode Cloud 时，你需要允许 Xcode Cloud 访问你的 Git 仓库。当你对代码库进行更改时，Xcode Cloud 会用这个访问权限自动构建和测试你的代码。

首次配置项目或工作区以使用 Xcode Cloud 的人，必须拥有该仓库在 Bitbucket Cloud 上的 _administrator_ 权限。如果你没有这个权限，请参阅[将 Xcode Cloud 连接到由管理员管理的 Git 仓库](configuring-xcode-cloud-for-your-team.md#Connect-Xcode-Cloud-to-an-admin-managed-Git-repository)。

要允许 Xcode Cloud 访问你在 [Bitbucket Cloud](https://bitbucket.org) 上的仓库：

1. 按照[配置你的第一个 Xcode Cloud 工作流](configuring-your-first-xcode-cloud-workflow.md)中所述，配置你的项目或工作区以使用 Xcode Cloud，并创建你的第一个工作流。Xcode 会分析你的项目，识别你使用的 SCM 提供方，然后在“授予对你源代码的访问权限”表单中指明你使用的是 Bitbucket Cloud。
2. 点按“授予访问权限”。Xcode 会打开你的浏览器，将你带到 [App Store Connect](https://appstoreconnect.apple.com) 网站。
3. 点按“在 Bitbucket 中完成步骤 1”，将 Xcode Cloud 与你的 Bitbucket 账户连接起来。这会带你前往你在 Bitbucket Cloud 网站上的账户。
4. 查看 Xcode Cloud 请求的权限，并允许其访问你的仓库。这会带你返回 App Store Connect 网站，该网站会指明你已成功将 Xcode Cloud 连接到 Bitbucket Cloud。
5. 返回 Xcode。它会指明 Xcode Cloud 可以访问你的源代码。
6. 点按“下一步”，完成第一个工作流的配置，并开始你的第一次构建。

## 另请参阅

### Bitbucket Cloud 与 Bitbucket Server

- [将 Xcode Cloud 连接到 Bitbucket Server](connecting-xcode-cloud-to-bitbucket-server.md) — 允许 Xcode Cloud 访问你的 Bitbucket Server 仓库。
