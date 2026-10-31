---
title: 响应 App 的启动
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/responding-to-the-launch-of-your-app
source_url: 'https://developer.apple.com/documentation/uikit/responding-to-the-launch-of-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/responding-to-the-launch-of-your-app.json'
content_hash: 'sha256:a2670b4ccb4268cf'
translated: true
---

> 导航： [Technologies](../technologies.md) · [UIKit](../uikit.md) · [App and environment](app-and-environment.md)

# 响应 App 的启动

初始化你的 App 的数据结构，准备运行你的 App，并响应系统在启动时的任何请求。

## 概述

当用户轻点主屏幕上的 App 图标时，系统会启动你的 App。如果你的 App 请求了特定事件，系统还可能在后台启动你的 App 以处理这些事件。

所有 App 都有关联的进程和至少一个场景，由 [UIApplication](uiapplication.md) 和 [UIScene](uiscene.md) 对象表示。App 还有一个 _App delegate 对象_——一个符合 [UIApplicationDelegate](uiapplicationdelegate.md) 协议的对象——它响应该进程内发生的重要事件。即使实现了场景生命周期的 App 也使用 App delegate 来管理诸如启动和终止等基本事件。在启动时，UIKit 会自动创建 [UIApplication](uiapplication.md) 对象和你的 App delegate。然后它会在连接到你的 App 的一个或多个场景之前，启动 App 的主事件循环。

### 提供启动 storyboard

当用户在设备上首次启动你的 App 时，系统会显示你的启动 storyboard，直到你的 App 准备好显示其 UI。显示启动 storyboard 可以让用户确信你的 App 已启动并且正在做某事。如果你的 App 快速初始化自身并准备好 UI，用户可能只会短暂看到你的启动 storyboard。

Xcode 项目会自动包含一个默认的启动 storyboard 供你自定义，必要时你可以添加更多启动 storyboard。要向项目添加新的启动 storyboard，请执行以下操作：

1. 在 Xcode 中打开你的项目。
2. 选择 File \> New \> File。
3. 向你的项目添加 Launch Screen 资源。

向你的启动 storyboard 添加视图，并使用 Auto Layout 约束来调整它们的大小和位置，以便适应底层环境。UIKit 会完全按照你提供的内容显示，并使用你的约束将视图适配到可用空间。有关设计指导，参见 [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/launching/)。

> [!important] 重要
> 不要为你的启动屏幕使用静态图片。在 iOS 14 及更高版本中，启动屏幕被限制为 25 MB。

### 初始化 App 的数据结构

将 App 的启动时初始化代码放在以下一个或两个方法中：

- [- application:willFinishLaunchingWithOptions:](<uiapplicationdelegate/application(__willfinishlaunchingwithoptions_).md>)
- [- application:didFinishLaunchingWithOptions:](<uiapplicationdelegate/application(__didfinishlaunchingwithoptions_).md>)

UIKit 在 App 启动周期的开始调用这些方法。使用它们来：

