---
title: 使用可差分数据源更新集合视图
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, Xcode 13.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/updating-collection-views-using-diffable-data-sources
source_url: 'https://developer.apple.com/documentation/uikit/updating-collection-views-using-diffable-data-sources'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/updating-collection-views-using-diffable-data-sources.json'
content_hash: 'sha256:61c8ebecfac7317c'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [视图与控制](views-and-controls.md) · [集合视图](collection-views.md)

# 使用可差分数据源更新集合视图

<sub>示例代码</sub>

使用包含标识符的可差分数据源，简化集合视图中数据的显示与更新。

## 概述

_集合视图（collection view）_以区段和条目的形式呈现数据，在集合视图中显示数据的 App 会将这些区段和条目插入视图。App 还可能需要处理区段和条目的删除或移动。例如，此项目中的示例 App 在集合视图中显示食谱；使用该 App 的用户可以添加和删除食谱，还可以将食谱标记为个人收藏。为了支持这些操作，示例 App 会处理集合视图内数据的插入、删除、移动和更新。

在 App 中填充集合视图时，你可以创建采用 [UICollectionViewDataSource](uicollectionviewdatasource.md) 协议的自定数据源。若要让集合视图中的信息保持最新，你需要确定哪些数据发生了变化，并根据这些变化执行批量更新；这一过程要求仔细协调插入、删除和移动操作。

为避免该过程的复杂性，示例 App 使用 [UICollectionViewDiffableDataSource](uicollectionviewdiffabledatasource-9tqpa.md) 对象。_可差分数据源（diffable data source）_存储区段和条目的_标识符（identifier）_列表，用来表示集合视图中每个区段和条目的身份。这些标识符是稳定的，也就是说它们不会变化。相比之下，符合 [UICollectionViewDataSource](uicollectionviewdatasource.md) 的自定数据源使用_索引（index）_和_索引路径（index path）_，而它们并不稳定。索引和索引路径表示区段和条目的位置；随着数据源向集合视图添加、移除和重新排列内容，这些位置可能发生变化。不过，借助标识符，可差分数据源无需知道区段或条目在集合视图中的位置，就能引用它们。

> [!note] 注意
> 此示例使用集合视图显示数据，但其中介绍的概念也适用于表格视图（table view）。有关将可差分数据源与表格视图结合使用的更多信息，请参阅 [UITableViewDiffableDataSource](uitableviewdiffabledatasource-2euir.md)。

若要将值用作标识符，其数据类型必须符合 [`Hashable`](../swift/hashable.md) 协议。哈希处理使 [`Set`](../swift/set.md)、[`Dictionary`](../swift/dictionary.md) 和快照（snapshot，即 [NSDiffableDataSourceSnapshot](nsdiffabledatasourcesnapshot-swift.struct.md) 与 [NSDiffableDataSourceSectionSnapshot](nsdiffabledatasourcesectionsnapshot-swift.struct.md) 的实例）等数据集合可以将值用作键，从而实现快速高效的查找。可哈希类型也符合 [`Equatable`](../swift/equatable.md) 协议，因此你的标识符必须正确实现相等性。有关更多信息，请参阅 [`Equatable`](../swift/equatable.md)`.`

因为标识符可哈希且可比较是否相等，可差分数据源能够确定其当前快照与另一个快照之间的差异。然后，它可以根据这些差异代你在集合视图中插入、删除和移动区段与条目，无需再编写执行批量更新的自定代码。

> [!important] 重要
> 两个相等的标识符必须始终具有相同的哈希值。但反过来并不成立；具有相同哈希值的两个值不一定相等。这种情况称为_哈希冲突（hash collision）_。为了提高效率，请尽量确保不相等的标识符具有不同的哈希值。无法避免时偶尔出现哈希冲突没有问题，但要尽量减少冲突数量。否则，数据集合中的查找性能可能会受到影响。

### 定义可差分数据源

在此示例项目中，`RecipeListViewController` 会在集合视图中显示食谱列表。在控制器显示食谱之前，会先定义一个实例变量来存储可差分数据源。

```swift
private var recipeListDataSource: UICollectionViewDiffableDataSource<RecipeListSection, Recipe.ID>!
```

`RecipeListViewController` 声明 `recipeListDataSource` 时，将 `RecipeListSection` 用作区段标识符类型，将 `Recipe.ID` 用作条目标识符类型。这些标识符类型告诉数据源其中包含的值类型。

