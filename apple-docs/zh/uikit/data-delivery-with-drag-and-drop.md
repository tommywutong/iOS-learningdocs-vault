---
title: 用拖放传递数据
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

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [拖放](drag-and-drop.md)

# 用拖放传递数据

<sub>示例代码</sub>

使用条目提供程序（item provider），在拖放操作期间于 iPad App 之间共享数据。

## 概述

借助拖放，用户可以把数据从一个 iPad App 拷贝到另一个。数据通过一个 [`NSItemProvider`](../foundation/nsitemprovider.md) 对象在 App 之间共享。本示例代码项目展示了如何使用条目提供程序来：

- 共享一个联系人：用户把它从示例 iPad App 拖出并放进另一个 App。
- 取回联系人信息：用户把它从另一个 App 拖出并放进示例 App。

示例 iPad App 使用表格视图显示联系人列表。用户可以拖动一个或多个联系人，并放进通讯录（Contacts）或备忘录（Notes）等其他 App。同样，用户也可以用通讯录或备忘录之类的 App，把新的联系人拖放进示例 App。

### 添加拖动支持

示例 App 的表格视图显示联系人列表。当用户开始拖动一个联系人时，系统会调用 [- tableView:itemsForBeginningDragSession:atIndexPath:](<uitableviewdragdelegate/tableview(__itemsforbeginning_at_).md>) 方法。该方法的实现使用 `at` 参数确定联系人在列表中的位置，从列表中取出该联系人。然后该方法用联系人对象创建一个条目提供程序，并把条目提供程序包装进一个 [UIDragItem](uidragitem.md) 对象。方法把拖动条目放进一个数组并返回给系统。最后，系统把拖动条目加入当前的拖动会话（drag session）。

```swift
func tableView(_ tableView: UITableView,
               itemsForBeginning session: UIDragSession,
               at indexPath: IndexPath) -> [UIDragItem] {
    let contactCard = dataSource.clients[indexPath.row]
    let dragItem = UIDragItem(itemProvider: NSItemProvider(object: contactCard))
    return [dragItem]
}
```

用户可以选中多个联系人一起拖到另一个 App。用户每次选中一个联系人，系统就会调用 [- tableView:itemsForAddingToDragSession:atIndexPath:point:](<uitableviewdragdelegate/tableview(__itemsforaddingto_at_point_).md>) 方法。与开始拖动会话类似，该方法为选中的联系人创建条目提供程序，创建一个包含该条目提供程序的拖动条目，并返回包含该拖动条目的数组，让系统把拖动条目加入拖动会话。

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
> 关于如何在 Simulator 中为拖放操作选择多个条目，参见 [Simulate drag and drop on iOS](https://help.apple.com/simulator/mac/current/index.html?localePath=en.lproj#/devef03b3518)。

两种情况下，[UITableViewDragDelegate](uitableviewdragdelegate.md) 方法都使用 `ContactCard` 类的实例创建条目提供程序。该类实现了 [`NSItemProviderWriting`](../foundation/nsitemproviderwriting.md) 协议，因此可以用联系人卡片对象初始化新的条目提供程序。

通过遵循该协议，联系人卡片对象可以告诉条目提供程序它支持哪些数据类型；示例 App 支持 vCard 和纯文本。联系人卡片还能加载指定类型的数据，条目提供程序通过调用联系人卡片的 [`loadData(withTypeIdentifier:forItemProviderCompletionHandler:)`](<../foundation/nsitemproviderwriting/loaddata(withtypeidentifier_foritemprovidercompletionhandler_).md>) 方法来取得数据。

### 添加放下支持

当用户把另一个 App 中的联系人信息放进示例 App 时，系统会调用 [- tableView:performDropWithCoordinator:](<uitableviewdropdelegate/tableview(__performdropwith_).md>) 方法。`ContactsTableViewController` 实现了这个方法来处理放下操作。该方法的实现使用放下条目的条目提供程序调用 [`loadObject(ofClass:completionHandler:)`](<../foundation/nsitemprovider/loadobject(ofclass_completionhandler_)-8ak5d.md>)，取回一个表示被放下联系人信息的 `ContactCard` 对象。

`loadObject` 方法向 `ContactCard` 类索要联系人卡片对象。该类遵循 [`NSItemProviderReading`](../foundation/nsitemproviderreading.md) 协议，实现了 [`object(withItemProviderData:typeIdentifier:)`](<../foundation/nsitemproviderreading/object(withitemproviderdata_typeidentifier_).md>) 类方法，用条目提供程序的数据创建并初始化联系人卡片对象。

当用户把联系人放到表格视图的某个特定位置时，完成处理程序（来自 `loadObject` 调用）会创建一个占位符，在放下位置显示一个空隙。接着，完成处理程序把放下的联系人插入列表中放下位置对应的索引路径处。最后，完成处理程序用一个显示该联系人的视图替换占位符。

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

当用户把联系人放到表格视图的空白位置时，完成处理程序把放下的联系人追加到列表末尾，不显示空隙。

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

### 条目提供程序

- [NSItemProvider](../foundation/nsitemprovider.md) — 在拖放或拷贝粘贴活动期间于进程之间传递数据或文件，或从宿主 App 向 App 扩展传递数据或文件的条目提供程序。
- [NSItemProviderReading](../foundation/nsitemproviderreading.md) — 实现某个类以允许条目提供程序创建该类实例的协议。
- [NSItemProviderWriting](../foundation/nsitemproviderwriting.md) — 实现某个类以允许条目提供程序从该类实例取回数据的协议。
- [UIItemProviderPresentationSizeProviding](uiitemproviderpresentationsizeproviding.md)
- [UIItemProviderReadingAugmentationDesignating](uiitemproviderreadingaugmentationdesignating.md)
- [UIItemProviderReadingAugmentationProviding](uiitemproviderreadingaugmentationproviding.md)

## 下载

- [DataDeliveryWithDragAndDrop.zip](https://docs-assets.developer.apple.com/published/3c5ab9f0f457/DataDeliveryWithDragAndDrop.zip)
