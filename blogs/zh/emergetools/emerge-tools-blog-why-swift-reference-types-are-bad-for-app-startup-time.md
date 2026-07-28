---
title: 'Emerge Tools 博客 | 为什么 Swift 引用类型对 App 启动时间不利'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/SwiftReferenceTypes'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:c79b0accaec953ba'
translated: true
---

> 原文：[Emerge Tools 博客 | 为什么 Swift 引用类型对 App 启动时间不利](https://www.emergetools.com/blog/posts/SwiftReferenceTypes)　·　Emerge Tools 博客

# 为什么 Swift 引用类型对 App 启动时间不利

2021 年 3 月 4 日，作者

[Noah Martin](https://twitter.com/sond813)

SwiftiOSStartup time

![手机屏幕显示计时器在 00:00.42](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fblog2.b56ccfe4.png&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

App 的启动体验是用户对你的第一印象。用户在等待你的 App 启动时，每一毫秒都是他们本可以在其他地方度过的宝贵时间。如果你的 App 有很高的用户粘性并且每天被多次使用，那么用户就得一遍又一遍地等待启动。Apple [建议](https://developer.apple.com/videos/play/wwdc2019/423/?time=305)在 400 毫秒内绘制出第一帧画面。这能确保当 Springboard 的 App 打开动画完成时，你的 App 已经准备好被使用。

由于只有 400 毫秒的可用时间，开发者需要非常小心，避免无意中增加 App 的启动时间。然而，App 启动是一个相当复杂的过程，涉及许多活动部分，因此很难确切知道是什么导致了启动时间变长。我在开发 App 体积分析工具 [Emerge](https://www.emergetools.com/) 时，开始更深入地研究 App 二进制体积与启动时间之间的关系。在这篇文章中，我将为你揭示 App 启动中一个较为深奥的方面，并展示 Swift 引用类型如何影响二进制体积并导致更慢的 App 启动时间。

## [Dyld](https://www.emergetools.com/blog/posts/SwiftReferenceTypes#dyld)

你的 App 在 Mach-O 可执行文件被 [dyld](https://www.emergetools.com/glossary/dyld) 加载时启动。Dyld 是 Apple 的程序，负责让 App 准备好被使用。它与你所写代码运行在同一个进程中，并首先加载所有依赖的框架¹，包括任何系统框架。

dyld 的部分工作是“rebasing”二进制元数据中的指针，这些元数据描述了源代码中的类型。这些元数据支持动态运行时特性，但也可能是二进制体积膨胀的常见来源。以下是已编译的 App 二进制文件中 Obj-C 类的布局：

```swift
struct ObjcClass {
let isa: UInt64
let superclass: UInt64
let cache: UInt64
let mask: UInt32
let occupied: UInt32
let taggedData: UInt64
}
```

每个 `UInt64` 是另一段元数据的地址。这些数据位于 App 的二进制文件中，因此世界上的每个人都会从 App Store 下载完全相同的这份数据。然而，由于地址空间布局随机化（[ASLR](https://en.wikipedia.org/wiki/Address_space_layout_randomization)），你的 App 每次启动时都会被放置在内存中的不同位置（而不是始终从 0 开始）。这是一项安全特性，旨在使预测某个特定函数在内存中的位置变得困难。

ASLR 的问题在于，硬编码到 App 二进制文件中的地址现在是错误的，它被一个随机的起始位置偏移了。Dyld 负责通过 rebase 所有指针来考虑这个唯一的起始位置，从而纠正此问题。这个处理过程会针对可执行文件以及所有依赖框架（包括递归依赖）中的每个指针执行。dyld 还会进行其他类型的元数据设置，这些设置也会影响启动时间，例如“binding”，但在本文中，我们只关注 rebase。

所有这些指针设置都会增加 App 的启动时间，因此**减少指针设置可以带来更小的 App 二进制文件和更快的启动时间**。让我们看看这些设置从何而来，以及具体可能产生什么影响。

## [Swift 与 Obj-C](https://www.emergetools.com/blog/posts/SwiftReferenceTypes#swift-and-objc)

我们已经看到，rebase 时间是由 App 中的 Obj-C 元数据引起的，但究竟是什么在 Swift App 中导致了这些元数据呢？Swift 有 `@objc` 特性（attribute）来使声明在 Objective-C 代码中可见，但即使你的 Swift 类型对 Obj-C 代码不可见，也会生成元数据。这是因为**在 Apple 平台上，所有 Swift 类类型都包含 Objective-C 元数据**。让我们通过以下声明来看一下实际情况：

```swift
final class TestClass { }
```

这是纯 Swift 代码，它没有继承自 `NSObject`，也没有使用 `@objc`。然而，它会在二进制文件中生成一个 Obj-C 类元数据条目，并添加 9 个需要 rebase 的指针！为了证明这一点，可以使用像 Hopper 这样的工具检查二进制文件，你会看到你的“纯 Swift”类的 objc_class 条目：

![App 二进制文件中的 Obj-C 元数据](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog2%2F1.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

App 二进制文件中的 Obj-C 元数据

你可以通过将 `DYLD_PRINT_STATISTICS_DETAILS` 环境变量设置为 `1`，来查看启动 App 所需的确切指针 rebase 数量。这会在 App 启动后，将 rebase 修复（rebase fixups）的总数打印到控制台。我们甚至可以精确地找出这 9 个指针的位置。

![指针 rebasing 图解](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog2%2F2.jpg&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

并非所有 Swift 类型都会添加相同数量的 rebase。如果你通过从超类（superclass）重写或遵循 Obj-C 协议（protocol）来向 Obj-C 暴露方法，你会添加更多的 rebase。此外，Swift 类上的每个属性（property）都会在 Objective-C 元数据中生成一个实例变量（ivar）。

## [测量](https://www.emergetools.com/blog/posts/SwiftReferenceTypes#measuring)

rebase 对实际启动时间的影响会因设备类型和手机上正在运行的其他内容而异。我在仍然被广泛支持的最旧设备之一 iPhone 5S 上进行了测量。

iOS 启动可以大致分为热启动和冷启动。热启动是指系统已经启动了 App 并缓存了一些 dyld 设置信息。由于我测试的第一次启动是冷启动，所以它的速度比其他启动稍慢²。

在这个案例中，我们看到每 2000 次 rebase 操作会增加大约 1 毫秒的时间。这不会是对启动时间的绝对增加，因为某些操作可以并行执行，但它确实给了我们一个下限。而且，当有 40 万次 rebase 时，我们已经用掉了 Apple 建议的 400 毫秒限制的一半。

## [示例](https://www.emergetools.com/blog/posts/SwiftReferenceTypes#examples)

测量几个流行 App 中的 rebase 操作数量，可以让我们了解这在实践中是多么普遍。

```shell
% xcrun dyldinfo -rebase TikTok.app/TikTok | wc -l
2066598
```

TikTok 有超过 200 万次 rebase，这导致了整整一秒的启动时间！TikTok 使用 Objective-C，但我也测试了几个使用单体二进制架构（相对于框架）的最大型 Swift App，发现它们的 rebase 次数在 68.5 万到 180 万之间。

## [可以做什么？](https://www.emergetools.com/blog/posts/SwiftReferenceTypes#what-can-be-done)

尽管每个类都会增加 rebase 操作，但我并不建议用结构体（struct）替换每个 Swift 类。大型结构体也可能增加二进制体积，而且某些情况下你确实需要引用语义。与任何性能改进一样，你应该避免过早优化，并从测量开始。[Emerge](https://www.emergetools.com/) 可以确定你的 App 中有多少次 rebase，它们来自哪些模块，以及这些模块中的哪些类型是最大的贡献者。一旦你测量了问题，就可以在自己的 App 中寻找可以改进的领域。以下是一些常见情况：

#### [组合 vs 继承](https://www.emergetools.com/blog/posts/SwiftReferenceTypes#composition-vs-inheritance)

假设你有一个像这样的数据层：

这会生成大量元数据，但你可以用值类型来表示相同的概念，[这对于数据层来说是更优的选择](https://developer.apple.com/documentation/swift/choosing_between_structures_and_classes)，并且最终可以减少 22% 的 rebase。这涉及到用值组合（例如带关联值的枚举或泛型类型）来替代对象继承。

#### [Swift 中的分类](https://www.emergetools.com/blog/posts/SwiftReferenceTypes#categories-in-swift)

尽管 Swift 使用扩展（extension）而不是[分类（category）](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/CustomizingExistingClasses/CustomizingExistingClasses.html)，但你仍然可以通过声明一个使用 Objective-C 函数的扩展来生成分类二进制元数据。请看下面的示例声明：

这两个函数都包含在二进制元数据中，但由于它们在扩展中声明，因此它们会被 `TestClass` 上一个合成的分类所引用。将这些函数移入原始类声明中，可以避免分类元数据被包含在二进制文件中而带来的额外开销。这类元数据可以通过 [Emerge](https://www.emergetools.com/) 的二进制分析工具自动标记。

更进一步，你可以通过使用基于闭包（closure）的回调（例如 [iOS 14 中引入的](https://developer.apple.com/documentation/uikit/uibutton/3600777-init)）来完全避免 `@objc`。

#### [大量属性](https://www.emergetools.com/blog/posts/SwiftReferenceTypes#many-properties)

Swift 类中的每个属性会增加 3 到 6 个 rebase 修复，具体取决于该类是否为 `final`。对于具有 20 个以上属性的大型类来说，这些数量会迅速累积。例如：

将其改为由结构体支持，可以减少 60% 的 rebase 修复数量！

#### [代码生成](https://www.emergetools.com/blog/posts/SwiftReferenceTypes#codegen)

你可以进行的一项高投资回报率的更改是改进代码生成。代码生成的一个常见用途是创建跨代码库共享的数据模型。如果你正在对许多类型进行此操作，你应该警惕它们可能增加的大量 Obj-C 元数据。然而，即使是值类型也会在代码大小和 rebase 修复方面产生开销。最好的解决方案是最小化生成的类型数量，甚至用生成的函数替换自定义类型。

这些示例只是二进制体积可能导致启动时间增加的几种方式。另一个因素是代码从磁盘加载到内存所需的时间，你的代码越多，所需时间就越长。如果你希望获得帮助，寻找减少 App 体积和启动时间的方法，可以通过发送邮件至 [[email protected]](https://www.emergetools.com/cdn-cgi/l/email-protection#aad9dfdadac5d8deeacfc7cfd8cdcfdec5c5c6d984c9c5c7) 与 Emerge 团队联系！

---

[1] 框架（Framework）是一个重载术语。从技术上讲，dyld 会设置你的 App 启动所需的所有 Mach-O 映像文件。其中一些不是框架，而另一些框架并非 App 启动所必需。

[2] 我还对每个测试运行了几次，发现重复启动由于热启动的原因，rebase 时间也会更快。为简单起见，我在这里只报告了测试的第一次运行，因为它提供了一个更稳定的基准数字。
