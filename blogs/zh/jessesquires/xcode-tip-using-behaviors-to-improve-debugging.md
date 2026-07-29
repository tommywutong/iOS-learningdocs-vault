---
title: 'Xcode 技巧：利用行为（Behaviors）改进调试体验'
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2018/07/01/xcode-tip-debugging-behavior-new-tab/'
original_language: en
published: 2018-07-01
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:dc7f744ad3941ed4'
translated: true
---

> 原文：[Xcode Tip: Using behaviors to improve debugging](https://www.jessesquires.com/blog/2018/07/01/xcode-tip-debugging-behavior-new-tab/)　·　Jesse Squires

之前，我[讨论过](https://www.jessesquires.com/blog/2018/06/12/xcode-tip-improving-assistant-editor/)如何在编写 Swift 时让 Xcode 的助手编辑器（Assistant Editor）不再那么令人沮丧。最近学到的另一个技巧是使用 Xcode 的行为（Behaviors）来改善调试体验。

在 Xcode 中，我通常（也是默认）的调试体验大致如下：发现需要调试的问题，设置几个断点来进行调查。一旦第一个断点被触发，我的 App 就会暂停，Xcode 会把当前活动的编辑器跳转到被触发（hit）的断点处。有时我需要手动打开底部面板来显示控制台（如果它还没显示的话）。有时我需要手动调整显示“变量视图（Variables View）”和“控制台视图（Console View）”的方式，决定同时显示还是只显示其中一个。我在调试器中一步步执行，检查 App 的状态，调试所有问题等等。如果问题比较复杂，我大概率会设置多个断点，并频繁地在代码中来回跳转，跨越多个文件。

调试完成后，我结束调试会话，结果发现 Xcode 把我留在了调试结束的地方。我的编辑器显示的是指令指针（instruction pointer）在 LLDB 中最后指向的那个文件和代码行。“变量视图”和“控制台视图”依然显示着，尽管现在是空的。我完全丢失了开始调试之前正在编写代码的上下文。这可能会让人非常沮丧。

很久以前，我开始通过打开新标签页（tab）来缓解这个问题。这样一来，调试结束后我只需关闭该标签页，就能回到之前编写代码的地方继续工作。不过，每次调试会话仍然以同样的方式开始：我需要手动打开一个新标签页，显示控制台，隐藏侧边栏等等。然而，有一种更好的方法可以实现这一点，那就是使用 Xcode 行为。

![Xcode 行为设置](https://www.jessesquires.com/img/blog/xcode-behaviors-debugging.png)

<sub>Xcode 行为设置</sub>

在 Xcode 的偏好设置中，进入行为（Behaviors）标签页。导航到“运行（Running）”部分，点击“暂停（Pauses）”。在这里，你可以指示 Xcode 打开一个新标签页，勾选“显示名称为（Show tab named）”复选框并为其命名。默认情况下，“显示调试导航器（Show Debug Navigator）”应该已启用。接下来，我倾向于显示带有“变量与控制台视图（Variables & Console View）”的调试器，同时隐藏右侧的实用工具（Utilities）侧边栏。

这真是太棒了，我简直不敢相信自己之前竟然不知道这个功能。有了这些设置，当断点被触发时，Xcode 现在会自动打开一个新标签页，并按照我期望的方式精确配置好编辑器。调试完成后，我可以关闭该标签页，然后迅速回到之前中断的地方继续工作。Xcode 行为是一个强大的功能，我现在也会去自定义其他行为了。

感谢 Chris Miles 在 WWDC 2018 的演讲 [Advanced Debugging with Xcode and LLDB](https://developer.apple.com/videos/play/wwdc2018/412/) 中分享了这一点。这仅仅是他提到的一个小建议。当然，他还提供了**更多**关于有效且高效使用 LLDB 的绝妙技巧。那是我今年最喜欢的演讲之一。你应该去看看。
