---
title: UITableViewDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdelegate.json'
content_hash: 'sha256:cb81cfb5be343554'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md)

# UITableViewDelegate

<sub>协议</sub>

用于管理选择、配置节（section）的页眉和页脚、删除和重新排序单元格（cell）以及在表格视图（table view）中执行其他操作的方法。

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UITableViewDelegate : UIScrollViewDelegate
```

## 概述

使用此协议的方法来管理以下特性：

- 创建和管理自定义的页眉和页脚视图。
- 为行、页眉和页脚指定自定义高度。
- 提供高度估算以支持更好的滚动体验。
- 缩进行内容。
- 响应对行的选择。
- 响应表格行中的轻扫和其他操作。
- 支持编辑表格内容。

表格视图使用 [IndexPath](../foundation/indexpath.md) 来指定行和节。有关如何解读行索引和节索引的信息，请参阅[指定行和节的位置](uitableviewdatasource.md#Specify-the-location-of-rows-and-sections)。

## 关系

- **继承自**：[NSObjectProtocol](../objectivec/nsobjectprotocol.md)、[UIScrollViewDelegate](uiscrollviewdelegate.md)

- **遵循类型**：[UITableViewController](uitableviewcontroller.md)

## 主题

### 为表格视图配置行

- [- tableView:willDisplayCell:forRowAtIndexPath:](<uitableviewdelegate/tableview(__willdisplay_forrowat_).md>) — 告知委托（delegate），表格视图即将为特定行绘制单元格。
- [- tableView:indentationLevelForRowAtIndexPath:](<uitableviewdelegate/tableview(__indentationlevelforrowat_).md>) — 要求委托返回给定节中某一行的缩进层级。
- [- tableView:shouldSpringLoadRowAtIndexPath:withContext:](<uitableviewdelegate/tableview(__shouldspringloadrowat_with_).md>) — 用于让你微调表格中行的弹簧加载（spring-loading）行为。

### 响应行选择

- [处理表格视图中的行选择](handling-row-selection-in-a-table-view.md) — 检测用户何时轻点表格视图的单元格，以便你的 App 可以执行下一步的指示操作。
- [使用双指平移手势选择多个项目](selecting-multiple-items-with-a-two-finger-pan-gesture.md) — 通过在表格视图和集合视图（collection view）上使用多选手势，加速用户对多个项目的选择。
- [- tableView:willSelectRowAtIndexPath:](<uitableviewdelegate/tableview(__willselectrowat_).md>) — 告知委托即将选择某一行。
- [- tableView:didSelectRowAtIndexPath:](<uitableviewdelegate/tableview(__didselectrowat_).md>) — 告知委托某一行已被选中。
- [- tableView:willDeselectRowAtIndexPath:](<uitableviewdelegate/tableview(__willdeselectrowat_).md>) — 告知委托指定的行即将被取消选中。
- [- tableView:didDeselectRowAtIndexPath:](<uitableviewdelegate/tableview(__diddeselectrowat_).md>) — 告知委托指定的行现在已被取消选中。
- [- tableView:shouldBeginMultipleSelectionInteractionAtIndexPath:](<uitableviewdelegate/tableview(__shouldbeginmultipleselectioninteractionat_).md>) — 询问委托用户是否可以使用双指平移手势在表格视图中选择多个项目。
- [- tableView:didBeginMultipleSelectionInteractionAtIndexPath:](<uitableviewdelegate/tableview(__didbeginmultipleselectioninteractionat_).md>) — 告知委托用户何时开始在表格视图中使用双指平移手势选择多行。
- [- tableViewDidEndMultipleSelectionInteraction:](<uitableviewdelegate/tableviewdidendmultipleselectioninteraction(__).md>) — 告知委托用户何时停止在表格视图中使用双指平移手势选择多行。

### 提供自定义页眉和页脚视图

- [- tableView:viewForHeaderInSection:](<uitableviewdelegate/tableview(__viewforheaderinsection_).md>) — 要求委托提供一个视图，用于显示在表格视图指定节的页眉中。
- [- tableView:viewForFooterInSection:](<uitableviewdelegate/tableview(__viewforfooterinsection_).md>) — 要求委托提供一个视图，用于显示在表格视图指定节的页脚中。
- [- tableView:willDisplayHeaderView:forSection:](<uitableviewdelegate/tableview(__willdisplayheaderview_forsection_).md>) — 告知委托表格即将显示指定节的页眉视图。
- [- tableView:willDisplayFooterView:forSection:](<uitableviewdelegate/tableview(__willdisplayfooterview_forsection_).md>) — 告知委托表格即将显示指定节的页脚视图。

### 提供页眉、页脚和行高

- [- tableView:heightForRowAtIndexPath:](<uitableviewdelegate/tableview(__heightforrowat_).md>) — 要求委托返回指定位置的行应使用的高度。
- [- tableView:heightForHeaderInSection:](<uitableviewdelegate/tableview(__heightforheaderinsection_).md>) — 要求委托返回特定节页眉应使用的高度。
- [- tableView:heightForFooterInSection:](<uitableviewdelegate/tableview(__heightforfooterinsection_).md>) — 要求委托返回特定节页脚应使用的高度。
- [UITableViewAutomaticDimension](uitableview/automaticdimension.md) — 代表给定维度默认值的常量。

### 估算表格内容的高度

- [- tableView:estimatedHeightForRowAtIndexPath:](<uitableviewdelegate/tableview(__estimatedheightforrowat_).md>) — 要求委托返回指定位置行的估算高度。
- [- tableView:estimatedHeightForHeaderInSection:](<uitableviewdelegate/tableview(__estimatedheightforheaderinsection_).md>) — 要求委托返回特定节页眉的估算高度。
- [- tableView:estimatedHeightForFooterInSection:](<uitableviewdelegate/tableview(__estimatedheightforfooterinsection_).md>) — 要求委托返回特定节页脚的估算高度。

### 管理辅助视图

- [- tableView:accessoryButtonTappedForRowWithIndexPath:](<uitableviewdelegate/tableview(__accessorybuttontappedforrowwith_).md>) — 告知委托用户轻点了指定行的详细信息按钮。

### 管理上下文菜单

- [在 App 中添加上下文菜单（context menu）](adding-context-menus-in-your-app.md) — 通过在 iOS App 中添加上下文菜单，提供对有用操作的快速访问。
- [- tableView:contextMenuConfigurationForRowAtIndexPath:point:](<uitableviewdelegate/tableview(__contextmenuconfigurationforrowat_point_).md>) — 返回指定点所在行的上下文菜单配置。
- [- tableView:previewForDismissingContextMenuWithConfiguration:](<uitableviewdelegate/tableview(__previewfordismissingcontextmenuwithconfiguration_).md>) — 返回在关闭上下文菜单时的目标视图。
- [- tableView:previewForHighlightingContextMenuWithConfiguration:](<uitableviewdelegate/tableview(__previewforhighlightingcontextmenuwithconfiguration_).md>) — 返回一个视图，用于覆盖表格视图创建的默认预览（preview）。
- [- tableView:willDisplayContextMenuWithConfiguration:animator:](<uitableviewdelegate/tableview(__willdisplaycontextmenu_animator_).md>) — 通知委托上下文菜单即将出现。
- [- tableView:willEndContextMenuInteractionWithConfiguration:animator:](<uitableviewdelegate/tableview(__willendcontextmenuinteraction_animator_).md>) — 通知委托上下文菜单即将消失。
- [- tableView:willPerformPreviewActionForMenuWithConfiguration:animator:](<uitableviewdelegate/tableview(__willperformpreviewactionformenuwith_animator_).md>) — 通知委托用户已通过轻点预览触发提交操作。

### 响应行操作

- [- tableView:leadingSwipeActionsConfigurationForRowAtIndexPath:](<uitableviewdelegate/tableview(__leadingswipeactionsconfigurationforrowat_).md>) — 返回显示在行前缘的轻扫操作。
- [- tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:](<uitableviewdelegate/tableview(__trailingswipeactionsconfigurationforrowat_).md>) — 返回显示在行后缘的轻扫操作。
- [- tableView:shouldShowMenuForRowAtIndexPath:](<uitableviewdelegate/tableview(__shouldshowmenuforrowat_).md>) — 询问委托是否应该为某一行显示编辑菜单。 _(已废弃)_
- [- tableView:canPerformAction:forRowAtIndexPath:withSender:](<uitableviewdelegate/tableview(__canperformaction_forrowat_withsender_).md>) — 询问委托是否应该为给定行省略编辑菜单中的“拷贝”或“粘贴”命令。 _(已废弃)_
- [- tableView:performAction:forRowAtIndexPath:withSender:](<uitableviewdelegate/tableview(__performaction_forrowat_withsender_).md>) — 告知委托对给定行的内容执行拷贝或粘贴操作。 _(已废弃)_
- [- tableView:editActionsForRowAtIndexPath:](<uitableviewdelegate/tableview(__editactionsforrowat_).md>) — 询问委托应显示哪些操作来响应对指定行的轻扫。 _(已废弃)_

### 管理表格视图高亮

- [- tableView:shouldHighlightRowAtIndexPath:](<uitableviewdelegate/tableview(__shouldhighlightrowat_).md>) — 询问委托是否应该高亮指定的行。
- [- tableView:didHighlightRowAtIndexPath:](<uitableviewdelegate/tableview(__didhighlightrowat_).md>) — 告知委托指定的行已被高亮。
- [- tableView:didUnhighlightRowAtIndexPath:](<uitableviewdelegate/tableview(__didunhighlightrowat_).md>) — 告知委托指定索引路径的行已移除高亮。

### 编辑表格行

- [- tableView:willBeginEditingRowAtIndexPath:](<uitableviewdelegate/tableview(__willbegineditingrowat_).md>) — 告知委托表格视图即将进入编辑模式。
- [- tableView:didEndEditingRowAtIndexPath:](<uitableviewdelegate/tableview(__didendeditingrowat_).md>) — 告知委托表格视图已退出编辑模式。
- [- tableView:editingStyleForRowAtIndexPath:](<uitableviewdelegate/tableview(__editingstyleforrowat_).md>) — 要求委托返回表格视图中特定位置行的编辑样式。
- [- tableView:titleForDeleteConfirmationButtonForRowAtIndexPath:](<uitableviewdelegate/tableview(__titlefordeleteconfirmationbuttonforrowat_).md>) — 更改删除确认按钮的默认标题。
- [- tableView:shouldIndentWhileEditingRowAtIndexPath:](<uitableviewdelegate/tableview(__shouldindentwhileeditingrowat_).md>) — 询问委托当表格视图处于编辑模式时，指定行的背景是否应该缩进。

### 重新排序表格行

- [- tableView:targetIndexPathForMoveFromRowAtIndexPath:toProposedIndexPath:](<uitableviewdelegate/tableview(__targetindexpathformovefromrowat_toproposedindexpath_).md>) — 要求委托返回一个新的索引路径，以重新定位建议移动的行。

### 跟踪视图的移除

- [- tableView:didEndDisplayingCell:forRowAtIndexPath:](<uitableviewdelegate/tableview(__didenddisplaying_forrowat_).md>) — 告知委托指定的单元格已从表格中移除。
- [- tableView:didEndDisplayingHeaderView:forSection:](<uitableviewdelegate/tableview(__didenddisplayingheaderview_forsection_).md>) — 告知委托指定的页眉视图已从表格中移除。
- [- tableView:didEndDisplayingFooterView:forSection:](<uitableviewdelegate/tableview(__didenddisplayingfooterview_forsection_).md>) — 告知委托指定的页脚视图已从表格中移除。

### 管理表格视图聚焦

- [- tableView:canFocusRowAtIndexPath:](<uitableviewdelegate/tableview(__canfocusrowat_).md>) — 询问委托指定索引路径处的单元格本身是否可获得焦点（focus）。
- [- tableView:shouldUpdateFocusInContext:](<uitableviewdelegate/tableview(__shouldupdatefocusin_).md>) — 询问委托是否允许发生上下文指定的聚焦更新。
- [- tableView:didUpdateFocusInContext:withAnimationCoordinator:](<uitableviewdelegate/tableview(__didupdatefocusin_with_).md>) — 告知委托上下文指定的聚焦更新刚刚发生。
- [- indexPathForPreferredFocusedViewInTableView:](<uitableviewdelegate/indexpathforpreferredfocusedview(in_).md>) — 要求委托返回表格视图的首选聚焦视图的索引路径。
- [- tableView:selectionFollowsFocusForRowAtIndexPath:](<uitableviewdelegate/tableview(__selectionfollowsfocusforrowat_).md>) — 询问委托是否应将对应索引路径行的选择行为和聚焦行为关联起来。

### 执行主要操作

- [- tableView:canPerformPrimaryActionForRowAtIndexPath:](<uitableviewdelegate/tableview(__canperformprimaryactionforrowat_).md>) — 询问委托是否要对指定索引路径的行执行主要操作（primary action）。
- [- tableView:performPrimaryActionForRowAtIndexPath:](<uitableviewdelegate/tableview(__performprimaryactionforrowat_).md>) — 告知委托对指定索引路径的行执行主要操作。

## 另请参阅

### 表格管理

- [估算表格滚动区域的高度](estimating-the-height-of-a-table-s-scrolling-area.md) — 为表格视图的页眉、页脚和行提供高度估算，以确保滚动能准确反映内容的大小。
- [UITableViewController](uitableviewcontroller.md) — 专门管理表格视图的视图控制器（view controller）。
- [UITableViewFocusUpdateContext](uitableviewfocusupdatecontext.md) — 一个上下文对象，提供与从一个视图到另一个视图的特定聚焦更新相关的信息。
