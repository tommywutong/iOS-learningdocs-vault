---
title: 为翻译准备你 App 的文本
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/preparing-your-apps-text-for-translation
source_url: 'https://developer.apple.com/documentation/xcode/preparing-your-apps-text-for-translation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/preparing-your-apps-text-for-translation.json'
content_hash: 'sha256:e2b38c54046947af'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Localization](localization.md)

# 为翻译准备你 App 的文本

<sub>文章</sub>

使用可本地化 API，自动用你 App 面向用户的文本填充字符串目录。

## 概述

将所有面向用户的文本包裹在可本地化 API 中，这些 API 会根据设备上的「语言与地区」设置查找字符串的翻译。Xcode 也会在构建时找出可本地化 API 中的字符串，并为你将它们添加到字符串目录文件中。你也可以选择向可本地化 API 传递注释，为本地化人员提供额外的上下文。你还可以传递表名，将字符串组织到不同的字符串目录中。

有关字符串目录的更多信息，请参阅[使用字符串目录本地化和变化文本](localizing-and-varying-text-with-a-string-catalog.md)。

### 本地化视图层级结构中的文本

当你使用 SwiftUI 时，视图中所有类型为 [LocalizedStringKey](../swiftui/localizedstringkey.md) 的字符串字面量都会自动变为可本地化的。

例如，Xcode 会将这段代码片段中的以下字符串字面量添加到默认的字符串目录中：

```swift
// Text made localizable with LocalizedStringKey.
Text("Title")
Label("Thanks for shopping with us!", systemImage: "bag")
    .font(.title)
HStack {
    Button("Clear Cart") {}
    Button("Checkout") {}
}
```

### 创建可本地化的字符串

在创建包含你想要本地化的文本的 [String](../swift/string.md) 和 [AttributedString](../foundation/attributedstring.md) 对象时，请使用 [init(localized:)](<../swift/string/init(localized_).md>) 初始化方法。

```swift
// General localizable text.
String(localized: "Add a description for your collection here.")
```

该初始化方法会使用你传入的字符串作为键，根据设备设置查找对应的翻译。

要创建具有不同键和值的可本地化字符串，请使用 [init(localized:defaultValue:options:table:bundle:locale:comment:)](<../swift/string/init(localized_defaultvalue_options_table_bundle_locale_comment_).md>) 初始化方法。Xcode 会将第一个参数用作键，第二个参数用作默认源字符串。

```swift
// Localizable string with a different key and value.
String(localized: "LIGHTING_KEY", defaultValue: "Lightbulbs")
```

有关其他初始化方法选项，请参阅 [String](../swift/string.md#Creating-a-Localized-String)。对于面向旧版本平台的 App，请改用 [NSLocalizedString](../foundation/nslocalizedstring.md)。

### 为你的可本地化字符串添加注释

添加注释以在翻译你的文本时为本地化人员提供上下文并提供帮助。

在 SwiftUI 中，使用你 [Text](../swiftui/text.md) 视图的 [init(_:tableName:bundle:comment:)](<../swiftui/text/init(__tablename_bundle_comment_).md>) 初始化方法，并提供带有额外详情的注释。

```swift
// Provide additional localizable data with a `TextView`.

Stepper {
    Text("Increase or decrease the item quantity", comment: "Lets the shopper increase or decrease the quantity for an item in their shopping cart")
} onIncrement: {
    // ...
} onDecrement: {
    // ...
}
```

在 Swift 中，使用 [init(localized:table:bundle:locale:comment:)](<../swift/string/init(localized_table_bundle_locale_comment_).md>) 初始化方法：

```swift
// Localizable text with comments.
Text("Edit", comment: "The text label on a button to switch to editor mode.")
String(localized: "North America", comment: "The name of a continent.")
```

或者，让 Xcode 根据你代码的上下文自动为你生成注释。更多信息请参阅[自动生成注释](localizing-and-varying-text-with-a-string-catalog.md#Generate-comments-automatically)。

### 将可本地化字符串组织到表中

如果你的字符串目录中的翻译数量增长得太多，可以考虑在一个项目中使用多个字符串目录。这样，当你构建 App 时，Xcode 会把可本地化字符串添加到你用名称指定的目录中。

在你的代码中，通过将字符串目录名称传给可本地化 API 的 `tableName` 或 `table` 参数，来为每个翻译选择使用哪个字符串目录。

```swift
// A SwiftUI localization example pointing to a specific string catalog.
Text("Explore", tableName: "Navigation")

// A general text localization example pointing to a specific string catalog.
String(localized: "Gorgeous mountain peaks!", table: "LandmarkCollectionData")
```

使用 `String(localized:)` 和 `AttributedString(localized:)` 初始化方法也可以初始化 UIKit 和 AppKit 控制。

### 使用可本地化类型传递可本地化字符串

在你的视图中定义或传递可本地化文本时，请使用 Swift 中推荐用于传递字符串的类型 [LocalizedStringResource](../foundation/localizedstringresource.md)。

```swift
// Localizable strings in SwiftUI.

struct CardView: View {
    let title: LocalizedStringResource
    let subtitle: LocalizedStringResource
    
    var body: some View {
        ZStack {
            Rectangle()
            VStack {
                Text(title)
                Text(subtitle)
            }
            .padding()
        }
    }
}

CardView(title: "Recent Purchases", subtitle: "Items you've ordered in the past week")
```

这个类型不仅支持使用字符串字面量进行初始化，还支持添加注释、表名，或与字符串键不同的默认值。

`LocalizedStringResource` 也适用于在通用 Swift 代码中定义的字符串。例如，这里有一个结构体，定义了一个类型为 `LocalizedStringResource` 的标题，然后分别使用字符串字面量和 `LocalizedStringResource` 的实例对其进行实例化，两者都是可本地化的。

```swift
struct UserAction {
   let title: LocalizedStringResource
}

// Localizable text created with a string literal.
let action = UserAction(title: "Order items")

// Localizable text created with a `LocalizedStringResource`.
let actionWithComment = UserAction(title: LocalizedStringResource("Order items", comment: "Action title displayed in button"))
```

### 加载位于主软件包之外的可本地化字符串

当可本地化字符串位于另一个模块、框架或 Swift Package 中时，请将 [bundle()](<../foundation/bundle().md>) 宏作为可本地化 API 中的 `bundle` 参数传入，告诉系统在与该目标关联的软件包中查找翻译。

```swift
    // Localizable string within a framework.
    String(localized: "Songs", bundle: #bundle)
```

如果你在 App 目标中调用这段代码，该宏会返回主软件包。你也可以显式传入 `Bundle.main`，它同样是默认软件包。

或者，你可以使用 [init(for:)](<../foundation/bundle/init(for_).md>) 初始化方法，从位于该目标中的特定类创建一个软件包，并将其作为 `bundle` 参数传给可本地化 API。例如，你可以在 `BirdSongs` 类所在的框架代码中使用这个初始化方法。

```swift
// Localizable string within a framework.
String(localized: "Songs", bundle: Bundle(for: (BirdSongs.self)))
```

> [!important] 重要
> 避免从你不拥有的软件包中查找字符串。这样做可能会导致字符串目录中的自动字符串提取无法正常工作。

## 另请参阅

### 字符串与文本

- [为本地化准备你的界面](preparing-your-interface-for-localization.md) — 找出你 App 中需要翻译的文本，并验证你的界面能否适配已翻译的文本。
- [为翻译准备日期、货币和数字](preparing-dates-numbers-with-formatters.md) — 使用格式化程序，确保日期、货币和数字能在多种语言和区域设置下正确显示。
</content>
