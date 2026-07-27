---
title: 'UIKit Catalog: 创建和自定视图与控制'
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 14.1+, iPadOS 14.1+, Mac Catalyst 14.1+, Xcode 13.1+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uikit-catalog-creating-and-customizing-views-and-controls
source_url: 'https://developer.apple.com/documentation/uikit/uikit-catalog-creating-and-customizing-views-and-controls'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikit-catalog-creating-and-customizing-views-and-controls.json'
content_hash: 'sha256:349bd670c4c07680'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Mac Catalyst](mac-catalyst.md)

# UIKit Catalog: 创建和自定视图与控制

<sub>示例代码</sub>

使用视图和控制自定你 App 的用户界面。

## 概述

本示例带你了解可以在 iOS App 中进行的几种自定。它是用 Mac Catalyst 构建的，这意味着该示例可以同时在 iOS 和 macOS 上运行。该示例使用拆分视图控制器架构来导览 UIKit 视图和控制。主视图控制器（`OutlineViewController`）显示可用的视图和控制。当你选择其中一项时，`OutlineViewController` 会显示与之关联的次要视图控制器。

每个次要视图控制器的名称都反映了其目标项。例如，`AlertControllerViewController` 类展示了如何使用 `UIAlertController` 对象。这一规则唯一的例外是 `UISearchBar` 和 `UIToolbar`；该示例在多个视图控制器中演示了这些 API，以说明它们的控制如何运作，以及如何对其进行自定。为了展示如何管理 storyboard 的复杂度，该 App 将所有视图控制器都放在一个单独的 storyboard 中，并在需要时才加载各个视图控制器。

该示例演示了以下视图和控制；其中几项会在下面的小节中被引用：

- [UIActivityIndicatorView](uiactivityindicatorview.md)
- [UIAlertController](uialertcontroller.md)
- [UIButton](uibutton.md)
- [PointerStyleProvider](uibutton/pointerstyleprovider-swift.typealias.md)
- [UIDatePicker](uidatepicker.md)
- [UIPickerView](uipickerview.md)
- [UIColorPickerViewController](uicolorpickerviewcontroller.md)
- [UIColorWell](uicolorwell.md)
- [UIFontPickerViewController](uifontpickerviewcontroller.md)
- [UIImagePickerController](uiimagepickercontroller.md)
- [UIImageView](uiimageview.md)
- [UIImageView with SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols/overview)
- [UIPageControl](uipagecontrol.md)
- [UIProgressView](uiprogressview.md)
- [UISearchBar](uisearchbar.md)
- [UISegmentedControl](uisegmentedcontrol.md)
- [UISlider](uislider.md)
- [UIStackView](uistackview.md)
- [UIStepper](uistepper.md)
- [UISwitch](uiswitch.md)
- [UITextField](uitextfield.md)
- [UITextFormattingCoordinator](uitextformattingcoordinator.md)
- [UITextView](uitextview.md)
- [UIToolbar](uitoolbar.md)
- [UIVisualEffect](uivisualeffect.md)
- [WKWebView](../webkit/wkwebview.md)

### 配置示例代码项目

在 Xcode 中，在 iOS-Mac target 的 Signing and Capabilities 标签页上选择你的开发团队。

### 用按钮配置自定按钮的外观

你可以使用 `UIButton.Configuration` 来自定 UIButton 的外观和行为。该示例使用了 `filled()` 配置，因此按钮以红色背景色绘制：

```swift
var config = UIButton.Configuration.filled()
config.background.backgroundColor = .systemRed
button.configuration = config
```

### 显示自定提醒

`AlertControllerViewController` 演示了几种从界面中显示模态提醒和操作表单的技术。所有提醒的配置流程都是类似的：

1. 确定要在提醒中显示的消息。
2. 创建并配置一个 `UIAlertController` 对象。
3. 为用户可能采取的操作添加处理程序。
4. 呈现该提醒控制器。

