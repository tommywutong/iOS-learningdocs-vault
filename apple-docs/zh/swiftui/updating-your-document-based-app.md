---
title: 更新你的基于文稿的 App
framework: SwiftUI
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/updating-your-document-based-app
source_url: 'https://developer.apple.com/documentation/swiftui/updating-your-document-based-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/updating-your-document-based-app.json'
content_hash: 'sha256:9bdf51d1adde5d06'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [文稿](documents.md)

# 更新你的基于文稿的 App

<sub>文章</sub>

迁移现有 App，以借助 Swift 并发采用基于 URL 的文稿读写。

## 概述

如果你有一个现有的基于文稿的 App，你可以采用 [Document](document.md) 协议来利用直接 URL 访问、Swift 并发集成以及现代观察（observation）。[Document](document.md) 协议将读取和写入分离到专门的类型中，这让你能更好地控制文件 I/O，并支持对复杂文稿格式的部分读取和写入。

在 iOS 27、iPadOS 27、macOS 27 和 visionOS 27 之前的版本中，你通过遵循 `FileDocument` 或 `ReferenceFileDocument` 来创建文稿类型。在这些版本及之后的版本中，你可以根据你的 App 的用途，选择遵循 `Document` 协议，或遵循 `ReadableDocument` 和 `WritableDocument` 协议。虽然 `FileDocument` 和 `ReferenceFileDocument` 仍然可用，但它们不再被推荐用于新的文稿类型。

下表突出了这三个协议之间的差异，帮助你选择正确的迁移路径：

