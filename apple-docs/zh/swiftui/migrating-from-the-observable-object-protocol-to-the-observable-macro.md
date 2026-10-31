---
title: 从 ObservableObject 协议迁移到 Observable 宏
framework: SwiftUI
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, Xcode 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/migrating-from-the-observable-object-protocol-to-the-observable-macro
source_url: 'https://developer.apple.com/documentation/swiftui/migrating-from-the-observable-object-protocol-to-the-observable-macro'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/migrating-from-the-observable-object-protocol-to-the-observable-macro.json'
content_hash: 'sha256:b766eade906c5e9b'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [模型数据](model-data.md)

# 从 ObservableObject 协议迁移到 Observable 宏

<sub>示例代码</sub>

更新你现有的 App，以利用 Swift 中 Observation 的种种优势。

## 概述

从 iOS 17、iPadOS 17、macOS 14、tvOS 17 和 watchOS 10 开始，SwiftUI 提供了对 [Observation](../observation.md) 的支持，这是观察者设计模式的一种 Swift 专属实现。采用 Observation 可以给你的 App 带来以下好处：

- 跟踪可选值和对象集合，这在使用 [ObservableObject](../combine/observableobject.md) 时是无法做到的。
- 使用 [State()](<state().md>) 和 [Environment](environment.md) 等现有数据流原语，而不是 [StateObject](stateobject.md) 和 [EnvironmentObject](environmentobject.md) 等基于对象的等价物。
- 根据视图的 [body](view/body-8kl5o.md) 所读取的可观察属性的变化来更新视图，而不是根据可观察对象发生的任何属性变化来更新视图，这有助于提升 App 的性能。

要在你的 App 中利用这些好处，你将了解如何把依赖 [ObservableObject](../combine/observableobject.md) 的现有源代码替换为利用 [Observable()](<../observation/observable().md>) 宏的代码。

> [!note] 注意
> 下载本示例可以查看示例 App 迁移后的版本。要查看迁移前的版本，请下载[监测 App 中的数据变化](monitoring-model-data-changes-in-your-app.md)中提供的示例。你也可以使用迁移前的版本来配合本文编写代码。

### 使用 Observable 宏

要在现有 App 中采用 [Observation](../observation.md)，首先将数据模型类型中的 [ObservableObject](../combine/observableobject.md) 替换为 [Observable()](<../observation/observable().md>) 宏。[Observable()](<../observation/observable().md>) 宏会在编译时生成源代码，为该类型添加观察支持。

```swift
// BEFORE
import SwiftUI

class Library: ObservableObject {
    // ...
}
```

```swift
// AFTER
import SwiftUI

@Observable class Library {
    // ...
}
```

然后从可观察属性中移除 [Published](../combine/published.md) 属性包装器。Observation 不需要属性包装器就能让属性可观察。相反，属性相对于观察者（例如视图）的可访问性决定了属性是否可观察。

```swift
// BEFORE
class Library {
    @Published var books: [Book] = [Book(), Book(), Book()]
}
```

```swift
// AFTER
@Observable class Library {
    var books: [Book] = [Book(), Book(), Book()]
}
```

如果有些属性观察者可以访问，但你不想跟踪它们，请对属性应用 [ObservationIgnored()](<../observation/observationignored().md>) 宏。

### 增量迁移

你不需要在整个 App 中全盘替换 [ObservableObject](../combine/observableobject.md) 协议。相反，你可以增量地进行更改。首先把一个数据模型类型改为使用 [Observable()](<../observation/observable().md>) 宏。你的 App 可以混用使用不同观察系统的数据模型类型。不过，SwiftUI 会根据数据模型类型使用的观察系统（`Observable` 还是 `ObservableObject`）以不同的方式跟踪变化。

你可能会注意到 App 在不同跟踪方式下的细微行为差异。例如，当按 [Observable()](<../observation/observable().md>) 跟踪时，只有当可观察属性发生变化、且视图的 [body](view/body-8kl5o.md) 直接读取了该属性时，SwiftUI 才会更新视图。当 `body` 未读取的可观察属性发生变化时，视图不会更新。相比之下，当按 `ObservableObject` 跟踪时，只要 [ObservableObject](../combine/observableobject.md) 实例的任何发布属性发生变化，视图就会更新，即使视图并未读取发生变化的属性。

> [!note] 注意
> 要进一步了解当可观察属性变化时 SwiftUI 何时更新视图，请参阅[在 App 中管理模型数据](managing-model-data-in-your-app.md)。

### 迁移其他源代码

到目前为止，示例 App 唯一的更改是将 [Observable()](<../observation/observable().md>) 宏应用到 `Library`，并移除对 [ObservableObject](../combine/observableobject.md) 协议的支持。App 仍在使用 [ObservableObject](../combine/observableobject.md) 数据流原语（例如 [StateObject](stateobject.md)）来管理 `Library` 实例。如果你构建并运行该 App，SwiftUI 仍会按预期更新视图。这是因为 [StateObject](stateobject.md) 和 [EnvironmentObject](environmentobject.md) 等数据流属性包装器支持使用 [Observable()](<../observation/observable().md>) 宏的类型。SwiftUI 提供这种支持，是为了让 App 能够增量地修改源代码。

