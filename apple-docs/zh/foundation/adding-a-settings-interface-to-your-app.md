---
title: 向 App 添加设置界面
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/adding-a-settings-interface-to-your-app
source_url: 'https://developer.apple.com/documentation/foundation/adding-a-settings-interface-to-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/adding-a-settings-interface-to-your-app.json'
content_hash: 'sha256:a81f8cd219114de4'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [设置](settings.md)

# 向 App 添加设置界面

<sub>文章</sub>

创建用于显示和修改 App 设置的专用界面。

## 概述

如果 App 有可配置的设置，请添加设置界面，让用户能够编辑这些设置。设置界面会说明各项设置的用途，并提供按钮、滑块、文本栏和其他控制来更改关联值。通常，你会将设置界面纳入 App 的 UI。不过，某些平台允许你在系统的“设置”App 中显示 App 设置。对于用户不常更改的设置，或者你不想在 App 中加入设置界面时，可以选择使用“设置”App。

有关如何设计设置界面的信息，请参阅《人机界面指南》中的[设置](../design/human-interface-guidelines/settings.md)。

### 向 macOS App 添加设置窗口

在 macOS 中，App 会在可从 App 菜单访问的独立窗口中显示设置。标准 App 菜单为 Settings 菜单项预留了位置，选择该项后会显示设置窗口。

要使用 SwiftUI 定义 macOS App 的设置界面，请向 App 主体添加 [设置](../swiftui/settings.md) 场景。当 App 中存在此场景类型时，SwiftUI 会更新 App 菜单，加入用于显示设置界面的项目。当用户选择该菜单项时，SwiftUI 会显示一个新窗口，其中包含你提供的场景内容。以下代码展示了 SwiftUI App 主体中的设置场景：

```swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        #if os(macOS)
        Settings {
            SettingsView()
        }
        #endif
    }
}
```

在 SwiftUI 中构建设置场景内容时，请向存储设置的变量添加 [AppStorage](../swiftui/appstorage.md) 属性包装器（property wrapper）。此属性包装器会将指定设置的值与变量值同步。随后，你可以将该变量用作场景中相关控制的值。当用户更改控制的值时，SwiftUI 会自动将新值写回默认值数据库。SwiftUI 还会检测 App 外部发生的变化，并相应刷新设置界面。

如果使用 AppKit 构建 App，请添加包含设置内容的窗口和视图控制器（view controller）。Xcode 中的新 AppKit 项目包含用于打开设置界面的菜单项，但一开始并未配置该菜单项。请使用窗口和视图控制器构建设置界面，并将其连接到菜单项。使用 [UserDefaults](userdefaults.md) 对象配置视图控制器的各项控制。当用户更改某项控制的值时，将新值写回该默认值对象。

有关如何在界面中访问设置的信息，请参阅[从代码访问设置](accessing-settings-from-your-code.md)。有关 AppKit 视图控制器的更多信息，请参阅 [NSViewController](../appkit/nsviewcontroller.md)。

### 在其他平台上将设置集成到 App UI 中

在 iOS、iPadOS、tvOS、visionOS 或 watchOS 中，没有用于显示 App 设置的标准方式。在 macOS 中，通常会在用户从菜单访问的独立窗口中显示设置。不过，这种方式不太适用于其他 Apple 平台，因为其中许多平台不显示菜单，也不提供用户可以直接操作的窗口。要在这些平台上构建设置界面，请考虑用户在 App 中使用相关设置的方式：

- 如果用户经常更改设置，请让设置界面能够从 App 主 UI 轻松访问。例如，游戏的主屏幕可以包含用于显示游戏控制和其他设置的控制。
- 如果用户偶尔更改设置，请将设置放入仅在需要时显示的独立场景或视图控制器中。例如，使用标签页栏界面的 App 可以添加一个设置标签页。
- 如果用户很少更改设置，请将它们移到系统的[“设置”App](adding-a-settings-interface-to-your-app.md#Display-settings-in-the-systems-Settings-app) 中。“设置”App 会为每个 App 提供专用空间，其中既包含系统设置，也包含 App 专属设置。
- 在 watchOS App 中，请选择合理的默认值，尽量减少修改设置的需要。如果确实需要设置界面，请将它集成到 App UI 中。

构建任何类型的设置界面时，都应使用专用场景或视图控制器来管理界面及任何相关变化。使用专用场景可以让设置代码与其余代码清晰分离。默认值系统提供通知机制，可帮助你在设置变化时更新 App。有关检测这些变化的更多信息，请参阅[从代码访问设置](accessing-settings-from-your-code.md)。

### 在系统的“设置”App 中显示设置

在 iOS、iPadOS、tvOS 和 visionOS 中，你可以选择从系统的“设置”App 显示设置。“设置”App 会为每个 App 提供专用页面，其中包含与位置、通知以及 App 所用其他系统技术有关的系统级设置。你可以在此处添加 App 专属设置，但通常只应添加用户很少更改的设置。如果你不想在 App UI 中显示设置，也可以使用系统“设置”App。

要将 App 专属设置添加到系统“设置”App，请在 App 内加入 Settings bundle。_Settings bundle_ 是一个包目录，其中包含向系统描述设置界面的属性列表文件和其他文件。系统使用这些内容构建 App 专属设置界面，并将界面中的每项控制映射到默认值数据库中的特定设置。当用户在“设置”App 中作出更改时，系统会相应更新 App 的默认值数据库。

> [!note] 注意
> 在 Mac Catalyst 中运行的 iOS App 里，系统会根据 Settings bundle 的内容构建设置界面，并向 App 菜单添加 Settings 菜单项。当用户选择该菜单项时，系统会显示设置界面并为你管理交互。

要显示 App 设置时，需要请求系统打开“设置”App 并显示你的自定页面。为此，请使用 App 对象的 [openSettingsURLString](../uikit/uiapplication/opensettingsurlstring.md) 属性，其中包含指向自定设置页面的深层链接。使用此值创建 URL，并在准备显示设置时将该 URL 传给 [open(_:options:completionHandler:)](<../uikit/uiapplication/open(__options_completionhandler_).md>) 方法。

有关如何创建 Settings bundle 的信息，请参阅[为 App 构建 Settings bundle](building-a-settings-bundle-for-your-app.md)。

## 另请参阅

### 设置界面

- [为 App 构建 Settings bundle](building-a-settings-bundle-for-your-app.md) — 将 App 的自定设置集成到 iOS、iPadOS、tvOS 和 visionOS 的“设置”App 中，并支持 Mac Catalyst 设置窗口。
