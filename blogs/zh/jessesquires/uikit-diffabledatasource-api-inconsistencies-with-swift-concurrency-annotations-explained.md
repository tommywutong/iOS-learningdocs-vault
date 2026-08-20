---
title: 详解 UIKit DiffableDataSource 在 Swift 并发注解方面的 API 不一致问题
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2024/12/19/diffable-data-source-main-actor-inconsistency/'
original_language: en
published: 2024-12-19
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5e86041e72e83fb5'
translated: true
---

> 原文：[UIKit DiffableDataSource API inconsistencies with Swift Concurrency annotations explained](https://www.jessesquires.com/blog/2024/12/19/diffable-data-source-main-actor-inconsistency/)　·　Jesse Squires

UIKit 提供了两套可差分数据源（diffable data source）API，一套用于[集合](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa)，一套用于[表格](https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasource-2euir)。最近，我在开发 [ReactiveCollectionKit](https://www.jessesquires.com/blog/2024/10/18/introducing-reactivecollectionskit/) 时注意到，这些 API 在 iOS 18 SDK 中已针对 Swift 并发（Swift Concurrency）做了更新，但注解与文档却不一致。

使用快照（snapshot）的主要入口是 `apply(_:animatingDifferences:completion:)` 方法。这个方法在 [`UICollectionViewDiffableDataSource`](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/apply(_:animatingdifferences:completion:)) 和 [`UITableViewDiffableDataSource`](https://developer.apple.com/documentation/uikit/uitableviewdiffabledatasource-2euir/apply(_:animatingdifferences:completion:)) 中各有一个。两者的方法签名和文档完全相同。在 iOS 18 中，它们都被添加了 `@MainActor` 和 `@preconcurrency` 注解。

```
@MainActor @preconcurrency
func apply(
    _ snapshot: NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>,
    animatingDifferences: Bool = true,
    completion: (() -> Void)? = nil
)
```

然而，文档中却写道：

> 你可以从后台队列安全地调用此方法，但必须在你的 App 中始终一致地这样做。始终只从主队列或后台队列调用此方法。

如果你从后台队列调用这些方法，并尝试升级到 Swift 6，就会遇到问题。这是因为 Swift 6 并发使此方法无法从后台队列调用。编译器不允许你这样做，因为它是 `@MainActor` 而不是 `nonisolated`。那么……这是怎么回事？

我在 Mastodon 上联系了 UIKit 团队的 [Tyler Fox](https://mas.to/@smileyborg/)，询问这是否是一个错误。事实证明，这并不是错误，他的回复非常有帮助且见解深刻。为了留存记录和文档目的（也因为社交媒体是短暂且不可靠的），我将在这里转载[他的完整回复](https://mas.to/@smileyborg/113427085770601417)：

> 主要 Actor（main actor）注解是有意为之，详见随附的完整说明。不过遗憾的是，这里并没有完美的解决方案。
> 
> 另请务必参考[这份文档](https://developer.apple.com/documentation/uikit/views_and_controls/collection_views/updating_collection_views_using_diffable_data_sources)，了解关于可差分数据源的更多最佳实践，特别是如何使用合适的标识符（而不是轻量级数据结构），因为这是处理大数据集时实现高效性能的关键。
> 
> 这是 iOS 18 SDK 中对可差分数据源 API 做出的有意更改。现有的可差分数据源 API 和实现有严格的并发要求，而这些要求无法用 Swift 并发来表达（具体来说，它必须从单个调度队列中使用，而 `nonisolated` 无法表示这一点）。
> 
> 我们发现了一些因在后台队列/线程上使用可差分数据源而导致的问题，这样做的性能收益通常微乎其微，因为只有新旧快照中标识符的差异比较操作会在后台队列/线程上执行；而设置和执行 UI 更新以及单元格动画的工作始终在主线程上进行。因此，我们决定在使用 Swift 并发时将可差分数据源限制在主要 Actor 上，这样可以确保在所有情况下的正确性，而且无论如何这几乎总是最佳做法。如果你之前从后台队列应用快照，我们建议你更新实现，改为在主队列上执行。
> 
> 如果你担心性能问题，应该使用 Instruments（例如 Time Profiler）对你的 App 在大数据集下进行测量和剖析。你几乎肯定会发现，差异比较部分的工作（这是唯一可能不在主线程上进行的部分）与创建单元格、测量其大小、执行布局等 UI 更新相关工作相比微不足道。如果你确实在差异比较过程中看到了显著的工作量，请确保你使用了正确的标识符，并重新审视标识符的哈希和相等性实现。如果你的快照包含数万或数十万个项目（或更多），你可能希望使用分页等技术来减少 UI 中一次填充的项目总数。
> 
> 最后，如果你确实发现了一个你认为后台队列差异比较至关重要的用例，请务必提交反馈，以便我们了解该用例并提出建议，或考虑对 API 进行潜在的增强以更好地支持它。

如果你在使用这些 API 时遇到了问题，或者对文档中的不一致之处感到困惑，希望这篇文章能对你有所帮助！文档中仍然存在不一致之处，这并不理想。但是，我非常感激 Tyler 抽出时间回复并澄清了困惑。谢谢 Tyler！
