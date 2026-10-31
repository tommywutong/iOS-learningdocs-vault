---
title: 添加主屏幕快速操作
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, Xcode 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/add-home-screen-quick-actions
source_url: 'https://developer.apple.com/documentation/uikit/add-home-screen-quick-actions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/add-home-screen-quick-actions.json'
content_hash: 'sha256:90ce61d9ef1ae9ab'
translated: true
---

> 导航： [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Menus and shortcuts](menus-and-shortcuts.md)

# 添加主屏幕快速操作

<sub>示例代码</sub>

通过静态或动态的 3D Touch 主屏幕快速操作，暴露常用功能。

## 概述

在运行 iOS 13 或更高版本的设备的主屏幕上，当用户触摸并按住 App 图标时（在支持 3D Touch 的设备上，用户会短暂按压图标），App 可以显示主屏幕快速操作。

每个主屏幕快速操作都包含一个标题、一个位于左侧或右侧的图标（取决于你的 App 在主屏幕上的位置），以及一个可选的副标题。快速操作可以在构建时通过 App 的 `Info.plist` 静态定义，也可以在运行时动态配置。有关你可能使用快速操作暴露的功能类型的更多信息，参见 [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/home-screen-quick-actions)。

此示例项目中的 App 是一个基本的联系人管理器，允许用户查看和编辑少量联系人。初始视图控制器在表格视图中显示联系人列表。轻点任何联系人会显示一个详情屏幕，你可以在其中编辑姓名和电子邮件地址，或轻点以打开 Favorite 开关。

当你按压示例 App 的主屏幕图标时，会显示若干主屏幕快速操作。前两个提供对搜索和分享功能的访问，其余的则提供对收藏联系人的快捷方式。

### 定义静态快速操作

如果适合 App 的快速操作永远不会更改，请使用项目的 `Info.plist` 文件将它们定义为静态快速操作。此示例项目定义了两个静态快速操作：一个用于搜索，一个用于分享。`Info.plist` 文件中的 `UIApplicationShortcutItems` 键包含一个由两个字典组成的数组，代表这两个静态快速操作。

```xml
<key>UIApplicationShortcutItems</key>
<array>
    <dict>
        <key>UIApplicationShortcutItemType</key>
        <string>SearchAction</string>
        <key>UIApplicationShortcutItemIconType</key>
        <string>UIApplicationShortcutIconTypeSearch</string>
        <key>UIApplicationShortcutItemTitle</key>
        <string>Search</string>
        <key>UIApplicationShortcutItemSubtitle</key>
        <string>Search for an item</string>
    </dict>
    <dict>
        <key>UIApplicationShortcutItemType</key>
        <string>ShareAction</string>
        <key>UIApplicationShortcutItemIconType</key>
        <string>UIApplicationShortcutIconTypeShare</string>
        <key>UIApplicationShortcutItemTitle</key>
        <string>Share</string>
        <key>UIApplicationShortcutItemSubtitle</key>
        <string>Share an item</string>
    </dict>
</array>
```

`UIApplicationShortcutItemType` 的值必须是一个唯一字符串，当用户调用快速操作时，系统会将其传递给你的 App。在处理所选的快速操作时，唯一的 item type 用于区分定义的快速操作。

有关可用于配置主屏幕快速操作的其他 `Info.plist` 键的信息，参见 [UIApplicationShortcutItems](../bundleresources/information-property-list/uiapplicationshortcutitems.md)。

### 定义动态快速操作

动态快速操作取决于 App 的特定数据或状态。通过将共享 [UIApplication](uiapplication.md) 实例的 [shortcutItems](uiapplication/shortcutitems.md) 属性设置为 [UIApplicationShortcutItem](uiapplicationshortcutitem.md) 对象数组，来配置动态主屏幕快速操作。

可以在任何时刻设置动态屏幕快速操作，但示例在场景 delegate 的 [- sceneWillResignActive:](<uiscenedelegate/scenewillresignactive(__).md>) 函数中设置它们。在过渡到后台状态时是更新任何动态快速操作的好时机，因为系统会在用户返回主屏幕之前执行此代码。

```swift
func sceneWillResignActive(_ scene: UIScene) {
    // Transform each favorite contact into a UIApplicationShortcutItem.
    let application = UIApplication.shared
    application.shortcutItems = ContactsData.shared.favoriteContacts.map { contact -> UIApplicationShortcutItem in
        return UIApplicationShortcutItem(type: ActionType.favoriteAction.rawValue,
                                         localizedTitle: contact.name,
                                         localizedSubtitle: contact.email,
                                         icon: UIApplicationShortcutIcon(systemImageName: "star.fill"),
                                         userInfo: contact.quickActionUserInfo)
    }
}
```

不要限制提供给 [shortcutItems](uiapplication/shortcutitems.md) 属性的快速操作数量，因为系统只显示适合屏幕的项数。因此，`ContactsData` 类上 `favoriteContacts` 的实现会返回所有 `favorite` 属性设置为 `true` 的联系人。

### 定义快速操作图标

使用 `UIApplicationShortcutIcon` 类以两种不同的方式定义快速操作图标：使用模板图像或 SF Symbol。

使用模板图像名称：

