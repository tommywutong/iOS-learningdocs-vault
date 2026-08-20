---
title: Quick 5.0 发布
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2022/04/17/quick-5-released/'
original_language: en
published: 2022-04-17
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:84fa2228b91f4d62'
translated: true
---

> 原文：[Quick 5.0 released](https://www.jessesquires.com/blog/2022/04/17/quick-5-released/)　·　Jesse Squires

如果你为 Apple 平台开发并使用第三方测试框架，那么你很可能正在用 [Quick](https://github.com/quick/quick) 和 [Nimble](https://github.com/quick/nimble)。否则，你至少也应该听说过它们。我在个人项目中不使用任何第三方测试框架，但我曾与使用它们的团队合作过。而且我目前所在的团队就在用 Quick 和 Nimble，这也是为什么对我来说，能让 Quick 中最近出现的一个严重 bug 得到修复至关重要。

[Xcode 13.3](https://developer.apple.com/documentation/xcode-release-notes/xcode-13_3-release-notes) [引入了严重的衰退](https://github.com/Quick/Quick/issues/1123)，导致测试无法被发现。这意味着你整个测试套件中的所有测试都不会被执行，而 Xcode 却报告它们都成功通过了。这个 bug 还意味着你无法让任何测试失败。我并不完全清楚根本问题所在，也不知道“该怪谁”——是 Xcode 13.3 修复了 Quick 在无意中利用的错误行为，从而暴露了 Quick 中的问题？还是 Xcode 本身引入了一个真正的 bug？无论如何，好消息是这个问题已经在 [Quick 5.0 版本](https://github.com/Quick/Quick/releases/tag/v5.0.0)中修复了。

我的团队在将 CI 切换到 Xcode 13.3 后发现了这个问题，并迅速在 GitHub 上找到了[一个未解决的 issue](https://github.com/Quick/Quick/issues/1123)。甚至已经有人提交了一个拉取请求（Pull Request）来修复这个问题。（我应该向他们致谢，但他们后来删除了自己的 GitHub 账号，这很离奇。不知道发生了什么。）问题在于，Quick 项目当时有些被忽视了。许多原始作者和维护者多年没有参与该项目，而[上一个版本](https://github.com/Quick/Quick/releases/tag/v4.0.0)发布已经快一年了。[Sho Ikeda](https://github.com/ikesyo) 是最近最活跃的维护者，但当时也不在。没有人能立即审阅和合并这个 PR。

幸运的是，我认识几位原始的核心维护者，我联系了他们请求帮助解决这个紧急的问题，同时希望能获得项目的访问权限，以便我能帮助维护它，并发布包含此修复的官方版本。非常感谢 [Ash Furrow](https://twitter.com/ashfurrow) 和 [Jeff Hui](https://twitter.com/jeffhui)，尽管他们多年未参与该项目，但仍挺身而出！也要感谢 [Sho Ikeda](https://twitter.com/ikesyo) 在这些年里一直维护，直到这次最新版本。

总之，我上周每天花了几个小时来追踪 4.0 版本以来的所有变更，将它们整理到 [5.0 里程碑](https://github.com/Quick/Quick/milestone/7?closed=1)中，尽可能多地合并拉取请求，关闭过时的 issue 和 PR，并对项目进行了清洁和整理。我在 [Nimble](https://github.com/Quick/Nimble) 上也做了同样的工作，并将帮助完成[它的 10.0 版本发布](https://github.com/Quick/Nimble/milestone/11)。我不打算为这两个项目贡献代码，但我可以帮忙做项目管理、代码审查和发布。

我参与进来的主要关切仅仅是解决自己团队的阻塞问题，避免不得不维护项目的一个分支，但我决定超越这个目标，自愿帮助社区的其他成员，让项目变得更好。成千上万的人依赖这个项目，我完全理解他们被这个 bug 阻塞时的感受。我也认识到自己处于一个享有特权的地位——我有机会积累丰富的开源项目维护经验，也能深入参与 iOS 社区并与人建立联系。如果我无法利用我与 Ash 和 Jeff 的关系，这一切都不会发生。我很高兴能利用这份特权来帮助其他人。

Quick 5.0 版本的发布内容非常丰富。它不仅包含了上述关键 bug 的修复，还增加了一些新功能。你可以查看[完整的发布说明](https://github.com/Quick/Quick/releases/tag/v5.0.0)。这完全是社区共同努力的结果。**感谢各位的谢意，但在开源世界中，表达感激的最佳方式是金钱。** _资本主义就是这样，宝贝！_ 这是个没人想要的糟糕系统，但我们别无选择，只能参与其中。能够有能力和精力为开源免费工作是种特权，但这并不意味着贡献者不值得获得报酬。如果你在使用 Quick 和 Nimble，无法贡献时间，并且有多余的资金——那么请考虑[在 GitHub 上赞助我](https://github.com/sponsors/jessesquires)或通过其他[方式给我捐款](https://www.jessesquires.com/sponsor/)。你也应该向 5.0 版本的**其他贡献者**表达你的爱——_我说的爱，就是钱，宝贝！_——他们列在[发布说明的底部](https://github.com/Quick/Quick/releases/tag/v5.0.0)。
