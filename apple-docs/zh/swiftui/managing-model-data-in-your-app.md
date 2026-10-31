---
title: 在你的 App 中管理模型数据
framework: SwiftUI
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, Xcode 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/managing-model-data-in-your-app
source_url: 'https://developer.apple.com/documentation/swiftui/managing-model-data-in-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/managing-model-data-in-your-app.json'
content_hash: 'sha256:a2cc180f6bacb5f3'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [模型数据](model-data.md)

# 在你的 App 中管理模型数据

<sub>示例代码</sub>

在你的 App 的数据模型与视图之间建立连接。

## 概述

SwiftUI App 可以显示人们能够通过 App 的用户界面（UI）更改的数据。为了管理这些数据，App 会创建一个数据模型，即一个表示数据的自定义类型。数据模型将数据与与数据交互的视图分离开来。这种分离提高了模块化程度、改善了可测试性，并让理解 App 的工作方式变得更容易。

让模型数据（即数据模型的实例）与屏幕上显示的内容保持同步可能颇具挑战，尤其是当数据同时出现在 UI 的多个视图中时。

得益于 Observation，SwiftUI 能让你的 App 的 UI 随数据的变化保持最新。借助 [Observation](../observation.md)，SwiftUI 中的视图可以对可观察的数据模型形成依赖，并在数据变化时更新 UI。

> [!note] 注意
> SwiftUI 对 [Observation](../observation.md) 的支持从 iOS 17、iPadOS 17、macOS 14、tvOS 17 和 watchOS 10 开始提供。有关在现有 App 中采用 Observation 的信息，请参阅[从 Observable Object 协议迁移到 Observable 宏](migrating-from-the-observable-object-protocol-to-the-observable-macro.md)。

### 让模型数据可观察

要让 SwiftUI 看到数据的变化，请将 [Observable()](<../observation/observable().md>) 宏应用于你的数据模型。该宏会在编译期生成代码，为你的数据模型添加观察支持，让你的数据模型代码专注于存储数据的属性。例如，以下代码为一个图书数据模型定义了类型：

```swift
@Observable class Book: Identifiable {
    var title = "Sample Book Title"
    var author = Author()
    var isAvailable = true
}
```

> [!important] 重要
> [Observable()](<../observation/observable().md>) 宏除了添加观察功能之外，还会让你的数据模型类型符合 [Observable](../observation/observable.md) 协议，该协议向其他 API 发出你的类型支持观察的信号。不要只把 `Observable` 协议本身应用于你的数据模型类型，因为仅这样做不会添加任何观察功能。相反，在为你的类型添加观察支持时，请始终使用 `Observable` 宏。

### 在视图中观察模型数据

在 SwiftUI 中，当视图的 [body](view/body-8kl5o.md) 属性读取一个可观察数据模型对象（例如 `Book` 的实例）的某个属性时，视图就会对该对象形成依赖。如果 `body` 没有读取可观察数据模型对象的任何属性，视图就不会追踪任何依赖。

当被追踪的属性发生变化时，SwiftUI 会更新视图。如果 [body](view/body-8kl5o.md) 没有读取的其他属性发生变化，视图不受影响，从而避免不必要的更新。例如，以下代码中的视图只在图书的 `title` 变化时更新，而在 `author` 或 `isAvailable` 变化时不会更新：

```swift
struct BookView: View {
    var book: Book
    
    var body: some View {
        Text(book.title)
    }
}
```

即使视图不存储可观察类型（例如使用全局属性或单例时），SwiftUI 也会建立这种依赖追踪：

```swift
var globalBook: Book = Book()

struct BookView: View {
    var body: some View {
        Text(globalBook.title)
    }
}
```

当计算属性使用了某个可观察属性时，Observation 也支持对计算属性的追踪。例如，以下代码中的视图会在可借阅图书数量变化时更新：

