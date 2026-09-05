---
title: 为你的 Mac App 选择用户界面惯用形式
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

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [Mac Catalyst](mac-catalyst.md)

# 为你的 Mac App 选择用户界面惯用形式

<sub>文章</sub>

在用 Mac Catalyst 构建的 Mac App 中，选择 iPad 或 Mac 用户界面惯用形式（idiom）。

## 概述

用 Mac Catalyst 构建的 Mac App 可以运行在 [UIUserInterfaceIdiomPad](uiuserinterfaceidiom/pad.md) 或 [UIUserInterfaceIdiomMac](uiuserinterfaceidiom/mac.md) 两种用户界面惯用形式下。要在你的 Xcode 项目中开启 Mac Catalyst 之后选择 App 的运行惯用形式，从以下选项中选择：

- **Scale Interface to Match iPad** — 让你的 App 以 [UIUserInterfaceIdiomPad](uiuserinterfaceidiom/pad.md) 惯用形式运行。想快速把你的 iPad App 带到 Mac 上，就选这个。
- **Optimize Interface for Mac** — 让你的 App 以 [UIUserInterfaceIdiomMac](uiuserinterfaceidiom/mac.md) 惯用形式运行。想让控制的外观和行为与 AppKit 中的一样，就选这个。

> [!note] 注意
> 要了解在 Xcode 项目中开启 Mac Catalyst 的更多信息，参见[创建你的 iPad App 的 Mac 版本](creating-a-mac-version-of-your-ipad-app.md)。

### 从 iPad 惯用形式开始

默认情况下，开启 Mac Catalyst 后 Xcode 会选中 Scale Interface to Match iPad。这个选项为把你的 iPad App 带到 Mac 上提供了一条捷径。你的 Mac App 以 [UIUserInterfaceIdiomPad](uiuserinterfaceidiom/pad.md) 惯用形式运行，它告诉 macOS 缩放 App 的用户界面以匹配 Mac 的显示环境，同时保留 iPad 风格的外观与视图度量。

测试你的 App 时，你可能会发现采用外观和行为与 AppKit 一致的控制、或提供更清晰的文本，能提升 App 的用户体验。如果是这样，选择 Optimize Interface for Mac 切换到 [UIUserInterfaceIdiomMac](uiuserinterfaceidiom/mac.md)。不过，选择这个选项可能需要你对 App 做额外的修改。

### 更新你的 App 以使用 Mac 惯用形式

选择 Optimize Interface for Mac 意味着你的 Mac App 以 [UIUserInterfaceIdiomMac](uiuserinterfaceidiom/mac.md) 用户界面惯用形式运行，这会改变你的 App 的界面。一些控制会改变大小和外观，与它们交互的感受和与 AppKit 控制交互完全相同。例如，[UIButton](uibutton.md) 看起来与 [NSButton](../appkit/nsbutton.md) 一模一样。

由于用户界面惯用形式为 [UIUserInterfaceIdiomMac](uiuserinterfaceidiom/mac.md) 时系统会恰当地设置控制的大小，系统不再需要缩放你的 App 的界面来匹配 Mac 的尺寸。屏幕点的大小与基于 AppKit 的 App 完全一致。但如果你的 App 有硬编码的尺寸，或使用了按 iPad 尺寸准备的图片，你可能需要更新 App 来适应尺寸差异。你还可能需要调整自动布局约束。

一些控制提供了额外设置，帮你实现更接近 Mac 的外观。例如，当惯用形式为 [UIUserInterfaceIdiomMac](uiuserinterfaceidiom/mac.md) 时，把 [preferredStyle](uiswitch/preferredstyle.md) 设为 [UISwitchStyleCheckbox](uiswitch/style-swift.enum/checkbox.md)，[UISwitch](uiswitch.md) 就能显示为复选框。再把 [title](uiswitch/title.md) 设为复选框的文本。

```swift
let showFavoritesAtTop = UISwitch()
showFavoritesAtTop.preferredStyle = .checkbox
if traitCollection.userInterfaceIdiom == .mac {
    showFavoritesAtTop.title = "Always show favorite recipes at the top"
}
```

