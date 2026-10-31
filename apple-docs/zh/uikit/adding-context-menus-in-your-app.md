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

> 导航： [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Menus and shortcuts](menus-and-shortcuts.md) · [UIContextMenuInteraction](uicontextmenuinteraction.md)

# 在你的 App 中添加上下文菜单

<sub>示例代码</sub>

通过为 iOS App 中的用户界面元素添加上下文菜单，提供对有用操作的快速访问。

## 概述

此示例项目演示如何为用户界面元素（如视图、控件、表格视图、集合视图和网页视图）添加上下文菜单。App 通过操作、嵌套的子菜单操作和自定义预览来增强和扩展上下文菜单。有关上下文菜单设计的更多信息，参见 [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/ios/controls/context-menus/)。

### 创建上下文菜单

此示例展示两种创建上下文菜单的方式：

1. 对于 [UIView](uiview.md)，示例会创建一个 [UIContextMenuInteraction](uicontextmenuinteraction.md) 对象并将其附加到该视图。`UIContextMenuInteraction` 对象将用户的注意力聚焦于 UI 的特定部分，并提供用户可在该内容上执行的操作。然后 App 采用 [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md) 协议并提供一个 [UIContextMenuConfiguration](uicontextmenuconfiguration.md) 对象。
2. 对于更具体的 UI 元素（如表格、集合和网页视图），App 采用针对这些元素的特定协议，这些协议返回一个 `UIContextMenuConfiguration`。

采用 `UIContextMenuInteractionDelegate` 来管理上下文菜单的生命周期。App 实现 [- contextMenuInteraction:configurationForMenuAtLocation:](<uicontextmenuinteractiondelegate/contextmenuinteraction(__configurationformenuatlocation_).md>) 以返回一个 `UIContextMenuConfiguration` 对象。此配置对象由一个可选的 `identifier`、一个返回 [UIViewController](uiviewcontroller.md) 的 `previewProvider`，以及一个返回包含一组 [UIAction](uiaction.md) 项的 [UIMenu](uimenu.md) 的 `actionProvider` 组成。

具有丰富内容的上下文菜单还提供 [UITargetedPreview](uitargetedpreview.md)，这是一个在打开和动画化上下文菜单时描述源视图的对象。`UITargetedPreview` 指定在动画过渡期间使用的视图。

### 为视图添加上下文菜单

此示例通过调用 [- addInteraction:](<uiview/addinteraction(__).md>) 为 `UIView` 添加上下文菜单。

```swift
let interaction = UIContextMenuInteraction(delegate: self)
imageView.addInteraction(interaction)
```

当用户触摸并按住该视图时，视图会请求其 delegate 提供上下文菜单，调用 `contextMenuInteraction(_:configurationForMenuAtLocation:)`。

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

### 为表格视图添加上下文菜单

此示例在用户触摸并按住 [UITableViewCell](uitableviewcell.md) 时，为 [UITableView](uitableview.md) 添加上下文菜单。`UITableView` 会请求其 delegate 提供上下文菜单，调用 [- tableView:contextMenuConfigurationForRowAtIndexPath:point:](<uitableviewdelegate/tableview(__contextmenuconfigurationforrowat_point_).md>)。

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

### 为集合视图添加上下文菜单

此示例在用户触摸并按住 [UICollectionViewCell](uicollectionviewcell.md) 时，为 [UICollectionView](uicollectionview.md) 添加上下文菜单。`UICollectionView` 会请求其 delegate 提供上下文菜单，调用 [- collectionView:contextMenuConfigurationForItemAtIndexPath:point:](<uicollectionviewdelegate/collectionview(__contextmenuconfigurationforitemat_point_).md>)。

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

### 为控件添加上下文菜单

此示例为 [UIControl](uicontrol.md) 添加上下文菜单。UIKit 以两种不同的方式将上下文菜单附加到 `UIControl`：

- 通过将 `UIMenu` 对象设置为 `menu` 属性

```swift
let inspectAction = self.inspectAction()
let duplicateAction = self.duplicateAction()
let deleteAction = self.deleteAction()
buttonMenuAsPrimary.menu = UIMenu(title: "", children: [inspectAction, duplicateAction, deleteAction])
buttonMenuAsPrimary.showsMenuAsPrimaryAction = true
```

- 通过添加 `UIContextMenuInteraction` 对象

```swift
let interaction = UIContextMenuInteraction(delegate: self)
buttonMenu.addInteraction(interaction)
```

当用户触摸并按住该控件时，App 会请求其 delegate 提供上下文菜单，调用 [- contextMenuInteraction:configurationForMenuAtLocation:](<uicontextmenuinteractiondelegate/contextmenuinteraction(__configurationformenuatlocation_).md>)

```swift
func contextMenuInteraction(_ interaction: UIContextMenuInteraction,
                            configurationForMenuAtLocation location: CGPoint) -> UIContextMenuConfiguration? {
    return UIContextMenuConfiguration(identifier: nil,
                                      previewProvider: nil,
                                      actionProvider: {
            suggestedActions in
        // Use the ContextMenu protocol to produce the UIActions.
        let inspectAction = self.inspectAction()
        let duplicateAction = self.duplicateAction()
        let deleteAction = self.deleteAction()
        return UIMenu(title: "", children: [inspectAction, duplicateAction, deleteAction])
    })
}
```

### 为网页视图添加上下文菜单

从示例的 Web Views 大纲项中选择 Basic 测试用例。当用户触摸并按住 [`WKWebView`](../webkit/wkwebview.md) 中的链接时，App 会呈现 [`SFSafariViewController`](../safariservices/sfsafariviewcontroller.md) 来显示该链接内容，并附带一组默认的 `UIAction` 项。当用户触摸该视图控制器时，用户会离开 App 并进入 Safari。

从示例的 Web Views 大纲项中选择 Preview Provider 测试用例。当用户触摸并按住 `WKWebView` 中的链接时，App 会呈现一个自定义视图控制器。

此示例通过采用 [`WKUIDelegate`](../webkit/wkuidelegate.md) 协议来拦截并添加到该上下文菜单。`WKWebView` 会请求其 delegate 提供上下文菜单，调用 [`webView(_:contextMenuConfigurationForElement:completionHandler:)`](<../webkit/wkuidelegate/webview(__contextmenuconfigurationforelement_completionhandler_).md>)。

```swift
func webView(_ webView: WKWebView,
             contextMenuConfigurationForElement elementInfo: WKContextMenuElementInfo,
             completionHandler: @escaping (UIContextMenuConfiguration?) -> Void) {
    let configuration =
        UIContextMenuConfiguration(identifier: nil,
                                   previewProvider: { return SFSafariViewController(url: elementInfo.linkURL!) },
                                   actionProvider: { elements in
            guard elements.isEmpty == false else { return nil }
                                    
            // Add our custom action to the existing actions passed in.
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

- [- initWithDelegate:](<uicontextmenuinteraction/init(delegate_).md>) — 使用指定的 delegate 对象创建上下文菜单交互对象。
- [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md) — 通过为使用 Mac Catalyst 构建的 Mac App 的菜单栏和用户界面添加菜单和键盘快捷键，提供对有用操作的快速访问。

## 下载

- [AddingContextMenusInYourApp.zip](https://docs-assets.developer.apple.com/published/e845680c042f/AddingContextMenusInYourApp.zip)
