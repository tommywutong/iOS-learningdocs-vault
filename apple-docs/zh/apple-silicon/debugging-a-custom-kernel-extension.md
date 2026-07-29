---
title: 调试自定义内核扩展
framework: kernel
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/apple-silicon/debugging-a-custom-kernel-extension
source_url: 'https://developer.apple.com/documentation/apple-silicon/debugging-a-custom-kernel-extension'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/apple-silicon/debugging-a-custom-kernel-extension.json'
content_hash: 'sha256:bea82c7e2d3a4b31'
translated: true
---

> 导航：[技术](../technologies.md) · [Apple silicon](../apple-silicon.md)

# 调试自定义内核扩展

<sub>文章</sub>

配置你的系统，以便从第二台 Mac 调试自定义内核扩展。

## 概述

内核支持系统上的所有其他进程（包括调试器本身），因此你无法使用常规技术来调试内核。如果你开发内核扩展（kext），有以下几种调试方式：

- 将调试信息写入日志，稍后分析日志。
- 使用第二台电脑调试另一台 Mac 上的内核。
- 从内核崩溃中调试或检查内核核心（core）文件。

使用 Kernel Debug Kit 来设置双机调试和一个可选的 core-dump 服务器。使用双机调试，在运行时动态检查 kext 的状态。如果你没有直接将 core-dump 文件保存到用于调试的 Mac 上，core-dump 服务器会通过网络自动捕获它们。

### 安装 Kernel Debug Kit

Kernel Debug Kit（KDK）提供了调试内核所需的工具和支持。这个单独的下载包包含了自定义版本的内核，其中包含额外的断言和错误检查，以帮助你发现问题。

使用 KDK 进行双机调试：

1. 将两台 Mac 连接到同一网络。
2. 在两台 Mac 上以管理员身份登录。
3. 下载与你所调试的 macOS 版本对应的 KDK。
4. 在两台 Mac 电脑上安装 KDK。
5. 在你想要调试的电脑上安装你的 kext（以及相应的内核）。

KDK 包含关于如何在调试期间安装自定义内核的说明。它还提供了设置两台电脑之间连接的详细说明。如需更多信息，请登录并从 [https://developer.apple.com/download/more/](https://developer.apple.com/download/more/) 下载相应的 KDK。

### 调试 Kext

要开始调试会话，指定一台机器为调试机，另一台为目标机。在调试机上的 Terminal 中运行 `lldb`，并使用 `kdp-remote` 命令连接到远程电脑。`kdp-remote` 命令接受主机名或 IP 地址，并创建到相应 Mac 的调试器连接。将目标 Mac 的名称或 IP 地址作为参数传递给该命令。

```other
(lldb) kdp-remote MyComputer.local
```

建立连接后，像调试其他任何进程一样设置断点并单步执行自定义代码。调试器会自动搜索本机上的任何“聚焦”索引目录和 `/Library/Developer/KDKs/` 目录，以获取调试期间使用的符号信息。你可以通过使用包含这些符号的内核文件路径来启动 `lldb`，从而指定内核符号文件的位置。例如：

```other
% lldb /Library/Developer/KDKs/<KDK Version>/System/Library/Kernels/kernel
```

有关双机调试的更多信息，请参阅位于 KDK 的 `/Library/Developer/KDKs/<KDK Version>/` 目录中的 KDK Readme 文件。

.

## 另请参阅

### 内核与驱动

- [安装自定义内核扩展](installing-a-custom-kernel-extension.md) — 使用自定义安装包安装内核扩展，并帮助用户了解安装过程。
