---
title: 通过内存完整性强制增强 App 的安全性
session_id: 206
collection: meet-with-apple
year: null
duration: '12:21'
topics: [Developer Tools, Swift, 'Privacy & Security']
group: B · 内存管理与内存性能
evergreen: true
source_url: 'https://developer.apple.com/videos/play/meet-with-apple/206/'
content_hash: 'sha256:f8ed362cdd5bcdc3'
translated: true
---

# 通过内存完整性强制增强 App 的安全性

<sub>MEET-WITH-APPLE · 12:21 · 开发者工具、Swift、隐私与安全</sub>

了解内存完整性强制（Memory Integrity Enforcement，MIE）——一种全新的安全技术，硬件、操作系统和编译器协同工作……

> [!note] 归档理由
> 内存完整性强制（MIE）——硬件级内存安全，底层新知识

## 章节

- [简介](/videos/play/meet-with-apple/206/?time=5)
- [内存溢出与 Use-After-Free 漏洞](/videos/play/meet-with-apple/206/?time=89)
- [内存完整性强制](/videos/play/meet-with-apple/206/?time=188)
- [演示：内存损坏 Use-After-Free Bug](/videos/play/meet-with-apple/206/?time=282)
- [启用硬件内存标记](/videos/play/meet-with-apple/206/?time=352)
- [演示：硬件内存标记中断攻击尝试](/videos/play/meet-with-apple/206/?time=380)
- [其他配置选项](/videos/play/meet-with-apple/206/?time=404)
- [演示：修复内存损坏 Bug](/videos/play/meet-with-apple/206/?time=445)
- [其他考量](/videos/play/meet-with-apple/206/?time=572)
- [指针中的标记位](/videos/play/meet-with-apple/206/?time=610)
- [指针值的哈希、比较与算术运算](/videos/play/meet-with-apple/206/?time=630)
- [软模式](/videos/play/meet-with-apple/206/?time=662)
- [下一步](/videos/play/meet-with-apple/206/?time=691)

## 相关资源

