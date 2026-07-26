---
title: 实现现代集合视图
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 11.0+, Xcode 16.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/implementing-modern-collection-views
source_url: 'https://developer.apple.com/documentation/uikit/implementing-modern-collection-views'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/implementing-modern-collection-views.json'
content_hash: 'sha256:931356f84d109ceb'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Views and controls](views-and-controls.md) · [Collection views](collection-views.md)

# 实现现代集合视图

<sub>示例代码</sub>

为你的 App 引入组合式布局，并使用可差分数据源简化用户界面的更新。

## 概述

集合视图让你能以灵活的视觉排布方式呈现一组数据。这个示例 App 展示了如何创建各种类型的布局，并管理集合视图中的数据。该示例聚焦于两项关键技术：

- 组合式布局，一种可组合、灵活且快速的集合视图布局类型，让你能为你的内容构建任意种类的视觉排布。
- 可差分数据源，一种专门的数据源类型，提供了简单高效地管理集合视图数据和用户界面更新所需的行为。

### 配置示例代码项目

要在 Xcode 中运行这个示例代码项目，首先选择要在 iOS 还是 macOS 中查看示例。

要在 iOS 中查看示例：

1. 选择 Modern Collection Views 目标。
2. 在 Scheme 菜单中，选择一个 iOS 模拟器来运行该 App。

要在 macOS 中查看示例：

1. 选择 Modern Collection Views Mac 目标。
2. 在 Scheme 菜单中，选择「我的 Mac」。
3. 在该目标的构建设置中，在「签名与功能 \> 签名证书」下，选择「本地运行签名」。
4. 运行该 App，并从「Example」菜单导览到各个示例。

这里展示的代码示例来自 iOS 目标，但你可以在 macOS 目标的 `.swift` 文件中找到与 macOS 对应的示例。

### 创建网格布局

Grid 示例展示了如何通过使用分数尺寸来创建一行五个大小相等的条目，从而创建网格布局。它通过使用 `.fractionalWidth(0.2)` 创建一个水平组，组内每个条目的宽度都是组宽度的 20%。每行五个条目在同一区段内重复多次，从而形成一个网格。

```swift
let itemSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(0.2),
                                     heightDimension: .fractionalHeight(1.0))
let item = NSCollectionLayoutItem(layoutSize: itemSize)

let groupSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0),
                                      heightDimension: .fractionalWidth(0.2))
let group = NSCollectionLayoutGroup.horizontal(layoutSize: groupSize,
                                                 subitems: [item])

let section = NSCollectionLayoutSection(group: group)

let layout = UICollectionViewCompositionalLayout(section: section)
return layout
```

### 在条目周围添加间距

Inset Items Grid 示例在 Grid 示例的布局基础上进行扩展，展示了如何使用 [contentInsets](nscollectionlayoutitem/contentinsets.md) 属性在条目周围添加间距。在这里，这个属性会在每个条目的边缘周围施加均匀的间距。

```swift
let itemSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(0.2),
                                     heightDimension: .fractionalHeight(1.0))
let item = NSCollectionLayoutItem(layoutSize: itemSize)
item.contentInsets = NSDirectionalEdgeInsets(top: 5, leading: 5, bottom: 5, trailing: 5)
```

### 创建列布局

Two-Column Grid 示例展示了如何通过创建一个包含 [+ horizontalGroupWithLayoutSize:subitem:count:](<nscollectionlayoutgroup/horizontal(layoutsize_subitem_count_).md>) 的 `count` 参数中指定的确切条目数量的组，来创建两列布局。这种方法简化了对一个组包含多少条目的精确指定。在这种情况下，`count` 参数优先于 `itemSize`，条目大小会被自动计算，以适配指定数量的条目。

```swift
let itemSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0),
                                     heightDimension: .fractionalHeight(1.0))
let item = NSCollectionLayoutItem(layoutSize: itemSize)

let groupSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0),
                                      heightDimension: .absolute(44))
let group = NSCollectionLayoutGroup.horizontal(layoutSize: groupSize, repeatingSubitem: item, count: 2)
let spacing = CGFloat(10)
group.interItemSpacing = .fixed(spacing)
```

