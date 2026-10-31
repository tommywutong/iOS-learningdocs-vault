---
title: 迁移到新的导览类型
framework: SwiftUI
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/migrating-to-new-navigation-types
source_url: 'https://developer.apple.com/documentation/swiftui/migrating-to-new-navigation-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/migrating-to-new-navigation-types.json'
content_hash: 'sha256:8c65e521cb2ad107'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [导览](navigation.md)

# 迁移到新的导览类型

<sub>文章</sub>

用导览叠放和导览分栏视图替换导览视图，改进你 App 的导览行为。

## 概述

如果你的 App 的最低部署目标为 iOS 16、iPadOS 16、macOS 13、tvOS 16、watchOS 9、visionOS 1 或更高版本，请停止使用 [NavigationView](navigationview.md)，改用 [NavigationStack](navigationstack.md) 和 [NavigationSplitView](navigationsplitview.md) 实例。如何使用它们取决于你的导览是在单栏中进行还是跨多栏进行。借助这些较新的容器，你可以更好地控制视图呈现、容器配置和编程式导览。

### 更新单栏导览

如果你的 App 使用的是应用了 [stack](navigationviewstyle/stack.md) 导览视图样式的 [NavigationView](navigationview.md)——即人们通过把新视图压入叠放进行导览——请切换到 [NavigationStack](navigationstack.md)。

具体而言，不要再这样写：

```swift
NavigationView { // This is deprecated.
    /* content */
}
.navigationViewStyle(.stack)
```

而应创建一个导览叠放：

```swift
NavigationStack {
    /* content */
}
```

### 更新多栏导览

如果你的 App 使用两栏或三栏的 [NavigationView](navigationview.md)，或者在某些情况下为多栏、其他情况下为单栏（这在同时运行于 iPhone 和 iPad 的 App 中很典型），请切换到 [NavigationSplitView](navigationsplitview.md)。

不再使用两栏导览视图：

```swift
NavigationView { // This is deprecated.
    /* column 1 */
    /* column 2 */
}
```

而是使用 [init(sidebar:detail:)](<navigationsplitview/init(sidebar_detail_).md>) 初始化方法创建一个带有显式边栏和详情内容的导览分栏视图：

```swift
NavigationSplitView {
    /* column 1 */
} detail: {
    /* column 2 */
}
```

同样，不再使用三栏导览视图：

```swift
NavigationView { // This is deprecated.
    /* column 1 */
    /* column 2 */
    /* column 3 */
}
```

而是使用 [init(sidebar:content:detail:)](<navigationsplitview/init(sidebar_content_detail_).md>) 初始化方法创建一个带有显式边栏、内容和详情组成部分的导览分栏视图：

```swift
NavigationSplitView {
    /* column 1 */
} content: {
    /* column 2 */
} detail: {
    /* column 3 */
}
```

如果你需要在某一栏内进行导览，请在该栏中嵌入一个导览叠放。这种安排可以对每栏显示的内容进行更精细的控制。[NavigationSplitView](navigationsplitview.md) 还允许你自定义栏的可见性和宽度。

### 更新编程式导览

如果你使用带有 `isActive` 输入参数的 [NavigationLink](navigationlink.md) 初始化方法之一来执行编程式导览，请把这一自动化转移到所包裹的叠放上。具体做法是把你的导览链接改为使用 [init(value:label:)](<navigationlink/init(value_label_).md>) 初始化方法，然后使用接受路径输入的导览叠放初始化方法之一，例如 [init(path:root:)](<navigationstack/init(path_root_).md>)。

例如，如果你的导览视图带有响应各个状态变量而激活的链接：

```swift
@State private var isShowingPurple = false
@State private var isShowingPink = false
@State private var isShowingOrange = false

var body: some View {
    NavigationView { // This is deprecated.
        List {
            NavigationLink("Purple", isActive: $isShowingPurple) {
                ColorDetail(color: .purple)
            }
            NavigationLink("Pink", isActive: $isShowingPink) {
                ColorDetail(color: .pink)
            }
            NavigationLink("Orange", isActive: $isShowingOrange) {
                ColorDetail(color: .orange)
            }
        }
    }
    .navigationViewStyle(.stack) 
}
```

当你的代码中某个其他部分把其中一个状态变量设为 true 时，带有匹配标签的导览链接会随之激活。

把它改写为一个接受路径输入的导览叠放：

```swift
@State private var path: [Color] = [] // Nothing on the stack by default.

var body: some View {
    NavigationStack(path: $path) {
        List {
            NavigationLink("Purple", value: .purple)
            NavigationLink("Pink", value: .pink)
            NavigationLink("Orange", value: .orange)
        }
        .navigationDestination(for: Color.self) { color in
            ColorDetail(color: color)
        }
    }
}
```

