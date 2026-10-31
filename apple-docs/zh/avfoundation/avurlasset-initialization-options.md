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
doc_path: /documentation/avfoundation/avurlasset-initialization-options
source_url: 'https://developer.apple.com/documentation/avfoundation/avurlasset-initialization-options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avurlasset-initialization-options.json'
content_hash: 'sha256:21f3d86035cb0e84'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [媒体资源](media-assets.md) · [AVURLAsset](avurlasset.md)

# 初始化选项

<sub>API 集合</sub>

指定用于配置媒体资源初始化的选项。

## 主题

### 选项

- [AVURLAssetAllowsCellularAccessKey](avurlassetallowscellularaccesskey.md) — 一个布尔值，指示系统在连接到蜂窝网络时能否代表该媒体资源发起网络请求。
- [AVURLAssetAllowsConstrainedNetworkAccessKey](avurlassetallowsconstrainednetworkaccesskey.md) — 一个布尔值，指示系统是否允许代表该媒体资源发起的网络请求使用受约束的接口。
- [AVURLAssetAllowsExpensiveNetworkAccessKey](avurlassetallowsexpensivenetworkaccesskey.md) — 一个布尔值，指示系统是否允许代表该媒体资源发起的网络请求使用高成本接口。
- [AVURLAssetHTTPCookiesKey](avurlassethttpcookieskey.md) — URL 媒体资源随 HTTP 请求发送的 HTTP cookie。
- [AVURLAssetHTTPUserAgentKey](avurlassethttpuseragentkey.md) — 一个键，用于指定该媒体资源所发起请求的用户代理。
- [AVURLAssetOverrideMIMETypeKey](avurlassetoverridemimetypekey.md) — 一个键，用于指定用于标识媒体资源格式的 MIME 类型。
- [AVURLAssetPreferPreciseDurationAndTimingKey](avurlassetpreferprecisedurationandtimingkey.md) — 一个布尔值，指示该媒体资源是否应提供准确的时长和按时间的精确随机访问。
- [AVURLAssetPrimarySessionIdentifierKey](avurlassetprimarysessionidentifierkey.md) — 指定一个 UUID，作为该媒体资源发起的 HTTP 请求的会话标识符。
- [AVURLAssetReferenceRestrictionsKey](avurlassetreferencerestrictionskey.md) — 一个表示该媒体资源在解析对外部媒体数据的引用时所使用的限制的值。
- [AVURLAssetShouldSupportAliasDataReferencesKey](avurlassetshouldsupportaliasdatareferenceskey.md) — 一个布尔值，指示系统是否解析并处理媒体资源中的替身数据引用。
- [AVURLAssetURLRequestAttributionKey](avurlasseturlrequestattributionkey.md) — 一个指定该媒体资源所请求 URL 的归因的值。
- [AVURLAssetShouldParseExternalSphericalTagsKey](avurlassetshouldparseexternalsphericaltagskey.md) — 指示是否应将媒体资源中的额外投影媒体信号解析并处理为格式描述扩展。

## 另请参阅

### 创建媒体资源

- [init(url:)](<avurlasset/init(url_).md>) — 创建一个为指定 URL 处的媒体建模的媒体资源。
- [- initWithURL:options:](<avurlasset/init(url_options_)-2x8uu.md>) — 创建一个为指定 URL 处的媒体资源建模的媒体资源。
