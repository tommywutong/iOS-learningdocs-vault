---
title: 迁移到 UIKit 基于场景的生命周期
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle
source_url: 'https://developer.apple.com/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/transitioning-to-the-uikit-scene-based-life-cycle.json'
content_hash: 'sha256:71f242bf45c5ad3f'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [App and environment](app-and-environment.md)

# 迁移到 UIKit 基于场景的生命周期

<sub>文章</sub>

采用基于场景的生命周期，取代 UIKit 中的 App 委托生命周期。

## 概述

UIKit 基于场景的生命周期将 App 进程生命周期与 UI 生命周期分离开来，让 App 能够独立管理多个 UI 实例。例如，像文本编辑器这样基于文稿的 App，可以将每个打开的文稿显示在自己的场景中，让用户可以并排处理多个文稿。你的 App 进程只启动一次，由 [UIApplicationDelegate](uiapplicationdelegate.md) 处理，但每一块可见的 UI——每个_场景_——都拥有由 [UISceneDelegate](uiscenedelegate.md) 和 [UIWindowSceneDelegate](uiwindowscenedelegate.md) 协调的独立生命周期。[UISceneDelegate](uiscenedelegate.md) 处理适用于所有场景的基本生命周期事件，而 [UIWindowSceneDelegate](uiwindowscenedelegate.md) 负责窗口控制和几何变化等 UI 特有的事件。一个场景可以进入后台，而另一个场景保持活跃，系统可以创建、销毁和排列场景，而不会影响其他场景。

UIKit 将每个场景表示为一个 [UIWindowScene](uiwindowscene.md) 对象。对你 App 的代码而言，这意味着生命周期事件不再是全局发生的——它们按场景发生。保存状态或更新 UI 之类的任务，发生在场景层级而非 App 层级。

> [!important] 重要
> 采用基于场景的生命周期是必需的。从 iOS 27、iPadOS 27、Mac Catalyst 27、tvOS 27 和 visionOS 27 开始，使用最新 SDK 构建的 App 必须采用基于场景的生命周期，否则将无法启动。

有关配置场景支持的更多信息，请参阅[指定你 App 支持的场景](specifying-the-scenes-your-app-supports.md)。

从 iOS 18.4、iPadOS 18.4、Mac Catalyst 18.4、tvOS 18.4 和 visionOS 2.4 开始，UIKit 会为尚未迁移的 App 记录以下消息：

```other
This process does not adopt UIScene lifecycle. 
This will become an assert in a future version.
```

在 iOS 26、iPadOS 26、Mac Catalyst 26、tvOS 26 和 visionOS 26 中，消息变为：

```other
UIScene lifecycle will soon be required.
Failure to adopt will result in an assert in the future.
```

## 判断你的 App 是否需要迁移

如果你的 App 满足以下任一条件，就需要迁移到基于场景的生命周期：

- 你的信息属性列表中缺少 [UIApplicationSceneManifest](../bundleresources/information-property-list/uiapplicationscenemanifest.md) 键，或者该键没有指定任何配置。
- 你的 App 委托没有实现 [- application:configurationForConnectingSceneSession:options:](<uiapplicationdelegate/application(__configurationforconnecting_options_).md>)。

## 采用基于场景的生命周期

要配置你 App 的场景，请在你的信息属性列表中添加带有场景配置的 [UIApplicationSceneManifest](../bundleresources/information-property-list/uiapplicationscenemanifest.md) 键。如果你的 App 需要动态场景配置——例如根据用户活动自定场景，或处理不同的场景角色——请改为在你的 App 委托中实现 [- application:configurationForConnectingSceneSession:options:](<uiapplicationdelegate/application(__configurationforconnecting_options_).md>)。

### 为场景支持配置信息属性列表

在你的信息属性列表中添加带有场景配置的 [UIApplicationSceneManifest](../bundleresources/information-property-list/uiapplicationscenemanifest.md) 键：

1. 打开你的 Xcode 项目。
2. 选择你的 App target。
3. 前往你 App target 的 General 设置。
4. 在 Deployment Info 部分选择 “Scene manifest”。
5. 在信息属性列表中添加 [UIApplicationSceneManifest](../bundleresources/information-property-list/uiapplicationscenemanifest.md) 键。

例如：

