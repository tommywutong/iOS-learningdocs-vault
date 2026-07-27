---
title: 向菜单栏和用户界面添加菜单和快捷键
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, Xcode 13.1+]
languages: [swift, swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface
source_url: 'https://developer.apple.com/documentation/uikit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.json'
content_hash: 'sha256:f23ab9bbaf133f53'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Mac Catalyst](mac-catalyst.md)

# 向菜单栏和用户界面添加菜单和快捷键

<sub>示例代码</sub>

通过为使用 Mac Catalyst 构建的 Mac App 添加菜单和键盘快捷键，提供对常用操作的快速访问。

## 概述

这个示例项目演示了如何向菜单栏添加菜单命令和键盘快捷键。这个示例 App 使用其 `MenuController` 对象插入一个 [UIMenuSystem](uimenusystem.md) 对象，用于添加以下菜单：

- New：出现在「文件」菜单的开头，包含「New Date Item」和「New Text Item」两个操作，用于向表格视图添加条目。
- Cities：包含一组 UICommand 和 UIKeyCommand 对象。
- Navigation：包含一组用于命令键导览的 UIKeyCommand 对象。
- Style：包含一组带有勾选状态的 UICommand 对象。这个分组看起来就像用于文本格式设置的字体样式菜单。
- Tools：包含一组 UICommand 对象。

这个示例项目还展示了如何为视图添加上下文菜单，以及如何使用 [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md) 处理菜单命令的选择。

### 配置示例代码项目

在 Xcode 中，于 iOS 目标的「Signing and Capabilities」标签页上选择你的开发团队。

### 向菜单栏添加菜单

创建 `UIMenu` 对象，并使用它们来构建菜单和子菜单。这个示例在 macOS 上运行时会向菜单栏添加菜单，这些菜单中的按键命令元素在用户按下 command 键时，也会出现在 iPad 上的可发现性抬头显示（HUD）中。

iPad App 的 Mac 版本自带一个标准菜单栏。使用 [UIMenuSystem](uimenusystem.md) 类（代表主菜单系统或上下文菜单系统的对象）来修改菜单栏。

这个示例通过在 `AppDelegate` 中实现 [- buildMenuWithBuilder:](<uiresponder/buildmenu(with_).md>)，使用 `UIMenuSystem` 向 [mainSystem](uimenusystem/main.md) 系统菜单添加菜单和按键命令。这个函数接收一个 [UIMenuBuilder](uimenubuilder.md) 对象，示例随后使用它来添加和移除菜单。由于菜单可以在没有窗口或视图层级结构的情况下存在，系统只会查询 `UIApplication` 和 `UIApplicationDelegate` 来构建 App 的菜单栏。

菜单命令由 `UICommand`、`UIKeyCommand` 和 [UIAction](uiaction.md) 对象组成，这些对象被归入一个 `UIMenu` 容器中。

### 向文件菜单添加菜单命令

这个示例向「文件」菜单插入了一个名为 Command-O 的 `UIKeyCommand`，并创建了相应的键盘快捷键：

```swift
class func openMenu() -> UIMenu {
    let openCommand =
        UIKeyCommand(title: NSLocalizedString("OpenTitle", comment: ""),
                     image: nil,
                     action: #selector(AppDelegate.openAction),
                     input: "o",
                     modifierFlags: .command)
    let openMenu =
        UIMenu(title: "",
               image: nil,
               identifier: .openMenu,
               options: .displayInline,
               children: [openCommand])
    return openMenu
}
```

请注意，`UIKeyCommand` 的标题是使用 [`NSLocalizedString`](../foundation/nslocalizedstring.md) 函数得到的本地化字符串，这样可以用多种语言显示菜单名称。

这个示例将 Open 命令插入到菜单栏「文件」菜单的中间位置：

```swift
builder.insertChild(MenuController.openMenu(), atStartOfMenu: .file)
```

Mac App 通常也会在「文件」菜单中包含一个 Print 菜单命令。这个示例在「文件」菜单中同时包含了 Print 和 Export as PDF 菜单命令。当 `Info.plist` 包含值设置为 `true` 的 `UIApplicationSupportsPrintCommand` 键时，这些菜单命令会被自动插入。应用通过实现 `UIResponder` 的 `printContent(_ sender: Any?)` 函数来响应这些打印命令。

### 为编辑菜单贡献内容

剪切、拷贝、粘贴和删除等编辑操作，在大多数 App 中都很常用。这个示例 App 通过「编辑」菜单提供这些操作，用户可以在其中编辑示例的左侧内容或其主要的表格视图内容。这些操作对应第一响应者的函数 `cut(_ sender: Any?)`、`copy(_ sender: Any?)`、`paste(_ sender: Any?)`、`delete(_ sender: Any?)`。

这个示例实现了 `canPerformAction:withSender:`，用来判断是否支持这些编辑操作。

```swift
override func canPerformAction(_ action: Selector, withSender sender: Any?) -> Bool {
    if action == #selector(printContent) {
        // Allow for printing if a table view cell is selected.
        return tableView.indexPathForSelectedRow != nil
    } else if action == #selector(newAction(_:)) {
        // User wants to perform a New operation.
        return true
    } else {
        switch (tableView.indexPathForSelectedRow, action) {
        
        // These Edit commands are supported.
        case let (_?, action) where action == #selector(cut(_:)) ||
                                    action == #selector(copy(_:)) ||
                                    action == #selector(delete(_:)):
            return true
        case (_?, _):
            // Allow the nextResponder to make the determination.
            return super.canPerformAction(action, withSender: sender)
            
        // Paste is supported if the pasteboard has text.
        case (.none, action) where action == #selector(paste(_:)):
            return (UIPasteboard.general.string != nil) ? true :
                // Allow the nextResponder to make the determination.
                super.canPerformAction(action, withSender: sender)
        case (.none, _):
            return false
        }
    }
}
```