对于区段标识符类型，`recipeListDataSource` 使用 `RecipeListSection`，这是一个原始值类型为 [`Int`](../swift/int.md) 的枚举（在 Swift 中，`Int` 可哈希）。每个枚举 case 标识集合视图的一个区段。此示例只有一个区段 `main`，用于显示食谱列表。

```swift
private enum RecipeListSection: Int {
    case main
}
```

对于条目标识符类型，`recipeListDataSource` 使用 `Recipe.ID`。此类型来自 `Recipe` 结构体，其定义如下：

```swift
struct Recipe: Identifiable, Codable {
    var id: Int
    var title: String
    var prepTime: Int   // 以秒为单位。
    var cookTime: Int   // 以秒为单位。
    var servings: String
    var ingredients: String
    var directions: String
    var isFavorite: Bool
    var collections: [String]
    fileprivate var addedOn: Date? = Date()
    fileprivate var imageNames: [String]
}
```

此结构体符合 [`Identifiable`](../swift/identifiable.md) 协议，该协议要求结构体包含 [`id`](../swift/identifiable/id-8t2ws.md) 属性。由于符合 `Identifiable`，`Recipe` 结构体会自动公开关联类型（associated type）[`ID`](../swift/identifiable/id-swift.associatedtype.md)，该类型根据结构体中 `id` 属性的声明确定。又因为此类型必须可哈希，所以示例 App 可以将 `Recipe.ID` 用作条目标识符类型。

> [!note] 注意
> `Recipe` 结构体不符合 `Hashable` 协议。该结构体不必可哈希，因为可差分数据源和快照中存储的条目是食谱_标识符_（后备数据存储为每个食谱提供的 `Recipe.ID` 值），而不是完整的食谱结构体。

将 `Recipe.ID` 用作 `recipeListDataSource` 的条目标识符类型，意味着数据源以及应用到它的所有快照只包含 `Recipe.ID` 值，而不包含完整的食谱数据。因为标识符类型是一种简单的可哈希类型，所以这种方式可以让可差分数据源在集合视图中显示食谱时达到最佳性能。

### 配置可差分数据源

在使用可差分数据源中的数据填充集合视图之前，示例 App 会配置该数据源。App 创建一个 [UICollectionViewDiffableDataSource](uicollectionviewdiffabledatasource-9tqpa.md) 实例，并设置其_单元格提供程序（cell provider）_，这是一个为集合视图配置并返回单元格的闭包（closure）。

`RecipeListViewController` 在名为 `configureDataSource()` 的辅助方法中配置 `recipeListDataSource`。视图控制器（view controller）在其 [- viewDidLoad](<uiviewcontroller/viewdidload().md>) 方法中调用此方法。

`configureDataSource()` 方法创建单元格注册，并提供一个使用食谱数据配置各个单元格的处理程序闭包。该闭包接收一个 `Recipe` 实例，并使用它配置单元格。

> [!note] 注意
> 单元格注册的条目类型不必与可差分数据源使用的条目标识符类型相匹配。

接下来，`configureDataSource()` 创建 [UICollectionViewDiffableDataSource](uicollectionviewdiffabledatasource-9tqpa.md) 实例，并定义单元格提供程序闭包。该闭包接收食谱标识符，然后使用标识符从后备数据存储中检索食谱，并将食谱结构体传给单元格注册的处理程序闭包。

```swift
private func configureDataSource() {
    // 创建可差分数据源要使用的单元格注册。
    let recipeCellRegistration = UICollectionView.CellRegistration<UICollectionViewListCell, Recipe> { cell, indexPath, recipe in
        var contentConfiguration = UIListContentConfiguration.subtitleCell()
        contentConfiguration.text = recipe.title
        contentConfiguration.secondaryText = recipe.subtitle
        contentConfiguration.image = recipe.smallImage
        contentConfiguration.imageProperties.cornerRadius = 4
        contentConfiguration.imageProperties.maximumSize = CGSize(width: 60, height: 60)
        
        cell.contentConfiguration = contentConfiguration
        
        if recipe.isFavorite {
            let image = UIImage(systemName: "heart.fill")
            let accessoryConfiguration = UICellAccessory.CustomViewConfiguration(customView: UIImageView(image: image),
                                                                                 placement: .trailing(displayed: .always),
                                                                                 tintColor: .secondaryLabel)
            cell.accessories = [.customView(configuration: accessoryConfiguration)]
        } else {
            cell.accessories = []
        }
    }

    // 创建可差分数据源及其单元格提供程序。
    recipeListDataSource = UICollectionViewDiffableDataSource(collectionView: collectionView) {
        collectionView, indexPath, identifier -> UICollectionViewCell in
        // `identifier` 是 `Recipe.ID` 的实例。使用它从
        // 后备数据存储中检索食谱。
        let recipe = dataStore.recipe(with: identifier)!
        return collectionView.dequeueConfiguredReusableCell(using: recipeCellRegistration, for: indexPath, item: recipe)
    }
}
```