```swift
@Observable class Library {
    var books: [Book] = [Book(), Book(), Book()]
    
    var availableBooksCount: Int {
        books.filter(\.isAvailable).count
    }
}

struct LibraryView: View {
    @Environment(Library.self) private var library
    
    var body: some View {
        NavigationStack {
            List(library.books) { book in
                // ...
            }
            .navigationTitle("Books available: \(library.availableBooksCount)")
        }
    }
}
```

当视图对一个对象集合（无论是哪种集合类型）形成依赖时，视图会追踪对集合本身所做的更改。例如，以下代码中的视图对 `books` 形成了依赖，因为 `body` 读取了它。当 `books` 发生变化时（例如在集合中插入、删除、移动或替换条目），SwiftUI 会更新视图。

```swift
struct LibraryView: View {
    @State private var books = [Book(), Book(), Book()]

    var body: some View {
        List(books) { book in 
            Text(book.title)
        }
    }
}
```

但是，`LibraryView` 并不会对 `title` 属性形成依赖，因为视图的 [body](view/body-8kl5o.md) 没有直接读取它。视图将 [List](list.md) 的内容闭包存储为一个 `@escaping` 闭包，SwiftUI 会在列表条目出现在屏幕上之前惰性创建它们时调用该闭包。这意味着依赖图书 `title` 的不是 `LibraryView`，而是列表的每个 [Text](text.md) 条目各自依赖 `title`。对某个 `title` 的任何更改只会更新表示该图书的那个 [Text](text.md)，而不会更新其他视图。

> [!note] 注意
> Observation 会追踪视图的 [body](view/body-8kl5o.md) 属性执行范围内出现的任何可观察属性的更改。

你还可以与其他视图共享一个可观察的模型数据对象。如果接收方视图在其 [body](view/body-8kl5o.md) 中读取了该对象的任何属性，它就会形成依赖。例如，在以下代码中，`LibraryView` 与 `BookView` 共享一个 `Book` 实例，`BookView` 显示该图书的 `title`。如果图书的 `title` 发生变化，SwiftUI 只会更新 `BookView`，而不会更新 `LibraryView`，因为只有 `BookView` 读取了 `title` 属性。

```swift
struct LibraryView: View {
    @State private var books = [Book(), Book(), Book()]

    var body: some View {
        List(books) { book in 
            BookView(book: book)
        }
    }
}

struct BookView: View {
    var book: Book
    
    var body: some View {
        Text(book.title)
    }
}
```

如果视图没有任何依赖，SwiftUI 就不会在数据变化时更新该视图。这种方式使可观察的模型数据对象能够穿过视图层级结构的多个层级，而无需每个中间视图都形成依赖。

```swift
// 当 `book` 的任何属性变化时不会更新。
struct LibraryView: View {
    @State private var books = [Book(), Book(), Book()]
    
    var body: some View {
        List(books) { book in 
            LibraryItemView(book: book)
        }
    }
}

// 当 `book` 的任何属性变化时不会更新。
struct LibraryItemView: View {
    var book: Book
    
    var body: some View {
        BookView(book: book)
    }
}

// 当 `book.title` 变化时会更新。
struct BookView: View {
    var book: Book
    
    var body: some View {
        Text(book.title)
    }
}
```

但是，存储了可观察对象引用的视图会在引用发生变化时更新。这是因为存储的引用是视图值的一部分，而不是因为该对象是可观察的。例如，如果以下代码中对 book 的引用发生变化，SwiftUI 会更新该视图：

```swift
struct BookView: View {
    var book: Book
    
    var body: some View {
        // ...
    }
}
```

视图还可以对通过另一个对象访问的可观察数据模型对象形成依赖。例如，以下代码中的视图会在作者的 `name` 变化时更新：

```swift
struct LibraryItemView: View {
    var book: Book
    
    var body: some View {
        VStack(alignment: .leading) {
            Text(book.title)
            Text("Written by: \(book.author.name)")
                .font(.caption)
        }
    }
}
```

### 为模型数据创建事实来源

要创建并存储模型数据的事实来源（source of truth），请声明一个私有变量，并用一个可观察数据模型类型的实例来初始化它。然后添加 [State()](<state().md>) 宏，声明由 SwiftUI 管理该属性。例如，以下代码将数据模型类型 `Book` 的一个实例存储在状态变量 `book` 中：

