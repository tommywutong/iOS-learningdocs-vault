---
title: 'Emerge Tools 博客 | 顺序文件如何减少 App 启动时间'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/FasterAppStartupOrderFiles'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:4555f02b74c61445'
translated: true
---

> 原文：[Emerge Tools Blog | How Order Files Reduce App Startup Time](https://www.emergetools.com/blog/posts/FasterAppStartupOrderFiles)　·　Emerge Tools Blog

# 顺序文件如何减少 App 启动时间

2022 年 1 月 26 日，作者：

[Noah Martin](https://twitter.com/sond813)

iOSFeaturedStartup time

![顺序文件如何减少 App 启动时间](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fblog6.dc0b483d.jpg&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

一个超过 150MB 的 App 二进制文件，比如 Uber App 中的那个，仅加载到内存就需要 500 毫秒到 1 秒（在 iPhone 6s 上测量）。加载如此大的文件只是 App 启动时间的一部分。换个角度来看，Apple 推荐的启动时间仅为 400 毫秒[1]。在没有任何代码执行的情况下，这已经是推荐完整启动时间的 1-2 倍！

默认情况下，App 在启动期间可能需要读取其二进制文件超过 75% 的内容。然而，借助 **顺序文件（order files）**，我们可以在启动期间只读取所需的函数。

## [页面](https://www.emergetools.com/blog/posts/FasterAppStartupOrderFiles#pages)

为什么启动时会用到如此多的二进制内容？答案在于 iOS 如何处理内存。当从 App 的二进制文件中获取新指令时，必须将它们从磁盘加载到内存中。内核并非一次加载一条指令或一个字节，而是一次加载一大块内存，称为**页面（page）**。在 iOS 上，一个页面为 16KB[2]。因此，当首次需要访问 App 二进制文件中的某个指令时，包含该指令的整个 16KB 页面区域都会被映射到内存中。此过程称为**页面错误（page fault）**。

假设二进制文件的前 16KB 包含某个不常用功能（如验证码验证）所使用的代码，但其中恰好包含一个在 App 启动期间执行的 100 字节函数。那么，仅仅为了启动 App，就需要加载整个验证码功能。实际上，由于启动函数分散在二进制文件中，启动过程中最终可能会将大部分甚至全部二进制文件加载到内存中。

## [使用顺序文件](https://www.emergetools.com/blog/posts/FasterAppStartupOrderFiles#using-order-files)

顺序文件重新排列二进制文件，以允许仅读取启动时所需的代码。

源代码中的每个函数都表示为一个不可分割的单元，通常称为符号（symbol）。链接器（linker）决定这些符号的排列顺序，并且默认情况下会将同一源文件中定义的代码在二进制文件中放置在一起。然而，当你向链接器提供顺序文件时，此默认行为会被覆盖。顺序文件指示链接器按特定顺序放置函数。通过排列二进制文件，使所有启动函数聚集在一起，我们只需加载那些页面即可。

![显示多个源文件的代码如何在 App 二进制文件中排序的示意图。](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog6%2F1.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

来自多个源文件的代码在单个二进制文件中排序。

## [理论上的页面错误](https://www.emergetools.com/blog/posts/FasterAppStartupOrderFiles#page-faults)

这样做是值得的，因为页面错误的代价很高。与大多数计算机一样，iPhone 具有内存层次结构，各层级之间存在数量级的延迟。页面错误从最慢的层级读取数据——手机的闪存存储（NAND）。

访问已加载到 RAM 中的内存要快得多，而驻留在处理器缓存中的内存则最快。每个层级越来越小，因此尽量少用内存非常重要。使用的内存越多，低延迟缓存就越快被填满。实际上，还有更多的延迟来源，例如验证代码签名（code signing）。二进制文件按页签名，首次访问页面时，必须对数据进行哈希计算并与签名进行比较。你可以在内核函数 [`vm_fault_validate_cs`](https://opensource.apple.com/source/xnu/xnu-7195.81.3/osfmk/vm/vm_fault.c) 中看到此过程。

## [实践中的页面错误](https://www.emergetools.com/blog/posts/FasterAppStartupOrderFiles#page-faults-in-practice)

要测量实践中的页面错误，只需解引用指向 App 二进制文件中每个页面的指针即可。

我使用 App Store 中的多个 App 进行了测试，并测量了线性扫描中访问每个页面的时间。通过绘制每次访问的时间，你可以看到代表缓存层次结构每个级别的不同波段。以下实验在 iPhone 6S 上进行。

![页面错误持续时间图。](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog6%2F2.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Y 轴采用对数刻度，因此每个层级之间的性能相差 10 倍。

图表右下角的异常值是访问时间极快的页面。这些恰好是二进制文件的 Objective-C 元数据和常量字符串[3]部分。由于测量页面错误时间的代码是在 Objective-C 运行时初始化后运行的，因此这些页面都已被访问过。它们甚至在第一条代码运行之前就已从闪存存储中加载，并且在我访问它们时**已经位于快速缓存中**。

此分布表明，最坏情况下的页面错误大约需要 1 毫秒，但并未说明页面错误的预期持续时间。为此，我查看了读取二进制文件所有页面的累积时间。

![累积页面错误持续时间图。](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog6%2F3.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

趋势很明显！_页面错误的平均时间为 0.06 毫秒_。然而，这并不能解释为什么我们看到的慢速页面错误比快速页面错误少得多。让我们放大图表的一小部分：

![放大后的累积页面错误持续时间图。](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog6%2F4.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

大多数页面错误很快，但每 40-50 次页面错误就会出现一次非常慢的访问。它看起来像一个阶跃函数，并且可以通过系统**预取（prefetching）** 来解释。每次新的页面错误都会触发一次昂贵的查找，这实际上是在预期会使用更多页面的情况下将多个页面加载到内存中。这样做有性能成本，加载更少的页面会使最坏情况（worst-case）下的访问速度更快[4]，但这种行为做出的权衡有利于分摊时间。**这种权衡最适合按顺序访问来利用。乱序访问可能比完全不预取更糟。**

要了解原因，假设一个简化的情况，预取了 3 个页面。

![乱序与按序页面错误访问。](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog6%2F5.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

乱序情况下需要 3 次慢速页面错误才能读取 3 个页面，外加缓存 3 个额外页面的时间。按序情况下只需 2 次慢速页面错误。如果我们改变使用的是哪些页面而不仅仅是它们的顺序，可能只需要一次慢速页面错误。

## [比较顺序](https://www.emergetools.com/blog/posts/FasterAppStartupOrderFiles#comparing-orders)

为了衡量这种效果，我构建了一个可以插入到任何 App 中的动态库（dylib），用于检测内存访问的顺序。我将其与 App Store 中的大型 App 一起运行，并在我的测量函数中重现了它们的访问顺序。将此实际页面访问模式与理想的按序和随机访问模式结合起来，向我们展示了有多少改进空间。

![比较不同页面错误访问顺序的耗时。](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog6%2F6.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

正如预期，随机顺序一开始比线性顺序慢得多，并且总时间显著更长。斜率在末尾逐渐变缓，因为大部分 App 已经被预取。重现 App 启动期间发生页面错误的顺序介于最佳情况和随机访问之间。**顺序文件将你的 App 从绿线变为红线，同时减少了总页面数。**

最后，为了确认没有顺序文件的二进制文件中的页面访问相对随机，此图显示了页面错误编号（App 启动期间观察到的页面错误的顺序）与页面编号（页面在二进制文件中的位置）的关系。

![App 启动期间的页面错误顺序。](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog6%2F7.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

大多数页面错误以随机顺序出现，除了 App 启动开始时一个明显的线性模式（红色圆圈标出）。这条线上的所有页面都包含协议一致性（protocol conformance）元数据。这种行为是因为[在之前的博客文章中讨论的协议一致性的线性扫描](https://www.emergetools.com/blog/posts/SwiftProtocolConformance)。

## [🚀️ 启动助推器（Launch Booster）](https://www.emergetools.com/blog/posts/FasterAppStartupOrderFiles#launch-booster)

总之，访问一个内存页面所需的时间可以从几毫秒到百分之一毫秒不等，具体取决于哪个缓存拥有该页面。对 App 二进制文件中的符号进行排序，可以让系统优化内存访问，从而降低发生慢速页面错误的可能性，并通过将所需内存放置在尽可能少的页面上来减少页面错误的总数。

**这项研究催生了 Emerge 的新产品 [Launch Booster](https://docs.emergetools.com/docs/launch-booster-ios)，这是一项二进制排序服务，可在 CI 中分析 App 以确定最佳排序。使用 Launch Booster，我们看到 App 的启动时间减少了高达 20%！**

自最初发布以来，我们进一步改进了 Launch Booster。你可以[在此](https://www.emergetools.com/blog/posts/how-order-files-speed-up-protocols)阅读更多关于我们如何将协议查找时间减少 20% 的信息。

如果你对 Launch Booster 感兴趣或对顺序文件有任何疑问，请[告诉我们！](https://www.emergetools.com/cdn-cgi/l/email-protection#92e1e7e2e2fde0e6d2f7fff7e0f5f7e6fdfdfee1bcf1fdff)

---

[1] WWDC 2019 - [Session 423](https://developer.apple.com/videos/play/wwdc2019/423/)

[2] 有多个系统以页面为单位进行操作并使用不同的大小。例如，代码签名使用 4KB 页面。页面错误始终涉及 16KB 页面，因此我们在本文中重点关注页面的这一定义（即 16KB 页面）。

[3] 包括 Objective-C 类名，它们在静态初始化器运行之前由运行时注册。

[4] 这可以通过在较小的 App 二进制文件上执行相同的实验来观察。预取的页面更少，每个最坏情况都稍快一些。
