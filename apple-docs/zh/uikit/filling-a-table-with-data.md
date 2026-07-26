---
title: 用数据填充表格
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/filling-a-table-with-data
source_url: 'https://developer.apple.com/documentation/uikit/filling-a-table-with-data'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/filling-a-table-with-data.json'
content_hash: 'sha256:c3693530689dc91f'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Views and controls](views-and-controls.md) · [Table views](table-views.md)

# 用数据填充表格

<sub>文章</sub>

使用数据源对象动态创建和配置表格的单元格，或从故事板中静态提供它们。

## 概述

表格视图是界面中由数据驱动的元素。你可以通过一个数据源对象（一个采用 [UITableViewDataSource](uitableviewdatasource.md) 协议的对象），提供 App 的数据，以及在屏幕上渲染每条数据所需的视图。表格视图会在屏幕上排布你的视图，并与数据源对象协作以保持数据最新。

表格视图将你的数据组织为行和分区。行显示单个数据条目，分区将相关的行分组在一起。分区不是必需的，但对于组织已经具有层级结构的数据来说，它们是一种很好的方式。例如，「通讯录」App 会在一行中显示每个联系人的姓名，并根据姓氏的首字母将行分组到不同的分区中。

![](../../../attachments/716ef5e53d97bc3630380a6c3a5a7c51/filling-a-table-with-data-1@2x.png)

<sub>展示「通讯录」App 的示意图。「通讯录」App 主表格中的分区对应字母表中的字母。行对应单个联系人。</sub>

### 提供行数和分区数

表格视图在屏幕上出现之前，会要求你指定行和分区的总数。你的数据源对象通过两个方法提供这些信息：

```swift
func numberOfSections(in tableView: UITableView) -> Int  // Optional 
func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int
```

在实现这些方法时，请尽可能快地返回行数和分区数。这可能要求你以便于检索行和分区信息的方式来组织数据。例如，考虑使用数组来管理表格的数据。数组是组织分区和行的良好工具，因为它们与表格视图本身的自然组织方式相匹配。

下面的示例代码展示了数据源方法的一种实现，该方法返回多分区表格中的行数和分区数。在这个表格中，每行显示一个字符串，因此该实现为每个分区存储一个字符串数组。为了管理这些分区，该实现使用了一个数组的数组（称为 `hierarchicalData`）。要获取分区数，数据源返回 `hierarchicalData` 数组中的条目数。要获取特定分区中的行数，数据源返回相应子数组中的条目数。

```swift
var hierarchicalData = [[String]]() 
 
override func numberOfSections(in tableView: UITableView) -> Int {
   return hierarchicalData.count
}
   
override func tableView(_ tableView: UITableView, 
                        numberOfRowsInSection section: Int) -> Int {
   return hierarchicalData[section].count
}

```

### 定义行的外观

你可以在故事板文件中使用单元格来定义表格中行的外观。单元格是一个 [UITableViewCell](uitableviewcell.md) 对象，充当表格行的模板。单元格是视图，它们可以包含你需要用来显示内容的任何子视图。你可以向其内容区域添加标签、图像视图和其他视图，并使用约束来排布这些视图。

当你向 App 的界面添加一个表格视图时，它会包含一个供你配置的原型单元格。要添加更多原型单元格，选中该表格视图并更新其 Prototype Cells 属性。每个单元格都有一种样式，定义了它的外观。你可以选择 UIKit 提供的标准样式之一，或者定义自己的自定义样式。

下图展示了一个包含两个原型单元格的表格，每个单元格都使用了一种标准单元格样式。

![展示 Xcode 故事板编辑器中带有两个原型单元格的表格的示意图。](../../../attachments/af11edfd0856ca8bff5973faec0d1652/filling-a-table-with-data-2@2x.png)

在你的故事板文件中，为每个原型单元格执行以下操作：

- 将单元格样式设为 `custom`，或将其设为标准单元格样式之一。
- 为单元格的 Identifier 属性赋一个非空字符串。
- 对于自定义单元格，向该单元格添加视图和约束。
- 在 Identity inspector 中指定自定义单元格的类。

在创建带有自定义视图的单元格时，定义一个 [UITableViewCell](uitableviewcell.md) 的子类来管理这些视图。在你的子类中，为显示 App 数据的自定义视图添加出口，并将这些出口连接到故事板文件中的实际视图。你需要用这些出口在运行时配置单元格。

有关如何配置单元格外观的更多信息，请参阅[为表格配置单元格](configuring-the-cells-for-your-table.md)。

### 为每一行创建和配置单元格

在表格视图出现在屏幕上之前，它会要求其数据源对象为表格可见部分内或附近的行提供单元格。请从数据源对象的 [- tableView:cellForRowAtIndexPath:](<uitableviewdatasource/tableview(__cellforrowat_).md>) 方法中快速响应，以避免性能问题。按以下模式实现此方法：

