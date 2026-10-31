---
title: 在你的 App 中监视数据变化
framework: SwiftUI
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 16.2+, iPadOS 16.2+, Mac Catalyst 16.2+, macOS 13.1+, Xcode 14.3+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/monitoring-model-data-changes-in-your-app
source_url: 'https://developer.apple.com/documentation/swiftui/monitoring-model-data-changes-in-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/monitoring-model-data-changes-in-your-app.json'
content_hash: 'sha256:ba19e7a86d3c5fdc'
translated: true
---

> 导航： [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [Model data](model-data.md)

# 在你的 App 中监视数据变化

<sub>示例代码</sub>

使用可观察对象，在 App 的用户界面中显示数据的变化。

## 概述

你通常会把数据存储和处理放在一个与 App 的用户界面（UI）及其他逻辑相互分离的数据模型中。这种分离提升了模块化程度、改善了可测试性，也让你更容易理清 App 的工作方式。

传统上，你会用视图控制器在模型和 UI 之间来回搬运数据，但 SwiftUI 会替你完成其中大部分同步工作。为了让视图在数据变化时更新，你把数据模型类做成可观察对象、发布其属性，并使用属性包装器来声明它们的实例。为了确保用户驱动的数据变化能流回模型，你把 UI 控制绑定到模型属性。这些特性协同工作，帮助你为数据维护单一的事实来源。

> [!important] 重要
> 本文说明如何在最低部署目标早于 iOS 17、iPadOS 17、macOS 14、tvOS 17 或 watchOS 10 的 SwiftUI App 中观察模型数据变化。要让你的 App 为上述操作系统的更新版本做好准备，参见[从 Observable Object 协议迁移到 Observable 宏](migrating-from-the-observable-object-protocol-to-the-observable-macro.md)。如果你的 App 最低部署目标为 iOS 17、iPadOS 17、macOS 14、tvOS 17 或 watchOS 10 及更高版本，请使用[在 App 中管理模型数据](managing-model-data-in-your-app.md)中描述的观察方式。

### 让模型数据可观察

要让模型中的数据变化对 SwiftUI 可见，请让模型类采用 [ObservableObject](../combine/observableobject.md) 协议。例如，你可以创建一个作为可观察对象的 `Book` 类：

```swift
class Book: ObservableObject {
}
```

系统会自动为该类推断 [ObjectWillChangePublisher](../combine/observableobject/objectwillchangepublisher.md) 关联类型，并合成所需的 [objectWillChange](../combine/observableobject/objectwillchange.md) 方法，该方法会发出已发布属性的变化值。要发布某个属性，在该属性的声明上添加 [Published](../combine/published.md) 属性包装器：

```swift
class Book: ObservableObject {
    @Published var title = "Sample Book Title"
}
```

不需要发布属性时，避免发布带来的开销。只发布那些既可能变化又对 UI 重要的属性。例如，`Book` 类可能有一个 `identifier` 属性，它在初始化之后从不变化：

```swift
class Book: ObservableObject {
    @Published var title = "Sample Book Title"

    let identifier = UUID() // A unique identifier that never changes.
}
```

你仍然可以在用户界面中显示这个标识符，但由于它没有被发布，SwiftUI 不会监视这个特定属性的变化。

### 监视可观察对象的变化

要让 SwiftUI 监视某个可观察对象，在该属性的声明上添加 [ObservedObject](observedobject.md) 属性包装器：

```swift
struct BookView: View {
    @ObservedObject var book: Book
    
    var body: some View {
        Text(book.title)
    }
}
```

如上所示，你可以把可观察对象的单个属性传递给子视图。当数据变化时（例如从磁盘载入新数据时），SwiftUI 会更新所有受影响的视图。你也可以把整个可观察对象传给子视图，在视图层级结构的多个层级之间共享模型对象：

```swift
struct BookView: View {
    @ObservedObject var book: Book
    
    var body: some View {
        BookEditView(book: book)
    }
}

struct BookEditView: View {
    @ObservedObject var book: Book

    // ...
}
```

### 在视图中实例化模型对象

SwiftUI 可能在任何时候创建或重新创建视图，因此关键在于：用给定的一组输入来初始化视图时，必须总是得到相同的视图。因此，在视图内部创建被观察对象是不安全的。作为替代，SwiftUI 提供了 [StateObject](stateobject.md) 属性包装器，为你存储在视图层级结构中的引用类型创建单一的事实来源。你可以用这种方式在视图内部安全地创建 `Book` 实例：

```swift
struct LibraryView: View {
    @StateObject private var book = Book()
    
    var body: some View {
        BookView(book: book)
    }
}
```

状态对象的行为与被观察对象类似，区别在于：无论 SwiftUI 重新创建视图多少次，它都会为给定的视图实例创建并管理单一的对象实例。你可以在本地使用该对象，或者像上面的示例那样，把状态对象传入另一个视图的被观察对象属性。

虽然 SwiftUI 不会在视图内重新创建状态对象，但它会为每个视图实例创建一个独立的对象实例。例如，下面代码中的每个 `LibraryView` 都会得到一个独一无二的 `Book` 实例：

```swift
VStack {
    LibraryView()
    LibraryView()
}
```

你也可以在顶层的 [App](app.md) 实例中，或在 App 的某个 [Scene](scene.md) 实例中创建状态对象。例如，如果你为一个图书阅读 App 定义了一个名为 `Library` 的可观察对象来保存图书集合，你可以在 App 的顶层结构中创建单一的 library 实例：

```swift
@main
struct BookReader: App {
    @StateObject private var library = Library()

    // ...
}
```

### 在整个 App 中共享对象

如果你有一个想在整个 App 中使用的数据模型对象，但又不想让它穿过层层层级传递，可以改用 [environmentObject(_:)](<view/environmentobject(__).md>) 视图修饰符把这个对象放入环境：

```swift
@main
struct BookReader: App {
    @StateObject private var library = Library()
    
    var body: some Scene {
        WindowGroup {
            LibraryView()
                .environmentObject(library)
        }
    }
}
```

应用该修饰符的视图的任何后代视图，随后都可以通过声明一个带 [EnvironmentObject](environmentobject.md) 属性包装器的属性来访问这个数据模型实例：

```swift
struct LibraryView: View {
    @EnvironmentObject var library: Library
    
    // ...
}
```

如果你使用环境对象，可以像上面那样把它加到 App 层级结构顶部的视图上，也可以把它加到视图层级结构中某个子树的根视图上。无论哪种方式，请记得同时把它加到任何使用该对象的视图（或其有后代使用该对象的视图）的预览提供器中：

```swift
struct LibraryView_Previews: PreviewProvider {
    static var previews: some View {
        LibraryView()
            .environmentObject(Library())
    }
}
```

### 使用绑定创建双向连接

当你允许用户在 UI 中更改数据时，请使用指向相应属性的绑定。这能确保更新自动流回数据模型。你可以通过在对象名前加美元符号（`$`）来获得指向被观察对象、状态对象或环境对象属性的绑定。例如，如果你通过在 `BookEditView` 中添加一个 [TextField](textfield.md) 来让用户编辑书名，就给这个文本栏一个指向书的 `title` 属性的绑定：

```swift
struct BookEditView: View {
    @ObservedObject var book: Book
    
    var body: some View {
        TextField("Title", text: $book.title)
    }
}
```

绑定把视图元素连接到底层模型，使人们能够直接修改模型数据。

## 另请参阅

### 创建模型数据

- [在 App 中管理模型数据](managing-model-data-in-your-app.md) — 在你的 App 数据模型与视图之间创建连接。
- [从 Observable Object 协议迁移到 Observable 宏](migrating-from-the-observable-object-protocol-to-the-observable-macro.md) — 更新你现有的 App，以利用 Swift 中 Observation 的优势。
- [Observable()](<../observation/observable().md>) — 定义并实现 Observable 协议的一致性。
- [StateObject](stateobject.md) — 一种实例化可观察对象的属性包装器类型。
- [ObservedObject](observedobject.md) — 一种订阅可观察对象并在其变化时使视图失效的属性包装器类型。
- [ObservableObject](../combine/observableobject.md) — 一种带有发布器的对象类型，该发布器在对象变化之前发出信号。

## 下载

- [ObservableObjectSample.zip](https://docs-assets.developer.apple.com/published/6c60346a45d3/ObservableObjectSample.zip)
