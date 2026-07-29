---
title: 传递非 Sendable 闭包的 Swift 并发技巧
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2024/06/05/swift-concurrency-non-sendable-closures/'
original_language: en
published: 2024-06-05
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ab3f64bc64e804cb'
translated: true
---

> 原文：[Swift concurrency hack for passing non-sendable closures](https://www.jessesquires.com/blog/2024/06/05/swift-concurrency-non-sendable-closures/)　·　Jesse Squires

如果你曾在代码库中尝试采用 [Swift 并发](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/)，那你一定处理过几十——很可能几百——条警告和错误。有些问题可以直接解决，也就是说你的代码确实有误，只需修正即可。但在其他场景中，解决方案并不那么直接。尤其是使用那些你无法控制、且尚未针对并发更新的 API 时，很难让编译器满意。又或者，你可能遇到过这样的情况：**你**知道代码是正确的，但**编译器**却无法验证其正确性——要么是因为 Swift 并发中尚存的几个 bug，要么是因为你使用了 `@preconcurrency` API。

你可能多次见到的一条警告是：“在 `@Sendable` 闭包中捕获了非 sendable 类型的‘variable’”。最近我在一个项目中遇到了这条警告，想分享一下我绕开它的技巧。这个问题是上面提到的多个因素共同导致的结果。我正在与 `@preconcurrency` API 交互，**而且**我知道我的代码是并发安全的，但无法向编译器准确表达这一点。

### 背景

首先，聊聊我处理这条并发警告的具体上下文。我一直在做一个使用 `UICollectionViewDiffableDataSource` 的项目，并且正在将 UIKit API 封装得更友好一些。为了本文的阐述，我简化了很多复杂性，提供一个清晰、简单的例子。

我有一个自定义的可差分数据源（diffable data source），它在后台线程上执行差异计算：

```
@MainActor
final class DiffableDataSource: UICollectionViewDiffableDataSource<String, String> {
    typealias Snapshot = NSDiffableDataSourceSnapshot<String, String>

    typealias SnapshotCompletion = @MainActor () -> Void

    let diffingQueue = DispatchQueue(label: "diffingQueue")

    func applyDiff(snapshot: Snapshot, animated: Bool = true, completion: SnapshotCompletion? = nil) {
        self.diffingQueue.async {
            self.apply(snapshot, animatingDifferences: animated, completion: completion)
        }
    }
}
```

根据[文档](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource/3375795-apply)，`completion` 闭包总是在主队列上调用，并且你可以从后台队列调用 `apply(_:animatingDifferences:completion:)`：

> […]
>
> **completion**
> 动画完成时执行的闭包。该闭包无返回值，也不接收参数。系统会从主队列调用此闭包。
>
> […]
>
> 你可以安全地从后台队列调用此方法，但必须在 App 中始终一致地使用。始终仅从主队列或后台队列调用此方法。

另外请注意，`UICollectionViewDiffableDataSource` 带有 `@MainActor @preconcurrency` 注解。

启用最严格的并发检查后，上面的代码会产生 2 条警告：

```
func applyDiff(snapshot: Snapshot, animated: Bool = true, completion: SnapshotCompletion? = nil) {
    self.diffingQueue.async {
        self.apply(snapshot, animatingDifferences: animated, completion: completion)
        //                                                               ^
        // 在 `@Sendable` 闭包中捕获了非 sendable 类型 'DiffableDataSource.SnapshotCompletion?'（又名 'Optional<@MainActor () -> ()>'）
        // 将 '@MainActor () -> Void' 类型的函数值转换为 '() -> Void' 会丢失全局 Actor 'MainActor'；这在 Swift 6 中是一个错误
    }
}
```

一种解决方案是让 completion 闭包成为 `@Sendable`：

```
func applyDiff(snapshot: Snapshot, animated: Bool = true, completion: @escaping @Sendable () -> Void) {
    self.diffingQueue.async {
        self.apply(snapshot, animatingDifferences: animated, completion: completion)
    }
}
```

（注意，这种情况下我们不能使用已定义的 typealias `SnapshotCompletion`，而且它不能是可选值。）

不过，这行不通。这个 API 会更新集合视图（collection view）以反映快照中的数据状态，而且如前所述，`completion` 会在主线程上调用。`applyDiff(snapshot:)` 的调用方会在此 completion 闭包中执行额外的 UI 更新和动画，或处理 `@MainActor` 的成员和类型。这些成员和类型不能被标记为 `@Sendable`。例如，`DiffableDataSource` 实例的所有者可能是一个视图控制器（view controller）。此外，我不想对调用方强加 `@Sendable` 限制。

因此，将闭包设为 `@Sendable` 会在调用处产生如下错误：

```
self.dataSource.applyDiff(snapshot: snapshot) {

    // 在同步非隔离上下文中调用主要 Actor 隔离的实例方法 'someMethod()'

    // 主要 Actor 隔离的属性 'someProperty' 不能从 Sendable 闭包中引用；这在 Swift 6 中是一个错误
}
```

调用方可以将有问题的代码包裹在 `Task { @MainActor in }` 或 `MainActor.assumeIsolated { }` 中来消除这些问题。但这对调用方而言是一种负担，而且包装后的 API 也无法准确传达实际情况。我们需要的不是 `@Sendable () -> Void` 闭包，而是 `@MainActor () -> Void` 闭包。

于是我们陷入了这样的困境：Swift 编译器告诉我们捕获的闭包需要是 `@Sendable`，但我们无法让它成为 `@Sendable`；编译器还告诉我们闭包丢失了 `@MainActor`，但我们知道该闭包总是会在主队列上被调用。由于这两个问题，我们需要找到一种方法来绕过警告，并强制编译器按我们的意愿行事。

### 解决方案（一个技巧）

我们可以将 completion 闭包包装在另一个遵守 `@unchecked Sendable` 的类型中。

```
struct UncheckedCompletion: @unchecked Sendable {
    typealias Block = () -> Void

    let block: Block?

    init(_ block: Block?) {
        if let block {
            self.block = {
                dispatchPrecondition(condition: .onQueue(.main))
                block()
            }
        } else {
            self.block = nil
        }
    }
}
```

这样就能消除“在 `@Sendable` 闭包中捕获非 sendable 类型”的警告。再次强调，UIKit 保证这个 completion 闭包总是在主线程上调用，我们可以使用 `dispatchPrecondition()` 来验证这一点。

我们可以更新 API 来使用这个新的 `UncheckedCompletion` 包装器。

```
func applyDiff(snapshot: Snapshot, animated: Bool = true, completion: UncheckedCompletion) {
    self.diffingQueue.async {
        self.apply(snapshot, animatingDifferences: animated, completion: completion.block)
    }
}
```

然而，将 `UncheckedCompletion` 暴露给调用方也不是好的 API。我们应该隐藏这个细节。我们可以将 `applyDiff()` 方法再用另一个方法来包装，使用原始的 `SnapshotCompletion` 类型别名。

```
func applyDiff(_ snapshot: Snapshot, animated: Bool = true, completion: SnapshotCompletion? = nil) {
    self.applyDiff(snapshot: snapshot, animated: animated, completion: UncheckedCompletion(completion))
    //                                                                 ^ 包装在 UncheckedCompletion 中
}

private func applyDiff(snapshot: Snapshot, animated: Bool, completion: UncheckedCompletion) {
    self.diffingQueue.async {
        self.apply(snapshot, animatingDifferences: animated, completion: completion.block)
        //                                                               ^ 访问底层闭包
    }
}
```

现在，对调用方来说，公开的 API 看起来和之前完全一样，但他们可以在 completion 闭包中安全地使用 `@MainActor` 成员和类型，而不会出现任何警告或错误。

```
self.dataSource.applyDiff(snapshot: snapshot) {
    // 在这里可以安全地使用 @MainActor 做任何事情，没有警告或错误
}
```

### 这好吗？

这是个好主意吗？说实话，我也不确定！但在这种情况下，这似乎是最好的做法。如果你面临类似的情况——即**你知道**捕获的闭包总是在主线程上调用，并且你无法让它成为 `@Sendable`——那么这或许对你也是一种不错的解决方案！不过，试图将其通用化可能**不是个好主意**。请明智地使用！

##### [更新](#updated-05-june-2024)  _2024 年 6 月 5 日_

不出所料，[Matt Massicotte](https://mastodon.social/@mattiem) 出手相助，[在这里提供了一个更简单的解决方案](https://mastodon.social/@mattiem/112565464652182320)。虽然我的巧妙技巧确实有效，但我们还可以让闭包同时具有 `@Sendable` **和** `@MainActor`。之后，只需将调用 completion 闭包的代码包裹在 `MainActor.assumeIsolated { }` 中即可。以下是需要做的改动：

```
// 添加 @Sendable 有点奇怪，但 Swift 5.10 需要它。
// Swift 6（通过 SE-0434）将使其不再必要。
typealias SnapshotCompletion = @Sendable @MainActor () -> Void

func applyDiff(snapshot: Snapshot, animated: Bool = true, completion: SnapshotCompletion? = nil) {
    self.diffingQueue.async {
        // UIKit 保证 `completion` 在主队列上调用。
        self.apply(snapshot, animatingDifferences: animated, completion: {
            // 当你知道它处于主要 Actor 上（例如来自文档），但该信息未在 API 中编码时，
            // 你可以使用动态隔离来使其工作。
            MainActor.assumeIsolated {
                completion?()
            }
        })
    }
}
```

这很棒。代码少了很多。我不确定为什么我当初没有**尝试**为闭包使用 `@Sendable @MainActor`。可能是因为我假设 `@MainActor` **隐含**了 `@Sendable`——显然它**应该如此**，并且在 Swift 6 的 [SE-0434](https://github.com/apple/swift-evolution/blob/main/proposals/0434-global-actor-isolated-types-usability.md) 之后**也会如此**。

无论如何，这个技巧的总体思路在其他上下文中可能仍然有用——特别是如果你无法采用 Swift 6，需要停留在 Swift 5.10 上时。
