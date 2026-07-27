---
title: 获取崩溃报告和诊断日志
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/acquiring-crash-reports-and-diagnostic-logs
source_url: 'https://developer.apple.com/documentation/xcode/acquiring-crash-reports-and-diagnostic-logs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/acquiring-crash-reports-and-diagnostic-logs.json'
content_hash: 'sha256:49ced959c2409b5d'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Diagnosing issues using crash reports and device logs](diagnosing-issues-using-crash-reports-and-device-logs.md)

# 获取崩溃报告和诊断日志

<sub>文章</sub>

从 App Store、TestFlight 以及直接从设备收集崩溃报告和设备日志。

## 概述

在你的 App 分发给客户之后，可以通过收集崩溃报告和诊断日志来了解改进它的方法。如果某位客户报告了你 App 的一个问题，请使用 Xcode 中的 Crashes organizer 获取有关该问题的报告，具体做法见[报告是如何生成的？](https://help.apple.com/xcode/mac/current/#/dev675635e70) 如果 Crashes organizer 不包含你需要的诊断信息，或者你无法使用它，客户可以从他们的设备收集日志，并直接与你分享以解决问题。拿到崩溃报告后，你可能需要为该崩溃报告添加可识别的符号信息——更多信息请参阅 [Adding identifiable symbol names to a crash report](adding-identifiable-symbol-names-to-a-crash-report.md)。

对于非崩溃类的问题，请查看操作系统的控制台日志，找出用于诊断问题根源的重要信息。

### 从 TestFlight 和 App Store 收集崩溃报告

TestFlight 和 App Store 会为你 App 每个已提交的版本收集崩溃报告。如果你在向 App Store 提交构建版本时包含了符号信息，崩溃报告就会自动包含可识别的符号信息。推荐设置请参阅 [Building your app to include debugging information](building-your-app-to-include-debugging-information.md)。

Crashes organizer 会呈现来自那些分享了诊断和使用信息的客户的崩溃报告，具体说明见[与开发者共享崩溃、能耗和指标数据](https://help.apple.com/xcode/mac/current/#/deve2819c518)。无论设备的诊断和使用数据共享设置如何，你 App 的 TestFlight 用户都会自动与你分享崩溃报告。如果 Crashes organizer 中没有出现任何崩溃报告，请参阅 [organizer 中未出现崩溃、能耗或指标报告时该怎么办](https://help.apple.com/xcode/mac/current/#/dev9a80ab71d)，以启用从你客户处收集崩溃报告的功能。

以下几种崩溃报告类型无法通过 Crashes organizer 获取，但可以通过其他方式获取。请参阅[将崩溃报告和设备日志传输到 Mac](acquiring-crash-reports-and-diagnostic-logs.md#Transfer-crash-reports-and-device-logs-to-a-Mac)和[在设备上定位崩溃报告和内存日志](acquiring-crash-reports-and-diagnostic-logs.md#Locate-crash-reports-and-memory-logs-on-the-device)。

- 看门狗（watchdog）事件，例如由 App 启动时间过慢引起的事件
- 无效代码签名导致的崩溃
- 热事件（thermal event），即设备因某个 App 占用过多 CPU 而过热
- Jetsam 事件，即某个 App 的内存使用量过高

### 获取针对崩溃问题的编码助手建议

在 Crashes organizer 中选择一份崩溃报告后，点按检查器中的 Generate Recommendations，即可在 Xcode 中获得辅助分诊。选择一个工作区后，Xcode 会打开你的项目，并将崩溃的调用栈回溯粘贴到编码助手中，帮助你找出并修复崩溃的根本原因。

![](../../../attachments/d6c43e06fa82d84dea841181b1f81896/acquiring-crash-reports-and-diagnostic-logs-1@2x.png)

<sub>截图显示了 Xcode Organizer 中 Crashes reports 面板检查器里的 Generate Recommendations 按钮。</sub>

### 将崩溃报告和设备日志传输到 Mac

如果你可以访问你 App 崩溃所在的设备，可以通过将该设备连接到你的 Mac 来传输诊断日志。你可以使用 Xcode 中的 Devices and Simulators 窗口查看这些日志，具体说明见[关于 Devices and Simulators 窗口](https://help.apple.com/xcode/mac/current/#/dev7b20475ba)。

如果某位客户报告了一次崩溃，他们可以将该崩溃报告传输到 Mac 或 Windows 电脑上。请参阅[在 Mac 或 Windows 电脑上查找设备的崩溃和能耗日志](https://help.apple.com/xcode/mac/current/#/dev0f3181c2c)。

### 在设备上定位崩溃报告和内存日志

如果某位客户报告了你 App 中的一次崩溃，而你在 Crashes organizer 中没有对应的崩溃报告，请让该客户从他们的设备将崩溃报告通过电子邮件发给你。

> [!note] 注意
> 来自 watchOS 的崩溃报告，可以在配对的 iPhone 上获取。

要为 iOS、iPadOS、tvOS、visionOS 和 watchOS App 定位崩溃报告并通过电子邮件发送：

1. 在设备的“设置”中打开“分析与改进”部分。参阅[与 Apple 共享分析、诊断和使用信息](https://support.apple.com/en-us/HT202100)。
2. 轻点“分析数据”。
3. 找到你 App 对应的日志。对于崩溃报告，日志名称以 `<AppBinaryName>_<DateTime>` 开头；对于高内存占用导致的崩溃，则以 `JetsamEvent_<DateTime>` 开头。
4. 选择所需的日志。
5. 轻点分享图标，选择“邮件”将崩溃报告作为邮件附件发送。

要为 macOS 和 Mac Catalyst App 定位崩溃报告并通过电子邮件发送：

1. 从访达的 Applications \> Utilities 中打开 Console App。
2. 选择 _Crash Reports_。
3. 在列表中找到你 App 的崩溃报告。日志按你 App 的二进制文件名列出。
4. 右键点按所需日志的文件名。
5. 选择 Reveal in Finder。
6. 将访达中显示的文件拖到“邮件”中，将崩溃报告作为邮件附件发送。

### 在调试期间创建崩溃报告

如果你在使用 Xcode 调试 App 时遇到崩溃，调试器会拦截该崩溃，以便你检查 App 的状态。如果你想为该问题收集完整的崩溃报告，请分离调试器——可以使用 Xcode 中的 Debug \> Detach 菜单项，也可以在调试控制台中执行 `detach` 命令。这样可以让 App 完成崩溃过程，并让操作系统生成崩溃报告。有关如何收集崩溃报告文件，请参阅[在设备上定位崩溃报告和内存日志](acquiring-crash-reports-and-diagnostic-logs.md#Locate-crash-reports-and-memory-logs-on-the-device)。

### 访问设备控制台日志

如果某位客户报告了你 App 中一个非崩溃类的问题，请查看该设备的控制台日志以获取有关该问题的更多信息。

要访问某台设备的控制台日志：

1. 对于 iOS、iPadOS、tvOS 和 visionOS 的问题，请将设备连接到你的 Mac。对于 watchOS 的问题，请将日志记录描述文件安装到配对的 iPhone，然后将该 iPhone 连接到你的 Mac。参阅 [Profiles and Logs](https://developer.apple.com/bug-reporting/profiles-and-logs/?name=sysdiagnose&platform=watchos) 下载该描述文件。对于 macOS 的问题，请继续下一步。
2. 在 Mac 上，从访达的 Applications \> Utilities 中打开 Console App。
3. 在 Console 边栏中选择该设备。
4. 重现该问题，并记下确切的时间。
5. 查找该重现时间前后与该问题相关的日志。
6. 使用日志中的信息作为线索，进一步指导你对该问题的调查。

### 分享崩溃报告以获得帮助

如果你在调试某次崩溃时需要帮助，请从 Xcode organizer 中提取崩溃报告以便分享。在 Xcode organizer 中，按住 Control 点按该崩溃，选择 Show in Finder，即可在访达中显示 Xcode crashpoint 文档（`.xccrashpoint`）。然后，按住 Control 点按该文档，选择 Show Package Contents。在随后出现的访达窗口中，找到与你正在调查的崩溃相匹配的崩溃报告（`.crash`）。

在 [Developer Forums](https://developer.apple.com/forums/) 发帖时，请将完整的崩溃报告作为文本附件包含进去。这样可以保留全部诊断信息，同时避免讨论帖变得杂乱。如果你想突出显示某个特定部分，请使用三重反引号（```）代码块，将该片段包含在正文中。

请尽可能使用 Apple 的崩溃报告，因为第三方崩溃报告可能会遗漏必要的信息。分享崩溃报告之前，请务必对其进行符号化，否则该报告会显示十六进制地址，而不是函数名和行号，这会让诊断变得更加困难。有关符号化信息，请参阅 [Adding identifiable symbol names to a crash report](adding-identifiable-symbol-names-to-a-crash-report.md)。

崩溃报告通常具有 `.crash` 和 `.ips` 文件扩展名。如果你有一个 `.ips` 文件，在可用的情况下请优先发布它，而不是 `.crash` 文件。有些论坛允许 `.crash` 文件，但不允许 `.ips` 文件。为确保你的崩溃报告能够发布成功，请在上传前将 `.ips` 扩展名改为 `.txt`。如果论坛提示你的崩溃报告中含有“敏感语言”，请将其附加到回复中，而不是你的初始帖子中。如果你仍然无法直接发布崩溃报告，请将其上传到某个文件分享服务，并在帖子中附上该 URL。

在分享崩溃报告之前，请始终查找并隐去其中的敏感信息。将崩溃报告中出现的你 App 名称和 bundle ID 全部替换为保持原文本长度的隐去字符，以保持文本对齐，同时保留两者之间的区别。例如，将 `MyApp` 替换为 `MmVvv`，将 `com.company.myapp` 替换为 `com.ccccccc.mmmm`。

## 另请参阅

### 相关文档

- [Adding identifiable symbol names to a crash report](adding-identifiable-symbol-names-to-a-crash-report.md) — 用与你 App 代码相对应的函数名和行号，替换崩溃报告中的十六进制地址。
- [Identifying the cause of common crashes](identifying-the-cause-of-common-crashes.md) — 在崩溃报告中找出能识别常见问题的模式，并根据该模式调查问题。
- [Analyzing a crash report](analyzing-a-crash-report.md) — 在崩溃报告中找出有助于你诊断问题的线索。
- [Identifying high-memory use with jetsam event reports](identifying-high-memory-use-with-jetsam-event-reports.md) — 了解操作系统在可用内存不足时终止你 App 的原因。