```xml
<key>UIApplicationSceneManifest</key>
<dict>
    <key>UIApplicationSupportsMultipleScenes</key>
    <false/>
    <key>UISceneConfigurations</key>
    <dict>
        <key>UIWindowSceneSessionRoleApplication</key>
        <array>
            <dict>
                <key>UISceneConfigurationName</key>
                <string>Default Configuration</string>
                <key>UISceneDelegateClassName</key>
                <string>$(PRODUCT_MODULE_NAME).SceneDelegate</string>
                <key>UISceneStoryboardFile</key>
                <string>Main</string>
            </dict>
        </array>
    </dict>
</dict>
```

> [!note] 注意
> 支持多个场景是可选的，可能需要将你 App 的数据模型重构为场景特有的。在启用之前，先考虑你 App 的用户体验是否能从多个场景中受益。要支持多个场景，请将 [UIApplicationSupportsMultipleScenes](../bundleresources/information-property-list/uiapplicationscenemanifest/uiapplicationsupportsmultiplescenes.md) 设置为 `true`，并为每个 [UISceneConfiguration](uisceneconfiguration.md) 指定一个唯一的配置名称。

### 从你的 App 委托提供场景配置

如果你的 App 没有在信息属性列表中包含场景配置数据，或者需要动态场景配置——例如根据会话特有的数据加载不同的场景——请在你的 App 委托中实现 [- application:configurationForConnectingSceneSession:options:](<uiapplicationdelegate/application(__configurationforconnecting_options_).md>)：

```swift
@main
class AppDelegate: UIResponder, UIApplicationDelegate {
    func application(
        _ application: UIApplication,
        configurationForConnecting connectingSceneSession: UISceneSession,
        options: UIScene.ConnectionOptions
    ) -> UISceneConfiguration {

        // Each `UISceneConfiguration` must have a unique configuration name
        // that corresponds to an entry in the information property list scene manifest.
        let configurationName: String

        switch options.userActivities.first?.activityType {
        case UserActivity.GalleryOpenInspectorActivityType:
            // Create a photo inspector window scene.
            configurationName = "Inspector Configuration"
        default:
            // Create a default gallery window scene.
            configurationName = "Default Configuration"
        }

        return UISceneConfiguration(
            name: configurationName,
            sessionRole: connectingSceneSession.role
        )
    }
}
```

在此示例中，App 使用 [activityType](../foundation/nsuseractivity/activitytype.md) 属性来判断要创建哪个场景。有关为不同场景类型配置你的 App 的更多信息，请参阅[指定你 App 支持的场景](specifying-the-scenes-your-app-supports.md)。有关以编程方式创建多个窗口的信息，请参阅[在 iPad 上支持多个窗口](supporting-multiple-windows-on-ipad.md)。

### 配置你的窗口场景

UIKit 为每个场景实例创建一个 [UIWindowScene](uiwindowscene.md) 对象。在配置场景支持时，请指定 `UIWindowScene` 对象，而不是 [UIScene](uiscene.md) 对象。如果你的 App 为 CarPlay 采用了场景，请改用 [CPTemplateApplicationScene](../carplay/cptemplateapplicationscene.md)。要了解如何添加 CarPlay 场景，请参阅[在 CarPlay 中显示内容](../carplay/displaying-content-in-carplay.md)。

如果你从 storyboard 加载根视图控制器，请在信息属性列表场景清单中的 [UISceneConfigurations](../bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations.md) 键里包含该 storyboard 名称。系统会自动配置你的窗口场景和根视图控制器。

如果你以编程方式加载根视图控制器，请实现 [- scene:willConnectToSession:options:](<uiscenedelegate/scene(__willconnectto_options_).md>)，以创建一个 [UIWindow](uiwindow.md) 并将其与该场景关联：

```swift
import UIKit

class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    var window: UIWindow?

    func scene(
        _ scene: UIScene,
        willConnectTo session: UISceneSession,
        options connectionOptions: UIScene.ConnectionOptions
    ) {
        guard let windowScene = scene as? UIWindowScene else { return }

        window = UIWindow(windowScene: windowScene)
        window?.rootViewController = YourRootViewController()
        window?.makeKeyAndVisible()
    }
}
```

`SceneDelegate` 是一个符合 [UIWindowSceneDelegate](uiwindowscenedelegate.md) 的 [UIResponder](uiresponder.md) 子类。有关在启动时准备你 App 的更多信息，请参阅[响应你 App 的启动](responding-to-the-launch-of-your-app.md)。

## 迁移 App 生命周期逻辑

将你 App 现有的生命周期方法从 [UIApplicationDelegate](uiapplicationdelegate.md) 移动到 [UISceneDelegate](uiscenedelegate.md)：