### 为每个区段显示不同的布局

Distinct Sections 示例展示了如何在同一个集合视图布局的不同区段中显示不同的布局排布。要创建具有不同区段的布局，需要使用带有区段提供程序的组合式布局。区段提供程序中的代码访问区段的索引（`sectionIndex`）来确定它正在配置哪个区段，并为每个区段显示不同的布局。

```swift
let layout = UICollectionViewCompositionalLayout { (sectionIndex: Int,
    layoutEnvironment: NSCollectionLayoutEnvironment) -> NSCollectionLayoutSection? in

    guard let sectionLayoutKind = SectionLayoutKind(rawValue: sectionIndex) else { return nil }
    let columns = sectionLayoutKind.columnCount

    // The group auto-calculates the actual item width to make
    // the requested number of columns fit, so this widthDimension is ignored.
    let itemSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0),
                                         heightDimension: .fractionalHeight(1.0))
    let item = NSCollectionLayoutItem(layoutSize: itemSize)
    item.contentInsets = NSDirectionalEdgeInsets(top: 2, leading: 2, bottom: 2, trailing: 2)

    let groupHeight = columns == 1 ?
        NSCollectionLayoutDimension.absolute(44) :
        NSCollectionLayoutDimension.fractionalWidth(0.2)
    let groupSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0),
                                          heightDimension: groupHeight)
    let group = NSCollectionLayoutGroup.horizontal(layoutSize: groupSize, repeatingSubitem: item, count: columns)

    let section = NSCollectionLayoutSection(group: group)
    section.contentInsets = NSDirectionalEdgeInsets(top: 20, leading: 20, bottom: 20, trailing: 20)
    return section
}
return layout
```

### 在不同环境中显示不同的布局

Adaptive Sections 示例展示了如何创建一个能适配其所显示环境的布局。在这个示例中，显示的列数会根据可用屏幕大小而变化。要创建能适配新环境的布局，需要使用带有区段提供程序的组合式布局。区段提供程序中的代码访问当前布局环境中可用空间的大小（`layoutEnvironment.container.effectiveContentSize`），并根据可用宽度显示不同的列数。

```swift
let layout = UICollectionViewCompositionalLayout {
    (sectionIndex: Int, layoutEnvironment: NSCollectionLayoutEnvironment) -> NSCollectionLayoutSection? in
    guard let layoutKind = SectionLayoutKind(rawValue: sectionIndex) else { return nil }

    let columns = layoutKind.columnCount(for: layoutEnvironment.container.effectiveContentSize.width)

    let itemSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(0.2),
                                         heightDimension: .fractionalHeight(1.0))
    let item = NSCollectionLayoutItem(layoutSize: itemSize)
    item.contentInsets = NSDirectionalEdgeInsets(top: 2, leading: 2, bottom: 2, trailing: 2)

    let groupHeight = layoutKind == .list ?
        NSCollectionLayoutDimension.absolute(44) : NSCollectionLayoutDimension.fractionalWidth(0.2)
    let groupSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0),
                                           heightDimension: groupHeight)
    let group = NSCollectionLayoutGroup.horizontal(layoutSize: groupSize, repeatingSubitem: item, count: columns)
    let section = NSCollectionLayoutSection(group: group)
    section.contentInsets = NSDirectionalEdgeInsets(top: 20, leading: 20, bottom: 20, trailing: 20)
    return section
}
return layout
```

### 为条目添加徽章

Item Badges 示例展示了如何为集合视图中的条目添加徽章等附加视图。它通过为徽章创建一个附加条目，并在创建条目本身时传入该附加条目，从而在每个条目的右上角创建并添加一个徽章。数据源在其 [supplementaryViewProvider](uicollectionviewdiffabledatasource-9tqpa/supplementaryviewprovider-swift.property.md) 中配置每个徽章。

