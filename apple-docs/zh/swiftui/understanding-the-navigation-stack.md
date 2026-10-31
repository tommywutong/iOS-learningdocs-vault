---
title: 了解导览叠放
framework: SwiftUI
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/understanding-the-navigation-stack
source_url: 'https://developer.apple.com/documentation/swiftui/understanding-the-navigation-stack'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/understanding-the-navigation-stack.json'
content_hash: 'sha256:a6090ea62a2417d7'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [导览](navigation.md)

# 了解导览叠放

<sub>文章</sub>

了解导览叠放、链接，以及如何在 App 结构中管理导览类型。

## 概述

[NavigationStack](navigationstack.md) 是 App 导览结构的容器。使用导览叠放可以在根视图之上呈现一组叠放的视图。

`NavigationStack` 通过其初始化方法的 path 参数把状态暴露给你的 App。要创建一个带有可控路径的导览叠放，或跟踪导览叠放上的视图，请使用 [NavigationPath](navigationpath.md)，或使用绑定到包含 [`Hashable`](../swift/hashable.md) 元素的 [`RandomAccessCollection`](../swift/randomaccesscollection.md) 和 [`RangeReplaceableCollection`](../swift/rangereplaceablecollection.md) 的 [Binding](binding.md)。

`NavigationPath` 是一个类型擦除的集合，你可以在其中存储异构的数据列表。对于同构数据，请改用 [`Array`](../swift/array.md)。由于 `NavigationPath` 是类型擦除的，它可以表示与导览叠放中某个视图相对应的不同类型的数据。

> [!tip] 提示
> 避免把模型类型用作导览路径的元素。确保导览路径的元素是轻量的，不要把它们当作数据模型的传输载体。

导览叠放的另一个元素是_导览目的地_，它封装了人们可以在你的 App 内导览前往的视图。

你可以使用以下方式在 `NavigationStack` 上呈现目的地：

- **视图-目的地** — 使用 [init(destination:label:)](<navigationlink/init(destination_label_).md>) 初始化方法把一个视图直接压入导览叠放。视图-目的地链接是"发射后不管"的：SwiftUI 会跟踪导览状态，但从你的 App 的角度来看，没有任何有状态的钩子表明你压入了一个视图。
- **值-目的地** — 值-目的地表示你正在把一个值压入路径。SwiftUI 使用你压入路径的值，通过 [navigationDestination(for:destination:)](<view/navigationdestination(for_destination_).md>) 修饰符来确定对应的视图。你使用 [init(value:label:)](<navigationlink/init(value_label_).md>) 初始化方法把一个值附加到导览路径上，并使用 [navigationDestination(for:destination:)](<view/navigationdestination(for_destination_).md>) 修饰符把所附加路径的数据类型映射到特定的目的地视图。你还可以使用 [navigationDestination(isPresented:destination:)](<view/navigationdestination(ispresented_destination_).md>) 修饰符以编程方式把视图压入导览叠放。这种目的地是有状态的——状态通过布尔绑定显式地暴露给你的 App。当呈现状态更适合用某个值的存在与否（而不是布尔值）来建模时，请使用 [navigationDestination(item:destination:)](<view/navigationdestination(item_destination_).md>)。这个修饰符接受一个绑定到可空数据模型的绑定。

> [!note] 注意
> 值-目的地和视图-目的地链接并不直接描述可见的叠放；它们指向的是添加到路径中的数据。

### 呈现视图-目的地链接

你可以使用 `NavigationLink(destination:label:)` 把一个视图压入 `NavigationStack`。使用这个初始化方法时，你要同时指定一个标签——显示在链接本身上——和一个目的地——在有人点按链接时显示。

把 [NavigationLink](navigationlink.md) 包裹在视图层级结构中更高层的导览结构中——例如某个祖先视图。如果不满足这个条件，链接通常会显示为停用状态。

下面是一个在 `NavigationStack` 内包含两个链接的示例：

```swift
struct DestinationView: View {
    var body: some View {
        NavigationStack {
            NavigationLink {
                ColorDetail(color: .mint, text: "Mint")
            } label: {
                Text("Mint")
            }
            
            NavigationLink {
                ColorDetail(color: .red, text: "Red")
            } label: {
                Text("Red")
            }
        }
    }
}

struct ColorDetail: View {
    var color: Color
    var text: String

    var body: some View {
        VStack {
            Text(text)
            color
         }
    }
}
```

