---
title: 检测偏好设置窗口中的更改
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, Xcode 11.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/detecting-changes-in-the-preferences-window
source_url: 'https://developer.apple.com/documentation/uikit/detecting-changes-in-the-preferences-window'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/detecting-changes-in-the-preferences-window.json'
content_hash: 'sha256:3c4c4623cdc030df'
translated: true
---

> 导航： [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Mac Catalyst](mac-catalyst.md)

# 检测偏好设置窗口中的更改

<sub>示例代码</sub>

使用 Combine 监听并响应用户在通过 Mac Catalyst 构建的 Mac App 的偏好设置窗口中所做的更改。

## 概述

借助 [Combine](../combine.md)，你的 App 可以监听用户在 App 的偏好设置窗口中所做的更改，并对这些更改作出响应。示例 App 提供一个偏好设置窗口，其中包含一项设置：背景颜色。当用户选择一种颜色时，主视图的背景会变为与用户选择相匹配的颜色。

此示例代码项目展示了如何：

- 在通过 Mac Catalyst 构建的 Mac App 中添加偏好设置窗口。
- 为偏好设置注册默认值。
- 获取当前的偏好设置值。
- 监听并响应用户在偏好设置窗口中所做的更改。

要使用示例 App，请在 Xcode 中打开示例代码项目，并选择 My Mac 作为目标。然后构建并运行示例项目。

### 在 App 中提供偏好设置窗口

示例 App 包含一个 `Settings.bundle` 文件，系统用它自动将标准的偏好设置菜单项添加到 App 菜单。选择该菜单项会显示一个偏好设置窗口，系统根据 Settings bundle 中定义的偏好设置说明符生成该窗口。要了解更多信息，请参阅 [Displaying a Settings window](displaying-a-settings-window.md)。

示例 App 的 Settings bundle 为设置主视图的背景颜色包含一个偏好设置说明符。它还包含一个子面板偏好设置说明符，该说明符在偏好设置窗口中显示第二个偏好设置标签页。Settings bundle 文件 `Root.plist` 定义这些说明符，而文件 `OtherSettings.plist` 定义子面板的偏好设置说明符。

### 注册默认偏好设置值

当用户在偏好设置窗口中更改偏好设置时，窗口会将它们保存到用户默认值系统的 application domain。为了在 App 内存储与获取偏好设置值，示例 App 使用 [`UserDefaults`](../foundation/userdefaults.md)。然而，当示例 App 首次启动时，偏好设置值在用户默认值系统中还不存在。如果 App 尝试获取某个值，[`UserDefaults`](../foundation/userdefaults.md) 会返回 `nil`。

为确保 App 始终能获取到非 `nil` 的值，示例 App 会向 registration domain 注册默认偏好设置值。不过，该 domain 不会在 App 启动之间持久化这些值，因此示例 App 每次用户启动 App 时都会注册默认值。

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

    // To ensure that the app has a good set of preference values, register
    // the default values each time the app launches.
    registerDefaultPreferenceValues()

    return true
}
```

方法 `registerDefaultPreferenceValues()` 通过从 `Root.plist` 文件获取偏好设置说明符并解析说明符的默认值，从 Settings bundle 获取默认值。获取这些值后，该方法注册默认值。

```swift
func registerDefaultPreferenceValues() {
    let preferenceSpecifiers = retrieveSettingsBundlePreferenceSpecifiers(from: "Root.plist")
    let defaultValuesToRegister = parse(preferenceSpecifiers)

    // Register the default values with the registration domain.
    UserDefaults.standard.register(defaults: defaultValuesToRegister)
}
```

为了分析偏好设置说明符，`parse()` 方法遍历说明符数组，将默认值复制到字典 `defaultValuesToRegister` 中。如果方法检测到 `PSChildPaneSpecifier` 类型，它会获取子面板属性列表文件的名称，并将该文件中的默认值合并到 `defaultValuesToRegister` 字典中。收集完默认值后，该方法将字典返回给调用者。

```swift
func parse(_ preferenceSpecifiers: [NSDictionary]) -> [String: Any] {
    var defaultValuesToRegister = [String: Any]()

    // Parse the preference specifiers, copying the default values
    // into the `defaultValuesToRegister` dictionary.
    for preferenceItem in preferenceSpecifiers {
        if let key = preferenceItem["Key"] as? String,
            let defaultValue = preferenceItem["DefaultValue"] {
            defaultValuesToRegister[key] = defaultValue
        }

        // Add child pane preference specifiers.
        if let type = preferenceItem["Type"] as? String,
            type == "PSChildPaneSpecifier" {
            if var file = preferenceItem["File"] as? String {
                if file.hasSuffix(".plist") == false {
                    file += ".plist"
                }
                let morePreferenceSpecifiers = retrieveSettingsBundlePreferenceSpecifiers(from: file)
                let moreDefaultValuesToRegister = parse(morePreferenceSpecifiers)
                defaultValuesToRegister.merge(moreDefaultValuesToRegister) { (current, _) in current }
            }
        }
    }
    
    return defaultValuesToRegister
}
```

### 获取偏好设置值

向 registration domain 注册默认值后，App 可以获取偏好设置值，而不会遇到不可用的值。为了简化对背景颜色偏好设置值的访问，示例 App 扩展了 [`UserDefaults`](../foundation/userdefaults.md)，为每个偏好设置值包含属性。

```swift
extension UserDefaults {

    @objc dynamic var backgroundColorValue: Int {
        return integer(forKey: "backgroundColorValue")
    }
    
    @objc dynamic var someRandomOption: Bool {
        return bool(forKey: "someRandomOption")
    }

}
```

### 处理在偏好设置窗口中所做的更改

当用户在偏好设置窗口中更改背景颜色设置时，App 会更改其主视图的背景颜色。为了实现这一点，主视图的视图控制器在 [- viewDidLoad](<uiviewcontroller/viewdidload().md>) 方法中创建一个订阅者。当背景颜色值更改时，订阅者接收新值，将其映射为 [UIColor](uicolor.md) 对象，并将该颜色赋给视图的 [backgroundColor](uiview/backgroundcolor.md) 属性。

```swift
var subscriber: AnyCancellable?   // Subscriber of preference changes.

override func viewDidLoad() {
    super.viewDidLoad()
    
    // Set the view's initial background color to the color specified in Preferences.
    if let colorSetting = BackgroundColors(rawValue: UserDefaults.standard.backgroundColorValue) {
        view.backgroundColor = colorSetting.currentColor()
    }
    
    // Listen for changes to the background color preference made in the Preferences window.
    subscriber = UserDefaults.standard
        .publisher(for: \.backgroundColorValue, options: [.initial, .new])
        .map( { BackgroundColors(rawValue: $0)?.currentColor() })
        .assign(to: \UIView.backgroundColor, on: self.view)
}
```

## 另请参阅

### 用户偏好设置

- [Displaying a Settings window](displaying-a-settings-window.md) — 在通过 Mac Catalyst 构建的 Mac App 中提供 Settings 窗口，以便用户管理 Settings bundle 中定义的 App 设置。

## 下载

- [DetectingChangesInThePreferencesWindow.zip](https://docs-assets.developer.apple.com/published/1b05ad2e7b73/DetectingChangesInThePreferencesWindow.zip)
