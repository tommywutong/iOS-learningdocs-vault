---
title: 通过标签页栏和边栏提升你的 iPad App
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/elevating-your-ipad-app-with-a-tab-bar-and-sidebar
source_url: 'https://developer.apple.com/documentation/uikit/elevating-your-ipad-app-with-a-tab-bar-and-sidebar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/elevating-your-ipad-app-with-a-tab-bar-and-sidebar.json'
content_hash: 'sha256:220d0c0c708d2607'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [App and environment](app-and-environment.md)

# 通过标签页栏和边栏提升你的 iPad App

<sub>文章</sub>

提供一个紧凑、符合人体工程学的标签页栏，用于快速访问 App 的关键部分，再配上一个用于深入导览的边栏。

## 概述

在 iPadOS 中，标签页栏悬浮在内容的顶部，为 App 的内容留出更多空间。此外，由于标签页栏与导航栏共享空间，它让标签页更靠近 App 的其他控制。

![展示悬浮标签页栏位于屏幕顶部位置的 iPad 示意图。](../../../attachments/5194751ad1507036389d31462de10afc/elevating-your-ipad-app-with-a-tab-bar-and-sidebar-1@2x.png)

> [!note] SwiftUI 对应方案
> 有关在 SwiftUI 中采用这种标签页栏外观的信息，请阅读[通过标签页导览增强 App 的内容](../swiftui/enhancing-your-app-content-with-tab-navigation.md)。

### 创建标签页栏

创建一个 [UITabBarController](uitabbarcontroller.md)，并将 [UITab](uitab.md) 对象数组赋值给它的 [tabs](uitabbarcontroller/tabs.md) 属性。要创建标签页，调用 [- initWithTitle:image:identifier:viewControllerProvider:](<uitab/init(title_image_identifier_viewcontrollerprovider_).md>)。在闭包中，返回当有人选择该标签页时 App 呈现的视图控制器。如果你为标签页的图像使用 SF 符号，请确保选择轮廓变体。系统会根据上下文自动选择正确的变体（轮廓或填充）。此外，你可以在运行时更改标签页的属性，比如 [title](uitab/title.md) 或 [image](uitab/image.md)，系统会自动更新其外观。

```swift
// Create the tab bar controller.
let tabBarController = UITabBarController()

// Assign an array of tabs.
tabBarController.tabs = [

   UITab(title: "First",
         image: UIImage(systemName: "1.circle"),
         identifier: "First Tab") { _ in
             // Return the view controller that the tab displays.
             MyFirstViewController()
         },
   
   UITab(title: "Second",
         image: UIImage(systemName: "2.circle"),
         identifier: "Second Tab") { _ in
             // Return the view controller that the tab displays.
             MySecondViewController()
         },
   
   UITab(title: "Third",
         image: UIImage(systemName: "3.circle"),
         identifier: "Third Tab") { _ in
             // Return the view controller that the tab displays.
             MyThirdViewController()
         }
]
```

要添加搜索标签页，创建一个 [UISearchTab](uisearchtab.md) 实例并将其添加到 tabs 数组中。

```swift
// Create a search tab.
UISearchTab { _ in 
    // Return the view controller that the tab displays.
    UINavigationController(
        rootViewController: MySearchViewController()
    )
}

```

除了用系统提供的符号为搜索配置标签页外，当标签页栏处于紧凑状态时，`UISearchTab` 还会自动将搜索标签页与其他标签页分开。

![展示第一、第二和第三个标签页位于屏幕顶部位置的 iPad 示意图。](../../../attachments/d9f23673887e9524618cbe06e88a9690/elevating-your-ipad-app-with-a-tab-bar-and-sidebar-2@2x.png)

iPad 标签页栏支持数量不限的条目。如果没有足够的空间显示所有标签页，系统会折叠屏幕上放不下的标签页，并让用户可以滚动查看它们。不过，建议将标签页数量限制在标签页栏能容纳的范围内。这可以确保用户只需一次点按即可访问 App 的关键部分。

### 整合标签页栏和边栏

