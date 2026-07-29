---
title: 如何在 iOS 上运行 sysdiagnose
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2018/02/08/how-to-sysdiagnose-ios/'
original_language: en
published: 2018-02-08
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:95571f46d3d3c098'
translated: true
---

> 原文：[How to run sysdiagnose on iOS](https://www.jessesquires.com/blog/2018/02/08/how-to-sysdiagnose-ios/)　·　Jesse Squires

当你在 Apple 的某个平台上[提交 radar](https://developer.apple.com/bug-reporting/) 报告一个 bug 时，你（通常）应该总是附上一份 sysdiagnose。sysdiagnose 为试图了解 bug 是如何发生的人提供了大量有用的信息。除其他内容外，它包含操作系统各个部分的日志，以及所有最近的崩溃日志。没有它，你报告另一端 Apple 内部的人可能帮不了多大忙。在 macOS 上运行 sysdiagnose 比较常见，但在 iOS 上呢？

##### [更新](#updated-09-february-2018)  _2018 年 2 月 9 日_

显然，下面说明中的直接链接无法工作，即使你已登录到你的 Apple 开发者帐户也是如此。你可以在[官方 Bug 报告页面](https://developer.apple.com/bug-reporting/profiles-and-logs/?name=sysdiagnose)上找到所有 sysdiagnose 说明。

##### [更新](#updated-05-january-2019)  _2019 年 1 月 5 日_

非常感谢 Michael Prentice [指出](https://github.com/jessesquires/jessesquires.com/issues/87#issuecomment-450595104)你也可以在 iOS 模拟器上运行 sysdiagnose。要执行此操作，请运行 `xcrun simctl diagnose`，输出将放置在 `/private/tmp/` 中。

![Apple Bug 报告](https://www.jessesquires.com/img/blog/apple-bug-report.png)

<sub>[来源](https://dribbble.com/shots/3617982-Apple-Bug-Report-iOS)</sub>

### macOS 上的 sysdiagnose

在 macOS 上，[sysdiagnose 有相当完善的文档](https://developer.apple.com/legacy/library/documentation/Darwin/Reference/ManPages/man1/sysdiagnose.1.html)。你可以通过 `sudo sysdiagnose` 从命令行运行它，这会将生成的 `.tar.gz` 文件放在 `/var/tmp/` 中。或者，你可以使用键盘快捷键：`control` + `option` + `command` + `shift` + `.`——这会让你的屏幕闪一下，当报告生成完成后，访达（Finder.app）会打开包含它的文件夹（`/var/tmp/`）。它最多可能需要 10 分钟才能完成，并且没有任何视觉指示表示正在发生任何事情。请耐心等待，继续你正在做的任何工作。该报告将包含大量日志、系统统计信息和其他诊断信息。你可以在此处找到[适用于 macOS 的官方说明](https://download.developer.apple.com/OS_X/OS_X_Logs/sysdiagnose_Logging_Instructions.pdf)。

> **注意：**在所有系统上，设备在生成 sysdiagnose 的部分过程中将变得无响应，生成的 `.tar.gz` 通常约为 200-300 MB。

### iOS 上的 sysdiagnose

iOS 上的 sysdiagnose 呢？一位朋友最近告诉我这是可能的。经过一番搜索，我确实找到了在 iOS 上运行 sysdiagnose 的[官方开发者说明](https://download.developer.apple.com/iOS/iOS_Logs/sysdiagnose_Logging_Instructions.pdf)。要在 iOS 上触发 sysdiagnose，请同时按下两个音量按钮和电源按钮。如果成功触发，你会感觉到短暂的振动或触觉反馈。与 macOS 一样，它最多需要 10 分钟来生成。等待后，你可以通过导航到“设置”App > “隐私” > “分析” > “分析数据”来找到 `.tar.gz`。这有点隐蔽。这里会有一个按字母顺序排列的大量文件和日志列表。向下滚动到底部，直到找到“sysdiagnose…”文件。点击该文件，然后点击右上角的“分享”按钮，你就可以通过 AirDrop 将其发送到你的 Mac。然后将其附加到你的 bug 报告中。正如我之前提到的，这个文件大约有 200-300 MB，所以不要尝试通过电子邮件或 iMessage 发送它。

### tvOS 和 watchOS 的 sysdiagnose

我很惊讶地得知，你甚至可以在 tvOS 和 watchOS 上运行 sysdiagnose。

- [tvOS 的说明](https://download.developer.apple.com/iOS/tvOS_Logs/sysdiagnose_Logging_Instructions.pdf)
- [watchOS 的说明](https://download.developer.apple.com/iOS/watchOS_Logs/sysdiagnose_Logging_Instructions.pdf)

### 特定 App 的 sysdiagnose

一些 macOS 应用程序有自己的 sysdiagnose。对于 Xcode，你可以运行 `sudo sysdiagnose Xcode`。对于邮件（Mail.app），你可以运行 `sudo sysdiagnose Mail`。下次你遇到 Xcode 问题时，请提交一个 radar 并附上一份 sysdiagnose。

- [邮件（Mail.app）的说明](https://download.developer.apple.com/OS_X/OS_X_Logs/Mail_app_sysdiagnose_Logging_Instructions.pdf)
- [Xcode 的说明](https://download.developer.apple.com/OS_X/OS_X_Logs/Xcode_sysdiagnose_Logging_Instructions.pdf)

### 编写更好的 Bug 报告

Peter Steinberger 已经编写了一份关于[编写好的 Bug 报告](https://pspdfkit.com/blog/2016/writing-good-bug-reports/)的优秀指南。除了他所有出色的建议之外，经常附上一份 sysdiagnose 可能非常有帮助——即使你有可靠的复现步骤或特定的崩溃报告。sysdiagnose 包含额外的有用信息。它易于操作，并且可在所有平台上使用。
