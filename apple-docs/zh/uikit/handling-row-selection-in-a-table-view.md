---
title: 处理表格视图中的行选择
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/handling-row-selection-in-a-table-view
source_url: 'https://developer.apple.com/documentation/uikit/handling-row-selection-in-a-table-view'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/handling-row-selection-in-a-table-view.json'
content_hash: 'sha256:5af59a31bbc72e0d'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [视图与控制](views-and-controls.md) · [表格视图](table-views.md)

# 处理表格视图中的行选择

<sub>文章</sub>

检测用户何时点按表格视图单元格，以便你的 App 能执行下一步指定的操作。

## 概述

当用户点按表格视图的某一行时，通常会随之发生某种操作，例如滑入另一个视图，或者该行以对勾标记表明已选中状态。为了让你的 App 执行相应操作，它必须知道用户何时点按了该行，并做出相应响应。

### 配置行选择行为

使用以下属性来配置表格视图中行选择的行为：

- **[allowsSelection](uitableview/allowsselection.md)** — 决定当表格不处于编辑模式时，用户是否可以选择一行。默认值为 [true](../swift/true.md)。
- **[allowsMultipleSelection](uitableview/allowsmultipleselection.md)** — 决定当表格不处于编辑模式时，用户是否可以选择多于一行。默认值为 [false](../swift/false.md)。
- **[allowsSelectionDuringEditing](uitableview/allowsselectionduringediting.md)** — 决定当表格视图处于编辑模式时，用户是否可以选择一行。默认值为 [false](../swift/false.md)。
- **[allowsMultipleSelectionDuringEditing](uitableview/allowsmultipleselectionduringediting.md)** — 决定在编辑模式下，用户是否可以选择多于一行。默认值为 [false](../swift/false.md)。

### 响应行选择

当用户点按某一行时，表格视图会调用委托方法 [- tableView:didSelectRowAtIndexPath:](<uitableviewdelegate/tableview(__didselectrowat_).md>)。此时，你的 App 执行相应操作，例如显示所选徒步路线的详细信息：

```swift
func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
    let selectedTrail = trails[indexPath.row]
    
    if let viewController = storyboard?.instantiateViewController(identifier: "TrailViewController") as? TrailViewController {
        viewController.trail = selectedTrail
        navigationController?.pushViewController(viewController, animated: true)
    }
}
```

如果你通过将新的视图控制器推入导览堆栈来响应单元格选择，请在该视图控制器从堆栈中弹出时取消选中该单元格。如果你使用 [UITableViewController](uitableviewcontroller.md) 来显示表格视图，将 [clearsSelectionOnViewWillAppear](uitableviewcontroller/clearsselectiononviewwillappear.md) 属性设为 [true](../swift/true.md) 即可获得这一行为。否则，你可以在视图控制器的 [- viewWillAppear:](<uiviewcontroller/viewwillappear(__).md>) 方法中清除选择：

```swift
override func viewWillAppear(_ animated: Bool) {
    super.viewWillAppear(animated)
    if let selectedIndexPath = tableView.indexPathForSelectedRow {
        tableView.deselectRow(at: selectedIndexPath, animated: animated)
    }
}
```

如果该行显示了详情按钮附属视图，且用户点按了它，表格视图会调用 [- tableView:accessoryButtonTappedForRowWithIndexPath:](<uitableviewdelegate/tableview(__accessorybuttontappedforrowwith_).md>) 方法，而不是调用 [- tableView:didSelectRowAtIndexPath:](<uitableviewdelegate/tableview(__didselectrowat_).md>) 方法。要详细了解附属视图，请参阅[为表格配置单元格](configuring-the-cells-for-your-table.md)。

### 以编程方式选择行

行的选择可能源自 App 本身，而不是表格视图中的一次点按。例如，用户可能在通讯录中添加了一个新的联系人，然后返回到联系人列表。返回联系人列表后，App 会滚动列表以显示新添加联系人所在的行。在这种情况下，使用表格视图方法 [- selectRowAtIndexPath:animated:scrollPosition:](<uitableview/selectrow(at_animated_scrollposition_).md>) 来选中并滚动到新行。

