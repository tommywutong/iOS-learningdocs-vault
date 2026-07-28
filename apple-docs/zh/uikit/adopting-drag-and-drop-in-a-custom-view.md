---
title: 在自定义视图中采用拖放
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, Xcode 11.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/adopting-drag-and-drop-in-a-custom-view
source_url: 'https://developer.apple.com/documentation/uikit/adopting-drag-and-drop-in-a-custom-view'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/adopting-drag-and-drop-in-a-custom-view.json'
content_hash: 'sha256:a4373ad1d5779034'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [拖放](drag-and-drop.md)

# 在自定义视图中采用拖放

<sub>示例代码</sub>

演示如何为 `UIImageView` 实例启用拖放（drag and drop）。

## 概述

此示例代码项目使用 [UIImageView](uiimageview.md) 实例来展示 [UIView](uiview.md) 类的任意实例或子类如何充当拖动源或放置目的地。

要启用拖放，请向视图添加一个或多个交互对象。要提供或使用数据，请实现交互委托（delegate）中的协议方法。

### 开始使用

将此示例代码项目部署到 iPad，因为 iPad 支持在 App 之间进行拖放。首次启动此项目构建的 App 时，你会看到一个包含图像的图像视图。将此 App 与另一个包含图像的 App（例如“照片”）配合使用。例如，将 iPad 屏幕配置为分屏浏览，让此 App 与“照片”并排显示。然后，将图像从此 App 拖到“照片”，或将图像从“照片”拖到此 App。

### 启用拖放交互

要启用拖动、放置或两者，请将交互附加到视图。App 的 [- viewDidLoad](<uiviewcontroller/viewdidload().md>) 方法是放置这些代码的便利位置。

添加拖动交互：

```swift
let dragInteraction = UIDragInteraction(delegate: self)
imageView.addInteraction(dragInteraction)
```

添加放置交互：

```swift
let dropInteraction = UIDropInteraction(delegate: self)
view.addInteraction(dropInteraction)
```

为图像视图启用拖放还需要一个额外步骤，此项目使用的正是图像视图。你必须明确启用用户交互，如下所示：

```swift
imageView.isUserInteractionEnabled = true
```

### 为拖动会话提供数据

[- dragInteraction:itemsForBeginningSession:](<uidraginteractiondelegate/draginteraction(__itemsforbeginning_).md>) 方法是允许从视图开始拖动所必需的唯一方法。

```swift
func dragInteraction(_ interaction: UIDragInteraction, itemsForBeginning session: UIDragSession) -> [UIDragItem] {
    guard let image = imageView.image else { return [] }

    let provider = NSItemProvider(object: image)
    let item = UIDragItem(itemProvider: provider)
    item.localObject = image

    /*
         如此处所示，返回非空数组会启用拖动。你可以改为
         返回空数组来停用拖动。
    */
    return [item]
}
```

系统会响应用户发起拖动的手势，调用此委托方法。在你的实现中，返回包含一个或多个拖动条目的数组，每个条目带有一个条目提供器。在每个条目提供器中，为要拖动的模型对象指定一种或多种数据表示。模型对象必须遵循 [`NSItemProviderWriting`](../foundation/nsitemproviderwriting.md) 协议。

有关为拖动提供数据的更多信息，请参阅[将视图设为拖动源](making-a-view-into-a-drag-source.md)。

### 使用放置会话中的数据

要让视图能够使用放置会话中的数据，请实现三个委托方法。

首先，你的 App 可以根据拖动条目的统一类型标识符（UTI）、App 状态或其他要求拒绝条目。此实现只允许用户放置一个符合 `kUTTypeImage` UTI 的条目：

```swift
func dropInteraction(_ interaction: UIDropInteraction, canHandle session: UIDropSession) -> Bool {
    return session.hasItemsConforming(toTypeIdentifiers: [kUTTypeImage as String]) && session.items.count == 1
}
```

其次，你必须告诉系统希望如何使用数据，通常是进行拷贝。你通过放置提案来指定这一选择：

```swift
func dropInteraction(_ interaction: UIDropInteraction, sessionDidUpdate session: UIDropSession) -> UIDropProposal {
    let dropLocation = session.location(in: view)
    updateLayers(forDropLocation: dropLocation)

    let operation: UIDropOperation

    if imageView.frame.contains(dropLocation) {
        /*
             如果为 .move 操作添加
             App 内拖放支持，必须编写代码来协调拖动交互
             委托和放置交互委托。
        */
        operation = session.localDragSession == nil ? .copy : .move
    } else {
        // 不允许在图像视图之外放置。
        operation = .cancel
    }

    return UIDropProposal(operation: operation)
}
```

最后，当用户将手指从屏幕上抬起，表明其放置拖动条目的意图后，视图有一次机会请求拖动条目的特定数据表示：

```swift
func dropInteraction(_ interaction: UIDropInteraction, performDrop session: UIDropSession) {
    // 使用拖动条目（此示例中的类型为 UIImage）。
    session.loadObjects(ofClass: UIImage.self) { imageItems in
        let images = imageItems as! [UIImage]

        /*
             如果不使用 UIDropSession 类的 loadObjects(ofClass:completion:)
             便利方法（该方法会自动使用主线程），
             请明确将 UI 工作分派到主线程。
             例如，可以使用 `DispatchQueue.main.async` 方法。
        */
        self.imageView.image = images.first
    }

    // 根据需要执行其他 UI 更新。
    let dropLocation = session.location(in: view)
    updateLayers(forDropLocation: dropLocation)
}
```

除这三个方法外，拖放还提供其他 API 钩子，用于自定义你对该功能的采用。有关使用放置会话中数据的更多信息，请参阅[将视图设为放置目的地](making-a-view-into-a-drop-destination.md)。

## 另请参阅

### 基础

- [将拖动条目理解为承诺](understanding-a-drag-item-as-a-promise.md) — 使用拖动条目在源 App 和目的 App 之间传递数据表示承诺。
- [将视图设为拖动源](making-a-view-into-a-drag-source.md) — 采用拖动交互 API 来提供可供拖动的条目。
- [将视图设为放置目的地](making-a-view-into-a-drop-destination.md) — 采用放置交互 API，有选择地使用拖动的内容。
- [在表格视图中采用拖放](adopting-drag-and-drop-in-a-table-view.md) — 演示如何为表格视图（table view）启用和实现拖放。

## 下载

- [AdoptingDragAndDropInACustomView.zip](https://docs-assets.developer.apple.com/published/64088647bd17/AdoptingDragAndDropInACustomView.zip)
