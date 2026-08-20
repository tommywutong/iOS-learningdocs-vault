---
title: 如何调试通过推送通知或 URL 处理程序启动的 App
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2010/05/how-to-debug-app-launched-by-remote-event/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e4e0ab9c13fbc1d5'
translated: true
---

> 原文：[How to Debug an App That Was Launched by Push Notification or URL Handler](https://oleb.net/blog/2010/05/how-to-debug-app-launched-by-remote-event/)　·　Ole Begemann

# 如何调试通过推送通知或 URL 处理程序启动的 App

最近我在 [Stack Overflow](http://stackoverflow.com/) 上活跃度颇高。迄今为止，我已经在那里[回答了 315 个问题](http://stackoverflow.com/users/116862/ole-begemann)，虽然我自己没有提过任何问题，但我从其他人在那里分享的知识中获益良多。这确实是一个很棒的平台，比大多数编程论坛都要好得多。我觉得我回答过的很多问题对你也可能有用，所以我想在这里分享一些比较有意思的问题（当然也包括答案），或许比在 SO 上更详细一些。

从这个问题开始：[如何调试由外部事件（如推送通知或 URL 处理程序）启动的 App？](http://stackoverflow.com/questions/454188/how-do-you-debug-your-application-if-they-got-started-using-a-custom-url-scheme/) 在这些情况下你不会点击“构建并调试”，那么如何让调试器注意到你的 App 呢？你有两种选择：

# 1. 使用 NSLog 语句并在 Console.app 中检查

你的 `NSLog()` 调用的输出不仅会出现在 Xcode 的调试器控制台中，也会出现在系统日志中。要查看模拟器的日志（对测试自定义 URL 方案很有用），请在 OS X 中打开 Console.app，在左侧窗格中选择“控制台信息”（Console Messages），然后在“过滤”（Filter）字段中搜索你的 App 名称。要在设备上查看控制台信息（例如测试你的 App 如何处理接收到的推送通知），请在 Xcode 中打开管理工具（Organizer），选择你的设备，然后在 App 启动前切换到控制台（Console）标签。

# 2. 要求调试器等待你的 App 启动

有时候，`NSLog()` 还不够用，你需要调试器的全部功能。没问题：

1. 在你想要的位置设置断点，例如在 `application:didFinishLaunchingWithOptions:` 中。
2. 选择“项目”（Project）>“编辑活跃可执行文件”（Edit Active Executable）。在“调试”（Debugging）标签中，选中“等待下一次启动/推送通知”（Wait for next launch/push notification）复选框：

  [![Xcode 活跃可执行文件设置：调试，等待下一次启动](https://oleb.net/media/xcode-active-executable-debugging-wait-for-next-launch.png)](https://oleb.net/media/xcode-active-executable-debugging-wait-for-next-launch.png)
3. 像平常一样构建并调试。控制台会显示一条消息，告诉你调试器正在等待你的 App 启动。

  [![Xcode：调试器正在等待 App 启动](https://oleb.net/media/xcode-debugger-waiting-for-app-to-launch.png)](https://oleb.net/media/xcode-debugger-waiting-for-app-to-launch.png)
4. 通过调用你的自定义 URL 或发送推送通知来启动你的 App。调试器会自动附加到你的 App 进程并在断点处停止。
