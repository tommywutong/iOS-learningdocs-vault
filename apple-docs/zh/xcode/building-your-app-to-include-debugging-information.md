---
title: 构建包含调试信息的 App
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/building-your-app-to-include-debugging-information
source_url: 'https://developer.apple.com/documentation/xcode/building-your-app-to-include-debugging-information'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/building-your-app-to-include-debugging-information.json'
content_hash: 'sha256:37b39b1671c9d07c'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md)

# 构建包含调试信息的 App

<sub>文章</sub>

配置 Xcode，使其生成用于调试和崩溃报告的符号信息。

## 概述

Xcode 将源代码编译为机器码时，会生成 App 中的符号列表，包括类名、全局变量以及方法和函数名称。这些符号对应其定义所在的文件和行号；这种关联会创建*调试符号（debug symbol）*，使你能够使用 Xcode 中的调试器，或参照崩溃报告所报告的行号。默认情况下，App 的调试构建会将调试符号放在已编译的二进制文件内，而 App 的发布构建则会将调试符号放在配套的调试符号（`dSYM`）文件中，以减小分发版 App 的大小。

App 中的每个二进制文件——主 App 可执行文件、框架和 App 扩展——都有自己的 `dSYM` 文件。已编译的二进制文件及其配套的 `dSYM` 文件通过二者都记录的构建 UUID 绑定在一起。如果使用不同的 Xcode 版本或构建设置从同一源代码构建两个二进制文件，它们的构建 UUID 将不匹配。只有二进制文件和 `dSYM` 文件具有相同的构建 UUID 时，二者才彼此兼容。请保留所分发特定构建的 `dSYM` 文件，并在诊断崩溃报告中的问题时使用它们。

### 使用符号信息构建 App

在构建用于分发的 App 之前，请确认 [Debug Information Format](build-settings-reference.md#Debug-Information-Format) 构建设置已设为 DWARF with dSYM File。这样会生成必需的 `dSYM` 文件，使你能够在 App 发布后诊断崩溃。有关配置项目构建设置的说明，请参阅[配置 target 的构建设置](configuring-the-build-settings-of-a-target.md)。

这些 `dSYM` 文件是发布 App 后进行调试时最常需要的符号文件类型。

### 连同符号信息一起发布 App

归档（archive）App 以进行分发时，Xcode 会收集 App 的所有二进制文件和 `dSYM` 文件，并将它们存储在 Xcode 归档中。

如果通过 App Store 分发 App，或使用 TestFlight 进行 Beta 测试，则可以在将 App 上传到 App Store Connect 时选择包含符号文件。你需要随构建一起上传符号，这样 App Store 才能先将 App 的符号名称添加到崩溃报告中，再将其递送至 Xcode 中的 [Crashes 管理器](https://help.apple.com/xcode/mac/current/#/dev861f46ea8)。如果上传至 App Store 时不包含符号，你仍会通过 Crashes 管理器收到崩溃报告，但其中不含符号名称。如果 Mac 上有正确的 `dSYM` 文件，Xcode 会为这些崩溃报告添加符号名称。有关如何使用 `dSYM` 文件处理崩溃报告，请参阅[使用崩溃报告和设备日志诊断问题](diagnosing-issues-using-crash-reports-and-device-logs.md)。

> [!important] 重要
> 必须保留所分发 App 每个构建的 Xcode 归档。没有此归档，你可能无法通过崩溃报告诊断问题。

有关归档 App 以进行分发的更多信息，请参阅[分发 App 以进行 Beta 测试和发布](distributing-your-app-for-beta-testing-and-releases.md)。

## 另请参阅

### 报告

- [使用崩溃报告和设备日志诊断问题](diagnosing-issues-using-crash-reports-and-device-logs.md) — 使用崩溃报告和设备日志调试 App 问题。
