---
title: Xcode 命令行工具参考
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/xcode-command-line-tool-reference
source_url: 'https://developer.apple.com/documentation/xcode/xcode-command-line-tool-reference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/xcode-command-line-tool-reference.json'
content_hash: 'sha256:9b5d48e318f20cc4'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [命令行工具](command-line-tools.md)

# Xcode 命令行工具参考

<sub>文章</sub>

使用需要你安装 Xcode 并将该 App 设为活跃开发者目录的命令行工具。

## 概述

Xcode 包含一组仅随该 App 附带的命令行工具，例如 `devicectl`、`simctl` 和 `xcodebuild`。你必须先安装 Xcode 并将其设为活跃开发者目录，才能在终端中调用这些命令。

> [!note] 注意
> 有关访问命令行工具文档的更多信息，请参阅[阅读 UNIX 手册页面](../os/reading-unix-manual-pages.md)。

### 自动管理构建和版本号

- **`agvtool`** — 管理构建和版本号。要了解有关此命令的更多信息，请在终端中输入 `man agvtool`。

### 构建项目

- **`xcodebuild`** — 构建 Xcode 项目和工作区。要了解有关此命令的更多信息，请在终端中输入 `man xcodebuild`。

### 调试项目

- **`devicectl`** — 管理与主机连接的设备并进行交互。要了解有关此命令的更多信息，请在终端中输入 `xcrun devicectl help`。
- **`xcdebug`** — 在 Xcode 中启动调试会话。要了解有关此命令的更多信息，请在终端中输入 `xcdebug --help`。

### 编辑文件

- **`xed`** — 在 Xcode App 中打开文件。要了解有关此命令的更多信息，请在终端中输入 `man xed`。

### 识别与合并更改

- **`opendiff`** — 使用 FileMerge 以图形方式比较或合并文件或目录。要了解有关此命令的更多信息，请在终端中输入 `man opendiff`。

### 检查结果包

- **`xcresulttool`** — 读取结果包。要了解有关此命令的更多信息，请在终端中输入 `man xcresulttool`。

### 管理 Instruments 文件

- **`xctrace`** — 录制、导入、导出和符号化 Instruments 的 `.trace` 文件。要了解有关此命令的更多信息，请在终端中输入 `man xctrace`。

### 管理脚本定义

- **`desdp`** — 生成脚本定义（“sdef”）。要了解有关此命令的更多信息，请在终端中输入 `man desdp`。
- **`sdef`** — 提取脚本定义（“sdef”）。要了解有关此命令的更多信息，请在终端中输入 `man sdef`。
- **`sdp`** — 处理脚本定义（“sdef”）。要了解有关此命令的更多信息，请在终端中输入 `man sdp`。

### 管理界面

- **`actool`** — 编译、打印、更新和验证 Asset Catalog。要了解有关此命令的更多信息，请在终端中输入 `man actool`。
- **`ibtool`** — 编译、打印、更新和验证 Interface Builder 文稿。要了解有关此命令的更多信息，请在终端中输入 `man ibtool`。
- **`xcstringstool`** — 从源代码生成字符串表。要了解有关此命令的更多信息，请在终端中输入 `xcrun xcstringstool help`。

### 管理模拟器

- **`simctl`** — 控制模拟器。要了解有关此命令的更多信息，请在终端中输入 `xcrun simctl help`。

## 另请参阅

### 基础

- [安装命令行工具](installing-the-command-line-tools.md) — 使用安装器包或终端 App 安装 Xcode 的命令行工具。
- [配置命令行工具设置](configuring-command-line-tools-settings.md) — 在 Xcode 设置或终端中选择要用于命令行工具的 Xcode 版本。
