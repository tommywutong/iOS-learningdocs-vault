---
title: 'Wishlist：在 SwiftUI App 中规划旅行'
framework: SwiftUI
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, Xcode 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/wishlist-planning-travel-in-a-swiftui-app
source_url: 'https://developer.apple.com/documentation/swiftui/wishlist-planning-travel-in-a-swiftui-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/wishlist-planning-travel-in-a-swiftui-app.json'
content_hash: 'sha256:0ed63801fadde511'
translated: true
---

> 导航： [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [View fundamentals](view-fundamentals.md)

# Wishlist：在 SwiftUI App 中规划旅行

<sub>示例代码</sub>

构建一款旅行规划 App，把行程整理成集合并跟踪活动的完成情况。

## 概述

Wishlist 示例 App 帮助人们把行程归组到按季节划分的集合中，从而整理旅行计划。在每个行程内，人们可以创建活动，并在探索过程中把它们标记为已完成。这个 App 用成就徽章来奖励进度，跟踪诸如完成首个行程或在所有冒险中达到某个活动里程碑这样的里程碑。

这个示例项目演示了如何：

- 组合自定视图。
- 使用 [Observable()](<../observation/observable().md>) 宏管理状态。
- 自定导览标题的外观。
- 为视图变化添加动画。
- 创建到导览目的地的缩放过渡，以及在按钮与表单之间的缩放过渡。

### 组合自定视图

SwiftUI 视图遵循 [View](view.md) 协议，并通过一个计算属性 `body` 来定义其内容。每个视图返回一份关于屏幕上会显示什么的描述，由 SwiftUI 负责渲染。

Wishlist 通过组合 [VStack](vstack.md)、[HStack](hstack.md)、[Text](text.md)、[Image](image.md) 和 [Button](button.md) 等内置组件来构建自定视图：

```swift
struct TripCard: View {
    var trip: Trip
    var size: Size

    var body: some View {
        VStack(alignment: .leading, spacing: 5) {
            TripImageView(url: trip.photoURL)
                .scaledToFill()
                .frame(width: size.width, height: size.height)
                .clipShape(.rect(cornerRadius: 16))

            VStack(alignment: .leading, spacing: 0) {
                Text(trip.name)
                    .font(.body)

                if let subtitle = trip.subtitle {
                    Text(subtitle)
                        .font(.subheadline)
                        .foregroundStyle(.secondary)
                }
            }
        }
    }
}
```

外层的 `VStack` 把图像和文本纵向叠放，并将内容沿前导边缘对齐。通过堆叠修饰符来依次应用变换，每个修饰符都会把前一个视图包装进一个具有修改后行为的新视图。

### 使用可观察宏管理状态

当视图的依赖发生变化时，SwiftUI 会自动更新视图。用 [Observable()](<../observation/observable().md>) 标记模型类，即可启用自动更改跟踪。在 Wishlist 中，`@Observable` 宏会合成必要的代码，来发布对任何存储属性所做的更改：

```swift
@Observable
class DataSource {
    var trips: [Trip.ID: Trip] {
        didSet {
            updateGoalAchievements()
        }
    }
    var searchText = ""
}
```

`DataSource` 类把行程存储在以行程 ID 为键的 [Dictionary](../swift/dictionary.md) 中，以便高效查找。`didSet` 属性观察器会在 `trips` 字典变化时调用 `updateGoalAchievements()`，使目标进度与行程完成情况保持同步。任何从 `trips` 字典读取数据的视图（例如 `RecentTripsPageView`）都会在字典变化时自动更新，例如添加或移除行程时。

为了在整个示例 App 中共享这些数据，Wishlist 在 [App](app.md) 结构体中使用 [State](state.md) 属性包装器创建一个状态，然后使用 [environment(_:)](<view/environment(__).md>) 修饰符把数据注入视图层级结构：

```swift
@main
struct WishlistApp: App {
    @State private var dataSource = DataSource()

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(dataSource)
        }
    }
}
```

在视图内部，Wishlist 使用类型来获取这个可观察对象：先创建一个属性，再把该对象的类型提供给 [Environment](environment.md) 属性包装器：

```swift
struct WishlistView: View {
    @Environment(DataSource.self) private var dataSource

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: 10) {
                    RecentTripsPageView()
                    ForEach(TripCollection.allCases) { tripCollection in
                        TripCollectionView(
                            tripCollection: tripCollection,
                            cardSize: tripCollection.cardSize,
                            namespace: namespace
                        )
                    }
                }
            }
        }
    }
}
```

`@Environment` 属性包装器从环境中取回数据源，并在视图与可观察模型之间建立依赖关系。默认情况下，当以对象类型作为键时，从环境中读取对象会返回一个非可选的对象。这一默认行为假定当前层级结构中的某个视图之前已使用 `environment(_:)` 修饰符存储了该类型的非可选实例。如果某个视图尝试用类型来获取一个对象，而该对象不在环境中，SwiftUI 会抛出异常。

SwiftUI 会自动跟踪视图 `body` 内的属性访问。当任何被观察的属性发生变化时，SwiftUI 会更新视图中依赖该值的所有部分。

SwiftUI 中的一些内置视图和修饰符（例如 [Toggle](toggle.md) 和 [searchable(text:placement:prompt:)](<view/searchable(text_placement_prompt_).md>)）会接受指向某个属性的 [Binding](binding.md)。这使这些视图和修饰符能够把更改写回该属性。使用 [Bindable](bindable.md) 属性包装器为 `Observable` 对象的属性创建绑定。这包括全局变量、存在于 SwiftUI 类型之外的属性，甚至局部变量。例如，这个示例 App 在视图的 `body` 内创建了一个 `@Bindable` 变量：

```swift
struct SearchView: View {
    @Environment(DataSource.self) private var dataSource

    var body: some View {
        @Bindable var dataSource = dataSource

        NavigationStack {
            SearchResultsListView()
                .searchable(text: $dataSource.searchText)
        }
    }
}
```

`@Bindable` 属性包装器暴露了一个绑定投影前缀 `$`，用于产生 `Binding` 值。在上面的示例中，`$dataSource.searchText` 创建了一个 `Binding<String>`，把搜索栏连接到数据源。当有人在搜索栏中输入时，SwiftUI 通过绑定写入新值，更新可观察属性并使依赖它的视图失效。

### 自定导览标题的外观

在显示导览标题时，SwiftUI 将视觉呈现与语义含义分开。

在这个示例 App 中，`WishlistView` 视图使用 [ToolbarItem](toolbaritem.md) 和 [title](toolbaritemplacement/title.md) 这个 `toolbarItem` 放置位置来自定标题的视觉外观。

```swift
NavigationStack {
    ScrollView {
        // 内容
    }
    .toolbar {
        ToolbarItem(placement: .title) {
            ExpandedNavigationTitle(title: "Wishlist")
        }
    }
    .navigationTitle("Wishlist")
    .toolbarTitleDisplayMode(.inline)
}
```

`ExpandedNavigationTitle` 视图使用自定字体渲染标题。请务必使用 [navigationTitle(_:)](<view/navigationtitle(__).md>) 添加导览标题，当有人从详情视图返回时，系统会把它用作辅助功能标签。[toolbarTitleDisplayMode(_:)](<view/toolbartitledisplaymode(__).md>) 修饰符指定 [inline](toolbartitledisplaymode/inline.md) 后，会告诉 SwiftUI 在导览栏的内联位置显示标题，而不是以大标题显示。

对于延伸到安全区的内容，请改用 [largeTitle](toolbaritemplacement/largetitle.md) 放置位置。

### 为视图变化添加动画

为了把人们的注意力引向状态变化，可以用以下方式之一添加动画：

- 通过在 [withAnimation(_:_:)](<withanimation(____).md>) 全局函数的调用中更改状态，为一次状态变化的所有视觉变化添加动画。
- 通过对视图应用 [animation(_:value:)](<view/animation(__value_).md>) 视图修饰符，在特定值变化时为特定视图添加动画。

SwiftUI 会为许多内置视图修饰符产生的效果添加动画，例如设置缩放或不透明度值的那些效果。你可以让自己的自定视图遵循 [Animatable](animatable.md) 协议，从而为其他值添加动画。使用 [Animatable()](<animatable().md>) 宏即可做到。

请根据你要为离散动作添加动画，还是响应特定属性的变化，来选择合适的方式。

在 Wishlist 中，当有人删除一项活动时，`withAnimation` 确保移除过程有平滑的动画：

```swift
Button("Delete", role: .destructive) {
    withAnimation {
        model.removeActivity(activity)
    }
}
```

`withAnimation` 块会建立一个动画事务。`removeActivity(_:)` 触发的任何视图变化都会自动获得动画，并共享同一条动画曲线和时序。

如需更精细的控制，可以使用 `animation(_:value:)` 修饰符为特定视图应用动画。这种基于值的方式会创建一个有针对性的动画，只在指定值变化时触发，并且只影响该修饰符所在的视图层级结构。在 Wishlist 的活动完成按钮中，对勾图标只在 `isComplete` 切换时才为它的外观变化添加动画，其他视图变化则不受动画影响：

```swift
Image(systemName: activity.isComplete ? "checkmark.circle.fill" : "circle")
    .foregroundStyle(activity.isComplete ? Color.accentColor : .gray)
    .contentTransition(.symbolEffect)
    .animation(.snappy, value: activity.isComplete)
```

`animation(.snappy, value: activity.isComplete)` 修饰符告诉 SwiftUI：当 `activity.isComplete` 变化时，使用 snappy 弹簧曲线为这个图像添加动画。如果其他属性发生变化（例如视图的位置或不透明度），除非它们也依赖于 `isComplete`，否则这些变化不会有动画。

要进一步了解动画，请观看 WWDC23 场次 [10156: Explore SwiftUI animation](https://developer.apple.com/videos/play/wwdc2023/10156/)。

### 在导览目的地之间创建缩放过渡

要自定视图之间的动画过渡，请对源视图应用 [matchedTransitionSource(id:in:)](<view/matchedtransitionsource(id_in_).md>)，并对目的视图应用 [navigationTransition(_:)](<view/navigationtransition(__).md>) 与过渡 [zoom(sourceID:in:)](<navigationtransition/zoom(sourceid_in_).md>)，二者使用相互匹配的标识符。使用 [Namespace](namespace.md) 属性包装器创建一个唯一值，将源和目的关联起来。

在 Wishlist 中，当有人轻点一张行程卡片时，它会平滑地缩放并展开成行程详情界面，在整个导览过程中保持视觉上的连续性。关闭详情视图会反向播放动画，缩回原来的卡片位置。

```swift
struct WishlistView: View {
    @Namespace private var namespace

    var body: some View {
        NavigationStack {
            ...
            ForEach(TripCollection.allCases) { tripCollection in
                TripCollectionView(
                    tripCollection: tripCollection,
                    namespace: namespace
                )
            }
        }
    }
}

struct TripCollectionView: View {
    var tripCollection: TripCollection
    var namespace: Namespace.ID

    var body: some View {
        ...
        ForEach(dataSource.trips(in: tripCollection)) { trip in
            NavigationLink {
                TripDetailView(trip: trip)
                    .navigationTransition(.zoom(sourceID: trip.id, in: namespace))
            } label: {
                TripCard(trip: trip, size: cardSize)
                    .matchedTransitionSource(id: trip.id, in: namespace)
            }
        }
        ...
    }
}
```

`@Namespace` 属性包装器创建一个唯一的标识符空间，SwiftUI 用它来协调过渡。把同一个命名空间传给源视图和目的视图，即可建立二者的关联。

行程集合中的每张 `TripCard` 都会收到 `matchedTransitionSource(id:in:)`，以行程的 ID 作为标识符。当有人轻点某张卡片时，SwiftUI 会捕获它的位置、大小和圆角半径，作为过渡的起点。行程详情视图应用带有匹配标识符的 `navigationTransition(.zoom(sourceID:in:))`，声明自己是缩放目标。SwiftUI 在两个几何形状之间插值，把其中一个无缝地变形为另一个。

请观看 WWDC24 场次 [10145: Enhance your UI animations and transitions](https://developer.apple.com/videos/play/wwdc2024/10145/)，了解如何在你的 App 的导览和呈现中采用缩放过渡。

## 另请参阅

### 创建视图

- [声明自定视图](declaring-a-custom-view.md) — 定义视图并把它们组装成视图层级结构。
- [View](view.md) — 一种表示你的 App 用户界面一部分的类型，并提供用于配置视图的修饰符。
- [ContentBuilder](contentbuilder.md) — 一种自定参数特性，用于从闭包构建视图和其他内容类型。
- [ViewBuilder](viewbuilder.md) — 一种自定参数特性，用于从闭包构建视图。

## 下载

- [WishlistPlanningTravelInASwiftUIApp.zip](https://docs-assets.developer.apple.com/published/1a5604d20e5e/WishlistPlanningTravelInASwiftUIApp.zip)
