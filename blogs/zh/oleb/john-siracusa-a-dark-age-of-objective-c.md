---
title: 'John Siracusa：Objective-C 的黑暗时代'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/04/john-siracusa-a-dark-age-of-objective-c/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6ce18c46d4ff6ff7'
translated: true
---

> 原文：[John Siracusa: A Dark Age of Objective-C](https://oleb.net/blog/2011/04/john-siracusa-a-dark-age-of-objective-c/)　·　Ole Begemann

# John Siracusa：Objective-C 的黑暗时代

在[上周的《Hypercritical》播客节目](http://5by5.tv/hypercritical/14)中，John Siracusa 重新讨论了一个他早在 2005 年就曾在博客中写过的主题（从 21 分 09 秒开始）。当时，在一系列题为 [Avoiding Copland 2011](http://arstechnica.com/staff/fatbits/2005/09/1372.ars)（[第二部分](http://arstechnica.com/staff/fatbits/2005/09/1393.ars)、[第三部分](http://arstechnica.com/staff/fatbits/2005/10/1412.ars)）的博客文章中，John 思考 Apple 的未来是否潜伏着一场根本性的危机，其影响程度堪比当年向具备内存保护和抢占式多任务处理的现代操作系统转型时管理不善所导致的问题——Copland 项目的失败正是其缩影。在 1990 年代，这场危机几乎毁掉了 Apple。

# Apple 缺乏内存管理语言和 API

在 2005 年，John 认为 Objective-C 和 Cocoa 是 Apple 未来一个严重的潜在隐患。具体来说，Objective-C 需要手动管理内存（在 iOS 上至今仍是如此），并且迫使开发者与指针打交道，这固然让它比 Java 和 C# 等更抽象的平台更灵活、更快速，但最终，世界将不可避免地走向更高的抽象层次，从而使 Apple 的竞争对手获得优势：

> 在其他条件相同的情况下，当你面对两项技术——一项抽象程度更低但性能更高，另一项抽象程度更高但速度更慢——从长远来看，抽象程度更高、速度更慢的技术总是会胜出。因为硬件性能会随时间推移而提升，而人类处理复杂性的能力却不会[……]。

更糟糕的是，Apple 仅仅发明或采用一门新的编程语言是不够的：整个 Cocoa API 都是为 Objective-C 编写和优化的，任何与 Objective-C 有显著差异的语言，都需要一套全新、能发挥其优势的 API。

我认为 John 非常有说服力地论证了，Microsoft 在向更高抽象层次及相应 API 的过渡方面领先了多远（并且至今仍保持领先），以及完成这一壮举是多么了不起（.NET 于 2002 年初面世，距今已近十年）。当然，这并非说 Apple 落后了十年，因为 Cocoa 的 API 质量远胜 Win32 也是事实。

# iOS 的救场：宛如时光倒流

最初，John 预计 Apple 会在 2010–2015 年这个时间段内遭遇 Objective-C 带来的问题。当他[在 2010 年首次重新审视自己的预测](http://arstechnica.com/apple/news/2010/06/copland-2010-revisited.ars)时，这些预测一个都没有成真。John 认为 iPhone 的崛起是原因之一。当开发者面对 iOS 设备的限制（CPU 慢、内存极小、无交换空间）时，Objective-C 贴近底层的特性反而再次成为优势，这至少在一定程度上是 iOS 相比竞争对手性能普遍更好的原因之一。

> 这种新的硬件现实，有效地把 Apple 开发者心中对于高级编程语言和框架的时钟往回拨了；而 Objective-C 作为 C 语言超集的特性，也重新被视作一项优势。当你开发的 App 不断收到来自操作系统的低内存警告时，很难再为仍需处理像指针和 C 结构体这样底层、精确到每个字节的实体而焦虑不安。

但让我们再把目光投向未来几年：iOS 设备在性能方面已经取得了巨大进步，即便在今天，当新设备的内存已远超初代 iPhone，双核 CPU 也开始出现时，像垃圾回收这样的特性在 iOS 平台上也开始变得有意义。这一趋势在未来几年无疑会持续快速推进。而 Apple 在移动领域的竞争对手——无论是 Google、Microsoft 还是 HP——都已为其平台选定了托管语言。

所有这些似乎暂时并未困扰到 App 开发者，仍有成千上万的新手被 App Store 的成功前景*以及* Apple API 的质量所吸引，涌入 Objective-C 和 Cocoa 的世界（我对 Android 了解不多，但据我所知，许多人认为为 iOS 开发是更愉快的体验）。这无疑证明了这门语言和框架的高质量。

> 噢，我知道你在想什么。就是你，那位 Cocoa 开发者——你觉得我疯了。你会说，Cocoa 和 Objective-C 是 Apple 最大的优势，而不是一颗滴答作响的技术定时炸弹！而且，尽管它源于 C，但将其实现描述为“底层”是不公平的，因为它提供了连强大的 Java 都尚未拥有的动态能力和语言特性。
>
> [……]
>
> 尽管 2010 年没有出现危机，但 Apple 最终*还是*需要解决这个问题。五年前我就在思考它的原因，也正是如今我更加担忧它的原因：开发平台很难改变。首先是技术问题，需要选择或开发一门新语言，并为其创建一套新的 API。优秀的 API 需要数年时间来发展和成熟。看看 Cocoa 就是一个很好的例子。

# Apple 是否错失了 iOS 诞生时的良机？

这引出一个有趣的问题：Apple 是否在推出 iOS 时错失了转向新平台的绝佳机会？如果有足够的时间来规划这一切，他们本可以将 Objective-C 和 Cocoa 留在 Mac OS X 上，为这个崭新、闪亮的移动平台创建一个全新的操作系统，并搭配自己的编程语言和 API。如果当年 Steve Jobs 不是自豪地宣称 iPhone 运行的是 OS X，而是说绝对不可能把 OS X 移植到这么小、这么弱的设备上，我想没人会怀疑他。

就像现在这样，iOS SDK 会成为 Apple 的新星；而 Apple 本不应把为 iPhone 发明的特性（如 Core Animation）直接移植到 Mac 上的 Cocoa，而是让 Foundation 和 AppKit 缓慢而痛苦地消亡，并通过 Snow Leopard 和 Lion 将新的 iOS SDK 逐步引入 Mac，作为编写 Mac App 的另一种方式。如果 Apple 只接受用“UIKit”编写的 App 进入 Mac App Store，那么该商店的推出本可以成为这个平台最终的突破点。

这是一个有趣的思想实验，但它显然忽略了这样一个事实：这样的举措需要 Apple 投入更多的资源，并且很可能会将 iPhone 的发布推迟数年。开发一个成熟的平台需要时间，并且 iOS 能否像现在这样功能丰富且稳定是值得怀疑的。此外，我们刚刚也提到，Objective-C 的问题在移动设备上反而变成了优势。如果 iPhone 是在一个新的软件平台上推出，但同时面临 OS X 早期那样的性能问题，它还能取得同样的成功吗？我认为不会。“我一下子就被滚动效果征服了”这一点太重要了。

# 总有一天，必须有所改变

那么，我们现在处在什么位置呢？正如 John 所说，Objective-C *总有一天*会过时，尽管我们不知道具体是什么时候。而且，问题远不止自动内存管理这一点。在我看来，Objective-C 的长期弱点在于其严格的 C 语言血统。只要我们开发者还为了在集合（collection）中存储一个简单值或将其传给某个 API，而不得不在 `NSInteger` 和 `NSNumber *` 之间来回转换，那就说明有问题，而且应该被修复。

和 John 一样，我也希望 Apple 内部某个团队正在酝酿另一次过渡（transition）。至于 Apple 的解决方案是什么？我不知道。也许 Apple 持续投入巨大精力到 [LLVM 项目](http://llvm.org/)中，是表明 LLVM 与此有关的一个迹象。

我强烈推荐收听这期播客，或者阅读那四篇文章。都是好内容。

**2011 年 4 月 24 日更新：**我最初在我那篇 [iOS development highlights: July 2010](https://oleb.net/blog/2010/07/ios-development-highlights-july-2010/) 文章中写过一个关于此话题的段落。第一个要点包含了一些其他人帖子的好链接。我建议你去看看。
