---
title: 'UITableView 的构造、绘制与管理（再访）| Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/12/uitableview-construction-drawing-and.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:322d5dd4b9344025'
translated: true
---

> 原文：[UITableView 的构造、绘制与管理（再访）| Cocoa with Love](https://www.cocoawithlove.com/2010/12/uitableview-construction-drawing-and.html)　·　Cocoa with Love (Matt Gallagher)

在这篇文章中，我将展示我目前在多个项目中使用来构造和管理 UITableView 的类。这些代码融合并演化自我在早期几篇文章中介绍的一些想法，包括关于表格视图中异质单元格和简易自定义表格视图绘制的文章。不过，此次实现为了持续简化在 iOS 中创建定制表格和视图的任务，也选择了一些不同的做法。

## 引言

在本文中，我展示了以下示例应用。

![](https://www.cocoawithlove.com/assets/objc-era/TableViewRevisited.png)

> 下载示例应用的 Xcode 项目：[TableDesignRevisited.zip](https://www.cocoawithlove.com/assets/objc-era/TableDesignRevisited.zip)（65kB）

该应用包含一个带有 3 个分区的顶层表格视图。每个分区包含不同类型的行，具有不同的构造、绘制和行为。"Simple text" 行显示文本，可被选中，但随即取消选中，不执行其他操作。"Rows loaded from NIBs" 行在被点击时推入一个 "Detail View Controller"。"Editable Text Fields" 分区包含可点击编辑的行。

此示例类的目的是演示我在包含这些类型元素的基本 iOS 应用中用于构建视图和控制器的方法和实现。

这篇文章是对多位读者的回应，他们阅读了我早期关于 `UITableView` 和 `UITableViewController` 技巧与实践的文章，并询问我的方法在过去几年中是否有所改变。

## 示例应用的关键特性

该应用对表格视图和单元格的使用展示了众多非常有利的特性：

- **异质**（即不同类型）视图在单个表格中共存，无需条件代码来区分其行为
- **完全自定义绘制的表头、行和背景**——我意识到此示例应用中的行在分组的 `UITableView` 中可能看起来与 Apple 标准的 `UITableViewCell` 非常相似，但如果你凑近看，会注意到单元格的背景是微妙的从左到右渐变，而表格的背景是微妙的渐变，而非标准表格纹理（并且选中颜色完全不同）。所有自定义绘制都可以轻松修改或调整，使应用看起来新颖独特，或者也可以禁用以恢复为默认绘制代码
- 所有默认的行和表头绘制都可以处理 **"grouped" 或 "plain"** 两种 UITableView 样式（因此你不受限于某一种美学风格）
- **完全动画化**地插入和移除所有表格视图单元格
- 该应用展示了**通过代码构造以及从 NIB 文件加载**的视图和单元格，并使从 NIB 加载表格和单元格的代码路径快速便捷
- 表格由**自定义的 `UIViewController` 管理，而非 `UITableViewController`**。这意味着它避免了 `UITableViewController` 只能管理 `UITableView` 的限制——你可以将其他视图作为层级的一部分加载进来
- **视图滚动以避免键盘遮挡文本**（这是 `UITableViewController` 最大的优势）由自定义的 `UIViewController` 处理，因此保留了此 `UITableViewController` 的功能

## 随时间的演变

其中一些特性是我之前所写文章的一部分，包括：

- [Heterogeneous cells in a `UITableViewController`](https://www.cocoawithlove.com/2008/12/heterogeneous-cells-in.html)
- [Recreating `UITableViewController` to increase code reuse](https://www.cocoawithlove.com/2009/03/recreating-uitableviewcontroller-to.html)
- [Easy custom `UITableView` drawing](https://www.cocoawithlove.com/2009/04/easy-custom-uitableview-drawing.html)

本文中的代码最接近于最初 "Heterogeneous cells" 文章的后继。许多简化 `UITableViewController` 实现的想法仍然来自那篇文章。

具体来说，在基类中自动处理 `UITableView` 数据源和委托方法的 "Heterogeneous cells" 目标延续到了此代码中。来自 "Easy custom `UITableView` drawing" 的方法——通过设置子视图来自定义单元格绘制，而非将绘制代码放入 `UITableViewCell`——也在此处沿用。

然而，在风格和方法上有一些变化。

### 减少代码中的视图构造

除了最简单的视图外，我现在很少再通过代码构造视图，而是倾向于从 NIB 文件加载大部分视图。

我最初坚持使用 NIB 文件是因为我觉得 iOS 2 的 Interface Builder 功能不足，精确配置仍然需要在代码中进行设置。早期也存在性能方面的顾虑，但后来证明并不准确。如果你还记得：[代码构造很少带来速度优势](https://www.cocoawithlove.com/2010/03/load-from-nib-or-construct-views-in.html)，而且通常阅读起来不美观，难以维护。

因此，反对 NIB 文件的论点被证明是不准确或过时的，所需要的仅仅是允许无缝使用 NIB 文件进行加载的代码。

虽然为 `UIViewController` 加载 NIB 是标准 API 的一部分，但对于 `UITableViewCell` 来说则不那么明确。我采用的方法通常是只从 NIB 加载 `UITableViewCell` 的 content view——只需重写 `-nibName` 方法即可，非常简单。

在此类中，没有从 NIB 文件加载表格分区表头的简便路径，但自定义表格表头相当少见，我认为这并不重要。

### 移除专用的 Cell Controller 类

Cell Controller 类最初存在的目的是将控制器直接绑定到行的数据，并将控制与继承自视图的 `UITableViewCell` 保持分离。

Cell Controller 是 [Heterogeneous cells in a UITableViewController](https://www.cocoawithlove.com/2008/12/heterogeneous-cells-in.html) 文章的一个关键特性，但坦率地说，它与其周围的类集成得并不好。此外，从 `UITableViewCell` 的子视图连接 target/action 到 Cell Controller 在某些情况下也可能引起小问题。

相反，我选择接受 `UITableViewCell` 实际上是一个控制器（尽管它继承自 `UIView`），并将大部分单元格控制代码放在其中。与此相关，我不使用 `UITableViewCell` 进行任何绘制（这由 content view、background view 和 selected background view 完成）。`UITableViewCell` 仅仅是加载这些其他视图并将其连接到数据的控制器。

移除 Cell Controller 类还有一个额外优势：进一步解耦了行的数据与控制器（现在是 `UITableViewCell` 子类）。行数据与指向所需 `UITableViewCell` 子类的指针一起存储，但两者之间的连接仅在准备显示单元格时才建立。在此之前，行数据不直接连接到任何视图控制器；这是一种更好的方法，可以在 `UITableView`/`UITableViewCell` 架构内工作。

### 完全动画化，很少使用 reloadData

原始 Heterogeneous cells 实现的另一个问题是它需要完全构造表格的所有数据和单元格控制器，然后调用 `-[UITableView reloadData]` 在新的状态下重新创建整个表格。

新的实现侧重于将行和分区动画化地移入和移出表格，操作行和分区的方法都以此为重点。

当然，你也可以传递 `UITableViewRowAnimationNone` 作为动画，这样之后就需要调用 `reloadData`，因此旧的方法仍然可行。

### 对行和分区索引的宽容处理

在此实现中，操作行和分区的方法会尝试修正行索引或在出错时创建缺失的分区。其意图并非鼓励懒惰，而是在 bug 出现时能更宽容。让一行出现在表格的错误分区中，总好过整个程序因索引越界问题而崩溃。

## 实现与使用方法

## 视图控制器中的代码

`RootViewController` 是主屏幕的控制器（如上方截图所示）。

此视图中的行都以类似的方式构造（每个分区使用不同的单元格类，每行使用不同的数据）。以下是 "Rows loaded from NIBs" 分区中的行是如何构造的：

```objc
[self addSectionAtIndex:1 withAnimation:UITableViewRowAnimationFade];
for (NSInteger i = 0; i < 4; i++)
{
    [self
        appendRowToSection:1
        cellClass:[NibLoadedCell class]
        cellData:[NSString stringWithFormat:
            NSLocalizedString(@"This is row %ld", @""), i + 1]
        withAnimation:(i % 2) == 0 ?
            UITableViewRowAnimationLeft :
            UITableViewRowAnimationRight];
}
```

行的视图在此单一语句中配置完毕。你需要指定：

- 数据
- 用于在数据进入视图时控制和显示数据的类
- 行在分区/行层级中的位置
- 用于将单元格动画化地移入视图的动画

显然，这里使用的 "数据" 相当简单：只是 `NSString` 和 `NSDictionary` 实例。在真实程序中，你会将每个行的模型对象作为 `cellData` 参数传入。

与最初的 "Heterogeneous cells" 文章一样，一旦这些声明式工作完成，视图控制器中就不需要额外的工作了；`UITableViewDataSource` 和 `UITableViewDelegate` 的实现会自动处理。

动画不是必需的；你可以指定 `UITableViewRowAnimationNone`，然后在准备好刷新表格时调用 `-[UITableView reloadData]` 或 `-[UITableView reloadSections:withRowAnimation:]`。

## 表格视图单元格子类中的代码

每个行的实现也旨在尽可能简单。`NibLoadedCell` 的实现——完全自定义绘制、自定义布局、自定义行高和自定义操作——只有三个简短的方法：

```objc
+ (NSString *)nibName
{
    return @"NibCell";
}

- (void)handleSelectionInTableView:(UITableView *)aTableView
{
    [super handleSelectionInTableView:aTableView];
    
    NSInteger rowIndex = [self indexPath].row;
    [((PageViewController *)aTableView.delegate).navigationController
        pushViewController:
            [[[DetailViewController alloc] initWithRowIndex:rowIndex] autorelease]
        animated:YES];
}

- (void)configureForData:(id)dataObject
    tableView:(UITableView *)aTableView
    indexPath:(NSIndexPath *)anIndexPath
{
    [super configureForData:dataObject tableView:aTableView indexPath:anIndexPath];
    
    label.text = dataObject;
}
```

秉承让常见情况最简单化的传统，你需要做的只是设置 `-nibName`，默认实现就知道如何加载 nib 并设置一系列属性，包括基于 nib 文件中视图大小的默认行高。

常见行为，如选中后取消选中行，由 `handleSelectionInTableView:` 的 `super` 实现自动处理；而 `configureForData:tableView:indexPath:` 的默认实现则处理自定义行背景和选中背景的设置。

## 灵活性

该架构允许你根据工作方式不同而采取不同的做法。

例如：`LabelCell` 和 `TextFieldCell` 在其 `finishConstruction` 实现中通过代码构造，而 `NibLoadedCell` 则通过重写 `-nibName` 方法并返回其 NIB 文件名从 NIB 加载。类似地，`RootViewController` 的表格通过重写 `-loadView` 方法在代码中构造，而 `DetailViewController` 则简单地通过重写 `-nibName` 方法并返回其 NIB 文件名从 NIB 文件加载。

这些行通过在 `configureForData:tableView:indexPath:` 中调用 `super` 实现来使用 `PageCellBackground` 进行绘制。你可以轻松避免在此处调用 `super` 实现，以恢复为标准的 `UITableViewCell` 绘制。

想要默认的 `UITableView` 表头而不是自定义绘制的表头？移除 `RootViewController` 中 `-viewDidLoad` 方法里的 `self.useCustomHeaders = YES;` 这一行即可。

自定义绘制视图会在 `UITableViewStyleGrouped` 或 `UITableViewStylePlain` 样式下自行绘制。你可以通过更改 `RootViewController` 的 `loadView` 方法中创建的表格样式来查看区别。

## 工作原理

这些代码在任何方面都并非开创性。大部分代码之所以能工作，仅仅是因为基类中的默认行为：

- **PageViewController**——处理（几乎所有）数据源和委托方法。如果你将此视图控制器设为表格中任何 UITextField 的委托，它还将处理表格的滚动和视图大小调整，以使文本字段不被屏幕键盘遮挡。
- **PageCell**——从 NIB 文件加载 `UITableViewCell` 的 `contentView`（如果指定）。此外，或作为替代，你可以在 `finishConstruction` 方法中配置或构造 `contentView`。此方法还向 `PageViewController` 提供行的信息，包括行高（可以从 NIB 中提取）。其他方法包括一组可重写的方法，用于处理视图的配置（用于连接视图和数据，或以其他方式准备视图进行显示）以及处理视图中的触摸。
- **PageCellBackground**——以 `UITableViewStylePlain` 或 `UITableViewStyleGroup` 样式绘制自定义单元格背景。`PageCellBackground` 在 `PageCell` 的 `configureForData:tableView:indexPath:` 默认实现中被应用（因此你可以通过子类化此方法并且不调用 super 实现来禁用它）。或者，如果你只想更改单元格背景的美学样式，你也可以通过重写 `+[PageCell pageCellBackgroundClass]` 方法来更改所使用的 `PageCellBackground` 子类。

## 缺失的特性或无法处理的情况

### 行数据的不同结构

如同我在最初的 "Heterogeneous cells" 文章中提到的那样，此实现中使用的方法通过对你的数据结构做出一些假设，简化了默认的 UITableViewController 模板。具体来说，它假设表格中每一行的数据都已加载，并且为每行的数据构造了一个 `PageCellDescription`。

其缺点是，当前的实现无法以其现有形式与任何要求以不同方式存储或组织数据的设计集成。不同存储安排的一个例子是使用 `NSFetchedResultsController` 获取的数据——你需要一个工作方式不同的基类来与 `NSFetchedResultsController` 加载和缓存数据的不同方法集成。

### 分区的声明式处理

正如我多次提到的，当前的 `PageViewController` 只处理了 `UITableView` 的 _几乎所有_ 数据源和委托方法。最大的遗漏是对分区表头的处理——设置分区表头的文本仍然需要实现 `tableView:titleForHeaderInSection:`。

查看代码，你可能可以通过将分区作为一个描述数据结构（类似于每行由一个 `PageViewCellDescription` 实例描述）来处理，从而做出一些小的改进。这将允许你在向表格添加分区时，将分区的标题、表头视图、表尾视图和其他分区属性绑定在一起。

不过，这带来的实际简化可能很小，所以我还没有费心去做。

### 为你自己的程序定制

虽然 `PageViewController`、`PageCell` 和 `PageCellBackground` 视图中的默认行为可以按原样工作，但它们的目的是允许在你自己的程序中进行简单的定制。

你程序中独特的类应该在子类中应用其独特的特性，但对于你想在整个程序中建立的默认行为，通常最简单的做法是将类似自定义绘制这样的自定义行为直接插入到 `PageCellBackground` 或 `-[PageViewController tableView:viewForHeaderInSection:]` 中。如果你的程序从不使用这些默认值，则无需保留它们。

## 总结

> 下载示例应用的 Xcode 项目：[TableDesignRevisited.zip](https://www.cocoawithlove.com/assets/objc-era/TableDesignRevisited.zip)（65kB）

本文中的代码并非特别高级——大多数常规的 iOS 程序员都能轻松自己弄明白。

反而，这篇文章只是基本揭示了我如何在自己的一些程序中构建视图，以便新开发者能够获得关于他们应该如何构建自己的表格、视图和控制器以在 iOS 中进行基本用户界面管理的想法。

自从我早期写关于 `UITableView` 及其管理的文章以来，这些代码代表了 2 年的迭代。或许有机会从这种演变中学习，或者也有机会从我早期的天真和更新奇的癖好中学习。我当然对我方法的演变感到满意，并且我认为这些类的当前状态代表了一个基础，你可以从中以比从 Apple 的 Xcode 模板开始少得多的代码非常快速地实现新的基于表格的视图。
