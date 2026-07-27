---
title: 元数据查询搜索范围
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/metadata-query-search-scopes
source_url: 'https://developer.apple.com/documentation/foundation/metadata-query-search-scopes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/metadata-query-search-scopes.json'
content_hash: 'sha256:cdfbdbb6c75c4cfb'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [iCloud](icloud.md) · [NSMetadataQuery](nsmetadataquery.md)

# 元数据查询搜索范围

<sub>API 集合</sub>

[searchScopes](nsmetadataquery/searchscopes.md) 所使用的预定义搜索范围常量。

## 主题

### 常量

- [NSMetadataQueryUserHomeScope](nsmetadataqueryuserhomescope.md) — 搜索用户的个人目录。
- [NSMetadataQueryLocalComputerScope](nsmetadataquerylocalcomputerscope.md) — 搜索所有本地装载的宗卷（volume），包括用户的个人目录。即使用户的个人目录是远程宗卷，也会对其进行搜索。
- [NSMetadataQueryNetworkScope](nsmetadataquerynetworkscope.md) — 搜索用户装载的所有远程宗卷。
- [NSMetadataQueryUbiquitousDocumentsScope](nsmetadataqueryubiquitousdocumentsscope.md) — 搜索 App 的 iCloud 容器目录中 `Documents` 目录里的所有文件。
- [NSMetadataQueryUbiquitousDataScope](nsmetadataqueryubiquitousdatascope.md) — 搜索 App 的 iCloud 容器目录中不在 `Documents` 目录里的所有文件。
- [NSMetadataQueryAccessibleUbiquitousExternalDocumentsScope](nsmetadataqueryaccessibleubiquitousexternaldocumentsscope.md) — 搜索 App 容器外部的文稿。此搜索可以找到用户先前使用文稿选择器（picker）视图控制器（view controller）打开的 iCloud 文稿，让你的 App 无需用户直接交互即可再次访问这些文稿。结果的 [NSMetadataItemURLKey](nsmetadataitemurlkey.md) 特性（attribute）会返回具有安全作用域的 NSURL。有关使用具有安全作用域的 URL 的更多信息，请参阅 [NSURL](nsurl.md) 中的[具有安全作用域的 URL](nsurl.md#Security-Scoped-URLs)。
- [NSMetadataQueryIndexedLocalComputerScope](nsmetadataqueryindexedlocalcomputerscope.md) — 搜索所有已建立索引的本地装载宗卷，包括当前用户的个人目录（即使该个人目录位于远程位置）。
- [NSMetadataQueryIndexedNetworkScope](nsmetadataqueryindexednetworkscope.md) — 搜索用户装载的所有已建立索引的远程宗卷。

## 另请参阅

### 常量

- [内容相关性](content-relevance.md) — 除包含请求的元数据特性外，查询结果还包含内容相关性，可使用以下键访问。
- [通知信息字典所用的键](keys-for-use-with-a-notification-info-dictionary.md) — 用于从通知的用户信息字典中获取已更改项目集合的键常量。