但是，要完全采用 [Observation](../observation.md)，请在更新数据模型类型之后，将 [StateObject](stateobject.md) 的使用替换为 [State()](<state().md>)。例如，在下面的代码中，主 App 结构创建了一个 `Library` 实例并将其存储为 `StateObject`。它还使用 [environmentObject(_:)](<view/environmentobject(__).md>) 修饰符将 `Library` 实例添加到环境中。

```swift
// BEFORE
@main
struct BookReaderApp: App {
    @StateObject private var library = Library()

    var body: some Scene {
        WindowGroup {
            LibraryView()
                .environmentObject(library)
        }
    }
}
```

现在 `Library` 不再符合 [ObservableObject](../combine/observableobject.md)，代码可以改为使用 [State()](<state().md>) 而不是 [StateObject](stateobject.md)，并使用 [environment(_:)](<view/environment(__).md>) 修饰符将 `library` 添加到环境中。

```swift
// AFTER
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

在 `Library` 完全采用 [Observation](../observation.md) 之前，还需要一处更改。此前，视图 `LibraryView` 使用 [EnvironmentObject](environmentobject.md) 属性包装器从环境中获取 `Library` 实例。而现在，新代码改用 [Environment](environment.md) 属性包装器。

```swift
// BEFORE
struct LibraryView: View {
    @EnvironmentObject var library: Library

    var body: some View {
        List(library.books) { book in
            BookView(book: book)
        }
    }
}
```

```swift
// AFTER
struct LibraryView: View {
    @Environment(Library.self) private var library
    
    var body: some View {
        List(library.books) { book in
            BookView(book: book)
        }
    }
}
```

### 移除 ObservedObject 属性包装器

为了完成示例 App 的迁移，将数据模型类型 `Book` 改为支持 [Observation](../observation.md)：从类型声明中移除 [ObservableObject](../combine/observableobject.md)，并应用 [Observable()](<../observation/observable().md>) 宏。然后从可观察属性中移除 [Published](../combine/published.md) 属性包装器。

```swift
// BEFORE
class Book: ObservableObject, Identifiable {
    @Published var title = "Sample Book Title"
    
    let id = UUID() // A unique identifier that never changes.
}
```

```swift
// AFTER
@Observable class Book: Identifiable {
    var title = "Sample Book Title"
    
    let id = UUID() // A unique identifier that never changes.
}
```

接下来，从 `BookView` 的 `book` 变量中移除 [ObservedObject](observedobject.md) 属性包装器。采用 [Observation](../observation.md) 后不再需要这个属性包装器。这是因为 SwiftUI 会自动跟踪视图的 [body](view/body-8kl5o.md) 直接读取的任何可观察属性。例如，当 `book.title` 变化时，SwiftUI 会更新 `BookView`。

```swift
// BEFORE
struct BookView: View {
    @ObservedObject var book: Book
    @State private var isEditorPresented = false
    
    var body: some View {
        HStack {
            Text(book.title)
            Spacer()
            Button("Edit") {
                isEditorPresented = true
            }
        }
        .sheet(isPresented: $isEditorPresented) {
            BookEditView(book: book)
        }
    }
}
```

```swift
// AFTER
struct BookView: View {
    var book: Book
    @State private var isEditorPresented = false
    
    var body: some View {
        HStack {
            Text(book.title)
            Spacer()
            Button("Edit") {
                isEditorPresented = true
            }
        }
        .sheet(isPresented: $isEditorPresented) {
            BookEditView(book: book)
        }
    }
}
```

不过，如果视图需要绑定到某个可观察类型，请将 [ObservedObject](observedobject.md) 替换为 [Bindable](bindable.md) 属性包装器。这个属性包装器为可观察类型提供绑定支持，让期望绑定的视图能够更改可观察属性。例如，在下面的代码中，[TextField](textfield.md) 接收到一个绑定到 `book.title` 的绑定：

```swift
// BEFORE
struct BookEditView: View {
    @ObservedObject var book: Book
    @Environment(\.dismiss) private var dismiss
    
    var body: some View {
        VStack() {
            TextField("Title", text: $book.title)
                .textFieldStyle(.roundedBorder)
                .onSubmit {
                    dismiss()
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

```swift
// AFTER
struct BookEditView: View {
    @Bindable var book: Book
    @Environment(\.dismiss) private var dismiss
    
    var body: some View {
        VStack() {
            TextField("Title", text: $book.title)
                .textFieldStyle(.roundedBorder)
                .onSubmit {
                    dismiss()
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

## 另请参阅

### 创建模型数据

- [在 App 中管理模型数据](managing-model-data-in-your-app.md) — 在 App 的数据模型和视图之间建立连接。
- [Observable()](<../observation/observable().md>) — 定义并实现 Observable 协议的一致性。
- [监测 App 中的数据变化](monitoring-model-data-changes-in-your-app.md) — 使用可观察对象在 App 的用户界面中显示数据变化。
- [StateObject](stateobject.md) — 一种属性包装器类型，用于实例化可观察对象。
- [ObservedObject](observedobject.md) — 一种属性包装器类型，订阅可观察对象，并在可观察对象变化时使视图失效。
- [ObservableObject](../combine/observableobject.md) — 一种对象类型，具有在对象变化之前发出通知的发布者。

## 下载

- [ObservationSample.zip](https://docs-assets.developer.apple.com/published/b78f7ecb6749/ObservationSample.zip)
