---
title: 为表格分区添加页眉和页脚
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/adding-headers-and-footers-to-table-sections
source_url: 'https://developer.apple.com/documentation/uikit/adding-headers-and-footers-to-table-sections'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/adding-headers-and-footers-to-table-sections.json'
content_hash: 'sha256:9c35d73d7bfbcf75'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Views and controls](views-and-controls.md) · [Table views](table-views.md)

# 为表格分区添加页眉和页脚

<sub>文章</sub>

通过为表格视图的分区添加页眉和页脚视图，在视觉上区分不同的行分组。

## 概述

使用页眉和页脚视图作为分区起止的视觉标记。页眉和页脚视图是可选的，你可以根据需要对它们进行或多或少的自定义。

![展示页眉和页脚如何将表格的行分组的示意图。](../../../attachments/173f629dbeaa114642f4e228d9039f4a/media-3162087@2x.png)

要创建一个带有文本标签的基本页眉或页脚，重写表格数据源对象的 [- tableView:titleForHeaderInSection:](<uitableviewdatasource/tableview(__titleforheaderinsection_).md>) 或 [- tableView:titleForFooterInSection:](<uitableviewdatasource/tableview(__titleforfooterinsection_).md>) 方法。表格视图会为你创建一个标准的页眉或页脚，并将其插入到表格中的指定位置。

```swift
// Create a standard header that includes the returned text.
override func tableView(_ tableView: UITableView, titleForHeaderInSection 
                            section: Int) -> String? {
   return "Header \(section)"
}

// Create a standard footer that includes the returned text.
override func tableView(_ tableView: UITableView, titleForFooterInSection 
                            section: Int) -> String? {
   return "Footer \(section)"
}

```

> [!note] 注意
> 页眉和页脚通常应用于单个分区，但你也可以通过使用表格视图的 [tableHeaderView](uitableview/tableheaderview.md) 或 [tableFooterView](uitableview/tablefooterview.md) 属性，为整个表格提供单一的页眉或页脚视图。全局页眉出现在表格内容的顶部，全局页脚出现在底部。

### 自定义页眉和页脚视图

自定义页眉和页脚视图能为表格的各个分区带来独特的外观。使用自定义页眉和页脚，你可以指定所需的视图，并将其放置在分配空间内的任意位置。你还可以为表格的不同分区提供不同的页眉或页脚视图。

要创建自定义页眉或页脚视图：

1. 使用 [UITableViewHeaderFooterView](uitableviewheaderfooterview.md) 对象来定义页眉和页脚的外观。
2. 将你的 [UITableViewHeaderFooterView](uitableviewheaderfooterview.md) 对象注册到你的表格视图。
3. 在你的表格视图委托对象中实现 [- tableView:viewForHeaderInSection:](<uitableviewdelegate/tableview(__viewforheaderinsection_).md>) 和 [- tableView:viewForFooterInSection:](<uitableviewdelegate/tableview(__viewforfooterinsection_).md>) 方法，以创建和配置你的视图。

始终为你的页眉和页脚使用 [UITableViewHeaderFooterView](uitableviewheaderfooterview.md) 对象。该视图支持与单元格相同的复用模型，让你可以回收视图，而不必每次都重新创建。注册好你的页眉或页脚视图后，使用表格视图的 [- dequeueReusableHeaderFooterViewWithIdentifier:](<uitableview/dequeuereusableheaderfooterview(withidentifier_).md>) 方法来请求该视图的实例。如果有可回收的页眉或页脚视图可用，表格视图会先返回这些视图，然后再创建新的视图。

你可以直接使用 [UITableViewHeaderFooterView](uitableviewheaderfooterview.md) 对象，并将视图添加到它的 [contentView](uitableviewheaderfooterview/contentview.md) 属性中，也可以对其进行子类化并添加你自己的视图。使用叠放视图或 Auto Layout 约束，将你的子视图定位在内容视图内部。要更改内容背后的背景，请修改页眉页脚视图的 [backgroundView](uitableviewheaderfooterview/backgroundview.md) 属性。下面的示例代码展示了一个自定义页眉视图，它在创建时对图像和标签视图进行了定位。