`showSimpleAlert` 函数使用 `NSLocalizedString` 函数以用户偏好的语言获取提醒消息。`showSimpleAlert` 函数使用这些字符串来创建并配置 `UIAlertController` 对象。虽然提醒中的按钮标题是 OK，但该示例使用了取消操作，以确保提醒控制器为该按钮应用正确的样式：

```swift
func showSimpleAlert() {
    let title = NSLocalizedString("A Short Title is Best", comment: "")
    let message = NSLocalizedString("A message needs to be a short, complete sentence.", comment: "")
    let cancelButtonTitle = NSLocalizedString("OK", comment: "")

    let alertController = UIAlertController(title: title, message: message, preferredStyle: .alert)

    // Create the action.
    let cancelAction = UIAlertAction(title: cancelButtonTitle, style: .cancel) { _ in
        Swift.debugPrint("The simple alert's cancel action occurred.")
    }

    // Add the action.
    alertController.addAction(cancelAction)

    present(alertController, animated: true, completion: nil)
}
```

### 自定滑块的外观

该示例演示了显示 `UISlider`（一种用于从连续取值范围中选择单个值的控制）的不同方式。通过为左侧轨道、右侧轨道和滑块滑钮分配可伸缩图像来自定滑块的外观。在本例中，轨道图像是可伸缩的，且宽度为一个像素。可以让轨道图像更宽以提供圆角，但要确保为这些图像的 `capInsets` 属性设置合适的值以容纳圆角。

`configureCustomSlider` 函数设置了一个自定滑块：

```swift
@available(iOS 15.0, *)
func configureCustomSlider(slider: UISlider) {
    /** To keep the look the same betwen iOS and macOS:
        For setMinimumTrackImage, setMaximumTrackImage, setThumbImage to work in Mac Catalyst, use UIBehavioralStyle as ".pad",
        Available in macOS 12 or later (Mac Catalyst 15.0 or later).
        Use this for controls that need to look the same between iOS and macOS.
    */
    if traitCollection.userInterfaceIdiom == .mac {
        slider.preferredBehavioralStyle = .pad
    }
    
    let leftTrackImage = UIImage(named: "slider_blue_track")
    slider.setMinimumTrackImage(leftTrackImage, for: .normal)

    let rightTrackImage = UIImage(named: "slider_green_track")
    slider.setMaximumTrackImage(rightTrackImage, for: .normal)

    // Set the sliding thumb image (normal and highlighted).
    //
    // For fun, choose a different image symbol configuraton for the thumb's image between macOS and iOS.
    var thumbImageConfig: UIImage.SymbolConfiguration
    if slider.traitCollection.userInterfaceIdiom == .mac {
        thumbImageConfig = UIImage.SymbolConfiguration(scale: .large)
    } else {
        thumbImageConfig = UIImage.SymbolConfiguration(pointSize: 30, weight: .heavy, scale: .large)
    }
    let thumbImage = UIImage(systemName: "circle.fill", withConfiguration: thumbImageConfig)
    slider.setThumbImage(thumbImage, for: .normal)
    
    let thumbImageHighlighted = UIImage(systemName: "circle", withConfiguration: thumbImageConfig)
    slider.setThumbImage(thumbImageHighlighted, for: .highlighted)

    // Set the rest of the slider's attributes.
    slider.minimumValue = 0
    slider.maximumValue = 100
    slider.isContinuous = false
    slider.value = 84

    slider.addTarget(self, action: #selector(SliderViewController.sliderValueDidChange(_:)), for: .valueChanged)
}
```

### 向界面中添加搜索栏

使用 `UISearchBar` 接收来自用户的搜索相关信息。有多种方式可以自定搜索栏的外观：

- 添加一个取消按钮。
- 添加一个书签按钮。
- 设置书签图像，包括正常和高亮两种状态。
- 更改应用到搜索栏关键元素上的强调色。
- 设置搜索栏的背景图像。

