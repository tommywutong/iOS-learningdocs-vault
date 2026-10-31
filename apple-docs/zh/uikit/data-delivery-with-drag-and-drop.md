---
title: 使用拖放进行数据传递
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, Xcode 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/data-delivery-with-drag-and-drop
source_url: 'https://developer.apple.com/documentation/uikit/data-delivery-with-drag-and-drop'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/data-delivery-with-drag-and-drop.json'
content_hash: 'sha256:7134aa2dce321bf1'
translated: true
---

> 导航： [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Drag and drop](drag-and-drop.md)

# 使用拖放进行数据传递

<sub>示例代码</sub>

在 iPad App 之间进行拖放操作时，使用 item provider 共享数据。

## 概述

通过拖放，用户可以将数据从一个 iPad App 复制到另一个。数据通过 [`NSItemProvider`](../foundation/nsitemprovider.md) 对象在 App 之间共享。此示例代码项目展示如何使用 item provider 来：

- 共享用户从示例 iPad App 拖出并拖放到另一个 App 中的联系人。
- 检索用户从另一个 App 拖出并拖放到示例 App 中的联系人信息。

示例 iPad App 使用表格视图显示联系人列表。用户可以拖动一个或多个联系人并将其拖放到其他 App，如「联系人」或「备忘录」。同时，用户可以使用另一个 App（如「联系人」或「备忘录」）拖放新联系人到示例 App 中。

### 添加拖动支持

示例 App 中的表格视图显示联系人列表。当用户开始拖动联系人时，系统会调用 [- tableView:itemsForBeginningDragSession:atIndexPath:](<uitableviewdragdelegate/tableview(__itemsforbeginning_at_).md>) 方法。该方法的实现使用 `at` 参数确定联系人在列表中的位置，从列表中检索联系人。然后该方法使用联系人对象创建一个 item provider，并将 item provider 包装在 [UIDragItem](uidragitem.md) 对象中。该方法将拖拽项放入数组中并将其返回给系统。最后，系统将拖拽项添加到当前拖拽会话。

```swift
func tableView(_ tableView: UITableView,
               itemsForBeginning session: UIDragSession,
               at indexPath: IndexPath) -> [UIDragItem] {
    let contactCard = dataSource.clients[indexPath.row]
    let dragItem = UIDragItem(itemProvider: NSItemProvider(object: contactCard))
    return [dragItem]
}
```

用户可能会选择多个联系人拖动到另一个 App。每次用户选择一个联系人时，系统都会调用 [- tableView:itemsForAddingToDragSession:atIndexPath:point:](<uitableviewdragdelegate/tableview(__itemsforaddingto_at_point_).md>) 方法。与开始拖拽会话类似，此方法为所选联系人创建 item provider，创建包含 item provider 的拖拽项，并返回包含拖拽项的数组，以便系统将拖拽项添加到拖拽会话。

```swift
func tableView(_ tableView: UITableView,
               itemsForAddingTo session: UIDragSession,
               at indexPath: IndexPath,
               point: CGPoint) -> [UIDragItem] {
    // use this to NOT allow additional items to the drag:
    // return []

    let contactCard = dataSource.clients[indexPath.row]
    let dragItem = UIDragItem(itemProvider: NSItemProvider(object: contactCard))
    dragItem.localObject = true // makes it faster to drag and drop content within the same app
    return [dragItem]
}
```

