---
title: 在 UIKit 中向属性字符串添加表格
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/adding-tables-to-attributed-strings
source_url: 'https://developer.apple.com/documentation/uikit/adding-tables-to-attributed-strings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/adding-tables-to-attributed-strings.json'
content_hash: 'sha256:97946514f8c71aab'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [TextKit](textkit.md)

# 在 UIKit 中向属性字符串添加表格

<sub>文章</sub>

在属性字符串中创建并配置表格，并将其显示在文本视图中。

## 概述

[NSTextTable](nstexttable.md) 及其相关类让你可以在所有 Apple 平台上，将由行和列组成的表格直接嵌入到 [NSAttributedString](../foundation/nsattributedstring.md) 对象中。[NSAttributedString](../foundation/nsattributedstring.md) 将字符串与逐字符的格式属性（例如字体、颜色和段落样式）一起存储，是 UIKit 文本视图的主要文本类型。你需要通过三个对象来构建一个表格：

- **[NSTextTable](nstexttable.md)** 代表整个表格，并定义列数和布局算法。
- **[NSTextTableBlock](nstexttableblock.md)** 代表单个单元格，记录该单元格的行、列和跨度值。它属于某个父表格。
- **[NSTextBlock](nstextblock.md)** 是基类，它定义了表格和各个单元格所共享的视觉属性（背景颜色、边框、内边距、外边距）。

你可以通过创建一个 [NSTextTable](nstexttable.md)，然后为每个单元格创建一个 [NSTextTableBlock](nstexttableblock.md)，并使用 [textBlocks](nsparagraphstyle/textblocks.md) 将每个块分配给属性字符串中的一个段落，来构建表格。文本系统会读取相邻段落的 [textBlocks](nsparagraphstyle/textblocks.md) 数组，以确定表格的结构。

### 创建表格及其单元格

首先创建表格并配置其列数。以下代码展示了如何创建一个具有三个等宽列的表格，并启用折叠边框，使相邻单元格共享同一条边框线：

```swift
let table = NSTextTable()
table.numberOfColumns = 3
table.collapsesBorders = true
```

然后为每个单元格创建一个块，指定其在表格中的位置和跨度。以下辅助函数会在指定的行和列创建一个单元格，将其宽度设置为可用空间的三分之一，并应用浅灰色背景、分隔线颜色的 1 点边框，以及四条边各 4 点的内边距：

```swift
func makeCell(row: Int, column: Int, in table: NSTextTable) -> NSTextTableBlock {
    let cell = NSTextTableBlock(
        table: table,
        startingRow: row, rowSpan: 1,
        startingColumn: column, columnSpan: 1
    )
    cell.setContentWidth(33, type: .percentage)
    cell.backgroundColor = UIColor.secondarySystemBackground
    cell.setBorderColor(.separator)
    cell.setWidth(1, type: .absolute, for: .border)
    cell.setWidth(4, type: .absolute, for: .padding)
    return cell
}
```

### 将单元格应用于段落

每个单元格恰好对应属性字符串中的一个段落。使用 `NSMutableParagraphStyle.textBlocks` 将该单元格块分配给对应的段落。以下代码通过为每个位置创建一个单元格块，并将每个单元格对应的样式化段落追加到属性字符串中，构建了一个 2×3 的表格——两行三列：

```swift
let string = NSMutableAttributedString()

for row in 0..<2 {
    for column in 0..<3 {
        let cell = makeCell(row: row, column: column, in: table)

        let style = NSMutableParagraphStyle()
        style.textBlocks = [cell]

        let cellText = NSAttributedString(
            string: "Row \(row), Col \(column)\n",
            attributes: [.paragraphStyle: style]
        )
        string.append(cellText)
    }
}
```

[textBlocks](nsparagraphstyle/textblocks.md) 数组按照从最外层到最内层的块进行排序。对于没有嵌套块的表格，每个单元格段落都只有一个包含单一元素的数组。

### 配置各边的宽度和颜色

你可以使用 [- setWidth:type:forLayer:rectEdge:](<nstextblock/setwidth(__type_for_rectedge_).md>) 和 [- setBorderColor:rectEdge:](<nstextblock/setbordercolor(__rectedge_).md>)，为每一条边分别独立设置宽度和边框颜色。例如，以下代码为某个单元格的底边应用了一条 2 点宽的蓝色边框，而其他边保持不变：

```swift
cell.setWidth(2, type: .absolute, for: .border, rectEdge: .maxYEdge)
cell.setBorderColor(.systemBlue, rectEdge: .maxYEdge)
```

使用 [CGRectEdge](../corefoundation/cgrectedge.md) 的值 [CGRectEdge.minXEdge](../corefoundation/cgrectedge/minxedge.md)（前缘）、[CGRectEdge.maxXEdge](../corefoundation/cgrectedge/maxxedge.md)（后缘）、[CGRectEdge.minYEdge](../corefoundation/cgrectedge/minyedge.md)（顶部）和 [CGRectEdge.maxYEdge](../corefoundation/cgrectedge/maxyedge.md)（底部）。

要支持 iOS 26 及更早版本，使用 [- setWidth:type:forLayer:](<nstextblock/setwidth(__type_for_).md>) 和 [- setBorderColor:](<nstextblock/setbordercolor(__).md>) 为所有边应用统一的宽度或颜色。

### 选择布局算法

默认情况下，[NSTextTableLayoutAlgorithmAutomatic](nstexttable/layoutalgorithm-swift.enum/automatic.md) 会根据内容分配宽度。当你希望列宽根据内容自适应时——例如一个标签-值表格，其中较短的标签旁边是长度各异的值——请使用 [NSTextTableLayoutAlgorithmAutomatic](nstexttable/layoutalgorithm-swift.enum/automatic.md)。

如果你希望无论内容长度如何，都得到一致、可预测的列宽，请使用 [NSTextTableLayoutAlgorithmFixed](nstexttable/layoutalgorithm-swift.enum/fixed.md)，它会根据在第一行单元格上设置的显式 [contentWidth](nstextblock/contentwidth.md) 值来分配宽度。例如，如果你的 App 显示一个数据网格，其中每一列始终占据可用宽度的三分之一，可以将第一行的每个单元格都设置为 33%，并切换到固定布局：

```swift
table.layoutAlgorithm = .fixed
```

### 显示结果

将属性字符串赋值给 [UITextView](uitextview.md) 即可渲染该表格。文本系统会读取字符串中嵌入的段落样式信息，自动解读表格结构，因此无需对视图做额外配置：

```swift
textView.attributedText = string
```

## 另请参阅

### Formatting and attributes

- [NSParagraphStyle](nsparagraphstyle.md) — 属性字符串的段落或标尺属性。
- [NSMutableParagraphStyle](nsmutableparagraphstyle.md) — 一个用于更改段落样式属性中子属性值的对象。
- [NSTextTab](nstexttab.md) — 段落中的一个制表符。
- [NSTextList](nstextlist.md) — 构成单个列表的一段文本。
</content>