### 使用标识符载入可差分数据源

配置好可差分数据源后，`RecipeListViewController` 会调用其辅助方法 `loadRecipeData()`，将数据首次载入数据源，继而使用食谱填充集合视图。此方法检索食谱标识符列表，并创建一个 [NSDiffableDataSourceSnapshot](nsdiffabledatasourcesnapshot-swift.struct.md) 实例。然后，它向快照添加 `main` 区段和食谱标识符。最后，该方法调用 [applySnapshotUsingReloadData(_:)](<uicollectionviewdiffabledatasource-9tqpa/applysnapshotusingreloaddata(__).md>) 将快照应用到数据源，在不计算差异或以动画呈现变化的情况下，重置集合视图以反映快照中的数据状态。

```swift
private func loadRecipeData() {
    // 检索根据所选边栏条目（例如 All Recipes 或 Favorites）
    // 确定的食谱标识符列表。
    guard let recipeIds = recipeSplitViewController.selectedRecipes?.recipeIds()
    else { return }
    
    // 通过将食谱标识符添加到新快照来更新集合视图，
    // 并将快照应用到可差分数据源。
    var snapshot = NSDiffableDataSourceSnapshot<RecipeListSection, Recipe.ID>()
    snapshot.appendSections([.main])
    snapshot.appendItems(recipeIds, toSection: .main)
    recipeListDataSource.applySnapshotUsingReloadData(snapshot)
}
```

> [!important] 重要
> 每个条目标识符在快照内都必须唯一。因此，一个条目标识符不能出现在快照内的多个位置。区段标识符也是如此；它们必须唯一，不能同时存在于快照内的多个位置。

### 插入、删除和移动条目

使用示例 App 的用户可以对食谱数据进行两类更改：

- 更改数据集合本身，例如添加或移除食谱，或者对其重新排序。
- 更改现有条目的属性，例如更改食谱名称或将食谱标记为个人收藏。

若要处理数据集合的变化，App 会创建一个表示数据集合当前状态的新快照，并将其应用到可差分数据源。数据源将当前快照与新快照进行比较，以确定发生了哪些变化。然后，它根据这些变化在集合视图中执行所需的插入、删除和移动操作。

可差分数据源虽然可以确定当前快照与新快照之间的变化，却不会监视数据集合是否发生变化。检测数据变化并通过应用新快照将其告知可差分数据源，是 App 的责任。

> [!note] 注意
> App 可以使用 [`NotificationCenter`](../foundation/notificationcenter.md) 和 [Combine](../combine.md) 等不同机制，向 App 的其他部分报告数据变化。此示例使用 `NotificationCenter`。

为了通知 App 的其他部分食谱列表发生了变化（例如用户添加或移除食谱之后），示例使用通知中心（notification center）发送 `selectedRecipesDidChange` 通知。为了接收该通知，`RecipeListViewController` 添加一个通知观察者（observer），并将 `selectedRecipesDidChange(_:)` 用作其选择器（selector）。

```swift
NotificationCenter.default.addObserver(
    self,
    selector: #selector(selectedRecipesDidChange(_:)),
    name: .selectedRecipesDidChange,
    object: nil
)
```

`selectedRecipesDidChange(_:)` 与 `loadRecipeData()` 类似，但它使用 [apply(_:animatingDifferences:)](<uicollectionviewdiffabledatasource-9tqpa/apply(__animatingdifferences_).md>) 来应用通知提供的所选食谱标识符列表，而不是使用 [applySnapshotUsingReloadData(_:)](<uicollectionviewdiffabledatasource-9tqpa/applysnapshotusingreloaddata(__).md>)。[apply(_:animatingDifferences:)](<uicollectionviewdiffabledatasource-9tqpa/apply(__animatingdifferences_).md>) 方法会对集合视图执行增量更新，而不是完全重置所显示的数据。又因为 `animatingDifferences` 为 `true`，集合视图会以动画呈现出现的变化。

