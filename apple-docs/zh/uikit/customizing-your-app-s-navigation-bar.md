---
title: 自定 App 的导航栏
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+, Xcode 26.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/customizing-your-app-s-navigation-bar
source_url: 'https://developer.apple.com/documentation/uikit/customizing-your-app-s-navigation-bar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/customizing-your-app-s-navigation-bar.json'
content_hash: 'sha256:7d39352884dff380'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [视图控制器](view-controllers.md) · [UINavigationController](uinavigationcontroller.md)

# 自定 App 的导航栏

<sub>示例代码</sub>

在 App 的导航栏中创建自定标题、提示和按钮。

## 概述

当你使用导览控制器为 App 添加导览结构时，可以使用视图控制器的 [navigationItem](uiviewcontroller/navigationitem.md) 来配置 [UINavigationBar](uinavigationbar.md)，在内容上方、iOS 设备屏幕顶部的一个栏中加入导览和交互控制。

本示例代码项目演示如何使用 [UINavigationController](uinavigationcontroller.md) 和 [UIViewController](uiviewcontroller.md) 类作为 App 用户界面的构建单元。

该项目通过一组示例引导你自定 [UINavigationController](uinavigationcontroller.md) 和 [UINavigationBar](uinavigationbar.md) 的外观和行为，包括 App 导航栏的视图、提示、按钮和标题。

示例演示了通过视图控制器的 [UINavigationItem](uinavigationitem.md) 修改导航栏的方法，包括：

- 自定栏中的按钮
- 从栏按钮呈现菜单
- 调整按钮在导航栏或工具栏中的分组方式
- 在工具栏中集成系统搜索
- 更新栏的标题和副标题
- 添加导览提示
- 用标题或图像自定返回按钮

### 自定右侧视图

导航栏右侧可供自定的选项包括应用自定 `UIView` 或使用 `UIBarButtonItem`。

示例演示了在导航栏右侧放置三种 `UIBarButtonItem`：带标题的按钮、带图像的按钮，以及带 `UISegmentedControl` 的按钮。另一个分段控制让用户在这三个按钮之间切换。最初的栏按钮在 storyboard 中定义，方法是把 `UIBarButtonItem` 从对象库中拖入导航栏。示例还展示了如何使用代码创建并添加每种按钮类型。

例如，示例展示了如何在 `CustomRightViewController` 中将分段控制设置为右侧栏按钮项：

```swift
let segmentBarItem = UIBarButtonItem(customView: segmentedControl)
navigationItem.rightBarButtonItem = segmentBarItem
```

### 为按钮使用默认分组

当你向导览项添加栏按钮项时，系统会把以下按钮分组到一个共享玻璃背景中：

- 图像按钮
- 包含多个项目的栏按钮项分组

系统会为以下按钮提供单独的玻璃背景：

- 文本按钮
- [UIBarButtonSystemItemDone](uibarbuttonitem/systemitem/done.md) 按钮
- [UIBarButtonSystemItemClose](uibarbuttonitem/systemitem/close.md) 按钮
- [UIBarButtonItemStyleProminent](uibarbuttonitem/style-swift.enum/prominent.md) 按钮

示例在 `DefaultButtonGroupingViewController` 中展示了系统提供的默认分组示例：

```swift
let selectBarButton = UIBarButtonItem(title: NSLocalizedString("Select", comment: ""),
                                      style: .plain,
                                      target: nil,
                                      action: nil)
let shareBarButton = UIBarButtonItem(image: UIImage(systemName: "square.and.arrow.up"),
                                     style: .plain,
                                     target: nil,
                                     action: nil)
let infoBarButton = UIBarButtonItem(image: UIImage(systemName: "info.circle"),
                                    style: .plain,
                                    target: nil,
                                    action: nil)
let doneBarButton = UIBarButtonItem(barButtonSystemItem: .done,
                                    target: nil,
                                    action: nil)

navigationItem.rightBarButtonItems = [doneBarButton,
                                      shareBarButton,
                                      infoBarButton,
                                      selectBarButton]
```

### 自定按钮分组

当系统把按钮分组到共享玻璃背景中，而你想把按钮拆分到各自的玻璃背景时，请在想要拆分玻璃背景的按钮之间添加 [+ fixedSpaceItem](<uibarbuttonitem/fixedspace().md>)。