```swift
UIApplicationShortcutIcon(type: .favorite)
```

使用 SF Symbol 名称：

```swift
UIApplicationShortcutIcon(systemImageName: "star.fill")
```

如前所述，此示例 App 在其 `Info.plist` 中创建了两个静态快速操作，其图标设置为 `UIApplicationShortcutItemIconType`。

```xml
<key>UIApplicationShortcutItemIconType</key>
<string>UIApplicationShortcutIconTypeSearch</string>
```

使用 SF Symbol 创建快速操作图标：

```xml
<key>UIApplicationShortcutItemIconSymbolName</key>
<string>square.stack.3d.up</string>
```

为了支持旧版 iOS，你可以在 App 的 `Info.plist` 中为给定的 `UIApplicationShortcutItem` 指定多个与图标相关的键。iOS 按以下顺序选择图标：

1. `UIApplicationShortcutItemIconSymbolName`
2. `UIApplicationShortcutItemIconFile`
3. `UIApplicationShortcutItemIconType`

如果定义了 symbol name 图标，iOS 优先使用它；否则，如果定义了 icon file，则使用它；最后的选择是 icon type。

### 通过快速操作传递数据

此示例中的动态快速操作都具有相同的 [type](uiapplicationshortcutitem/type.md)，因为它们都执行相同的操作。然而，与每个关联的联系人信息不同，示例通过 [userInfo](uiapplicationshortcutitem/userinfo.md) 字典将其传递。

```swift
var quickActionUserInfo: [String: NSSecureCoding] {
    /** Encode the name of the contact into the userInfo dictionary so it can be passed
        back when a quick action is triggered. Note: In the real world, it's more appropriate
        to encode a unique identifier for the contact than for the name.
    */
    return [ SceneDelegate.favoriteIdentifierInfoKey: self.identifier as NSSecureCoding ]
}
```

静态主屏幕快速操作也可以通过在 App 的 `Info.plist` 文件的 `UIApplicationShortcutItemUserInfo` 键中包含它，来传递 [userInfo](uiapplicationshortcutitem/userinfo.md) 数据。

示例作为 [userInfo](uiapplicationshortcutitem/userinfo.md) 传递的所有值都符合 [NSSecureCoding](../foundation/nssecurecoding.md)。

### 响应快速操作

当某人发起主屏幕快速操作时，App 会以下列方式之一被通知：

- 如果 App 尚未加载，它会被启动，并通过 [- scene:willConnectToSession:options:](<uiscenedelegate/scene(__willconnectto_options_).md>) 函数的 `connectionOptions` 参数传递快捷项的详细信息。

```swift
func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
    /** Process the quick action if the user selected one to launch the app.
        Grab a reference to the shortcutItem to use in the scene.
    */
    if let shortcutItem = connectionOptions.shortcutItem {
        // Save it off for later when we become active.
        savedShortCutItem = shortcutItem
    }
}
```

- 如果你的 App 已加载，系统会调用你的场景 delegate 的 [- windowScene:performActionForShortcutItem:completionHandler:](<uiwindowscenedelegate/windowscene(__performactionfor_completionhandler_).md>) 函数。

```swift
func windowScene(_ windowScene: UIWindowScene,
                 performActionFor shortcutItem: UIApplicationShortcutItem,
                 completionHandler: @escaping (Bool) -> Void) {
    let handled = handleShortCutItem(shortcutItem: shortcutItem)
    completionHandler(handled)
}
```

当此示例处理快速操作时，它会显示一个提醒，但在真实世界的 App 中会执行实际功能。

### 在 App 启动时调试快速操作

要让 Xcode 在 App 启动时调试快速操作，App 需要配置目标的 scheme。按照以下说明在启动时调试快速操作：

1. 构建并运行 App，以便将其安装在设备上。
2. 退出 App。
3. 在 SceneDelegate.swift 的 `scene(_:willConnectTo:options:)` 函数中设置断点，以便在某人选择快捷方式时使用。
4. 在 Xcode 中找到目标的 Scheme：打开 Product -\> Scheme -\> Edit Scheme
5. 选择 Run Scheme，Info 选项卡。
6. 将 Launch 设置更改为 “Wait for executable to be launched”。
7. 再次在 Xcode 中运行 App（Xcode 的调试器随后会等待）。
8. 转到主屏幕，轻点并按住示例的 App 图标。
9. 选择一个快速操作快捷方式。

调试器会在断点处暂停 App。

## 另请参阅

### Home Screen quick actions

- [UIApplicationShortcutItem](uiapplicationshortcutitem.md) — 一个应用程序快捷项，也称为主屏幕动态快速操作，它指定用户为你的 App 发起的操作。
- [UIApplicationShortcutIcon](uiapplicationshortcuticon.md) — 你可以选择与主屏幕快速操作关联的图像，以改善其外观和可用性。
- [UIMutableApplicationShortcutItem](uimutableapplicationshortcutitem.md) — 一个可变的主屏幕动态快速操作，它是为你的 App 指定可配置用户发起操作的项。

## 下载

- [AddHomeScreenQuickActions.zip](https://docs-assets.developer.apple.com/published/e75c7b34d8fd/AddHomeScreenQuickActions.zip)