- [简介](https://developer.apple.com/videos/play/meet-with-apple/206/?time=5)
- [内存溢出与 Use-After-Free 漏洞](https://developer.apple.com/videos/play/meet-with-apple/206/?time=89)
- [内存完整性强制](https://developer.apple.com/videos/play/meet-with-apple/206/?time=188)
- [演示：内存损坏 Use-After-Free Bug](https://developer.apple.com/videos/play/meet-with-apple/206/?time=282)
- [启用硬件内存标记](https://developer.apple.com/videos/play/meet-with-apple/206/?time=352)
- [演示：硬件内存标记中断攻击尝试](https://developer.apple.com/videos/play/meet-with-apple/206/?time=380)
- [其他配置选项](https://developer.apple.com/videos/play/meet-with-apple/206/?time=404)
- [演示：修复内存损坏 Bug](https://developer.apple.com/videos/play/meet-with-apple/206/?time=445)
- [其他考量](https://developer.apple.com/videos/play/meet-with-apple/206/?time=572)
- [指针中的标记位](https://developer.apple.com/videos/play/meet-with-apple/206/?time=610)
- [指针值的哈希、比较与算术运算](https://developer.apple.com/videos/play/meet-with-apple/206/?time=630)
- [软模式](https://developer.apple.com/videos/play/meet-with-apple/206/?time=662)
- [下一步](https://developer.apple.com/videos/play/meet-with-apple/206/?time=691)
- [内存完整性强制：Apple 设备上内存安全的完整愿景](https://security.apple.com/blog/memory-integrity-enforcement/)
- [为 App 启用增强的安全性](https://developer.apple.com/documentation/Xcode/enabling-enhanced-security-for-your-app)
- [HD 视频](https://devstreaming-cdn.apple.com/videos/meet-with-apple/2025/206/5/83750d91-e7ae-4960-afe0-f81661b11bce/downloads/meet-with-apple-206_hd.mp4?dl=1)
- [SD 视频](https://devstreaming-cdn.apple.com/videos/meet-with-apple/2025/206/5/83750d91-e7ae-4960-afe0-f81661b11bce/downloads/meet-with-apple-206_sd.mp4?dl=1)
- [高级调试与地址消毒器](https://developer.apple.com/videos/play/wwdc2015/413)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，我是 Julian。我是开发者安全工具团队的一名工程师。在本视频中，我将介绍如何通过内存完整性强制（Memory Integrity Enforcement）来增强 App 的安全性。App 触及我们生活的方方面面。它们是每个人都信任并托付其私密细节的基本工具——位置与浏览历史、照片、消息、联系人、财务信息，以及更多。与此同时，App 又与互联网相连，因此这些 App 中的安全漏洞可能使用户受到攻击。针对个人的攻击可能带来从欺诈、身份盗窃到勒索，甚至威胁生命的严重后果。

人们期望自己的数据得到保密和安全。如果这一承诺未能兑现，便构成了信任的破坏。安全是支撑隐私的技术基础。因此，安全对于消息、社交媒体和浏览器类 App 尤为重要。这些 App 处理大量不受信任的输入，并且通常覆盖面广泛，使攻击者能够精确瞄准其受害者。最常见的安全漏洞之一是内存损坏（memory corruption）。攻击者可以利用内存 Bug 劫持对 App 的控制并窃取用户敏感数据。例如，缓冲区溢出破坏会越过缓冲区的边界，损坏另一个分配中的内存。然后，当另一个指针读取该内存时，可能导致数据损坏和难以重现的崩溃。但更糟的是，通过精心构造写入操作，攻击者可能诱使你的 App 执行其控制下的任意代码。

攻击者还可以利用许多 Use-After-Free Bug。假设一个 App 释放了一块内存，但留下了一个指向它的悬空指针。然后 App 创建了一个新的分配，恰好被放置在同一内存位置。如果 App 意外地通过悬空指针进行读取或写入，就会导致内存损坏。

防止内存损坏的最佳方法是使用内存安全（memory-safe）的语言，例如 Swift。

内存安全的语言通过为你管理内存，确保编程错误不会导致内存损坏。但即使你用 Swift 编写所有新代码，你的 App 仍可能因为现有代码库而包含一些 C 和 C++ 代码。或者它可能依赖用无法保证内存安全的语言编写的外部库。内存完整性强制（Memory Integrity Enforcement，MIE）是一项新技术，它使攻击者极难利用内存损坏 Bug。这是内存安全的一次重大进步，硬件、操作系统和编译器协同工作，通过安全中止程序执行来阻止对无效内存的访问。首批支持的设备是 iPhone 17、iPhone Air、iPhone 17 Pro 和 Pro Max。请查阅“为 App 启用增强的安全性”以了解哪些其他 Apple 设备受支持。其工作原理如下。在内存完整性强制下，系统分配器为每个堆（heap）分配分配一个标记，并将该标记编码在返回指针中。在每次从内存加载或存储时，硬件检查指针中的标记是否与分配的标记匹配。例如，如果标记为 A 的指针用于读取或写入同样标记为 A 的内存，则访问被允许继续进行。

但在 Use-After-Free 场景中，标记为 A 的悬空指针将访问一个赋予不同标记的新分配。这就是标记不匹配，因此硬件中止程序执行，使攻击者无法损坏内存。这种方法也能防止缓冲区溢出破坏，因为分配器会为相邻分配分配不同的标记。这是我的演示 App，其中包含一个内存损坏漏洞。请注意，App 本身是用 Swift 编写的，但也使用了一个外部的 C 库来解析图像。我怀疑这个库存在 Use-After-Free Bug，但不知道具体在哪里。我会运行这个 App。

看起来我收到了一条消息。我想查看照片，于是点击了它。

哦不，发生了什么事？事实证明，这不仅仅是一张可爱狗狗的照片，而是一张由恶意攻击者精心构造的图像。在后台，该图像利用一个 Use-After-Free Bug 将我的私密消息发送到了互联网上的一台服务器。这非常可怕。现在，我夸张了这次攻击的视觉效果。攻击者通常会尽量使活动保持隐蔽。

在更现实的攻击中，用户数据会在用户甚至没有意识到的情况下被泄露。要在 Xcode 中通过内存完整性强制保护你的 App，请前往 App target 的签名与功能（Signing and Capabilities）编辑器，点击“添加功能”（Add Capability），然后选择“增强安全性”（Enhanced Security）。这将启用一系列强大的安全保护，包括硬件内存标记（Hardware Memory Tagging）。

对于本地测试，请确保内存标记的软模式（Soft Mode）已关闭。稍后我会详细讨论软模式。我已经启用了硬件内存标记并重新启动了 App。我再次点击了恶意图像。

App 现在终止了，而不是允许攻击者窃取我的消息。点击终止原因会显示，App 因标记不匹配而中止。

以下是一些硬件内存标记的其他配置选项。“内存标记纯数据”（Memory Tag Pure Data）选项将保护范围扩展到更广泛的分配。如果你的 App 使用解释器或即时（Just-In-Time）编译器，请启用“阻止接收已标记内存”（Prevent Receiving Tagged Memory）。确保启用了增强安全类型分配器（Enhanced Security Type Allocator）。它能有效防止利用 Use-After-Free Bug 的攻击，并且可以与内存标记结合使用以提供最佳保护。最后，还有用于验证你的 App 是否已为内存标记做好准备的软模式（Soft Mode）选项。在我的演示 App 中，攻击者的利用现在被阻止了。但用户体验并不理想。为了防止 App 崩溃，我仍然需要修复底层的内存损坏 Bug。Xcode 帮助你发现并修复这些 Bug，使它们在你开发环境中影响用户之前就被解决。为此，请前往 Scheme 编辑器，在诊断（Diagnostics）面板中启用硬件内存标记。我在 Scheme 编辑器中启用了硬件内存标记诊断，并再次运行了 App。我再次通过点击图像触发了 Bug。App 将再次终止，但现在 Xcode 提供了额外信息来帮助我理解问题。首先，它指出标记不匹配是由于使用了已释放的内存——一个 Use-After-Free。调试导航器显示了一个有用的堆栈跟踪，告诉我内存是在哪里被释放的。在这个例子中，是在 `process_image_message` 函数中。

回到崩溃点，发现它位于一个异步派发的 block 中。

好的，我现在理解了问题所在。主线程（main thread）在后台线程有机会处理消息之前就将其释放了。为了解决这个问题，我将把消息的释放从主线程移到异步 block 的末尾，这样它只在处理完成后才被释放。

我将再次启动 App，以确保我的更改修复了底层 Bug。

我将再次点击图像。嗯，看起来不错。App 收到了恶意图像，但攻击者无法以此劫持 App。

接下来，我将讨论让你的 App 为内存完整性强制做好准备的其他几项考量。现在是时候修复在 App 正常使用期间出现的任何残留的缓冲区溢出或 Use-After-Free Bug 了。你可以通过在测试中启用硬件内存标记诊断来发现并理解这些 Bug。

这将使许多难以重现的内存损坏 Bug 变成可操作的崩溃。

如果你没有支持内存完整性强制的设备，请改用地址消毒器（Address Sanitizer）。硬件内存标记将标记存储在指针的高位中，以保护分配。

你需要确保这些位没有被你的 App 使用或修改。如果你的 App 使用自定义标记指针方案，请将其调整为将此信息存储在其他地方。

在哈希、比较或对指针进行算术运算时也要小心。启用内存标记后，指向不同分配的指针将具有不同的标记，因此设置不同的高位。

请考虑这将如何影响指针值的哈希、比较和算术运算。

避免比较源自不同分配的指针。并在必要时屏蔽标记位。

软模式有助于你验证是否已找到并修复了 App 中的内存损坏 Bug。它以模拟崩溃日志的形式提供关于标记不匹配的遥测数据，而不会终止执行。在你的 TestFlight 和客户群体中启用此模式，以增强信心，确保不存在遗留的内存损坏 Bug。一旦你的内存损坏 Bug 被修复，请关闭软模式以保护用户。以下是你的下一步行动。如果你的 App 处理未经验证的输入，请采用内存完整性强制来保护你的用户。这对于消息、社交媒体和浏览器类 App 尤其重要。通过修复已知的内存损坏 Bug 来让你的 App 做好准备。并确保你的 App 没有将指针标记位用于其他目的。

在启用硬件内存标记诊断的情况下测试你的 App。并使用软模式验证你的修复。然后关闭软模式以保护用户。感谢观看并采用内存完整性强制。
