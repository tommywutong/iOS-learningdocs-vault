---
title: 恢复 App 的状态
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, Xcode 13.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/restoring-your-app-s-state
source_url: 'https://developer.apple.com/documentation/uikit/restoring-your-app-s-state'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/restoring-your-app-s-state.json'
content_hash: 'sha256:4ecce70667c83b87'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [View controllers](view-controllers.md)

# 恢复 App 的状态

<sub>示例代码</sub>

通过保留当前活动，为用户提供连续性体验。

## 概述

本示例项目演示如何保留 App 的状态信息，并在后续启动时将 App 恢复到该先前状态。在后续启动时，将界面恢复到先前的交互点能为用户提供连续性，让他们能够快速完成未完成的任务。

用户在使用你的 App 时会执行影响用户界面的操作。例如，用户可能正在查看某条特定信息页面，而在用户离开该 App 后，操作系统可能会终止它以释放其占用的资源。用户应当能够回到他们离开时的位置——而 UI 状态恢复正是让这种体验变得无缝衔接的核心部分。

本示例 App 演示了在系统中断 App 的场景下如何使用状态保留与恢复。该示例项目管理一组产品。每个产品都有标题、图像及其他可供查看和编辑的元数据。该项目展示了如何在其 `DetailParentViewController` 中保留和恢复某个产品。

该示例支持两种状态保留方式。在 iOS 13 及更高版本中，App 使用 [`NSUserActivity`](../foundation/nsuseractivity.md) 对象为每个窗口场景保存状态。在 iOS 12 及更早版本中，App 通过保存和恢复视图控制器的配置来保留其用户界面的状态。

对于基于场景的 App，UIKit 会要求每个场景使用一个 [`NSUserActivity`](../foundation/nsuseractivity.md) 对象保存其状态信息。`NSUserActivity` 是现代状态恢复机制在 [UIScene](uiscene.md) 与 [UISceneDelegate](uiscenedelegate.md) 中的核心组成部分。在你自己的 App 中，你可以使用该活动对象来存储重建场景界面并恢复该界面内容所需的信息。如果你的 App 不支持场景，请改用基于视图控制器的状态恢复流程来保留界面状态。

有关状态恢复的更多信息，请参阅[在启动之间保留 App 的 UI](preserving-your-app-s-ui-across-launches.md)。

### 配置示例代码项目

在 Xcode 中，于 iOS target 的 General 选项卡上选择你的开发团队。

### 启用状态保留与恢复

为提供所需的活动对象，本示例在其场景委托中实现了 [- stateRestorationActivityForScene:](<uiscenedelegate/staterestorationactivity(for_).md>) 方法，如下例所示。实现此方法会告知系统该示例支持基于用户活动的状态恢复。此方法的实现从场景的 [userActivity](uiresponder/useractivity.md) 属性返回活动对象，该示例会在场景变为非活跃状态时填充该属性。

```swift
func stateRestorationActivity(for scene: UIScene) -> NSUserActivity? {
    return scene.userActivity
}
```

对于基于视图控制器的状态恢复，本示例通过 App 委托的 [- application:shouldSaveApplicationState:](<uiapplicationdelegate/application(__shouldsaveapplicationstate_).md>) 和 [- application:shouldRestoreApplicationState:](<uiapplicationdelegate/application(__shouldrestoreapplicationstate_).md>) 方法选择启用状态保留与恢复。这两个方法都返回一个 `Bool` 值，指示是否应执行相应步骤。本示例对这两个函数都返回 `true`。

以下示例为该 App 启用状态保留：

```swift
func application(_ application: UIApplication, shouldSaveSecureApplicationState coder: NSCoder) -> Bool {
    return true
}
```

以下示例为该 App 启用状态恢复：

```swift
func application(_ application: UIApplication, shouldRestoreSecureApplicationState coder: NSCoder) -> Bool {
    return true
}
```

### 使用活动对象恢复 App 状态

基于场景的状态恢复是恢复 App 用户界面的推荐方式。[`NSUserActivity`](../foundation/nsuseractivity.md) 对象会捕获 App 在当前时刻的状态。就本示例而言，App 会在用户显示或编辑产品信息时保留和恢复这些信息。当用户关闭该 App 或该 App 进入后台时，示例 App 会将产品数据保存到一个 `NSUserActivity` 对象中。当用户再次启动该 App 时，示例的 [- scene:willConnectToSession:options:](<uiscenedelegate/scene(__willconnectto_options_).md>) 方法会检查是否存在活动对象。如果存在，该方法会配置该活动对象所指定的详情视图控制器。