```swift
let badgeAnchor = NSCollectionLayoutAnchor(edges: [.top, .trailing], fractionalOffset: CGPoint(x: 0.3, y: -0.3))
let badgeSize = NSCollectionLayoutSize(widthDimension: .absolute(20),
                                      heightDimension: .absolute(20))
let badge = NSCollectionLayoutSupplementaryItem(
    layoutSize: badgeSize,
    elementKind: ItemBadgeSupplementaryViewController.badgeElementKind,
    containerAnchor: badgeAnchor)

let itemSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(0.25),
                                     heightDimension: .fractionalHeight(1.0))
let item = NSCollectionLayoutItem(layoutSize: itemSize, supplementaryItems: [badge])
item.contentInsets = NSDirectionalEdgeInsets(top: 5, leading: 5, bottom: 5, trailing: 5)
```

### 为区段添加页眉和页脚

Section Headers/Footers 示例展示了如何为集合视图的每个区段添加页眉和页脚。它创建了代表页眉和页脚的边界附加条目，并将它们设置为该区段的 [boundarySupplementaryItems](nscollectionlayoutsection/boundarysupplementaryitems.md)。

```swift
let headerFooterSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0),
                                             heightDimension: .estimated(44))
let sectionHeader = NSCollectionLayoutBoundarySupplementaryItem(
    layoutSize: headerFooterSize,
    elementKind: SectionHeadersFootersViewController.sectionHeaderElementKind, alignment: .top)
let sectionFooter = NSCollectionLayoutBoundarySupplementaryItem(
    layoutSize: headerFooterSize,
    elementKind: SectionHeadersFootersViewController.sectionFooterElementKind, alignment: .bottom)
section.boundarySupplementaryItems = [sectionHeader, sectionFooter]
```

该示例使用附加注册来为页眉和页脚配置其内容和外观。

```swift
let headerRegistration = UICollectionView.SupplementaryRegistration
<TitleSupplementaryView>(elementKind: SectionHeadersFootersViewController.sectionHeaderElementKind) {
    (supplementaryView, string, indexPath) in
    supplementaryView.label.text = "\(string) for section \(indexPath.section)"
    supplementaryView.backgroundColor = .lightGray
    supplementaryView.layer.borderColor = UIColor.black.cgColor
    supplementaryView.layer.borderWidth = 1.0
}
```

集合视图使用这些附加注册，在可差分数据源的 [supplementaryViewProvider](uicollectionviewdiffabledatasource-9tqpa/supplementaryviewprovider-swift.property.md) 中出列已配置好的页眉和页脚。

```swift
dataSource.supplementaryViewProvider = { (view, kind, index) in
    return self.collectionView.dequeueConfiguredReusableSupplementary(
        using: kind == SectionHeadersFootersViewController.sectionHeaderElementKind ? headerRegistration : footerRegistration, for: index)
}
```

### 将区段页眉固定到区段上

Pinned Section Headers 示例展示了如何将区段页眉固定到其所属的区段上。这样一来，只要该页眉所关联区段的任何部分在滚动时可见，页眉就会显示，而页脚则保持原位。这个示例把页眉的 [pinToVisibleBounds](nscollectionlayoutboundarysupplementaryitem/pintovisiblebounds.md) 属性设置为 `true`，并将其 [zIndex](nscollectionlayoutsupplementaryitem/zindex.md) 增加到大于 `1` 的值，使页眉在滚动时显示在区段的上方。

```swift
let sectionHeader = NSCollectionLayoutBoundarySupplementaryItem(
    layoutSize: NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0),
                                      heightDimension: .estimated(44)),
    elementKind: PinnedSectionHeaderFooterViewController.sectionHeaderElementKind,
    alignment: .top)
let sectionFooter = NSCollectionLayoutBoundarySupplementaryItem(
    layoutSize: NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0),
                                      heightDimension: .estimated(44)),
    elementKind: PinnedSectionHeaderFooterViewController.sectionFooterElementKind,
    alignment: .bottom)
sectionHeader.pinToVisibleBounds = true
sectionHeader.zIndex = 2
section.boundarySupplementaryItems = [sectionHeader, sectionFooter]
```

该示例使用附加注册来为页眉和页脚配置其内容和外观。集合视图使用这些附加注册，在可差分数据源的 [supplementaryViewProvider](uicollectionviewdiffabledatasource-9tqpa/supplementaryviewprovider-swift.property.md) 中出列已配置好的页眉和页脚。

