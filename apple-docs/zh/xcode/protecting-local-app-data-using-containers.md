---
title: 在 macOS 上使用容器保护本地 App 数据
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/protecting-local-app-data-using-containers
source_url: 'https://developer.apple.com/documentation/xcode/protecting-local-app-data-using-containers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/protecting-local-app-data-using-containers.json'
content_hash: 'sha256:2cf17830f6bb5c44'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [能力](capabilities.md)

# 在 macOS 上使用容器保护本地 App 数据

<sub>文章</sub>

保护 App 的本地存储数据，使其免遭未经授权的访问和修改。

## 概述

[App 沙盒化](../security/app-sandbox.md)会自动保护 App 的数据。系统为具备 App 沙盒化能力的 App 创建的 App 数据容器提供[系统完整性保护](https://support.apple.com/en-us/102149)，有助于防止潜在恶意软件修改受保护的文件和文件夹。

在 macOS 15 及更高版本中，即使 App 不具备 App 沙盒化能力，App Group 容器也会为该 App 的本地文件提供系统完整性保护。这些 App Group 容器会限制不属于该 App Group 的任何 App 进行访问。任何不在 App Group 中的 App 如果尝试访问由 App Group 或 App 数据容器保护的位置，系统都会提示用户授权访问。有关更多信息，请参阅 [macOS Sequoia 15 发布说明](../macos-release-notes/macos-15-release-notes.md)中的“系统完整性保护”部分。

> [!important] 重要
> 对于任何不具备 App 沙盒化能力的 App，请将 App Group 容器用作主要本地存储位置，以帮助保护私有数据。这些 App 包括：以捆绑包结构封装的主可执行文件、App 扩展、轻 App、系统扩展和 XPC 服务。

## 为 App 添加 App Group 成员资格

按照[配置 App Group](configuring-app-groups.md)中的步骤，将 [App Groups entitlement](../bundleresources/entitlements/com.apple.security.application-groups.md) 添加到 App 的 target。由同一开发者团队签名的多个 App 和支持进程可以共享同一 App Group。

有关诊断添加 App Groups entitlement 时遇到的问题的信息，请参阅[诊断 entitlement 问题](../bundleresources/diagnosing-issues-with-entitlements.md)。

## 访问 App Group 容器

当 App 成为 App Group 成员后，你可以使用多种 API 在该组的共享容器中读取和写入数据。有关更多详细信息，请参阅[访问 App Group 的共享容器](configuring-app-groups.md#Access-an-app-groups-shared-container)。

## 另请参阅

### 安全性

- [配置 Family Controls](configuring-family-controls.md) — 添加 Family Controls entitlement，以便在 App 及其 Screen Time API App 扩展中启用家长控制功能。
- [配置强化运行时](configuring-the-hardened-runtime.md) — 通过限制对敏感资源的访问并防止常见漏洞利用，保护 macOS App 的运行时完整性。
- [配置 macOS App 沙盒化](configuring-the-macos-app-sandbox.md) — 通过限制对文件系统、网络连接等的访问，保护系统资源和用户数据免受受侵害 App 的影响。
- [配置钥匙串共享](configuring-keychain-sharing.md) — 在属于同一开发者的多个 App 之间共享钥匙串项目。
- [在现有 macOS App 中访问 App Group 容器](accessing-app-group-containers.md) — 确保 App 具有 App Group 容器 entitlement，并且 macOS 能够对其进行授权。
