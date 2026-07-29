---
title: 'GitHub 技巧：关注发布版本'
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2020/07/30/github-tip-watching-releases/'
original_language: en
published: 2020-07-30
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a47977441fb20a5b'
translated: true
---

> 原文：[GitHub Tip: watching releases](https://www.jessesquires.com/blog/2020/07/30/github-tip-watching-releases/)　·　Jesse Squires

不久前，GitHub [增加了一个新选项](https://github.blog/changelog/2018-11-27-watch-releases/)，用于“关注”（watching）仓库。这个设置决定了项目上的哪些事件会向你发送通知（notification）。

此前，选项包括：

1. 不关注（Not Watching）：当参与讨论或被 @ 提及时收到通知。
2. 关注（Watching）：收到所有讨论的通知。
3. 忽略（Ignoring）：从不收到通知。

新增的选项是“仅发布（Releases Only）”——在新版本发布时，以及参与讨论或被 @ 提及时会收到通知。它完美地介于“不关注”和“关注”之间。对我来说，这是 GitHub 上最好用也最有用的功能之一。

![仅关注 GitHub 发布的版本](https://www.jessesquires.com/img/blog/github-watch-releases.png)

<sub>仅关注 GitHub 发布的版本</sub>

为什么它如此有用？我很少想收到一个项目上*所有*活动的通知，尤其当我只是该项目的用户而非贡献者时。更重要的是，许多项目没有博客或邮件列表来宣布新版本——而即便是那些提供博客或邮件列表的项目，它们往往也只宣布主要版本，而不是*所有*版本。即便如此，我也经常在我的 RSS 阅读器中错过这些公告（前提是该博客提供了 RSS 源（feed））。

无论如何，我更不想让项目发布的公告塞满我的 RSS 源。GitHub 是我工作的地方，也是我想收到通知的地方。我使用的许多工具都需要保持更新，比如 [SwiftLint](https://github.com/realm/SwiftLint)、[Jazzy](https://github.com/realm/jazzy) 和 [CocoaPods](https://github.com/cocoapods/cocoapods)。对这些项目以及其他项目“关注发布版本”一直很棒。有时，我等待一个项目的补丁版本，以修复我遇到的某个特定 bug；或者，我可能等待 CocoaPods 支持最新版本的 Xcode——现在 GitHub 会在每个版本发布时通知我。

还有一个额外好处：我还在 [actions/virtual-environments](https://github.com/actions/virtual-environments) 上关注发布版本，这样每当 [GitHub Actions](https://github.com/features/actions) 环境发生变化时，我都会收到通知。这意味着一旦新的 Xcode 版本部署到 GitHub Actions，我就可以更新我所有的 workflow。
