---
title: 为自定键盘配置开放访问权限
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/configuring-open-access-for-a-custom-keyboard
source_url: 'https://developer.apple.com/documentation/uikit/configuring-open-access-for-a-custom-keyboard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/configuring-open-access-for-a-custom-keyboard.json'
content_hash: 'sha256:0b2bdbc0284e727f'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [键盘与输入](keyboards-and-input.md) · [创建自定键盘](creating-a-custom-keyboard.md)

# 为自定键盘配置开放访问权限

<sub>文章</sub>

启用网络访问权限以及对共享组容器的写入权限。

## 概述

自定键盘在独立进程中的沙盒（sandbox）环境内运行。此沙盒的默认配置禁止访问网络，也禁止写入容器 App 的共享组容器（但允许读取）。开放访问权限（open access）可让你存储键盘配置、对用户输入的文本执行更复杂的分析，或提供需要服务器支持的高级功能。

在键盘的 `Info.plist` 中将 [RequestsOpenAccess](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/AppExtensionKeys.html#//apple_ref/doc/uid/TP40014212-SW24) 标志设为 [true](../swift/true.md)，即可启用这些功能。用户必须在「设置」中为你的键盘打开「允许完全访问」开关，明确允许键盘获得开放访问权限。

> [!important] 重要
> 不应轻率地启用开放访问权限。键盘会处理一些最为敏感的用户数据。请参阅下文的[赢得用户信任](configuring-open-access-for-a-custom-keyboard.md#Gain-user-trust)。

### 确定是否需要开放访问权限

请仔细考虑你是否确实需要开放访问权限。开放访问权限虽然为自定键盘提供了许多可能性，但也增加了你的责任。请考虑下面的列表，其中描述了启用或停用开放访问权限时的能力和隐私注意事项。

当 [RequestsOpenAccess](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/AppExtensionKeys.html#//apple_ref/doc/uid/TP40014212-SW24) 设为 [false](../swift/false.md)，或者用户在「设置」中禁止你的键盘完全访问时，用户知道按键输入只会发送到当前使用该键盘的 App。系统通过为键盘启用以下能力和限制来保证这一点：

- 能够执行基本键盘应有的所有常规任务
- 能够访问用于自动更正和文本建议的常用词词典
- 能够访问「设置」中的文本快捷键列表
- 除键盘自身的沙盒容器外，不能访问文件系统；只能以只读方式访问容器 App 的共享容器
- 不能访问麦克风和扬声器
- 不能直接或间接参与 iCloud、Game Center 或 App 内购买

但是，当 [RequestsOpenAccess](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/AppExtensionKeys.html#//apple_ref/doc/uid/TP40014212-SW24) 设为 [true](../swift/true.md) 时，用户必须明确允许你的键盘获得开放访问权限。他们需要在「设置」中为你的键盘选择「允许完全访问」。启用此选项时，他们知道键盘开发者能够获得自己的按键输入。系统会为开放访问键盘启用以下能力和限制：

- 开放访问键盘具有上一列表中的所有能力。
- 经用户授权，键盘可以访问「定位服务」和「通讯录」。
- 键盘和容器 App 可以使用共享容器。
- 键盘可以发送按键输入和其他输入事件，以便在服务器端处理。
- 键盘可以使用 iCloud，确保所有设备上的设置和自动更正词典保持最新。
- 键盘可以通过容器 App 参与 Game Center 和 App 内购买。
- 如果键盘支持移动设备管理（MDM），它可以与受管理的 App 配合使用。

> [!important] 重要
> 开放访问键盘必须遵守《App Store 审核指南》和《iOS 开发者计划许可协议》中有关联网键盘的准则。有关更多信息，请参阅 [App 审核支持](https://developer.apple.com/support/app-store/) 页面。

你可以使用 [UIInputViewController](uiinputviewcontroller.md) 的 [hasFullAccess](uiinputviewcontroller/hasfullaccess.md) 属性确定键盘是否具有开放访问权限。

### 赢得用户信任

下表描述了对于建立和维护用户信任尤其重要的方面。

| **方面** | **注意事项** |
|---|---|
| 按键输入数据的安全性 | 用户希望按键输入发送到他们正在输入内容的文稿或文本字段，而不是被归档到服务器或用于他们不清楚的用途。 |
| 适当且最低限度地使用其他用户数据 | 如果你的键盘使用其他用户数据，例如「定位服务」或「通讯录」数据库中的数据，你有责任向用户说明并展示这样做能带来的好处。 |

如果你构建的键盘没有开放访问权限，系统会确保按键输入无法发送回你的服务器或任何其他位置。如果你的目标是提供常规键盘功能，请使用不联网的键盘。由于沙盒受到限制，不联网的键盘能让你在遵守 Apple 数据隐私准则和赢得用户信任方面取得良好开端。

与开放访问权限相关的每项键盘能力都会让作为开发者的你承担相应责任，如下表所示。总的来说，应尽可能尊重用户数据，不要将其用于任何用户不清楚的用途。

| **开放访问键盘的能力** | **用户收益** | **开发者责任** |
|---|---|---|
| 与容器 App 共享容器 |  | 安全地存储数据，并且只将其用于文本输入 |
| 将按键输入数据发送到你的服务器 |  | 安全地传输数据，并且只将其用于文本输入 |
| 基于网络提供的数据动态更新自动更正词典 | 将新闻中的人名、地名和时事添加到自动更正词典 | 不要出于任何用户不清楚的原因，将用户身份与他们对热点信息或其他网络信息的使用相关联。 |
| 访问「通讯录」 | 将与用户相关的人名、地点和电话号码添加到自动更正词典 | 不要将「通讯录」数据用于任何用户不清楚的用途。 |
| 访问「定位服务」 | 将附近的地名添加到自动更正词典 | 不要在后台使用「定位服务」。不要出于任何用户不清楚的原因，将位置数据发送到你的服务器。 |

开放访问键盘及其容器 App 可以将按键输入数据发送到你的服务器，让你可以将计算资源用于触摸事件处理和输入预测等功能。如果使用此能力，存储收到的按键输入或语音数据的时间不得超过将文本返回给用户或提供已向用户说明的功能所需的时间。

## 另请参阅

### 键盘配置

- [配置自定键盘界面](configuring-a-custom-keyboard-interface.md) — 为文本编辑设计灵活、实用且响应迅速的界面。
