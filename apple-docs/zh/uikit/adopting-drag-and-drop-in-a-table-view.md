---
title: 在表格视图中采用拖放
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, Xcode 12.5+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/adopting-drag-and-drop-in-a-table-view
source_url: 'https://developer.apple.com/documentation/uikit/adopting-drag-and-drop-in-a-table-view'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/adopting-drag-and-drop-in-a-table-view.json'
content_hash: 'sha256:ae2ce7f214db13ba'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Drag and drop](drag-and-drop.md)

# 在表格视图中采用拖放

<sub>示例代码</sub>

演示如何为表格视图启用并实现拖放。

## 概述

此示例代码项目使用 [UITableView](uitableview.md) 实例来展示如何将表格视图设为拖动源和放置目的地。

要启用拖放，请将表格视图指定为其自身的拖动委托和放置委托。要提供或使用数据，请实现拖放委托方法。

与自定义视图所遵循的流程相比，在表格视图中采用拖放存在一些重要差异。有关步骤比较，请参阅[在自定义视图中采用拖放](adopting-drag-and-drop-in-a-custom-view.md)。

### 在示例 App 中拖动文本

将此项目部署到 iPad，因为 iPad 支持在 App 之间进行拖放。首次启动此项目构建的 App 时，你会看到一个包含多行内容的表格，每行都有一个文本字符串。将此 App 与另一个支持编辑文本字符串的 App（例如“备忘录”或“提醒事项”）配合使用。例如，将 iPad 屏幕配置为分屏浏览，让此 App 与“提醒事项”并排显示。然后，将一行内容从此 App 拖到“提醒事项”，或将一条提醒事项拖到此 App。

此 App 还支持通过上下拖动行来重新排列它们。不过，此 App 的重新排列使用传统的 [- tableView:canMoveRowAtIndexPath:](<uitableviewdatasource/tableview(__canmoverowat_).md>) 和 [- tableView:moveRowAtIndexPath:toIndexPath:](<uitableviewdatasource/tableview(__moverowat_to_).md>) 方法，而不是拖放 API。

### 启用拖放交互