[UIPageControl](uipagecontrol.md) 对以 Mac 惯用形式运行的 App 不可用。如果你试图在视图中显示这个控制，你的 App 会抛出异常。当用户界面惯用形式为 [UIUserInterfaceIdiomMac](uiuserinterfaceidiom/mac.md) 时，请用类似功能替换它。

### 判断当前的用户界面惯用形式

要判断你的 App 是否以 Mac 惯用形式运行，把 [userInterfaceIdiom](uitraitcollection/userinterfaceidiom.md) 属性的值与 [UIUserInterfaceIdiomMac](uiuserinterfaceidiom/mac.md) 比较。当比较结果为 [true](../swift/true.md) 时，你就可以为 Mac 调整 App 的行为，例如显示一个不同的子视图。

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

### 设置首选行为风格

采用 Mac 惯用形式后，[UIButton](uibutton.md) 和 [UISlider](uislider.md) 等一些控制的外观与它们的 AppKit 对应物完全一致。不过，有些情况下你可能既想利用 App 中的 Mac 惯用形式，又想保留某个控制的 iPad 外观和行为。举例来说，设想一个 iPad App 显示一个带自定义滑块图标（thumb image）的滑块。默认情况下，用 Mac Catalyst 构建的 App 的 Mac 版本，在用户界面惯用形式为 [UIUserInterfaceIdiomMac](uiuserinterfaceidiom/mac.md) 时会显示一个标准的 macOS 滑块。

要让滑块在 App 的 iPad 版本和 Mac 版本中外观一致，把滑块的 [preferredBehavioralStyle](uislider/preferredbehavioralstyle.md) 设为 [UIBehavioralStylePad](uibehavioralstyle/pad.md)。这个行为风格告诉滑块：即便 App 正在使用 Mac 惯用形式，也要表现得像用户界面惯用形式是 [UIUserInterfaceIdiomPad](uiuserinterfaceidiom/pad.md) 一样。

请记住，macOS 不会缩放使用 Mac 惯用形式的 App 的界面，所以即便首选行为风格是 [UIBehavioralStylePad](uibehavioralstyle/pad.md)，你也可能需要更新 App 以适应尺寸差异。例如，带自定义滑块图标的滑块，在 Mac App 中可能需要与 iPad App 中不同尺寸的图片。

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

当行为风格为 [UIBehavioralStyleMac](uibehavioralstyle/mac.md) 时，[UIButton](uibutton.md) 和 [UISlider](uislider.md) 的某些属性和方法在 Mac 惯用形式下不受支持，调用它们会抛出异常；例如，为按钮设置 [UIControlStateNormal](uicontrol/state-swift.struct/normal.md) 之外任何控制状态的标题或图片，以及设置滑块的滑块图标、最小或最大轨道图片、着色颜色或值图片。而当控制的行为风格为 [UIBehavioralStylePad](uibehavioralstyle/pad.md) 时，这些属性和方法在 Mac 惯用形式下都可正常使用。

### 提供不同的代码路径

即便你的 Mac App 以 [UIUserInterfaceIdiomPad](uiuserinterfaceidiom/pad.md) 惯用形式运行，你可能也需要改变 Mac App 的外观或行为。使用 `targetEnvironment()` 编译条件，根据目标环境选择不同的代码路径。

例如，如果你的 iPad App 在删除按钮旁边的弹出窗口中显示删除条目的确认信息，而你想在 Mac App 中把确认信息显示为警告框（alert），就添加一个 `targetEnvironment()` 条件来判断警告控制器的首选风格。

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

### App 支持

- [Bring an iPad App to the Mac with Mac Catalyst](../tutorials/mac-catalyst.md) — 用与你的 iPad App 相同的代码库构建原生 Mac App。
- [针对 Mac 优化你的 iPad App](optimizing-your-ipad-app-for-mac.md) — 借助 macOS 的系统特性，让你的 iPad App 更像 Mac App。
- [LSMinimumSystemVersion](../bundleresources/information-property-list/lsminimumsystemversion.md) — App 在 macOS 上运行所需的最低操作系统版本。
- [UIApplicationSupportsTabbedSceneCollection](../bundleresources/information-property-list/uiapplicationscenemanifest/uiapplicationsupportstabbedscenecollection.md) — 表示用 Mac Catalyst 构建的 App 是否支持自动标签页模式的布尔值。
