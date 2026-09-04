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

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [菜单和快捷键](menus-and-shortcuts.md)

# 添加主屏幕快速操作

<sub>示例代码</sub>

通过静态或动态 3D Touch 主屏幕快速操作，展现常用的功能。

## 概述

在运行 iOS 13 或更高版本的设备的主屏幕上，当用户长按 App 图标时（在支持 3D Touch 的设备上，用户短暂按压图标即可），App 可以显示主屏幕快速操作（Home Screen quick action）。

每个主屏幕快速操作都包含一个标题、一个位于左侧或右侧的图标（取决于你的 App 在主屏幕上的位置），以及一个可选的副标题。快速操作可以在构建时通过 App 的 `Info.plist` 静态定义，也可以在运行时动态配置。有关你可以使用快速操作展现的功能类型，参见[《人机界面指南》](https://developer.apple.com/design/human-interface-guidelines/home-screen-quick-actions)。

本示例项目中的 App 是一个基本的联系人管理器，允许用户查看和编辑少量联系人。初始视图控制器（view controller）在一个表格视图（table view）中显示联系人列表。轻点任意联系人会显示一个详情屏幕，你可以在其中编辑姓名和电子邮箱地址，或者轻点打开 Favorite 开关。

当你按压示例 App 的主屏幕图标时，会显示若干主屏幕快速操作。前两个提供搜索和共享功能的入口，其余的提供前往个人收藏联系人的快捷方式。

### 定义静态快速操作

如果适合某个 App 的快速操作从不变化，可以使用项目的 `Info.plist` 文件把它们定义为静态快速操作。本示例项目定义了两个静态快速操作：一个用于搜索，一个用于共享。`Info.plist` 文件中的 `UIApplicationShortcutItems` 键包含一个由两个字典组成的数组，代表这两个静态快速操作。

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

`UIApplicationShortcutItemType` 的值必须是一个唯一字符串，当用户调用某个快速操作时，系统会把它传递给你的 App。在处理所选的快速操作时，这个唯一的条目类型用于区分各个已定义的快速操作。

有关可用于配置主屏幕快速操作的其他 `Info.plist` 键，参见 [UIApplicationShortcutItems](../bundleresources/information-property-list/uiapplicationshortcutitems.md)。

### 定义动态快速操作

动态快速操作依赖于 App 的特定数据或状态。把共享 [UIApplication](uiapplication.md) 实例的 [shortcutItems](uiapplication/shortcutitems.md) 属性设置为一个由 [UIApplicationShortcutItem](uiapplicationshortcutitem.md) 对象组成的数组，即可配置动态主屏幕快速操作。

你可以在任何时间点设置动态快速操作，但本示例在场景委托（scene delegate）的 [- sceneWillResignActive:](<uiscenedelegate/scenewillresignactive(__).md>) 函数中设置它们。在转入后台状态的过程中是更新动态快速操作的好时机，因为系统会在用户回到主屏幕之前执行这段代码。

```swift
func sceneWillResignActive(_ scene: UIScene) {
    // 把每个个人收藏联系人转换成一个 UIApplicationShortcutItem。
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

不要限制提供给 [shortcutItems](uiapplication/shortcutitems.md) 属性的快速操作数量，因为系统只显示能装满屏幕的条目数。因此，`ContactsData` 类中 `favoriteContacts` 的实现会返回所有 `favorite` 属性被设置为 `true` 的联系人。

### 定义快速操作图标

使用 `UIApplicationShortcutIcon` 类定义快速操作图标有两种不同的方式：使用模板图像或 SF 符号（SF Symbol）。

使用模板图像名称时：

```swift
UIApplicationShortcutIcon(type: .favorite)
```

使用 SF 符号名称时：

```swift
UIApplicationShortcutIcon(systemImageName: "star.fill")
```

如前所述，本示例 App 在其 `Info.plist` 中创建了两个静态快速操作，它们的图标设置为 `UIApplicationShortcutItemIconType`。

```xml
<key>UIApplicationShortcutItemIconType</key>
<string>UIApplicationShortcutIconTypeSearch</string>
```

使用 SF 符号创建快速操作图标：

```xml
<key>UIApplicationShortcutItemIconSymbolName</key>
<string>square.stack.3d.up</string>
```

为了支持旧版本的 iOS，你可以在 App 的 `Info.plist` 中为某个给定的 `UIApplicationShortcutItem` 指定多个与图标相关的键。iOS 按以下顺序选择图标：

1. `UIApplicationShortcutItemIconSymbolName`
2. `UIApplicationShortcutItemIconFile`
3. `UIApplicationShortcutItemIconType`

如果定义了符号名称图标，iOS 会优先使用它；否则使用图标文件（如果已定义）；最后的选择才是图标类型。

### 通过快速操作传递数据

本示例中的动态快速操作都具有相同的 [type](uiapplicationshortcutitem/type.md)，因为它们执行的都是同一个操作。不过，与每个快速操作关联的联系人信息各不相同，示例会把这些信息传递到 [userInfo](uiapplicationshortcutitem/userinfo.md) 字典中。

```swift
var quickActionUserInfo: [String: NSSecureCoding] {
    /** 把联系人的姓名编码进 userInfo 字典，以便在触发快速操作时把它
        传回。注意：在实际开发中，为联系人编码一个唯一标识符
        比编码姓名更合适。
    */
    return [ SceneDelegate.favoriteIdentifierInfoKey: self.identifier as NSSecureCoding ]
}
```

静态主屏幕快速操作也可以传递 [userInfo](uiapplicationshortcutitem/userinfo.md) 数据，方法是把它放进 App 的 `Info.plist` 文件中的 `UIApplicationShortcutItemUserInfo` 键里。

示例作为 [userInfo](uiapplicationshortcutitem/userinfo.md) 传递的所有值都符合 [NSSecureCoding](../foundation/nssecurecoding.md)。

### 响应快速操作

当用户发起某个主屏幕快速操作时，App 会以下列方式之一收到通知：

- 如果 App 尚未载入，系统会启动它，并通过 [- scene:willConnectToSession:options:](<uiscenedelegate/scene(__willconnectto_options_).md>) 函数的 `connectionOptions` 参数把快捷方式条目的详细信息传入。

```swift
func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
    /** 如果用户选择了某个快速操作来启动 App，就处理这个快速操作。
        获取 shortcutItem 的引用，以便在这个场景中使用。
    */
    if let shortcutItem = connectionOptions.shortcutItem {
        // 先把它保存下来，等之后进入活跃状态时使用。
        savedShortCutItem = shortcutItem
    }
}
```

- 如果你的 App 已经载入，系统会调用你的场景委托的 [- windowScene:performActionForShortcutItem:completionHandler:](<uiwindowscenedelegate/windowscene(__performactionfor_completionhandler_).md>) 函数。

```swift
func windowScene(_ windowScene: UIWindowScene,
                 performActionFor shortcutItem: UIApplicationShortcutItem,
                 completionHandler: @escaping (Bool) -> Void) {
    let handled = handleShortCutItem(shortcutItem: shortcutItem)
    completionHandler(handled)
}
```

本示例处理快速操作时会显示一个提醒（alert），但在真实的 App 中会执行实际的功能。

### 调试 App 启动时的快速操作

要让 Xcode 调试 App 启动时的快速操作，App 需要配置好 target 的 scheme。按照以下说明来调试启动时的快速操作：

1. 构建并运行 App，把它安装到设备上。
2. 退出 App。
3. 在 SceneDelegate.swift 的 `scene(_:willConnectTo:options:)` 函数中设置一个断点，供用户选择快捷方式时使用。
4. 在 Xcode 中找到 target 的 scheme：选取 Product -\> Scheme -\> Edit Scheme
5. 选择 Run Scheme，然后进入 Info 标签页。
6. 把 Launch 设置改为“Wait for executable to be launched”。
7. 在 Xcode 中再次运行 App（此时 Xcode 的调试器会等待）。
8. 回到主屏幕，长按示例 App 的图标。
9. 选择一个快速操作快捷方式。

调试器会让 App 在断点处暂停。

## 另请参阅

### 主屏幕快速操作

- [UIApplicationShortcutItem](uiapplicationshortcutitem.md) — 一种应用快捷方式条目，也称为主屏幕动态快速操作，为你的 App 指定一个由用户发起的操作。
- [UIApplicationShortcutIcon](uiapplicationshortcuticon.md) — 一种可以选择性地与主屏幕快速操作关联的图像，用于改善其外观和易用性。
- [UIMutableApplicationShortcutItem](uimutableapplicationshortcutitem.md) — 一种可变的主屏幕动态快速操作，即为你的 App 指定可配置的、由用户发起的操作的条目。

## 下载

- [AddHomeScreenQuickActions.zip](https://docs-assets.developer.apple.com/published/e75c7b34d8fd/AddHomeScreenQuickActions.zip)