```swift
dataSource.supplementaryViewProvider = { (view, kind, index) in
    return self.collectionView.dequeueConfiguredReusableSupplementary(
        using: kind == PinnedSectionHeaderFooterViewController.sectionHeaderElementKind ? headerRegistration : footerRegistration, for: index)
}
```

### 用背景装饰区段

Section Background Decoration 示例展示了如何通过添加区段背景来区分各个区段。它使用 [+ backgroundDecorationItemWithElementKind:](<nscollectionlayoutdecorationitem/background(elementkind_).md>) 创建一个装饰条目来生成区段背景，然后将该装饰条目设置为该区段的 [decorationItems](nscollectionlayoutsection/decorationitems.md) 属性。

```swift
let sectionBackgroundDecoration = NSCollectionLayoutDecorationItem.background(
    elementKind: SectionDecorationViewController.sectionBackgroundDecorationElementKind)
sectionBackgroundDecoration.contentInsets = NSDirectionalEdgeInsets(top: 5, leading: 5, bottom: 5, trailing: 5)
section.decorationItems = [sectionBackgroundDecoration]
```

以下代码随后使用 [- registerClass:forDecorationViewOfKind:](<uicollectionviewlayout/register(__fordecorationviewofkind_)-361k6.md>) 向布局注册背景视图。

```swift
let layout = UICollectionViewCompositionalLayout(section: section)
layout.register(
    SectionBackgroundDecorationView.self,
    forDecorationViewOfKind: SectionDecorationViewController.sectionBackgroundDecorationElementKind)
return layout
```

### 通过嵌套组创建自定布局

Nested Groups 示例展示了如何通过在其他组内嵌套组来创建灵活的布局排布。它创建了一个包含两个条目的垂直组，并将该垂直组与一个条目组合到一个水平父组中。

```swift
let leadingItem = NSCollectionLayoutItem(
    layoutSize: NSCollectionLayoutSize(widthDimension: .fractionalWidth(0.7),
                                      heightDimension: .fractionalHeight(1.0)))
leadingItem.contentInsets = NSDirectionalEdgeInsets(top: 10, leading: 10, bottom: 10, trailing: 10)

let trailingItem = NSCollectionLayoutItem(
    layoutSize: NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0),
                                      heightDimension: .fractionalHeight(0.3)))
trailingItem.contentInsets = NSDirectionalEdgeInsets(top: 10, leading: 10, bottom: 10, trailing: 10)
let trailingGroup = NSCollectionLayoutGroup.vertical(
    layoutSize: NSCollectionLayoutSize(widthDimension: .fractionalWidth(0.3),
                                       heightDimension: .fractionalHeight(1.0)),
    repeatingSubitem: trailingItem,
    count: 2)
let nestedGroup = NSCollectionLayoutGroup.horizontal(
    layoutSize: NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0),
                                      heightDimension: .fractionalHeight(0.4)),
    subitems: [leadingItem, trailingGroup])
```

### 水平滚动区段

Orthogonal Sections 示例展示了如何在整体垂直滚动的布局中创建一个水平滚动的区段。将区段的 [orthogonalScrollingBehavior](nscollectionlayoutsection/orthogonalscrollingbehavior.md) 属性设置为 [UICollectionLayoutSectionOrthogonalScrollingBehaviorNone](uicollectionlayoutsectionorthogonalscrollingbehavior/none.md) 以外的值，会使该区段的内容沿垂直于主布局轴的方向排布。在这种情况下，因为该布局默认垂直滚动，所以该区段会水平滚动。

```swift
section.orthogonalScrollingBehavior = .continuous
```

### 选择水平滚动和分页行为

Orthogonal Section Behaviors 示例展示了 [UICollectionLayoutSectionOrthogonalScrollingBehavior](uicollectionlayoutsectionorthogonalscrollingbehavior.md) 的每一个选项。该布局的每个区段都演示了一种不同的正交滚动行为，展示了滚动选项和分页选项之间的差异。在这种情况下，因为该布局默认垂直滚动，所以这些区段本身会水平滚动。