### 使用视图控制器恢复 App 状态

本示例通过保存其视图控制器层级结构的状态来保留状态。视图控制器采用 [UIStateRestoring](uistaterestoring.md) 协议，该协议定义了将自定状态信息保存到归档以及之后恢复该信息的方法。

该示例指定了要保存哪些视图控制器，并为该视图控制器分配一个恢复标识符。恢复标识符是 UIKit 用来标识某个视图控制器或其他用户界面元素的字符串。每个视图控制器的标识符必须是唯一的。该示例在 Interface Builder 中分配这些标识符，但这也可以在代码中完成。

该示例为 Storyboard 文件中的每个视图控制器分配一个恢复 ID。你可以通过选中视图控制器并查看身份检查器来获取这项信息。该视图控制器的 Storyboard ID 通常与恢复 ID 相同。

本示例在详情视图控制器的 [`encodeRestorableState(with:)`](<../appkit/nsresponder/encoderestorablestate(with_).md>) 方法中保存状态信息，并在 [`restoreState(with:)`](<../appkit/nsresponder/restorestate(with_).md>) 方法中恢复该状态。由于它已经将视图控制器的状态封装在一个 [`NSUserActivity`](../foundation/nsuseractivity.md) 对象中，这些方法的实现就在现有的活动对象上进行操作。随后，该示例会从这些方法中调用所需的超类方法，从而让 UIKit 恢复视图控制器其余的继承状态。

以下示例为 `InfoViewController` 启用状态保留：

```swift
override func encodeRestorableState(with coder: NSCoder) {
    super.encodeRestorableState(with: coder)

    coder.encode(product?.identifier.uuidString, forKey: InfoViewController.restoreProductKey)
}
```

以下示例为 `InfoViewController` 启用状态恢复：

```swift
override func decodeRestorableState(with coder: NSCoder) {
    super.decodeRestorableState(with: coder)
    
    guard let decodedProductIdentifier =
        coder.decodeObject(forKey: InfoViewController.restoreProductKey) as? String else {
        fatalError("A product did not exist in the restore. In your app, handle this gracefully.")
    }
    product = DataModelManager.sharedInstance.product(fromIdentifier: decodedProductIdentifier)
}
```

### 在设备上测试状态恢复

本示例会恢复以下用户界面：

- 详情视图控制器 — 在集合视图中点按某个产品以打开其详情信息。App 会恢复所选的产品和所选的标签页。
- 详情视图控制器的编辑状态 — 在详情视图中，点按"编辑"。App 会恢复编辑视图及其内容。
- 次要窗口 —（仅限 iPad）将集合视图中的某个产品拖动到设备屏幕的左侧或右侧，以创建第二个场景窗口。App 会恢复该场景及其产品。创建次要窗口的另一种方式是，在集合视图中点按并按住某个产品，通过其上下文菜单选择"在新窗口中打开"。

在调试该示例项目时，如果用户强制退出该 App，系统会自动删除其已保留的状态。删除已保留的状态信息是一项安全预防措施。此外，如果该 App 在启动时崩溃，系统也会删除已保留的状态。要测试该示例 App 恢复其状态的能力，请不要在调试期间使用 App 切换器强制退出它。请改用 Xcode 停止该 App，或以编程方式停止该 App。一种方法是使用 Home 按钮挂起该示例 App，然后在 Xcode 中停止调试器。再次使用 Xcode 启动该示例 App，UIKit 就会启动状态恢复流程。

## 另请参阅

### 界面恢复

- [Restoring your app’s state with SwiftUI](../swiftui/restoring-your-app-s-state-with-swiftui.md) — 通过保留用户当前的活动，为用户提供 App 连续性体验。
- [Preserving your app’s UI across launches](preserving-your-app-s-ui-across-launches.md) — 在系统终止 App 之后，将其恢复到先前的状态。
- [UIViewControllerRestoration](uiviewcontrollerrestoration.md) — 对象采用的一组方法，使其能够在状态恢复期间充当视图控制器的恢复类。
- [UIObjectRestoration](uiobjectrestoration.md) — 恢复类用来恢复已保留对象的接口。
- [UIStateRestoring](uistaterestoring.md) — 用于向状态恢复归档中添加对象的方法。

## 下载

- [RestoringYourAppsState.zip](https://docs-assets.developer.apple.com/published/a9326fb01c82/RestoringYourAppsState.zip)
