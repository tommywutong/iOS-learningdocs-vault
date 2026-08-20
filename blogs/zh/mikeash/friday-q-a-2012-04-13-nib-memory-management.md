---
title: 'Friday Q&A 2012-04-13：Nib 内存管理'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-04-13-nib-memory-management.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:7985bb049eb54373'
translated: true
---

> 原文：[Friday Q&A 2012-04-13: Nib Memory Management](https://www.mikeash.com/pyblog/friday-qa-2012-04-13-nib-memory-management.html)　·　mikeash.com Friday Q&A

发布于 2012-04-13 14:14 | [RSS 源](https://www.mikeash.com/pyblog/rss.py) ([全文源](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2012-04-27: PLCrashReporter and Unwinding the Stack With DWARF](https://www.mikeash.com/pyblog/friday-qa-2012-04-27-plcrashreporter-and-unwinding-the-stack-with-dwarf.html)  
上一篇：[Introducing PLWeakCompatibility](https://www.mikeash.com/pyblog/introducing-plweakcompatibility.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [memory](https://www.mikeash.com/pyblog/?tag=memory) [nib](https://www.mikeash.com/pyblog/?tag=nib)

Friday Q&A 2012-04-13：Nib 内存管理

作者：[Mike Ash](https://www.mikeash.com/)

**Nib 加载概述**  
当你加载一个 nib 时，会按顺序执行两个重要步骤。首先，加载器会实例化 nib 中的所有对象。其次，它会连接 nib 中指定的所有 outlet。

在内存管理方面，有两个相关领域。第一个是如何正确管理 outlet。第二个是如何管理 nib 中的顶层对象。一个 nib 包含一个对象层级结构，其中每个对象由其父对象拥有，但该层级结构顶层的对象属于特殊情况。

**Mac Nib 加载**  
我们来谈谈 Mac 上的 nib 加载在两个相关内存管理领域中的工作方式。

顶层对象使用 `alloc` 和 `init`（或特定类的初始化方法，例如 `NSWindow` 实例的 `-initWithContentRect:styleMask:backing:defer:`）进行实例化。它们随后保持此状态，最终释放它们的责任被隐式转移给 File's Owner 对象。如果你使用 `NSWindowController` 或 `NSViewController` 加载 nib，它会自动获取这些对象的所有权，并在控制器销毁时释放它们。

要设置 outlet，nib 加载器首先查找 setter 方法。如果 outlet 名为 `foo`，加载器会查找名为 `setFoo:` 的方法。如果存在这样的方法，加载器就会调用它，将 outlet 的值作为参数传入。

如果没有这样的方法，加载器会查找与 outlet 同名的实例变量（instance variable）。如果找到这样的实例变量，加载器会直接将其值设置为 outlet 的值，而不执行任何内存管理。

最后，如果既找不到方法也找不到实例变量，outlet 连接失败，outlet 不会被设置。

**iOS Nib 加载**  
现在来谈谈 iOS 上的 nib 加载工作方式。总的来说非常相似，但有一些细微的差别。不必试图找出所有差异，我会指出它们并随后进行分析。

顶层对象使用 `alloc` 和 `init`（或特定类的初始化方法）进行实例化，然后自动释放（autoreleased）。如果没有其他东西保留它们，这些对象会自动被销毁。

要设置 outlet，nib 加载器会使用 outlet 的值和名称调用 `-setValue:forKey:`。然后键值编码（Key-Value Coding，KVC）机制接管并查找设置该特定键的方法。对于名为 `foo` 的 outlet，它会首先查找名为 `setFoo:` 的方法。如果存在这样的方法，它会调用该方法，将 outlet 的值作为参数传入。

如果没有这样的方法，KVC 机制会查找名为 `_foo`、`_isFoo`、`foo` 或 `isFoo` 的实例变量。如果找到其中任何一个，它会将第一个找到的实例变量设置为 outlet 的值，同时释放该实例变量中的旧值（如果有）并保留（retain）新值。

如果没有找到方法和实例变量，KVC 会调用 `setValue:forUndefinedKey:`。默认情况下，这会引发一个异常，并且可以重写此方法以实现针对未知键的自定义行为。

**差异**  
这两个系统相似但不完全相同。差异源于 iOS 更现代的特性。毫无例外，在两个系统不同的地方，iOS 的方式更加合理。不幸的是，Mac 的方式无法在不严重破坏向后兼容性的情况下改变。这些差异是：

- 在 Mac 上，你必须显式释放顶层对象，除非你使用 `NSWindowController` 或 `NSViewController` 加载 nib。在 iOS 上，它们是自动释放的。
- 在 iOS 上，由于 KVC 的工作方式，直接设置 ivar 会保留 outlet。在 Mac 上，outlet 不会被保留。
- 因为在 iOS 上直接设置 ivar 会导致一次 retain，所以这些 outlet 必须在 `dealloc` 中释放。在 Mac 上，可以忽略它们。
- 在 iOS 上，由于 KVC 的原因，直接设置 ivar 的搜索模式比在 Mac 上更全面。

**相似之处**  
追踪这些差异既费心神又容易出错，尤其是当你在两个平台之间切换时。弄错可能会导致泄漏或崩溃（或两者兼有）。处理这些差异的最佳方法是坚持使用两个平台相同的领域。幸运的是，这些领域也是处理 nib 最方便、最好的方式。

当使用 Cocoa 控制器类（Mac 上的 `NSWindowController` 和 `NSViewController`，iOS 上的 `UIViewController`）加载 nib 时，nib 中的顶层对象会自动为你处理，因此在这种情况下两个平台的行为变得相同。直接加载 nib 的情况极为罕见，如果你发现自己正在这样做，你大概应该停下来，改用这些控制器之一。

当对 outlet 使用 `@property` 时，两个平台的内存管理是一致的，因为它们都会使用 setter（如果存在）。你可以根据喜好设置 property 的内存管理方式，尽管通常更倾向于使用 `strong` 或 `retain`。在这种情况下，你必须在 `dealloc` 中 `release` property 的值，就像你对其他任何 strong property 所做的那样，除非你使用的是 ARC。对于 iOS 上子视图的 outlet，`weak` 可能是一个不错的选择，因为视图可能会被卸载，而你不想让强引用在背后让它们保持存活。

**一张便捷的表格**  
以下是各种情况的完整摘要，以方便的表格形式呈现：

| **Outlet 类型** | **Mac** | **iOS** |
|---|---|---|
| 直接设置 ivar | 未保留引用，不要释放 | 保留引用，必须在 dealloc 中释放 |
| Strong/retain setter | 在 dealloc 中释放（或让 ARC 处理） | 在 dealloc 中释放（或让 ARC 处理） |
| Assign/weak setter | 不需要做任何事 | 不需要做任何事 |
|  |  |  |
| 顶层对象 | 使用 `NSWindowController` 或 `NSViewController` 加载 nib，别傻了 | 使用 `UIViewController` 加载 nib，别傻了 |
| 说真的，顶层对象怎么办？ | 释放每个顶层对象以平衡加载 nib 时发送的 `alloc` | 不需要做任何事 |

**结论**  
Nib 内存管理在 Mac 和 iOS 之间相似，但又恰好足够不同以至于令人恼火地困惑。幸运的是，通过坚持使用两个平台行为相同的领域，很容易减轻混淆，这本身也是最佳实践。始终使用 Cocoa 控制器加载 nib，而不是直接自己加载 nib。始终为你的 outlet 声明 property。与任何 property 一样，如果你的 outlet property 是 strong 的，那么你必须在 `dealloc` 中释放其底层实例变量（或让 ARC 为你完成）。

今天就到这里。下次回来，我们将带来另一期激动人心、令人愉悦的 Friday Q&A。在那之前，由于 Friday Q&A 是由读者建议驱动的，请[发送](mailto:mike@mikeash.com)你的话题想法。

喜欢这篇文章吗？我正出售整本包含这些文章的书！第二卷和第三卷现已出版！提供 ePub、PDF、印刷版以及 iBooks 和 Kindle 格式。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS 源](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-04-13-nib-memory-management.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。