这个版本使用 [navigationDestination(for:destination:)](<view/navigationdestination(for_destination_).md>) 视图修饰符把呈现的数据与对应的视图解耦。这样，`path` 数组就能表示叠放上的每一个视图。你对数组所做的更改会直接影响容器当前显示的内容，以及人们在叠放中导览时遇到的内容。如果你使用 [NavigationPath](navigationpath.md) 而不是普通的数据集合来存储路径信息，你还可以支持更复杂的编程式导览。更多信息请参阅 [NavigationStack](navigationstack.md)。

### 更新基于选择的导览

如果你对使用带有 `selection` 输入参数的 [NavigationLink](navigationlink.md) 初始化方法之一的 [List](list.md) 元素执行编程式导览，你可以把选择逻辑移到列表上。例如，假设你的导览视图带有响应 `selection` 状态变量而激活的链接：

```swift
let colors: [Color] = [.purple, .pink, .orange]
@State private var selection: Color? = nil // Nothing selected by default.

var body: some View {
    NavigationView { // This is deprecated.
        List {
            ForEach(colors, id: \.self) { color in
                NavigationLink(color.description, tag: color, selection: $selection) {
                    ColorDetail(color: color)
                }
            }
        }
        Text("Pick a color")
    }
}
```

使用同样的属性，你可以把 body 改写为：

```swift
var body: some View {
    NavigationSplitView {
        List(colors, id: \.self, selection: $selection) { color in
            NavigationLink(color.description, value: color)
        }
    } detail: {
        if let color = selection {
            ColorDetail(color: color)
        } else {
            Text("Pick a color")
        }
    }
}
```

列表会与导览逻辑相互协调：当你在代码的其他部分更改选择状态变量时，带有对应颜色的导览链接会被激活。同样，如果有人选择了与某个特定颜色关联的导览链接，列表会更新选择值，供代码的其他部分读取。

### 通过可用性检查提供向后兼容

如果你的 App 需要运行在早于 iOS 16、iPadOS 16、macOS 13、tvOS 16、watchOS 9 或 visionOS 1 的平台版本上，你可以使用[可用性条件](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/statements/#Availability-Condition)在继续支持旧客户端的同时开始迁移。例如，你可以创建一个自定义包装视图，根据条件选用 [NavigationSplitView](navigationsplitview.md) 或 [NavigationView](navigationview.md)：

```swift
struct NavigationSplitViewWrapper<Sidebar, Content, Detail>: View
    where Sidebar: View, Content: View, Detail: View
{
    private var sidebar: Sidebar
    private var content: Content
    private var detail: Detail
    
    init(
        @ViewBuilder sidebar: () -> Sidebar,
        @ViewBuilder content: () -> Content,
        @ViewBuilder detail:  () -> Detail
    ) {
        self.sidebar = sidebar()
        self.content = content()
        self.detail = detail()
    }
    
    var body: some View {
        if #available(iOS 16, macOS 13, tvOS 16, watchOS 9, visionOS 1, *) {
            // Use the latest API.
            NavigationSplitView {
                sidebar
            } content: {
                content
            } detail: {
                detail
            }
        } else {
            // Support previous platform versions.
            NavigationView {
                sidebar
                content
                detail
            }
            .navigationViewStyle(.columns)
        }
    }
}
```

根据你 App 的需要自定义这个包装器。例如，你可以在可用性检查的相应分支中，向 [NavigationSplitView](navigationsplitview.md) 添加 [navigationSplitViewStyle(_:)](<view/navigationsplitviewstyle(__).md>) 之类的导览分栏视图样式修饰符。

## 另请参阅

### 在分栏中呈现视图

- [为你的 SwiftUI App 带来健壮的导览结构](bringing-robust-navigation-structure-to-your-swiftui-app.md) — 使用导览链接、叠放、目的地和路径，为所有平台提供流畅的体验，并支持深层链接和状态恢复等行为。
- [NavigationSplitView](navigationsplitview.md) — 一个以两栏或三栏呈现视图的视图，其中前导栏中的选择控制后续栏中的呈现。
- [navigationSplitViewStyle(_:)](<view/navigationsplitviewstyle(__).md>) — 设置此视图内导览分栏视图的样式。
- [navigationSplitViewColumnWidth(_:)](<view/navigationsplitviewcolumnwidth(__).md>) — 为包含此视图的栏设置固定的首选宽度。
- [navigationSplitViewColumnWidth(min:ideal:max:)](<view/navigationsplitviewcolumnwidth(min_ideal_max_).md>) — 为包含此视图的栏设置灵活的首选宽度。
- [NavigationSplitViewVisibility](navigationsplitviewvisibility.md) — 导览分栏视图中前导栏的可见性。
- [NavigationLink](navigationlink.md) — 一个控制导览呈现的视图。