尽管标签页栏和边栏在 iPadOS App 中都扮演着相似的导览角色，但它们各有优势。标签页栏始终可用，代表 App 的关键部分。边栏提供更丰富的可选目的地集合；不过，用户通常需要导览回边栏才能选择其他选项。

如果你的 App 包含丰富的视图层级结构，你可以创建一个标签页条目数组，系统会将其显示为标签页栏或边栏。这种组合提供了两种导览样式的最佳特性。以标签页栏显示时，用户可以快速访问 App 中最重要的部分。以边栏显示时，用户可以查看 App 的完整范围和深度。

![](../../../attachments/7020d9af6aba086fd48540d3323c70b4/elevating-your-ipad-app-with-a-tab-bar-and-sidebar-3@2x.png)

<sub>两台并排放置的 iPad 示意图。第一台 iPad 以横屏方向在屏幕左侧显示边栏。第二台 iPad 以竖屏方向在屏幕顶部显示标签页栏。</sub>

使用 [UITab](uitab.md) 和 [UITabGroup](uitabgroup.md) 类来创建标签页的层级结构。如果 tabs 数组至少包含一个标签页组，系统会自动将这些标签页同时显示为标签页栏和边栏。否则，它只会将该数组显示为标签页栏。你也可以通过设置 [UITabBarController](uitabbarcontroller.md) 对象的 [mode](uitabbarcontroller/mode-swift.property.md) 属性来显式定义系统如何显示你的标签页。

```swift
// Enable the sidebar.
tabBarController.mode = .tabSidebar

// Get the sidebar.
let sidebar = tabBarController.sidebar

// Show the sidebar.
sidebar.isHidden = false
```

默认情况下，系统在横屏方向呈现边栏，并在竖屏方向隐藏它；不过，用户可以在任一方向下切换标签页栏和边栏。你也可以通过设置边栏的 [hidden](uitabbarcontroller/sidebar-swift.class/ishidden.md) 属性以编程方式显示和隐藏它。

### 为边栏构建条目层级结构

你可以使用 [UITabGroup](uitabgroup.md) 在边栏中定义一个条目区块。为该区块的内容提供一个标签页数组，并提供一个视图控制器，当有人从标签页栏中选择该区块时显示它。

```swift
let sectionOne = UITabGroup(
    title: "Section 1",
    image: UIImage(systemName: "1.square.fill"),
    identifier: "Section one",
    children:
        [
            UITab(
                title: "Subitem A",
                image: UIImage(systemName: "a.circle"),
                identifier: "Section 1, item A"
            ) { _ in
                MyFirstSubitemTabViewController()
            },
            
            UITab(
                title: "Subitem B",
                image: UIImage(systemName: "b.circle"),
                identifier: "Section 1, item B"
            ) { _ in
                MySecondSubitemTabViewController()
            },
            
            UITab(
                title: "Subitem C",
                image: UIImage(systemName: "c.circle"),
                identifier: "Section 1, item C"
            ) { _ in
                MyThirdSubitemTabViewController()
            },
        ]) { _ in
            // Return a view controller that the system displays when someone selects the section in the tab bar.
            MySectionViewController()
        }
```

标签页栏将标签页组显示为单个标签页条目，而边栏将其显示为包含子条目的区块。边栏先显示顶层标签页条目，再显示区块。

![](../../../attachments/bb9b16265dd5e2772ccb94bd8f914a22/elevating-your-ipad-app-with-a-tab-bar-and-sidebar-4@2x.png)

<sub>横屏方向的 iPad 示意图，展示边栏中显示的标签页层级结构。顶层标签页先出现，随后是标签页组。</sub>

你可以将一个 [UITabGroup](uitabgroup.md) 嵌套在另一个 [UITabGroup](uitabgroup.md) 内，从而在边栏中创建更深的层级结构；不过，建议将 App 限制在两层，最多三层。此外，你可以在运行时通过修改标签页组的 [children](uitabgroup/children.md) 属性来动态更改其内容。

### 为边栏添加操作

你可以通过设置标签页组的 [sidebarActions](uitabgroup/sidebaractions.md) 属性为边栏添加操作。这些操作的作用就像放置在标签页组内的按钮一样。