```swift
class MyCustomHeader: UITableViewHeaderFooterView {
    let title = UILabel()
    let image = UIImageView()

    override init(reuseIdentifier: String?) {
        super.init(reuseIdentifier: reuseIdentifier)
        configureContents()
    }

    func configureContents() {
        image.translatesAutoresizingMaskIntoConstraints = false
        title.translatesAutoresizingMaskIntoConstraints = false

        contentView.addSubview(image)
        contentView.addSubview(title)

        // Center the image vertically and place it near the leading
        // edge of the view. Constrain its width and height to 50 points.
        NSLayoutConstraint.activate([
            image.leadingAnchor.constraint(equalTo: contentView.layoutMarginsGuide.leadingAnchor),
            image.widthAnchor.constraint(equalToConstant: 50),
            image.heightAnchor.constraint(equalToConstant: 50),
            image.centerYAnchor.constraint(equalTo: contentView.centerYAnchor),
        
            // Center the label vertically, and use it to fill the remaining
            // space in the header view. 
            title.heightAnchor.constraint(equalToConstant: 30),
            title.leadingAnchor.constraint(equalTo: image.trailingAnchor, 
                   constant: 8),
            title.trailingAnchor.constraint(equalTo: 
                   contentView.layoutMarginsGuide.trailingAnchor),
            title.centerYAnchor.constraint(equalTo: contentView.centerYAnchor)
        ])
    }
}
```

作为配置表格视图的一部分，注册你的页眉视图。

```swift
override func viewDidLoad() {
   super.viewDidLoad()
   
   // Register the custom header view.
   tableView.register(MyCustomHeader.self, 
       forHeaderFooterViewReuseIdentifier: "sectionHeader")
}
```

在你的委托的 [- tableView:viewForHeaderInSection:](<uitableviewdelegate/tableview(__viewforheaderinsection_).md>) 方法中，创建并配置你的自定义视图。下面的示例代码取出（dequeue）已注册的自定义页眉，并配置其标题和图像属性。

```swift
override func tableView(_ tableView: UITableView, 
        viewForHeaderInSection section: Int) -> UIView? {
   let view = tableView.dequeueReusableHeaderFooterView(withIdentifier:
               "sectionHeader") as! MyCustomHeader
   view.title.text = sections[section]
   view.image.image = UIImage(named: sectionImages[section])

   return view
}
```

下图展示了最终生成的页眉。

![](../../../attachments/4c535042500d0efd03471a318c5dc05f/media-3148907@2x.png)

<sub>展示自定义页眉的示意图。自定义页眉包含一张图片和一段说明各分区内容的文字。</sub>

### 更改页眉和页脚的高度

表格视图会将分区页眉和页脚的高度与代表它们的视图分开跟踪。[UITableView](uitableview.md) 为这两者提供了默认尺寸。如果你所有的页眉（或所有的页脚）高度都相同，可以使用表格视图的 [sectionHeaderHeight](uitableview/sectionheaderheight.md) 和 [sectionFooterHeight](uitableview/sectionfooterheight.md) 属性来指定该高度，或者使用表格视图提供的默认值。

如果你的页眉或页脚高度并不完全相同，或者可以动态变化，请使用委托对象的 [- tableView:heightForHeaderInSection:](<uitableviewdelegate/tableview(__heightforheaderinsection_).md>) 和 [- tableView:heightForFooterInSection:](<uitableviewdelegate/tableview(__heightforfooterinsection_).md>) 方法来提供高度。当你实现这些方法时，必须为表格中的每个页眉和页脚都提供值。表格视图只会询问可见页眉和页脚的高度。当用户滚动时，表格视图会在每个页眉或页脚出现时要求你提供其高度，包括它移出屏幕后再次回到屏幕上时。

## 另请参阅

### 相关文档

- [Estimating the height of a table’s scrolling area](estimating-the-height-of-a-table-s-scrolling-area.md) — 为表格视图的页眉、页脚和行提供高度估算值，以确保滚动能准确反映内容的大小。

### Cells, headers, and footers

- [Configuring the cells for your table](configuring-the-cells-for-your-table.md) — 通过在故事板中定义一个或多个原型单元格，指定表格的行的外观和内容。
- [Creating self-sizing table view cells](creating-self-sizing-table-view-cells.md) — 创建支持动态字体、并使用系统间距约束调整文本标签周围间距的表格视图单元格。
- [UITableViewCell](uitableviewcell.md) — 表格视图中单行内容的视觉表示形式。
- [UITableViewHeaderFooterView](uitableviewheaderfooterview.md) — 一个可复用的视图，你可以将其放置在表格分区的顶部或底部，以显示该分区的附加信息。
</content>
