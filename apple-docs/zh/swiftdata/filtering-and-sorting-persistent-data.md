---
title: 过滤和排序持久化数据
framework: SwiftData
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, Xcode 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/filtering-and-sorting-persistent-data
source_url: 'https://developer.apple.com/documentation/swiftdata/filtering-and-sorting-persistent-data'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/filtering-and-sorting-persistent-data.json'
content_hash: 'sha256:3827c79bf90d65b1'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftData](../swiftdata.md)

# 过滤和排序持久化数据

<sub>示例代码</sub>

使用谓词（predicate）和动态查询管理数据存储的呈现。

## 概述

这个示例 App 显示了一个地震列表，展示了每次地震的时间、位置和大小。为了帮助使用者直观地了解列表，App 还在地图上标出了每次地震的位置。你可以选择列表中的地震，使其在地图上高亮。

该 App 使用 SwiftData 来存储和管理地震数据，并依赖动态查询以不同方式呈现数据。例如，使用者可以选择要显示哪一天的地震，按震级或时间以正序或倒序排列地震，并按位置名称进行过滤。

![](../../../attachments/0b52d2772645d45035621de11df2e387/Filtering-and-sorting-persistent-data-1@2x.png)

<sub>示例 App 在 iPhone 14 Pro 上运行的屏幕截图。App 的列表视图显示了一个地震列表。底部工具栏左侧的文字表明，在总共存储的 9,738 次地震中，列表显示了 145 次。底部工具栏右侧的日期选择器已激活，显示了一个用于选择日期的日历。日期选择器的日历中当前高亮显示的是 2023 年 8 月 21 日。顶部工具栏有一个排序按钮和一个垃圾桶按钮。</sub>

![](../../../attachments/2a6c4e748fb2209640b9da88793898b0/Filtering-and-sorting-persistent-data-2@2x.png)

<sub>示例 App 在 iPhone 14 Pro 上运行的屏幕截图。App 的列表视图显示了一个地震列表。底部工具栏左侧的文字表明，在总共存储的 9,738 次地震中，列表显示了 145 次。底部工具栏右侧的日期选择器未激活，显示日期为 2023 年 8 月 21 日。顶部工具栏右侧的排序按钮被选中，显示了一个弹出框，其中有「正序」、「倒序」、「时间」和「震级」选项。其中「倒序」和「时间」选项都带有勾选标记。顶部工具栏还有一个垃圾桶按钮。</sub>

![](../../../attachments/4fc3986c9459e39aa5ac0d470c4fcef7/Filtering-and-sorting-persistent-data-3@2x.png)

<sub>示例 App 在 iPhone 14 Pro 上运行的屏幕截图。App 的列表视图显示了 3 次地震。底部工具栏左侧的文字表明，在总共存储的 9,738 次地震中，列表显示了 3 次。底部工具栏右侧的日期选择器未激活，显示日期为 2023 年 8 月 21 日。显示区域顶部出现了一个搜索字段，其中包含文本「Nevada」。列表中所有可见项的位置名称中都包含文本「Nevada」。</sub>

> [!note] 注意
> 要了解 App 如何检索和存储地震数据，请参阅[维护服务器数据的本地副本](maintaining-a-local-copy-of-server-data.md)。

### 使用简单查询读取整个集合

App 的 `ContentView` 通过对 `quakes` 属性应用 [Query](query.md) 宏来获取完整的地震列表：

```swift
@Query private var quakes: [Quake]
```

该查询宏注入代码，使地震实例数组与数据存储中的项保持同步。视图使用这个地震列表根据所选地震配置导航栏。例如，它在 macOS 中设置标题和副标题：

```swift
.navigationTitle(quakes[selectedId]?.location.name ?? "Earthquakes")
.navigationSubtitle(quakes[selectedId]?.fullDate ?? "")
```

上述代码依赖于 App 在 [Array](../swift/array.md) 扩展中定义的下标方法：

```swift
extension Array where Element: Quake {
    subscript(id: Quake.ID?) -> Quake? {
        first { $0.id == id }
    }
}
```

该下标定义基于这样一个事实：模型对象——也就是带有 [Model()](<model().md>) 宏标注的类型，如 `Quake`——会自动遵循 [Identifiable](../swift/identifiable.md) 协议，这意味着每个地震实例都有一个唯一的 `id` 参数。当使用者在列表或地图视图中选择了一个地震时，App 会将 `selectedId` 设置为所选地震的标识符。

### 添加排序参数以排列数据

地图视图绘制圆圈来表示特定位置的地震，圆圈的大小与地震的震级相对应。为了避免多个圆圈重叠时看不清楚，`MapView` 按震级对其查询进行排序，以便地图将较大的圆圈绘制在较小的圆圈后面。