> [!note] 注意
> 有关如何使用模拟器选择多个项进行拖放操作的信息，参见 [Simulate drag and drop on iOS](https://help.apple.com/simulator/mac/current/index.html?localePath=en.lproj#/devef03b3518)。

在这两种情况下，[UITableViewDragDelegate](uitableviewdragdelegate.md) 方法使用 `ContactCard` 类的实例创建 item provider。此类实现了 [`NSItemProviderWriting`](../foundation/nsitemproviderwriting.md) 协议，使得可以使用联系人卡片对象初始化新的 item provider。

通过符合此协议，联系人卡片对象可以告诉 item provider 它支持的数据类型；示例 App 支持 vCard 和纯文本。联系人卡片还可以加载指定类型的数据，item provider 通过调用联系人卡片的 [`loadData(withTypeIdentifier:forItemProviderCompletionHandler:)`](<../foundation/nsitemproviderwriting/loaddata(withtypeidentifier_foritemprovidercompletionhandler_).md>) 方法来检索。

### 添加放置支持

当用户将联系人信息从另一个 App 拖放到示例 App 中时，系统会调用 [- tableView:performDropWithCoordinator:](<uitableviewdropdelegate/tableview(__performdropwith_).md>) 方法。`ContactsTableViewController` 实现此方法以处理放置操作。该方法的实现使用放置项的 item provider 来调用 [`loadObject(ofClass:completionHandler:)`](<../foundation/nsitemprovider/loadobject(ofclass_completionhandler_)-8ak5d.md>)，它检索一个表示放置的联系人信息的 `ContactCard` 对象。

`loadObject` 方法向 `ContactCard` 类请求联系人卡片对象。该类符合 [`NSItemProviderReading`](../foundation/nsitemproviderreading.md) 协议，实现了 [`object(withItemProviderData:typeIdentifier:)`](<../foundation/nsitemproviderreading/object(withitemproviderdata_typeidentifier_).md>) 类方法，它使用 item provider 数据创建并初始化联系人卡片对象。

当用户在表格视图的特定位置放置联系人时，完成处理程序（来自 `loadObject` 调用）会创建一个占位符，显示放置位置的间隙。接下来，处理程序将放置的联系人插入到联系人列表中放置位置的索引路径处。最后，完成处理程序用显示联系人的视图替换占位符。

```swift
_ = dropItem.dragItem.itemProvider.loadObject(
    ofClass: ContactCard.self,
    completionHandler: { (data, error) in
        if error == nil {
            DispatchQueue.main.async {
                let placeHolder = UITableViewDropPlaceholder(
                    insertionIndexPath: destinationIndexPath!,
                    reuseIdentifier: ClientsDataSource.tableCellIdentifier,
                    rowHeight: UITableView.automaticDimension)

                let placeHolderContext = coordinator.drop(dropItem.dragItem, to: placeHolder)

                placeHolderContext.commitInsertion(dataSourceUpdates: { (insertionIndexPath) in
                    // Update our data source with the newly dropped contact.
                    if let newContact = data as? ContactCard {
                        self.dataSource.clients.insert(newContact, at: insertionIndexPath.item)
                    }
                })
            }
        } else {
            print("""
                There was an error in loading the drop item: ### \(#function),
                \(String(describing: error?.localizedDescription))
                """)
        }
    })
```

当用户将联系人放置在表格视图的空位置时，完成处理程序会将放置的联系人添加到列表末尾，而不显示间隙。

```swift
_ = dropItem.dragItem.itemProvider.loadObject(
    ofClass: ContactCard.self,
    completionHandler: { (data, error) in
        if error == nil {
            if let newContact = data as? ContactCard {
                self.dataSource.clients.append(newContact)
                DispatchQueue.main.async {
                    self.tableView.reloadData()
                }
            }
        } else {
            print("""
                There was an error in loading the drop item: ### \(#function),
                \(String(describing: error?.localizedDescription))
                """)
        }
    })
```

## 另请参阅

### Item providers

- [NSItemProvider](../foundation/nsitemprovider.md) — 用于在拖放或复制粘贴活动期间，或从宿主 App 到 App 扩展之间传递数据或文件的 item provider。
- [NSItemProviderReading](../foundation/nsitemproviderreading.md) — 用于实现一个类，以允许 item provider 创建该类的实例的协议。
- [NSItemProviderWriting](../foundation/nsitemproviderwriting.md) — 用于实现一个类，以允许 item provider 从该类的实例检索数据的协议。
- [UIItemProviderPresentationSizeProviding](uiitemproviderpresentationsizeproviding.md)
- [UIItemProviderReadingAugmentationDesignating](uiitemproviderreadingaugmentationdesignating.md)
- [UIItemProviderReadingAugmentationProviding](uiitemproviderreadingaugmentationproviding.md)

## 下载

- [DataDeliveryWithDragAndDrop.zip](https://docs-assets.developer.apple.com/published/3c5ab9f0f457/DataDeliveryWithDragAndDrop.zip)