### 添加用于控制用户界面的命令

在这个示例中，你可以使用 [UIKeyCommand](uikeycommand.md) 更改主要（左侧）表格视图的选择。这些按键命令被连接到上箭头键和下箭头键，并被直接添加到表格视图。下面的示例展示了如何将下箭头键添加为一个 `UIKeyCommand`：

```swift
let downArrowCommand =
    UIKeyCommand(input: UIKeyCommand.inputDownArrow,
                 modifierFlags: [],
                 action: #selector(PrimaryViewController.downArrowAction(_:)))
addKeyCommand(downArrowCommand)
```

这个示例还演示了如何将菜单命令添加为命令键等效项。下面的示例展示了如何创建一个包含全部四个方向键作为命令键的菜单：

```swift
class func navigationMenu() -> UIMenu {
    let keyCommands = [ UIKeyCommand.inputRightArrow,
                        UIKeyCommand.inputLeftArrow,
                        UIKeyCommand.inputUpArrow,
                        UIKeyCommand.inputDownArrow ]
    let arrows = Arrows.allCases
    
    let arrowKeyChildrenCommands = zip(keyCommands, arrows).map { (command, arrow) in
        UIKeyCommand(title: arrow.localizedString(),
                     image: nil,
                     action: #selector(AppDelegate.navigationMenuAction(_:)),
                     input: command,
                     modifierFlags: .command,
                     propertyList: [CommandPListKeys.ArrowsKeyIdentifier: arrow.rawValue])
    }
    
    let arrowKeysGroup = UIMenu(title: "",
                  image: nil,
                  identifier: .arrowsMenu,
                  options: .displayInline,
                  children: arrowKeyChildrenCommands)
    
    return UIMenu(title: NSLocalizedString("NavigationTitle", comment: ""),
                  image: nil,
                  identifier: .navMenu,
                  options: [],
                  children: [arrowKeysGroup])
}
```

### 显示上下文菜单

这个示例通过使用 `UIContextMenuInteractionDelegate`（一个用于显示与内容相关操作的交互对象）来显示上下文菜单。

在 macOS 上，用户可以按住 control 点按或右键点按 `DetailViewController`。在 iPadOS 上，用户可以点按并按住 `DetailViewController`。这个示例使用 `UIContextMenuInteractionDelegate` 来显示 Cut、Copy、Paste、Delete、Rename 和 Share 命令。这种上下文菜单是一组 `UIAction` 对象的集合。`UIAction` 是一种在闭包中执行其操作的菜单元素。在 iOS 中，你可以选择使用 [- contextMenuInteraction:previewForHighlightingMenuWithConfiguration:](<uicontextmenuinteractiondelegate/contextmenuinteraction(__previewforhighlightingmenuwithconfiguration_).md>) 来自定义这个上下文菜单的高亮预览。这个委托函数返回一个主要的视图控制器。重写这个函数，可以根据表格视图的状态或粘贴板的状态来启用菜单命令。

### 调整样式菜单

这个示例实现了 [- validateCommand:](<uiresponder/validate(__).md>)，可以在用户于纯文本、粗体、斜体、下划线这几种字体样式之间进行选择时，调整「样式」菜单。

```swift
// The font style menu item check marks used in the Style menu.
var fontMenuStyleStates = Set<String>()

// Update the state of a given command by adjusting the Style menu.
// Note: Only command groups that are added will be called to validate.
override func validate(_ command: UICommand) {
    // Obtain the plist of the incoming command.

    if let fontStyleDict = command.propertyList as? [String: String] {
        // Check if the command comes from the Style menu.
        if let fontStyle = fontStyleDict[MenuController.CommandPListKeys.StylesIdentifierKey] {
            // Update the Style menu command state (checked or unchecked).
            command.state = fontMenuStyleStates.contains(fontStyle) ? .on : .off
        }
    } else {
        // Validate the disabled command. This keeps the menu item disabled.
        if let commandPlistString = command.propertyList as? String {
            if commandPlistString == MenuController.disabledCommand {
                command.attributes = .disabled
            }
        }
    }
}
```

### 添加设置菜单

Mac App 通常使用「设置」窗口来显示特定于 App 的设置。这个示例通过向 Xcode 项目的目标添加一个 Settings bundle 来添加「设置」窗口。用户可以通过「应用」菜单中的「设置」菜单命令自动使用该窗口。要了解设置的更多内容，请参阅 [Displaying a Settings window](displaying-a-settings-window.md)。

## 另请参阅

### User interactions

- [Navigating an app’s user interface using a keyboard](navigating-an-app-s-user-interface-using-a-keyboard.md) — 在 iPad App 和使用 Mac Catalyst 构建的 App 中，使用键盘和可获得焦点的 UI 元素在用户界面元素之间导览。
- [Handling key presses made on a physical keyboard](handling-key-presses-made-on-a-physical-keyboard.md) — 检测用户何时按下和释放物理键盘上的按键。
- [UIHoverGestureRecognizer](uihovergesturerecognizer.md) — 一种连续手势识别器，用于解读指针在视图上方的移动。

## 下载

- [AddingMenusAndShortcutsToTheMenuBarAndUserInterface.zip](https://docs-assets.developer.apple.com/published/5e60ae06106d/AddingMenusAndShortcutsToTheMenuBarAndUserInterface.zip)
</content>