要启用拖动、放置或两者，请将表格视图指定为其自身的拖动或放置委托。App 的 [- viewDidLoad](<uiviewcontroller/viewdidload().md>) 方法是放置这些代码的便利位置。以下代码同时启用拖动和放置：

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    tableView.dragInteractionEnabled = true
    tableView.dragDelegate = self
    tableView.dropDelegate = self

    navigationItem.rightBarButtonItem = editButtonItem
}
```

与自定义视图不同，表格视图没有用于添加交互的 `interactions` 属性。表格视图会直接使用拖动委托和放置委托。

### 为拖动会话提供数据

要提供从表格视图拖动的数据，请实现 [- tableView:itemsForBeginningDragSession:atIndexPath:](<uitableviewdragdelegate/tableview(__itemsforbeginning_at_).md>) 方法。以下是这段代码中与模型无关的部分：

```swift
func tableView(_ tableView: UITableView, itemsForBeginning session: UIDragSession, at indexPath: IndexPath) -> [UIDragItem] {
    return model.dragItems(for: indexPath)
}
```

以下辅助函数由 `tableView(_:itemsForBeginning:at:)` 方法使用，充当此示例代码项目中数据模型的接口：

```swift
func dragItems(for indexPath: IndexPath) -> [UIDragItem] {
    let placeName = placeNames[indexPath.row]

    let data = placeName.data(using: .utf8)
    let itemProvider = NSItemProvider()

    itemProvider.registerDataRepresentation(forTypeIdentifier: kUTTypePlainText as String, visibility: .all) { completion in
        completion(data, nil)
        return nil
    }

    return [
        UIDragItem(itemProvider: itemProvider)
    ]
}
```

### 使用放置会话中的数据

要在表格视图中使用放置会话的数据，请实现三个委托方法。

首先，你的 App 可以根据拖动条目的类、App 状态或其他要求拒绝条目。此项目的实现只允许用户放置 [`NSString`](../foundation/nsstring.md) 类的实例。以下是这段代码中与模型无关的部分：

```swift
func tableView(_ tableView: UITableView, canHandle session: UIDropSession) -> Bool {
    return model.canHandle(session)
}
```

以下辅助函数由 [- tableView:canHandleDropSession:](<uitableviewdropdelegate/tableview(__canhandle_).md>) 方法使用，充当数据模型的接口：

```swift
func canHandle(_ session: UIDropSession) -> Bool {
    return session.canLoadObjects(ofClass: NSString.self)
}
```

其次，你必须告诉系统希望如何使用数据，通常是进行拷贝。你通过放置提案来指定这一选择：

```swift
func tableView(_ tableView: UITableView, dropSessionDidUpdate session: UIDropSession, withDestinationIndexPath destinationIndexPath: IndexPath?) -> UITableViewDropProposal {
    var dropProposal = UITableViewDropProposal(operation: .cancel)

    // 只接受一个拖动条目。
    guard session.items.count == 1 else { return dropProposal }

    // .move 拖动操作仅适用于此 App 内部且处于编辑模式时的拖动。
    if tableView.hasActiveDrag {
        if tableView.isEditing {
            dropProposal = UITableViewDropProposal(operation: .move, intent: .insertAtDestinationIndexPath)
        }
    } else {
        // 拖动来自 App 外部。
        dropProposal = UITableViewDropProposal(operation: .copy, intent: .insertAtDestinationIndexPath)
    }

    return dropProposal
}
```

最后，当用户将手指从屏幕上抬起，表明其放置拖动条目的意图后，表格视图有一次机会请求拖动条目的特定数据表示：

```swift
/**
     此委托方法是访问和载入拖动条目所提供数据表示的
     唯一机会。放置协调器支持访问放置的条目、更新表格视图，
     以及指定可选动画。包含一个条目的本地拖动会通过
     数据源上现有的
     `tableView(_:moveRowAt:to:)` 方法处理。
*/
func tableView(_ tableView: UITableView, performDropWith coordinator: UITableViewDropCoordinator) {
    let destinationIndexPath: IndexPath

    if let indexPath = coordinator.destinationIndexPath {
        destinationIndexPath = indexPath
    } else {
        // 获取表格视图的最后一个索引路径。
        let section = tableView.numberOfSections - 1
        let row = tableView.numberOfRows(inSection: section)
        destinationIndexPath = IndexPath(row: row, section: section)
    }

    coordinator.session.loadObjects(ofClass: NSString.self) { items in
        // 使用拖动条目。
        let stringItems = items as! [String]

        var indexPaths = [IndexPath]()
        for (index, item) in stringItems.enumerated() {
            let indexPath = IndexPath(row: destinationIndexPath.row + index, section: destinationIndexPath.section)
            self.model.addItem(item, at: indexPath.row)
            indexPaths.append(indexPath)
        }

        tableView.insertRows(at: indexPaths, with: .automatic)
    }
}
```

除这三个方法外，拖放还提供其他 API 钩子，用于自定义表格视图对该功能的采用。有关提供和使用数据的更多信息，请参阅[在表格视图中支持拖放](supporting-drag-and-drop-in-table-views.md)。

## 另请参阅

### 基础

- [将拖动条目理解为承诺](understanding-a-drag-item-as-a-promise.md) — 使用拖动条目在源 App 和目的 App 之间传递数据表示承诺。
- [将视图设为拖动源](making-a-view-into-a-drag-source.md) — 采用拖动交互 API 来提供可供拖动的条目。
- [将视图设为放置目的地](making-a-view-into-a-drop-destination.md) — 采用放置交互 API，有选择地使用拖动的内容。
- [在自定义视图中采用拖放](adopting-drag-and-drop-in-a-custom-view.md) — 演示如何为 `UIImageView` 实例启用拖放。

## 下载

- [AdoptingDragAndDropInATableView.zip](https://docs-assets.developer.apple.com/published/eaf99c41437f/AdoptingDragAndDropInATableView.zip)