> [!note] 注意
> 以编程方式选择一行不会调用委托方法 [- tableView:willSelectRowAtIndexPath:](<uitableviewdelegate/tableview(__willselectrowat_).md>) 或 [- tableView:didSelectRowAtIndexPath:](<uitableviewdelegate/tableview(__didselectrowat_).md>)，也不会向观察者发送 [UITableViewSelectionDidChangeNotification](uitableview/selectiondidchangenotification.md) 通知。

### 管理选择列表

你还可以使用单元格选择来维护包含式和排他式的已选项目列表。包含式列表可以有一个或多个已选项目，而排他式列表最多只能有一个。

在你的 App 中提供选择列表时，不要使用单元格的选中状态来表示项目的状态。而应该显示对勾标记或附属视图。要使用对勾标记表示状态，请实现 [- tableView:didSelectRowAtIndexPath:](<uitableviewdelegate/tableview(__didselectrowat_).md>) 委托方法，然后使用 [- deselectRowAtIndexPath:animated:](<uitableview/deselectrow(at_animated_).md>) 取消选中该单元格，接着将单元格的 [accessoryType](uitableviewcell/accessorytype-swift.property.md) 属性设为 [UITableViewCellAccessoryCheckmark](uitableviewcell/accessorytype-swift.enum/checkmark.md)。

例如，一个面向背包客的 App 可能会让用户创建一份打包清单——一份包含睡袋、帐篷等露营装备的包含式列表。当用户点按某个项目以表示他们已经打包了这件装备时，App 会取消选中该行，更新该项目的数据模型，并在已打包项目所在的行中显示对勾标记。再次点按该项目会将其标记为未打包，并移除对勾标记。示例如下：

```swift
func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
    // Unselect the row, and instead, show the state with a checkmark.
    tableView.deselectRow(at: indexPath, animated: false)
    
    guard let cell = tableView.cellForRow(at: indexPath) else { return }
    
    // Update the selected item to indicate whether the user packed it or not.
    let item = packingList[indexPath.row]
    let newItem = PackingItem(name: item.name, isPacked: !item.isPacked)
    packingList.remove(at: indexPath.row)
    packingList.insert(newItem, at: indexPath.row)
    
    // Show a check mark next to packed items.
    if newItem.isPacked {
        cell.accessoryType = .checkmark
    } else {
        cell.accessoryType = .none
    }
}
```

管理排他式列表的方式与之类似。取消选中该行，并显示对勾标记或附属视图以表示选中状态。但与包含式列表不同，排他式列表任何时候都只能限定一个已选项目。

例如，背包客 App 可能让用户根据单一难度级别——简单、适中和困难——来筛选徒步路线列表。对于这种排他式列表，App 必须移除先前所选项目上的对勾标记，并为当前所选项目显示对勾标记。App 还必须记住当前选中的是哪个项目。例如：

```swift
func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
    // Unselect the row.
    tableView.deselectRow(at: indexPath, animated: false)
    
    // Did the user tap on a selected filter item? If so, do nothing.
    let selectedFilterRow = selectedFilters[indexPath.section]
    if selectedFilterRow == indexPath.row {
        return
    }

    // Remove the checkmark from the previously selected filter item.
    if let previousCell = tableView.cellForRow(at: IndexPath(row: selectedFilterRow, section: indexPath.section)) {
        previousCell.accessoryType = .none
    }
    
    // Mark the newly selected filter item with a checkmark.
    if let cell = tableView.cellForRow(at: indexPath) {
        cell.accessoryType = .checkmark
    }
    
    // Remember this selected filter item.
    selectedFilters[indexPath.section] = indexPath.row
}
```

## 另请参阅

### 选择管理

- [使用双指平移手势选择多个项目](selecting-multiple-items-with-a-two-finger-pan-gesture.md) — 使用表格视图和集合视图上的多选手势，加快用户对多个项目的选择速度。
