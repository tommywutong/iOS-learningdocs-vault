---
title: 为你的 App 构建 Settings bundle
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/building-a-settings-bundle-for-your-app
source_url: 'https://developer.apple.com/documentation/foundation/building-a-settings-bundle-for-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/building-a-settings-bundle-for-your-app.json'
content_hash: 'sha256:0b54373c9fc72026'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [设置](settings.md)

# 为你的 App 构建 Settings bundle

<sub>文章</sub>

将 App 的自定义设置集成到 iOS、iPadOS、tvOS 和 visionOS 的「设置」App 中，并支持 Mac Catalyst 设置窗口。

## 概述

在 iOS、iPadOS、tvOS 和 visionOS 中，你可以通过系统的「设置」App 显示 App 的部分或全部设置。「设置」App 已经会显示每个 App 特有的系统设置。例如，如果某个 App 支持推送通知，「设置」App 会显示系统用于传递这些通知的提醒类型详情。如果你不想在 App 界面中显示设置，可以改为在「设置」App 中显示它们。通常，当用户不经常修改这些设置时，可以采用这种方式。

若要向系统的「设置」App 添加自定义设置，请在 App 中包含一个 Settings bundle。_Settings bundle_ 包含向系统描述 App 设置的静态文件。系统使用这些文件中的信息构建 App 设置界面的内容，并将设置更改存回 App 的默认值数据库。App 的自定义设置会显示在所有系统特有设置的下方。

如果你的 iOS App 支持 Mac Catalyst，当 App 在 macOS 中运行时，系统会使用 App 的 Settings bundle 创建适当的设置界面。系统会为你显示并管理这个设置界面，还会自动向 App 菜单添加一个用于显示该界面的菜单项。这个由系统提供的设置界面符合用户对 macOS App 的体验预期。

> [!note] 注意
> 若要确定何时应向 App 添加 Settings bundle，请参阅《人机界面指南》中的[设置](../design/human-interface-guidelines/settings.md)。

### 向项目添加 Settings bundle 和初始内容

Xcode 提供了可添加到项目并进行修改的 Settings bundle 模板。若要向 App 添加此 bundle：

1. 在 Xcode 中打开 App 项目。
2. 选择 New \> File from Template。
3. 在 Resources 部分中选择 Settings Bundle。
4. 点按 Next。
5. 将 Settings bundle 添加到 App 目标。
6. 以名称 `Settings.bundle` 保存该 bundle。

向项目添加 Settings bundle 时，Xcode 会创建 bundle 目录，并在其中填充一些初始文件。每个 Settings bundle 的主文件都是名为 `Root.plist` 的属性列表文件，它描述设置界面主页的内容。该属性列表文件包含一个字典，其中的特殊键和值用于描述你的界面。将设置界面的各个元素放入 Preference Items 键对应的数组中。使用其他键配置内容页面和元素本身。

从初始 `Root.plist` 文件中移除不需要的所有元素，并将其替换为所需元素。下表列出了可以包含的元素类型，以及使用这些元素显示 App 设置的相关建议。

