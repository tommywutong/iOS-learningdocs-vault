---
title: 指定你的 App 的启动画面
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/specifying-your-apps-launch-screen
source_url: 'https://developer.apple.com/documentation/xcode/specifying-your-apps-launch-screen'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/specifying-your-apps-launch-screen.json'
content_hash: 'sha256:1850168805bc1612'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Asset management](asset-management.md)

# 指定你的 App 的启动画面

<sub>文章</sub>

通过自定义启动画面，让你的 iOS App 的启动体验更快、响应更灵敏。

## 概述

每个 iOS App 都必须提供一个_启动画面_，即在你的 App 启动期间显示的画面。启动画面会在你的 App 启动时立即出现，并很快被 App 的第一个画面替换。

你可以通过以下两种方式之一，在 Xcode 项目中为你的 App 创建启动画面：

- 信息属性列表
- 用户界面文件

为了让 App 的启动体验尽可能无缝，请使用与你 App 第一个画面高度相似的基本视图来创建启动画面。
有关设计启动画面的准则，请参阅[《人机界面指南》](https://developer.apple.com/design/human-interface-guidelines/guidelines/overview)中的[启动](https://developer.apple.com/design/human-interface-guidelines/patterns/launching/)。

### 在信息属性列表中配置启动画面

对于用户界面简单的 App，使用 App 中的信息属性列表提供了一种快速、直接的方法来配置启动画面。

1. 在你目标的设置中，选择 Info 选项卡。
2. 在 Custom iOS Target Properties 区域中，展开 Launch Screen 键。
3. 点击添加按钮（+），输入 `UILaunchScreen`，然后按 Return 键，将启动画面键添加到属性列表中。如果 `UILaunchScreen` 键已经存在，你可以跳过此步骤。
4. 选中 `UILaunchScreen` 键，点击添加按钮，添加其他键以指定启动画面的配置选项。

![](../../../attachments/3417cef9027059fb04c67da2580e88ec/specifying-your-apps-launch-screen-2@2x.png)

<sub>名为「Launch Screen」的信息属性列表区域的屏幕截图。UILaunchScreen 键嵌套在 Launch Screen 下方。UILaunchScreen 下方嵌套着一个新行，用于指示在哪里添加其他键。</sub>

通过在 [UILaunchScreen](../bundleresources/information-property-list/uilaunchscreen.md) 的可用键中指定一组启动画面选项的组合，来定义启动画面的外观。

### 配置启动画面故事板

或者，你也可以在一个用户界面文件（即扩展名为 `.storyboard` 的文件）中配置启动画面。启动画面故事板包含基本的 UIKit 视图，并使用尺寸类别和 Auto Layout 约束来支持不同的设备尺寸和分辨率。

创建启动画面故事板时，请遵循以下准则：

- 只使用 UIKit 类。
- 使用单个根视图，该视图为 [UIView](../uikit/uiview.md) 或 [UIViewController](../uikit/uiviewcontroller.md) 对象。
- 不要与你的代码建立任何连接，例如，不要添加操作或出口。
- 不要使用已废弃的视图，比如 `UIWebView`。
- 不要使用任何自定义类。
- 不要使用运行时属性。

如果你是从故事板模板创建 iOS App 的，Xcode 会向你的项目添加一个名为 `LaunchScreen.storyboard` 的默认启动画面文件。编辑 `LaunchScreen.storyboard` 来配置你的启动画面。

如果你的项目不包含默认的启动画面文件，请添加一个启动画面文件，并在项目编辑器中为该目标设置启动画面文件。

1. 选择 File \> New \> File from Template。
2. 在 User Interface 下，选择 Launch Screen，然后点击 Next。
3. 为启动画面文件命名，选择一个位置，选择你想要添加该文件的目标，然后点击 Create。
4. 在你目标的设置中，选择 General 选项卡，找到「App Icons and Launch Screen」区域。
5. 从 Launch Screen File 弹出式菜单中，选择新的启动画面文件。

![](../../../attachments/0715ea8200fa2050b0bbea0b29c28d5f/specifying-your-apps-launch-screen-3@2x.png)

<sub>选中 General 选项卡的目标设置屏幕截图。App Icons and Launch Screen 区域中显示了一个名为 Launch Screen File 的字段，列出了要使用的启动画面故事板文件的名称。</sub>

## 另请参阅

### App 图标与启动画面

- [使用 Icon Composer 创建你的 App 图标](creating-your-app-icon-using-icon-composer.md) — 使用 Icon Composer 为你的 App 图标在不同平台和外观下进行样式设计。
- [配置你的 App 以使用备用 App 图标](configuring-your-app-to-use-alternate-app-icons.md) — 为你的 App 添加备用 App 图标，让用户选择要显示哪个图标。
- [使用素材目录配置你的 App 图标](configuring-your-app-icon.md) — 向素材目录添加 App 图标变体，用于在 App Store、主屏幕、设置和搜索结果等位置代表你的 App。
