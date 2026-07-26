---
title: 源代码管理设置
framework: xcode
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/source-code-management-setup
source_url: 'https://developer.apple.com/documentation/xcode/source-code-management-setup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/source-code-management-setup.json'
content_hash: 'sha256:c4ae70da2772a9a1'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md)

# 源代码管理设置

允许 Xcode Cloud 访问你的 Git 仓库。

## 概述

借助 Xcode Cloud，你可以采用一套 CI/CD 实践，帮助你开发和维护你的 App 与框架。要让 Xcode Cloud 在你做出更改时自动构建并测试你的代码，请为存放你代码的 Git 仓库提供一条端口 443 上持续可用的安全 HTTPS 连接。

当你把你的工作区或项目配置为使用 Xcode Cloud 时，Xcode 会对其进行分析，以检测你所使用的源代码管理（SCM）提供方。在 "Grant Access to Your Source Code" 表单中，点击 Grant Access，让 Xcode 引导你完成你的 SCM 提供方原生的授权流程。

请确保你拥有向 Xcode Cloud 授予你的 Git 仓库访问权限所需的许可或角色。此外，如果你使用的是自托管的 SCM 提供方——例如 Bitbucket Server——请确保 Xcode Cloud 能够访问你的 Git 仓库。有关 Xcode Cloud 所需权限、角色以及所使用的 IP 地址范围的信息，请参阅[使用远程源代码控制仓库](setting-up-your-project-to-use-xcode-cloud.md#Use-a-remote-source-control-repository)。

> [!note] 注意
> Xcode Cloud 自带对 [Git LFS](https://git-lfs.github.com/) 的支持。

## 主题

### Bitbucket Cloud and Bitbucket Server

- [Connecting Xcode Cloud to Bitbucket Cloud](connecting-xcode-cloud-to-bitbucket-cloud.md) — 允许 Xcode Cloud 访问你的 Bitbucket Cloud 仓库。
- [Connecting Xcode Cloud to Bitbucket Server](connecting-xcode-cloud-to-bitbucket-server.md) — 允许 Xcode Cloud 访问你的 Bitbucket Server 仓库。

### GitHub and GitHub Enterprise

- [Connecting Xcode Cloud to GitHub](connecting-xcode-cloud-to-github.md) — 允许 Xcode Cloud 访问你的 GitHub 仓库。
- [Connecting Xcode Cloud to GitHub Enterprise](connecting-xcode-cloud-to-github-enterprise.md) — 允许 Xcode Cloud 访问你的 GitHub Enterprise 仓库。

### GitLab

- [Connecting Xcode Cloud to GitLab](connecting-xcode-cloud-to-gitlab.md) — 允许 Xcode Cloud 访问你的 GitLab 仓库。
- [Connecting Xcode Cloud to a self-managed GitLab instance](connecting-xcode-cloud-to-a-self-managed-gitlab-instance.md) — 允许 Xcode Cloud 访问你的自管理 GitLab 仓库。

## 另请参阅

### Source code management

- [Configuring requirements for merging a pull request](configuring-requirements-for-merging-a-pull-request.md) — 通过要求 Xcode Cloud 构建或操作成功完成后才能合并 pull request，来保护稳定分支。