示例在 `CustomButtonGroupsViewController` 中演示了这种做法。默认情况下，`shareBarButton` 和 `infoBarButton` 共享一个玻璃背景，因为它们都是带图像的按钮。示例在它们之间添加了一个 [+ fixedSpaceItem](<uibarbuttonitem/fixedspace().md>)，使它们各自拥有自己的玻璃背景：

```swift
navigationItem.rightBarButtonItems = [doneBarButton,
                                      shareBarButton,
                                      .fixedSpace(0),
                                      infoBarButton,
                                      selectBarButton]
```

### 自定按钮标签和背景颜色

设置栏按钮项的色调颜色（tint color），为按钮的文本或图像提供颜色。示例在 `CustomButtonColorsViewController` 中演示了这种做法：

```swift
let shareBarButton = UIBarButtonItem(image: UIImage(systemName: "square.and.arrow.up"),
                                     style: .plain,
                                     target: nil,
                                     action: nil)
shareBarButton.tintColor = .systemOrange
```

要让某个按钮更引人注目，你可以使用醒目的按钮样式，让系统用色调颜色填充按钮的背景。示例演示了两种做法。首先，将栏按钮项的样式设置为 [UIBarButtonItemStyleProminent](uibarbuttonitem/style-swift.enum/prominent.md)：

```swift
let infoBarButton = UIBarButtonItem(image: UIImage(systemName: "info.circle"),
                                    style: .plain,
                                    target: nil,
                                    action: nil)
infoBarButton.tintColor = .systemOrange
infoBarButton.style = .prominent
```

其次，使用带系统默认图像和颜色的系统条目：

```swift
let doneBarButton = UIBarButtonItem(barButtonSystemItem: .done,
                                    target: nil,
                                    action: nil)
```

### 为使用弹性间距的工具栏项目分组

当你使用弹性间距栏按钮项在工具栏中均匀间隔按钮时，系统会在弹性间距之间提供单独的玻璃背景。在 `CustomToolbarLayoutViewController` 中，示例展示了如何让所有按钮共享同一个玻璃背景，方法是先用 [hidesSharedBackground](uibarbuttonitem/hidessharedbackground.md) 配置弹性间距：

```swift
let flexibleSpace = UIBarButtonItem.flexibleSpace()
flexibleSpace.hidesSharedBackground = false
```

然后，示例使用它配置的弹性间距来间隔按钮：

```swift
toolbarItems = [
    .init(image: UIImage(systemName: "location")),
    flexibleSpace,
    .init(image: UIImage(systemName: "number")),
    flexibleSpace,
    .init(image: UIImage(systemName: "camera")),
    flexibleSpace,
    .init(image: UIImage(systemName: "trash"))
]
```

### 在工具栏中集成搜索

当你使用 [UISearchController](uisearchcontroller.md) 和导览控制器的工具栏时，系统提供了一种内置方法在 App 中集成搜索。示例在 `ToolbarSystemSearchViewController` 中演示了如何进行这种集成。

首先，示例实例化一个搜索控制器：

```swift
searchController = UISearchController(searchResultsController: SearchResultsViewController())
```

然后，示例告诉导览项使用它刚实例化的搜索控制器：

```swift
navigationItem.searchController = searchController
```

最后，示例将导览项的 [searchBarPlacementBarButtonItem](uinavigationitem/searchbarplacementbarbuttonitem.md) 添加到工具栏按钮：

```swift
toolbarItems = [
    .init(image: UIImage(systemName: "location")),
    .init(image: UIImage(systemName: "number")),
    .init(image: UIImage(systemName: "camera")),
    flexibleSpace,
    navigationItem.searchBarPlacementBarButtonItem
]
```

完成这些步骤后，系统会在工具栏中显示一个搜索按钮。当用户轻点搜索栏时，系统会显示一个搜索界面，用户可以在其中输入搜索参数并执行搜索。

### 自定标题视图

另一种做法是将导航栏配置为使用 `UIView` 作为标题，例如使用 `UISegmentedControl` 作为居中的自定标题视图。

示例在 `CustomTitleViewController` 中展示了如何将分段控制设置为标题视图：

```swift
self.navigationItem.titleView = segmentedControl
```

