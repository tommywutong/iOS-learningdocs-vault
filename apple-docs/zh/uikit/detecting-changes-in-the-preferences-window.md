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

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [Mac Catalyst](mac-catalyst.md)

# 检测偏好设置窗口中的更改

<sub>示例代码</sub>

在用 Mac Catalyst 构建的 Mac App 中，使用 Combine 监听并响应用户在偏好设置窗口中所做的更改。

## 概述

借助 [Combine](../combine.md)，你的 App 可以监听用户对 App 偏好设置（Preferences）窗口所做的更改并作出响应。示例 App 提供了一个只有一项设置的偏好设置窗口：背景颜色。当用户选择一种颜色时，主视图的背景会随之改变以匹配其选择。

本示例代码项目展示了如何：

- 在用 Mac Catalyst 构建的 Mac App 中添加一个偏好设置窗口。
- 为偏好设置注册默认值。
- 取回当前的偏好设置值。
- 监听并响应用户在偏好设置窗口中所做的更改。

要使用示例 App，请在 Xcode 中打开示例代码项目并选择 My Mac 作为目的地，然后构建并运行示例项目。

### 在 App 中提供偏好设置窗口

示例 App 包含一个 `Settings.bundle` 文件，系统会用它自动把标准的偏好设置（Preferences）菜单项添加到 App 菜单。选择该菜单项会显示一个偏好设置窗口，它由系统根据 Settings bundle 中定义的偏好设置指定器（preference specifier）生成。要了解更多，参见[显示设置窗口](displaying-a-settings-window.md)。

示例 App 的 Settings bundle 有一个用于设置主视图背景颜色的偏好设置指定器。它还有一个子面板偏好设置指定器，会在偏好设置窗口中显示第二个偏好设置标签页。这些指定器定义在 Settings bundle 的 `Root.plist` 文件中，而子面板的偏好设置指定器定义在 `OtherSettings.plist` 文件中。

### 注册默认偏好设置值

当用户在偏好设置窗口中更改偏好时，窗口会把更改保存到用户默认系统（user defaults system）的应用程序域。为了在 App 内存储和取回偏好设置值，示例 App 使用了 [`UserDefaults`](../foundation/userdefaults.md)。但当示例 App 首次启动时，用户默认系统中并不存在这些偏好设置值。如果 App 试图取回某个值，[`UserDefaults`](../foundation/userdefaults.md) 会返回 `nil`。

为确保 App 总能取回非 `nil` 的值，示例 App 向注册域（registration domain）注册了默认偏好设置值。不过该域不会在多次启动之间持久化这些值，所以示例 App 在用户每次启动 App 时都重新注册默认值。

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

    // To ensure that the app has a good set of preference values, register
    // the default values each time the app launches.
    registerDefaultPreferenceValues()

    return true
}
```

`registerDefaultPreferenceValues()` 方法从 Settings bundle 取回默认值：先从 `Root.plist` 文件取得偏好设置指定器，再解析出各指定器的默认值。取回这些值后，方法注册默认值。

```swift
func registerDefaultPreferenceValues() {
    let preferenceSpecifiers = retrieveSettingsBundlePreferenceSpecifiers(from: "Root.plist")
    let defaultValuesToRegister = parse(preferenceSpecifiers)

    // Register the default values with the registration domain.
    UserDefaults.standard.register(defaults: defaultValuesToRegister)
}
```

为了解析偏好设置指定器，`parse()` 方法遍历指定器数组，把默认值拷贝进 `defaultValuesToRegister` 字典。如果方法检测到 `PSChildPaneSpecifier` 类型，就取得子面板属性列表文件的名称，并把该文件中的默认值合并进 `defaultValuesToRegister` 字典。收集完默认值后，方法把字典返回给调用方。

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

### 取回偏好设置值

向注册域注册默认值之后，App 取回偏好设置值就不会再遇到值不存在的情况。为了简化对背景颜色偏好值的访问，示例 App 扩展了 [`UserDefaults`](../foundation/userdefaults.md)，为每个偏好设置值添加了属性。

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

### 处理偏好设置窗口中所做的更改

当用户在偏好设置窗口中更改背景颜色设置时，App 会改变主视图的背景颜色。为此，主视图的视图控制器在 [- viewDidLoad](<uiviewcontroller/viewdidload().md>) 方法中创建一个订阅者（subscriber）。当背景颜色值变化时，订阅者收到新值，把它映射为一个 [UIColor](uicolor.md) 对象，并把颜色赋给视图的 [backgroundColor](uiview/backgroundcolor.md) 属性。

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

### 用户偏好

- [显示设置窗口](displaying-a-settings-window.md) — 在用 Mac Catalyst 构建的 Mac App 中提供一个设置窗口，让用户管理 Settings bundle 中定义的 App 设置。

## 下载

- [DetectingChangesInThePreferencesWindow.zip](https://docs-assets.developer.apple.com/published/1b05ad2e7b73/DetectingChangesInThePreferencesWindow.zip)
