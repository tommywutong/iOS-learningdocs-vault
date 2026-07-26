---
title: IGListKit - 开篇
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/iglistkit-first/'
original_language: zh
published: 2020-11-30
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0afd9be7279d61df'
translated: n/a
---

> 原文：[IGListKit - 开篇](https://dirtmelon.github.io/posts/iglistkit-first/)　·　dirtmelon

## UICollectionView/UITableView

作为一个 iOS 开发者，在日常开发中少不了与 `UITableView/UICollectionView` 打交道。因为复用池的存在，即使在处理大量数据的情况下，它们仍能保持较低的内存占用，而简单的 `DataSource/Delegate` 设计方式，可以让我们只需要几行代码就可以完成对 `UITableView/UICollectionView` 数据和交互的相关配置。由于 `UITableView` 对界面布局的限制，你无法在 `UITableView` 中自定义布局，比如瀑布流之类的样式。于是苹果在 iOS6.0 中推出了 `UICollectionView` ， [Steipete](https://twitter.com/steipete) 为了支持更老旧的系统，自己写了个 [PSTCollectionView](https://github.com/steipete/PSTCollectionView) ，通过这个框架可以大致了解 `UICollectionView` 的内部实现。 虽然 `UICollectionView` 通过把 `Layout` 抽出来的方式以提供自定义布局，但是在处理数据时本质上和 `UITableView` 还是相同的。 日常使用 `UICollectionView/UITableView` 时都会遇到下面几个问题：

- 复用流程。如果想在 `UITableView/UICollectionView` 中复用 `Cell` ，那么你需要先调用`register(_:forCellReuseIdentifier:)` 注册对应的 `Cell` 类型，然后在对应的方法中调用 `dequeueReusableCell(withIdentifier:)` 从复用池中取出或者生成一个新的 `Cell` 来使用。如果在获取 `Cell` 前忘记调用 `register` 进行注册，那么你就会收获一个应用崩溃，至于为什么需要先进行注册， [register(_:forCellReuseIdentifier:)](https://developer.apple.com/documentation/uikit/uitableview/1614888-register) 有简单说明；
- 不支持 `diff` 。在数据源变化时我们需要更新对应的界面，而苹果本身并没提供一套相关的 API 给我们计算相关的删除，插入或者更新的位置（ `indexPath` ），我们需要自己去计算，找出更新的数据源，然后删除，插入或者更新对应的 `Cell` 。在大多数情况下，由于有复用机制的存在，我们直接使用 `reloadData` 也不会有什么问题，复用机制使得在 `reloadData` 时只会对显示在屏幕上的 `Cell` 进行处理，需要处理视图数量并不多，但是应该有更好的办法来支持 `diff` ，不是么？（ PS ：苹果在 WWDC19 上推出 Diffable Data Source 功能，支持局部刷新）；
- 模块的隔离。在界面变得复杂时，我们需要处理数据的获取，处理 `Cell` 的配置，处理埋点统计之类的功能，对于这些模块的隔离，系统本身的框架并没有提供这么一套东西给我们，所以很多时候会写在 `ViewController` 里，于是变成了 `Massive View Controller` 。如果自行设计一套方案，很容易弄出一套不但使用起来非常难受，而且还难以迁移的框架。

## IGListKit

`IGListKit` 是 Instagram 推出的一套数据驱动的 `UICollectionView` 框架，以此来创建快速灵活的列表界面，为什么选择 `UICollectionView` 而不是 `UITableView` ，因为 `UICollectionView` 支持自定义布局，比 `UITableView` 更加灵活。 `IGListKit` 的主要特性如下：

- 不再需要调用 `performBatchUpdates(_:, completion:)` 或者 `reloadData()` ；
- 更好的架构以复用 `Cell` 和组件；
- 支持多种数据类型；
- 与 `diff` 算法解耦；
- 全面的单元测试；
- 支持对自己的数据模型进行自定义 `diff` 操作；
- 使用 `UICollectionView` 更加简单；
- 可扩展的 API ；
- 使用 `Objective-C` 编写，同时完全支持 `Swift` 。

`IGListKit` 的数据处理流程如下：

![1kER0gFAQIVjfYIX2ByJP8Q](https://raw.githubusercontent.com/dirtmelon/blog-images/main/1kER0gFAQIVjfYIX2ByJP8Q.png)

数据经由 `Adapter` 进行处理后转给对应的 `SectionController` ，而 `SectionController` 则会根据不同的数据类型来返回不同的 `Cell` 。整个过程中， `UIViewController` 只和 `Adapter` 和 `Updater` 进行交互，并根据不同的数据类型返回不同的 `SectionController` 。而对于 `Cell` 的处理则完全交给 `SectionController` 来进行，这一步的好处是使得 `SectionController` 可以进行复用，扩大复用粒度，同时 `SectionController` 的复用粒度也是比较合适的。因为我们可能需要对不同的 `UIViewController` 进行配置，但是有很大可能它们的 `Cell` 显示方式都是相同，只是其它一些逻辑或者 UI 不同。我们也可以经由 `SectionController` 进行组装，合成不同的界面。

使用 `IGListKit` 时，创建一个列表界面就会变得非常容易。 首先我们需要创建一个 `IGListSectionController` 的子类，需要重写的方法有两个：

1. `cellForItemAtIndex:` ；
2. `sizeForItemAtIndex:` 。 下面以 `LabelSectionController` 为例子进行说明：

```swift
class LabelSectionController: ListSectionController {
  override func sizeForItem(at index: Int) -> CGSize {
    return CGSize(width: collectionContext!.containerSize.width, height: 55)
  }

  override func cellForItem(at index: Int) -> UICollectionViewCell {
    return collectionContext!.dequeueReusableCell(of: MyCell.self, for: self, at: index)
  }
}
```

可以看到 `Cell` 的配置和数据的处理都交给了 `SectionController` 来进行。完成 `LabelSectionController` 的配置后，需要在 `UIViewController` 或者其它什么地方把各个模块串联起来：

```swift
let layout = UICollectionViewFlowLayout()
let collectionView = UICollectionView(frame: .zero, collectionViewLayout: layout)

let updater = ListAdapterUpdater()
let adapter = ListAdapter(updater: updater, viewController: self)
adapter.collectionView = collectionView
```

可以看到 `UICollectionView` 设置布局 `Layout` 部分没有变动，但是使用了 `IGListAdapter` 和 `IGListAdapterUpdater` 将 `UIViewController` 和 `UICollectionView` 串起来。这里使用了默认的 `UICollectionViewFlowLayout` 和 `IGListAdapterUpdater` ，你也可以配置自定义的类来使用一些高级特性。

跟 `UICollectionView` 类似，需要给 `adapter` 设置 `dataSource` ：

```swift
adapter.dataSource = self

// IGListAdapterDataSource 相关方法
func objects(for listAdapter: ListAdapter) -> [ListDiffable] {
  // this can be anything!
  return [ "Foo", "Bar", 42, "Biz" ]
}

func listAdapter(_ listAdapter: ListAdapter, sectionControllerFor object: Any) -> ListSectionController {
  if object is String {
    return LabelSectionController()
  } else {
    return NumberSectionController()
  }
}

func emptyView(for listAdapter: ListAdapter) -> UIView? {
  return nil
}
```

你可以返回任何数据类型，只要它们支持 `IGListDiffable` 协议就可以了。

### 不可变

返回的数据应该是不可变的。如果你返回可变的对象且你会对它们进行编辑， `IGListKit` 就无法正确地计算出它们之间的差异。这是因为对象已经发生了改变。因此，该对象的改动就会丢失掉。你可以返回一个新的，不可变的对象，而且支持了 `IGListDiffable` 协议。

`IGListKit` 的基本用法和大概架构已经介绍完毕，更详细的介绍可以看官方文档： [IGListKit Reference](https://instagram.github.io/IGListKit/index.html) ，后续会对源码进行解析。
