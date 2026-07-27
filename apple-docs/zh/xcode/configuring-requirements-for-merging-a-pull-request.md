---
title: 配置合并拉取请求的要求
framework: updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/configuring-requirements-for-merging-a-pull-request
source_url: 'https://developer.apple.com/documentation/xcode/configuring-requirements-for-merging-a-pull-request'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/configuring-requirements-for-merging-a-pull-request.json'
content_hash: 'sha256:3df869e578202d60'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md)

# 配置合并拉取请求的要求

<sub>文章</sub>

要求 Xcode Cloud 构建或操作成功后才能合并拉取请求，从而保护稳定分支。

## 概述

当你配置一个会针对拉取请求（pull request，PR）的每项更改启动新构建的 Xcode Cloud 工作流程时，Xcode Cloud 会在源代码管理（source code management，SCM）提供商的 PR 网页上报告构建状态。因此，你可以识别 PR 中的更改所导致的问题。但是，构建状态并不会阻止你合并 Xcode Cloud 构建失败的 PR。

为防止合并包含错误的 PR，[Bitbucket Cloud](https://bitbucket.org)、[Bitbucket Server](https://bitbucket.org/product/enterprise)、[GitHub](https://github.com) 和 [GitHub Enterprise](https://github.com/enterprise) 允许你配置 PR 在能够合并前必须满足的要求。Xcode Cloud 支持这些分支保护功能。你可以要求整个 Xcode Cloud 构建成功后才能合并 PR，也可以要求特定 Xcode Cloud 操作成功。

配置 PR 要求的用户界面取决于 SCM 提供商：

- [Bitbucket Cloud](https://bitbucket.org) 和 [Bitbucket Server](https://bitbucket.org/product/enterprise) 将其分支保护功能称为_代码洞察（code insights）_。有关 Bitbucket 代码洞察和配置 PR 要求的更多信息，请参阅 [Bitbucket 文档](https://support.atlassian.com/bitbucket-cloud/docs/code-insights/)。
- [GitHub](https://github.com) 和 [GitHub Enterprise](https://github.com/enterprise) 将其分支保护功能称为_状态检查（status checks）_。有关 GitHub 状态检查和配置 PR 要求的更多信息，请参阅 [GitHub 文档](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks)。
- [GitLab](https://gitlab.com) 和[自行管理的 GitLab 实例](https://about.gitlab.com/install)不附带用于阻止合并含有错误的 PR 的分支保护功能，而只会显示构建状态信息。这是 GitLab 和自行管理的 GitLab 实例的限制，并非仅限于 Xcode Cloud。

> [!note] 注意
> 若要配置 PR 要求，你需要具备最初将 Xcode Cloud 连接到 Git 仓库时所需的同等权限或角色。有关所需权限和角色的信息，请参阅[使用远程源代码控制仓库](setting-up-your-project-to-use-xcode-cloud.md#Use-a-remote-source-control-repository)。

## 配置要求

若要要求 Xcode Cloud 构建或操作成功后才能合并 PR：

1. 配置一个会针对 PR 更改启动新构建的工作流程。有关更多信息，请参阅[针对拉取请求的更改启动构建](configuring-start-conditions.md#Start-builds-for-changes-to-a-pull-request)。
2. 前往 SCM 提供商网站的配置部分，并按照说明为 PR 添加要求。

例如，配置一个针对 PR 的每项更改启动构建并执行测试和归档操作的 Xcode Cloud 工作流程。在 SCM 提供商的网站上，要求 Xcode Cloud 构建成功，以确保目标分支只接收经过验证的更改。或者，要求归档操作成功，并允许在测试操作失败时仍合并 PR。这种配置的常见使用场景是功能开发期间：即使面向功能分支的 PR 会导致单元测试失败，你也认为可以合并。

## 另请参阅

### 源代码管理

- [源代码管理设置](source-code-management-setup.md) — 允许 Xcode Cloud 访问你的 Git 仓库。
