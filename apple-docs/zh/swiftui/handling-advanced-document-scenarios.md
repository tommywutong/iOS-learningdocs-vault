---
title: 处理高级文稿场景
framework: SwiftUI
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/handling-advanced-document-scenarios
source_url: 'https://developer.apple.com/documentation/swiftui/handling-advanced-document-scenarios'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/handling-advanced-document-scenarios.json'
content_hash: 'sha256:19e3fec2fae04c02'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [文稿](documents.md)

# 处理高级文稿场景

<sub>文章</sub>

扩展你的基于文稿的 App，以支持自定文件格式、按需文件访问和进度报告。

## 概述

创建出可正常运行的基于文稿的 App 后，你可以扩展它以处理超出基本读写范畴的场景。通过使用自定 [UTType](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype) 来支持系统默认不了解的文件格式。使用 [makeFileCoordinator()](<urldocumentconfiguration/makefilecoordinator().md>) 在正常的读取和写入生命周期之外访问文件，例如按需打开包（package）中的某个特定子文件。添加进度报告，在长时间操作期间为用户提供反馈。

> [!note] 注意
> 如果你是刚接触 SwiftUI 中基于文稿的 App，请从[创建基于文稿的 App](creating-a-document-based-app.md) 开始。

## 声明自定文件格式

系统了解常用的内置格式及其标识符，例如 [utf8PlainText](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/utf8plaintext)、[jpeg](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/jpeg) 和 [markdown](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/markdown)。对于你自己的文件格式，请声明一个自定 [`UTType`](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype)，让访达、文稿浏览器和「聚焦」都能理解它们。

每个自定类型都需要一个基本类型来告诉系统它是什么类型的文件。对于单文件文稿，使用 `public.data` 或符合它的类型作为基本类型；对于系统以目录形式存储、但以单个文件形式呈现的文稿，使用 `com.apple.package`。

在 App target 的信息属性列表中的 `UTExportedTypeDeclarations` 下声明内容类型，让访达、文稿浏览器和「聚焦」都能识别它。将 `UTTypeConformsTo` 设置为匹配的基本类型，并添加一个 `UTTypeTagSpecification`，将类型映射到你的文件名扩展名。下面的示例声明了一个笔记本（notebook）包；对于扁平文件格式，把 `com.apple.package` 换成 `public.data`，如下所示：

```xml
<key>UTExportedTypeDeclarations</key>
<array>
    <dict>
        <key>UTTypeIdentifier</key>
        <string>com.example.notebook</string>
        <key>UTTypeConformsTo</key>
        <array>
            <string>com.apple.package</string>
        </array>
        <key>UTTypeTagSpecification</key>
        <dict>
            <key>public.filename-extension</key>
            <array>
                <string>examplenotebook</string>
            </array>
        </dict>
    </dict>
</array>
```

为方便起见，在代码中镜像这个声明，如下所示：

```swift
extension UTType {
    static let notebook = UTType(exportedAs: "com.example.notebook")
}
```

然后从文稿的 [readableContentTypes](readabledocument/readablecontenttypes.md) 和 [writableContentTypes](writabledocument/writablecontenttypes.md) 引用你的类型，如下所示：

```swift
static let readableContentTypes: [UTType] = [.notebook]
static let writableContentTypes: [UTType] = [.notebook, .utf8PlainText]
```

有关为专有格式声明统一类型标识符的更多信息，请参阅[为 App 定义文件和数据类型](../uniformtypeidentifiers/defining-file-and-data-types-for-your-app.md)。

> [!note] 注意
> 每台 Mac 都会注册系统提供的标准内容类型，但每台计算机能识别的较少见类型集合取决于其安装的软件。例如，如果没有已安装的 App 声明某些媒体类型，计算机可能无法识别它们。同样，未安装 Xcode 的计算机无法识别 `com.apple.xcode.resultbundle`（Xcode result bundle 的类型标识符）。

## 在读写之外访问文件

SwiftUI 会自动为 `read` 和 `write` 调用协调文件访问。要在其他时间访问文件 URL——例如读取包中的某个特定子文件时——请使用配置的文件协调器，如下所示：

```swift
let coordinator = document.configuration.makeFileCoordinator()
coordinator.coordinate(
    readingItemAt: packageURL.appending(path: "metadata.json"),
                       options: []) { url in
    do {
        let data = try Data(contentsOf: url)
        let metadata = try JSONDecoder().decode(NotebookMetadata.self, from: data)
        // 处理元数据。
    } catch {
        // 处理错误。
    }
}
```

> [!important] 重要
> 在 `read` 和 `write` 之外进行磁盘访问时，请务必使用 [makeFileCoordinator()](<urldocumentconfiguration/makefilecoordinator().md>)。直接访问文件 URL 有损坏数据的风险，因为其他进程（包括 iCloud）随时可能更改它。

## 报告进度

包（package）让你可以增量地读取和写入；你不必在每次更改时加载或保存整个文稿，而是可以只读取需要的文件、只写入发生变化的文件。对于由多个文件组成的笔记本文稿、把数据存储在单独文件中的自定图像格式，或包含嵌入式媒体的项目，这可能意味着快速的自动保存与缓慢的自动保存之间的差别。