1. 调用表格视图的 [- dequeueReusableCellWithIdentifier:forIndexPath:](<uitableview/dequeuereusablecell(withidentifier_for_).md>) 方法来获取一个单元格对象。
2. 使用 App 的自定义数据配置单元格的视图。
3. 将单元格返回给表格视图。

对于标准单元格样式，[UITableViewCell](uitableviewcell.md) 包含你需要配置的视图所对应的属性。对于自定义单元格，你需要在设计时向单元格添加视图，并添加出口来访问它们。

下面的示例代码展示了数据源方法的一个版本，用于配置一个包含单个文本标签的单元格。该单元格使用基本（Basic）样式，即标准单元格样式之一。对于基本样式的单元格，[UITableViewCell](uitableviewcell.md) 的 [textLabel](uitableviewcell/textlabel.md) 属性包含一个你可以用数据配置的标签视图。

```swift
override func tableView(_ tableView: UITableView,
                        cellForRowAt indexPath: IndexPath) -> UITableViewCell {
   // Ask for a cell of the appropriate type.
   let cell = tableView.dequeueReusableCell(withIdentifier: "basicStyleCell", for: indexPath)
        
   // Configure the cell’s contents with the row and section number.
   // The Basic cell style guarantees a label view is present in textLabel.
   cell.textLabel!.text = "Row \(indexPath.row)"
   return cell
}
```

表格视图不会要求你为表格的每一行都创建单元格。相反，表格视图会惰性地管理单元格，只向你请求那些位于表格可见部分内或附近的单元格。惰性创建单元格可以减少表格使用的内存量。不过，这也意味着你的数据源对象必须快速创建单元格。不要在 [- tableView:cellForRowAtIndexPath:](<uitableviewdatasource/tableview(__cellforrowat_).md>) 方法中加载表格的数据或执行耗时的操作。

> [!note] 注意
> 除了使用标准单元格样式外，你还可以定义包含任意所需视图的自定义单元格。有关配置单元格的详细信息，请参阅[为表格配置单元格](configuring-the-cells-for-your-table.md)。

### 预取数据以提升性能

表格视图的滚动性能至关重要。如果为表格获取数据涉及一项开销较大的操作，比如从数据库中获取数据，请使用预取数据源对象——一个采用 [UITableViewDataSourcePrefetching](uitableviewdatasourceprefetching.md) 协议的对象——在数据滚动进入可视区域之前异步开始加载它。

有关如何实现预取数据源的信息，请参阅 [UITableViewDataSourcePrefetching](uitableviewdatasourceprefetching.md)。

### 在故事板中静态指定数据

在原型设计期间，或当表格内容永远不会改变时，使用静态表格可以节省时间。使用静态表格时，你需要预先在故事板文件中指定表格的全部数据；你不需要实现数据源对象。在运行时，UIKit 会从故事板中加载该数据并为你管理它。由于你无法在运行时更改静态表格中的数据，请在正式发布的 App 中谨慎使用它们。

在故事板文件中配置静态表格：

1. 向故事板添加一个 [UITableViewController](uitableviewcontroller.md) 对象。
2. 选中该表格视图控制器的表格视图。
3. 在 Attributes inspector 中将表格视图的 Content 属性更改为 `Static Cells`。
4. 使用表格视图的 Sections 属性指定表格的分区数。
5. 将每个分区的 Row 属性设为你想要的行数。
6. 用你想要的视图和内容配置每个单元格。

> [!important] 重要
> 包含静态数据的表格视图需要一个 [UITableViewController](uitableviewcontroller.md) 对象来管理该数据。

如果你有可能在未来想要更新表格视图的内容，就不要使用静态数据。将数据源对象赋给一个表格视图包含静态数据的 [UITableViewController](uitableviewcontroller.md) 是一种编程错误。

## 另请参阅

### 数据

- [异步地将图像加载到表格视图和集合视图中](asynchronously-loading-images-into-table-and-collection-views.md) — 异步地存储和获取图像，让你的 App 响应更灵敏。
- [UITableViewDataSource](uitableviewdatasource.md) — 一个对象为管理数据、并为表格视图提供单元格而采用的方法。
- [UITableViewDataSourcePrefetching](uitableviewdatasourceprefetching.md) — 一种协议，为表格视图的数据需求提前发出警示，让你能提早开始可能长时间运行的数据操作。
- [UITableViewDiffableDataSource](uitableviewdiffabledatasource-2euir.md) — 你用来管理数据、并为表格视图提供单元格的对象。
- [NSDiffableDataSourceSnapshot](nsdiffabledatasourcesnapshot-swift.struct.md) — 视图中数据在特定时间点状态的一种表示。
- [UILocalizedIndexedCollation](uilocalizedindexedcollation.md) — 一个对象，用于组织、排序和本地化带有分区索引的表格视图的数据。
- [UIDataSourceTranslating](uidatasourcetranslating.md) — 用于管理数据源对象的高级接口。
- [UIRefreshControl](uirefreshcontrol.md) — 一种标准控制，可用于发起滚动视图内容的刷新。
