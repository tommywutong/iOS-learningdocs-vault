---
title: 让视图成为拖拽源
framework: SwiftUI
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/making-a-view-into-a-drag-source
source_url: 'https://developer.apple.com/documentation/swiftui/making-a-view-into-a-drag-source'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/making-a-view-into-a-drag-source.json'
content_hash: 'sha256:35b4d5465d6b7585'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [拖放](drag-and-drop.md)

# 让视图成为拖拽源

<sub>文章</sub>

采用 draggable API 为拖放操作提供条目。

## 概述

当有人拖动你的 App 中某个条目在屏幕上的视觉表示时（例如照片、「地图」位置、「日历」日程或一段文本选择），该拖拽操作会携带一些与之关联的数据，以及系统所显示的数据预览。添加 [draggable(_:)](<view/draggable(__).md>) 修饰符以使视图能够作为拖拽源发挥作用，并提供一个符合 [`Transferable`](../coretransferable/transferable.md) 协议的值。

`Transferable` 协议描述了如何为共享和数据传输序列化和反序列化你的模型对象。它通过组合 Core Transferable 框架内置的一个或多个 [`TransferRepresentation`](../coretransferable/transferrepresentation.md) 类型来提供传输表示。

### 将视图启用为拖拽源

使用 `draggable(_:)` 修饰符在 App 内、你自己的一组 App 之间，或你的 App 与其他支持导入或导出指定数据格式的 App 之间发送或接收 `Transferable` 条目。

```swift
struct MyView: View {
    let name = "Mei Chen"
    
    var body: some View {
        Text(name)
            .draggable(name)
    }
}
```

使用 [draggable(_:preview:)](<view/draggable(__preview_).md>) 修饰符为被拖动的条目定义自定义预览。

```swift
    Text(name)
        .draggable(name) {
            ZStack {
                RoundedRectangle(cornerRadius: 10)
                    .frame(width: 300, height: 300)
                    .foregroundStyle(.yellow.gradient)
                Text("Drop \(name)")
                    .font(.title)
                    .foregroundStyle(.red)
            }
        }
```

要在系统过渡到显示你的自定义 `preview` 时自定它所显示的抬升预览，请应用一个带有 [dragPreview](contentshapekinds/dragpreview.md) 类型的 [contentShape(_:_:eoFill:)](<view/contentshape(____eofill_).md>) 修饰符。例如，你可以更改预览的圆角半径，如下面的代码示例所示：

```swift
    Text(name)
        .contentShape(.dragPreview, RoundedRectangle(cornerRadius: 7))
        .draggable(name) {
            ZStack {
                RoundedRectangle(cornerRadius: 20)
                    .frame(width: 300, height: 300)
                    .foregroundStyle(.yellow.gradient)
                Text("Drop \(name)")
                    .font(.title)
                    .foregroundStyle(.red)
            }
        }
```

### 为拖放操作创建可传输条目

要支持模型对象的拖拽操作，请让模型遵循 `Transferable` 协议以创建可传输条目，并实现 [`transferRepresentation`](../coretransferable/transferrepresentation.md) 静态属性。像 [`String`](../swift/string.md)、[`Data`](../foundation/data.md)、[`URL`](../foundation/url.md) 和 [`Image`](image.md) 这样的类型已经符合 `Transferable`，因此很容易在拖放操作中使用它们。

定义一个表示用户资料的数据模型，它是一个符合 [`Codable`](../swift/codable.md) 的类型，具有 `name` 和 `phoneNumber` 属性。

```swift
struct Profile: Codable, Identifiable {
    var id: UUID = UUID()
    var name: String
    var phoneNumber: String
}
```

扩展 `Profile` 使其遵循 `Transferable` 协议来组合一个传输表示，并添加带有自定义统一类型标识符 `com.example.profile` 的 [`CodableRepresentation`](../coretransferable/codablerepresentation.md) 来表示 `Profile` 数据结构。

```swift
extension Profile: Transferable {
    static var transferRepresentation: some TransferRepresentation {
        CodableRepresentation(contentType: .profile)
        ProxyRepresentation(exporting: \.name)
    }
}
```

请确保在 App 的 `Info.plist` 文件中包含该自定义统一类型标识符。更多信息请参阅[为你的 App 定义文件和数据类型](../uniformtypeidentifiers/defining-file-and-data-types-for-your-app.md)。

在 [`UTType`](../uniformtypeidentifiers/uttype-swift.struct.md) 上将新的统一类型标识符声明为便捷变量。对于导出式声明，使用以下代码：

```swift
extension UTType {
    static var profile = UTType(exportedAs: "com.example.profile")
}
```

前面代码示例中的另一种传输表示是 [`ProxyRepresentation`](../coretransferable/proxyrepresentation.md)，它使用 `String` 结构体内置的 `Transferable` 一致性。`ProxyRepresentation` 作为一种备选方案，让人们可以把资料条目拖放到任何不支持 `com.example.profile` 内容类型、但支持文本格式的文本编辑器中。

要向可拖动条目添加更多传输表示，请按优先顺序指定一个或多个额外的表示。这可以确保系统根据接收方可为拖放操作接受的内容类型，使用最合适的表示。更多信息请参阅[为模型类型选择传输表示](../coretransferable/choosing-a-transfer-representation-for-a-model-type.md)。

要使用 `com.example.profile` 内容类型进行拖拽操作，请将 profiles 传递给 `draggable(_:)` 修饰符。

```swift
struct ContentView: View {
    @State private var profiles = [
        Profile(name: "Juan Chavez", phoneNumber: "(408) 555-4301"),
        Profile(name: "Mei Chen", phoneNumber: "(919) 555-2481")
    ]
    
    var body: some View {
        List {
            ForEach(profiles) { profile in
                Text(profile.name)
                    .draggable(profile)
            }
        }
    }
}
```

### 启用列表重排

在 [List](list.md) 中，你可以使用 [onMove(perform:)](<dynamicviewcontent/onmove(perform_).md>) 修饰符来启用重排。该修饰符允许你通过长按某一行然后将其拖动到新位置来重新排列列表条目。将 `onMove(perform:)` 修饰符添加到 `List` 以启用该交互。

```swift
    List {
        ForEach(profiles) { profile in
            Text(profile.name)
        }
        .onMove { indices, newOffset in
            // 根据来源和目标索引更新条目数组。
            profiles.move(fromOffsets: indices, toOffset: newOffset)
        }
    }
```

要有条件地停用特定行上的条目重排，请将 [moveDisabled(_:)](<view/movedisabled(__).md>) 设置为 `true`。

## 另请参阅

### 基础

- [使用 SwiftUI 采用拖放](adopting-drag-and-drop-using-swiftui.md) — 在列表、表格和自定义视图中启用拖放交互。
- [在列表、叠放、网格和自定义布局中重排条目](reordering-items-in-lists-stacks-grids-and-custom-layouts.md) — 使用重排修饰符为 SwiftUI 布局添加拖拽重排交互。
