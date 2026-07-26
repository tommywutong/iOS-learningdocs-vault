---
title: CoreLocationUI
framework: CoreLocationUI
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocationui
source_url: 'https://developer.apple.com/documentation/corelocationui'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocationui.json'
content_hash: 'sha256:90990d1a4d22cd58'
translated: true
---

> 导航：[Technologies](technologies.md)

# CoreLocationUI

<sub>框架</sub>

通过标准、安全的界面简化对用户位置数据的访问。

## 概述

CoreLocationUI 框架包含一套标准化界面，可与 [Core Location](corelocation.md) 安全交互，以请求访问位置数据的授权。

CoreLocationUI 为 SwiftUI app 提供了 [LocationButton](corelocationui/locationbutton.md)，为 UIKit app 提供了 [CLLocationButton](corelocationui/cllocationbutton.md)。当你希望某人为你的 app 授予一次性获取其位置的授权时，可将这些按钮添加到界面中。该按钮的样式与标准的 Core Location 设计语言保持一致，让用户在与之交互时产生熟悉感和信任感。

> [!note] 注意
> 在使用 Mac Catalyst 构建的 Mac app 中，以及在 visionOS 上运行的兼容 iPad 和 iPhone app 中，该位置按钮会忽略用户输入。

## 主题

### Location authorization

- [Sharing Your Location to Find a Park](corelocationui/sharing-your-location-to-find-a-park.md) — 使用可定制的位置按钮请求位置访问权限。
- [LocationButton](corelocationui/locationbutton.md) — 一个授予一次性位置授权的 SwiftUI 按钮。
- [CLLocationButton](corelocationui/cllocationbutton.md) — 一个授予一次性位置授权的按钮。

### Button customization

- [CLLocationButtonIcon](corelocationui/cllocationbuttonicon.md) — 指定按钮上位置箭头图标样式的常量。
- [CLLocationButtonLabel](corelocationui/cllocationbuttonlabel.md) — 指定按钮标签文字的常量。
