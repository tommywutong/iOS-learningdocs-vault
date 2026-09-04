---
title: 创建字符串的宽度与设备变体
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/creating-width-and-device-variants-of-strings
source_url: 'https://developer.apple.com/documentation/xcode/creating-width-and-device-variants-of-strings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/creating-width-and-device-variants-of-strings.json'
content_hash: 'sha256:c53fa7e96c87a433'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [本地化](localization.md)

# 创建字符串的宽度与设备变体

<sub>文章</sub>

针对不同的界面宽度和设备，改变本地化后的字符串。

## 概述

> [!important] 重要
> 在 Xcode 15 及更高版本中，请改用动态类型（Dynamic Type）以及字符串目录来创建宽度变体和设备变体。更多信息参见[在 App 中支持多种语言](supporting-multiple-languages-in-your-app.md)和[使用字符串目录进行本地化与文本变体](localizing-and-varying-text-with-a-string-catalog.md)。

你可以使用 `.stringsdict` 文件为字符串提供针对不同视图宽度和不同设备的变体。例如，iOS 设备在横屏和竖屏模式下显示不同的字符串，或者用 Mac Catalyst 构建的 iPad App 在 Mac 上运行时显示不同的字符串。

`.stringsdict` 文件是一个属性列表，定义可本地化字符串的复数、宽度和设备变体。`.stringsdict` 文件包含一个键值对字典，其中的值是复数规则、宽度规则或设备规则。

规则的键是你在代码中传给 [Text](../swiftui/text.md) 结构、[NSLocalizedString](../foundation/nslocalizedstring.md) 宏及类似 API 的字符串。规则可以是复数规则、宽度规则或设备规则，决定宏返回哪条格式化后的字符串。

要为包含数量的格式化字符串创建复数变体，参见[本地化包含复数的字符串](localizing-strings-that-contain-plurals.md)。

### 向项目添加字符串字典文件

要向项目添加 `.stringsdict` 文件，选取 File \> New \> File from Template。在出现的面板中，选择平台，在 Filter 栏输入 `strings`，选择 Stringsdict File，然后点按 Next。在出现的对话框中，输入文件名，选择位置，然后点按 Create。

### 为不同宽度提供字符串变体

_宽度规则_（width rule）为界面中不同的可用宽度指定变体。它包含一个仅有一对键值对的字典。字典中的键是 `NSStringVariableWidthRuleType`，值是另一个字典，其中每个变体各有一对键值对。变体的键是一个宽度，值是一个字符串。

在下面的 `.stringsdict` 文件中，对于代码里的 `hello` 字符串，宽度变体是 `1`、`22` 和 `53`，对应的值是 `Hi`、`Hello` 和 `Greetings and Salutations`：

```other
<plist version="1.0">
    <dict>
        <key>hello</key>
        <dict>
            <key>NSStringVariableWidthRuleType</key>
            <dict>
                <key>1</key>
                <string>Hi</string>
                <key>22</key>
                <string>Hello</string>
                <key>53</key>
                <string>Greetings and Salutations</string>
            </dict>
        </dict>
    </dict>
</plist>

```

对于 [UILabel](../uikit/uilabel.md) 对象，宽度以能在 App 窗口内容纳的 em 单位计；否则宽度没有关联的单位。

宽度规则为一段宽度范围定义变体：

- 如果宽度介于两个数值相邻的键之间，API 返回键较小的那个变体。
- 如果宽度小于所有键，API 返回最小键对应的变体。

在上面的代码中，如果宽度是 `2`，宏返回 `Hi`；如果宽度是 `52`，宏返回 `Hello`。

要在代码中取得特定宽度对应的变体，参见 [variantFittingPresentationWidth(_:)](<../foundation/nsstring/variantfittingpresentationwidth(__).md>) 方法。

### 提供设备专属的字符串变体

_设备规则_（device rule）依据设备指定不同的字符串。例如，你的通用 App 在 iOS 设备上和 Mac 上运行时，可以给用户呈现不同的操作说明。

设备规则包含一个仅有一对键值对的字典。键是 `NSStringDeviceSpecificRuleType`，值是一个字典，包含以下可选键值对：

| 键 | 描述 |
|---|---|
| appletv | 在 Apple TV 上使用的字符串。 |
| applevision | 在 Apple Vision Pro 上使用的字符串。 |
| applewatch | 在 Apple Watch 上使用的字符串。 |
| ipad | 在 iPad 上使用的字符串。 |
| iphone | 在 iPhone 上使用的字符串。 |
| ipod | 在 iPod 上使用的字符串。 |
| mac | 在 Mac 上使用的字符串。 |

在下面的 `.stringsdict` 文件中，当你在代码里传入 `UserInstructions` 字符串时，App 运行在 iPhone 上会返回 `Tap here`，运行在 Mac 上返回 `Click here`，运行在 Apple TV 上返回 `Press here`：

```other
<plist version="1.0">
<dict>
    <key>UserInstructions</key>
    <dict>
        <key>NSStringDeviceSpecificRuleType</key>
        <dict>
            <key>iphone</key>
            <string>Tap here</string>
            <key>mac</key>
            <string>Click here</string>
            <key>appletv</key>
            <string>Press here</string>
        </dict>
    </dict>
</dict>
</plist>
```

## 另请参阅

### 旧式本地化技术

- [本地化包含复数的字符串](localizing-strings-that-contain-plurals.md) — 使用字符串字典文件，确保包含语言复数的字符串得到正确的本地化。
