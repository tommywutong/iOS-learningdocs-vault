---
title: GameSave
framework: GameSave
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/gamesave
source_url: 'https://developer.apple.com/documentation/gamesave'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/gamesave.json'
content_hash: 'sha256:c771c4bd762597c0'
translated: true
---

> 导航：[Technologies](technologies.md)

# GameSave

<sub>框架</sub>

在 iCloud 中存储和同步你的应用程序的存档文件。

## 概述

GameSave 使用 iCloud Drive 在设备之间同步你的应用程序的存档数据。该框架提供了一组 API，用于向某个目录读写一个或多个文件，同时将 iCloud 的相关概念抽象出来。它会处理常见的存档同步场景，例如冲突解决和离线游戏。此外，它还为这些典型场景提供了一组便捷的界面提醒。当设备未登录 iCloud Drive 时，GameSave 也支持本地保存。

> [!important] 重要
> 若要让 GameSave 将游戏数据存储在玩家的 iCloud 账户中，你需要提供一个标识符，用于标识存储数据的 iCloud 容器。请在你的项目中添加 iCloud 功能，并勾选 iCloud Documents 复选框。更多信息请参阅 [配置 iCloud 服务](xcode/configuring-icloud-services.md)。

## 主题

### 同步目录

- [GameSaveSyncedDirectory](gamesave/gamesavesynceddirectory.md) — 用于存放游戏存档数据的云同步目录。

### 错误域

- [GameSaveErrorDomain](gamesave/gamesaveerrordomain.md) — GameSave 错误的错误域名称。

### 同步目录（Objective-C）

- [GSSyncedDirectory](gamesave/gssynceddirectory.md) — 用于存放游戏存档数据的云同步目录。