```swift
case continuous, continuousGroupLeadingBoundary, paging, groupPaging, groupPagingCentered, none
func orthogonalScrollingBehavior() -> UICollectionLayoutSectionOrthogonalScrollingBehavior {
    switch self {
    case .none:
        return UICollectionLayoutSectionOrthogonalScrollingBehavior.none
    case .continuous:
        return UICollectionLayoutSectionOrthogonalScrollingBehavior.continuous
    case .continuousGroupLeadingBoundary:
        return UICollectionLayoutSectionOrthogonalScrollingBehavior.continuousGroupLeadingBoundary
    case .paging:
        return UICollectionLayoutSectionOrthogonalScrollingBehavior.paging
    case .groupPaging:
        return UICollectionLayoutSectionOrthogonalScrollingBehavior.groupPaging
    case .groupPagingCentered:
        return UICollectionLayoutSectionOrthogonalScrollingBehavior.groupPagingCentered
    }
}
```

### 更新集合视图中的数据

Mountains Search 示例展示了当用户筛选数据时，如何更新集合视图中的数据和用户界面。它显示一份山脉名称列表，并允许用户在搜索栏中输入文本，根据山脉名称进行筛选。

这个集合视图 `mountainsCollectionView` 包含一个区段，其中的条目由每座山的原始数据列表创建而来。这个示例将每条数据封装到一个 `Mountain` 结构体中，该结构体定义在 `MountainsController` 中。为了管理数据，这个示例使用了一个包含单个区段和 `Mountain` 类型条目的可差分数据源。当该可差分数据源被创建时，它会连接到 `mountainsCollectionView`，并注册一个 `LabelCell` 单元格类型，用于在集合视图中显示山脉的名称。然后，它用山脉的名称配置该单元格。

`performQuery(with:)` 方法负责更新数据和用户界面。该方法接收当前输入的筛选文本，并生成一份名称中包含该文本的山脉列表。然后，它使用快照构造新筛选出的数据的表示。该快照包含与之前相同的单个区段，但现在它不再包含代表每座山的条目，而只包含筛选后的山脉。

该方法随后调用 [apply(_:animatingDifferences:completion:)](<uicollectionviewdiffabledatasource-9tqpa/apply(__animatingdifferences_completion_).md>)，将快照中的数据应用到可差分数据源上。可差分数据源会将快照中的数据存储为新的数据状态，计算旧状态与新状态之间的差异，并触发用户界面显示新的状态。

```swift
func performQuery(with filter: String?) {
    let mountains = mountainsController.filteredMountains(with: filter).sorted { $0.name < $1.name }

    var snapshot = NSDiffableDataSourceSnapshot<Section, MountainsController.Mountain>()
    snapshot.appendSections([.main])
    snapshot.appendItems(mountains)
    dataSource.apply(snapshot, animatingDifferences: true)
}
```

### 更新多个区段中的数据

Settings: Wi-Fi 示例展示了如何在使用多种区段和条目类型的表格视图中更新数据和用户界面。它重现了 iOS「设置」中的 Wi-Fi 页面，让用户能打开或关闭 Wi-Fi 开关，以查看可用和当前的 Wi-Fi 网络。

`updateUI(animated:)` 方法根据 Wi-Fi 是否已启用来决定显示哪些区段和条目。如果 Wi-Fi 已禁用，该方法只会把 `.config` 区段及其条目添加到快照中。如果 Wi-Fi 已启用，该方法还会添加 `.networks` 区段及其条目。

```swift
let configItems = configurationItems.filter { !($0.type == .currentNetwork && !controller.wifiEnabled) }

currentSnapshot = NSDiffableDataSourceSnapshot<Section, Item>()

currentSnapshot.appendSections([.config])
currentSnapshot.appendItems(configItems, toSection: .config)

if controller.wifiEnabled {
    let sortedNetworks = controller.availableNetworks.sorted { $0.name < $1.name }
    let networkItems = sortedNetworks.map { Item(network: $0) }
    currentSnapshot.appendSections([.networks])
    currentSnapshot.appendItems(networkItems, toSection: .networks)
}

self.dataSource.apply(currentSnapshot, animatingDifferences: animated)
```

### 增量更新数据

Insertion Sort Visualization 示例展示了如何增量更新数据，展示数据从初始状态变化到最终状态过程中可见的进度。它显示了若干行原本随机排列的色板，随后逐步将其按光谱顺序排序。