- 初始化 App 在各场景间使用的数据结构。
- 验证 App 具有运行所需的资源。
- 在 App 首次启动时执行任何一次性设置。例如，在可写目录中安装模板或用户可修改的文件。参见 [Performing one-time setup for your app](performing-one-time-setup-for-your-app.md)。
- 连接到 App 使用的任何关键服务。例如，如果你的 App 支持远程通知，连接到 Apple Push Notification 服务。
- 检查启动选项字典中关于 App 为何启动的信息。参见 [Determine why your app launched](responding-to-the-launch-of-your-app.md#Determine-why-your-app-launched)。

对于尚未采用场景生命周期的 App，UIKit 会在启动时自动加载你的默认用户界面。使用 [- application:didFinishLaunchingWithOptions:](<uiapplicationdelegate/application(__didfinishlaunchingwithoptions_).md>) 方法在该界面出现在屏幕上之前对其进行额外更改。例如，你可能安装不同的视图控制器，以反映用户上次使用 App 时所做操作。

### 将长时间运行的任务移出主线程

当用户启动你的 App 时，通过快速启动留下好印象。在 [- application:didFinishLaunchingWithOptions:](<uiapplicationdelegate/application(__didfinishlaunchingwithoptions_).md>)、[- application:willFinishLaunchingWithOptions:](<uiapplicationdelegate/application(__willfinishlaunchingwithoptions_).md>) 或 [- scene:willConnectToSession:options:](<uiscenedelegate/scene(__willconnectto_options_).md>) 中执行长时间运行的任务，可能会让用户觉得你的 App 响应迟缓。快速返回对于启动到后台也很重要，因为系统会限制 App 的后台执行时间。

将对 App 初始化不关键的任务移出启动时序。例如：

- 推迟初始化 App 不会立即需要的功能。
- 将重要的长时间运行任务移出 App 的主线程。例如，在全局 dispatch 队列上异步运行它们，或在 [Task](../swift/task.md) 中运行。

### 确定场景为何连接

当 UIKit 连接到你的 App 中的场景时，它会传递一个 [ConnectionOptions](uiscene/connectionoptions.md) 对象，其中包含关于 UIKit 为何连接到该场景的信息。例如，这可能表示用户请求你的 App 打开一个 [URL](../foundation/url.md)，你可以使用它来显示与 `URL` 中提供的信息相关的屏幕。

以下代码展示如何检查场景连接选项中包含查询项信息的 `URL`：

```swift
class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
        
        // Confirm the scene is a window scene in iOS or iPadOS. 
        guard let _ = (scene as? UIWindowScene) else { return }
        
        // Check if the scene connection options include a URL,
        // and whether the URL has query items.
        guard let linkedUrl = connectionOptions.urlContexts.first?.url,
              let linkedComponents = URLComponents(url: linkedUrl, resolvingAgainstBaseURL: false),
              let queryItems = linkedComponents.queryItems,
              !queryItems.isEmpty else {
            return
        }
        
        // Check and handle the URL and query items here.
    }
    // Other methods…
}
```

### 确定 App 为何启动

当 UIKit 启动你的 App 时，它会调用 [- application:willFinishLaunchingWithOptions:](<uiapplicationdelegate/application(__willfinishlaunchingwithoptions_).md>) 和 [- application:didFinishLaunchingWithOptions:](<uiapplicationdelegate/application(__didfinishlaunchingwithoptions_).md>) 方法，以指示它已到达 App 启动过程中的这些点。如果你的 App 尚未实现场景生命周期，UIKit 会向这些方法传递一个启动选项字典，其中包含关于 App 为何启动的信息。该字典中的键指示需要立即执行的重要任务。例如，它们可能反映用户在别处开始并希望在你的 App 中继续的操作。始终检查启动选项字典的内容中是否有你期望的键，并对它们的存在做出适当响应。

> [!important] 重要
> 当你采用场景生命周期时，UIKit 会调用 [- application:willFinishLaunchingWithOptions:](<uiapplicationdelegate/application(__willfinishlaunchingwithoptions_).md>) 和 [- application:didFinishLaunchingWithOptions:](<uiapplicationdelegate/application(__didfinishlaunchingwithoptions_).md>) 方法，但不再向这些方法提供启动选项字典。请改为实现场景连接方法，以接收关于 App 启动和场景连接的详细信息。更多信息，参见 [Scenes](scenes.md)。

以下代码展示处理接收 `URL` 的 App 的 App delegate 方法。代码检查启动选项中是否有传入的 URL，以及该 `URL` 是否包含可用于配置 App 的查询项。如果没有，代码返回 `false`，表示你的 App 无法处理这些启动选项。

```swift
class AppDelegate: UIResponder, UIApplicationDelegate {
    
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        
        // Check if the launch options include a URL,
        // and whether the URL has query items.
        guard let linkedUrl = launchOptions?[.url] as? URL,
              let linkedComponents = URLComponents(url: linkedUrl, resolvingAgainstBaseURL: false),
              let queryItems = linkedComponents.queryItems,
              !queryItems.isEmpty else {
            return false
        }
        
        // Check whether your app can handle the URL and query
        // items here. Then return `true` if so, otherwise `false`.
        // ...
        
        return true
    }
    // Other methods…
}
```

系统不会包含某个键，除非你的 App 支持对应的功能。例如，系统不会为不支持远程通知的 App 包含 [UIApplicationLaunchOptionsRemoteNotificationKey](uiapplication/launchoptionskey/remotenotification.md) 键。

有关启动选项键列表以及如何处理它们的信息，参见 [LaunchOptionsKey](uiapplication/launchoptionskey.md)。

## 主题

### Launch time

- [About the app launch sequence](about-the-app-launch-sequence.md) — 了解系统在 App 启动时执行你的代码的顺序。
- [Performing one-time setup for your app](performing-one-time-setup-for-your-app.md) — 确保你的 App 环境正确配置。
- [Preserving your app’s UI across launches](preserving-your-app-s-ui-across-launches.md) — 在系统终止 App 后，将其恢复到之前的状态。

## 另请参阅

### Life cycle

- [Managing your app’s life cycle](managing-your-app-s-life-cycle.md) — 当你的 App 位于前台或后台时，响应系统通知，并处理其他重要的与系统相关的事件。
- [UIApplication](uiapplication.md) — 在 iOS 中运行的 App 的控制与协调中心点。
- [UIApplicationDelegate](uiapplicationdelegate.md) — 用于管理 App 共享行为的一组方法。
- [Scenes](scenes.md) — 同时管理你的 App UI 的多个实例，并将资源导向 UI 的适当实例。
- [Transitioning to the UIKit scene-based life cycle](transitioning-to-the-uikit-scene-based-life-cycle.md) — 采用基于场景的生命周期，以在 UIKit 中替代 App delegate 生命周期。
