---
title: 使用 SwiftUI 采用拖放
framework: SwiftUI
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+, Xcode 16.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/adopting-drag-and-drop-using-swiftui
source_url: 'https://developer.apple.com/documentation/swiftui/adopting-drag-and-drop-using-swiftui'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/adopting-drag-and-drop-using-swiftui.json'
content_hash: 'sha256:dd101f14097aab3c'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [拖放](drag-and-drop.md)

# 使用 SwiftUI 采用拖放

<sub>示例代码</sub>

在列表、表格和自定义视图中启用拖放交互。

## 概述

本示例代码项目演示了 SwiftUI 视图如何充当拖拽源或放置目的地。

要启用拖拽交互，请将 [draggable(_:)](<view/draggable(__).md>) 修饰符添加到某个视图，以便在 App 内、你自己的一组 App 之间，或你的 App 与其他支持导入或导出指定数据格式的 App 之间发送或接收 [`Transferable`](../coretransferable/transferable.md) 条目。要处理放置的内容，请使用 [dropDestination(for:action:isTargeted:)](<view/dropdestination(for_action_istargeted_).md>) 修饰符来接收预期的放置条目。

在示例 App 中，人们可以把一个联系人从联系人列表中拖出并放入另一个 App；例如「通讯录」「备忘录」或「信息」。此外，人们还可以把来自其他 App（例如「通讯录」或「备忘录」）的新联系人拖放到示例 App 中。

在 iPad 上，人们可以在分屏浏览中将本示例与第二个 App（例如「通讯录」或「备忘录」）配合使用。人们可以把本 App 中的一行拖到「通讯录」，也可以把「通讯录」中的联系人拖到本 App 中。

### 启用拖拽交互

要启用拖动，请将 `draggable(_:)` 修饰符添加到某个视图，以发送符合 `Transferable` 协议的条目。

```swift
List {
    ForEach(dataModel.contacts) { contact in
        NavigationLink {
            ContactDetailView(contact: contact)
        } label: {
            CompactContactView(contact: contact)
                .draggable(contact) {
                    ThumbnailView(contact: contact)
                }
        }
    }
}
```

当有人从联系人列表中拖动一个联系人时，App 会使用 [draggable(_:preview:)](<view/draggable(__preview_).md>) 修饰符为被拖动的条目定义自定义预览。

要进一步了解如何采用 draggable API 为拖拽操作提供条目，请参阅[让视图成为拖拽源](making-a-view-into-a-drag-source.md)。

### 启用放置交互

使用 `dropDestination(for:action:isTargeted:)` 修饰符来接收被拖动的条目，并定义处理放置内容的目的地。

```swift
.dropDestination(for: Contact.self) { droppedContacts, index in
    dataModel.handleDroppedContacts(droppedContacts: droppedContacts, index: index)
}
```

该修饰符需要一个符合 `Transferable` 协议的 `Contact` 类型。`dropDestination(for:action:isTargeted:)` 修饰符的实现使用 [transferRepresentation](https://developer.apple.com/coretransferable/transferrepresentation) 来接收表示被放置联系人信息的拖拽条目。

App 按优先顺序定义了传输表示。App 会使用最合适的表示来创建并初始化一个 `Contact` 对象。

```swift
static var transferRepresentation: some TransferRepresentation {
    // 允许通过自定义内容类型传输 Contact。
    CodableRepresentation(contentType: .exampleContact)
    // 允许以 vCard 格式导入和导出 Contact 数据。
    DataRepresentation(contentType: .vCard) { contact in
        try contact.toVCardData()
    } importing: { data in
        try await parseVCardData(data)
    }
    .suggestedFileName { $0.fullName }
    // 支持导出 `phoneNumber` 字符串作为整个 `Contact` 的代理。
    ProxyRepresentation { contact in
        contact.phoneNumber
    } importing: { value in
        Contact(id: UUID().uuidString, givenName: value, familyName: "", phoneNumber: "")
    }
}
```

如果 App 收到带有自定义[统一类型标识符](../uniformtypeidentifiers.md)（例如 `com.example.contact`）的条目，它会使用 [`CodableRepresentation`](../coretransferable/codablerepresentation.md) 来表示 `Contact` 数据结构。

示例 App 声明的 `com.example.contact` 遵循 public.contact。为确保操作系统知道如何处理该内容类型，它应当遵循 `UTType.data`、`UTType.package` 或继承自这两者的某个类型。

[`ProxyRepresentation`](../coretransferable/proxyrepresentation.md) 作为一种备选表示，允许人们把联系人拖放到任何不支持 `com.example.contact` 或 [`vCard`](../uniformtypeidentifiers/uttype-swift.struct/vcard.md) 内容、但支持文本格式的文本编辑器中。在这种情况下，App 会将 `phoneNumber` 作为字符串导出。当有人把一个字符串放到 [List](list.md) 或 [Table](table.md) 上时，示例 App 会使用 `ProxyRepresentation` 将该字符串转换为 `Contact` 对象。

最后，[`DataRepresentation`](../coretransferable/datarepresentation.md) 会创建 `Contact` 对象的二进制表示，并为支持 `vCard` 内容类型的接收方构建该值。

当有人把联系人放到 `Table` 或 `List` 上时，完成处理程序会将被放置的联系人插入到放置位置的联系人集合中。如果放置操作未指定索引，完成处理程序会将联系人添加到集合的末尾。

```swift
func handleDroppedContacts(droppedContacts: [Contact], index: Int? = nil) {
    guard let firstContact = droppedContacts.first else {
        return
    }
    // 如果第一个联系人的 ID 已存在于联系人列表中，
    // 则将该联系人从当前位置移动到新的索引处。
    // 如果未指定索引，则将联系人插入到列表末尾。
    if let existingIndex = contacts.firstIndex(where: { $0.id == firstContact.id }) {
        let indexSet = IndexSet(integer: existingIndex)
        contacts.move(fromOffsets: indexSet, toOffset: index ?? contacts.endIndex)
    } else {
        contacts.insert(firstContact, at: index ?? contacts.endIndex)
    }
}
```

最后，`dropDestination(for:action:isTargeted:)` 修饰符可以接收从任何其他视图或 App 发起的拖拽交互。

有关采用拖放的设计指引，请参阅《人机界面指南》\> [Drag and drop](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop)。

## 另请参阅

### 基础

- [让视图成为拖拽源](making-a-view-into-a-drag-source.md) — 采用 draggable API 为拖放操作提供条目。
- [在列表、叠放、网格和自定义布局中重排条目](reordering-items-in-lists-stacks-grids-and-custom-layouts.md) — 使用重排修饰符为 SwiftUI 布局添加拖拽重排交互。

## 下载

- [AdoptingDragAndDropUsingSwiftUI.zip](https://docs-assets.developer.apple.com/published/865816f9f1f5/AdoptingDragAndDropUsingSwiftUI.zip)
