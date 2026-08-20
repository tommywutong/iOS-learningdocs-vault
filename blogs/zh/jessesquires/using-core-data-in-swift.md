---
title: 在 Swift 中使用 Core Data
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2015/05/25/using-core-data-in-swift/'
original_language: en
published: 2015-05-25
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:104de1cf54d352d4'
translated: true
---

> 原文：[Using Core Data in Swift](https://www.jessesquires.com/blog/2015/05/25/using-core-data-in-swift/)　·　Jesse Squires

我最近在旧金山 [Realm](http://realm.io) 举办的 Swift Language User Group（[#SLUG](http://www.meetup.com/swift-language/events/220612410/)）聚会上做了一次演讲。这次[演讲的视频](http://realm.io/news/jesse-squires-core-data-swift/)现已在 Realm 的博客上线，并与我的[幻灯片](https://speakerdeck.com/jessesquires/using-core-data-in-swift)同步。如果你还没看过，快去看看吧！Realm 在发布这些聚会演讲方面做得非常出色——除了视频和幻灯片，还有完整的逐字稿和字幕。

### 演讲摘要

Realm 的笔记和逐字稿很精彩，但我想在此简要重申一下演讲的主要观点。

1.  把你的模型放在独立的框架中。例如，`MyAppModel.framework`。这会为你的模型提供清晰的命名空间，让你的 App 模块化，方便模型在其他地方复用，并且让它们更容易测试。不要将模型添加到测试目标（Test Target），而要 `import MyAppModel`。
2.  为你的 `NSManagedObject` 子类编写使用[依赖注入](http://en.wikipedia.org/wiki/Dependency_injection)的[指定初始化方法](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/Initialization.html)。换句话说，你的初始化方法应参数化以接收其**所有**属性的值。这可以防止由于 `@NSManaged` 而导致模型绕过 Swift 严格的初始化规则。不这样做，你最终可能会得到一个**并未**完全初始化的模型实例。此外，尽可能提供默认参数值。
3.  使用 Swift 特性。充分利用可选值、`typealias` 和 `enum` 来让你的模型更加清晰。请记住，Xcode 不会正确生成带有可选属性的类。
4.  使用 [JSQCoreDataKit](https://github.com/jessesquires/JSQCoreDataKit)！:) 我计划在我自己的业余项目中使用它时，不断改进并为其添加功能。如果你正在使用 Swift 和 Core Data 构建 App，请考虑使用它——非常欢迎贡献代码！
5.  我对将类型安全和函数式范式引入 Core Data 很感兴趣。目前，这种方法意味着要摒弃 Objective-C 的许多动态特性，不幸的是，这导致像 [Mantle](https://github.com/Mantle/Mantle) 这样的流行库无法兼容。这主要归因于在 Swift 中使用指定初始化方法。

### 其他说明

有评论提到了遍历 [`NSManagedObjectModel`](https://developer.apple.com/library/prerelease/ios/documentation/Cocoa/Reference/CoreDataFramework/Classes/NSManagedObjectModel_Class/index.html) 的问题。相关细节和讨论可以在[这个 gist](https://gist.github.com/nevyn/d22c4684370fa07078dd) 中找到。

Alejandro（[@**mephl**](https://twitter.com/mephl)）[指出](https://twitter.com/mephl/status/601003780700655616)，自 iOS 8 起就有了 `NSBatchUpdateRequest`。真是好消息！还有其他人觉得每年在 WWDC 上跟踪所有变化和新增内容变得越来越困难了吗？

### 提交 Radar，否则滚蛋

关于我在 Swift 中使用 Core Data 时遇到的问题，我已经提交了以下 radars。欢迎提交重复报告！另外，别忘了报告你发现的任何其他问题。

- [rdar://21098460](https://openradar.appspot.com/radar?id=6747306682482688)
- [rdar://21098402](https://openradar.appspot.com/radar?id=5534736382427136)
- [rdar://21098433](https://openradar.appspot.com/radar?id=4963635386384384)
