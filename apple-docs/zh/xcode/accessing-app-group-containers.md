---
title: 在现有 macOS App 中访问 App Group 容器
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/accessing-app-group-containers
source_url: 'https://developer.apple.com/documentation/xcode/accessing-app-group-containers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/accessing-app-group-containers.json'
content_hash: 'sha256:595584baad69e87c'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Capabilities](capabilities.md)

# 在现有 macOS App 中访问 App Group 容器

<sub>文章</sub>

确保你的 App 具备 App Group 容器的 entitlement，并且 macOS 能够对其进行授权。

## 概述

在 macOS 15 及后续版本中，即使 App 不具备 App 沙盒化能力，App Group 容器也能为你 App 的本地文件提供 [System Integrity Protection](https://developer.apple.com/documentation/macos-release-notes/macos-15-release-notes#System-Integrity-Protection)。这些 App Group 容器会限制不在该 App Group 内的 App 进行访问。不在该 App Group 内的 App 如果尝试访问 App Group 或 App 数据容器内的位置，会导致系统向用户弹出提示，请求他们的授权。

要确保你使用 App Group 的 App 也具备 System Integrity Protection，你需要确认这些 App 拥有正确的 entitlement，并且 macOS 能够对这些 entitlement 进行授权。关于向 App 添加 App Group 的更多信息，请参阅 [Configuring app groups](configuring-app-groups.md)。

可以使用 App Group 容器的 App 包括：打包在 Bundle 结构中的主可执行文件、App 扩展、App Clip 以及 XPC 服务。

## 为你的 App 添加 App Group 成员身份

确保你的 App target 在 [App Groups Entitlement](../bundleresources/entitlements/com.apple.security.application-groups.md) 中列出了它所属的全部 App Group。你可以使用 Xcode 为你的 App 授予 App Group entitlement。更多详情，请参阅 [Configuring app groups](configuring-app-groups.md)。

一个 App 可以属于多个 App Group，但需遵循以下准则：

- 不同的开发者团队不能使用同一个 App Group。
- 同一个开发者团队可以让该团队签名的多个 App 及其配套进程共用同一个 App Group。

> [!important] 重要
> 在 macOS 上，建议你使用以 `group.` 为前缀的标识符。以 `<Developer team identifier>.<group name>` 为前缀的标识符也受支持，但存在一些限制，详见下方“使用无需预配的 App Group”一节。

### 使用已预配的 App Group

如果你的 App 声明它属于一个以 `group.` 开头的 App Group，你需要在 App 的预配描述文件（provisioning profile）中包含该 Group。

将所有受限 entitlement（包括 App Group entitlement）都包含在该进程的预配描述文件中；这些 entitlement 的值必须与预配描述文件中 entitlement 的值相匹配，并要顾及其中的任何通配符。

你此前为 macOS App 创建的预配描述文件，可能并未包含对 App Group entitlement 的授权。你可以在终端中运行命令 `sudo launchctl procinfo <pid>`，检查 macOS 是否在运行时为你的进程设置了 entitlements validated 标志：

```
% sudo launchctl procinfo `pgrep <your app's executable file name>`
…
code signing info = valid
    …
    entitlements validated
…
```

如果你在 App target 的 Signing & Capabilities 编辑器中勾选了“Automatically manage signing”，并将 `REGISTER_APP_GROUPS` 构建设置设为 `Yes`，Xcode 会自动获取新的预配描述文件。要将预配描述文件应用到守护进程，或应用到你不在 Bundle 中分发的其他可执行文件，请参阅 [Signing a daemon with a restricted entitlement](signing-a-daemon-with-a-restricted-entitlement.md)。

如果你在正确预配 App Group entitlement 时遇到任何问题，请参阅 [Diagnosing Issues with Entitlements](../bundleresources/diagnosing-issues-with-entitlements.md) 以获取诊断帮助。

### 使用无需预配的 App Group

要在 macOS 上使用带有 `<Developer team identifier>.<group name>` 标识符的 App Group，你不需要预配描述文件。系统会检查团队标识符前缀是否与你用来为 App 签名的开发者团队标识符相匹配。你也不需要在开发者网站上注册这些 App Group 标识符。但是，使用这些标识符存在一些限制：

- `<Developer team identifier>.<group name>` 在 iOS、iPadOS、tvOS、visionOS 或 watchOS 上不受支持。
- 钥匙串访问组（Keychain Access Groups）不支持以 `<Developer team identifier>.<group name>` 为前缀的标识符。更多信息，请参阅 [Sharing access to keychain items among a collection of apps](../security/sharing-access-to-keychain-items-among-a-collection-of-apps.md)

## 访问 App Group 容器

当你的 App 成为某个 App Group 的成员后，使用 FileManager API 来获取共享容器的路径。关于访问该数据的更多详情，请参阅 [Access an app group's shared container](configuring-app-groups.md#Access-an-app-groups-shared-container)。

## 另请参阅

### Security

- [Configuring Family Controls](configuring-family-controls.md) — 添加 Family Controls entitlement，为你的 App 及其 Screen Time API App 扩展启用家长控制功能。
- [Configuring the hardened runtime](configuring-the-hardened-runtime.md) — 通过限制对敏感资源的访问并防范常见漏洞利用，保护你 macOS App 运行时的完整性。
- [Configuring the macOS App Sandbox](configuring-the-macos-app-sandbox.md) — 通过限制对文件系统、网络连接等的访问，保护系统资源和用户数据免受受损 App 的侵害。
- [Configuring keychain sharing](configuring-keychain-sharing.md) — 在属于同一开发者的多个 App 之间共享钥匙串项目。
- [Protecting local app data using containers on macOS](protecting-local-app-data-using-containers.md) — 保护你 App 的本地存储数据，使其免遭未经授权的访问和修改。
