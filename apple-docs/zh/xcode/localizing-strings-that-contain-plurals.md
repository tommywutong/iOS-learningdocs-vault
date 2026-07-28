---
title: 本地化包含复数的字符串
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/localizing-strings-that-contain-plurals
source_url: 'https://developer.apple.com/documentation/xcode/localizing-strings-that-contain-plurals'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/localizing-strings-that-contain-plurals.json'
content_hash: 'sha256:e5e4ccad8a0bcde8'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [本地化](localization.md)

# 本地化包含复数的字符串

<sub>文章</sub>

使用 strings 字典文件来确保包含语言复数的字符串能被正确本地化。

## 概述

> [!important] 重要
> 在 Xcode 15 及更高版本中，字符串目录是本地化包含复数的字符串的推荐方式。在较早版本的 Xcode 中，请使用 strings 和 `stringsdict` 文件。有关字符串目录的更多信息，请参阅[使用字符串目录本地化和变化文本](localizing-and-varying-text-with-a-string-catalog.md)。

不同语言对于名词和单位的复数处理有不同的语法规则。因此，如果你本地化包含可变数量的格式化字符串，请使用 `.stringsdict` 文件为语言中的每种复数形式提供不同的翻译。

例如，如果你将 `%d home(s) found` 格式化字符串传递给 [NSLocalizedString](../foundation/nslocalizedstring.md) 宏或类似的 API（例如 [Text](../swiftui/text.md) 结构体），你可以使用 `.stringsdict` 文件返回字符串的不同版本。在英语中，当 `d` 为 `1` 时，你可以返回 `one home found` 或 `1 home found`；当 `d` 大于 `1` 时，返回 `%d homes found`。对于其他语言，`.stringsdict` 文件可以有更多或更少的格式化字符串复数变体。

当你导出和导入本地化时，Xcode 会自动为你处理 `.stringsdict` 文件。但是，如果你不使用本地化服务，你需要了解 `.stringsdict` 文件的格式，以便在开发语言和其他语言中进行本地化。

### 向你的项目添加 strings 字典文件

要向你的项目添加 `.stringsdict` 文件，请选择“文件”>“新建”>“从模板新建”。在出现的表单（sheet）中，选择平台，在“过滤”字段中输入 `strings`，选择“Stringsdict 文件”，然后点按“下一步”。在出现的对话框中，输入文件的名称，选择位置，然后点按“创建”。

`.stringsdict` 文件是项目中的资源文件，但 Xcode 不会自动本地化它。当该文件在项目导航器中处于选中状态时，打开检查器，然后在“本地化”下点按“本地化”。在出现的对话框中，选择一种语言，然后点按“本地化”。选择“基础”以本地化所有语言版本的文件。

如果你之前已向项目添加了本地化，请在检查器的“本地化”下选择其他本地化。如果你选择了多个本地化，`.stringsdict` 文件会在项目导航器中成为一个组，其中包含每种语言版本。

稍后当你添加更多本地化时，在选择该本地化的资源时，请务必包含 `.stringsdict` 文件。

### 以开发语言本地化 strings 字典文件

接下来，将复数规则和变体添加到开发语言版本的 `.stringsdict` 文件中。

在项目导航器中，选择 `.stringsdict` 文件。如果它显示为一个组，请选择该文件的开发语言版本（语言显示在括号中）。由于 `.stringsdict` 文件是一个属性列表，默认情况下它会在属性编辑器中显示。要使用源代码编辑器编辑 `.stringsdict` 文件，请按住 Control 键点按它，然后选择“打开方式”>“源代码”。

一个新的 `.stringsdict` 文件包含一个字典，其中包含单个格式化字符串的复数变体。对于你的 App 中包含数值的每个格式化字符串，将格式化字符串作为键，并将一个*复数变体*字典作为值，该字典包含以下键值对：

| 键 | 值 |
|---|---|
| `NSStringLocalizedFormatKey` | 一个包含变量的格式化字符串。要用复数规则替换该字符串，请在变量前加上 `%#@` 字符，并在其后加上 `@` 字符，如 `%#@homes@` 所示，其中 `homes` 是变量。 |
| `[变量]` | 一个字典，用于指定格式化字符串中某个变量的复数变体。 |

例如，为你代码中使用的面向用户的格式化字符串输入单独的字典。如果格式化字符串包含多个变量，请为每个变量输入一个单独的子字典。在以下 `.stringsdict` 文件中，格式化字符串为：`%d home(s) found`、`%d service hour(s)` 和 `%d award(s)`：

```other
<plist version="1.0">
    <dict>
        <key>%d home(s) found</key>
        <dict>
            <key>NSStringLocalizedFormatKey</key>
            <string>%#@homes@</string>
            <key>homes</key>
            <dict>
                ...
            </dict>
        </dict>
        <key>%d service hour(s)</key>
        <dict>
            …
        </dict>
        <key>%d award(s)</key>
        <dict>
            …
        </dict>
    </dict>
</plist>
```