`configureSearchBar` 函数设置了一个自定搜索栏：

```swift
func configureSearchBar() {
    searchBar.showsCancelButton = true
    searchBar.showsBookmarkButton = true

    searchBar.tintColor = UIColor.systemPurple

    searchBar.backgroundImage = UIImage(named: "search_bar_background")

    // Set the bookmark image for both normal and highlighted states.
    let bookImage = UIImage(systemName: "bookmark")
    searchBar.setImage(bookImage, for: .bookmark, state: .normal)

    let bookFillImage = UIImage(systemName: "bookmark.fill")
    searchBar.setImage(bookFillImage, for: .bookmark, state: .highlighted)
}
```

### 自定工具栏的外观

该示例展示了如何自定 `UIToolbar`——一种沿界面底部边缘显示一个或多个按钮的特殊视图。通过确定工具栏的样式（黑色或默认）、半透明程度、强调色和背景色来自定工具栏。

`CustomToolbarViewController` 中的以下 `viewDidLoad` 函数设置了一个带强调色的工具栏：

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    // See the `UIBarStyle` enum for more styles, including `.Default`.
    toolbar.barStyle = .black
    toolbar.isTranslucent = false

    toolbar.tintColor = UIColor.systemGreen
    toolbar.backgroundColor = UIColor.systemBlue

    let toolbarButtonItems = [
        refreshBarButtonItem,
        flexibleSpaceBarButtonItem,
        actionBarButtonItem
    ]
    toolbar.setItems(toolbarButtonItems, animated: true)
}
```

`CustomToolbarViewController` 通过更改工具栏的背景图像演示了进一步的自定：

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    let toolbarBackgroundImage = UIImage(named: "toolbar_background")
    toolbar.setBackgroundImage(toolbarBackgroundImage, forToolbarPosition: .bottom, barMetrics: .default)

    let toolbarButtonItems = [
        customImageBarButtonItem,
        flexibleSpaceBarButtonItem,
        customBarButtonItem
    ]
    toolbar.setItems(toolbarButtonItems, animated: true)
}
```

### 添加页面控制界面

使用 `UIPageControl` 来构建 App 用户界面的结构。_页面控制_是一种特殊的控制，显示一排水平的圆点，每个圆点对应 App 文稿或其他数据模型实体中的一个页面。通过为所有页面指示圆点以及当前页面指示圆点设置强调色来自定页面控制。

`configurePageControl` 函数设置了一个自定的页面控制：

```swift
func configurePageControl() {
    // The total number of available pages is based on the number of available colors.
    pageControl.numberOfPages = colors.count
    pageControl.currentPage = 2

    pageControl.pageIndicatorTintColor = UIColor.systemGreen
    pageControl.currentPageIndicatorTintColor = UIColor.systemPurple
    
    pageControl.addTarget(self, action: #selector(PageControlViewController.pageControlValueDidChange), for: .valueChanged)
}
```

### 向控制中添加菜单

将菜单附加到 `UIButton` 和 `UIBarButtonItem` 等控制上。使用 [UIAction](uiaction.md) 类创建菜单，并通过设置 [UIMenu](uimenu.md) 属性将菜单附加到每个控制。

如下所示，将菜单附加到 `UIButton`：

```swift
button.menu = UIMenu(children: [
    UIAction(title: String(format: NSLocalizedString("ItemTitle", comment: ""), "1"),
             identifier: UIAction.Identifier(ButtonMenuActionIdentifiers.item1.rawValue),
             handler: menuHandler),
    UIAction(title: String(format: NSLocalizedString("ItemTitle", comment: ""), "2"),
             identifier: UIAction.Identifier(ButtonMenuActionIdentifiers.item2.rawValue),
             handler: menuHandler)
])

button.showsMenuAsPrimaryAction = true
```

如下所示，创建一个附带菜单的 `UIBarButtonItem`：