[DocumentReader](documentreader.md) 和 [DocumentWriter](documentwriter.md) 分别通过各自的 `read` 和 `write` 方法接收一个 [Subprogress](https://developer.apple.com/documentation/foundation/subprogress) 参数。通过该参数报告进度，让 SwiftUI 能在长时间操作期间显示相应的 UI。

通过指定总单位数，从 [`Subprogress`](https://developer.apple.com/documentation/foundation/subprogress) 创建一个 [ProgressReporter](https://developer.apple.com/documentation/foundation/progressreporter)。然后随着工作完成调用 [complete(count:)](<https://developer.apple.com/documentation/foundation/progressreporter/complete(count:)>)，如下所示：

```swift
@concurrent 
func read(from source: URL, progress: consuming Subprogress) async throws -> sending ImageSnapshot {
    let progressManager = progress.start(totalCount: 2)
    let data = try Data(contentsOf: source)
    progressManager.complete(count: 1)
    let image = try decodeImage(from: data)
    progressManager.complete(count: 1)
    return ImageSnapshot(image: image)
}
```

对于包文稿，你可以把每个文件视为等量的一份工作，如下所示。这种方式可以在写入器逐个处理文件时提供细粒度的反馈。

```swift
@concurrent
func write(
    snapshot: sending NotebookSnapshot, to destination: URL,
    previous: sending NotebookSnapshot?, progress: consuming Subprogress
) async throws {
    let changedPages = snapshot.pages.filter { (identifier, content) in
        previous?.pages[identifier] != content
    }

    // 元数据占一个单位，每个发生变化的页面各占一个单位。
    let totalUnits = 1 + changedPages.count
    let progressManager = progress.start(totalCount: totalUnits)

    // 写入元数据。
    let metadataURL = destination.appending(path: "metadata.json")
    let metadataData = try JSONEncoder().encode(snapshot.metadata)
    try metadataData.write(to: metadataURL, options: .atomic)
    progressManager.complete(count: 1)

    // 逐个写入每个发生变化的页面。
    let fileManager = FileManager.default
    let pagesDirectory = destination.appending(path: "pages")

    // 如果 pages 子目录尚不存在，则创建它。
    try? fileManager.createDirectory(
        at: pagesDirectory, withIntermediateDirectories: true
    )

    for (identifier, content) in changedPages {
        let pageURL = pagesDirectory.appending(
            path: "\(identifier.uuidString).txt"
        )
        let data = Data(content.utf8)
        try data.write(to: pageURL, options: .atomic)
        progressManager.complete(count: 1)
    }
}
```

如果你使用 [FileHandle](https://developer.apple.com/documentation/foundation/filehandle) 或 [OutputStream](https://developer.apple.com/documentation/foundation/outputstream) 分块写入文件——例如一个大的媒体文件——请在每个块写入后报告进度，而不是只在最后报告一次。每次调用 [`complete(count:)`](<https://developer.apple.com/documentation/foundation/progressreporter/complete(count:)>) 都会让进度条向前推进，因此应把调用分散在整个写入过程中。

下面的示例以分块方式把一个大型媒体文件写入磁盘。将总单位数设为以字节为单位的文件大小，并在每个块写入后调用报告器，让进度条平滑更新。

```swift
@concurrent
func write(
    snapshot: sending MediaSnapshot, to destination: URL,
    previous: sending MediaSnapshot?, progress: consuming Subprogress
) async throws {
    let payload = snapshot.payload
    let totalBytes = payload.count
    let progressManager = progress.start(totalCount: totalBytes)

    try Data().write(to: destination)
    let fileHandle = try FileHandle(forWritingTo: destination)
    defer { try? fileHandle.close() }

    // 目标是在整个写入过程中进行约 100 次进度更新，并加以限制，
    // 使块大到足以摊销系统调用开销，
    // 又小到能在极小负载下保持进度条移动。
    let targetUpdateCount = 100
    let minimumChunkSize = 64 * 1024        //  64 KB
    let maximumChunkSize = 4 * 1024 * 1024  //   4 MB
    let chunkSize = min(
        maximumChunkSize,
        max(minimumChunkSize, totalBytes / targetUpdateCount)
    )

    var offset = 0
    while offset < totalBytes {
        let end = min(offset + chunkSize, totalBytes)
        let chunk = payload[offset..<end]
        try fileHandle.write(contentsOf: chunk)
        progressManager.complete(count: end - offset)
        offset = end
    }
}
```

块大小会随文件大小自适应，因此大文件不会产生不必要的系统开销。如果你改为流式传输到 [`OutputStream`](https://developer.apple.com/documentation/foundation/outputstream)，同样的模式也适用：打开流，按计算好的大小写入块，用写入的字节数调用 [`complete(count:)`](<https://developer.apple.com/documentation/foundation/progressreporter/complete(count:)>)，完成后再调用 `ProgresManager.complete(count:)`。

> [!note] 注意
> 即使你报告了进度，是否显示进度视图仍由 SwiftUI 决定。

## 另请参阅

### 创建文稿

- [创建基于文稿的 App](creating-a-document-based-app.md) — 构建可供用户通过协调的文件访问来打开、编辑和保存文件的 App。
- [更新你的基于文稿的 App](updating-your-document-based-app.md) — 迁移现有 App，以采用基于 URL 的文稿读取和写入并使用 Swift 并发。
- [使用 SwiftUI 构建基于文稿的 App](building-a-document-based-app-with-swiftui.md) — 在多平台 App 中创建、保存和打开文稿。
- [使用 SwiftData 构建基于文稿的 App](building-a-document-based-app-using-swiftdata.md) — 跟随 WWDC 讲者一起用 SwiftData 改造 App。
- [DocumentGroup](documentgroup.md) — 一种场景，支持打开、创建和保存文稿。