| UIApplicationDelegate | UISceneDelegate |
|---|---|
| [- applicationDidBecomeActive:](<uiapplicationdelegate/applicationdidbecomeactive(__).md>) | [- sceneDidBecomeActive:](<uiscenedelegate/scenedidbecomeactive(__).md>) |
| [- applicationWillResignActive:](<uiapplicationdelegate/applicationwillresignactive(__).md>) | [- sceneWillResignActive:](<uiscenedelegate/scenewillresignactive(__).md>) |
| [- applicationDidEnterBackground:](<uiapplicationdelegate/applicationdidenterbackground(__).md>) | [- sceneDidEnterBackground:](<uiscenedelegate/scenedidenterbackground(__).md>) |
| [- applicationWillEnterForeground:](<uiapplicationdelegate/applicationwillenterforeground(__).md>) | [- sceneWillEnterForeground:](<uiscenedelegate/scenewillenterforeground(__).md>) |

迁移后，在 iPad 上的 Full Screen Apps、Windowed Apps 和 Stage Manager 中测试你的 App。要了解如何响应状态转换，请参阅[管理你 App 的生命周期](managing-your-app-s-life-cycle.md)。

## 支持非交互式外接显示器场景

如果你的 App 不在外接显示器上呈现自定内容，你无需为这个场景角色配置任何内容。当外接显示器连接时，系统会镜像你 App 的主显示器；或者在已启用扩展显示的兼容 iPad 机型上，将你 App 的交互式窗口呈现到外接显示器上。

在 iOS 26 及更早版本中，系统会自动连接一个 [UIWindowSceneSessionRoleExternalDisplayNonInteractive](uiscenesession/role-swift.struct/windowexternaldisplaynoninteractive.md) 场景，你的 App 可以通过不为其提供内容来选择退出。从 iOS 27 开始，只有在你的 App 注册了一个_场景配件_后，才会接收到这个场景。场景配件声明了系统在相关功能可用时（例如通过线缆或 AirPlay 连接的外接显示器）代表你的 App 呈现的补充内容。你的 App 声明要提供哪些内容，系统决定何时何地呈现这些内容。由于该内容仅在有可用显示器时才会出现，请将你的 App 设计为在没有外接显示器的情况下也能完全正常运作。

如果你的 App 此前是通过在 [- application:configurationForConnectingSceneSession:options:](<uiapplicationdelegate/application(__configurationforconnecting_options_).md>) 或你的场景委托中检查所连接场景的角色，来为这个场景提供内容的，请移除该角色特有的逻辑，改为注册一个场景配件。你可以复用现有的场景委托作为该配件的委托类，也可以新建一个专用于外接显示器场景的委托。

在你 App 主界面中的某个视图控制器上注册该配件。选择那个其内容会被外接显示器补充的视图控制器：

```swift
class PlayerViewController: UIViewController {
    var displayRegistration: UISceneAccessoryRegistration?

    override func viewDidLoad() {
        super.viewDidLoad()

        // Describe the scene to present, including the delegate that attaches its window.
        let configuration = UISceneConfiguration()
        configuration.delegateClass = ExternalDisplaySceneDelegate.self

        // Register the accessory so the system can present this content on an external display.
        let accessory = UISceneAccessory.externalNonInteractive(sceneConfiguration: configuration)
        displayRegistration = registerSceneAccessory(accessory)
    }
}
```

当你的 App 呈现该视图控制器且有可用的外接显示器时，系统会连接该场景，并在你的委托上调用 [- scene:willConnectToSession:options:](<uiscenedelegate/scene(__willconnectto_options_).md>)。这个场景的内容会铺满整个屏幕。

有关在已连接显示器上呈现内容的更多信息，包括如何控制内容何时出现、响应显示器可用性变化，以及如何停止呈现内容，请参阅[在已连接显示器上呈现内容](presenting-content-on-a-connected-display.md)。

## 另请参阅

### 生命周期

- [Managing your app’s life cycle](managing-your-app-s-life-cycle.md) — 在你的 App 处于前台或后台时响应系统通知，并处理其他重要的系统相关事件。
- [Responding to the launch of your app](responding-to-the-launch-of-your-app.md) — 初始化你 App 的数据结构，为 App 运行做好准备，并响应系统在启动时提出的任何请求。
- [UIApplication](uiapplication.md) — 在 iOS 中运行的 App 的集中控制与协调点。
- [UIApplicationDelegate](uiapplicationdelegate.md) — 一组方法，用于管理你 App 的共享行为。
- [Scenes](scenes.md) — 同时管理你 App UI 的多个实例，并将资源导向到你 UI 相应的实例。
