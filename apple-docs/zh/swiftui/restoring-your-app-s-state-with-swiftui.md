---
title: 使用 SwiftUI 还原 App 状态
framework: SwiftUI
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, Xcode 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/swiftui/restoring-your-app-s-state-with-swiftui
source_url: 'https://developer.apple.com/documentation/swiftui/restoring-your-app-s-state-with-swiftui'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/restoring-your-app-s-state-with-swiftui.json'
content_hash: 'sha256:e1b11926182bc6c1'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [持久化存储](persistent-storage.md)

# 使用 SwiftUI 还原 App 状态

<sub>示例代码</sub>

通过保存用户当前的活动为用户提供 App 连续性。

## 概述

这个 SwiftUI 示例项目演示了如何保存 App 的状态信息，并在后续启动时将 App 还原到之前的状态。在后续启动过程中，将界面还原到之前的交互点可以为用户提供连续性，让他们能快速完成正在进行的任务。

在使用 App 时，用户执行的操作会影响用户界面。例如，用户可能正在查看特定页面信息，离开 App 后，系统可能会终止 App 以释放其占用的资源。用户可以回到离开时的位置——UI 状态恢复是实现这种无缝体验的核心部分。

该示例 App 演示了在系统中断 App 的情况下，状态保存与还原的使用方式。示例项目管理了一组产品。每个产品都有标题、图像和其他可以查看和编辑的元数据。该项目展示了如何在 `DetailView` 中保存和还原产品。

### 配置示例代码项目

在 Xcode 中，在 iOS 目标的“Signing and Capabilities”（签名与功能）标签页上选择你的开发团队。

### 启用状态保存与还原

该示例代码项目使用 SwiftUI 的 [Scene](scene.md) 管理 App 的用户界面，其生命周期由系统管理。在 iOS 上，状态恢复在窗口或场景级别尤其重要，因为窗口经常出现和消失。有必要为每个窗口保存和还原关联的状态。在 iPad 上这一点格外重要，因为多任务切换器中的 App 不一定在运行。场景级别的状态恢复可以保持它们仍在运行的假象。

为了支持状态保存与还原，该示例使用了 [NSUserActivity](../foundation/nsuseractivity.md) 对象。对于每个用户活动，App 都必须提供在 `Info.plist` 中定义的活动类型。

### 使用场景存储

SwiftUI 提供了“存储场景数据”（Scene Storage）的概念，即 [SceneStorage](scenestorage.md)。其运作方式类似于 [State](state.md)，是一种由键/值对组成的属性包装器（property wrapper）类型。键让系统能够正确地保存和还原值。值必须为 `plist` 类型，这样系统才能正确保存和还原它。iOS 通过键/值接收此场景存储，然后向持久化的、每个场景各自的存储区域读写数据。操作系统会代为管理场景存储的保存和还原。支持场景存储的底层数据不能直接获取，因此 App 必须通过 `@SceneStorage` 属性包装器来访问它。操作系统不保证数据将在何时或以何种频率持久化。场景存储中的数据不必然等同于 App 的数据模型。场景存储旨在与数据模型**配合**使用。总体而言，可以将场景存储视为‘作用域限定在场景内的状态’。请勿将场景存储用于敏感数据。

每个需要自行保存状态的视图都需要实现 `@SceneStorage` 属性包装器。例如，`ContentView` 使用它来还原选中的产品：

```swift
@SceneStorage("ContentView.selectedProduct") private var selectedProduct: String?
```

`DetailView` 使用它来还原当前选中的标签页：

```swift
@SceneStorage("DetailView.selectedTab") private var selectedTab = Tabs.detail
```

> [!note] 注意
> 每个场景存储键都必须唯一，并正确限定作用域到 App 内的区域或用途。由于此场景存储是 App 本地的，因此无需在键前添加 App 的 Bundle Identifier。在需要的地方使用一些消除歧义的前缀以确保其唯一性。

### 通过活动对象还原 App 状态

`NSUserActivity` 对象可以捕获当前时刻的 App 状态。例如，它可以包含关于 App 当前正显示的数据的信息。系统会保存所提供的对象，并在下一次启动时将其返回给 App。当用户关闭 App 或 App 进入后台时，该示例会创建一个新的 `NSUserActivity` 对象。

