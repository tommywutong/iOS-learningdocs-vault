---
title: 指定你的 App 支持的场景
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/specifying-the-scenes-your-app-supports
source_url: 'https://developer.apple.com/documentation/uikit/specifying-the-scenes-your-app-supports'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/specifying-the-scenes-your-app-supports.json'
content_hash: 'sha256:981c806dbc2ca8cd'
translated: true
---

> 导航： [Technologies](../technologies.md) · [UIKit](../uikit.md) · [App and environment](app-and-environment.md) · [Scenes](scenes.md)

# 指定你的 App 支持的场景

<sub>文章</sub>

告诉系统你的 App 的场景，包括你用于管理每个场景及其初始用户界面的对象。

## 概述

为你的 App 添加场景支持，以接收 UIKit 提供的场景特定生命周期事件，并使用场景对象与方法来管理用户界面。如果你在 App 的场景配置中启用对多窗口的支持，人们可以在支持该功能的平台上创建 App UI 的多个副本。对于 App UI 的每个副本，你使用场景对象来管理在屏幕上呈现 UI 的窗口、视图与视图控制器。

当你的 App 或用户请求新场景时，UIKit 会创建相应的场景对象并处理其初始设置。为此，UIKit 依赖于你提供的信息。在 App 的 Xcode 项目中，声明你的 App 支持的一种或多种场景类型，以及 App 用于管理这些场景的对象。你可以静态地在 App 目标 Xcode 的 Info 选项卡中完成，也可以在运行时动态完成。

### 在项目设置中启用场景支持

更新 App 的配置设置以选择加入场景：

1. 打开你的 Xcode 项目。
2. 导航到 App 目标的 Info 设置选项卡。
3. 在 Custom iOS Target Properties 部分添加 [UIApplicationSceneManifest](../bundleresources/information-property-list/uiapplicationscenemanifest.md) 字典键。

该键的值是一个字典，初始包含 [UIApplicationSupportsMultipleScenes](../bundleresources/information-property-list/uiapplicationscenemanifest/uiapplicationsupportsmultiplescenes.md) 键与 [UISceneConfigurations](../bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations.md) 键。

将 [UIApplicationSupportsMultipleScenes](../bundleresources/information-property-list/uiapplicationscenemanifest/uiapplicationsupportsmultiplescenes.md) 键的值设置为 [true](../swift/true.md)，以告诉系统你的 App 是否支持多个同时存在的场景；若你希望一次只显示一个场景，则设置为 [false](../swift/false.md)。支持多个场景需要你做额外的工作，以确保场景之间不会相互干扰。例如，如果场景使用相同共享数据结构，它们必须协调对这些结构的访问，以保持 App 数据的完整性。

### 配置每个场景的详细信息

UIKit 使用你提供的信息来处理 App 场景的创建。提供此信息的最简单方式是在 App 的 Info 设置中：

1. 打开 Xcode 项目并导航到 App 目标的 Info 设置选项卡。
2. 展开 Application Scene Manifest 条目。该条目对应 [UIApplicationSceneManifest](../bundleresources/information-property-list/uiapplicationscenemanifest.md) 键。如果它不存在，请按 [Enable scene support in your project settings](specifying-the-scenes-your-app-supports.md#Enable-scene-support-in-your-project-settings) 中的描述添加它。
3. 在 Scene Configuration 条目中，点击 Add (+) 按钮。
4. 选择 Window Application Session Role，向 App 添加主场景。
5. 在提供的条目中填写场景详细信息。

大多数 App 只需要一个主场景，但你可以添加多个场景并分别进行配置。例如，你可能包含第二个场景专门用于显示与通知相关的内容。UIKit 对每个场景需要以下信息：

- 场景的类名，即 [UIWindowScene](uiwindowscene.md)。
- App 用于管理该场景的自定委托对象的类名。该类必须遵循 [UIWindowSceneDelegate](uiwindowscenedelegate.md) 协议。
- 一个 App 内部用于标识该场景的唯一名称。
- 包含该场景初始 UI 的 storyboard 名称。请指定名称，但不要包含 `.storyboard` 文件扩展名。

有关如何配置场景的更多信息，请参阅 [UISceneConfigurations](../bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations.md)。

### 为场景创建界面

你使用 storyboard 指定场景的 UI。你分配给 [UISceneStoryboardFile](../bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uiscenestoryboardfile.md) 键的 storyboard 包含你想要为场景显示的初始视图控制器。除了创建场景对象外，UIKit 还会自动为你的场景创建一个窗口，并将 storyboard 中的初始视图控制器安装到其中。你可以使用 [UIWindowSceneDelegate](uiwindowscenedelegate.md) 对象的方法以编程方式替换该视图控制器。

> [!important] 重要
> 不要忘记在 storyboard 中指定初始视图控制器。UIKit 在配置 UI 时依赖该视图控制器的存在。

### 动态更改场景的配置

在实际创建场景对象之前，UIKit 会调用 App 委托的 [- application:configurationForConnectingSceneSession:options:](<uiapplicationdelegate/application(__configurationforconnecting_options_).md>) 方法，让你更改与场景相关的详细信息。你可以使用此方法根据 UIKit 提供的选项调整场景配置。例如，当系统向你的场景传递通知响应时，你可能会指定一个包含与通知相关界面的不同 storyboard。

如果你不实现或动态配置场景，UIKit 会使用 App 的 `Info.plist` 文件中的信息来创建场景。

### 采用基于场景的生命周期语义

添加场景支持会更改 App 响应生命周期事件的方式。在不使用场景生命周期对象的 App 中，App 委托对象处理转换到前台或后台。当你向 App 添加场景支持后，UIKit 会将该职责转移给场景委托对象。场景生命周期相互独立，也独立于 App 本身，因此你的场景委托对象必须处理这些转换。

有关如何处理生命周期事件的信息，请参阅 [Managing your app’s life cycle](managing-your-app-s-life-cycle.md)。

## 另请参阅

### 配置

- [UIApplicationSceneManifest](../bundleresources/information-property-list/uiapplicationscenemanifest.md) — 关于 App 基于场景的生命周期支持的信息。
- [UISceneConfiguration](uisceneconfiguration.md) — 关于 UIKit 在创建特定场景时使用的对象与 storyboard 的信息。
- [UISceneSession](uiscenesession.md) — 一个包含 App 某个场景信息的对象。
