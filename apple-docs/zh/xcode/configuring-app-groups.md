---
title: 配置 App Group
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/configuring-app-groups
source_url: 'https://developer.apple.com/documentation/xcode/configuring-app-groups'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/configuring-app-groups.json'
content_hash: 'sha256:8ee6d289f87ca0f6'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [功能](capabilities.md)

# 配置 App Group

<sub>文章</sub>

让同一开发者创建的多个已安装 App 能够相互通信和共享数据。

## 概述

_App Group_ 允许同一团队开发的多个 App 访问一个或多个共享容器。它还让这些 App 能够通过 Mach IPC、POSIX 信号量和共享内存、UNIX 域套接字以及其他 IPC 机制进行额外的进程间通信（IPC）。在 macOS 中，App Group 可以协助沙盒化 App 之间以及沙盒化 App 与非沙盒化 App 之间的通信。App 可以属于一个或多个 App Group。你还可以使用 App Group 在 App 扩展或轻 App 与其宿主 App 之间共享数据。

创建 App Group 前，请按照[添加功能](adding-capabilities-to-your-app.md#Add-a-capability)中的步骤，将 [App Groups Entitlement](../bundleresources/entitlements/com.apple.security.application-groups.md) 添加到 App 的 target。

![](../../../attachments/593f221f639b7c3d4719cc4480788c2a/app-groups@2x.png)

<sub>Xcode 的 Capabilities 资源库截图，左侧列出可用功能，右侧显示信息面板。列表展示了从 App Groups 到 Custom Network Protocol 的一系列功能，其中 App Groups 功能处于选中状态。信息面板中的文字说明，App Groups 允许访问由多个相关 App 共享的组容器，并允许这些 App 之间进行某些额外的进程间通信。</sub>

### 创建 App Group

将 App Groups 功能添加到你的 App 后，Xcode 会从你的开发者账户获取所有现有组，并在该功能的区域中显示它们。使用 App Groups 列表下方的 Refresh 按钮，可以随时重新获取账户中的组。每个开发者账户最多可以注册 1,000 个 App Group。

要注册 App Group，请参阅[注册 App Group](https://developer.apple.com/help/account/manage-identifiers/register-an-app-group)。iOS、iPadOS、tvOS、visionOS 和 watchOS App 都需要注册 App Group。

选中列表中一个或多个组的复选框，即可启用这些组并将你的 App 添加为其成员。反之，取消选中某个组的复选框，即可撤销 App 的成员资格。

要为你的 App 创建 App Group，请执行以下操作：

1. 点按 App Groups 列表下方的添加按钮（+）。
2. 在出现的对话框中输入容器 ID。容器 ID 必须以 `group.` 开头，后接一个自定字符串。
3. 点按 OK 保存新的 App Group。

![](../../../attachments/d9955cd1f522778ccf573c0ed08ce893/add-app-group@2x.png)

<sub>Xcode 在你点按添加按钮后显示的 Add a new container 对话框截图。对话框说明，如果指定名称的容器尚不存在，Xcode 将创建一个新容器，将其添加到你的 App ID，并将新容器添加到 App 的 entitlements 中。文本框中包含值 group.com.example.mygroup。</sub>

Xcode 会在 App Groups 列表中自动选中新 App Group；此选择表示你的 App 现在是该 App Group 的成员。

![](../../../attachments/c11dad97a87ea3b1a10f8709275065f3/app-group-other@2x.png)

<sub>将 App Groups 功能添加到 target 后的截图。组列表包含一个名为 group.com.example.mygroup 的 App Group。</sub>

> [!note] 注意
> 你还可以使用命名约定 `<开发者团队 ID>.<组名称>` 创建 macOS App Group。使用此命名方案时，macOS 会检查尝试访问 App Group 容器的进程代码签名中，是否包含与 App Group 容器 ID 相同的 `Developer-Team-ID`。

### 访问 App Group 的共享容器

当你的 App 成为 App Group 的成员后，可以使用多种 API 读取和写入该组共享容器中的数据，例如：

- 使用 [init(suiteName:)](<../foundation/userdefaults/init(suitename_).md>) 方法访问 App Group 的共享 UserDefaults 数据库，从而共享偏好设置和其他有限数据。
- 调用 [containerURL(forSecurityApplicationGroupIdentifier:)](<../foundation/filemanager/containerurl(forsecurityapplicationgroupidentifier_).md>) 方法获取 App Group 共享容器的物理位置，之后即可使用该位置读取和写入数据。
- 在后台 URL 会话的配置中设置 [sharedContainerIdentifier](../foundation/urlsessionconfiguration/sharedcontaineridentifier.md) 属性，以将文件直接下载到 App Group 的共享容器中。

你还可以将标识符以 `group.` 前缀开头的 App Group 用作钥匙串访问组。有关更多信息，请参阅[在一组 App 之间共享钥匙串项目的访问权限](../security/sharing-access-to-keychain-items-among-a-collection-of-apps.md)。

## 另请参阅

### 数据管理

- [配置关联域](configuring-an-associated-domain.md) — 在你的 App 与网站之间建立双向关联，以启用通用链接、接力、轻 App 和共享网页凭据。
- [配置 iCloud 服务](configuring-icloud-services.md) — 在不同设备上运行的多个 App 实例之间共享用户或 App 数据。
