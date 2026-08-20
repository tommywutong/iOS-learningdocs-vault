---
title: Swift 与 Objective-C 中的协议组合
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2017/06/05/protocol-composition-in-swift-and-objc/'
original_language: en
published: 2017-06-05
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4b74d5bab6022fd8'
translated: true
---

> 原文：[Protocol composition in Swift and Objective-C](https://www.jessesquires.com/blog/2017/06/05/protocol-composition-in-swift-and-objc/)　·　Jesse Squires

Swift 和 Objective-C 中的[协议（Protocol）](https://developer.apple.com/library/content/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html)是解耦代码的强大工具。它们让你能在使用协议的类之间约定一份契约，但将具体实现推迟到符合者（conformer）去完成。它们让你能够[划分接口](https://en.wikipedia.org/wiki/Interface_segregation_principle)并[反转控制](https://en.wikipedia.org/wiki/Dependency_inversion_principle)。Swift 和 Objective-C 中协议的一个有趣之处在于，协议的成员可以是*可选的*（Swift 中的 `optional` 或 Objective-C 中的 `@optional`）。然而，这带来了一系列缺点，并降低了代码的健壮性，因此人们通常会避免使用。不过，拥有可选成员有时确实是你设计中合理的概念模型。那么，你该如何设计协议，使其在不使用 `optional` 或 `@optional` 的情况下提供可选语义呢？

### `@optional` 的问题

我们先从 Objective-C 说起。可选协议方法是在 Objective-C 2.0 中引入的，并在 Cocoa 和 Cocoa Touch 中被广泛使用。例如，在使用 UIKit 工作时，你一直都在实现带有可选方法的协议。然而，尽管它们很普遍，却普遍不被鼓励，并被认为是一种糟糕的设计。这是因为在 Objective-C 中，如果方法被标记为 `@optional`，你就会失去编译期检查。如果一个方法是可选的，那么编译器就无法强制要求符合者实现它。另一方面，如果你声明了符合某个协议，却没有实现必需的方法，就会产生错误。因此，*调用方有责任*在调用可选方法之前检查 [`-respondsToSelector:`](https://developer.apple.com/reference/objectivec/1418956-nsobject/1418583-respondstoselector)。如果你忘记了这个检查，而该类没有实现可选方法，你的程序会在运行时崩溃，并抛出“does not respond to selector”异常。

考虑下面的例子：

```
@protocol MyViewControllerDelegate <NSObject>

- (void)didDismissController:(MyViewController *)controller;

@optional
- (void)controller:(MyViewController *)controller didSelectItem:(MyItem *)item;

@end

@interface MyViewController : UIViewController

@property (nonatomic, weak) id<MyViewControllerDelegate> delegate;

@end
```

在 `delegate` 上调用必需方法很直接：

```
[self.delegate didDismissController:self];
```

而对于可选方法，你不仅失去了编译器的帮助，而且每次需要向 `delegate` 对象发送消息时，还要承担检查 `-respondsToSelector:` 的额外运行时开销。

```
if ([self.delegate respondsToSelector:@selector(controller:didSelectItem:)]) {
    [self.delegate controller:self didSelectItem:item];
}
```

### `optional` 的问题

Swift 解决了上述的安全问题，并为可选成员提供了便捷的 `?` 语法：

```
delegate?.controller?(self, didSelect: item)
```

在这种情况下，你不必担心 Swift 中的运行时崩溃，但还有另一个问题。在 Swift 中，`optional` 并*不是*真正“语言的一部分”或“纯 Swift”特性——这个功能依赖于 Objective-C 运行时，并且**它仅仅是为了与 Objective-C 互操作而存在**。任何包含可选成员的 Swift 协议都必须被标记为 `@objc`。[我以前写过](https://www.jessesquires.com/blog/2016/06/04/avoiding-objc-in-swift/)关于如何在 Swift 代码中尽可能避免 `@objc`。当 `@objc` 侵入你的对象图时，几乎所有东西都必须继承自 `NSObject`，这意味着你不能使用 Swift 的结构体、枚举或其他优秀特性。这让你不是在写 Swift，而只是“使用新语法的 Objective-C”。显然，`optional` 在 Swift 中算不上一项真正的选择。

### “永不使用可选”的解决方案

一种朴素的解决方案是干脆永远不使用 `optional` 或 `@optional`。这简单直接，对于简单的情况来说很棒。你提供一个严格的契约，并避免了上述缺点，但在许多情况下，这给符合协议的类带来了不必要的负担。你最终会得到一堆空方法，或者像 `nil`、`-1` 或 `false` 这样的哨兵值（sentinel value）方法。看看大家熟悉的 [`UITableViewDataSource`](https://developer.apple.com/reference/uikit/uitableviewdatasource) 协议。它有两个必需方法和**九个**可选方法。想象一下，如果所有这些方法都是 `@required`，但你却想放弃这些行为，那你就得保留九个空的方法存根，或者对于 [`tableView(_: titleForHeaderInSection:) -> String?`](https://developer.apple.com/reference/uikit/uitableviewdatasource/1614850-tableview) 这样的方法，你必须返回 `nil`。

### 使用多个协议和属性

一个更好的方法是将大型协议拆分成更小的协议，并为每个小协议提供一个唯一的属性（比如委托（delegate））。再次以 [`UITableViewDataSource`](https://developer.apple.com/reference/uikit/uitableviewdatasource) 为例。这些方法有着清晰的语义分组。它可以很容易地被拆分成多个协议，而 `UITableView` 可以为每个协议提供一个属性。Ash Furrow [有一篇很棒的文章](https://ashfurrow.com/blog/protocols-and-swift/)正是关于如何做到这一点的。因此，我们可以按以下方式重新构想这些 API：

```
class TableView {
    weak var dataSource: TableViewDataSource?
    weak var titlesDataSource: TableViewTitlesDataSource?
    weak var reorderingDataSource: TableViewReorderingDataSource?

    // 以此类推...
}

protocol TableViewDataSource: class {
    func numberOfSections(in tableView: UITableView) -> Int
    func tableView(tableView: TableView, numberOfRowsInSection section: Int) -> Int
    func tableView(tableView: TableView, cellForRowAtIndexPath indexPath: IndexPath) -> TableViewCell
}

protocol TableViewTitlesDataSource: class {
    func tableView(tableView: TableView, titleForHeaderInSection section: Int) -> String?
    func tableView(tableView: TableView, titleForFooterInSection section: Int) -> String?
}

protocol TableViewReorderingDataSource: class {
    func tableView(tableView: TableView, canMoveRowAtIndexPath indexPath: IndexPath) -> Bool
    func tableView(tableView: TableView, moveRowAtIndexPath sourceIndexPath: IndexPath, toIndexPath destinationIndexPath: IndexPath)
}

// 以此类推...
```

这种设计将“可选性”从协议本身转移到了类中的一个额外可选属性上。如果你想要在表格视图（table view）中使用页眉和页脚，你可以通过设置 `titlesDataSource` 来选择启用。要选择放弃，你可以将这个属性设为 `nil`。`reorderingDataSource` 同样如此，以此类推。初看起来，这种设计对 `UITableView` 很合适。许多方法彼此之间没有直接关系，且存在清晰的语义分组。然而在实践中，访问多个独立的属性来查询同一个底层数据源会显得很别扭。

```
// 通过 `dataSource` 访问 sections
let sections = dataSource?.tableView(tableView: self, numberOfRowsInSection: 0)

// 通过 `titlesDataSource` 访问标题
let headerTitle = titlesDataSource?.tableView(tableView: self, titleForHeaderInSection: 0)

// 通过 `reorderingDataSource` 访问重新排序
let canMove = reorderingDataSource?.tableView(tableView: self, canMoveRowAtIndexPath: IndexPath(row: 0, section: 0))
```

拥有这些分离的协议和属性并不理想。尽管有很好的语义分组，但这些方法*都是相关的*，因为它们需要访问*相同的底层数据*才能协同工作。要容纳完整的 `UITableViewDataSource` 协议，将需要五个不同的协议，每个协议在 `UITableView` 上都有一个对应的属性。然后你可以以同样的方式重组 [`UITableViewDelegate`](https://developer.apple.com/reference/uikit/uitableviewdelegate) 协议，这至少会有 10 个协议和属性。拥有如此多的 `dataSource` 和 `delegate` 属性既不直观又繁琐。我们如何改进这一点呢？

### 组合协议

与其使用多个分离的协议，不如设计一个协议联合体。这提供了一个单一的、顶层的“入口点”来引用。你可以将一个协议中的可选成员提取到一个新的协议中，然后在原始协议上为这个新协议添加一个可选属性。其结果是一个全面的顶层协议和一组“嵌套”协议。

调整上面的表格视图例子：

```
class TableView {
    weak var dataSource: TableViewDataSource?
}

protocol TableViewDataSource: class {
    func numberOfSections(in tableView: UITableView) -> Int
    func tableView(tableView: TableView, numberOfRowsInSection section: Int) -> Int
    func tableView(tableView: TableView, cellForRowAtIndexPath indexPath: IndexPath) -> TableViewCell

    var titles: TableViewTitlesDataSource? { get }
    var reordering: TableViewReorderingDataSource? { get }
}

// 以此类推...
```

现在表格视图只有一个 `dataSource` 属性。其他协议仍然存在，但它们被融入到了 `titles` 和 `reordering` 属性中。这个设计的另一个积极方面是，嵌套协议的选择启用/选择放弃行为被显式声明了。`TableViewDataSource` 的符合者可以返回 `nil` 来选择放弃，或者返回 `self` 来选择启用这些额外的方法。

```
class MyDataSource: TableViewDataSource, TableViewTitlesDataSource {

    func numberOfSections(in tableView: UITableView) -> Int {
        // 返回 sections
    }

    func tableView(tableView: TableView, numberOfRowsInSection section: Int) -> Int {
        // 返回每个 section 的行数
    }

    func tableView(tableView: TableView, cellForRowAtIndexPath indexPath: IndexPath) -> TableViewCell {
        // 配置并返回一个单元格
    }

    var titles: TableViewTitlesDataSource? {
        // 选择启用页眉和页脚
        return self;
    }

    func tableView(tableView: TableView, titleForHeaderInSection section: Int) -> String? {
        // 返回页眉标题
    }

    func tableView(tableView: TableView, titleForFooterInSection section: Int) -> String? {
        // 返回页脚标题
    }

    var reordering: TableViewReorderingDataSource? {
        // 选择放弃重新排序
        return nil
    }
}
```

访问这些嵌套成员都通过一个单一的入口点：

```
let sections = dataSource?.tableView(tableView: self, numberOfRowsInSection: 0)

let headerTitle = dataSource?.titles?.tableView(tableView: self, titleForHeaderInSection: 0)

let canMove = dataSource?.reordering?.tableView(tableView: self, canMoveRowAtIndexPath: IndexPath(row: 0, section: 0))
```

这减少了 `UITableView` 的 API 表面积，因为它只有一个 `dataSource` 属性，而不是五个——更不用说拆分 `UITableViewDelegate` 后可能产生的 10 个 `delegate` 属性了。它统一了数据源协议的所有方法，而不必诉诸于使用 `optional`，同时允许你以简洁的方式选择放弃额外的行为。在 Objective-C 的情况下，对 `-respondsToSelector:` 的检查变成了简单的 `nil` 检查，并且编译器可以强制要求整个协议被实现。总的来说，它感觉更干净、更具内聚性，尤其是在调用点。

**更新：** [@IanKay](https://twitter.com/IanKay/status/871773445373149184) 指出，你可以[通过使用协议扩展（protocol extension）进一步减少子协议中的样板代码](https://gist.github.com/IanKeen/68eba888221a1a8de03dbbdd8a4dfcf1)。例如：

```
extension TableViewDataSource {
    var titles: TableViewTitlesDataSource? { return nil }
    var reordering: TableViewReorderingDataSource? { return nil }
}
```

更多细节请参见[完整的要点](https://gist.github.com/IanKeen/68eba888221a1a8de03dbbdd8a4dfcf1)。

### 结论

如我们所见，有很多方法可以设计出解决“可选协议问题”的方案。你可以设计一个完全避免可选性的模型，可以提供许多带有对应属性的协议，也可以设计一个协议的“嵌套组合”。每种情况都不同，但我经常发现这种嵌套组合的方法是最优雅、最强大、最直观的。
