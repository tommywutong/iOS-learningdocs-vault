---
title: 解决 GitHub Enterprise 连接问题
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/resolve-github-enterprise-connection-issues
source_url: 'https://developer.apple.com/documentation/xcode/resolve-github-enterprise-connection-issues'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/resolve-github-enterprise-connection-issues.json'
content_hash: 'sha256:1da815c681d8dd47'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md)

# 解决 GitHub Enterprise 连接问题

<sub>文章</sub>

验证 Xcode Cloud 能否访问你的 GitHub Enterprise 仓库，并修复配置问题。

## 概述

Xcode Cloud 需要能够访问你的 Git 仓库，才能检出你的代码并构建你的 App。你可以在创建第一个工作流程时授予此访问权限；或者在企业场景中，由你团队的管理员在你开始使用 Xcode Cloud 之前为你配置好这个连接。

如果你在使用 GitHub Enterprise 的大型团队中工作，你可能无法控制团队 GitHub Enterprise 设置的配置。因此，你可能会遇到 Xcode Cloud 无法访问你的 Git 仓库、也无法启动构建的问题。在这种情况下，Xcode 和 App Store Connect 会显示提示配置或权限问题的消息。

出现这些问题的常见原因包括：

- 你 GitHub Enterprise 实例的管理员更改了权限；例如更改了 Xcode Cloud 用于访问你仓库的 GitHub Enterprise App 的权限。
- 你 GitHub Enterprise 实例的回调 URL 发生了变化。
- Xcode Cloud 用于连接你仓库的 GitHub Enterprise App 收到了更新，需要更新权限。

修复权限和配置问题的方法取决于你的 GitHub Enterprise 实例，但重新启用 Xcode Cloud 与你仓库连接的常见方法包括：

- 前往你 GitHub Enterprise 团队的设置页面，查看是否有尚未处理的权限更新请求。
- 前往管理你 Git 仓库访问权限的 GitHub App 的设置页面，验证回调 URL。此外，请验证已配置的权限和事件是否与下方的表格和列表相符。

所需权限：

| 类型 | 值 |
|---|---|
| Checks | Read and write |
| Contents | Read-only |
| Metadata | Read-only |
| Pull Requests | Read-only |
| Statuses | Read and write |

所需事件：

- Create
- Check Run
- Check Suite
- Delete
- Pull Request
- Pull Request Review
- Push
- Repository

作为最后手段，你可以按照[在 Xcode Cloud 中断开你的 Git 仓库连接](removing-your-project-from-xcode-cloud.md#Disconnect-your-Git-repository-in-Xcode-Cloud)中的描述，断开 Xcode Cloud 与你 GitHub Enterprise 仓库的连接，并按照[移除个人访问令牌或 App](removing-your-project-from-xcode-cloud.md#Remove-personal-access-tokens-or-apps)中的描述，卸载守护你 GitHub Enterprise 仓库访问权限的 App。不过，之后你需要重新将 GitHub Enterprise 连接到 Xcode Cloud，并在 GitHub Enterprise 上为你的每个仓库配置访问权限——如果你的仓库和项目很多，这可能会花费相当长的时间。

> [!important] 重要
> 请确保不要删除你的 Xcode Cloud 数据和工作流程。如果你这样做，你将失去对工作流程和构建数据的访问权限，并且需要为你的项目重新配置 Xcode Cloud 工作流程。

## 另请参阅

### 疑难解答

- [解决常见的配置和构建问题](resolving-common-configuration-and-build-issues.md) — 查看常见的配置和构建问题，并了解如何解决它们。
- [为 Xcode Cloud 报告反馈](reporting-feedback-for-xcode-cloud.md) — 就你在使用 Xcode Cloud 构建时遇到的问题提供反馈。