这个示例与其他可差分数据源示例的关键区别在于：这个示例不通过创建空快照来更新数据的状态。相反，`performSortStep()` 方法通过使用 `dataSource.snapshot()` 检索集合视图数据的当前状态。然后，它只修改该快照的一部分，以逐步执行可视化排序步骤。

```swift
// Get the current state of the UI from the data source.
var updatedSnapshot = dataSource.snapshot()

// For each section, if needed, step through and perform the next sorting step.
updatedSnapshot.sectionIdentifiers.forEach {
    let section = $0
    if !section.isSorted {

        // Step the sort algorithm.
        section.sortNext()
        let items = section.values

        // Replace the items for this section with the newly sorted items.
        updatedSnapshot.deleteItems(items)
        updatedSnapshot.appendItems(items, toSection: section)

        sectionCountNeedingSort += 1
    }
}
```

### 创建一个简单的列表布局

Simple List 示例展示了如何创建一个能适配任意屏幕大小的基本列表布局。它使用某个系统定义的列表外观创建一个配置。然后，它通过将该配置传给 [list(using:)](<uicollectionviewcompositionallayout/list(using_).md>) 来创建列表布局。这种方法生成一个只有单个区段、样式为列表的组合式布局。

```swift
let config = UICollectionLayoutListConfiguration(appearance: .insetGrouped)
return UICollectionViewCompositionalLayout.list(using: config)
```

### 选择列表外观

List Appearances 示例展示了 [Appearance](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum.md) 的每一个选项。点按导览栏中的外观名称，会将列表切换为另一种外观，从而展示每种列表样式。每个列表都使用 [UICollectionLayoutListConfiguration.HeaderMode.firstItemInSection](uicollectionlayoutlistconfiguration-swift.struct/headermode-swift.enum/firstiteminsection.md) 页眉模式，使列表的每个区段都可以展开和折叠。

```swift
var config = UICollectionLayoutListConfiguration(appearance: self.appearance)
config.headerMode = .firstItemInSection
```

### 自定列表单元格

List with Custom Cells 示例展示了如何配置一个自定的列表单元格子类。这个示例聚焦于 `CustomListCell`，它是 [UICollectionViewListCell](uicollectionviewlistcell.md) 的一个自定子类，将若干种子视图组合到一个单元格中。它使用内容配置来设置这些视图的外观和内容。

`updateConfiguration(using:)` 方法负责设置单元格的初始外观和内容。每当单元格的配置状态发生变化时，系统都会调用这个方法，以针对新状态更新单元格的外观。为了配置列表内容视图，它会为当前状态获取默认的列表内容配置。

```swift
var content = defaultListContentConfiguration().updated(for: state)
```

然后，它自定该配置的值，并将该配置赋给 `listContentView` 的 [configuration](uilistcontentview/configuration.md) 属性。

对于图像视图和标签，`updateConfiguration(using:)` 方法会为当前状态获取默认的值单元格配置，并将其存储在 `valueConfiguration` 中。它会将这个配置中预先配置好的默认样式和度量值复制到自定视图中，以确保与系统样式保持一致。

```swift
categoryIconView.tintColor = valueConfiguration.imageProperties.resolvedTintColor(for: tintColor)
categoryIconView.preferredSymbolConfiguration = .init(font: valueConfiguration.secondaryTextProperties.font, scale: .small)
```

为了向集合视图注册这个自定单元格子类，这个示例使用了单元格注册。该单元格注册用对应条目的数据配置每个单元格。它还为该单元格添加了一个显示指示符单元格附属项。

```swift
let cellRegistration = UICollectionView.CellRegistration<CustomListCell, Item> { (cell, indexPath, item) in
    cell.updateWithItem(item)
    cell.accessories = [.disclosureIndicator()]
}
```

可差分数据源在出列单元格时使用这个单元格注册。

```swift
return collectionView.dequeueConfiguredReusableCell(using: cellRegistration, for: indexPath, item: item)
```

### 构建包含多种区段类型的布局

