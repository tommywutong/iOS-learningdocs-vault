---
title: Swift 发布版本有主题
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2017/03/swift-themed-releases/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4300e23a156e8910'
translated: true
---

> 原文：[Swift releases have themes](https://oleb.net/blog/2017/03/swift-themed-releases/)　·　Ole Begemann

# Swift 发布版本有主题

大约一周前，[Swift Core Team](https://swift.org/community/#core-team) 成员 Ben Cohen 在 [swift-evolution](https://swift.org/community/#swift-evolution) 上[写了一篇富有见地的帖子](https://forums.swift.org/t/additive-proposals/5312/2)，回答了一个关于纯新增提案被 [Swift 4](https://github.com/apple/swift/blob/master/CHANGELOG.md#swift-40) 接受的可能性的[问题](https://forums.swift.org/t/additive-proposals/5312)。

Ben 解释了 Core Team 用来决定哪些提案应该进入下一个语言版本的依据。其要点是，每个 Swift 发布版本应聚焦于少量主题，并且对这些主题有贡献的提案将获得优先考虑。

我认为[那篇帖子](https://forums.swift.org/t/additive-proposals/5312/2)没有获得应有的关注，因此我在此完整引用它（链接和强调为我所加）：

> 值得注意的是，目前一些纯新增提案正在范围内，前提是它们与 [Swift 4 设定的主题](https://forums.swift.org/t/looking-back-on-swift-3-and-ahead-to-swift-4/3610)保持一致。例如，针对 [`String`](https://developer.apple.com/reference/swift/string)、[`Dictionary`](https://developer.apple.com/reference/swift/dictionary) 和 [`Sequence`](https://developer.apple.com/reference/swift/sequence)/[`Collection`](https://developer.apple.com/reference/swift/collection) 的纯新增提案已被标准库接受。在未来的 Swift 发布版本中，与其他主题（如进一步的字符串工作（比如原生正则表达式）、move-only 类型、并发（concurrency）、反射或进一步的泛型增强）对齐的纯新增提案，很可能也会进入范围。_我们认为，保持对特定主题的聚焦对语言演进至关重要，而不受约束且与当前任何主题无关的纯新增提案，其被接受的门槛始终会非常高。_
> 
> 原因之一是带宽问题——无论是核心团队还是社区。将讨论集中在主题上，有助于其他社区参与者跟进邮件列表（尽管[迁移到论坛格式](https://forums.swift.org/t/plan-to-move-swift-evolution-and-swift-users-mailing-lists-to-discourse/5128)有望在这方面有所帮助）。而且，通过确保提案与每个发布版本的整体目标主题一致，我们更能避免出现大量提案被接受但最终未被实现的情况。
> 
> 此外，当讨论集中在特定主题上时，_我们能够为该主题内的功能提供更完整、更连贯的设计_。我们可以探索（比如）Swift 4 的所有[新泛型功能](https://github.com/apple/swift/blob/master/CHANGELOG.md#swift-40)如何协同工作，以提供一个完整、连贯且更易使用和解释的系统；或者所有新的字符串功能如何共同造就[了不起的字符串](https://github.com/apple/swift/blob/master/docs/StringManifesto.md)。_这既关乎信息传递——Swift 4 带来了什么？——也关乎我们能更有机会构建一个连贯的设计。_
> 
> 连贯的设计不仅对于一个发布版本内部很重要——因为它能让开发者更容易学会共同使用新特性——_而且对于语言的长期健康同样重要_。没有主题化的提案，很难看出单个提案如何融入 Swift 的整体方向。我们可能会冒着做出微小局部更改的风险，而这些更改后来在我们考虑与之相关的更广泛变更时会让我们后悔。还有一个风险是，我们可能注意不到语言中积累了太多关键字或概念——它们单独看来都有意义，但总体上并不协调。
> 
> 例如，最近关于[元类型重构](https://github.com/DevAndArtist/swift-evolution/blob/refactor_existential_metatypes/proposals/0126-refactor-metatypes.md)的提案，确实需要在反射这一更大背景下加以考虑，因此可能应等到该主题进入范围。另一个例子：近期提案 [SE-154](https://github.com/apple/swift-evolution/blob/master/proposals/0154-dictionary-key-and-value-collections.md)，旨在更改 `Dictionary` 上键和值集合的类型——孤立地看它并没有真正意义：它仍然只是提供了一种略显笨拙的方式来解决字典需要“初始”值然后就地更新该值的问题。但它需要作为 [ABI 稳定性（ABI stability）](https://github.com/apple/swift/blob/master/docs/ABIStabilityManifesto.md)主题的一部分来考虑。部分出于这个原因，我们决定在[阶段 2](https://forums.swift.org/t/swift-4-stage-2-starts-now/5203) 中开启关于 `Dictionary` 的[更广泛讨论](https://forums.swift.org/t/dictionary-enhancements/5204)。
> 
> 对于 [Swift 3](https://github.com/apple/swift-evolution/blob/master/releases/swift-3_0.md) 和 [Swift 4](https://forums.swift.org/t/looking-back-on-swift-3-and-ahead-to-swift-4/3610)，核心团队为每个发布版本设定了主题。_核心团队希望更早地让社区参与进来，以帮助定义未来发布版本的主题，但他们仍在思考最佳方式。_

Swift 4.0 还要等半年才到来，但推测 Swift 5 的主题永远不嫌早。肯定有 [ABI 稳定性](https://github.com/apple/swift/blob/master/docs/ABIStabilityManifesto.md)，但还有别的吗？更多的字符串改进？并发？反射？