每个想要为接力（Handoff）、聚焦（Spotlight）等功能宣传 `NSUserActivity` 的 SwiftUI 视图，都必须指定一个 [userActivity(_:isActive:_:)](<view/useractivity(__isactive___).md>) 视图修饰符来宣传该 `NSUserActivity`。`activityType` 参数是用户活动的类型；`isActive` 参数指示是否宣传指定类型的用户活动（此参数默认为 `true`）；以及是否使用指定的处理程序来填充用户活动的内容。用户活动的作用域仅适用于视图所在的场景或窗口。多个视图可以宣传相同的活动类型，这些处理程序都可以为用户活动的内容做出贡献。请注意，处理程序仅会在 `isActive` 参数为 `true` 的 `userActivity` 视图修饰符上被调用。如果没有任何 `userActivity` 视图修饰符将 `isActive` 指定为 `true`，则该用户活动将不会被 iOS 宣传。

每个想要处理传入的 `NSUserActivity` 的 SwiftUI 视图，都必须指定一个 [onContinueUserActivity(_:perform:)](<view/oncontinueuseractivity(__perform_).md>) 视图修饰符。该修饰符接收 `NSUserActivity` 类型和一个处理程序，当视图在其所在的场景或窗口中接收到指定活动类型时，会调用该处理程序。

```swift
.onContinueUserActivity(DetailView.productUserActivityType) { userActivity in
    if let product = try? userActivity.typedPayload(Product.self) {
        selectedProduct = product.id.uuidString
    }
}
```

### 测试状态恢复

该示例会还原以下用户界面：

- 详细信息视图控制器（Detail View Controller）——在集合视图中轻点一个产品以打开其详细信息。App 会还原所选产品和所选标签页。
- 详细信息视图控制器的编辑状态——在详细信息视图中轻点“Edit”（编辑）。App 会还原编辑视图及其内容。
- 辅助窗口——（仅 iPad）从集合视图中将一个产品拖到设备屏幕的左侧或右侧，以创建第二个场景窗口。App 会还原该场景及其产品。

状态恢复可以在设备和模拟器上进行测试。调试示例项目时，如果用户强制退出 App，系统会自动删除其保存的状态。删除保存的状态信息是一种安全预防措施。此外，如果 App 在启动时崩溃，系统也会删除保存的状态。

要测试示例 App 还原状态的能力，在调试过程中请勿使用 App 切换器强制退出。相反，使用 Xcode 停止 App，或以编程方式停止 App。另一种技巧是使用 Home 按钮挂起示例 App，然后在 Xcode 中停止调试器。再使用 Xcode 启动示例 App，SwiftUI 会启动状态恢复过程。

要将聚焦与接力（Handoff）一起使用，请遵循以下步骤：

1. 在 Xcode 中，在 `DetailView.swift` 的 `onContinueUserActivity` 闭包处设置断点。
2. 运行示例项目。
3. 在集合视图中轻点一个产品（“Cherries”），导航到其详细信息。
4. 从屏幕顶部下拉系统表单（sheet）（以强制聚焦更新其索引并请求活动）。注意，iOS 会调用 `DetailView` 的 `userActivity` 闭包。
5. 返回 App，再返回到集合视图。
6. 轻点“Cherries”之外的产品（例如“Mango”）。
7. 通过轻点 Home 按钮挂起 App。
8. 在 Home 屏幕上，向下滑动以打开聚焦窗口。
9. 在聚焦搜索字段中输入“Cherries”。搜索结果会显示“显示 Cherries 产品（Show Cherries Product）”。
10. 轻点它。注意，`DetailView` 的 `onContinueUserActivity` 闭包被调用。`DetailView` 会显示 Cherries 产品。

## 另请参阅

### 跨 App 启动保存状态

- [defaultAppStorage(_:)](<view/defaultappstorage(__).md>)——视图内 `AppStorage` 所使用的默认存储。
- [AppStorage](appstorage.md)——一种属性包装器类型，它反映 `UserDefaults` 中的一个值，并在该用户默认值更改时使视图失效。
- [SceneStorage](scenestorage.md)——一种属性包装器类型，向持久化、每个场景各自的存储区域进行读写。

## 下载

- [RestoringYourAppsStateWithSwiftUI.zip](https://docs-assets.developer.apple.com/published/cc4ebfd8f9d2/RestoringYourAppsStateWithSwiftUI.zip)