在这个示例中，点按标题为 "Mint" 的标签会把 `ColorDetail(color: .mint, text: "Mint")` 视图压入导览叠放。导览叠放的内容为：位于深度 `0` 的根视图（`NavigationLink` 本身），以及位于深度 `1` 的 `ColorDetail(color: .mint, text: "Mint")`。

使用 [init(destination:label:)](<navigationlink/init(destination_label_).md>) 时，请注意：

- SwiftUI 会跟踪导览状态和导览路径的内容；但是，对于系统何时压入视图，没有任何暴露给你的 App 的有状态钩子。
- 它的状态无法以编程方式恢复。

请使用[管理导览状态和组合链接](understanding-the-navigation-stack.md#Manage-navigation-state-and-compose-links)中描述的有状态导览技术来跟踪导览链接何时被触发，而不是使用 [onAppear(perform:)](<view/onappear(perform_).md>) 或 `View/task(priority:_:)`。

使用 [navigationDestination(isPresented:destination:)](<view/navigationdestination(ispresented_destination_).md>) 修饰符并提供一个绑定到 `Boolean` 值的绑定，即可进行编程式导览。例如，你可以以编程方式把 `ColorDetail` 视图压入叠放：

```swift
struct DestinationView: View { 
    @State private var showDetails = false
    var favoriteColor: Color
    
    NavigationStack {
        VStack {
            Circle()
                .fill(favoriteColor)
            Button("Show details") {
                showDetails = true
            }
        }
        .navigationDestination(isPresented: $showDetails) {
            ColorDetail(color: favoriteColor, text: color.description)
        }
    }
}
```

当你希望基于状态切换而不是人们的交互进行导览时，或者当你的 App 呈现一个一次性目的地、其数据类型与导览叠放的同构路径不同时，请使用这种方法。

### 呈现值-目的地链接

当你向导览路径添加数据时，SwiftUI 会把该数据类型映射到一个视图，然后在有人点按链接时把它压入导览叠放。要描述叠放显示的视图，请在 `NavigationStack` 内使用 [navigationDestination(for:destination:)](<view/navigationdestination(for_destination_).md>) 视图修饰符。

下面的示例把 `DestinationView` 实现为一系列导览链接：

```swift
NavigationStack {
    List {
        NavigationLink("Mint", value: Color.mint)
        NavigationLink("Red", value: Color.red)
    }
    .navigationDestination(for: Color.self) { color in
        ColorDetail(color: color, text: color.description)
    }
}
```

在上面的示例中，SwiftUI 使用值类型——本例中为 `Color`——来确定合适的导览目的地。使用基于值的导览，你可以为单个叠放定义多种可能的目的地。当有人点按 "Mint" 时，SwiftUI 会把带有 `.mint` 值的 `ColorDetail` 视图压入叠放。

基于值的导览在目的地类型混合的场景中大放异彩。你可以扩展你的 App，在处理颜色之外还能处理与食谱相关的内容：

```swift
struct ValueView: View {
    private var recipes: [Recipe] = [.applePie, .chocolateCake]
    
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("Mint", value: Color.mint)
                NavigationLink("Red", value: Color.red)
                ForEach(recipes) { recipe in
                    NavigationLink(recipe.description, value: recipe)
                }
            }
            .navigationDestination(for: Color.self) { color in
                ColorDetail(color: color, text: color.description)
            }
            .navigationDestination(for: Recipe.self) { recipe in
                RecipeDetailView(recipe: recipe)
            }
        }
    }
}

struct RecipeDetailView: View {
    var recipe: Recipe
    
    var body: some View {
        Text(recipe.description)
    }
}

enum Recipe: Identifiable, Hashable, Codable {
    case applePie
    case chocolateCake
    
    var id: Self { self }
    
    var description: String {
        switch self {
        case .applePie:
            return "Apple Pie"
        case .chocolateCake:
            return "Chocolate Cake"
        }
    }
}
```

在这个示例中，`NavigationStack` 支持两种目的地类型：用于颜色的 `Color`，和用于食谱的 `Recipe`。SwiftUI 根据来自导览链接的值的数据类型确定正确的目的地视图。

当你需要基于某个条目的存在与否导览到一个视图时，请使用 [navigationDestination(item:destination:)](<view/navigationdestination(item_destination_).md>)。当该条目绑定为非 nil 时，SwiftUI 会把值传入目的地闭包，并把视图压入叠放。例如：

```swift
struct ContentView: View {
    private var recipes: [Recipe] = [.applePie, .chocolateCake]
    @State private var selectedRecipe: Recipe?
    
    var body: some View {
        NavigationStack {
            List(recipes, selection: $selectedRecipe) { recipe in
                NavigationLink(recipe.description, value: recipe)
            }
            .navigationDestination(item: $selectedRecipe) { recipe in
                RecipeDetailView(recipe: recipe)
            }
        }
    }
}
```

当有人点按一个食谱时，`selectedRecipe` 的值会更新，SwiftUI 会把 `RecipeDetailView(recipe: recipe)` 压入导览叠放。把 `selectedRecipe` 重新设为 nil 即可把该视图从叠放中弹出。

### 管理导览状态和组合链接

默认情况下，导览叠放自行管理状态以跟踪叠放上的视图。不过，你的 App 可以通过用一个绑定到你创建的数据值集合的绑定来初始化叠放，从而共享对状态的控制。

当你想观察此叠放的导览状态时，请使用 [init(path:root:)](<navigationstack/init(path_root_).md>)，它接受一个绑定到 `NavigationPath` 实参的绑定。

`NavigationPath` 数据类型是一个异构集合类型，接受任何 `Hashable` 值。你可以通过调用 [append(_:)](<navigationpath/append(__).md>) 向路径添加内容，或者当人们点按 [init(value:label:)](<navigationlink/init(value_label_).md>) 这类值-目的地链接时添加内容。

当你使用 [init(_:value:)](<navigationlink/init(__value_).md>) 把一个值压入叠放时，你实际上是把该值附加到路径上，如下所示：

```swift
struct ContentView: View {
    @State private var path = NavigationPath()

    var body: some View {
        NavigationStack(path: $path) {
            List {
                NavigationLink("Mint", value: Color.mint)
                NavigationLink("Red", value: Color.red)
            }
            .navigationDestination(for: Color.self) { color in
                ColorDetail(color: color)
            }
        }
    }
}
```

在这个示例中，当有人激活一个链接时，SwiftUI 会把相应的值（例如 `Color.mint`）添加到 `path` 中。SwiftUI 使用名为 `path` 的 [State](state.md) 属性来管理导览叠放的状态。

[init(path:root:)](<navigationstack/init(path_root_).md>) 还提供了另一个初始化方法，其 path 参数接受一个指向 `RandomAccessCollection` 和 `RangeReplaceableCollection` 实参的 [Binding](binding.md)。你可以把路径存储为一个对象的属性，该对象利用 [`Observable`](<../observation/observable().md>) 宏数据类型，并使用 `willSet` 和 `didSet` 等属性观察器或 [onChange(of:initial:_:)](<view/onchange(of_initial___).md>) 修饰符，在值-目的地链接被触发时响应更改。

在这种情况下，导览路径是一个同构集合类型，接受标准类型（例如 `Array`）或自定义数据类型，如下所示：

```swift
@Observable
class NavigationManager {
    var path: [Color] = [] {
        willSet {
            print("will set to \(newValue)")
        }
        
        didSet {
            print("didSet to \(path)")
        }
    }
}

struct ContentView: View {
    @State private var navigationManager = NavigationManager()

    var body: some View {
        NavigationStack(path: $navigationManager.path) {
            List {
                NavigationLink("Mint", value: Color.mint)
                NavigationLink("Red", value: Color.red)
            }
            .navigationDestination(for: Color.self) { color in
                ColorDetail(color: color, text: color.description)
            }
        }
    }
}
```

在上面的示例中，`willSet` 和 `didSet` 属性观察器跟踪导览链接何时被触发。

你还可以使用对 `path` 变量的引用来执行编程式导览。例如，你可以把一个视图从叠放中弹出：

```swift
@Observable
class NavigationManager {
    var path: [Color] = [] {
        willSet {
            print("will set to \(newValue)")
        }
        
        didSet {
            print("didSet to \(path)")
        }
    }
    
    @discardableResult
    func navigateBack() -> Color? {
        path.popLast()
    }
}
```

当你的叠放显示依赖单一数据类型的视图时，请使用标准类型；当你需要在单个叠放中呈现多种数据类型时，请使用 `NavigationPath`，如下例所示：

```swift
struct ValueView: View {
    @State private var path = NavigationPath()
    
    var body: some View {
        NavigationStack(path: $path) {
            List {
                NavigationLink("Mint", value: Color.mint)
                NavigationLink("Red", value: Color.red)
                NavigationLink("Apple Pie", value: Recipe.applePie)
                NavigationLink("Chocolate Cake", value: Recipe.chocolateCake)
            }
            .navigationDestination(for: Color.self) { color in
                ColorDetail(color: color)
            }
            .navigationDestination(for: Recipe.self) { recipe in
                RecipeDetailView(recipe: recipe)
            }
        }
    }
}
```

> [!note] 注意
> 值-目的地链接和视图-目的地链接最终都会把一个用户可见的视图压入叠放。不过，压入的值-目的地会反映在叠放的 `path` `Binding` 中（如果提供了的话），而压入的视图-目的地则不会。

组合使用时，这些导览 API 允许你根据最合适的情况选用两种链接风格。

在这里，当有人点按 "View Mint Color" 链接时，SwiftUI 先把基于值的目的地链接压入叠放，然后再压入一个视图-目的地链接：

```swift
struct ContentView: View {
    @State private var navigationManager = NavigationManager()

    var body: some View {
        NavigationStack(path: $navigationManager.path) {
            NavigationLink("View Mint Color", value: Color.mint)
                .navigationDestination(for: Color.self) { color in
                    NavigationLink("Push Recipe View") {
                        RecipeDetailView(recipe: .applePie)
                    }
                }
        }
    }
}
```

这段示例代码运行后，当有人依次点按每个 `NavigationLink` 时，导览叠放会构建出三个视图：

- **根视图** — `NavigationStack` 的起始视图。
- **值集合** — 压入路径的零个或多个值的序列，例如 `Color.mint`。这些值充当标识符或键，SwiftUI 用它们来确定要呈现哪些视图。
- **视图集合** — 添加到路径的视图序列，例如 `RecipeDetailView`。这个视图被包裹在导览目的地中，当有人点按链接时显示。

SwiftUI 会跟踪整个导览路径。底层数据结构如下例所示：

```swift
Root → [Color.mint] → [RecipeDetailView]
```

从概念上讲，SwiftUI 会把基于视图的目的地叠放在导览路径中基于值的目的地之上。例如，下面的代码把上例中的 `RecipeDetailView` 替换为一个 `NavigationLink`：

```swift
struct ContentView: View {
    @State private var navigationManager = NavigationManager()

    var body: some View {
        NavigationStack(path: $navigationManager.path) {
            NavigationLink("View Mint Color", value: Color.mint)
                .navigationDestination(for: Color.self) { color in
                    NavigationLink("Push Recipe View") {
                        NavigationLink("Push another view", value: Color.pink)
                    }
                }
        }
    }
}
```

运行修改后的示例，视图-目的地链接仍然位于叠放顶部。

如果你在叠放中使用异构或同构路径，你可以观察到导览路径随时间的变化，如下所示：

```swift
@Observable
class NavigationManager {
    var path: [Color] = [] {
        didSet {
            print("didSet to \(path)")
        }
    }
}

struct ContentView: View {
    @State private var navigationManager = NavigationManager()

    var body: some View {
        NavigationStack(path: $navigationManager.path) {
            NavigationLink("View Mint Color", value: Color.mint)
                .navigationDestination(for: Color.self) { color in
                    NavigationLink("Push Recipe View") {
                        RecipeDetailView(recipe: .applePie)
                    }
                }
        }
    }
}
```

当有人在 App 中导览时，它会打印以下日志：

```swift
New path: []
New Path: [Color.mint]
```

之所以打印这些日志，是因为视图-目的地导览链接不会导致任何你的 App 可以观察到的状态变化。如果你尝试在视图-目的地链接位于叠放上的情况下压入一个值，SwiftUI 会弹出所有视图目的地，并把该值的目的地压入叠放。

### 恢复导览路径的状态

导览路径的状态恢复让你能够在后续启动时把界面恢复到上一次交互的位置，为使用你 App 的人们提供连续性。

在 iOS 中，状态恢复在窗口或场景层面尤为重要，因为窗口的来去非常频繁。因此，思考导览路径的状态恢复时，应当采用与你在窗口或场景层面处理 App 状态恢复相同的方式。请参阅[使用 SwiftUI 恢复 App 的状态](restoring-your-app-s-state-with-swiftui.md)了解如何存储场景数据。

使用 `Codable`，你可以手动持久化和加载导览叠放路径，方法有两种，取决于路径数据类型是同构还是异构。按下面的示例存储同构路径：

```swift
@Observable
class NavigationManager {
    var path: [Recipe] = [] {
        didSet {
            save()
        }
    }
    
    /// 存储 JSON 文件的 URL，该文件用于保存导览路径。
    private static var dataURL: URL {
        .documentsDirectory.appending(path: "NavigationPath.json")
    }
    
    init() {
        do {
            // 从 Documents 目录中找到的 'NavigationPath' 数据文件加载数据模型。
            let path = try load(url: NavigationManager.dataURL)
            self.path = path
        } catch {
            // 处理错误。
        }
    }
    
    func save() {
        let encoder = JSONEncoder()
        do {
            let data = try encoder.encode(path)
            try data.write(to: NavigationManager.dataURL)
        } catch {
            // 处理错误。
        }
    }
    
    /// 从先前保存的状态加载导览路径。
    func load(url: URL) throws -> [Recipe] {
        let data = try Data(contentsOf: url, options: .mappedIfSafe)
        let decoder = JSONDecoder()
        return try decoder.decode([Recipe].self, from: data)
    }
}

struct ContentView: View {
    @State private var navigationManager = NavigationManager()

    var body: some View {
        NavigationStack(path: $navigationManager.path) {
            List {
                NavigationLink("Mint", value: Color.mint)
                NavigationLink("Red", value: Color.red)
                NavigationLink("Apple Pie", value: Recipe.applePie)
                NavigationLink("Chocolate Cake", value: Recipe.chocolateCake)
            }
            .navigationDestination(for: Color.self) { color in
                ColorDetail(color: color, text: color.description)
            }
            .navigationDestination(for: Recipe.self) { recipe in
                RecipeDetailView(recipe: recipe)
            }
        }
    }
}
```

在上面的示例中，当 `path` 发生变化时，`didSet` 属性观察器会被触发并调用 `save` 函数。该函数把新路径保存到磁盘，使 App 能够在初始化 `NavigationManager` 时恢复它。

使用 `NavigationPath` 存储异构路径，如下例所示：

```swift
@Observable
class NavigationManager {
    var path = NavigationPath() {
        didSet {
            save()
        }
    }
    
    /// 存储 JSON 文件的 URL，该文件用于保存导览路径。
    private static var dataURL: URL {
        .documentsDirectory.appending(path: "NavigationPath.json")
    }
    
    init() {
        do {
            // 从 Documents 目录中找到的 'NavigationPath' 数据文件加载数据模型。
            let path = try load(url: NavigationManager.dataURL)
            self.path = path
        } catch {
            // 处理错误
        }
    }
    
    func save() {
        guard let codableRepresentation = path.codable else { return }
        let encoder = JSONEncoder()
        do {
            let data = try encoder.encode(codableRepresentation)
            try data.write(to: NavigationManager.dataURL)
        } catch {
            //处理错误。
        }
    }
    
    /// 从先前保存的数据加载导览路径。
    func load(url: URL) throws -> NavigationPath {
        let data = try Data(contentsOf: url, options: .mappedIfSafe)
        let decoder = JSONDecoder()
        let path = try decoder.decode(NavigationPath.CodableRepresentation.self, from: data)
        return NavigationPath(path)
    }
}

```

在上面的示例中，`save` 方法会检查 `path.codable` 是否为 nil。这个值以可序列化的格式描述路径的内容。如果路径中任何被类型擦除的元素不符合 `codable`，它就会返回 `nil`。

执行这个检查很重要，因为 `NavigationPath` 不要求数据类型符合 `Codable`。`NavigationPath` 只要求类型符合 `Hashable`，因此你无法在编译期验证导览路径是不是一个有效的 `Codable` 表示。

要了解关于导览叠放、链接和路径的更多信息，请参阅[为你的 SwiftUI App 带来健壮的导览结构](bringing-robust-navigation-structure-to-your-swiftui-app.md)。