每个格式化字符串的变量字典决定了代码中的 [Text](../swiftui/text.md) 结构体、[NSLocalizedString](../foundation/nslocalizedstring.md) 宏或类似 API 返回哪个字符串。它包含语言中每种语法复数变体的键值对，这被称为一个*分类*。

例如，以下包含英语本地化的 `.stringsdict` 文件包含 `zero`、`one` 和 `other` 分类的复数变体。对于 `%d home(s) found` 格式化字符串，API 为 `0` 返回 `No homes found`，为 `1` 返回 `%d home found`，为 `other` 值返回 `%d homes found`。

```other
<plist version="1.0">
    <dict>
        <key>%d home(s) found</key>
        <dict>
            <key>NSStringLocalizedFormatKey</key>
            <string>%#@homes@</string>
            <key>homes</key>
            <dict>
                <key>NSStringFormatSpecTypeKey</key>
                <string>NSStringPluralRuleType</string>
                <key>NSStringFormatValueTypeKey</key>
                <string>d</string>
                <key>zero</key>
                <string>No homes found</string>
                <key>one</key>
                <string>%d home found</string>
                <key>other</key>
                <string>%d homes found</string>
            </dict>
        </dict>
    </dict>
</plist>
```

一个变量字典可以包含以下键值对：

| 键 | 值 |
|---|---|
| `NSStringFormatSpecTypeKey` | 指定语言规则的类型。唯一可能的值是 `NSStringPluralRuleType`，表示一种语言复数变体。 |
| `NSStringFormatValueTypeKey` | 一个数字的字符串格式说明符，例如表示整数的字母 `d`。 |
| `zero, one, two, few, many, other` | 特定语言复数分类的格式化字符串。在字符串中使用格式说明符是可选的。`other` 分类是必需的。 |

复数分类的含义取决于语言，并非所有语言都有相同的分类。例如，英语只需要 `one` 和 `other` 分类来表示复数形式，而 `zero` 是可选的。阿拉伯语对于 `zero`、`one`、`two`、`few`、`many` 和 `other` 分类有不同的复数形式。虽然俄语也使用 `many` 分类，但哪些数字属于 `many` 分类的规则与阿拉伯语不同。

有关每种语言的分类和复数规则，请参阅 [CLDR 语言复数规则](http://cldr.unicode.org/index/cldr-spec/plural-rules)。

### 以其他语言本地化 strings 字典文件

在你以开发语言本地化 `.stringsdict` 文件并将其他本地化添加到项目之后，你就可以导出本地化了。

当你导出本地化时，Xcode 会自动将每个格式化字符串的语言特定分类添加到导出的 XLIFF 文件中。本地化人员只需要在 XLIFF 文件中为每个分类输入翻译。然后，当你导入本地化时，Xcode 会更新项目中已本地化的 `.stringsdict` 文件。

例如，如果你导出包含 `.stringsdict` 文件中 `%d home(s) found` 格式化字符串的俄语本地化，Xcode 会向俄语版本的 XLIFF 文件添加 `one`、`many` 和 `other` 分类。本地化人员插入翻译，当你导入本地化时，`.stringsdict` 文件会包含俄语正确的变量字典键值对。

```other
<plist version="1.0">
    <dict>
       <key>%d home(s) found</key>
         <dict>
            <key>NSStringLocalizedFormatKey</key>
            <string>%#@homes@</string>
            <key>homes</key>
            <dict>
                <key>NSStringFormatSpecTypeKey</key>                
                <string>NSStringPluralRuleType</string>
                <key>NSStringFormatValueTypeKey</key>
                <string>d</string>
                <key>one</key>
                <string>найден %d дом</string>
                <key>many</key>
                <string>найдены %d дома</string>
                <key>other</key>
                <string>найдены %d домов</string>
            </dict>
        </dict>
    </dict>
</plist>
```

你可以自己在 Xcode 中编辑 `.stringsdict` 文件，但请记住，除了 `other` 分类之外，所有分类都是可选的。此外，如果你不为所有特定语言的分类提供规则，本地化文本可能在语法上不正确。相反，如果你为一种语言不使用的分类提供了规则，系统会忽略该规则，并使用 `other` 分类的格式字符串。

此外，在本地化的格式化字符串中使用 `NSStringFormatValueTypeKey` 格式说明符是可选的。例如，英语中 `one` 分类的格式字符串可以是 `One home found`，而 `other` 分类可以是 `%d homes found`。

你可以在复数变体中使用格式说明符（`%d`）或拼写出数字（`one`），但不要在字符串中使用数值（`1`），因为如果用户更改了区域设置，它可能没有正确的本地化。

## 另请参阅

### 相关文档

- [添加对语言和区域的支持](adding-support-for-languages-and-regions.md) — 为你支持的每种语言和区域选择要本地化的资源。
- [导出本地化](exporting-localizations.md) — 将项目中的可本地化文件提供给本地化人员。
- [导入本地化](importing-localizations.md) — 将你为某种语言和区域翻译或改编的文件导入到你的项目中。

### 旧版本地化技术

- [创建字符串的宽度和设备变体](creating-width-and-device-variants-of-strings.md) — 针对不同的界面宽度和设备更改本地化字符串。
