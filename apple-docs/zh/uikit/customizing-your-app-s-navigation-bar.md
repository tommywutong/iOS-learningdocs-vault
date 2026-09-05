---
title: 自定义你的 App 的导航栏
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

# 自定义你的 App 的导航栏

<sub>示例代码</sub>

在你的 App 的导航栏中创建自定义标题、提示与按钮。

## 概述

当你使用导览控制器为你的 App 添加导览结构时，你可以使用视图控制器的 [navigationItem](uiviewcontroller/navigationitem.md) 来配置 [UINavigationBar](uinavigationbar.md)，在 iOS 设备屏幕顶部、内容上方的栏中放入导览与交互控制。

本示例代码项目演示了如何把 [UINavigationController](uinavigationcontroller.md) 和 [UIViewController](uiviewcontroller.md) 类用作你的 App 用户界面的构建块。

项目通过一组示例引导你自定义 [UINavigationController](uinavigationcontroller.md) 和 [UINavigationBar](uinavigationbar.md) 的外观与行为，包括你的 App 导航栏中的视图、提示、按钮和标题。

示例展示了通过视图控制器的 [UINavigationItem](uinavigationitem.md) 修改导航栏的方法。包括：

- 自定义栏中的按钮
- 从栏按钮呈现菜单
- 调整按钮在导航栏或工具栏中的分组方式
- 在工具栏中集成系统搜索
- 更新栏的标题与副标题
- 添加导览提示
- 用标题或图片自定义返回按钮

### 自定义右侧视图

导航栏右侧可供自定义的选项包括应用自定义 `UIView`，或使用 `UIBarButtonItem`。

示例演示了在导航栏右侧放置三种 `UIBarButtonItems`：带标题的按钮、带图片的按钮，以及带 `UISegmentedControl` 的按钮。另外一个分段控制让用户可以在三个按钮之间切换。最初的栏按钮定义在 storyboard 中，做法是把 `UIBarButtonItem` 从对象库拖入导航栏。示例还展示了如何用代码创建并添加每种按钮类型。

例如，示例展示了如何在 `CustomRightViewController` 中把分段控制设为右侧栏按钮项：

```swift
let segmentBarItem = UIBarButtonItem(customView: segmentedControl)
navigationItem.rightBarButtonItem = segmentBarItem
```

### 对按钮使用默认分组

当你向导览项添加栏按钮项时，系统会把按钮分组放进一个共享的玻璃背景，对象是：

- 图像按钮
- 包含多个条目的栏按钮项组

系统为以下对象提供单独的玻璃背景：

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

### 自定义按钮分组

当系统把按钮分进一个共享玻璃背景，而你想把按钮拆分到各自的玻璃背景时，在想要拆分的位置为按钮之间添加 [+ fixedSpaceItem](<uibarbuttonitem/fixedspace().md>)。

示例在 `CustomButtonGroupsViewController` 中演示了这一做法。默认情况下，`shareBarButton` 和 `infoBarButton` 共享一个玻璃背景，因为它们都是带图片的按钮。示例在两者之间添加了一个 [+ fixedSpaceItem](<uibarbuttonitem/fixedspace().md>)，让它们各自拥有独立的玻璃背景：

```swift
navigationItem.rightBarButtonItems = [doneBarButton,
                                      shareBarButton,
                                      .fixedSpace(0),
                                      infoBarButton,
                                      selectBarButton]
```

### 自定义按钮标签与背景颜色

设置栏按钮项的着色颜色（tint color），为按钮的文本或图片提供颜色。示例在 `CustomButtonColorsViewController` 中演示了这一做法：

```swift
let shareBarButton = UIBarButtonItem(image: UIImage(systemName: "square.and.arrow.up"),
                                     style: .plain,
                                     target: nil,
                                     action: nil)
shareBarButton.tintColor = .systemOrange
```

要突出某个按钮，可以使用醒目按钮样式，让系统用着色颜色填充按钮的背景。示例演示了两种做法。第一种，把栏按钮项的 style 设为 [UIBarButtonItemStyleProminent](uibarbuttonitem/style-swift.enum/prominent.md)：

```swift
let infoBarButton = UIBarButtonItem(image: UIImage(systemName: "info.circle"),
                                    style: .plain,
                                    target: nil,
                                    action: nil)
infoBarButton.tintColor = .systemOrange
infoBarButton.style = .prominent
```

第二种，使用带系统默认图片与颜色的系统条目：

```swift
let doneBarButton = UIBarButtonItem(barButtonSystemItem: .done,
                                    target: nil,
                                    action: nil)
```

### 对使用弹性间距的工具栏条目分组

当你使用弹性间距栏按钮项让工具栏中的按钮均匀分布时，系统会在各弹性间距之间提供独立的玻璃背景。在 `CustomToolbarLayoutViewController` 中，示例展示了如何让所有按钮共享同一个玻璃背景：先用 [hidesSharedBackground](uibarbuttonitem/hidessharedbackground.md) 配置弹性间距：

```swift
let flexibleSpace = UIBarButtonItem.flexibleSpace()
flexibleSpace.hidesSharedBackground = false
```

