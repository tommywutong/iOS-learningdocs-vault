---
title: 在你的 App 中添加上下文菜单
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, Xcode 12.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/adding-context-menus-in-your-app
source_url: 'https://developer.apple.com/documentation/uikit/adding-context-menus-in-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/adding-context-menus-in-your-app.json'
content_hash: 'sha256:963dfd4d20603b1f'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [菜单和快捷键](menus-and-shortcuts.md) · [UIContextMenuInteraction](uicontextmenuinteraction.md)

# 在你的 App 中添加上下文菜单

<sub>示例代码</sub>

通过在你的 iOS App 中添加上下文菜单（context menu），提供对常用操作的快速访问。

## 概述

本示例项目演示如何向视图、控制（control）、表格视图、集合视图和网页视图等用户界面元素添加上下文菜单。App 通过操作、嵌套的子菜单操作和自定义预览来增强和扩展上下文菜单。有关上下文菜单设计的更多信息，参见[《人机界面指南》](https://developer.apple.com/design/human-interface-guidelines/ios/controls/context-menus/)。

### 创建上下文菜单

本示例展示创建上下文菜单的两种方式：

1. 对于 [UIView](uiview.md)，本示例创建一个 [UIContextMenuInteraction](uicontextmenuinteraction.md) 对象并把它附加到该视图上。`UIContextMenuInteraction` 对象把用户的注意力集中到 UI 的特定部分，并提供供用户对该内容执行的操作。随后，App 采用 [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md) 协议，并提供一个 [UIContextMenuConfiguration](uicontextmenuconfiguration.md) 对象。
2. 对于表格、集合和网页视图这类更具体的 UI 元素，App 会为这些元素采用各自特定的协议，由这些协议返回一个 `UIContextMenuConfiguration`。

采用 `UIContextMenuInteractionDelegate` 来管理上下文菜单的生命周期。App 实现 [- contextMenuInteraction:configurationForMenuAtLocation:](<uicontextmenuinteractiondelegate/contextmenuinteraction(__configurationformenuatlocation_).md>) 来返回一个 `UIContextMenuConfiguration` 对象。这个配置对象由一个可选的 `identifier`、一个返回 [UIViewController](uiviewcontroller.md) 的 `previewProvider`，以及一个返回带有若干 [UIAction](uiaction.md) 条目的 [UIMenu](uimenu.md) 的 `actionProvider` 组成。

内容丰富的上下文菜单还会提供一个 [UITargetedPreview](uitargetedpreview.md)，它是一个描述源视图的对象，在打开上下文菜单并为其添加动画时使用。`UITargetedPreview` 指定在动画过渡期间使用的视图。

### 向视图添加上下文菜单

本示例通过调用 [- addInteraction:](<uiview/addinteraction(__).md>) 向一个 `UIView` 添加上下文菜单。

```swift
let interaction = UIContextMenuInteraction(delegate: self)
imageView.addInteraction(interaction)
```

当用户在该视图上长按时，视图会通过调用 `contextMenuInteraction(_:configurationForMenuAtLocation:)` 请求它的委托提供上下文菜单。

```swift
func contextMenuInteraction(_ interaction: UIContextMenuInteraction,
                            configurationForMenuAtLocation location: CGPoint) -> UIContextMenuConfiguration? {
    return UIContextMenuConfiguration(identifier: nil,
                                      previewProvider: nil,
                                      actionProvider: {
            suggestedActions in
        let inspectAction =
            UIAction(title: NSLocalizedString("InspectTitle", comment: ""),
                     image: UIImage(systemName: "arrow.up.square")) { action in
                self.performInspect()
            }
            
        let duplicateAction =
            UIAction(title: NSLocalizedString("DuplicateTitle", comment: ""),
                     image: UIImage(systemName: "plus.square.on.square")) { action in
                self.performDuplicate()
            }
            
        let deleteAction =
            UIAction(title: NSLocalizedString("DeleteTitle", comment: ""),
                     image: UIImage(systemName: "trash"),
                     attributes: .destructive) { action in
                self.performDelete()
            }
                                        
        return UIMenu(title: "", children: [inspectAction, duplicateAction, deleteAction])
    })
}
```

### 向表格视图添加上下文菜单

当用户长按某个 [UITableViewCell](uitableviewcell.md) 时，本示例向 [UITableView](uitableview.md) 添加上下文菜单。`UITableView` 会通过调用 [- tableView:contextMenuConfigurationForRowAtIndexPath:point:](<uitableviewdelegate/tableview(__contextmenuconfigurationforrowat_point_).md>) 请求它的委托提供上下文菜单。

```swift
override func tableView(_ tableView: UITableView,
                        contextMenuConfigurationForRowAt indexPath: IndexPath,
                        point: CGPoint) -> UIContextMenuConfiguration? {
    return UIContextMenuConfiguration(identifier: nil,
                                      previewProvider: nil,
                                      actionProvider: {
            suggestedActions in
        let inspectAction =
            UIAction(title: NSLocalizedString("InspectTitle", comment: ""),
                     image: UIImage(systemName: "arrow.up.square")) { action in
                self.performInspect(indexPath)
            }
        let duplicateAction =
            UIAction(title: NSLocalizedString("DuplicateTitle", comment: ""),
                     image: UIImage(systemName: "plus.square.on.square")) { action in
                self.performDuplicate(indexPath)
            }
        let deleteAction =
            UIAction(title: NSLocalizedString("DeleteTitle", comment: ""),
                     image: UIImage(systemName: "trash"),
                     attributes: .destructive) { action in
                self.performDelete(indexPath)
            }
        return UIMenu(title: "", children: [inspectAction, duplicateAction, deleteAction])
    })
}
```

### 向集合视图添加上下文菜单

当用户长按某个 [UICollectionViewCell](uicollectionviewcell.md) 时，本示例向 [UICollectionView](uicollectionview.md) 添加上下文菜单。`UICollectionView` 会通过调用 [- collectionView:contextMenuConfigurationForItemAtIndexPath:point:](<uicollectionviewdelegate/collectionview(__contextmenuconfigurationforitemat_point_).md>) 请求它的委托提供上下文菜单。

```swift
override func collectionView(_ collectionView: UICollectionView,
                             contextMenuConfigurationForItemAt indexPath: IndexPath,
                             point: CGPoint) -> UIContextMenuConfiguration? {
    return UIContextMenuConfiguration(identifier: nil, previewProvider: nil) { suggestedActions in
        let inspectAction = self.inspectAction(indexPath)
        let duplicateAction = self.duplicateAction(indexPath)
        let deleteAction = self.deleteAction(indexPath)
        return UIMenu(title: "", children: [inspectAction, duplicateAction, deleteAction])
    }
}
```

### 向控制添加上下文菜单

本示例向一个 [UIControl](uicontrol.md) 添加上下文菜单。UIKit 以两种不同的方式把上下文菜单附加到 `UIControl` 上：

- 通过用一个 `UIMenu` 对象设置 `menu` 属性

```swift
let inspectAction = self.inspectAction()
let duplicateAction = self.duplicateAction()
let deleteAction = self.deleteAction()
buttonMenuAsPrimary.menu = UIMenu(title: "", children: [inspectAction, duplicateAction, deleteAction])
buttonMenuAsPrimary.showsMenuAsPrimaryAction = true
```

- 通过添加一个 `UIContextMenuInteraction` 对象

```swift
let interaction = UIContextMenuInteraction(delegate: self)
buttonMenu.addInteraction(interaction)
```

当用户在该控制上长按时，App 会通过调用 [- contextMenuInteraction:configurationForMenuAtLocation:](<uicontextmenuinteractiondelegate/contextmenuinteraction(__configurationformenuatlocation_).md>) 请求它的委托提供上下文菜单

```swift
func contextMenuInteraction(_ interaction: UIContextMenuInteraction,
                            configurationForMenuAtLocation location: CGPoint) -> UIContextMenuConfiguration? {
    return UIContextMenuConfiguration(identifier: nil,
                                      previewProvider: nil,
                                      actionProvider: {
            suggestedActions in
        // 使用 ContextMenu 协议来生成这些 UIAction。
        let inspectAction = self.inspectAction()
        let duplicateAction = self.duplicateAction()
        let deleteAction = self.deleteAction()
        return UIMenu(title: "", children: [inspectAction, duplicateAction, deleteAction])
    })
}
```

### 向网页视图添加上下文菜单

从示例的 Web Views 大纲项中选择 Basic 测试用例。当用户长按 [`WKWebView`](../webkit/wkwebview.md) 中的链接时，App 会呈现一个 [`SFSafariViewController`](../safariservices/sfsafariviewcontroller.md)，用一组默认的 `UIAction` 条目来显示该链接的内容。当用户轻点这个视图控制器时，用户就会离开该 App 并进入 Safari。

从示例的 Web Views 大纲项中选择 Preview Provider 测试用例。当用户长按 `WKWebView` 中的链接时，App 会呈现一个自定义视图控制器。

本示例通过采用 [`WKUIDelegate`](../webkit/wkuidelegate.md) 协议来拦截该上下文菜单并向其中添加内容。`WKWebView` 会通过调用 [`webView(_:contextMenuConfigurationForElement:completionHandler:)`](<../webkit/wkuidelegate/webview(__contextmenuconfigurationforelement_completionhandler_).md>) 请求它的委托提供上下文菜单。

```swift
func webView(_ webView: WKWebView,
             contextMenuConfigurationForElement elementInfo: WKContextMenuElementInfo,
             completionHandler: @escaping (UIContextMenuConfiguration?) -> Void) {
    let configuration =
        UIContextMenuConfiguration(identifier: nil,
                                   previewProvider: { return SFSafariViewController(url: elementInfo.linkURL!) },
                                   actionProvider: { elements in
            guard elements.isEmpty == false else { return nil }
                                    
            // 把我们的自定义操作添加到传入的既有操作中。
            var elementsToUse = elements
            let inspectAction = self.extraAction(elementInfo.linkURL!)
            let editMenu = UIMenu(title: "", options: .displayInline, children: [inspectAction])
            elementsToUse.append(editMenu)
                   
            let contextMenuTitle = elementInfo.linkURL?.lastPathComponent
            return UIMenu(title: contextMenuTitle!, image: nil, identifier: nil, options: [], children: elementsToUse)
        }
    )
    completionHandler(configuration)
}
```

## 另请参阅

### 创建上下文菜单交互对象

- [- initWithDelegate:](<uicontextmenuinteraction/init(delegate_).md>) — 用指定的委托对象创建一个上下文菜单交互对象。
- [向菜单栏和用户界面添加菜单和快捷键](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md) — 向使用 Mac Catalyst 构建的 Mac App 添加菜单和键盘快捷键，以便快速访问实用操作。

## 下载

- [AddingContextMenusInYourApp.zip](https://docs-assets.developer.apple.com/published/e845680c042f/AddingContextMenusInYourApp.zip)
