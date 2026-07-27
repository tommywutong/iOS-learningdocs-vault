---
title: 将 Xcode Cloud 连接到自托管的 GitLab 实例
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/connecting-xcode-cloud-to-a-self-managed-gitlab-instance
source_url: 'https://developer.apple.com/documentation/xcode/connecting-xcode-cloud-to-a-self-managed-gitlab-instance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/connecting-xcode-cloud-to-a-self-managed-gitlab-instance.json'
content_hash: 'sha256:e23ed18f5b61887e'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md) · [Source code management setup](source-code-management-setup.md)

# 将 Xcode Cloud 连接到自托管的 GitLab 实例

<sub>文章</sub>

允许 Xcode Cloud 访问你自托管的 GitLab 仓库。

## 概述

首次配置项目或工作区以使用 Xcode Cloud 时，你需要允许 Xcode Cloud 访问你的 Git 仓库。当你对代码库进行更改时，Xcode Cloud 会用这个访问权限自动构建和测试你的代码。

首次配置项目以使用 Xcode Cloud 的人，必须拥有该 GitLab 仓库的 _maintainer_ 角色。如果你没有这个角色，请参阅[将 Xcode Cloud 连接到由管理员管理的 Git 仓库](configuring-xcode-cloud-for-your-team.md#Connect-Xcode-Cloud-to-an-admin-managed-Git-repository)。

要允许 Xcode Cloud 访问你[自托管的 GitLab](https://about.gitlab.com/install) 仓库：

1. 按照[配置你的第一个 Xcode Cloud 工作流](configuring-your-first-xcode-cloud-workflow.md)中所述，配置你的项目或工作区以使用 Xcode Cloud，并创建你的第一个工作流。Xcode 会分析你的项目，识别你使用的 SCM 提供方，然后在“授予对你源代码的访问权限”表单中显示你自托管 GitLab 实例的 URL。
2. 点按“授予访问权限”。Xcode 会打开你的浏览器，将你带到 [App Store Connect](https://appstoreconnect.apple.com) 网站。
3. 选择自托管 GitLab，创建一个用于管理你 GitLab 仓库访问权限的 GitLab App。
4. 复制重定向 URI，然后点按“your GitLab Self-hosted host”打开你 GitLab 实例的网站。它会显示创建新 GitLab App 的页面。
5. 为 GitLab App 输入一个便于识别的名称；例如 `Xcode Cloud`。
6. 将 Xcode Cloud 的重定向 URI 粘贴到 GitLab 网页上创建 GitLab App 时的相应字段中。
7. 勾选 _api_、_read_repository_ 和 _read_user_ 旁边的复选框，允许该 App 访问这些范围。
8. 保存该 App。
9. 复制 GitLab App 的 Application ID，粘贴到 App Store Connect 网站上对应的字段中，然后对 Application Secret 重复此步骤。
10. 在 App Store Connect 网站上点按“注册”，将 Xcode Cloud 连接到该 GitLab App。
11. 点按“在 GitLab 中授权”打开你 GitLab 实例的网站，并为你的仓库安装该 GitLab App。
12. 查看 Xcode Cloud 请求的权限，并允许其访问你的账户。这会带你返回 App Store Connect 网站，该网站会指明你已成功将 Xcode Cloud 连接到你自托管的 GitLab 实例。
13. 返回 Xcode。它会指明 Xcode Cloud 可以访问你的源代码。
14. 点按“下一步”，完成第一个工作流的配置，并开始你的第一次构建。

## 另请参阅

### GitLab

- [将 Xcode Cloud 连接到 GitLab](connecting-xcode-cloud-to-gitlab.md) — 允许 Xcode Cloud 访问你的 GitLab 仓库。
