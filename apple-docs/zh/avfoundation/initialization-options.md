---
title: 初始化选项
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/initialization-options
source_url: 'https://developer.apple.com/documentation/avfoundation/initialization-options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/initialization-options.json'
content_hash: 'sha256:3c0dcbc912162296'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [QuickTime 影片](quicktime-movies.md) · [AVMovie](avmovie.md)

# 初始化选项

<sub>API 集合</sub>

指定用于配置影片初始化的选项。

## 主题

### 选项

- [AVMovieReferenceRestrictionsKey](avmoviereferencerestrictionskey.md) — 一个键，用于指定影片在解析对外部媒体数据的引用时所使用的限制。
- [AVMovieShouldSupportAliasDataReferencesKey](avmovieshouldsupportaliasdatareferenceskey.md) — 一个键，用于指定一个布尔值，指示系统是否解析并处理影片中的替身数据引用。 _(已废弃)_

## 另请参阅

### 创建影片

- [init(url:)](<avmovie/init(url_).md>) — 创建一个为指定 URL 处的媒体建模的影片。
- [- initWithURL:options:](<avmovie/init(url_options_)-1wjrq.md>) — 从 QuickTime 影片文件或 ISO 基础媒体文件中存储的影片标头创建影片对象。
- [- initWithData:options:](<avmovie/init(data_options_).md>) — 从影片文件的数据创建影片对象。