```swift
var customTitleBarButtonItem: UIBarButtonItem {
    let buttonMenu = UIMenu(title: "",
                            children: (1...5).map {
                               UIAction(title: "Option \($0)", handler: menuHandler)
                            })
    return UIBarButtonItem(image: UIImage(systemName: "list.number"), menu: buttonMenu)
}
```

### 为你的视图添加辅助功能支持

旁白及其他系统辅助功能技术使用视图和控制提供的信息，帮助所有用户导览内容。UIKit 视图内置了默认的辅助功能支持。通过提供自定的辅助功能信息来改善用户体验。

在这个 UIKitCatalog 示例中，多个视图控制器为其关联视图配置了 `accessibilityType` 和 `accessibilityLabel` 属性。选择器视图的列没有标签，因此选择器视图会向其委托询问相应的辅助功能信息：

```swift
func pickerView(_ pickerView: UIPickerView, accessibilityLabelForComponent component: Int) -> String? {
    
    switch ColorComponent(rawValue: component)! {
    case .red:
        return NSLocalizedString("Red color component value", comment: "")

    case .green:
        return NSLocalizedString("Green color component value", comment: "")

    case .blue:
        return NSLocalizedString("Blue color component value", comment: "")
    }
}
```

### 支持 Mac Catalyst

该示例 App 是用 Mac Catalyst 构建的，这意味着该示例可以同时在 iOS 和 Mac 上运行。这是通过在 Project Settings 中勾选 Mac 复选框实现的。有关 Mac Catalyst 工作原理的更多信息，请参阅 [Mac Catalyst](https://developer.apple.com/mac-catalyst/)。

当为 Mac Catalyst 构建时，该示例实现了以下效果：

- 针对 Mac 的界面优化。启用 Optimize Interface For the Mac 项目设置后，App 可以完全控制屏幕上的每一个像素，并且可以采用更多 Mac 特有的控制。为 Mac Catalyst 构建该示例，可以让 App 利用 macOS 中的系统特性。Show Designed for iPad Run Destination 选项让这个作为 iPad App 的示例，可以在搭载 Apple 芯片的 Mac 上原样运行。这需要 macOS 11 以及一台搭载 Apple 芯片的 Mac。
- 隐藏导览栏和标题栏。该示例 App 隐藏了它们，让 App 看起来更像一个 Mac App。它还通过使用 traitCollection 的 `userInterfaceIdiom` 更改了其他行为。
- 半透明背景。通过将拆分视图控制器的 `primaryBackgroundStyle` 设置为 `.sidebar`，主视图控制器或边栏会在其视图后方显示模糊的桌面。在 iOS 上运行时，设置该属性没有效果。

## 另请参阅

### 用户界面

- [Building and improving your app with Mac Catalyst](building-and-improving-your-app-with-mac-catalyst.md) — 通过支持原生控制、多个窗口、共享、打印、菜单和键盘快捷键，使用 Mac Catalyst 改进你的 iPadOS App。
- [Displaying a checkbox in your Mac app built with Mac Catalyst](displaying-a-checkbox-in-your-mac-app-built-with-mac-catalyst.md) — 当你的 App 在 Mac 用户界面习惯用法下运行时，将切换控制呈现为 Mac 风格的复选框。
- [Removing the title bar in your Mac app built with Mac Catalyst](removing-the-title-bar-in-your-mac-app-built-with-mac-catalyst.md) — 通过移除标题栏来显示铺满窗口整个高度的内容。
- [Toolbar](toolbar.md) — 在窗口标题栏下方、你的自定内容上方提供一处放置控制的空间。
- [Touch Bar](../appkit/touch-bar.md) — 在 Touch Bar 中显示交互式内容和控制。

## 下载

- [UIKitCatalogCreatingAndCustomizingViewsAndControls.zip](https://docs-assets.developer.apple.com/published/b311f3c6a450/UIKitCatalogCreatingAndCustomizingViewsAndControls.zip)
