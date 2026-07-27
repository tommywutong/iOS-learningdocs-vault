---
title: 通知信息字典所用的键
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/keys-for-use-with-a-notification-info-dictionary
source_url: 'https://developer.apple.com/documentation/foundation/keys-for-use-with-a-notification-info-dictionary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/keys-for-use-with-a-notification-info-dictionary.json'
content_hash: 'sha256:74bf92a76b65748b'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [iCloud](icloud.md) · [NSMetadataQuery](nsmetadataquery.md)

# 通知信息字典所用的键

<sub>API 集合</sub>

用于从通知的用户信息字典中获取已更改项目集合的键常量。

## 概述

查询泛在搜索范围（ubiquitous scope）时，仅在 OS X v10.10 和 iOS 8.0 或更高版本中，并且仅当用户的 iCloud 账户启用 iCloud 云盘时，才会将这些键添加到用户信息字典。要在更早版本的 SDK 中跟踪更改，请改为对查询的 `results` 属性使用 KVO。

## 主题

### 常量

- [NSMetadataQueryUpdateAddedItemsKey](nsmetadataqueryupdateaddeditemskey.md) — 用于获取添加到查询结果中的项目数组的键。默认情况下，此数组包含表示查询结果的 [NSMetadataItem](nsmetadataitem.md) 对象；不过，查询的委托（delegate）可以使用不同类的实例替换这些对象。
- [NSMetadataQueryUpdateChangedItemsKey](nsmetadataqueryupdatechangeditemskey.md) — 用于获取查询结果中已更改项目数组的键。默认情况下，此数组包含表示查询结果的 [NSMetadataItem](nsmetadataitem.md) 对象；不过，查询的委托可以使用不同类的实例替换这些对象。
- [NSMetadataQueryUpdateRemovedItemsKey](nsmetadataqueryupdateremoveditemskey.md) — 用于获取从查询结果中移除的项目数组的键。默认情况下，此数组包含表示查询结果的 [NSMetadataItem](nsmetadataitem.md) 对象；不过，查询的委托可以使用不同类的实例替换这些对象。

## 另请参阅

### 常量

- [元数据查询搜索范围](metadata-query-search-scopes.md) — [searchScopes](nsmetadataquery/searchscopes.md) 所使用的预定义搜索范围常量。
- [内容相关性](content-relevance.md) — 除包含请求的元数据特性外，查询结果还包含内容相关性，可使用以下键访问。
