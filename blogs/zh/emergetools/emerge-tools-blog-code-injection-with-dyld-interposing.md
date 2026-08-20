---
title: 'Emerge Tools 博客 | 使用 dyld Interposing 进行代码注入'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/DyldInterposing'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:bcda78ea532dd45f'
translated: true
---

> 原文：[Emerge Tools Blog | Code Injection with Dyld Interposing](https://www.emergetools.com/blog/posts/DyldInterposing)　·　Emerge Tools Blog

# 使用 dyld Interposing 进行代码注入

2022年5月24日，作者：[Noah Martin](https://twitter.com/sond813)

iOSSwift性能

![使用 dyld Interposing 进行代码注入](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fblog7.f13166e1.jpg&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Objective-C 运行时的动态特性可以被用于许多目的，包括方法调配（method swizzling）。有很多[教程](https://nshipster.com/method-swizzling/)解释了如何使用 swizzling，对于很多目的来说它都能胜任。然而，它并不总是能用的。

Swizzling 处理 Objective-C 方法，但不能用于 C/C++ 函数。非 Obj-C 的底层调用对于逆向工程 iOS App 很有用，但有时你需要在一个没有源代码的 App 中拦截它们。

在这篇文章中，我们将研究一种较少为人知的技术，用于在函数调用处注入代码，这种技术适用于 C/C++ 函数，也适用于未修改的 App 二进制文件。这些基本构建模块支撑着许多开发者工具，包括我在 Emerge Tools 的工作。

## [示例](https://www.emergetools.com/blog/posts/DyldInterposing#example)

假设你正在尝试逆向工程一个 App，以了解它如何使用钥匙串（Keychain）。你知道在某处 App 会调用 [`SecItemCopyMatching`](https://developer.apple.com/documentation/security/1398306-secitemcopymatching)，但不清楚存储了什么数据以及存储在什么键下。这个函数无法被 swizzle，因为它不是 Objective-C 的。你也不能修改原始源代码，你拥有的只有编译好的 App。

在这篇文章中，我们将实现一个解决方案，它在 App 运行时将所有从钥匙串请求的数据打印到标准输出。该方案使用了一个框架，它 interpose `SecItemCopyMatching`，并在启动时通过 `DYLD_INSERT_LIBRARIES` 加载。

## [DYLD_INSERT_LIBRARIES](https://www.emergetools.com/blog/posts/DyldInterposing#dyld-insert-libraries)

虽然不是 interposing 严格必需的，但插入库通常与 interposing 结合使用，对于任何探索 iOS 内部原理的人来说都是极好的资源，所以值得快速概述一下。

`DYLD_INSERT_LIBRARIES` 是一个环境变量，允许你向 App 的进程添加代码。其格式只是一个以冒号分隔的框架列表，这些框架将在 App 启动时被链接。例如：`DYLD_INSERT_LIBRARIES=@executable_path/Frameworks/InterposingSample.framework/InterposingSample`。如果你曾经在 Linux/Android 上使用过 `LD_PRELOAD`，这就是 iOS 中的等价物。

这一个环境变量[1] 潜力巨大，你可以编写一个 `+load` 方法，在 App 启动时添加任何你想要的额外逻辑，包括 swizzling、响应 NSNotifications 或呈现一个全新的 UI。这甚至被 SwiftUI 预览（previews）所使用，检查来自预览的崩溃报告会显示这一行：`DYLD_INSERT_LIBRARIES=/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Library/Developer/CoreSimulator/Profiles/Runtimes/iOS.simruntime/Contents/Resources/RuntimeRoot//System/Library/PrivateFrameworks/PreviewsInjection.framework/PreviewsInjection`

## [DYLD_INTERPOSE](https://www.emergetools.com/blog/posts/DyldInterposing#dyld-interposing)

当你使用 [dyld](https://www.emergetools.com/glossary/dyld) interposing 时，你甚至不需要使用像 `+load` 这样的初始化方法，因为它是一个比 swizzling 声明式（declarative）得多的 API。正如[我之前讨论过的](https://www.emergetools.com/blog/posts/SwiftReferenceTypes)，App 启动时第一个运行的代码是 dyld，而不是你编写的代码。dyld 的职责之一就是将调用从一个二进制文件绑定（bind）到另一个，例如从你的 App 到 Apple 的框架。Interposing 是一种告诉 dyld 用一个已被 bind 的函数替换另一个的方式。

### [Dyld Binding](https://www.emergetools.com/blog/posts/DyldInterposing#dyld-binding)

嵌入在你的二进制文件中的是一个引用外部符号的表格，我在[上一篇博客文章](https://www.emergetools.com/blog/posts/iOS15LaunchTime)中写过这种数据在 iOS 15 中的新格式。一些符号是 lazily bound 的，仅在首次使用时才通过每个 App 中都包含的一个名为 `dyld_stub_helper` 的函数进行 bind。其他符号则在 App 启动时立即 bound。这两种方法都允许 dyld 对定义在另一个二进制文件中的任何函数的地址拥有最终决定权，幸运的是，它给了你修改这个地址以指向你自己函数的机会。

### [Interposing](https://www.emergetools.com/blog/posts/DyldInterposing#interposing)

![图示展示了映像和 interposed 函数之间的连接关系。](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog7%2F1.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

使用插入框架 interpose SecItemCopyMatching

Interposing 的工作原理是添加一个新的 Mach-O section（`__DATA, __interpose`），其中包含一个元组列表，这些元组保存了替换函数（replacement）和被替换函数（replacee）的地址。如果任何库（包括插入的库）包含了这个 Mach-O section（`__DATA, __interpose`），那么 dyld 将使用这个列表，将任何对被替换函数的调用替换为替换函数，只要该调用不是来自包含替换函数的二进制文件本身。**这意味着在你插入的框架中，任何对你试图 interpose 的函数的调用仍将指向原始函数。**

查看 dyld 的源代码，我们可以准确地看到这些 interposed 地址是在哪里加载的：

![Dyld 源代码](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog7%2F2.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

为了在你的二进制文件中创建这个新的 section，Apple 提供了一个[便捷的宏（macro）](https://github.com/apple-opensource/dyld/blob/b6b86eb2db14440d373f6f7fd21be4a2bc0da897/include/mach-o/dyld-interposing.h)：

![dyld_interpose 宏](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog7%2F3.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

现在，把所有这些整合起来，我们可以看到如何实现一个框架，完成我们最初示例中的目标：

## [你能用它做什么？](https://www.emergetools.com/blog/posts/DyldInterposing#what-can-you-do-with-this)

很多！在 [Emerge Tools](https://www.emergetools.com)，我们将这项技术用于所有运行时性能测量，例如顺序文件生成和性能测试。通过 interposing，你可以 hook 到未修改的 App 中，以测量 App 行为、提取信息或完全改变行为。对于开发者工具来说，这是一个强大的运行时优势。任何时候当你发现自己需要 swizzle 一个 C/C++ 函数或任何不属于 Objective-C 的东西（因此无法被 swizzle）时，了解 interposing 作为你可以求助于的替代方案是很好的。有一点免责声明：我还没有在 App Store 的 App 中尝试过这个，但总的来说，我建议只将其用于本地测试！

## [其他方法](https://www.emergetools.com/blog/posts/DyldInterposing#other-methods)

在 iOS App 中，除了 Objective-C 运行时之外，还有其他几种实现代码注入的方法。[Fishhook](https://github.com/facebook/fishhook) 是一个由 Facebook 创建的流行库。与 dyld interposing 类似，它利用了 Mach-O symbol binding。使用 fishhook 你不需要一个单独的 dylib，如果你能控制 App 的源代码，这可能会方便得多。我倾向于在可能的情况下使用 dyld interposing，因为它是一个完全第一方的解决方案，但 fishhook 只有几百行 C 代码，并且可以提供指导，让你从更底层的角度理解 symbol binding 过程是如何工作的。

细心的读者可能会注意到 dyld 源代码中的另一个特性：通过函数 `dyld_dynamic_interpose` 实现的动态 interposing。这只是一种在运行时告诉 dyld 开始 interpose 某个函数的方式。这与 fishhook 的工作方式类似；你不需要一直 interpose 一个函数，而是可以通过编程方式安装一个 hook。该 API 至少有一个用例被 [Peter Steinberger 在 Chrome 源代码中发现](https://twitter.com/steipete/status/1258482647933870080?s=21)。看起来 Chrome 正在覆盖 CoreAudio 以修改其行为，看到 interposing 在生产环境中使用的例子很有趣！

---

[1] 如果你对其他 dyld 环境变量感兴趣，请查看 `man dyld`
