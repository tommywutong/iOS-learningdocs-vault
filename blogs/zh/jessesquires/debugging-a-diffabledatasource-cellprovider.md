---
title: 调试 DiffableDataSource 的 CellProvider
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2021/07/11/debugging-diffabledatasource-cellproviders/'
original_language: en
published: 2021-07-11
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0ec6378c1f19ec45'
translated: true
---

> 原文：[Debugging a DiffableDataSource CellProvider](https://www.jessesquires.com/blog/2021/07/11/debugging-diffabledatasource-cellproviders/)　·　Jesse Squires

我最近在做一个 iOS 项目，该项目使用了[现代集合视图（collection view）](https://developer.apple.com/documentation/uikit/views_and_controls/collection_views/implementing_modern_collection_views)——也就是[可差分数据源（diffable data source）](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource)、[快照（snapshot）](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot)和[单元格提供器（cell provider）](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource/cellprovider)。我把所有组件都接好了，集合视图也工作了——至少我当时是这么以为的。但在更新集合视图时，我注意到了某些非常奇怪且不可预测的行为：有时候单元格更新正确，其他时候则是看到重复或丢失的数据。下面是问题所在。

为了便于理解，我把示例代码简化了。实际项目中我用视图模型（view model）来封装集合视图及其配置的大部分功能。

以下是最初的视图模型和可差分数据源代码的精简版：

```
struct ViewModel {
    // 其他视图模型代码

    func dequeueAndConfigureCellFor(collectionView: UICollectionView, at indexPath: IndexPath) -> UICollectionViewCell {
        // 创建、配置并返回一个单元格
        let cellConfig = self.cellConfiguration(at: indexPath)
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: cellConfig.cellId, for: indexPath)
        cell.configure(with: cellConfig)
        return cell
    }
}

typealias DiffableDataSource = UICollectionViewDiffableDataSource<String, String>

extension DiffableDataSource {
    convenience init(collectionView: UICollectionView, viewModel: ViewModel) {
        self.init(collectionView: collectionView) { collectionView, indexPath, itemIdentifier in
            return viewModel.dequeueAndConfigureCellFor(collectionView: collectionView, at: indexPath)
        }
    }
}
```

`ViewModel` 封装了大量数据、配置和功能。这里需要指出的是，`ViewModel` 处理了所有的单元格配置。然后，我们将 `ViewModel` 实例传递给 `DiffableDataSource`，在数据源的 `CellProvider` 闭包中使用该视图模型来出队并配置单元格。最后，在视图控制器（view controller）中把所有内容连接起来。

```
class ViewController: UICollectionViewController {
    var viewModel = ViewModel()

    lazy var dataSource: DiffableDataSource = {
        DiffableDataSource(collectionView: self.collectionView, viewModel: self.viewModel)
    }()

    override func viewDidLoad() {
        super.viewDidLoad()
        self.collectionView.dataSource = self.dataSource
    }
}
```

创建 `DiffableDataSource` 后，将其赋值给集合视图的 dataSource。乍一看一切正常。但是当我通过应用新的[快照](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource/3375795-apply)来更新集合视图时，遇到了奇怪的行为。假设集合中有 4 个单元格 `[A, B, C, D]`，更新后得到的结果可能是 `[A, B, B, D]`、`[B, B, D, C]` 或 `[A, C, D, D]`。所以……发生了什么？

问题在于 `ViewModel` 是一个 `struct`——值类型（value type）——它在 `CellProvider` 闭包中被捕获，因而在初次加载后从未更新。碰巧集合视图中始终有相同数量的项，因此从未发生越界错误——否则可能会更早暴露问题。值得重申的是，实际代码比示例代码复杂得多。因此在这个例子中显而易见的问题，在实际的应用程序代码中完全不是那么明显。

如何修复这个 Bug？我们需要避免捕获视图模型。有几种可能的解决方案。首先，你可以把 `ViewModel` 改为 `class`——引用类型（reference type）。在我的情况中这不是一个选项，因为 `ViewModel` 设计为无状态的，并且是由底层模型类型生成的。另一个解决方案是捕获一个**拥有**视图模型的引用类型。如果还没有明确的拥有者，你可以把 `ViewModel` 包装在某种容器类中。在上面的示例中，真正的问题是 `DiffableDataSource` 扩展中定义的 `convenience init`——那里发生了不正确的捕获。我们应该移除这个方法，改用主指定初始化方法，然后在闭包中捕获视图控制器。

```
class ViewController: UICollectionViewController {
    var viewModel = ViewModel()

    lazy var dataSource: DiffableDataSource = {
        DiffableDataSource(collectionView: self.collectionView) { [unowned self] view, indexPath, itemId in
            self.dequeueAndConfigureCellFor(collectionView: view, at: indexPath)
        }
    }()

    override func viewDidLoad() {
        super.viewDidLoad()
        self.collectionView.dataSource = dataSource
    }

    func dequeueAndConfigureCellFor(collectionView: UICollectionView, at indexPath: IndexPath) -> UICollectionViewCell {
        self.viewModel.dequeueAndConfigureCellFor(collectionView: collectionView, at: indexPath)
    }
}
```

通过这段代码，我们正确地捕获了 `self`——即拥有 `viewModel` 的视图控制器（引用类型）。当 `dataSource` 调用单元格提供器来配置单元格时，它会引用视图控制器上的新方法，后者将调用转发给视图模型。这确保了始终引用最新版本的视图模型——该视图模型会基于底层数据频繁重新生成。

还需要注意，在 `CellProvider` 闭包中我们把 `self` 捕获为 `unowned` 而不是 `weak`——这能防止循环引用，但比使用 `weak` “更不安全”，因为它表现为隐式展开的可选值。我们可以推理出这里安全使用 `unowned` 的原因：`self` 拥有 `dataSource`，因此在 `dataSource` 和闭包的整个生命周期中 `self` 始终存在。

再次说明，此示例代码已经简化以说明问题。在你自己的项目中，你可能希望将所有视图模型和数据源代码封装在视图控制器之外。

这里的重要收获是确保**不要在你传递给可差分数据源的单元格提供器闭包中捕获值类型**。相比实现老式的 [`UICollectionViewDataSource` 协议](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource)，我喜欢使用“现代集合视图”API，但它们确实引入了不同类型的复杂性，也带来了犯细微错误的新机会。
