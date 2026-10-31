---
title: 为你的 Mac App 选择用户界面 idiom
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/choosing-a-user-interface-idiom-for-your-mac-app
source_url: 'https://developer.apple.com/documentation/uikit/choosing-a-user-interface-idiom-for-your-mac-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/choosing-a-user-interface-idiom-for-your-mac-app.json'
content_hash: 'sha256:074dcdd97d935e39'
translated: true
---

> 导航： [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Mac Catalyst](mac-catalyst.md)

# 为你的 Mac App 选择用户界面 idiom

<sub>文章</sub>

在使用 Mac Catalyst 构建的 Mac App 中选择 iPad 或 Mac 用户界面 idiom。

## 概述

使用 Mac Catalyst 构建的 Mac App 可以在 [UIUserInterfaceIdiomPad](uiuserinterfaceidiom/pad.md) 或 [UIUserInterfaceIdiomMac](uiuserinterfaceidiom/mac.md) 用户界面 idiom 中运行。要选择 App 运行的 idiom，请在 Xcode 项目中打开 Mac Catalyst 后，从以下选项中选择：

- **Scale Interface to Match iPad** — 在 [UIUserInterfaceIdiomPad](uiuserinterfaceidiom/pad.md) idiom 中运行你的 App。选择此选项可快速将你的 iPad App 带到 Mac。
- **Optimize Interface for Mac** — 在 [UIUserInterfaceIdiomMac](uiuserinterfaceidiom/mac.md) idiom 中运行你的 App。选择此选项可显示外观和行为类似于 AppKit 中可用控件的控件。

> [!note] 注意
> 要了解如何在 Xcode 项目中打开 Mac Catalyst，参见 [Creating a Mac version of your iPad app](creating-a-mac-version-of-your-ipad-app.md)。

### 从 iPad idiom 开始

默认情况下，打开 Mac Catalyst 后，Xcode 会选择 Scale Interface to Match iPad。此选项提供了一种将你的 iPad App 带到 Mac 的简化方法。你的 Mac App 在 [UIUserInterfaceIdiomPad](uiuserinterfaceidiom/pad.md) idiom 中运行，这会告诉 macOS 将 App 的用户界面缩放以匹配 Mac 显示环境，同时保留 iPad 风格的外观和视图度量。

在测试 App 时，你可能会发现采用外观和行为类似于 AppKit 中控件的控件，或提供更清晰的文本，可以增强 App 的用户体验。如果是这种情况，通过选择 Optimize Interface for Mac 切换到 [UIUserInterfaceIdiomMac](uiuserinterfaceidiom/mac.md)。然而，选择此选项可能需要你对 App 进行额外的更改。

### 更新你的 App 以使用 Mac idiom

选择 Optimize Interface for Mac 意味着你的 Mac App 在 [UIUserInterfaceIdiomMac](uiuserinterfaceidiom/mac.md) 用户界面 idiom 中运行，这会改变 App 的界面。某些控件会更改其大小和外观，与它们交互的感觉与与 AppKit 控件交互相同。例如，[UIButton](uibutton.md) 与 [NSButton](../appkit/nsbutton.md) 看起来相同。

因为当用户界面 idiom 为 [UIUserInterfaceIdiomMac](uiuserinterfaceidiom/mac.md) 时，系统会适当设置控件大小，系统不再需要缩放 App 的界面以匹配 Mac 尺寸。屏幕点的大小与基于 AppKit 的 App 中的相同。然而，如果你的 App 有硬编码的尺寸或使用为 iPad 调整大小的图像，你可能需要更新 App 以适应尺寸差异。你可能还需要调整 Auto Layout 约束。

某些控件提供额外的设置，帮助你实现更 Mac 风格的外观。例如，当 idiom 为 [UIUserInterfaceIdiomMac](uiuserinterfaceidiom/mac.md) 时，[UISwitch](uiswitch.md) 可以通过将 [preferredStyle](uiswitch/preferredstyle.md) 设置为 [UISwitchStyleCheckbox](uiswitch/style-swift.enum/checkbox.md) 来显示为复选框。然后将 [title](uiswitch/title.md) 设置为复选框的文本。

```swift
let showFavoritesAtTop = UISwitch()
showFavoritesAtTop.preferredStyle = .checkbox
if traitCollection.userInterfaceIdiom == .mac {
    showFavoritesAtTop.title = "Always show favorite recipes at the top"
}
```

[UIPageControl](uipagecontrol.md) 对运行在 Mac idiom 中的 App 不可用。如果你尝试在视图中显示此控件，你的 App 会抛出异常。当用户界面 idiom 为 [UIUserInterfaceIdiomMac](uiuserinterfaceidiom/mac.md) 时，请用类似功能替换它。

### 确定当前用户界面 idiom

要确定你的 App 是否在 Mac idiom 中运行，请将 [userInterfaceIdiom](uitraitcollection/userinterfaceidiom.md) 属性的值与 [UIUserInterfaceIdiomMac](uiuserinterfaceidiom/mac.md) 比较。当比较结果为 [true](../swift/true.md) 时，你可以为 Mac 定制 App 的行为；例如，显示不同的子视图。