```swift
struct BookView: View {
    @State private var book = Book()
    
    var body: some View {
        Text(book.title)
    }
}
```

通过用 [State()](<state().md>) 包装 book，你是在告诉 SwiftUI 来管理该实例的存储。SwiftUI 每次重新创建 `BookView` 时，都会将 `book` 变量连接到受管实例，从而为视图提供模型数据的单一事实来源。

你也可以在顶层的 [App](app.md) 实例中，或在你的 App 的某个 [Scene](scene.md) 实例中创建状态对象。例如，以下代码在 App 的顶层结构中创建了一个 `Library` 实例：

```swift
@main
struct BookReaderApp: App {
    @State private var library = Library()
    
    var body: some Scene {
        WindowGroup {
            LibraryView()
                .environment(library)
        }
    }
}
```

### 在视图层级结构中共享模型数据

如果你有一个想在整个 App 中共享的数据模型对象（例如 `Library`），你可以：

- 将数据模型对象传递给视图层级结构中的每个视图；或者
- 将数据模型对象添加到视图的环境（environment）中

当你的视图层级结构较浅时，将模型数据传递给每个视图会很方便；例如，当某个视图不与它的子视图共享该对象时。但是，你通常无法确定某个视图是否需要将对象传递给子视图，也可能无法确定层级结构深处的某个子视图是否需要该模型数据。

要在视图层级结构中共享模型数据而不必将其传递给每个视图，请将模型数据添加到视图的环境（environment）中。你可以使用 [environment(_:_:)](<view/environment(____).md>) 或 [environment(_:)](<view/environment(__).md>) 修饰符把数据添加到环境中，并传入模型数据。

在使用 [environment(_:_:)](<view/environment(____).md>) 修饰符之前，你需要创建一个自定义的 [EnvironmentKey](environmentkey.md)。然后扩展 [EnvironmentValues](environmentvalues.md)，加入一个自定义环境属性，用于获取和设置自定义键的值。例如，以下代码为 `library` 创建了一个环境键和属性：

```swift
extension EnvironmentValues {
    var library: Library {
        get { self[LibraryKey.self] }
        set { self[LibraryKey.self] = newValue }
    }
}

private struct LibraryKey: EnvironmentKey {
    static let defaultValue: Library = Library()
}
```

有了自定义环境键和属性之后，视图就可以将模型数据添加到它的环境中。例如，`LibraryView` 使用 [environment(_:_:)](<view/environment(____).md>) 修饰符将 `Library` 实例的事实来源添加到它的环境中：

```swift
@main
struct BookReaderApp: App {
    @State private var library = Library()
    
    var body: some Scene {
        WindowGroup {
            LibraryView()
                .environment(\.library, library)
        }
    }
}
```

要从环境中获取 `Library` 实例，视图需要定义一个存储该实例引用的局部变量，然后用 [Environment](environment.md) 属性包装器包装该变量，并传入指向自定义环境值的键路径。

```swift
struct LibraryView: View {
    @Environment(\.library) private var library

    var body: some View {
        // ...
    }
}
```

你也可以使用 [environment(_:)](<view/environment(__).md>) 修饰符，在无需定义自定义环境值的情况下将模型数据直接存储在环境中。例如，以下代码使用该修饰符将一个 `Library` 实例添加到环境中：

```swift
@main
struct BookReaderApp: App {
    @State private var library = Library()
    
    var body: some Scene {
        WindowGroup {
            LibraryView()
                .environment(library)
        }
    }
}
```

要从环境中获取该实例，另一个视图需要定义一个局部变量来存储该实例，并用 [Environment](environment.md) 属性包装器包装它。但这一次你可以不提供指向环境值的键路径，而是提供模型数据类型，如下面的代码所示：

```swift
struct LibraryView: View {
    @Environment(Library.self) private var library
    
    var body: some View {
        // ...
    }
}
```

