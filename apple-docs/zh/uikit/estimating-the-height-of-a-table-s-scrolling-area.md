---
title: 估算表格滚动区域的高度
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/estimating-the-height-of-a-table-s-scrolling-area
source_url: 'https://developer.apple.com/documentation/uikit/estimating-the-height-of-a-table-s-scrolling-area'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/estimating-the-height-of-a-table-s-scrolling-area.json'
content_hash: 'sha256:376d84110597372e'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Views and controls](views-and-controls.md) · [Table views](table-views.md)

# 估算表格滚动区域的高度

<sub>文章</sub>

为表格视图的页眉、页脚和行提供高度估算值，以确保滚动能准确反映内容的大小。

## 概述

只要有可能，表格视图就会为单元格、页眉和页脚使用高度估算值，以提升性能和滚动行为。表格视图在屏幕上出现之前，必须计算其内容视图的高度，因为它需要这些信息来配置与滚动相关的参数。如果你不为条目提供预估高度，表格视图就必须提前计算条目的实际高度，这可能开销很大。

> [!important] 重要
> 如果你的表格视图包含自适应尺寸的单元格、页眉或页脚，你必须为这些条目提供预估高度。

表格视图会根据标准的页眉、页脚和行样式，为表格视图的条目提供默认的高度估算值。如果你表格中的条目明显比默认值短或长，你可以通过为表格的 [estimatedRowHeight](uitableview/estimatedrowheight.md)、[estimatedSectionHeaderHeight](uitableview/estimatedsectionheaderheight.md) 和 [estimatedSectionFooterHeight](uitableview/estimatedsectionfooterheight.md) 属性赋值来提供自定义估算值。如果各个条目的高度各不相同，可以使用委托对象的以下方法提供自定义估算值：

- [- tableView:estimatedHeightForRowAtIndexPath:](<uitableviewdelegate/tableview(__estimatedheightforrowat_).md>)
- [- tableView:estimatedHeightForHeaderInSection:](<uitableviewdelegate/tableview(__estimatedheightforheaderinsection_).md>)
- [- tableView:estimatedHeightForFooterInSection:](<uitableviewdelegate/tableview(__estimatedheightforfooterinsection_).md>)

在估算页眉、页脚和行的高度时，速度比精度更重要。表格视图会为表格中的每一个条目请求估算值，因此不要在委托方法中执行长时间运行的操作。相反，生成的估算值只需足够接近，能对滚动有用即可。当条目出现在屏幕上时，表格视图会用条目的实际高度替换你的估算值。

下面的示例代码为不同高度的表格行计算预估高度。第一行的单元格始终使用一种包含多行文本的自定义样式。所有其他行都使用表格视图提供的基本（Basic）样式。

```swift
let cellMarginSize: CGFloat = 4.0
override func tableView(_ tableView: UITableView, 
         estimatedHeightForRowAt indexPath: IndexPath) -> CGFloat {
   // Choose an appropriate default cell size.
   var cellSize = UITableView.automaticDimension
        
   // The first cell is always a title cell. Other cells use the Basic style.
   if indexPath.row == 0 {
      // Title cells consist of one large title row and two body text rows.
      let largeTitleFont = UIFont.preferredFont(forTextStyle: .largeTitle)
      let bodyFont = UIFont.preferredFont(forTextStyle: .body)
            
      // Get the height of a single line of text in each font.
      let largeTitleHeight = largeTitleFont.lineHeight + largeTitleFont.leading
      let bodyHeight = bodyFont.lineHeight + bodyFont.leading
            
      // Sum the line heights plus top and bottom margins to get the final height.
      let titleCellSize = largeTitleHeight + (bodyHeight * 2.0) + (cellMarginSize * 2)

      // Update the estimated cell size.
      cellSize = titleCellSize
   }
        
   return cellSize
}
```

当表格视图使用高度估算值时，它会主动管理从其滚动视图继承来的 [contentOffset](uiscrollview/contentoffset.md) 和 [contentSize](uiscrollview/contentsize.md) 属性。不要尝试直接读取或修改这些属性。它们的值只对 [UITableView](uitableview.md) 有意义。

## 另请参阅

### 相关文档

- [创建自适应尺寸的表格视图单元格](creating-self-sizing-table-view-cells.md) — 创建支持动态字体、并使用系统间距约束来调整文本标签周围间距的表格视图单元格。

### 表格管理

- [UITableViewController](uitableviewcontroller.md) — 一个专门用于管理表格视图的视图控制器。
- [UITableViewDelegate](uitableviewdelegate.md) — 用于管理选择、配置分区页眉和页脚、删除和重新排序单元格，以及在表格视图中执行其他操作的方法。
- [UITableViewFocusUpdateContext](uitableviewfocusupdatecontext.md) — 一个上下文对象，提供与某次焦点从一个视图更新到另一个视图相关的信息。
