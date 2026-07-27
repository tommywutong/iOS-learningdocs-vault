---
title: 将 Xcode Cloud 连接到 Bitbucket Server
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/connecting-xcode-cloud-to-bitbucket-server
source_url: 'https://developer.apple.com/documentation/xcode/connecting-xcode-cloud-to-bitbucket-server'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/connecting-xcode-cloud-to-bitbucket-server.json'
content_hash: 'sha256:d0f7626e9b193260'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md) · [Source code management setup](source-code-management-setup.md)

# 将 Xcode Cloud 连接到 Bitbucket Server

<sub>文章</sub>

允许 Xcode Cloud 访问你的 Bitbucket Server 仓库。

## 概述

首次配置项目或工作区以使用 Xcode Cloud 时，你需要允许 Xcode Cloud 访问你的 Git 仓库。当你对代码库进行更改时，Xcode Cloud 会用这个访问权限自动构建和测试你的代码。

首次将项目或工作区配置为使用 Xcode Cloud 的人，必须拥有该仓库在 Bitbucket Server 上的 _administrator_ 权限。如果你没有这个权限，请参阅[将 Xcode Cloud 连接到由管理员管理的 Git 仓库](configuring-xcode-cloud-for-your-team.md#Connect-Xcode-Cloud-to-an-admin-managed-Git-repository)。

要允许 Xcode Cloud 访问你在 [Bitbucket Server](https://bitbucket.org/product/enterprise) 上的仓库：

1. 按照[配置你的第一个 Xcode Cloud 工作流](configuring-your-first-xcode-cloud-workflow.md)中所述，配置你的项目或工作区以使用 Xcode Cloud，并创建你的第一个工作流。Xcode 会分析你的项目，识别你使用的 SCM 提供方，然后在“授予对你源代码的访问权限”表单中显示你 Bitbucket Server 主机的 URL。
2. 点按“授予访问权限”。Xcode 会打开你的浏览器，将你带到 [App Store Connect](https://appstoreconnect.apple.com) 网站。
3. 在 App Store Connect 网站上输入你 Bitbucket Server 实例的主机名。当它分析你的项目时，Xcode Cloud 会获知你 Bitbucket Server 实例的主机名，并为你在网站上填好对应字段。
4. 检查填入的主机名是否正确（例如，确保其中包含所需的端口），然后点按“注册”。
5. 点按“your Bitbucket Server host”。这会打开你的 Bitbucket Server 实例，并显示你账户的“Personal access tokens”部分。不要关闭显示 Xcode Cloud 网页的标签页或窗口。
6. 点按“Create a token”，开始创建一个供 Xcode Cloud 用来访问你仓库的个人访问令牌。
7. 为访问令牌输入一个便于识别的名称；例如 `Xcode Cloud`。
8. 将令牌配置为对项目具有 _Read_ 权限、对仓库具有 _Admin_ 权限。
9. 创建令牌，并在继续之前务必将其复制并存放到安全的地方。Bitbucket Server 不会再次显示这条信息。例如，你可以在“钥匙串访问”中创建一条安全备注，把令牌添加进去。
10. 切换回显示 App Store Connect 网站的浏览器标签页或窗口，也就是你开始将 Xcode Cloud 连接到 Bitbucket Server 的地方。
11. 将你的个人访问令牌粘贴到对应字段中。
12. 点按“注册”。App Store Connect 会指明你已成功将 Xcode Cloud 连接到 Bitbucket Server。
13. 返回 Xcode。它会指明 Xcode Cloud 可以访问你的源代码。
14. 点按“下一步”，完成第一个工作流的配置，并开始你的第一次构建。

## 另请参阅

### Bitbucket Cloud 与 Bitbucket Server

- [将 Xcode Cloud 连接到 Bitbucket Cloud](connecting-xcode-cloud-to-bitbucket-cloud.md) — 允许 Xcode Cloud 访问你的 Bitbucket Cloud 仓库。
