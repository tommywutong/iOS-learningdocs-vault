---
title: '轻松自定义 UITableView 绘图 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/04/easy-custom-uitableview-drawing.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:bb7a4a2cdcf869c6'
translated: true
---

> 原文：[Easy custom UITableView drawing | Cocoa with Love](https://www.cocoawithlove.com/2009/04/easy-custom-uitableview-drawing.html)　·　Cocoa with Love (Matt Gallagher)

自定义 `UITableView` 确实很容易。我会向你展示如何完全自定义 `UITableView` 的外观，而无需重写或派生子类，也无需使用任何棘手的 hack。

## 让我的表格漂亮起来

大多数 iPhone App 的核心是 `UITableView`。要让你的 iPhone App 脱颖而出，最简单的方法就是让你的 `UITableView` 看起来美观。

自定义你的 `UITableView` 其实非常简单。你不需要自定义绘图代码，也不需要创建任何子类。Cocoa Touch 提供了你所需的所有绘图能力，你只需以正确的方式使用正确的类并提供布局即可。

## 示例应用

我将展示的方法会把左侧的表格变成右侧的表格：

![](https://www.cocoawithlove.com/assets/objc-era/customtableview.png)

_左侧：一个包含三行的默认 `UITableView`。右侧：同一表格视图自定义后的效果。_

## 如何失败地自定义 UITableView

从 Mac OS X 迁移过来让我更难适应——`UITableView` 需要以非常特定的方式进行自定义，并且在结构上与 Mac OS X 的 `NSTableView` 和 `NSCell` 绘图方式截然不同。

以下都是自定义表格的_**非常糟糕的方法**_（即使它们确实能用）：

- 派生 `UITableView` 的子类来自定义单元格的绘图
- 派生 `UITableViewCell` 的子类来自定义单元格内容的绘图
- 创建你自己的 `UITableViewCell` 数组并返回它们，而不是使用 `dequeueReusableCellWithIdentifier:`

关于第二点：自定义 `UITableViewCell` 是可以的——但你不应该用它来绘图。`UITableViewCell` 类更像是一个控制类——它处理行为和布局，而不是绘图。你可以自定义 `UITableViewCell` 来加载特定的 `contentView`（并在那里进行自定义绘图）。

最后一点（即你应该始终使用 `dequeueReusableCellWithIdentifier:`）只与绘图间接相关，但如果你绕过了正常的单元格队列架构，它将显著降低你的绘图速度。

## 如何成功地自定义 UITableView

关于表格绘图，只需理解几个要点。

**第一**：`UITableView` 本身除了背景之外不绘制任何东西。要自定义 `UITableView` 的背景，你只需将其 `backgroundColor` 设置为 `[UIColor clearColor]`，然后你可以在 `UITableView` _后面_的视图中绘制自己的背景。

**第二**：`tableHeaderView`（以及表格的 footer 和 section 的 header 及 footer）不一定只是一个标题。你可以在表格头部插入你自己的视图，以及它的子视图，从而自由地进行布局和自定义绘图。

**第三**：`UITableViewCell` 由 5 个不同的子视图组成。自定义正确的子视图是出色 `UITableViewCell` 绘图的秘诀。这些子视图是：

1. `backgroundView`——该行的整个背景（包括在 `UITableViewStyleGrouped` 样式表格中看起来是 `UITableView` 背景的部分）。
2. `selectedBackgroundView`——当行被选中时替换 `backgroundView`。
3. `image`——单元格左侧的一个可自定义图像（实际上不是一个子视图）。
4. `accessoryView`——单元格右侧的一个可自定义视图。
5. `contentView`——位于 `image` 和 `accessoryView` 之间的一个可自定义视图（技术上来说，它延伸到 `image` 的背后）。

你可以使用你自己自定义的绘图视图来自定义这些中的任何一项（除了 `image` 必须是 `UIImage`）。

然而，由于表格的像素大小不会改变，通常最简单的方法是直接为每个部分使用 `UIImageView`。然后，你可以将在其他程序中绘制的高度复杂的视图截取为所需的 5 个部分，并让 `UIImage` 的命名图像缓存的自动缓存机制为你管理内存。

有一种反对意见是不应该在代码中绘制视图，因为 iPhone 的绘图速度远不如 Mac OS X 快。像渐变和多个重叠组件这样的操作确实会给 iPhone 带来很大负担。

自定义绘图代码适用于简单和纯色绘图。在大多数其他情况下——正如本文中所示——我建议你使用 `UIImageView` 在表格中绘制你的视图。

## 实现

尽管所有自定义绘图都由 `UIImageView` 处理，但仍有一些工作要做。你必须处理所有的布局和视图配置。

### 配置 UITableView 和布局表格头部

作为这具体含义的示例，请看本文的 `viewDidLoad` 方法：

```objc
- (void)viewDidLoad
{
    //
    // Change the properties of the imageView and tableView (these could be set
    // in interface builder instead).
    //
    tableView.separatorStyle = UITableViewCellSeparatorStyleNone;
    tableView.rowHeight = 100;
    tableView.backgroundColor = [UIColor clearColor];
    imageView.image = [UIImage imageNamed:@"gradientBackground.png"];
    
    //
    // Create a header view. Wrap it in a container to allow us to position
    // it better.
    //
    UIView *containerView =
        [[[UIView alloc]
            initWithFrame:CGRectMake(0, 0, 300, 60)]
        autorelease];
    UILabel *headerLabel =
        [[[UILabel alloc]
            initWithFrame:CGRectMake(10, 20, 300, 40)]
        autorelease];
    headerLabel.text = NSLocalizedString(@"Header for the table", @"");
    headerLabel.textColor = [UIColor whiteColor];
    headerLabel.shadowColor = [UIColor blackColor];
    headerLabel.shadowOffset = CGSizeMake(0, 1);
    headerLabel.font = [UIFont boldSystemFontOfSize:22];
    headerLabel.backgroundColor = [UIColor clearColor];
    [containerView addSubview:headerLabel];
    self.tableView.tableHeaderView = containerView;
}
```

该方法处理 `tableView` 的配置（设置 `backgroundColor`、`rowHeight` 并在表格后面设置一个图像），同时还为表格头部创建了自己的布局。

这里的头部布局是针对表格的头部视图。你可以通过实现 `UITableViewDelegate` 方法 `tableView:viewForHeaderInSection:` 来为每个表格 section 包含一个自定义 header。表格和 section 的 footer 也有等效的属性和方法。

这种类型的布局可以在 Interface Builder 中处理，并通过加载 XIB 文件来实现。不过遗憾的是，在 iPhone 上，从 XIB 文件加载大量视图很慢（我怀疑这是由于从闪存读取速度慢），而且并不总能配置所有属性。

因此，我通常先在 Interface Builder 中勾勒我的视图，然后在代码中手动重新创建相同的内容。这就是我在这里所做的：为 `headerLabel` 选取在视图中看起来平衡的坐标。

### 单元格背景

单元格背景需要包含表格 "sections" 的顶部和底部。因此，`backgroundView` 和 `selectedBackgroundView` 通常需要逐行设置。

在你为给定行配置单元格的 `tableView:cellForRowAtIndexPath:` 方法中，以下代码将处理该行为：

```objc
UIImage *rowBackground;
UIImage *selectionBackground;
NSInteger sectionRows = [aTableView numberOfRowsInSection:[indexPath section]];
NSInteger row = [indexPath row];
if (row == 0 && row == sectionRows - 1)
{
    rowBackground = [UIImage imageNamed:@"topAndBottomRow.png"];
    selectionBackground = [UIImage imageNamed:@"topAndBottomRowSelected.png"];
}
else if (row == 0)
{
    rowBackground = [UIImage imageNamed:@"topRow.png"];
    selectionBackground = [UIImage imageNamed:@"topRowSelected.png"];
}
else if (row == sectionRows - 1)
{
    rowBackground = [UIImage imageNamed:@"bottomRow.png"];
    selectionBackground = [UIImage imageNamed:@"bottomRowSelected.png"];
}
else
{
    rowBackground = [UIImage imageNamed:@"middleRow.png"];
    selectionBackground = [UIImage imageNamed:@"middleRowSelected.png"];
}
((UIImageView *)cell.backgroundView).image = rowBackground;
((UIImageView *)cell.selectedBackgroundView).image = selectionBackground;
```

### 在 contentView 内布局

`contentView` 内元素的布局只需在构造 `contentView` 时设置（而不是逐行设置）。

可惜的是，在 `contentView` 中布局 `UILabel`（例如本例中的 "Cell at row X." 和 "Some other infomation." 标签）有点冗长。

以下代码在 `UITableViewCell` 分配后立即运行，用于定位 "Cell at row X." 标签：

```objc
const CGFloat LABEL_HEIGHT = 20;
UIImage *image = [UIImage imageNamed:@"imageA.png"];

//
// Create the label for the top row of text
//
topLabel =
    [[[UILabel alloc]
        initWithFrame:
            CGRectMake(
                image.size.width + 2.0 * cell.indentationWidth,
                0.5 * (aTableView.rowHeight - 2 * LABEL_HEIGHT),
                aTableView.bounds.size.width -
                    image.size.width - 4.0 * cell.indentationWidth
                        - indicatorImage.size.width,
                LABEL_HEIGHT)]
    autorelease];
[cell.contentView addSubview:topLabel];

//
// Configure the properties for the text that are the same on every row
//
topLabel.tag = TOP_LABEL_TAG;
topLabel.backgroundColor = [UIColor clearColor];
topLabel.textColor = [UIColor colorWithRed:0.25 green:0.0 blue:0.0 alpha:1.0];
topLabel.highlightedTextColor = [UIColor colorWithRed:1.0 green:1.0 blue:0.9 alpha:1.0];
topLabel.font = [UIFont systemFontOfSize:[UIFont labelFontSize]];

//
// Create a background image view.
//
cell.backgroundView = [[[UIImageView alloc] init] autorelease];
cell.selectedBackgroundView = [[[UIImageView alloc] init] autorelease];
```

在我看来，似乎应该有更高效的方法来实现这一点。我认为这种可能性是存在的。

这段代码大部分时间都在计算标签应该放置的位置。它需要位于图像的右侧，`accessoryView` 的左侧，行的中间，但在 "Some other information." 标签之上。

### 其他装饰

`accessoryView` 只是一个 `UIImageView`。`cell.image` 作为一个属性进行设置。这些都非常简单，但它们使表格单元格的影响力大大增强。

## 结论

> 你可以[下载 EasyCustomTable 项目（zip 文件）](https://www.cocoawithlove.com/assets/objc-era/EasyCustomTable.zip)（60kb）。

代码顶部包含一个 `#define`，允许你打开和关闭自定义绘图。

这些内容都不是什么革命性的东西（iPhone 文档中都有），但很容易错过那些使这一切变得简单的属性和方法。

这确实需要自定义图像。如果你从未绘制过任何东西，现在是学习 [inkscape](http://www.inkscape.org/) 的好时机（它是免费的，而且性价比很高）。你也可以使用 Adobe Illustrator，但如果你有那么多钱，不如请一位艺术家为你绘制。

在代码中布局内容可能是我所介绍方法中最薄弱的部分。为了简化操作，你可以先在 Interface Builder 中预先布局好一切，然后将布局复制到代码中。对于复杂的布局，你甚至可以尝试使用 [nib2objc](http://github.com/akosma/nib2objc/tree/master) 将你的 XIB 文件自动转换为代码（虽然我从未这样做过，但我提到 nib2objc 是因为这个想法太酷了）。
