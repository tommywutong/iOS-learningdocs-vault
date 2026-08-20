---
title: 'SwiftUI App 生命周期：ScenePhase 与 AppDelegate 适配器的问题'
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2024/06/29/swiftui-scene-phase/'
original_language: en
published: 2024-06-29
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ffa11c9078aa13d2'
translated: true
---

> 原文：[SwiftUI app lifecycle: issues with ScenePhase and using AppDelegate adaptors](https://www.jessesquires.com/blog/2024/06/29/swiftui-scene-phase/)　·　Jesse Squires

SwiftUI 在 iOS 14 和 macOS 11 中引入了 [`ScenePhase`](https://developer.apple.com/documentation/swiftui/scenephase) API。这是 SwiftUI 处理应用程序生命周期事件（application lifecycle events）的方案。同时，SwiftUI 还为 iOS 引入了 [`UIApplicationDelegateAdaptor`](https://developer.apple.com/documentation/swiftui/uiapplicationdelegateadaptor)，为 macOS 引入了 [`NSApplicationDelegateAdaptor`](https://developer.apple.com/documentation/swiftui/nsapplicationdelegateadaptor)，它们允许你在两个平台上提供一个 `AppDelegate`，以接收额外的应用程序生命周期事件以及当时 SwiftUI 缺失的其他事件。遗憾的是，其中许多应用程序事件 API 仍然缺失，而且 `ScenePhase` 存在大量错误（或至少是意外行为）。

### `ScenePhase` 事件（和视图生命周期事件）的局限性

`ScenePhase` 的问题在于它过于局限，只有 3 种状态：`active`、`inactive` 和 `background`。在理想情况下，应用程序**不一定**需要知道它是首次启动还是即将被终止。但在实践中，这些都是极其相关且重要的应用程序事件。在很多场景下，区分首次（或“冷”）启动和仅仅返回活跃状态是非常有用的。同样，也有充分的理由区别对待后台状态和终止。

我认为 `ScenePhase` 应该扩展以包含 `didLaunch` 和 `willTerminate` 事件，因为试图推断这些状态是繁琐且容易出错的，即使不是完全不可能。或者更好的是，我真正想要的是一个独立的 `AppPhase` API，允许你将应用程序级别的生命周期事件与窗口场景（window scenes）分开处理。

“场景”这个概念实际上核心在于**窗口**，而不是**整个应用程序**，这也是该 API 部分问题的根源。场景阶段与应用程序窗口的生命周期相关并为其建模。碰巧在 iOS 上，你的 App 通常只有一个窗口，因此 `ScenePhase` API 在该平台上更合适——事实上，它在 iOS 上的表现也确实更好。（是的，iPadOS 现在可以有多个窗口，但我们不要陷入那个混乱的局面。）不同平台之间的差异使得使用 `ScenePhase` 更加困难，因为感觉 SwiftUI 试图在所有平台上强制推行一个统一的模型，尽管它们的范式存在关键差异。

`ScenePhase` [文档](https://developer.apple.com/documentation/swiftui/scenephase/background)指出，你*“应当预期进入后台阶段的 App 会被终止。”* 这很遗憾，因为用户有可能（而且可能很常见）在 App 间切换并迅速返回你的 App。如果临时进入后台和完全终止之间没有区别，那么你的 App 最终可能会做大量不必要的拆解和重新设置工作。如下文所示，这对 macOS App 来说实际上是一个糟糕的建议。

UIKit 和 AppKit 在这 5 个主要事件之上都提供了额外的粒度，即“将要”和“已经发生”的 API。例如，`applicationWillResignActive()` 和 `applicationDidResignActive()`。我能理解简化 SwiftUI API 的动机，但在某些场景下，SwiftUI 过于局限，了解某个事件*即将发生*与了解某个事件*已经发生*是很有价值的。

同样的局限性也存在于 SwiftUI 的[视图生命周期](https://developer.apple.com/documentation/swiftui/view-fundamentals#responding-to-view-life-cycle-updates)方法 [`onAppear()`](https://developer.apple.com/documentation/swiftui/view/onappear(perform:)) 和 [`onDisappear()`](https://developer.apple.com/documentation/swiftui/view/ondisappear(perform:)) 中——根据文档，这些方法更准确的命名应该是 `willAppear()` 和 `didDisappear()`。`onAppear()` 在视图出现*之前*被调用，而 `onDisappear()` 在视图消失*之后*被调用，这既不一致又令人困惑。

### `ScenePhase` 的 Bug 和怪异行为

除了过于局限之外，SwiftUI 中的 `ScenePhase` 还存在许多错误。也许其中一些行为是设计使然，但如果是的话，那肯定是出乎意料的。

下面是一个 `ScenePhase` 的最小化实现示例。请注意，此代码片段会打印 `scenePhase` 所有变化的结果，以便你观察正在发生的事情。

```
@main
struct MyApp: App {
    @Environment(\.scenePhase) var scenePhase

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .onChange(of: scenePhase, initial: true) { oldValue, newValue in
            print("ScenePhase: \(oldValue) -> \(newValue)")
        }
    }
}
```

#### 在 iOS 上的行为

在 iOS 上，`onChange(of:)` 的表现基本符合预期。以下是一些常见场景及相关场景阶段过渡：

- 初始启动 App：`inactive` \> `active`。
- 进入后台：`active` \> `inactive` \> `background`。
- 返回前台：`background` \> `inactive` \> `active`。
- 临时后台（例如切换控制中心）：在 `active` 和 `inactive` 之间切换。
- App 终止：如果当前为 `active`，则 `inactive` \> `background`。值得注意的是，如果 App 已经在后台，你强制退出它，则不会发生任何场景阶段过渡。这意味着你必须将所有 `background` 事件视为 App 正在被终止。如上所述，这在所有场景中并非最优。

一个行为上的怪癖取决于你是否选择接收初始值，即向 `initial:` 参数传递 `true` 或 `false`。如果你传递 `true`，那么 `ScenePhase` 的第一个 `onChange(of:)` 事件是从 `inactive` 到 `inactive`，然后你才会收到过渡到 `active` 的更新。

出乎意料的是，主视图会在你的 App 收到场景阶段变化**之前**收到 `onAppear()`。在上面的示例中，就是 `ContentView`。这就像在你的根视图控制器（root view controller）收到 `viewWillAppear()` **之前**，先收到了 `application(_:didFinishLaunchingWithOptions:)` 被调用。这个事件序列对我来说毫无意义，并引发了关于如何在 SwiftUI 中准确地架构你的 App 启动流程的担忧。

上面稀疏的 `ScenePhase` 过渡与 `UIApplicationDelegate` 提供的丰富且粒度分明的事件形成了鲜明对比。

#### 在 macOS 上的行为

在 macOS 上，`onChange(of:)` 的行为非常不同且非常出乎意料。以下是类似于上面的一组场景及相关场景阶段过渡：

- 初始启动 App：`active` \> `active`。（什么？哈哈）
- 进入后台（使另一个应用程序置于最前并激活）：**无事件**。

    - 返回前台：**无事件**。
- 进入后台（通过隐藏应用程序，cmd-H）：`active` \> `background`。

    - 返回前台：`background` \> `active`。
- 关闭主窗口（但保持应用程序运行）：无场景阶段事件。但你会收到主视图的 `onDisappear()`。
- App 终止（通过 cmd-Q）：**无事件**。

如上所述，`ScenePhase` [文档](https://developer.apple.com/documentation/swiftui/scenephase/background)指出，你*“应当预期进入后台阶段的 App 会被终止。”* 基于上面列出的过渡，这对 Mac App 来说是一个可怕的假设。隐藏应用程序（cmd-H）是我发现的在 macOS 上触发 `background` 场景阶段的唯一方法。当用户只是隐藏你的 App 时就准备终止，这毫无意义。那将会是多么糟糕的用户体验！

如果你在 macOS 上向 `initial:` 参数传递 `false`，你将不会收到任何初始场景阶段变化。

在我的测试中，我从未能让一个 macOS App 过渡到 `inactive` 场景阶段。不清楚这是设计使然，还是一个错误。看起来像一个错误。

与 iOS 不同，macOS 会以正确的顺序为主视图接收 `onAppear()`。也就是说，场景阶段先变为 `active`，_然后_ App 为主视图接收 `onAppear()`。但出乎意料的是，在 macOS 上隐藏应用程序时，你_不会_收到 `onDisappear()` 事件。只有在关闭窗口时才会收到 `onDisappear()`，并且值得注意的是，_没有_场景阶段事件发生。

如果不明白的话，在需要访问应用程序生命周期事件甚至可靠的 App 窗口生命周期事件的 macOS 应用程序中，实际上不可能完全依赖 `ScenePhase`。在 macOS 上，`ScenePhase` 事件完全不够用，并且与 `NSApplicationDelegate` 以及当然还有 [`NSWindowDelegate`](https://developer.apple.com/documentation/appkit/nswindowdelegate) 提供的丰富且粒度分明的事件形成了更加鲜明的对比。

### App Delegate 适配器不推荐使用

尽管我上面列出的 API 存在诸多缺陷和不可靠的行为，但 iOS 上的 [`UIApplicationDelegateAdaptor`](https://developer.apple.com/documentation/swiftui/uiapplicationdelegateadaptor) 和 macOS 上的 [`NSApplicationDelegateAdaptor`](https://developer.apple.com/documentation/swiftui/nsapplicationdelegateadaptor) 的文档都_不推荐_使用它们，并带有一个大大的可怕警告：

> **重要**
> 
> 尽可能在不使用 App Delegate 的情况下管理 App 的生命周期事件。例如，优先处理 `ScenePhase` 的变化，而不是依赖委托回调……

这很有趣，尤其是在 macOS 上，`ScenePhase` 实际上根本无法工作，完全无法替代委托回调。根据我的经验，在这两个平台上（主要是 macOS），如果你需要可靠且粒度分明的应用程序生命周期事件，你必须使用 App Delegate。

### 使用 App Delegate 适配器（及其问题）

如果你想在 SwiftUI _之外_响应应用程序生命周期事件，你可以提供一个 App Delegate。首先，你需要在你的 SwiftUI App 中创建这些属性。

```
#if canImport(AppKit)
@NSApplicationDelegateAdaptor var appDelegate: NSAppDelegate
#endif

#if canImport(UIKit)
@UIApplicationDelegateAdaptor var appDelegate: UIAppDelegate
#endif
```

然后你可以为 iOS 实现一个 `AppDelegate`：

```
import UIKit

final class UIAppDelegate: NSObject, UIApplicationDelegate {
    var window: UIWindow?

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
        print(#function)
        return true
    }

    func applicationDidBecomeActive(_ application: UIApplication) {
        print(#function)
    }

    func applicationWillResignActive(_ application: UIApplication) {
        print(#function)
    }

    func applicationDidEnterBackground(_ application: UIApplication) {
        print(#function)
    }

    func applicationWillEnterForeground(_ application: UIApplication) {
        print(#function)
    }

    func applicationWillTerminate(_ application: UIApplication) {
        print(#function)
    }
}
```

你也可以为 macOS 实现一个 `AppDelegate`：

```
import AppKit

final class NSAppDelegate: NSObject, NSApplicationDelegate {

    func applicationWillFinishLaunching(_ notification: Notification) {
        print(#function)
    }

    func applicationDidFinishLaunching(_ notification: Notification) {
        print(#function)
    }

    func applicationWillHide(_ notification: Notification) {
        print(#function)
    }

    func applicationDidHide(_ notification: Notification) {
        print(#function)
    }

    func applicationDidBecomeActive(_ notification: Notification) {
        print(#function)
    }

    func applicationWillResignActive(_ notification: Notification) {
        print(#function)
    }

    func applicationDidResignActive(_ notification: Notification) {
        print(#function)
    }

    func applicationWillTerminate(_ notification: Notification) {
        print(#function)
    }
}
```

专业提示：因为 App Delegate 被定义为协议，你可以创建一个同时遵循这两个协议的单一类。这可以成为在平台之间共享代码的好策略。

在 macOS 上，你会按预期收到所有 `NSApplicationDelegate` 回调。一切正常。与文档相反，我会_避免_在 macOS 上_完全_尝试使用 `ScenePhase`。

在 iOS 上，App Delegate 适配器则是另一回事。它们不会按我期望的方式工作。在上面 `UIApplicationDelegate` 中定义的所有回调中，只有 `application(_:didFinishLaunchingWithOptions:)` 和 `applicationWillTerminate(_:)` 会在 SwiftUI App 中被调用。即使你已在 iOS 上通过为 [`UIApplicationSceneManifest`](https://developer.apple.com/documentation/bundleresources/information_property_list/uiapplicationscenemanifest) 提供正确的 plist 值而_选择退出_了多窗口支持，此行为仍然会发生。

如果你想要 iOS 上更细粒度的场景事件，你必须提供一个遵循 [`UIWindowSceneDelegate`](https://developer.apple.com/documentation/uikit/uiwindowscenedelegate) 的 `SceneDelegate` 类。你仍然可以[关闭多窗口](https://developer.apple.com/documentation/bundleresources/information_property_list/uiapplicationscenemanifest/uiapplicationsupportsmultiplescenes)，但你必须在你 App 的 plist 中提供场景配置和 `UISceneDelegateClassName`。只有这样，你才会收到相应的回调。

这是一个 plist 示例：

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
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
                </dict>
            </array>
        </dict>
    </dict>
</dict>
</plist>
```

以及一个更新后的 App Delegate，连同一个默认的场景 Delegate：

```
final class UIAppDelegate: NSObject, UIApplicationDelegate {

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
        print(#function)
        return true
    }

    func applicationWillTerminate(_ application: UIApplication) {
        print(#function)
    }

    // MARK: UISceneSession Lifecycle

    func application(_ application: UIApplication,
                     configurationForConnecting connectingSceneSession: UISceneSession,
                     options: UIScene.ConnectionOptions) -> UISceneConfiguration {
        print(#function)
        return UISceneConfiguration(name: "Default Configuration", sessionRole: connectingSceneSession.role)
    }

    func application(_ application: UIApplication, didDiscardSceneSessions sceneSessions: Set<UISceneSession>) {
        print(#function)
    }
}

final class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    var window: UIWindow?

    func scene(_ scene: UIScene,
               willConnectTo session: UISceneSession,
               options connectionOptions: UIScene.ConnectionOptions) {
        print(#function)
        guard let _ = (scene as? UIWindowScene) else { return }
    }

    func sceneDidDisconnect(_ scene: UIScene) {
        print(#function)
    }

    func sceneDidBecomeActive(_ scene: UIScene) {
        print(#function)
    }

    func sceneWillResignActive(_ scene: UIScene) {
        print(#function)
    }

    func sceneWillEnterForeground(_ scene: UIScene) {
        print(#function)
    }

    func sceneDidEnterBackground(_ scene: UIScene) {
        print(#function)
    }
}
```

注意，对于 SwiftUI，你需要做的只是像上面那样声明相同的 `@UIApplicationDelegateAdaptor`，所有这些就能生效。场景 Delegate 是从你的 App plist 中确定的，并且在设置 Delegate 方面，一切似乎“都能正常工作”。

### 结论

在上面的代码中，我使用了 `print(#function)` 将所有事件打印到控制台。这对于辨明所有这些 API 如何协同工作——或者有时，如何不工作——非常有启发性。如果你好奇，我鼓励你在示例 App 中将它们整合在一起，以实验和可视化回调发生的顺序。

一方面，`ScenePhase` API 可以在 iOS 上让你走得很远。但如果你需要更细粒度的控制，你需要定义一个 App Delegate、一个 Scene Delegate，并在你的 App 的 plist 中提供相应的场景清单。如果你要经历所有这些麻烦，你不如将你的 App 结构设计为拥有一个 UIKit 外壳，而不是试图完全依赖 SwiftUI。另一方面，`ScenePhase` API 在 macOS 上基本上毫无用处，你必须使用 App Delegate——尽管这设置起来要容易得多。对于复杂的 Mac App，AppKit 外壳可能是最好的方法。

可能两个平台上都有一些简单的工具类 App，永远不需要担心我在这里描述的所有问题，但对于严肃的应用程序，你将会遇到这些问题。此外，App Delegate 还有_更多_我在这里没有讨论的职责和功能——如果你的 App 需要其中任何功能，那么无论怎样_你确实必须_有一个 App Delegate。

这么多年过去了，SwiftUI 仍然没有为在这两个平台上构建应用程序提供这些必要且基础的 API，这令人失望。SwiftUI 需要更强大、更可靠的 API 来管理 App 生命周期、窗口生命周期和视图生命周期。
