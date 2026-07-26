---
title: 为 Mac 优化你的 iPad App
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/optimizing-your-ipad-app-for-mac
source_url: 'https://developer.apple.com/documentation/uikit/optimizing-your-ipad-app-for-mac'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/optimizing-your-ipad-app-for-mac.json'
content_hash: 'sha256:a7253ca457fa9dc2'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Mac Catalyst](mac-catalyst.md)

# 为 Mac 优化你的 iPad App

<sub>文章</sub>

利用 macOS 中的系统功能，让你的 iPad App 更像一个 Mac App。

## 概述

你的 iPad App 的 Mac 版本无需你付出任何努力，就能支持 macOS 中众多的系统功能，包括：

- 为你的 App 提供的默认菜单栏
- 对触控板、鼠标和键盘输入的支持
- 对窗口调整大小和全屏显示的支持
- Mac 风格的滚动条
- 复制粘贴支持
- 拖放支持
- 对系统 Touch Bar 控制的支持

不过，你也可以扩展你的 App，让它利用更多的系统功能。

> [!important] 重要
> 使用 Mac Catalyst 构建的 Mac App 只能使用标记为在 Mac Catalyst 中可用的 [AppKit](../appkit.md) API，例如 [NSToolbar](../appkit/nstoolbar.md) 和 [NSTouchBar](../appkit/nstouchbar.md)。Mac Catalyst 不支持访问不可用的 AppKit API。

### 添加菜单栏项目

你 App 的 Mac 版本自带一个标准菜单栏。使用 [UIMenuBuilder](uimenubuilder.md) 添加和移除菜单项目，即可对其进行自定。要了解更多信息，请参阅[向菜单栏和用户界面添加菜单与快捷键](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md)。

### 显示 Settings 窗口

Mac App 通常通过显示一个 Settings 窗口，让用户管理特定于该 App 的设置。用户通过依次选择 App 菜单和菜单栏中的 Settings 菜单项来查看这个窗口。如果你的 App 有一个 Settings bundle，系统会自动为你的 App 提供一个 Settings 窗口。要了解更多信息，请参阅[显示 Settings 窗口](displaying-a-settings-window.md)。

### 为主要视图控制器添加 Liquid Glass 背景

使用拆分视图控制器的 iPad App 在 macOS 上运行时，会获得 Mac 风格的垂直拆分视图。你可以通过为主要视图控制器的背景应用 Liquid Glass，帮助你的 iPad App 在 Mac 上看起来更自然。要做到这一点，请把你的拆分视图控制器的 [primaryBackgroundStyle](uisplitviewcontroller/primarybackgroundstyle.md) 设置为 [UISplitViewControllerBackgroundStyleSidebar](uisplitviewcontroller/backgroundstyle/sidebar.md)，如下面的代码所示。

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

    let splitViewController = window!.rootViewController as! UISplitViewController
    let navigationController = splitViewController.viewControllers[splitViewController.viewControllers.count - 1] as! UINavigationController
    navigationController.topViewController!.navigationItem.leftBarButtonItem = splitViewController.displayModeButtonItem
    
    // 为主要视图控制器添加 Liquid Glass 背景。
    splitViewController.primaryBackgroundStyle = .sidebar
    
    splitViewController.delegate = self
    
    return true
}
```

把你的拆分视图控制器的 [primaryBackgroundStyle](uisplitviewcontroller/primarybackgroundstyle.md) 设置为 [UISplitViewControllerBackgroundStyleNone](uisplitviewcontroller/backgroundstyle/none.md)，可以避免为主要视图控制器的背景设置样式。

### 检测视图中的指针

无论是选择文本栏还是移动窗口，Mac 用户都依靠指针来与 App 交互。当用户把指针移动到界面元素上时，某些元素应当改变外观。例如，Web 浏览器会在指针移动到某个链接上时高亮显示该链接。

要检测用户何时把指针移动到你 App 中的某个视图上，请为该视图添加一个 [UIHoverGestureRecognizer](uihovergesturerecognizer.md)。这会告知你的 App 指针何时进入或离开该视图，或是在其上方移动。

```swift
class ViewController: UIViewController {

    @IBOutlet var button: UIButton!

    override func viewDidLoad() {
        super.viewDidLoad()

        let hover = UIHoverGestureRecognizer(target: self, action: #selector(hovering(_:)))
        button.addGestureRecognizer(hover)
    }

    @objc
    func hovering(_ recognizer: UIHoverGestureRecognizer) {
        switch recognizer.state {
        case .began, .changed:
            button.titleLabel?.textColor = #colorLiteral(red: 1, green: 0, blue: 0, alpha: 1)
        case .ended:
            button.titleLabel?.textColor = UIColor.link
        default:
            break
        }
    }
}
```

## 另请参阅

### App support

- [Bring an iPad App to the Mac with Mac Catalyst](../tutorials/mac-catalyst.md) — 用与你的 iPad App 相同的代码库构建一个原生 Mac App。
- [Choosing a user interface idiom for your Mac app](choosing-a-user-interface-idiom-for-your-mac-app.md) — 在用 Mac Catalyst 构建的 Mac App 中，选择 iPad 或 Mac 的用户界面习惯用法。
- [LSMinimumSystemVersion](../bundleresources/information-property-list/lsminimumsystemversion.md) — App 在 macOS 上运行所需的最低操作系统版本。
- [UIApplicationSupportsTabbedSceneCollection](../bundleresources/information-property-list/uiapplicationscenemanifest/uiapplicationsupportstabbedscenecollection.md) — 一个布尔值，表示用 Mac Catalyst 构建的 App 是否支持自动标签模式。