```swift
@objc
private func selectedRecipesDidChange(_ notification: Notification) {
    // 根据通知的 `userInfo` 字典创建所选食谱标识符的快照，
    // 并将其应用到可差分数据源。
    guard
        let userInfo = notification.userInfo,
        let selectedRecipeIds = userInfo[NotificationKeys.selectedRecipeIds] as? [Recipe.ID]
    else { return }
    
    var snapshot = NSDiffableDataSourceSnapshot<RecipeListSection, Recipe.ID>()
    snapshot.appendSections([.main])
    snapshot.appendItems(selectedRecipeIds, toSection: .main)
    recipeListDataSource.apply(snapshot, animatingDifferences: true)

    // 此示例 App 的设计使得次要（详细信息）视图控制器中
    // 显示的所选食谱可能存在于新快照中，但在应用快照前
    // 并不存在于集合视图中。例如，在显示
    // 个人收藏食谱列表时，用户可以点按
    // `isFavorite` 按钮，将所选食谱取消标记为个人收藏。
    // 这会从个人收藏列表中移除所选食谱。
    // 再次点按该按钮，食谱会重新出现在
    // 列表中。在这种情况下，App 需要重新选择
    // 该食谱，使它在集合视图中显示为选中状态。
    selectRecipeIfNeeded()
}
```

### 更新现有条目

若要处理现有条目属性的变化，App 会从可差分数据源检索当前快照，并在快照上调用 [reconfigureItems(_:)](<nsdiffabledatasourcesnapshot-swift.struct/reconfigureitems(__).md>) 或 [reloadItems(_:)](<nsdiffabledatasourcesnapshot-swift.struct/reloaditems(__).md>)。然后，它将快照应用到可差分数据源，后者会更新指定条目的显示。

同样，检测数据变化的是 App，而不是可差分数据源。

为了将食谱的变化告知 App 的其他部分（例如当用户将食谱标记为个人收藏时），示例会发送 `recipeDidChange` 通知。`RecipeListViewController` 使用观察者接收通知，并将 `recipeDidChange(_:)` 用作选择器。

```swift
NotificationCenter.default.addObserver(
    self,
    selector: #selector(recipeDidChange(_:)),
    name: .recipeDidChange,
    object: nil
)
```

`recipeDidChange` 通知表示单个食谱的数据发生了变化。因为只有一个食谱发生变化，不需要更新集合视图中显示的整个食谱列表。示例只会更新显示已更改食谱的单元格。例如，当用户将食谱标记为个人收藏时，该食谱旁边会出现心形图标；当用户取消其个人收藏标记时，心形图标会消失。

为了使用最新食谱数据更新单元格，`recipeDidChange(_:)` 方法会确认可差分数据源包含通知提供的食谱标识符。然后，该方法从数据源检索当前快照，调用 [reconfigureItems(_:)](<nsdiffabledatasourcesnapshot-swift.struct/reconfigureitems(__).md>)，并传入食谱标识符。这次调用会指示数据源更新由食谱标识符所标识的单元格中显示的数据。最后，`recipeDidChange(_:)` 将更新后的快照应用到数据源。

```swift
@objc
private func recipeDidChange(_ notification: Notification) {
    guard
        // 从 `userInfo` 字典获取 `recipeId`。
        let userInfo = notification.userInfo,
        let recipeId = userInfo[NotificationKeys.recipeId] as? Recipe.ID,
        // 确认数据源包含该食谱。
        recipeListDataSource.indexPath(for: recipeId) != nil
    else { return }
    
    // 获取可差分数据源的当前快照。
    var snapshot = recipeListDataSource.snapshot()
    // 更新集合视图中显示的食谱数据。
    snapshot.reconfigureItems([recipeId])
    recipeListDataSource.apply(snapshot, animatingDifferences: true)
}
```

可差分数据源将更新后的快照与当前快照进行比较，并应用差异——在此例中，是重新配置显示已更改食谱的条目的请求。为完成请求，数据源会调用其单元格提供程序闭包；该闭包会检索更新后的食谱，并使用最新食谱数据配置单元格。又因为应用快照时 `animatingDifferences` 为 `true`，集合视图会通过显示或隐藏心形图标，以动画形式呈现单元格的视觉变化。

### 使用轻量数据结构填充快照

