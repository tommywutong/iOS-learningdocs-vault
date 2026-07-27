---
title: 将 Xcode Cloud 连接到 GitLab
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/connecting-xcode-cloud-to-gitlab
source_url: 'https://developer.apple.com/documentation/xcode/connecting-xcode-cloud-to-gitlab'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/connecting-xcode-cloud-to-gitlab.json'
content_hash: 'sha256:6e5a11e3c8f50f6d'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md) · [Source code management setup](source-code-management-setup.md)

# 将 Xcode Cloud 连接到 GitLab

<sub>文章</sub>

允许 Xcode Cloud 访问你的 GitLab 仓库。

## 概述

首次配置项目或工作区以使用 Xcode Cloud 时，你需要允许 Xcode Cloud 访问你的 Git 仓库。当你对代码库进行更改时，Xcode Cloud 会用这个访问权限自动构建和测试你的代码。

首次配置项目或工作区以使用 Xcode Cloud 的人，必须拥有该 GitLab 仓库的 _maintainer_ 角色。如果你没有这个角色，请参阅[将 Xcode Cloud 连接到由管理员管理的 Git 仓库](configuring-xcode-cloud-for-your-team.md#Connect-Xcode-Cloud-to-an-admin-managed-Git-repository)。

要允许 Xcode Cloud 访问你在 [GitLab](https://gitlab.com) 上的仓库：

1. 按照[配置你的第一个 Xcode Cloud 工作流](configuring-your-first-xcode-cloud-workflow.md)中所述，配置你的项目或工作区以使用 Xcode Cloud，并创建你的第一个工作流。Xcode 会分析你的项目，识别你使用的 SCM 提供方，并在“授予对你源代码的访问权限”表单中指明你使用的是 GitLab。
2. 点按“授予访问权限”。Xcode 会打开你的浏览器，将你带到 [App Store Connect](https://appstoreconnect.apple.com) 网站。
3. 点按“在 GitLab 中授权”，打开 GitLab 网站并安装一个用于管理你 GitLab 仓库访问权限的 GitLab App。
4. 查看 Xcode Cloud 请求的权限，并允许其访问你的账户。这会带你返回 App Store Connect 网站，该网站会指明你已成功将 Xcode Cloud 连接到 GitLab。
5. 返回 Xcode。它会指明 Xcode Cloud 可以访问你的源代码。
6. 点按“下一步”，完成第一个工作流的配置，并开始你的第一次构建。

## 另请参阅

### GitLab

- [将 Xcode Cloud 连接到自托管的 GitLab 实例](connecting-xcode-cloud-to-a-self-managed-gitlab-instance.md) — 允许 Xcode Cloud 访问你自托管的 GitLab 仓库。