然后，示例使用配置好的弹性间距来分布按钮：

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

当你使用 [UISearchController](uisearchcontroller.md) 和导览控制器的工具栏时，系统提供了一种内建方法把搜索集成到你的 App 中。示例在 `ToolbarSystemSearchViewController` 中演示了如何完成这种集成。

首先，示例实例化一个搜索控制器：

```swift
searchController = UISearchController(searchResultsController: SearchResultsViewController())
```

然后，示例告诉导览项使用它刚刚实例化的搜索控制器：

```swift
navigationItem.searchController = searchController
```

最后，示例把导览项的 [searchBarPlacementBarButtonItem](uinavigationitem/searchbarplacementbarbuttonitem.md) 加到工具栏按钮中：

```swift
toolbarItems = [
    .init(image: UIImage(systemName: "location")),
    .init(image: UIImage(systemName: "number")),
    .init(image: UIImage(systemName: "camera")),
    flexibleSpace,
    navigationItem.searchBarPlacementBarButtonItem
]
```

这些步骤完成后，系统会在工具栏中显示一个搜索按钮。当用户轻点搜索栏时，系统会显示一个搜索界面，用户可以在其中输入搜索参数并执行搜索。

### 自定义标题视图

另一种选择是配置导航栏使用一个 `UIView` 作为标题，例如用 `UISegmentedControl` 作为居中的自定义标题视图。

示例在 `CustomTitleViewController` 中展示了如何把分段控制设为标题视图：

```swift
self.navigationItem.titleView = segmentedControl
```

### 自定义标题与副标题

导航栏可以包含一个标题和一个副标题。示例在 `TitleSubtitleViewController` 中演示了设置标题与副标题：

```swift
navigationItem.title = "Title"
navigationItem.subtitle = "Subtitle"
```

除了用字符串设置标题和副标题，你还可以使用属性字符串或自定义视图。

### 自定义大号副标题视图

你可以设置自定义视图来代替标题、副标题、大标题或大标题下方的副标题。在 `LargeTitleViewController` 中，示例展示了一个按钮作为大标题下方自定义副标题视图的例子：

```swift
self.navigationController?.navigationBar.prefersLargeTitles = true

var subtitleConfiguration = UIButton.Configuration.plain()
subtitleConfiguration.title = "Subtitle Button"
subtitleConfiguration.baseForegroundColor = .systemBlue

let subtitleButton = UIButton(configuration: subtitleConfiguration)
navigationItem.largeSubtitleView = subtitleButton
```

### 修改导览提示

导航栏还可以在顶部包含一个提示（prompt）或一行文本。

示例在 `NavigationPromptViewController` 中演示了如何使用 `UINavigationItem` 的 [prompt](uinavigationitem/prompt.md) 属性在导航栏上方显示一行自定义文本：

```swift
navigationItem.prompt = NSLocalizedString("Navigation prompts appear at the top.", comment: "")
```

### 自定义返回按钮标题

长按返回按钮，用户可以在不同的栈层级之间快速切换。示例在 `MainViewController` 中向当前导览栈推入了 10 个视图控制器，以演示如何为栈中的每个视图控制器层级自定义返回按钮标题。

### 用图片自定义返回按钮

也可以只用一张图片作为返回按钮，不带任何返回按钮文本，也不带通常出现在返回按钮旁边的返回箭头。示例在 `CustomBackButtonDetailViewController` 中这样设置返回按钮的图片：

```swift
let backButtonBackgroundImage = UIImage(systemName: "list.bullet")
let backButton = UIBarButtonItem(image: backButtonBackgroundImage,
                                 style: .plain,
                                 target: self,
                                 action: #selector(backButtonTapped(_:)))
navigationItem.leftBarButtonItem = backButton
```

### 修改导航栏中的大标题

自定义导航栏的另一种选择是启用大标题显示模式，让它显示更大版本的标题。当视图控制器包含滚动视图时，系统会在可滚动内容的顶部显示大标题，并在用户开始滚动时以动画方式把标题收进导航栏。

下面的代码展示了示例如何在 `LargeTitleViewController` 中为导航栏启用大标题显示模式：

```swift
self.navigationController?.navigationBar.prefersLargeTitles = true
```

关于控制导航栏如何显示导览项标题的更多信息，参见 [largeTitleDisplayMode](uinavigationitem/largetitledisplaymode-swift.property.md)。

### 为栏按钮项附加菜单

菜单附件把 App 功能集中在一处，提供更广泛且便捷的访问。示例在 `BarButtonMenu` 中把一个 [UIMenu](uimenu.md) 附加到右侧的 `UIBarButtonItem` 控制上：

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

- [navigationBar](uinavigationcontroller/navigationbar.md) — 由导览控制器管理的导航栏。
- [- setNavigationBarHidden:animated:](<uinavigationcontroller/setnavigationbarhidden(__animated_).md>) — 设置导航栏是否隐藏。

## 下载

- [CustomizingYourAppsNavigationBar.zip](https://docs-assets.developer.apple.com/published/8b8c14d97eaf/CustomizingYourAppsNavigationBar.zip)