存储标识符的另一种方式，是使用轻量数据结构填充可差分数据源和快照。数据结构方式很方便，并且在某些情况下可能很合适——例如快速制作原型，或显示由属性不会发生变化的静态条目组成的集合——但它存在明显的限制和取舍。例如，[`Hashable`](../swift/hashable.md) 和 [`Equatable`](../swift/equatable.md) 的实现必须纳入结构体中所有可能变化的属性。结构体内数据的任何变化都会使其不再等于先前版本，而可差分数据源在应用新快照时正是以此来确定发生了哪些变化。

此示例使用这种方式在边栏中显示条目。在 `SidebarViewController` 中，自定结构体 `SidebarItem` 定义边栏条目的属性，即 `title` 和 `type`。

```swift
private struct SidebarItem: Hashable {
    let title: String
    let type: SidebarItemType
    
    enum SidebarItemType {
        case standard, collection, expandableHeader
    }
}
```

这些属性的组合决定每个边栏条目的哈希值。由于属性值不会变化，使用此 `SidebarItem` 结构体而非标识符填充快照，是可以接受的使用场景。

```swift
private func createSnapshotOfStandardItems() -> NSDiffableDataSourceSectionSnapshot<SidebarItem> {
    let items = [
        SidebarItem(title: StandardSidebarItem.all.rawValue, type: .standard),
        SidebarItem(title: StandardSidebarItem.favorites.rawValue, type: .standard),
        SidebarItem(title: StandardSidebarItem.recents.rawValue, type: .standard)
    ]
    return createSidebarItemSnapshot(.standardItems, items: items)
}
```

这种方式的缺点是，可差分数据源不再能够跟踪身份。每当现有条目发生变化时，可差分数据源会将该变化视为删除旧条目并插入新条目。结果，集合视图会丢失与该条目相关的重要状态。例如，当条目的任何属性发生变化时，选中的条目会变为未选中，因为从可差分数据源的角度来看，App 删除了该条目，又添加了一个新条目取代它。

此外，如果应用快照时 `animatingDifferences` 为 `true`，每次变化都需要执行旧单元格退出动画和新单元格进入动画；这可能会损害性能，并导致单元格中的用户界面状态（包括动画）丢失。

另外，使用数据结构填充快照时，这种策略会导致你无法使用 [reconfigureItems(_:)](<nsdiffabledatasourcesnapshot-swift.struct/reconfigureitems(__).md>) 或 [reloadItems(_:)](<nsdiffabledatasourcesnapshot-swift.struct/reloaditems(__).md>) 方法，因为这些方法要求使用正确的标识符。更新现有条目数据的唯一机制，是应用一个包含新数据结构的新快照，这会导致可差分数据源对每个已更改条目执行一次删除和一次插入操作。

对于许多真实使用场景，将数据结构直接存储到可差分数据源和快照中并不是稳健的解决方案，因为数据源会丧失跟踪身份的能力。只应在条目不会发生变化的简单使用场景（例如此示例中的边栏条目）中，或条目的身份并不重要时使用此方式。对于其他所有使用场景，或者不确定应采用哪种方式时，请使用正确的标识符填充可差分数据源和快照。

## 另请参阅

### 数据

- [实现现代集合视图](implementing-modern-collection-views.md) — 为你的 App 引入组合式布局（compositional layout），并使用可差分数据源简化用户界面的更新。
- [构建高性能列表和集合视图](building-high-performance-lists-and-collection-views.md) — 通过预取和图像准备提高 App 中列表与集合的性能。
- [UICollectionViewDiffableDataSource](uicollectionviewdiffabledatasource-9tqpa.md) — 用于管理数据并为集合视图提供单元格的对象。
- [UICollectionViewDataSource](uicollectionviewdatasource.md) — 用于管理数据并为集合视图提供单元格的对象所采用的方法。
- [UICollectionViewDataSourcePrefetching](uicollectionviewdatasourceprefetching.md) — 一种协议，可预先告知集合视图的数据需求，以便触发异步（asynchronous）数据加载操作。
- [NSDiffableDataSourceSnapshot](nsdiffabledatasourcesnapshot-swift.struct.md) — 视图中数据在特定时间点所处状态的表示。
- [NSDiffableDataSourceSectionSnapshot](nsdiffabledatasourcesectionsnapshot-swift.struct.md) — 布局区段中数据在特定时间点所处状态的表示。
- [UIRefreshControl](uirefreshcontrol.md) — 可发起滚动视图（scroll view）内容刷新的标准控制。

## 下载

- [UpdatingCollectionViewsUsingDiffableDataSources.zip](https://docs-assets.developer.apple.com/published/70021f020614/UpdatingCollectionViewsUsingDiffableDataSources.zip)