```swift
let childViewController: UIViewController
if traitCollection.userInterfaceIdiom == .mac {
    childViewController = MacOptimizedChildViewController()
} else {
    childViewController = ChildViewController()
}
addChild(childViewController)
childViewController.view.frame = view.bounds
view.addSubview(childViewController.view)
childViewController.didMove(toParent: self)
```

### 设置首选行为样式

采用 Mac idiom 时，某些控件（如 [UIButton](uibutton.md) 和 [UISlider](uislider.md)）看起来与它们的 AppKit 对应控件相同。然而，在某些情况下，你可能想在 App 中利用 Mac idiom，但保留控件的 iPad 外观和行为。例如，考虑一个显示带有自定义 thumb 图像的滑块的 iPad App。默认情况下，使用 Mac Catalyst 构建的 App 的 Mac 版本在用户界面 idiom 为 [UIUserInterfaceIdiomMac](uiuserinterfaceidiom/mac.md) 时会显示标准的 macOS 滑块。

为了提供在 iPad 和 Mac 版本的 App 中外观一致的滑块，请将滑块的 [preferredBehavioralStyle](uislider/preferredbehavioralstyle.md) 设置为 [UIBehavioralStylePad](uibehavioralstyle/pad.md)。此行为样式告诉滑块表现得如同用户界面 idiom 为 [UIUserInterfaceIdiomPad](uiuserinterfaceidiom/pad.md)，即使 App 使用的是 Mac idiom。

请记住，macOS 不会缩放使用 Mac idiom 的 App 的界面，因此即使首选行为样式为 [UIBehavioralStylePad](uibehavioralstyle/pad.md)，你可能仍需要更新 App 以适应尺寸差异。例如，带有自定义 thumb 图像的滑块可能需要与 iPad App 中使用的不同大小的图像用于 Mac App。

```swift
let slider = UISlider()
slider.minimumValue = 0
slider.maximumValue = 1
slider.value = 0.5
slider.preferredBehavioralStyle = .pad

if slider.traitCollection.userInterfaceIdiom == .mac {
    slider.setThumbImage(#imageLiteral(resourceName: "customSliderThumbMac"), for: .normal)
} else {
    slider.setThumbImage(#imageLiteral(resourceName: "customSliderThumb"), for: .normal)
}
```

当行为样式为 [UIBehavioralStyleMac](uibehavioralstyle/mac.md) 时，[UIButton](uibutton.md) 和 [UISlider](uislider.md) 的某些属性和方法在 Mac idiom 中不支持，调用它们会抛出异常；例如，为 [UIControlStateNormal](uicontrol/state-swift.struct/normal.md) 以外的任何控件状态设置按钮的标题或图像，以及设置滑块的 thumb 图像、最小或最大轨道图像、tint 颜色或值图像。然而，当控件的行为样式为 [UIBehavioralStylePad](uibehavioralstyle/pad.md) 时，这些属性和方法可在 Mac idiom 中使用。

### 提供不同的代码路径

即使你的 Mac App 在 [UIUserInterfaceIdiomPad](uiuserinterfaceidiom/pad.md) idiom 中运行，你可能仍需要更改 Mac App 的外观或行为。使用 `targetEnvironment()` 编译条件来根据目标环境选择不同的代码路径。

例如，如果你的 iPad App 在删除按钮旁边以 popover 显示删除项确认，但你希望在 Mac App 中将确认显示为提醒，请添加 `targetEnvironment()` 条件以确定提醒控制器的首选样式。

```swift
let deleteAction = UIAlertAction(title: "Delete", style: .destructive) { (action) in
    if dataStore.delete(recipe) {
        self.recipe = nil
    }
}

let cancelAction = UIAlertAction(title: "Cancel", style: .cancel, handler: nil)

#if targetEnvironment(macCatalyst)
let preferredStyle = UIAlertController.Style.alert
#else
let preferredStyle = UIAlertController.Style.actionSheet
#endif

let alert = UIAlertController(title: "Are you sure you want to delete \(recipe.title)?", message: nil, preferredStyle: preferredStyle)
alert.addAction(deleteAction)
alert.addAction(cancelAction)

if let popoverPresentationController = alert.popoverPresentationController {
    popoverPresentationController.barButtonItem = sender as? UIBarButtonItem
}

present(alert, animated: true, completion: nil)
```

## 另请参阅

### App support

- [Bring an iPad App to the Mac with Mac Catalyst](../tutorials/mac-catalyst.md) — 从与你的 iPad App 相同的代码库构建原生 Mac App。
- [Optimizing your iPad app for Mac](optimizing-your-ipad-app-for-mac.md) — 通过利用 macOS 中的系统功能，使你的 iPad App 更像 Mac App。
- [LSMinimumSystemVersion](../bundleresources/information-property-list/lsminimumsystemversion.md) — App 在 macOS 中运行所需的最低操作系统版本。
- [UIApplicationSupportsTabbedSceneCollection](../bundleresources/information-property-list/uiapplicationscenemanifest/uiapplicationsupportstabbedscenecollection.md) — 一个布尔值，指示使用 Mac Catalyst 构建的 App 是否支持自动标签模式。