```swift
// Create the action.
let refreshAction = UIAction(title: "Refresh", image: UIImage(systemName: "arrow.clockwise")) { _ in
    myAction()
}

// Assign the action.
sectionOne.sidebarActions = [refreshAction]
```

要支持轻扫操作或上下文菜单，需要为你的边栏分配一个采用 [Delegate](uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol.md) 协议的委托，并实现以下可选方法：

- [- tabBarController:sidebar:leadingSwipeActionsConfigurationForTab:](<uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(__sidebar_leadingswipeactionsconfigurationfor_).md>)
- [- tabBarController:sidebar:trailingSwipeActionsConfigurationForTab:](<uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(__sidebar_trailingswipeactionsconfigurationfor_).md>)
- [- tabBarController:sidebar:contextMenuConfigurationForTab:](<uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(__sidebar_contextmenuconfigurationfor_).md>)

要支持拖放操作，需要为你的标签页栏分配一个采用 [UITabBarControllerDelegate](uitabbarcontrollerdelegate.md) 协议的委托，并实现 [- tabBarController:tab:operationForAcceptingItemsFromDropSession:](<uitabbarcontrollerdelegate/tabbarcontroller(__tab_operationforacceptingitemsfrom_).md>) 和 [- tabBarController:tab:acceptItemsFromDropSession:](<uitabbarcontrollerdelegate/tabbarcontroller(__tab_acceptitemsfrom_).md>) 方法。

### 启用自定义

用户可以使用系统提供的按钮将标签页栏和边栏切换到编辑模式，从而自定义两者中的内容。在编辑期间，用户可以：

- 将条目从边栏拖到标签页栏中，将它们添加到标签页栏。
- 将条目从标签页栏拖出，将它们从标签页栏中移除。
- 拖动条目以在标签页栏中重新排序。
- 拖动条目以在其所属标签页组内重新排序。
- 取消勾选边栏中的条目以隐藏它们。这也会将它们从标签页栏中移除。

系统会自动持久化用户对这些栏所做的任何自定义。你可以实现 [- tabBarController:displayOrderDidChangeForGroup:](<uitabbarcontrollerdelegate/tabbarcontroller(__displayorderdidchangefor_).md>) 和 [- tabBarController:visibilityDidChangeForTabs:](<uitabbarcontrollerdelegate/tabbarcontroller(__visibilitydidchangefor_).md>) 委托方法来接收有关这些更改的通知。

![展示处于编辑模式下的边栏和标签页栏、横屏方向的 iPad 示意图。](../../../attachments/2c1d198113fa2823bf3b4767a2137ef6/elevating-your-ipad-app-with-a-tab-bar-and-sidebar-5@2x.png)

默认情况下，标签页栏中只会出现顶层标签页。用户可以在边栏中添加或移除任意标签页，但无法隐藏或重新排序边栏中的条目。

要控制标签页栏中出现哪些条目，以及用户可以如何自定义它们，请设置 [UITab](uitab.md) 对象的 [preferredPlacement](uitab/preferredplacement.md) 属性。从概念上讲，你可以将标签页栏视为拥有三个不同的区域：

- 固定标签页出现在标签页栏的前缘。
- 默认、可选和可移动的标签页出现在固定标签页之后。
- 固定钉住的标签页始终显示在后缘，并且只显示标签页的图像。

在可能的情况下，让标签页可自定义，以便用户可以选择将哪些标签页放置在标签页栏中。如果你的 App 中有任何核心标签页，考虑将它们设为固定标签页，这样用户就无法移除或移动它们。对于像搜索这样醒目的条目，使用钉住的标签页。此外，由于钉住的标签页只显示标签页图标，请确保选择用户能够识别并容易理解的图像。

![](../../../attachments/546084e124ca71f50de854b1ea664bc5/elevating-your-ipad-app-with-a-tab-bar-and-sidebar-6@2x.png)

<sub>横屏方向的 iPad 示意图，展示标签页栏和边栏中的固定、可选、钉住和可移动标签页。</sub>

