---
title: 配置
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/configurations
source_url: 'https://developer.apple.com/documentation/uikit/configurations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/configurations.json'
content_hash: 'sha256:cd18373a01de88f2'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [外观自定](appearance-customization.md)

# 配置

<sub>API 集合</sub>

使用配置指定视图和单元格的外观与内容。

## 概述

配置提供了一种轻量方式，可以将内容和样式应用于视图，而无需自行管理外观的渲染。

通过配置，你可以获取系统针对各种视图状态提供的默认样式，并按需自定该样式。然后，将该配置分配给支持配置的视图（如 [UICollectionViewCell](uicollectionviewcell.md)），或者用它创建自定内容视图（如 [UIListContentView](uilistcontentview.md)）。视图的配置状态发生变化时，配置会自行更新，使视图反映该状态的新样式。

配置分为两种类型：

- 背景配置，用于指定视图的背景外观。有关更多信息，请参阅 `UIBackgroundConfiguration`。
- 内容配置，用于指定内容（如图像和文本）以及该内容的样式（如色调颜色和内边距）。对于基于列表的内容，[UIListContentConfiguration](uilistcontentconfiguration-swift.struct.md) 定义了许多自定选项。

## 主题

### 配置状态

- [UIViewConfigurationState](uiviewconfigurationstate-swift.struct.md) — 封装视图状态的结构体。
- [UICellConfigurationState](uicellconfigurationstate-swift.struct.md) — 封装单元格状态的结构体。
- [UIConfigurationState](uiconfigurationstate-8d7pd.md) — 对封装视图状态的对象的要求。
- [UIConfigurationStateCustomKey](uiconfigurationstatecustomkey.md) — 定义视图自定状态的键。

### 内容配置

- [UIListContentConfiguration](uilistcontentconfiguration-swift.struct.md) — 用于基于列表的内容视图的内容配置。
- [UIListContentView](uilistcontentview.md) — 用于显示基于列表的内容的内容视图。
- [UIContentConfiguration](uicontentconfiguration-9eib5.md) — 对为内容视图提供配置的对象的要求。
- [UIContentView](uicontentview-5fh3z.md) — 对使用配置创建的内容视图的要求。

### 内容不可用配置

- [UIContentUnavailableConfiguration](uicontentunavailableconfiguration-swift.struct.md) — 用于内容不可用视图的内容配置。
- [UIContentUnavailableConfigurationState](uicontentunavailableconfigurationstate-swift.struct.md) — 封装内容不可用视图状态的结构体。

### 背景配置

- [UIBackgroundConfiguration](uibackgroundconfiguration-swift.struct.md) — 描述特定背景外观的配置。

### 颜色转换器

- [UIConfigurationColorTransformer](uiconfigurationcolortransformer-swift.struct.md) — 根据输入颜色生成修改后输出颜色的转换器。