| 元素类型 | 用途 |
|---|---|
| [子页面](building-a-settings-bundle-for-your-app.md#Add-a-child-page-element) | 显示单独设置页面的元素。使用此元素来组织大量设置。 |
| [分组](building-a-settings-bundle-for-your-app.md#Add-a-group-element) | 标记一组相关元素起始位置的元素。「设置」App 会在视觉上对后续元素进行分组，并为该组应用你提供的标题。 |
| [多值](building-a-settings-bundle-for-your-app.md#Add-a-multi-value-element) | 在页面中占据一行的元素。当用户轻点或点按此元素时，它会显示一个新页面，其中包含一组互斥选项。此元素提供了比单选组更紧凑的视觉形式。 |
| [单选组](building-a-settings-bundle-for-your-app.md#Add-a-radio-group-element) | 在当前页面显示一组互斥选项的元素。此元素与多值元素类似，但无需额外导览。 |
| [滑块](building-a-settings-bundle-for-your-app.md#Add-a-slider-element) | 让用户从某个值范围中选择单个数值的元素。 |
| [文本栏](building-a-settings-bundle-for-your-app.md#Add-a-text-field-element) | 显示设置名称和可编辑文本栏的元素。可使用它采集基于文本的内容。 |
| [标题](building-a-settings-bundle-for-your-app.md#Add-a-title-element) | 显示只读设置名称和值的元素。使用此元素显示不希望用户更改的设置信息。 |
| [切换开关](building-a-settings-bundle-for-your-app.md#Add-a-toggle-switch-element) | 提供二元选择的元素。可使用它启用或停用功能。 |

### 本地化设置界面的内容

构建设置界面时，请使用开发语言指定界面元素的文本。若要本地化这些文本，请针对支持的每种语言向 Settings bundle 添加字符串文件。构建设置界面时，「设置」App 会载入适用于相应语言的字符串文件，并进行相关替换。以下清单显示了一个包含英语和德语本地化字符串的 bundle 结构。

```
Settings.bundle/
    Root.plist
    en.lproj/
        root.strings
    de.lproj/
        root.strings 
```

Settings bundle 中的每个属性列表文件都可以有自己专用的字符串文件。构建设置页面时，向页面添加 Strings Filename 键，并将其值设为相关字符串文件的名称。字符串文件名称中不要包含文件扩展名。例如，为上一清单中的 `Root.plist` 文件指定字符串文件时，请将该键的值设为 `root`。

在每个字符串文件中，将每对翻译字符串单独放在一行，并用等号（=）分隔字符串。将原始值放在等号左侧，让译者将翻译后的值放在右侧。以下清单显示了一个将一组字符串从英语翻译为德语的字符串文件内容。

```
"Group" = "Gruppe";
"Name" = "Name";
"Enabled" = "Aktiviert";
```

### 指定每个设置页面的内容

Settings bundle 中的每个属性列表文件都包含描述该页面内容的顶层键。在 `Root.plist` 文件中包含这些键，以指定主设置页面的内容。还应在添加到 Settings bundle 的所有子页面属性列表文件中包含这些键。这些键会告诉「设置」App 在页面上显示哪些元素，以及在何处查找本地化资源。下表列出了支持的键及其用途。

| 键名 | 数据类型 | 描述 |
|---|---|---|
| Preference Items（必需） | Array | 要在当前页面显示的元素。数组中的每一项都是一个 Dictionary，其中包含单个元素的键和值。按照你希望各项在页面上出现的顺序，将它们排列在数组中。此键的原始名称为 `PreferenceSpecifiers`。 |
| Strings Filename | String | 用于存储当前页面本地化文本的 `.strings` 文件名称，不包括文件扩展名。针对支持的每种语言，在 Settings bundle 中创建该语言专用的项目目录，并在目录中放置此文件的副本。如果省略此键，系统不会显示设置界面的本地化版本。此键的原始名称为 `StringsTable`。 |
| Settings Page Title | String | 页面名称，「设置」App 不会使用它。此键的原始名称为 `Title`。 |

### 添加子页面元素

如果 App 的设置界面包含大量元素，请使用子页面元素以分层方式组织它们。「设置」App 遇到子页面元素时，会向设置界面的当前页面添加一行。轻点或点按该行会转到一个新页面，其内容由你在 Settings bundle 的另一个属性列表文件中提供。下表列出了支持的键及其用途。

| 键名 | 值类型 | 描述 |
|---|---|---|
| Type（必需） | String | 此键的值始终为 `Child Pane`。此键的原始名称为 `Type`，原始值为 `PSChildPaneSpecifier`。 |
| Title（必需，可本地化） | String | 系统显示在文本栏旁边的标题字符串。此键的原始名称为 `Title`。 |
| Filename（必需） | String | 要载入的属性列表文件名称。指定文件名时不要包含 `.plist` 扩展名。将该文件放在 Settings bundle 的根目录中，与现有的 `Root.plist` 文件并列。此键的原始名称为 `File`。 |
| Icon | String | Settings bundle 中的图像名称，不包括文件扩展名。对于在 Mac Catalyst 中运行的 iOS App，系统会将此图像显示为 App「设置」窗口中的工具栏标签页图标。iOS、iPadOS、tvOS 和 visionOS 中的「设置」App 会忽略此键。此键的原始名称为 `Icon`。 |

### 添加分组元素

包含分组元素，以便在视觉上分隔当前页面中的设置。「设置」App 遇到分组元素时，会以特殊的视觉处理方式渲染该组中的各项，表明它们彼此相关，而与其他元素无关。该组包含紧跟在分组元素之后的各项。当 Preference Items 数组中没有更多元素，或者「设置」App 遇到单选组元素或另一个分组元素时，该组结束。下表列出了支持的键及其用途。

| 键名 | 值类型 | 描述 |
|---|---|---|
| Type（必需） | String | 此键的值始终为 `Group`。此键的原始名称为 `Type`，原始值为 `PSGroupSpecifier`。 |
| Title（可本地化） | String | 要显示在分组项目之前的标题字符串。使用此键指定设置组的用途。此键的原始名称为 `Title`。 |

### 添加多值元素

多值元素让用户可以从一组互斥值中选择一个值。「设置」App 会在当前页面上为此元素显示一行。当用户轻点或点按该行时，「设置」会显示一个包含可用值的新页面，并在所选值旁边放置勾号。当用户更改所选值时，系统会将新值保存到 App 的默认值数据库。下表列出了支持的键及其用途。

| 键名 | 值类型 | 描述 |
|---|---|---|
| Type（必需） | String | 此键的值始终为 `Multi Value`。此键的原始名称为 `Type`，原始值为 `PSMultiValueSpecifier`。 |
| Identifier（必需） | String | App 默认值数据库中某个键的名称。当用户更新设置时，系统会将新值写入默认值数据库中的此键。此键的原始名称为 `Key`。 |
| Title（必需，可本地化） | String | 要在项目所在行的前缘显示的文本。行的后缘包含当前所选值（如果有），以及用于表明轻点或点按该行会显示新页面的 V 形图标。此键的原始名称为 `Title`。 |
| Default Value（必需） | Boolean | 所需的默认选中值。如果默认值数据库不包含指定标识符的值，「设置」App 会使用此值。此键的原始名称为 `DefaultValue`。 |
| Titles（必需，可本地化） | Array | 字符串数组，其中每个字符串都包含一个选项的易读描述。此数组中的每个字符串都与 Values 数组中相同索引处的值对应。Values 数组必须具有相同数量的元素。此键的原始名称为 `Titles`。 |
| Values（必需） | Array | 对应选项的值数组。数组中的项目可以是任意属性列表类型。当用户选择一个选项时，系统会将此数组中的对应值写入默认值数据库。此数组与 Title 数组必须具有相同数量的元素。此键的原始名称为 `Values`。 |

### 添加单选组元素

单选组元素会在当前页面显示一组互斥值。此元素与多值元素类似，但会将项目放置在当前页面，而不是显示新页面。轻点或点按一行会取消选择其他行，并将新值保存到 App 的默认值数据库。请避免将此选项用于大量可能值。下表列出了支持的键及其用途。

| 键名 | 值类型 | 描述 |
|---|---|---|
| `Type`（必需） | String | 此键的原始名称为 `Type`，值始终为 `PSRadioGroupSpecifier`。 |
| `Identifier`（必需） | String | App 默认值数据库中某个键的名称。当用户更新设置时，系统会将新值写入默认值数据库中的此键。此键的原始名称为 `Key`。 |
| `Title`（可本地化） | String | 要为组名称显示的文本。「设置」App 会将此文本放在选项组上方。使用此字符串传达该组的用途。此键的原始名称为 `Title`。 |
| `FooterText`（可本地化） | String | 要在分组框下方显示的附加文本。此键的原始名称为 `FooterText`。 |
| `DefaultValue`（必需） | Boolean | 所需的默认选中值。如果默认值数据库不包含指定标识符的值，「设置」App 会使用此值。此键的原始名称为 `DefaultValue`。 |
| `Titles`（必需，可本地化） | Array | 字符串数组，其中每个字符串都包含一个选项的易读描述。此数组中的每个字符串都与 Values 数组中相同索引处的值对应。Values 数组必须具有相同数量的元素。此键的原始名称为 `Titles`。 |
| `Values`（必需） | Array | 对应选项的值数组。数组中的项目可以是任意属性列表类型。当用户选择一个选项时，系统会将此数组中的对应值写入默认值数据库。此数组与 Title 数组必须具有相同数量的元素。此键的原始名称为 `Values`。 |

如果项目列表中先前出现过分组元素，此元素的存在会结束该组，并专门为单选组值创建一个新组。如果你在单选组之后显示任何项目，请将第一个项目设为另一个分组元素，以创建新的设置组。

### 添加滑块元素

滑块元素显示一行，其中包含一个可用于表示连续值范围的滑块控制。此行中的控制等同于 [Slider](../swiftui/slider.md)、[UISlider](../uikit/uislider.md) 或 [NSSlider](../appkit/nsslider.md) 控制。滑块控制横跨整行宽度，滑块的最小值位置位于该行的前缘。下表列出了支持的键及其用途。

| 键名 | 值类型 | 描述 |
|---|---|---|
| Type（必需） | String | 此键的值始终为 `Slider`。此键的原始名称为 `Type`，原始值为 `PSSliderSpecifier`。 |
| Identifier（必需） | String | App 默认值数据库中某个键的名称。当用户更新设置时，系统会将新值写入默认值数据库中的此键。此键的原始名称为 `Key`。 |
| Default Value（必需） | Boolean | 所需的默认值。如果默认值数据库不包含指定标识符的值，「设置」App 会使用此值。此键的原始名称为 `DefaultValue`。 |
| Minimum Value（必需） | Number | 当滑块拇指位于最小值位置时，要存储到默认值数据库中的数值。此键的原始名称为 `MinimumValue`。 |
| Maximum Value（必需） | Number | 当滑块拇指位于最大值位置时，要存储到默认值数据库中的数值。此键的原始名称为 `MaximumValue`。 |
| Min Value Image Filename | String | Settings bundle 中的图像名称，不包括文件扩展名。「设置」App 会将此图像显示在滑块的最小值位置旁边，并根据需要缩放图像以适应可用空间。此键的原始名称为 `MinimumValueImage`。 |
| Max Value Image Filename | String | Settings bundle 中的图像名称，不包括文件扩展名。「设置」App 会将此图像显示在滑块的最大值位置旁边，并根据需要缩放图像以适应可用空间。此键的原始名称为 `MaximumValueImage`。 |

> [!note] 注意
> tvOS 不支持设置界面中的滑块控制，并且 tvOS 中的「设置」App 会忽略属性列表文件中的滑块元素。

### 添加文本栏元素

文本栏元素会显示一行，其中包含用于键入文本值的可编辑区域。元素标题显示在行的前缘，值显示在后缘。轻点或点按该行会显示系统键盘，以便用户键入内容。下表列出了支持的键及其用途。

| 键名 | 值类型 | 描述 |
|---|---|---|
| Type（必需） | String | 此键的值始终为 `Text Field`。此键的原始名称为 `Type`，原始值为 `PSTextFieldSpecifier`。 |
| Identifier（必需） | String | App 默认值数据库中某个键的名称。当用户更新设置时，系统会将新值写入默认值数据库中的此键。此键的原始名称为 `Key`。 |
| Title（可本地化） | String | 要在行的前缘显示的文本。使用此值描述设置的用途。如果省略此键，可编辑文本栏会横跨整行宽度。此键的原始名称为 `Title`。 |
| Default Value | Boolean | 所需的默认值。如果默认值数据库不包含指定标识符的值，「设置」App 会使用此值。此键的原始名称为 `DefaultValue`。 |
| Text Field Is Secure | Boolean | 一个布尔值，指示是否隐藏键入的文本。将此键的值设为 `YES` 可隐藏文本，设为 `NO` 则在用户键入时显示文本。如果省略此键，「设置」App 会将其设为 `NO`。此键的原始名称为 `IsSecure`。 |
| Keyboard Type | String | 要显示的键盘类型。将此键的值设为以下字符串之一：`Alphabet`、`NumbersAndPunctuation`、`NumberPad`、`URL` 或 `EmailAddress`。这些值对应可用于标准文本栏控制的键盘类型。如果省略此键，「设置」App 会将键盘类型设为 `Alphabet`。此键的原始名称为 `KeyboardType`。 |
| Autocapitalization Style | String | 键入时采用的自动大写方式。将此键的值设为以下值之一：`None`、`Sentences`、`Words` 或 `AllCharacters`。这些值对应系统文本输入特性（trait）的自动大写样式。如果省略此键，「设置」App 会使用 `None` 样式。此键的原始名称为 `AutocapitalizationType`。 |
| Autocorrection Style | String | 要应用于所键入文本的自动更正样式。将此键的值设为以下值之一：`Default`、`Yes` 或 `No`。这些值对应系统文本输入特性的自动更正行为。如果省略此键，「设置」App 会使用 `Default` 样式。此键的原始名称为 `AutocorrectionType`。 |

> [!important] 重要
> 由于「设置」App 会显示并管理设置界面，因此 App 无法在系统将设置文本保存到数据库之前对其进行验证。当你在代码中检索相关设置的值时，请在使用前对其进行验证。

### 添加标题元素

标题元素显示只读版本的设置名称及其当前配置值（如果有）。使用此元素显示不希望用户更改的设置。例如，你可以使用此栏显示用户通过 App 界面创建的登录信息。下表列出了支持的键及其用途。

| 键名 | 值类型 | 描述 |
|---|---|---|
| Type（必需） | String | 此键的值始终为 `Title`。此键的原始名称为 `Type`，原始值为 `PSTitleValueSpecifier`。 |
| Identifier（必需） | String | App 默认值数据库中某个键的名称。当用户更新设置时，系统会将新值写入默认值数据库中的此键。此键的原始名称为 `Key`。 |
| Title（必需，可本地化） | String | 要在行的前缘显示的文本。使用此值描述设置的用途。此键的原始名称为 `Title`。 |
| Default Value（必需） | String | 所需的默认选中值。如果默认值数据库不包含指定标识符的值，「设置」App 会使用此值。此键的原始名称为 `DefaultValue`。 |
| Titles（可本地化） | Array | 字符串数组，其中每个字符串都包含一个选项的易读描述。此数组中的每个字符串都与 Values 数组中相同索引处的值对应。Values 数组必须具有相同数量的元素。此键的原始名称为 `Titles`。 |
| Values | Array | 指定选项的值数组。此数组中的值可以是任意属性列表类型。此数组与 Title 数组必须具有相同数量的元素。此键的原始名称为 `Values`。 |

使用此元素的 Titles 和 Values 键，为可能难以理解的设置提供有意义的描述。如果 Values 数组包含当前设置，「设置」App 会改为显示 Titles 数组中的关联字符串。如果设置包含数组中没有的值，「设置」App 会原样显示该值。

### 添加切换开关元素

切换开关元素显示一个提供二元选择的控制，并显示一个描述该选择含义的标题。此元素等同于 [Toggle](../swiftui/toggle.md)、[UISwitch](../uikit/uiswitch.md) 或 [NSSwitch](../appkit/nsswitch.md) 控制。通常，你会将此元素用于启用或停用功能的设置。下表列出了支持的键及其用途。

| 键名 | 值类型 | 描述 |
|---|---|---|
| Type（必需） | String | 此键的值始终为 `Toggle Switch`。此键的原始名称为 `Type`，原始值为 `PSToggleSwitchSpecifier`。 |
| Title（必需，可本地化） | String | 要在行的前缘显示的文本。「设置」App 会将开关控制放在行的后缘。此键的原始名称为 `Title`。 |
| Identifier（必需） | String | App 默认值数据库中某个键的名称。当用户更新设置时，系统会将新值写入默认值数据库中的此键。此键的原始名称为 `Key`。 |
| Default Value（必需） | Boolean | 所需的默认值。如果默认值数据库不包含指定标识符的值，「设置」App 会使用此值。此键的原始名称为 `DefaultValue`。 |
| Value for ON | Any | 开关处于“开”位置时要存储在默认值数据库中的值。包含此键可在默认值数据库中存储非布尔值。例如，可以将此值设为文本为“ON”的字符串。此键的原始名称为 `TrueValue`。 |
| Value for OFF | Any | 开关处于“关”位置时要存储在默认值数据库中的值。包含此键可在默认值数据库中存储非布尔值。例如，可以将此值设为文本为“OFF”的字符串。此键的原始名称为 `FalseValue`。 |
| Description | String | 要在 macOS 中显示在切换开关下方的较长描述性字符串。此键仅适用于在 Mac Catalyst 中运行的 iOS App；其他平台会忽略它。此键的原始名称为 `Description`。 |
| `TrueConfirmationPrompt` | Dictionary | 一个字典，用于定义当用户尝试将开关设为“开”位置时要显示的提示。此键仅适用于在 Mac Catalyst 中运行的 iOS App；其他平台会忽略它。 |
| `FalseConfirmationPrompt` | Dictionary | 一个字典，用于定义当用户尝试将开关设为“关”位置时要显示的提示。此键仅适用于在 Mac Catalyst 中运行的 iOS App；其他平台会忽略它。 |

对于在 Mac Catalyst 中运行的 iOS App，如果你希望用户在系统更新设置前确认更改，请包含 `TrueConfirmationPrompt` 或 `FalseConfirmationPrompt` 键。当存在这些键时，系统会显示一个提示，其中包含你在相应键的字典中提供的信息。如果用户确认更改，系统会将新设置写入默认值数据库。下表列出了该字典支持的键和值。

| 键名 | 值类型 | 描述 |
|---|---|---|
| `Type`（必需） | String | 此键的值必须是 `PSConfirmationPrompt`。 |
| `Title`（必需） | String | 包含提示标题的字符串。此标题可能不会在某些设备上显示。 |
| `Prompt`（必需） | String | 提示中显示的说明性文本，用于确认切换更改。使用此字符串请用户确认选择。 |
| `ConfirmText` | String | 要在提示的确认按钮中显示的文本。如果用户点按此按钮，系统会将设置更改为新值。如果不提供此键，系统会为按钮提供默认标题。 |
| `DenyText` | String | 要在提示的取消按钮中显示的文本。如果用户点按此按钮，系统不会更改设置。如果不提供此键，系统会为按钮提供默认标题。 |

## 另请参阅

### 设置界面

- [向 App 添加设置界面](adding-a-settings-interface-to-your-app.md) — 创建用于显示和修改 App 设置的专用界面。
