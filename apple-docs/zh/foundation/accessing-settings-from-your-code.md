---
title: 从代码访问设置
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/accessing-settings-from-your-code
source_url: 'https://developer.apple.com/documentation/foundation/accessing-settings-from-your-code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/accessing-settings-from-your-code.json'
content_hash: 'sha256:953d3aa92adb7b0b'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [设置](settings.md)

# 从代码访问设置

<sub>文章</sub>

在 App 运行时检索或更改设置，并监测这些值的外部变化。

## 概述

设置是 App 外部的数据值，但能帮助你配置 App 的行为和外观。在运行时，你可以使用设置来选择要执行的代码路径。例如，你可能会使用设置来配置 App 所用的测量单位。你可以选择 App 支持哪些设置，以及允许用户配置哪些设置。

要在代码中使用设置，请在需要时从 [UserDefaults](userdefaults.md) 对象中获取。定义设置时，应为值选择数值、字符串、日期或 URL 等简单数据类型。简单数据类型比对象等复杂类型更合适，因为简单类型在 App 版本之间具有更好的可移植性。

### 在启动时注册 App 的默认设置

每个 [UserDefaults](userdefaults.md) 对象都让你能够在需要设置前提供一套完整的初始设置。App 启动时，唯一可用的设置是全局设置和 App 上次运行时明确设置的值。新安装的 App 没有初始值，因此你必须在 App 启动周期的早期设置这些值。设置一组默认值可避免每次获取设置时都检查 `nil`。

要注册一组默认设置，请创建一个字典，其中包含 App 的所有设置键和一组适当的初始值。选择能让 App 处于大多数人愿意使用的配置下的初始设置。在启动时或 App 生命周期早期，调用 [- registerDefaults:](<userdefaults/register(defaults_).md>) 方法并传入所创建的字典。此方法会将提供的默认值放入 [NSRegistrationDomain](userdefaults/registrationdomain.md)，当其他域都不包含同一设置时，使它们成为最终选择。有关域的更多信息，请参阅 [UserDefaults](userdefaults.md)。

### 使用设置数据配置 SwiftUI 视图

如果使用设置来配置 SwiftUI 界面，请用 [AppStorage](../swiftui/appstorage.md) 属性包装器（property wrapper）包装用于存储这些值的变量。虽然你可以通过编程方式从 [UserDefaults](userdefaults.md) 获取值，但属性包装器会自动完成值的获取和设置过程。

以下示例展示了一个视图，其中的变量从 App 设置中检索其值。声明中的 `"ShowLineNumbers"` 值是 SwiftUI 用于获取和设置该值的设置键。声明中的初始值会成为默认值，SwiftUI 会将其添加到默认值数据库的注册域。

```swift
struct EditingPrefs: View {
    @AppStorage("ShowLineNumbers") var showLineNumbers = false

    var body: some View {
        Toggle("Show line numbers", isOn: $showLineNumbers) 
    }
}
```

除非指定其他选项，否则 SwiftUI 会从标准默认值数据库检索设置。要使用另一组设置，请向视图添加 [defaultAppStorage(_:)](<../swiftui/scene/defaultappstorage(__).md>) 修饰符。此修饰符的参数是你提供的 [UserDefaults](userdefaults.md) 对象。指定包含你要使用的设置的对象。例如，可以指定一个默认值对象，其中包含 App 与某个 App 扩展共享的设置。

### 直接获取和设置存储值

每个 [UserDefaults](userdefaults.md) 对象都提供用于获取和设置设置的方法。请选择与你所需值类型对应的方法，并提供以设置名称作为内容的键字符串。以下代码展示了如何使用这些方法获取和设置各种值：

```swift
let defaults = UserDefaults()
        
// 更改设置。
let showLineNumbers = true
let title = "Hello, World!"
defaults.set(showLineNumbers, forKey: "ShowLineNumbers")
defaults.set(title, forKey: "TitleString")
defaults.set(true, forKey: "CacheDataAggressively")
        
// 检索设置。
let boolValue = defaults.bool(forKey: "ShowLineNumbers")
let stringValue = defaults.string(forKey: "TitleString")
```

当你为设置分配新值时，App 的本地 [UserDefaults](userdefaults.md) 对象会立即更新其内存缓存，后续对同一设置的请求会返回新值。如果在进程之间共享设置，系统会更新自己的缓存，使各进程能够访问新值。系统还会将更改异步写入磁盘，确保它们在 App 多次启动之间持续存在。

### 响应设置的外部变化

设置发生变化时，你可能需要更新 App 的某些部分以反映新值。变化既可能来自 App 内部，也可能来自外部。你可以通过多种方式监测这些变化：

- 在 SwiftUI 视图中，向存储设置的变量添加 [AppStorage](../swiftui/appstorage.md) 属性包装器。SwiftUI 会响应来自 App 内外的变化来更新变量值。
- 要检测 App 内部发生的变化，请使用 `UserDefaults` 对象注册 [DidChangeMessage](userdefaults/didchangemessage.md) 或 [NSUserDefaultsDidChangeNotification](userdefaults/didchangenotification.md)。
- 要检测 App 外部发生的变化，请使用键值观察来监测 [UserDefaults](userdefaults.md) 对象中的特定设置。例如，可以用这种方法检测用户在系统“设置”App 中对你 App 专属设置所做的更改。在 macOS 中，外部变化也可能来自 `defaults` 命令行工具。

以下示例展示了一个使用键值观察来监测设置变化的类型。创建对象后，调用 `configureObserver` 函数会将该对象注册为标准默认值数据库中 `ShowLineNumbers` 设置的观察者。当该设置的值发生变化时，默认值系统会调用对象的 [observeValue(forKeyPath:of:change:context:)](<../objectivec/nsobject-swift.class/observevalue(forkeypath_of_change_context_).md>) 方法来报告变化。系统仅在设置的实际值发生变化时调用此方法。如果代码为设置分配了一个值，但新值与旧值相同，默认值系统不会通知观察者。

```swift
@objc class MyObserver: NSObject {
    let defaults = UserDefaults()
    
    func configureObserver() {
        defaults.addObserver(self, forKeyPath: "ShowLineNumbers", options: [.new, .old], context: nil)
    }
    
    override func observeValue(forKeyPath keyPath: String?, of object: Any?, 
                                                change: [NSKeyValueChangeKey : Any]?, context: UnsafeMutableRawPointer?) {
        print(“Setting changed: \(keyPath ?? "nil")")
    }
}
```

## 另请参阅

### App 专属设置

- [UserDefaults](userdefaults.md) — 用户默认值数据库的接口，该数据库存储系统范围和 App 专属设置。
