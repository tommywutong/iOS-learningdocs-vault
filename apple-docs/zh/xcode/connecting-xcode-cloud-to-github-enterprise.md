---
title: 将 Xcode Cloud 连接到 GitHub Enterprise
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/connecting-xcode-cloud-to-github-enterprise
source_url: 'https://developer.apple.com/documentation/xcode/connecting-xcode-cloud-to-github-enterprise'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/connecting-xcode-cloud-to-github-enterprise.json'
content_hash: 'sha256:3cdffcd27089778b'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md) · [Source code management setup](source-code-management-setup.md)

# 将 Xcode Cloud 连接到 GitHub Enterprise

<sub>文章</sub>

允许 Xcode Cloud 访问你的 GitHub Enterprise 仓库。

## 概述

首次配置项目或工作区以使用 Xcode Cloud 时，你需要允许 Xcode Cloud 访问你的 Git 仓库。当你对代码库进行更改时，Xcode Cloud 会用这个访问权限自动构建和测试你的代码。

如果你把代码托管在某个 GitHub 组织下，首次配置项目以使用 Xcode Cloud 的人必须是该_组织的所有者_。如果你没有使用 GitHub 组织，首次配置项目以使用 Xcode Cloud 的人必须拥有 _admin_ 权限。如果你没有所需的角色或权限，请参阅[将 Xcode Cloud 连接到由管理员管理的 Git 仓库](configuring-xcode-cloud-for-your-team.md#Connect-Xcode-Cloud-to-an-admin-managed-Git-repository)。

如果你的 GitHub Enterprise 实例设置了 IP 白名单，在继续之前请确保已把[我们的 IP 地址范围](https://developer.apple.com/documentation/xcode/Setting-up-your-project-to-use-Xcode-Cloud#Use-a-remote-source-control-repository)添加进去。

要允许 Xcode Cloud 访问你在 [GitHub Enterprise](https://github.com/enterprise) 上的仓库：

1. 按照[配置你的第一个 Xcode Cloud 工作流](configuring-your-first-xcode-cloud-workflow.md)中所述，配置你的项目或工作区以使用 Xcode Cloud，并创建你的第一个工作流。Xcode 会分析你的项目，识别你使用的 SCM 提供方，然后在“授予对你源代码的访问权限”表单中显示你 GitHub Enterprise 实例的 URL。
2. 点按“授予访问权限”。Xcode 会打开你的浏览器，将你带到 [App Store Connect](https://appstoreconnect.apple.com) 网站。
3. 选择 GitHub Enterprise。
4. 注册你 GitHub Enterprise 主机的主机名。对应的字段应该已经包含了你实例的 URL。检查它是否正确；例如，确保其中包含所需的端口。
5. 点按“在 GitHub Enterprise 中完成步骤 1”，跳转到你 GitHub Enterprise 主机的网站。
6. 查看 GitHub App 的名称，然后创建它。GitHub Enterprise 会用这个 App 授予 Xcode Cloud 对你仓库的访问权限。
7. 查看并授权 GitHub App 请求的权限。
8. 授权 Xcode Cloud 在 GitHub Enterprise 上验证你的身份，将你的 GitHub Enterprise 账户与你的 Apple Account 关联起来。
9. 选择只为你项目所在的仓库安装 GitHub App。不要为每个仓库都安装它。安装完成后，GitHub Enterprise 会带你返回 App Store Connect 网站。此时 App Store Connect 会指明你已成功将 Xcode Cloud 连接到 GitHub Enterprise。
10. 返回 Xcode。它会指明 Xcode Cloud 可以访问你的源代码。
11. 点按“下一步”，完成你的第一个工作流，并开始你的第一次构建。

## 另请参阅

### GitHub 与 GitHub Enterprise

- [将 Xcode Cloud 连接到 GitHub](connecting-xcode-cloud-to-github.md) — 允许 Xcode Cloud 访问你的 GitHub 仓库。