### 自定标题和副标题

导航栏可以包含标题和副标题。示例在 `TitleSubtitleViewController` 中演示了设置标题和副标题：

```swift
navigationItem.title = "Title"
navigationItem.subtitle = "Subtitle"
```

除了用字符串设置标题和副标题外，你还可以使用属性字符串或自定视图。

### 自定大标题下方的副标题视图

你可以设置自定视图来显示在标题、副标题、大标题或大标题下方副标题的位置。在 `LargeTitleViewController` 中，示例展示了一个按钮作为大标题下方的自定副标题视图的例子：

```swift
self.navigationController?.navigationBar.prefersLargeTitles = true

var subtitleConfiguration = UIButton.Configuration.plain()
subtitleConfiguration.title = "Subtitle Button"
subtitleConfiguration.baseForegroundColor = .systemBlue

let subtitleButton = UIButton(configuration: subtitleConfiguration)
navigationItem.largeSubtitleView = subtitleButton
```

### 修改导览提示

导航栏还可以在顶部包含一个提示或单行文本。

示例在 `NavigationPromptViewController` 中演示了如何使用 `UINavigationItem` 的 [prompt](uinavigationitem/prompt.md) 属性在导航栏上方显示一行自定文本：

```swift
navigationItem.prompt = NSLocalizedString("Navigation prompts appear at the top.", comment: "")
```

### 自定返回按钮标题

长按返回按钮可以让用户快速在不同栈层级之间切换。示例在 `MainViewController` 中向当前导航栈压入 10 个视图控制器，以演示为栈中每个视图控制器层级自定返回按钮标题。

### 用图像自定返回按钮

还可以使用图像作为返回按钮，不带任何返回按钮文本，也不带通常出现在返回按钮旁边的返回箭头。示例在 `CustomBackButtonDetailViewController` 中这样设置返回按钮的图像：

```swift
let backButtonBackgroundImage = UIImage(systemName: "list.bullet")
let backButton = UIBarButtonItem(image: backButtonBackgroundImage,
                                 style: .plain,
                                 target: self,
                                 action: #selector(backButtonTapped(_:)))
navigationItem.leftBarButtonItem = backButton
```

### 修改导航栏中的大标题

自定导航栏的另一个选项是启用大标题显示模式，让它显示更大版本的标题。当视图控制器包含滚动视图时，系统会在可滚动内容的顶部显示大标题，并在用户开始滚动时把标题以动画方式收进导航栏。

下面的代码展示了示例如何在 `LargeTitleViewController` 中为导航栏启用大标题显示模式：

```swift
self.navigationController?.navigationBar.prefersLargeTitles = true
```

有关控制导航栏如何显示导览项标题的更多信息，请参阅 [largeTitleDisplayMode](uinavigationitem/largetitledisplaymode-swift.property.md)。

### 为栏按钮项附加菜单

菜单附件让你能在一个地方便捷地访问 App 的各项功能。示例在 `BarButtonMenu` 中将一个 [UIMenu](uimenu.md) 附加到右侧的 `UIBarButtonItem` 控制上：

```swift
let barButtonMenu = UIMenu(title: "", children: [
    UIAction(title: NSLocalizedString("Copy", comment: ""), image: UIImage(systemName: "doc.on.doc"), handler: menuHandler),
    UIAction(title: NSLocalizedString("Rename", comment: ""), image: UIImage(systemName: "pencil"), handler: menuHandler),
    UIAction(title: NSLocalizedString("Duplicate", comment: ""), image: UIImage(systemName: "plus.square.on.square"), handler: menuHandler),
    UIAction(title: NSLocalizedString("Move", comment: ""), image: UIImage(systemName: "folder"), handler: menuHandler)
])
optionsBarItem.menu = barButtonMenu
```

## 另请参阅

### 配置导航栏

- [navigationBar](uinavigationcontroller/navigationbar.md) — 导览控制器所管理的导航栏。
- [- setNavigationBarHidden:animated:](<uinavigationcontroller/setnavigationbarhidden(__animated_).md>) — 设置导航栏是否隐藏。

## 下载

- [CustomizingYourAppsNavigationBar.zip](https://docs-assets.developer.apple.com/published/8b8c14d97eaf/CustomizingYourAppsNavigationBar.zip)