要创建一个出现在边栏中、但用户无法将其添加到标签页栏的条目，请将 [preferredPlacement](uitab/preferredplacement.md) 属性设为 [UITabPlacementSidebarOnly](uitab/placement/sidebaronly.md)。要创建一个用户可以在边栏中添加或移除的条目，请将其 [allowsHiding](uitab/allowshiding.md) 属性设为 [true](../swift/true.md)。如果有人将某个条目从边栏中移除，系统也会将其从标签页栏中移除。

```swift
// Create the tab.
var customizableItem = UITab(
        title: "Optional",
        image: UIImage(systemName: "questionmark.app"),
        identifier: "Optional Item"
) { _ in
    MyOptionalViewController()
}

// Let people add and remove this item in the sidebar.
customizableItem.allowsHiding = true

// Set the item as hidden in the sidebar by default.
customizableItem.isHiddenByDefault = true
```

要让用户在标签页组内重新组织条目，请将该组的 [allowsReordering](uitabgroup/allowsreordering.md) 属性设为 [true](../swift/true.md)。

```swift
sectionOne.allowsReordering = true
```

你也可以使用标签页组的 [displayOrderIdentifiers](uitabgroup/displayorderidentifiers.md) 属性以编程方式设置组内条目的顺序。默认情况下，系统根据标签页组的 [children](uitabgroup/children.md) 属性设置其顺序。

> [!important] 重要
> 当有人自定义标签页栏或边栏时，系统会持久化这些更改。App 下次启动时，会将每个标签页的 [hidden](uitab/ishidden.md) 和 [displayOrderIdentifiers](uitabgroup/displayorderidentifiers.md) 属性设为自定义后的值。系统会在将标签页添加到 [UITabBarController](uitabbarcontroller.md) 时赋予这些值。如果你的 App 在添加标签页之前以编程方式设置了 [hidden](uitab/ishidden.md) 或 [displayOrderIdentifiers](uitabgroup/displayorderidentifiers.md) 属性，自定义后的值会覆盖 App 赋予的值。但是，如果你在添加标签页之后更改这些值，你设置的值会覆盖自定义结果。

### 在其他平台上使用标签页栏和边栏

[UITab](uitab.md) API 在所有支持 UIKit 的平台上都可用。考虑在 iOS、Mac Catalyst、tvOS 和 visionOS 中基于 UIKit 的项目里使用此 API 来创建标签页栏。

标签页栏的配置会根据平台和可用空间的不同而呈现不同的样式：

- 在 iPad 上，系统在顶部显示标签页栏，在前缘显示边栏。
- 在 iPhone、Apple TV 以及 App 以紧凑尺寸显示的 iPad 上，系统显示该平台的常规标签页栏。
- 对于 Mac Catalyst，如果标签页栏控制器的 [mode](uitabbarcontroller/mode-swift.property.md) 属性为 [UITabBarControllerModeTabBar](uitabbarcontroller/mode-swift.enum/tabbar.md)，系统会显示标签页栏；如果为 [UITabBarControllerModeTabSidebar](uitabbarcontroller/mode-swift.enum/tabsidebar.md)，系统会显示边栏。

在 visionOS 中，系统会显示该平台的常规标签页，但 [UITabGroup](uitabgroup.md) 在显示该组的视图控制器时可以显示边栏。

## 另请参阅

### iPad、Mac 与 Apple Vision Pro

- [为你的 iPad App 打造桌面级体验](building-a-desktop-class-ipad-app.md) — 通过采用桌面级增强功能来优化你 iPad App 的用户体验，涵盖 Stage Manager 多任务处理、文稿交互、文本编辑、搜索等方面。
- [在你的 iPad App 中支持桌面级特性](supporting-desktop-class-features-in-your-ipad-app.md) — 通过添加桌面级特性和文稿支持来增强你的 iPad App。
- [在 iPad、Mac 和 Apple Vision Pro 上实现多任务处理](multitasking-on-ipad-mac-and-apple-vision-pro.md) — 实现多任务处理 API，让你的 App 与 iPadOS、macOS 和 visionOS 无缝集成。

