---
title: 'Emerge Tools 博客 | iOS 16 如何让你的 App 启动更快'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/iOS16LaunchTime'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:ce2fe3708c50fa5a'
translated: true
---

> 原文：[Emerge Tools Blog | How iOS 16 makes your app launch faster](https://www.emergetools.com/blog/posts/iOS16LaunchTime)　·　Emerge Tools 博客

# iOS 16 如何让你的 App 启动更快

2022 年 7 月 6 日　作者：

[Noah Martin](https://twitter.com/sond813)

iOSPerformanceStartup time

![文字为 "iOS 16 Startup Time Discoveries" 的图示](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fblog8.857fc0f9.png&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

WWDC22 的[平台状态](https://developer.apple.com/videos/play/wwdc2022/102/)承诺带来一些重要的启动时间改进：

_得益于动态链接器的改进，像 Lyft 或 Airbnb 这样的 App 启动速度几乎翻了一倍。_

这一改进来自于加速协议检查，而我在[之前的博客文章](https://www.emergetools.com/blog/posts/SwiftProtocolConformance)中已经说明了这种检查曾经何其缓慢。此外，iOS 16 还通过减少从磁盘读取的数据量，缩短了加载二进制文件所需的时间。这也正是[前一篇文章](https://www.emergetools.com/blog/posts/FasterAppStartupOrderFiles)的主题。

这些改进归根结底源于 [dyld](https://www.emergetools.com/glossary/dyld) 的变化——dyld 是负责引导你的 App 并开始执行你的代码的程序。它们还采用了两种方向相反（却又都很常见）的性能优化方式——**立即加载（eager loading）** 和 **延迟求值（lazy evaluation）**。

在这篇文章中，我们来看一下 iOS 16 中到底发生了什么改变、实际加速效果如何，以及你怎样才能在 App 中最充分地利用这些新特性。

## [协议检查](https://www.emergetools.com/blog/posts/iOS16LaunchTime#protocol-checks)

协议一致性检查发生在 Swift 运行时中，用来判定 `myVar as? MyProtocol` 这类代码的结果。每次有一个类型符合某个协议时，二进制文件中都会包含一条“一致性记录”。在检查一致性时，运行时会遍历每一条一致性记录，看看是否有任意一条与当前操作匹配。这个循环的时间复杂度是 O(n)，其中 n 就是你 App 中一致性记录的数量。对于大型 App，记录数以万计甚至超过十万次，导致每次一致性检查都非常缓慢。

即使在你自己没有显式编写一致性的情况下，协议一致性检查在 Swift App 中也无处不在，因为它们也会被 `String(describing:)` 或 `AnyHashable` 等常见操作触发。对于 Lyft 和 Airbnb 这类大型 Swift App 来说，将近一半的启动时间都消耗在了协议一致性检查上。

真正重大的变化发生在“dyld 闭包（dyld closure）”中，这是一种按 App 缓存，用来在 App 启动过程中加速各种 dyld 操作。**这个闭包现在包含了预先计算好的一致性信息**，这让每次查找都变得快得多。请注意，dyld 闭包并不总是会被使用，例如它已经过期，或者正在通过 Xcode 启动 App，这都会让情况变得复杂。这一改变作为 [Mike Ash 提交的 PR](https://github.com/apple/swift/pull/41185) 的一部分，在 Swift 开源项目中得以实现，其中新增了 dyld API 调用：`_dyld_find_protocol_conformance_on_disk`。一旦通过这个缓存找到了对应的一致性，原本 O(n) 的操作就会被完全跳过，因此，对于那些拥有一致性记录数量庞大的 App，我们理应看到大幅改善。

### [实际测试](https://www.emergetools.com/blog/posts/iOS16LaunchTime#testing-protocol-checks)

在 Emerge，我们会运行大量性能测试来确定 PR 对 App 启动的影响。所以很自然的，我们也想把这次预计算一致性检查到底会如何影响启动时间测个清楚。

由于我们面对的是两个不同的操作系统版本，没办法在同一台设备上对比。于是我选择了一份包含 1 万、2 万、3 万、4 万和 5 万条一致性记录的二进制文件，对执行一次一致性检查所需的时间进行微基准测试。每一版二进制文件都分别在 iOS 16 设备和 iOS 15 设备上启动，并把 1 万条一致性记录的版本作为基线，仅比较各版本相对于基线的耗时。

![在 iOS 16 和 iOS 15 上检查一致性的耗时](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog8%2F1.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

很明显，随着一致性记录越来越多，iOS 15 会逐渐变慢，而 iOS 16 则不受影响——问题解决了！但在实际场景中，闭包并不总是可用，所以我们需要再等几个月，等到 iOS 16 真正覆盖到用户设备，才能确切知道这一变化在生产环境中的影响到底有多大。这一改进对所有 App 都生效，即使它们的最低部署目标低于 iOS 16。

## [页面错误](https://www.emergetools.com/blog/posts/iOS16LaunchTime#page-faults)

第二大改进来自于减少启动时必须从磁盘加载的数据量。当一段代码第一次被执行时，内核会在一个被称为**页面错误（page fault）** 的过程中，将其周围的内存块（被称为一个页面）加载进来。在 App 启动时，二进制文件的某些部分需要先经过“地址修正（fixups）”，才能运行（对这部分内容的深入解释可以参考[之前的博客文章](https://www.emergetools.com/blog/posts/SwiftReferenceTypes)）。在 iOS 15 上，所有地址修正都是在 App 启动时完成的，这意味着二进制文件中任何需要修正的位置，都必须提前被调入内存。而现在，一项名为[页面内链接（page-in linking）](https://developer.apple.com/wwdc22/110362)的新特性会改用延迟求值的方式来处理地址修正，只有当某个页面首次被访问时，才会解析该页面上的修正。

去年的 WWDC 为用于执行这些地址修正的元数据引入了一种重要的新格式，我也[在当时进行过详细解读](https://www.emergetools.com/blog/posts/iOS15LaunchTime)。要实现地址修正的延迟求值，就必须使用这种新格式，因此，只有当你的 App 面向 iOS 13.4 或更新版本时，iOS 16 用户才能享受到这一改进。

### [实际测试](https://www.emergetools.com/blog/posts/iOS16LaunchTime#testing-page-faults)

在 iOS 15 上，二进制文件的 `__DATA` 和 `__DATA_CONST` 段包含了全部地址修正，所以，在你的代码正式运行之前，页面错误的总数量就等于这些段的大小。借助 Emerge 的工具，我们还能衡量你的代码运行到底需要访问多少页面——两者之差，就是你在 iOS 16 中可以减少的页面错误数量。

### [充分获益](https://www.emergetools.com/blog/posts/iOS16LaunchTime#getting-the-full-benefit)

这当然是一大改进，能立即减少页面错误，但其实还有办法让减少的幅度更大。Emerge 提供一项名为 Launch Booster 的排序文件服务，它能自动重新排列二进制文件中的符号，以最大限度地降低页面错误。在 iOS 15 上向 App Store 部署排序文件后，我们**平均将启动时间缩短了 18%**。如今，既然 iOS 16 不再自动加载每一个页面，对二进制文件进行重新排序就可以让你的 App 启动得更快！如果你想进一步了解如何自动缩短启动时间、用好 iOS 16 的各项改进，欢迎[联系](https://www.emergetools.com/cdn-cgi/l/email-protection#6d1e181d1d021f192d0800081f0a08190202011e430e0200) Emerge 团队。