默认情况下，以对象类型作为键从环境中读取对象时，会返回一个非可选对象。这个默认行为假定当前层级结构中的某个视图之前已使用 [environment(_:)](<view/environment(__).md>) 修饰符存储了该类型的非可选实例。如果视图尝试使用其类型来获取某个对象，而该对象不在环境中，SwiftUI 会抛出异常。

在无法保证对象一定在环境中的情况下，请按照以下代码所示获取对象的可选版本。如果对象在环境中不可用，SwiftUI 会返回 `nil` 而不是抛出异常。

```swift
@Environment(Library.self) private var library: Library?
```

### 在视图中更改模型数据

在大多数 App 中，人们可以更改 App 呈现的数据。当数据变化时，任何显示该数据的视图都应更新以反映变化后的数据。借助 SwiftUI 中的 Observation，视图无需使用属性包装器或绑定即可支持数据更改。例如，以下代码在按钮的操作闭包中切换图书的 `isAvailable` 属性：

```swift
struct BookView: View {
    var book: Book
    
    var body: some View {
        List {
            Text(book.title)
            HStack {
                Text(book.isAvailable ? "Available for checkout" : "Waiting for return")
                Spacer()
                Button(book.isAvailable ? "Check out" : "Return") {
                    book.isAvailable.toggle()
                }
            }
        }
    }
}
```

不过，有时视图需要先获得一个绑定才能更改可变属性的值。要提供绑定，请用 [Bindable](bindable.md) 属性包装器包装模型数据。例如，以下代码用 `@Bindable` 包装了 `book` 变量，然后使用 [TextField](textfield.md) 更改图书的 `title` 属性，并使用 [Toggle](toggle.md) 更改 `isAvailable` 属性，通过 `$` 语法将绑定传递给每个属性。

```swift
struct BookEditView: View {
    @Bindable var book: Book
    @Environment(\.dismiss) private var dismiss
    
    var body: some View {
        VStack() {
            HStack {
                Text("Title")
                TextField("Title", text: $book.title)
                    .textFieldStyle(.roundedBorder)
                    .onSubmit {
                        dismiss()
                    }
            }
            
            Toggle(isOn: $book.isAvailable) {
                Text("Book is available")
            }
            
            Button("Close") {
                dismiss()
            }
            .buttonStyle(.borderedProminent)
        }
        .padding()
    }
}
```

你可以对 [Observable](../observation/observable.md) 对象的属性和变量使用 [Bindable](bindable.md) 属性包装器。这包括全局变量、存在于 SwiftUI 类型之外的属性，甚至局部变量。例如，你可以在视图的 [body](view/body-8kl5o.md) 中创建一个 `@Bindable` 变量：

```swift
struct LibraryView: View {
    @State private var books = [Book(), Book(), Book()]

    var body: some View {
        List(books) { book in 
            @Bindable var book = book
            TextField("Title", text: $book.title)
        }
    }
}
```

`@Bindable` 变量 `book` 提供了一个绑定，将 [TextField](textfield.md) 连接到图书的 `title` 属性，使人们能够直接对模型数据进行更改。

## 另请参阅

### 创建模型数据

- [从 Observable Object 协议迁移到 Observable 宏](migrating-from-the-observable-object-protocol-to-the-observable-macro.md) — 更新你现有的 App，以利用 Swift 中 Observation 的优势。
- [Observable()](<../observation/observable().md>) — 定义并实现 Observable 协议的一致性。
- [在你的 App 中监控数据变化](monitoring-model-data-changes-in-your-app.md) — 使用可观察对象在你的 App 的用户界面中显示数据变化。
- [StateObject](stateobject.md) — 一种实例化可观察对象的属性包装器类型。
- [ObservedObject](observedobject.md) — 一种订阅可观察对象的属性包装器类型，在可观察对象变化时使视图失效。
- [ObservableObject](../combine/observableobject.md) — 一种具有发布者的对象类型，在对象发生变化之前发出消息。

## 下载

- [ManagingModelDataSample.zip](https://docs-assets.developer.apple.com/published/6c08da4d9562/ManagingModelDataSample.zip)
