---
title: 构建高性能列表和集合视图
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, Xcode 13.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/building-high-performance-lists-and-collection-views
source_url: 'https://developer.apple.com/documentation/uikit/building-high-performance-lists-and-collection-views'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/building-high-performance-lists-and-collection-views.json'
content_hash: 'sha256:aef3e0e250d6496b'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [图像与 PDF](images-and-pdf.md) · [UIImage](uiimage.md)

# 构建高性能列表和集合视图

<sub>示例代码</sub>

通过预取（Prefetching）和图片预处理来提升 App 中列表和集合的性能。

## 概述

> [!note] 注意
> 本示例代码项目与 WWDC21 会议 [10252：打造极致丝滑的列表和集合视图](https://developer.apple.com/wwdc21/10252/) 相关联。

## 另请参阅

### 加载与缓存图片

- [为不同外观提供图片](providing-images-for-different-appearances.md) — 提供适合浅色与深色外观以及高对比度环境的图片资源。
- [在 UI 中配置和显示符号图片](configuring-and-displaying-symbol-images-in-your-ui.md) — 创建可缩放图片，使其与 App 的文本结合，并动态调整这些图片的外观。
- [为 App 创建自定义符号图片](creating-custom-symbol-images-for-your-app.md) — 使用 SF 符号（`SF Symbols`）创建、整理和标注符号图片。
- [+ imageNamed:inBundle:compatibleWithTraitCollection:](<uiimage/init(named_in_compatiblewith_).md>) — 使用与指定特性集合（Trait Collection）兼容的具名图片资源创建图片对象。
- [+ imageNamed:inBundle:withConfiguration:](<uiimage/init(named_in_with_).md>) — 使用与你指定的配置兼容的具名图片资源创建图片。
- [init(named:in:variableValue:configuration:)](<uiimage/init(named_in_variablevalue_configuration_).md>) — 使用你指定的名称、配置和可变值创建图片。
- [+ imageNamed:](<uiimage/init(named_).md>) — 从指定的具名资源创建图片对象。
- [init(imageLiteralResourceName:)](<uiimage/init(imageliteralresourcename_).md>) — 返回指定资源的图片对象。
- [+ systemImageNamed:withConfiguration:](<uiimage/init(systemname_withconfiguration_).md>) — 创建一个包含具有指定配置的系统符号图片的图片对象。
- [init(systemName:variableValue:configuration:)](<uiimage/init(systemname_variablevalue_configuration_).md>) — 创建一个包含具有你指定的配置和可变值的系统符号图片的图片对象。
- [+ systemImageNamed:compatibleWithTraitCollection:](<uiimage/init(systemname_compatiblewith_).md>) — 创建一个包含适合指定特性的系统符号图片的图片对象。
- [+ systemImageNamed:](<uiimage/init(systemname_).md>) — 创建一个包含系统符号图片的图片对象。
- [init(resource:)](<uiimage/init(resource_).md>)

## 下载

- [BuildingHighPerformanceListsAndCollectionViews.zip](https://docs-assets.developer.apple.com/published/7f5574e912c4/BuildingHighPerformanceListsAndCollectionViews.zip)
