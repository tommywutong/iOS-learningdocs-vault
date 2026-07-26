---
title: GeoToolbox
framework: GeoToolbox
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/geotoolbox
source_url: 'https://developer.apple.com/documentation/geotoolbox'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/geotoolbox.json'
content_hash: 'sha256:9f9510bc2eaae10b'
translated: true
---

> 导航：[Technologies](technologies.md)

# GeoToolbox

<sub>框架</sub>

确定地图坐标的地点描述符信息。

## 概述

使用 `GeoToolbox` 创建 `PlaceDescriptor` 结构，以便在地图技术和第三方地图系统中使用。

## 主题

### 获取有关地点的丰富信息

- [PlaceDescriptor](geotoolbox/placedescriptor.md) — 一个结构，包含有关某个地点的标识信息，地图服务可以据此尝试查找电话号码、网站等丰富的地点信息。

### 创建地点描述符

- [init(item:)](<geotoolbox/placedescriptor/init(item_).md>) — 根据地图项创建一个地点描述符。
- [init(representations:commonName:supportingRepresentations:)](<geotoolbox/placedescriptor/init(representations_commonname_supportingrepresentations_).md>) — 创建一个地点描述符，适用于搜索或检索有关某个地点的丰富数据。

### 描述地点和地图服务提供方的值

- [PlaceRepresentation](geotoolbox/placedescriptor/placerepresentation.md) — 表示某个实际地点的值，适用于搜索或检索丰富数据。
- [SupportingPlaceRepresentation](geotoolbox/placedescriptor/supportingplacerepresentation.md) — 使用地图服务提供方的专有属性（例如来自地图服务提供方的字母数字位置标识符）描述某个实际地点的值。
