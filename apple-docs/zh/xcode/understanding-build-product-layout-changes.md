---
title: 了解 Xcode 中构建产品布局的变化
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/understanding-build-product-layout-changes
source_url: 'https://developer.apple.com/documentation/xcode/understanding-build-product-layout-changes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/understanding-build-product-layout-changes.json'
content_hash: 'sha256:a29760338b598a5b'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [构建系统](build-system.md)

# 了解 Xcode 中构建产品布局的变化

<sub>文章</sub>

## 概述

Xcode 已更改 App 和 App 扩展 target 的未优化构建布局。这项更改让工具和工作流能够共享构建产品，例如让 Previews 执行模式与正常的构建并运行调试构建共享构建产品。这种布局可以节省时间，还有助于防止因工具需要不同类型的构建配置来完成工作而引起正确性问题。

如果你的高级工作流依赖未优化构建中可执行文件的特定布局，必要时可以选择停用默认行为。

### 检查 App bundle

打开 App bundle 时，你会在可执行文件目录中看到两个动态库（`.dylib`）文件。例如，下面是 iOS App bundle 的部分布局：

```
MyApp.app
    - MyApp
    - MyApp.debug.dylib
    - __preview.dylib
    - <other resources>
```

带 `.debug.dylib` 后缀的文件包含你的所有代码，这些代码在发行版配置中会链接为可执行二进制文件。对于正常的构建并运行操作，`MyApp` 可执行文件会变成一个小型桩程序，转而跳到调试 `.dylib` 中的入口点；必要时，它也可以将控制权交给 Xcode 中的 Previews。Previews 使用 `__preview.dylib` 执行这种早期置换。

未优化构建的符号和 Mach-O 分区会链接到这个单独的 `.dylib` 文件中，这与链接到主二进制文件的发行版构建不同。

### 停用调试 dylib

如果你需要扫描自行注入的自定链接器分区，请使用 `OTHER_LDFLAGS` 精确控制输出二进制文件。如果你的工具会扫描二进制文件中的特定符号以进行验证，也可能需要适配这种默认的未优化构建布局。如果无法更改工具来扫描调试 `.dylib`，则可以完全停用这种布局。

当以下三个条件均满足时，构建设置 `ENABLE_DEBUG_DYLIB` 会控制这种模式，且默认为 `YES`：

- 构建 target 是一个 bundle 化的可执行 target
- 已设置 `SWIFT_VERSION`
- `SWIFT_OPTIMIZATION_LEVEL` 设为 `-Onone`

你可以通过向该特定 target 添加 `ENABLE_DEBUG_DYLIB=NO` 来覆盖此行为。这项覆盖按 target 生效，并非用于整个工作区。它只会影响可执行 target。

停用后，该 target 将无法使用 Previews。对于与可执行 target 分开的框架和软件包，Previews 仍然可以正常工作。如果主可执行 target 必须停用这项功能，你仍应继续对依赖 target 使用 Previews。

如果本文没有解决你的构建问题，请使用 [Feedback Assistant](https://developer.apple.com/bug-reporting/) 提交反馈。

## 另请参阅

### 构建设置

- [配置 target 的构建设置](configuring-the-build-settings-of-a-target.md) — 指定用于编译、链接并从 target 生成产品的选项，并识别从项目或系统继承的设置。
- [向你的项目添加构建配置文件](adding-a-build-configuration-file-to-your-project.md) — 以纯文本文件的形式指定项目构建设置，并为调试构建和发行版构建提供不同的设置。
- [构建设置参考](build-settings-reference.md) — 详细列出各项控制或改变 target 构建方式的 Xcode 构建设置。
- [识别并解决框架模块问题](identifying-and-addressing-framework-module-issues.md) — 使用模块验证器检测并修复框架模块中的常见问题。