![示例 App 在 iPhone 14 Pro 上运行的屏幕截图。](../../../attachments/d4aefb890b159499d09e002f8d7d794b/Filtering-and-sorting-persistent-data-4@2x.png)

它通过在查询宏中添加参数来引入排序：

```swift
@Query(sort: \Quake.magnitude, order: .reverse)
private var quakes: [Quake]
```

此查询的输出驱动了地图内容构建器的 `QuakeMarker` 实例的生成，并且始终以所需的顺序出现：

```swift
Map(selection: $selectedIdMap) {
    ForEach(quakes) { quake in
        QuakeMarker(
            quake: quake,
            selected: quake.id == selectedId)
    }
}
```

> [!note] 注意
> App 将 `selectedIdMap` 绑定到地图的 selection 输入，并手动将其与代码中其他地方使用的主要 `selectedId` 值同步。保持独立的 selection 值使 App 能够检测到由地图驱动的更改，然后滚动列表以匹配。

### 使用谓词定义过滤器

为确保 App 的界面保持易用性，App 基于以下条件限制显示的地震数量：

- **日期** — 为避免地图上标记过多，App 一次只显示一天的地震。使用者可以选择查看哪一天。
- **位置名称** — 为了能让使用者聚焦于特定地震，使用者可以在搜索字段中输入文本，App 会将其与地震位置名称进行匹配。

为了实现这种过滤，App 定义了一个静态方法，该方法返回一个 [Predicate](../foundation/predicate.md)，该谓词同时考虑了搜索日期和搜索文本：

```swift
static func predicate(
    searchText: String,
    searchDate: Date
) -> Predicate<Quake> {
    let calendar = Calendar.autoupdatingCurrent
    let start = calendar.startOfDay(for: searchDate)
    let end = calendar.date(byAdding: .init(day: 1), to: start) ?? start

    return #Predicate<Quake> { quake in
        (searchText.isEmpty || quake.location.name.contains(searchText))
        &&
        (quake.time > start && quake.time < end)
    }
}
```

App 将此谓词应用于它动态创建的查询，如下一节所述。通过在中心位置定义一次谓词，多个视图中的查询都可以使用它。这使得当相关视图（如列表视图和地图视图）具有不同的查询时，可以轻松地同步它们。

### 动态更新查询

当使用者选择了新日期或更改了搜索文本时，App 需要更新查询以匹配。地图视图通过提供一个带有 `searchDate` 和 `searchText` 输入的初始化方法，并使用这些值重建存储的查询来实现这一点：

```swift
init(
    selectedId: Binding<Quake.ID?>,
    selectedIdMap: Binding<Quake.ID?>,
    searchDate: Date = .now,
    searchText: String = ""
) {
    _selectedId = selectedId
    _selectedIdMap = selectedIdMap

    _quakes = Query(
        filter: Quake.predicate(
            searchText: searchText,
            searchDate: searchDate),
        sort: \.magnitude,
        order: .reverse
    )
}
```

因为这些值是视图初始化方法的输入，所以当任何一个值发生变化时，SwiftUI 都会重新求值初始化方法来产生一个新的查询。这反过来又会更新视图的外观。

地震列表视图做了类似的事情，尽管在这种情况下它还接收排序配置输入：

```swift
init(
    selectedId: Binding<Quake.ID?>,
    selectedIdMap: Binding<Quake.ID?>,
    
    searchText: String = "",
    searchDate: Date = .now,
    sortParameter: SortParameter = .time,
    sortOrder: SortOrder = .reverse
) {
    _selectedId = selectedId
    _selectedIdMap = selectedIdMap

    let predicate = Quake.predicate(searchText: searchText, searchDate: searchDate)
    switch sortParameter {
    case .time: _quakes = Query(filter: predicate, sort: \.time, order: sortOrder)
    case .magnitude: _quakes = Query(filter: predicate, sort: \.magnitude, order: sortOrder)
    }
}
```

这两个初始化方法有不同的排序约束，以匹配它们各自呈现方式的需求，但它们使用相同的谓词来确保列表中显示的地震集始终与地图上显示的地震集匹配。

## 另请参阅

### 模型获取

- [Query()](<query().md>) — 获取所附加模型类型的所有实例。
- [其他查询宏](additionalquerymacros.md) — 补充宏，使你能够缩小查询结果范围，并告诉 SwiftData 如何对这些结果进行排序、排列和分区。
- [Query](query.md) — 一种使用指定条件获取模型的类型，并管理这些模型，使其与底层数据保持同步。
- [FetchDescriptor](fetchdescriptor.md) — 一种描述在执行获取时要使用的条件、排序顺序和任何其他配置的类型。

## 下载

- [SwiftDataLocalDataCacheSample.zip](https://docs-assets.developer.apple.com/published/5e964e0daa88/SwiftDataLocalDataCacheSample.zip)
