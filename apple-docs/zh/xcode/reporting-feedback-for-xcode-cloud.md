---
title: 报告 Xcode Cloud 反馈
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/reporting-feedback-for-xcode-cloud
source_url: 'https://developer.apple.com/documentation/xcode/reporting-feedback-for-xcode-cloud'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/reporting-feedback-for-xcode-cloud.json'
content_hash: 'sha256:e6c844aeb6675251'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md)

# 报告 Xcode Cloud 反馈

<sub>文章</sub>

针对使用 Xcode Cloud 构建时遇到的问题提供反馈。

## 概述

你可以直接从 Report navigator 中的某次构建提交关于 Xcode Cloud 的反馈。当你从某次构建提交反馈时，系统会用该构建的相关上下文信息预先填充反馈表单，供 Apple 用于对 bug 进行分诊。

预先填充的信息包括描述该构建的详细信息，以及可能为 bug 成因提供线索的日志和构建产物。

> [!important] 重要
> 这些产物和日志可能包含个人数据和知识产权内容。你可以在提交反馈之前选择不提供其中任何或全部文件。

### 发起反馈

如果要报告与特定构建无关的反馈，请在 Xcode 中选择 Help \> Provide Feedback，或启动 Feedback Assistant App。如果你需要报告包含特定构建上下文的反馈：

1. 在 Report navigator 的大纲视图中定位到指定的构建编号。
2. Control 点按该构建编号以打开上下文菜单。
3. 选择 Send Feedback。

另外，也可以在 Xcode 中某次构建内的问题横幅上点按 Report Issue 按钮来发起报告。

通过从特定构建发起反馈，Xcode 会用相关信息预先填充反馈表单，包括描述该构建的详细信息（例如团队名称、产品名称和构建编号），以及与分诊构建相关问题有关的系统生成的日志和产物。

### 查看附件

由 Xcode Cloud 发起的命令所生成的文本日志、result bundle 以及 sysdiagnose 日志，在分诊与构建相关的问题时非常有用。请提供这些日志以帮助让 bug 更具可操作性，但在提交反馈之前请先查看这些日志。

要查看某个特定附件，请点按 Attachments 下所列条目右侧的放大镜图标。这会打开 Finder 并定位到该附件在磁盘上的位置。

总体而言，日志和构建产物分为 5 种不同类型：

- **可执行构建产物** — 这些是为在特定类型的设备或模拟器上运行而构建的 App 或其测试所产生的产物。这类产物包括：产品归档和测试产品。产品归档，例如 App Store 归档导出文件，代表你安装到设备上的 App。而测试产品则代表测试过程中运行的可执行文件。
- **来自你所提供脚本的文本日志** — 这些是你所提供自定脚本的日志。这些日志可能包含网络请求、所运行子命令的条目，以及用于向其他服务进行身份验证的凭据。
- **由 Xcode Cloud 发起的命令所生成的文本日志** — Xcode Cloud 在处理构建时依赖某些命令行工具。此类命令行工具的一个示例是 `xcodebuild`，Xcode Cloud 用它来归档导出、构建产品并运行测试。这些日志包含命令行工具生成的输出内容和网络请求。这些日志可能包含来自产品源代码的信息，例如类和方法的名称。
- **Result bundle** — 这些是 `xcodebuild` 子命令（例如 `archive`、`build` 和 `test`）生成的特殊产物。Result bundle 包含 `xcodebuild` 子命令执行期间发生的事件摘要，且可能包含知识产权相关的痕迹。要了解关于 bundle 的更多信息，请参阅 [Bundle](../foundation/bundle.md)。
- **Sysdiagnose 日志** — 这些是 Xcode Cloud 在异常场景（例如 Simulator 或虚拟机崩溃）下生成的特殊产物。Sysdiagnose 日志包含来自不同 Apple 平台上可用诊断工具的日志集合。这些日志提供了崩溃发生前一刻机器状态的相关上下文，例如打开的文件句柄数量以及各个进程的状态。

### 移除附件并提交反馈

只包含你希望共享的附件。要移除你不想共享的附件：

1. 点按 Attachments 下所列条目旁边的垃圾桶图标。
2. 在 Feedback Assistant 对话框中选择 Remove 以确认移除。

当报告已反映出你想要共享的反馈内容时，点按 Submit 按钮将反馈发送给 Apple。

## 另请参阅

### Troubleshooting

- [Resolving common configuration and build issues](resolving-common-configuration-and-build-issues.md) — 查看常见的配置和构建问题，并了解如何解决这些问题。
- [Resolve GitHub Enterprise connection issues](resolve-github-enterprise-connection-issues.md) — 验证 Xcode Cloud 能否访问你的 GitHub Enterprise 仓库，并修复配置问题。