Emoji Explorer 示例展示了如何创建包含多种区段类型的组合式布局。这个示例在一个组合式布局中包含一个正交滚动区段、一个大纲区段和一个列表区段。`createLayout()` 方法定义了一个区段提供程序，为每个区段提供内容。

对于顶部区段，它通过设置 [orthogonalScrollingBehavior](nscollectionlayoutsection/orthogonalscrollingbehavior.md) 属性来启用水平滚动。

```swift
section.orthogonalScrollingBehavior = .continuousGroupLeadingBoundary
```

大纲区段使用 [UICollectionLayoutListConfiguration.Appearance.sidebar](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebar.md) 列表外观。它使用一个区段快照来填充，从而创建一个层级化的数据结构。

```swift
let rootItem = Item(title: String(describing: category), hasChildren: true)
outlineSnapshot.append([rootItem])
let outlineItems = category.emojis.map { Item(emoji: $0) }
outlineSnapshot.append(outlineItems, to: rootItem)
```

列表区段使用 [UICollectionLayoutListConfiguration.Appearance.insetGrouped](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/insetgrouped.md) 列表外观。这个区段的配置为每个单元格添加了一个滑动操作，让该单元格可以被标记为「收藏」。

```swift
configuration.leadingSwipeActionsConfigurationProvider = { [weak self] (indexPath) in
    guard let self = self else { return nil }
    guard let item = self.dataSource.itemIdentifier(for: indexPath) else { return nil }
    return self.leadingSwipeActionConfigurationForListCellItem(item)
}
```

每个区段都有对应的单元格注册，用于配置各自的单元格类型。集合视图使用这些注册来出列已配置好的单元格，以在每个区段中显示。

```swift
switch section {
case .recents:
    return collectionView.dequeueConfiguredReusableCell(using: gridCellRegistration, for: indexPath, item: item.emoji)
case .list:
    return collectionView.dequeueConfiguredReusableCell(using: listCellRegistration, for: indexPath, item: item)
case .outline:
    if item.hasChildren {
        return collectionView.dequeueConfiguredReusableCell(using: outlineHeaderCellRegistration, for: indexPath, item: item.title!)
    } else {
        return collectionView.dequeueConfiguredReusableCell(using: outlineCellRegistration, for: indexPath, item: item.emoji)
    }
}
```

### 创建值单元格列表

Emoji Explorer - List 示例展示了如何创建使用值单元格样式的单元格列表。它为列表中的每个单元格应用了带有默认值单元格样式的内容配置。

```swift
var contentConfiguration = UIListContentConfiguration.valueCell()
contentConfiguration.text = emoji.text
contentConfiguration.secondaryText = String(describing: emoji.category)
cell.contentConfiguration = contentConfiguration
```

## 另请参阅

### 数据

- [使用可差分数据源更新集合视图](updating-collection-views-using-diffable-data-sources.md) — 使用包含标识符的可差分数据源，简化集合视图中数据的显示和更新。
- [构建高性能列表和集合视图](building-high-performance-lists-and-collection-views.md) — 通过预取和图像准备，提升你 App 中列表和集合的性能。
- [UICollectionViewDiffableDataSource](uicollectionviewdiffabledatasource-9tqpa.md) — 用于管理数据并为集合视图提供单元格的对象。
- [UICollectionViewDataSource](uicollectionviewdatasource.md) — 由用于管理数据并为集合视图提供单元格的对象所采用的方法。
- [UICollectionViewDataSourcePrefetching](uicollectionviewdatasourceprefetching.md) — 一种协议，为集合视图提前提供数据需求的预警，从而可以触发异步数据加载操作。
- [NSDiffableDataSourceSnapshot](nsdiffabledatasourcesnapshot-swift.struct.md) — 特定时间点视图中数据状态的表示。
- [NSDiffableDataSourceSectionSnapshot](nsdiffabledatasourcesectionsnapshot-swift.struct.md) — 特定时间点布局区段中数据状态的表示。
- [UIRefreshControl](uirefreshcontrol.md) — 一种可以启动滚动视图内容刷新的标准控制。

## 下载

- [ImplementingModernCollectionViews.zip](https://docs-assets.developer.apple.com/published/76a6e639ef2e/ImplementingModernCollectionViews.zip)
</content>
