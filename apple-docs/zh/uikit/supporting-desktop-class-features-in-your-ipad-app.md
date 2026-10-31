---
title: 为你的 iPad App 支持桌面级功能
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, Xcode 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/supporting-desktop-class-features-in-your-ipad-app
source_url: 'https://developer.apple.com/documentation/uikit/supporting-desktop-class-features-in-your-ipad-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/supporting-desktop-class-features-in-your-ipad-app.json'
content_hash: 'sha256:aa704d51aa1ea1ce'
translated: true
---

> 导航： [Technologies](../technologies.md) · [UIKit](../uikit.md) · [App and environment](app-and-environment.md)

# 为你的 iPad App 支持桌面级功能

<sub>示例代码</sub>

通过添加桌面级功能和文稿支持，增强你的 iPad App。

## 概述

此示例项目展示了如何构建一个充分利用 iPad 桌面级功能（如硬件键盘和触控板支持、Stage Manager 以及丰富的文稿编辑能力）的 App。该 App 是一个标记文稿编辑器，允许创建、编辑、预览和保存文稿，包括带有自定义操作的标题菜单、文稿重命名、查找与替换等功能。

> [!note] 注意
> 此示例代码项目与 WWDC22 会话相关：[10069: Meet desktop class iPad](https://developer.apple.com/wwdc22/10069/)、[10070: Build a desktop class iPad app](https://developer.apple.com/wwdc22/10070/) 和 [10076: Bring your iOS app to the Mac](https://developer.apple.com/wwdc22/10076/)。

### 选择合适的导航样式

因为 App 允许聚焦地查看和编辑单个文稿，所以它使用 [UINavigationItemStyleEditor](uinavigationitem/itemstyle/editor.md) 导航样式。此导航样式将导航项的标题移动到 leading 边缘，并在栏的中心打开空间，用于放置常见的文稿操作。要选择导航样式，编辑器视图控制器会分配导航项的 [style](uinavigationitem/style.md) 属性。

### 添加中心项以快速访问常见操作

中心项组是在导航栏中显示的控件组，用于提供对 App 最重要能力的快速访问。某人可以通过移动、移除或添加某些组来自定义导航栏的中心项。要启用用户自定义，App 会为导航项的 [customizationIdentifier](uinavigationitem/customizationidentifier.md) 属性分配一个字符串。

```swift
// Set a `customizationIdentifier` and add center item groups.
navigationItem.customizationIdentifier = "editorViewCustomization"
```

编辑器视图控制器在 `configureCenterItemGroups()` 中配置中心项，并将它们分配给导航项的 [centerItemGroups](uinavigationitem/centeritemgroups.md) 属性。编辑器视图控制器使用 [- creatingFixedGroup](<uibarbuttonitem/creatingfixedgroup().md>) 创建一个某人不能移动或移除的固定组，用于 Sync Scrolling 项。

```swift
UIBarButtonItem(primaryAction: UIAction(title: "Sync Scrolling", image: syncScrollingImage) { [unowned self] action in
    syncScrolling.toggle()
    if let barButtonItem = action.sender as? UIBarButtonItem {
        barButtonItem.image = syncScrollingImage
    }
}).creatingFixedGroup(),
```

其他中心项组是可选的，这意味着某人可以在导航栏中自定义它们的放置位置。将 `isInDefaultCustomization` 设置为 `false` 的可选组默认不会出现在导航栏中。它们会出现在某人可以通过溢出菜单中的自定义选项访问的自定义弹出窗口中。

```swift
UIBarButtonItem(primaryAction: UIAction(title: "Strikethrough", image: UIImage(systemName: "strikethrough")) { [unowned self] _ in
    insertTag(.strikethrough)
}).creatingOptionalGroup(customizationIdentifier: "strikethrough", isInDefaultCustomization: false),
```

### 添加带有系统和自定义操作的标题菜单

当某人轻点导航项的标题时，会出现标题菜单。此菜单可以呈现与当前文稿相关的操作。要配置标题菜单，编辑器视图控制器会为导航项的 [titleMenuProvider](uinavigationitem/titlemenuprovider.md) 属性分配一个闭包。

```swift
navigationItem.titleMenuProvider = { suggested in
    let custom = [
        UIMenu(title: "Export…", image: UIImage(systemName: "arrow.up.forward.square"), children: [
            UIAction(title: "HTML", image: UIImage(systemName: "safari")) { [unowned self] _ in
                previewView.exportAsWebArchive(named: document.localizedName, presenter: self)
            },
            UIAction(title: "PDF", image: UIImage(systemName: "doc.richtext")) { [unowned self] _ in
                previewView.exportAsPDF(named: document.localizedName, presenter: self)
            }
        ])
    ]
    return UIMenu(children: suggested + custom)
}
```

该闭包返回一个菜单，它组合了建议的系统操作和自定义操作。菜单中的第一组操作是系统传入闭包的 `suggested` 操作，包括 Move 和 Duplicate。下一组操作是 App 定义的 `custom` 操作：将文稿导出为 HTML 和 PDF。

### 配置文稿标头

文稿标头显示关于当前文稿的有用信息，例如其标题、文件类型和大小。它还提供一个位置，用于分享或拖放文稿。要在标题菜单顶部显示文稿标头，编辑器视图控制器会为导航项的 [documentProperties](uinavigationitem/documentproperties.md) 属性分配一个 [UIDocumentProperties](uidocumentproperties.md) 对象。

### 启用系统查找与替换体验

编辑器视图支持编辑文稿内容。因为编辑器视图是 [UITextView](uitextview.md) 的子类，启用系统查找与替换体验只需一行代码。

```swift
// Enable Find and Replace in editor text view and register as its
// delegate.
editorTextView.isFindInteractionEnabled = true
```

设置 [findInteractionEnabled](uitextview/isfindinteractionenabled.md) 属性可以使用标准键盘快捷键在文稿中查找文本，并使用系统提供的查找面板快速替换它。

### 增强多选

大纲视图是一个集合视图，作为文稿的目录，允许快速导航或对文稿中的顶级标签执行操作。当某人使用键盘和指针与 App 交互时，此视图支持增强的多选体验。大纲视图通过设置 [allowsMultipleSelection](uicollectionview/allowsmultipleselection.md)、[allowsFocus](uicollectionview/allowsfocus.md) 和 [selectionFollowsFocus](uicollectionview/selectionfollowsfocus.md) 为 `true`，在不将集合视图置于编辑模式的情况下启用对标签的轻量多选。

```swift
// Enable multiple selection.
collectionView.allowsMultipleSelection = true

// Enable keyboard focus.
collectionView.allowsFocus = true

// Allow keyboard focus to drive selection.
collectionView.selectionFollowsFocus = true
```

某人可以使用键盘和指针来选择标签，并执行二次点击以打开包含相关操作的上下文菜单。大纲视图通过实现 [- collectionView:contextMenuConfigurationForItemsAtIndexPaths:point:](<uicollectionviewdelegate/collectionview(__contextmenuconfigurationforitemsat_point_).md>) 来根据选择中的标签数量呈现专门的上下文菜单，当选择包含一个或多个标签时返回不同的配置。

```swift
if indexPaths.count > 1 {
    // Action titles for a multiple-item menu.
    hideTitle = "Hide Selected"
    deleteTitle = "Delete Selected"
} else {
    // Action titles for a single-item menu.
    hideTitle = "Hide"
    deleteTitle = "Delete"
}
```

### 在轻点单个项时执行主要操作

除了在大纲视图中的标签上执行二次点击外，某人还可以轻点单个标签，以滚动到编辑器视图中其对应的位置。为了将轻点单个标签以导航到文稿中该位置这一明确用户操作，与选择多个标签区分开来，大纲视图实现了 [- collectionView:performPrimaryActionForItemAtIndexPath:](<uicollectionviewdelegate/collectionview(__performprimaryactionforitemat_).md>)。当某人轻点单个标签而没有扩展多选标签时，系统会调用此方法。

```swift
func collectionView(_ collectionView: UICollectionView, performPrimaryActionForItemAt indexPath: IndexPath) {
    // Get the element at the `indexPath`.
    if let element = dataSource.itemIdentifier(for: indexPath) {
        delegate?.outline(self, didChoose: element)
    }

    // Wait a short amount of time before deselecting the cell for visual clarity.
    DispatchQueue.main.asyncAfter(deadline: .now() + 0.2) {
        collectionView.deselectItem(at: indexPath, animated: true)
    }
}
```

## 另请参阅

### iPad, Mac, and Apple Vision Pro

- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md) — 通过采用多任务处理、Stage Manager、文稿交互、文本编辑、搜索等桌面级增强功能，优化你的 iPad App 的用户体验。
- [Elevating your iPad app with a tab bar and sidebar](elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md) — 提供紧凑、符合人体工程学的标签页栏，用于快速访问 App 的关键部分，以及用于深入导航的边栏。
- [Multitasking on iPad, Mac, and Apple Vision Pro](multitasking-on-ipad-mac-and-apple-vision-pro.md) — 实现多任务 API，以便将你的 App 与 iPadOS、macOS 和 visionOS 无缝集成。

## 下载

- [SupportingDesktopClassFeaturesInYourIPadApp.zip](https://docs-assets.developer.apple.com/published/037b0a0bd9d7/SupportingDesktopClassFeaturesInYourIPadApp.zip)