|  | [FileDocument](filedocument.md) | [ReferenceFileDocument](referencefiledocument.md) | [Document](document.md) |
|---|---|---|---|
| 类型 | 值（`struct`） | 引用（`class`） | 引用（`class`） |
| 读取 | [init(configuration:)](<filedocument/init(configuration_).md>) | [init(configuration:)](<referencefiledocument/init(configuration_).md>) | [reader(configuration:)](<readabledocument/reader(configuration_).md>) + [apply(snapshot:previous:)](<readabledocument/apply(snapshot_previous_).md>) |
| 写入 | [fileWrapper(configuration:)](<filedocument/filewrapper(configuration_).md>) | [fileWrapper(snapshot:configuration:)](<referencefiledocument/filewrapper(snapshot_configuration_).md>) | [writer(configuration:)](<writabledocument/writer(configuration_).md>) + [snapshot(contentType:)](<writabledocument/snapshot(contenttype_).md>) |
| 读取与写入的执行方式 | 同步 | 同步 | `async`/`sending`，具有显式的 Actor 边界 |
| 文件访问 | 仅 [FileWrapper](https://developer.apple.com/documentation/foundation/filewrapper) | 仅 [`FileWrapper`](https://developer.apple.com/documentation/foundation/filewrapper) | URL 或 [`FileWrapper`](https://developer.apple.com/documentation/foundation/filewrapper) |
| 撤销 | 自动（值语义） | 手动（[UndoManager](https://developer.apple.com/documentation/foundation/undomanager)） | 手动（[`UndoManager`](https://developer.apple.com/documentation/foundation/undomanager)） |
| 观察 | 不适用（值类型） | [ObservableObject](https://developer.apple.com/documentation/combine/observableobject) | [@Observable](https://developer.apple.com/documentation/observation/observable) |

## 更新你的 App

根据你的 App 使用的已废弃协议，选择相应的标签页并按照清单更新你的 App：

**FileDocument**

1. **从结构体转换为标注了 [`@Observable`](https://developer.apple.com/documentation/observation/observable) 的类。** 遵循 [FileDocument](filedocument.md) 的文稿类型通常是值类型，而 [Document](document.md) 协议要求引用类型。请用一个标注了 [`@Observable`](https://developer.apple.com/documentation/observation/observable) 的 `final class` 替换你的结构体。
2. **将读取逻辑分离到 [DocumentReader](documentreader.md) 中。** 对于读取，使用 [FileWrapperDocumentReader](filewrapperdocumentreader.md) 并提供一个闭包，将 [`FileWrapper`](https://developer.apple.com/documentation/foundation/filewrapper) 转换为快照值。
3. **实现 [apply(snapshot:previous:)](<readabledocument/apply(snapshot_previous_).md>)。** 使用此方法在读取器传来新快照时更新你的文稿属性。
4. **将写入逻辑分离到 [DocumentWriter](documentwriter.md) 中。** 对于写入，使用 [FileWrapperDocumentWriter](filewrapperdocumentwriter.md) 并提供一个闭包，将快照转换为 [`FileWrapper`](https://developer.apple.com/documentation/foundation/filewrapper)。
5. **实现 [snapshot(contentType:)](<writabledocument/snapshot(contenttype_).md>)。** 添加此方法以在主要 Actor 上捕获文稿的当前状态。将其标记为 `async throws` 并返回一个 `sending` 值。
6. **添加撤销注册。** 使用 [FileDocument](filedocument.md) 时，SwiftUI 通过值语义和 [Binding](https://developer.apple.com/documentation/swiftui/binding) 自动管理撤销。而使用 [Document](document.md) 协议时，你需要使用 [`UndoManager`](https://developer.apple.com/documentation/foundation/undomanager) 自行注册撤销操作。你的内容视图环境中取得的撤销管理器已经连接到文稿。
7. **更新你的 [DocumentGroup](documentgroup.md) 初始化方法。** 将 `DocumentGroup(newDocument:)` 替换为接收 [URLDocumentConfiguration](urldocumentconfiguration.md) 和 [DocumentCreationContext](documentcreationcontext.md) 的基于闭包的初始化方法。
8. **更新你的内容视图。** 将 `@Binding var document: MyDocument` 替换为对可观察类的直接引用，并使用 [@Bindable](https://developer.apple.com/documentation/swiftui/bindable) 来创建绑定。

**ReferenceFileDocument**

1. **将你的文稿标记为 [`@Observable`](https://developer.apple.com/documentation/observation/observable)。** [ReferenceFileDocument](referencefiledocument.md) 协议早于 Observation 框架。请添加 [`@Observable`](https://developer.apple.com/documentation/observation/observable) 宏，并移除所有 [`ObservableObject`](https://developer.apple.com/documentation/combine/observableobject) 一致性和 [@Published](https://developer.apple.com/documentation/combine/published) 属性包装器。
2. **将读取逻辑分离到 [DocumentReader](documentreader.md) 中。** 对于读取，使用 [FileWrapperDocumentReader](filewrapperdocumentreader.md) 并提供一个闭包，将 [`FileWrapper`](https://developer.apple.com/documentation/foundation/filewrapper) 转换为快照值。
3. **实现 [apply(snapshot:previous:)](<readabledocument/apply(snapshot_previous_).md>)。** 使用此方法在读取器传来新快照时更新你的文稿属性。
4. **将写入逻辑分离到 [DocumentWriter](documentwriter.md) 中。** 对于写入，使用 [FileWrapperDocumentWriter](filewrapperdocumentwriter.md) 并提供一个闭包，将快照转换为 [`FileWrapper`](https://developer.apple.com/documentation/foundation/filewrapper)。
5. **实现 [snapshot(contentType:)](<writabledocument/snapshot(contenttype_).md>)。** 更新此方法，在返回类型上添加 `async throws` 和 `sending`，以支持跨并发边界的安全传输。
6. **更新你的 [DocumentGroup](documentgroup.md) 初始化方法。** 将基于类型的初始化方法替换为接收 [URLDocumentConfiguration](urldocumentconfiguration.md) 和 [DocumentCreationContext](documentcreationcontext.md) 的基于闭包的初始化方法。
7. **审查撤销注册。** 撤销注册在概念上是一样的，但请验证更改后你的撤销操作是否正常工作。

如果你现有的基于文稿的 App 使用 [FileDocument](filedocument.md) 或 [ReferenceFileDocument](referencefiledocument.md)，下表展示了各个概念如何映射到 [Document](document.md) 协议：

**FileDocument**

| 之前 | 之后 |
|---|---|
| [FileDocument](filedocument.md) | [Document](document.md) |
| `struct`（值类型） | [`@Observable`](https://developer.apple.com/documentation/observation/observable) `final class`（引用类型） |
| [init(configuration:)](<filedocument/init(configuration_).md>) | 独立的 [DocumentReader](documentreader.md) |
| [fileWrapper(configuration:)](<filedocument/filewrapper(configuration_).md>) | 独立的 [DocumentWriter](documentwriter.md) |
| 隐式快照（值语义） | 显式的 [snapshot(contentType:)](<writabledocument/snapshot(contenttype_).md>) 方法 |
| 通过 [`Binding`](https://developer.apple.com/documentation/swiftui/binding) 自动撤销 | 使用 [`UndoManager`](https://developer.apple.com/documentation/foundation/undomanager) 手动注册撤销 |
| `DocumentGroup(newDocument:)` | [DocumentGroup](documentgroup.md) 初始化方法 |

**ReferenceFileDocument**

| 之前 | 之后 |
|---|---|
| [ReferenceFileDocument](referencefiledocument.md) | [Document](document.md) |
| [init(configuration:)](<referencefiledocument/init(configuration_).md>) | 独立的 [DocumentReader](documentreader.md) |
| [fileWrapper(snapshot:configuration:)](<referencefiledocument/filewrapper(snapshot_configuration_).md>) | 独立的 [DocumentWriter](documentwriter.md) |
| 仅 [`FileWrapper`](https://developer.apple.com/documentation/foundation/filewrapper) | 通过 [DocumentReader](documentreader.md) 和 [DocumentWriter](documentwriter.md) 访问 [`FileWrapper`](https://developer.apple.com/documentation/foundation/filewrapper) 和 URL |
| [ReferenceFileDocument](referencefiledocument.md) 上的单一 `Snapshot` 类型 | [DocumentWriter](documentwriter.md) 和 [DocumentReader](documentreader.md) 上各自独立的 `Snapshot` 类型 |

以下示例展示了一个完整的文本文稿在从 [FileDocument](filedocument.md) 迁移前后的样子：

**之前**

```swift
struct TextDocument: FileDocument {
    static let readableContentTypes: [UTType] = [.plainText]

    var text: String

    init(configuration: ReadConfiguration) throws {
        guard let data = configuration.file.regularFileContents,
              let string = String(data: data, encoding: .utf8)
        else {
            throw CocoaError(.fileReadCorruptFile)
        }
        text = string
    }

    func fileWrapper(configuration: WriteConfiguration) throws -> FileWrapper {
        let data = Data(text.utf8)
        return FileWrapper(regularFileWithContents: data)
    }
}

struct TextDocumentApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: TextDocument()) { file in
            TextEditor(text: file.$document.text)
        }
    }
}
```

**之后**

```swift
@Observable
final class TextDocument: Document {
    static let readableContentTypes: [UTType] = [.plainText]

    var text: String

    init(text: String = "") {
        self.text = text
    }

    func reader(configuration: sending ReadConfiguration) -> sending FileWrapperDocumentReader<String> {
        FileWrapperDocumentReader(configuration) { fileWrapper in
            guard let data = fileWrapper.regularFileContents else {
                throw CocoaError(.fileReadCorruptFile)
            }
            return String(decoding: data, as: UTF8.self)
        }
    }

    func writer(configuration: sending WriteConfiguration) -> sending FileWrapperDocumentWriter<String> {
        FileWrapperDocumentWriter(configuration) { snapshot in
            FileWrapper(
                regularFileWithContents: Data(snapshot.utf8)
            )
        }
    }

    @MainActor
    func snapshot(contentType: UTType) async throws -> sending String {
        text
    }

    @MainActor
    func apply(snapshot: sending String, previous: sending String?) async throws {
        text = snapshot
    }
}

struct TextDocumentApp: App {
    var body: some Scene {
        DocumentGroup { document in
            TextDocumentView(document: document)
        } makeDocument: { _, _ in
            TextDocument()
        }
    }
}

struct TextDocumentView: View {
    @Bindable var document: TextDocument
    @Environment(\.undoManager) private var undoManager

    var body: some View {
        TextEditor(text: $document.text)
            .onChange(of: document.text) { oldValue, _ in
                undoManager?.registerUndo(
                    withTarget: document
                ) { document in
                    document.text = oldValue
                }
            }
    }
}
```

关键的结构性变化是从值语义转向引用语义。使用 [FileDocument](filedocument.md) 时，SwiftUI 通过指向结构体的 [`Binding`](https://developer.apple.com/documentation/swiftui/binding) 来追踪更改并自动管理撤销。而使用 [Document](document.md) 时，你使用 [`@Observable`](https://developer.apple.com/documentation/observation/observable) 来追踪更改并显式注册撤销操作——但由此获得了异步 I/O、基于 URL 的文件访问，以及状态捕获与序列化之间的清晰分离。

以下示例展示了一个完整的文本文稿在从 [ReferenceFileDocument](referencefiledocument.md) 迁移前后的样子：

**之前**

```swift
final class OldTextDocument: ReferenceFileDocument {
    typealias Snapshot = String

    static let readableContentTypes = [UTType.utf8PlainText]

    @Published var text: String

    init() {
        text = ""
    }

    required init(configuration: ReadConfiguration) throws {
        if let data = configuration.file.regularFileContents {
            text = String(data: data, encoding: .utf8) ?? ""
        } else {
            text = ""
        }
    }

    func snapshot(contentType: UTType) throws -> String {
        text
    }

    func fileWrapper(
        snapshot: String, configuration: WriteConfiguration
    ) throws -> FileWrapper {
        let data = snapshot.data(using: .utf8) ?? Data()
        return FileWrapper(regularFileWithContents: data)
    }
}
```

**之后**

```swift
@Observable
final class TextDocument: Document {
    static let readableContentTypes = [UTType.utf8PlainText]

    var text: String

    init() {
        text = ""
    }

    func reader(configuration: sending ReadConfiguration) -> sending FileWrapperDocumentReader<String> {
        FileWrapperDocumentReader(configuration) { fileWrapper in
            if let data = fileWrapper.regularFileContents,
               let text = String(data: data, encoding: .utf8) {
                return text
            }
            return ""
        }
    }

    @MainActor
    func apply(snapshot: sending String, previous: sending String?) async throws {
        text = snapshot
    }

    func writer(configuration: sending WriteConfiguration) -> sending FileWrapperDocumentWriter<String> {
        FileWrapperDocumentWriter(configuration) { snapshot, previous in
            let data = snapshot.data(using: .utf8) ?? Data()
            return FileWrapper(regularFileWithContents: data)
        }
    }

    @MainActor
    func snapshot(contentType: UTType) async throws -> sending String {
        text
    }
}

struct TextDocumentView: View {
    @Bindable var document: TextDocument
    @Environment(\.undoManager) private var undoManager

    var body: some View {
        TextEditor(text: $document.text)
            .onChange(of: document.text) { oldValue, _ in
                undoManager?.registerUndo(
                    withTarget: document
                ) { document in
                    document.text = oldValue
                }
            }
    }
}
```

迁移后的文稿清晰地分离了各项职责，支持面向高级用例的 URL 访问，采用了 Observation 框架，并集成了 Swift 并发。

## 另请参阅

### 创建文稿

- [创建基于文稿的 App](creating-a-document-based-app.md) — 构建让人们能够使用协调的文件访问来打开、编辑和保存文件的 App。
- [处理高级文稿场景](handling-advanced-document-scenarios.md) — 扩展你的基于文稿的 App，以支持自定义文件格式、按需文件访问和进度报告。
- [使用 SwiftUI 构建基于文稿的 App](building-a-document-based-app-with-swiftui.md) — 在多平台 App 中创建、保存和打开文稿。
- [使用 SwiftData 构建基于文稿的 App](building-a-document-based-app-using-swiftdata.md) — 跟随 WWDC 演讲者一起使用 SwiftData 改造一个 App。
- [DocumentGroup](documentgroup.md) — 一种支持打开、创建和保存文稿的场景。
