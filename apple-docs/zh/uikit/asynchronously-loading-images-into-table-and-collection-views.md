---
title: 将图像异步加载到表格视图和集合视图中
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, Xcode 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/asynchronously-loading-images-into-table-and-collection-views
source_url: 'https://developer.apple.com/documentation/uikit/asynchronously-loading-images-into-table-and-collection-views'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/asynchronously-loading-images-into-table-and-collection-views.json'
content_hash: 'sha256:3b3f0b0b0c060e32'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [视图与控制](views-and-controls.md) · [表格视图](table-views.md)

# 将图像异步加载到表格视图和集合视图中

<sub>示例代码</sub>

异步存储和获取图像，让 App 的响应更灵敏。

## 概述

缓存图像有助于让 App 中的表格视图（table view）和集合视图（collection view）快速实例化，并迅速响应滚动操作。示例项目中的 App 演示了如何使用 URL 获取图像。这些图像不属于资源目录，而是作为 App 软件包的一部分，用于模拟通过 URL 异步加载每幅图像。这可确保用户界面保持响应。本项目还支持 Mac Catalyst。

### 处理图像加载和缓存

在示例中，`ImageCache.swift` 类演示了一种基本机制：使用 [`NSURLSession`](../foundation/urlsession.md) 从 URL 加载图像，并使用 [`NSCache`](../foundation/nscache.md) 缓存下载的图像。`UITableView` 和 `UICollectionView` 等视图是 `UIScrollView` 的子类。

当用户在视图中滚动时，App 会重复请求同一幅图像。此示例会保留相关的完成 block，直到图像加载完成，然后将图像传递给所有发出请求的 block，因此 API 只需调用一次即可获取给定 URL 对应的图像。以下代码显示示例项目如何构建基本的缓存和加载方法：

```swift
// 如果缓存的图像可用，则返回该图像；否则异步加载并缓存它。
final func load(url: NSURL, item: Item, completion: @escaping (Item, UIImage?) -> Swift.Void) {
    // 检查缓存的图像。
    if let cachedImage = image(url: url) {
        DispatchQueue.main.async {
            completion(item, cachedImage)
        }
        return
    }
    // 如果图像有多个请求方，则追加它们的完成 block。
    if loadingResponses[url] != nil {
        loadingResponses[url]?.append(completion)
        return
    } else {
        loadingResponses[url] = [completion]
    }
    // 获取图像。
    ImageURLProtocol.urlSession().dataTask(with: url as URL) { (data, response, error) in
        // 检查错误和数据，然后尝试创建图像。
        guard let responseData = data, let image = UIImage(data: responseData),
            let blocks = self.loadingResponses[url], error == nil else {
            DispatchQueue.main.async {
                completion(item, nil)
            }
            return
        }
        // 缓存图像。
        self.cachedImages.setObject(image, forKey: url, cost: responseData.count)
        // 遍历图像的每个请求方，并将图像传回。
        for block in blocks {
            DispatchQueue.main.async {
                block(item, image)
            }
            return
        }
    }.resume()
}
```

### 合理更新数据源

如果 App 在启动时加载所有数据，就有可能耗尽内存，或因耗时过长而被终止。除非 App 必须先加载所有数据才能运行，否则请在 UI 请求图像时再加载。

> [!note] 注意
> 为确保项目在屏幕上可见之前完成加载，请在适用时使用预取 API。有关预取数据的最佳实践，请参阅[预取集合视图数据](prefetching-collection-view-data.md)。

通常，App 应等待数据源请求单元格，然后提取并设置图像。示例项目演示了一种在可复用视图上提取和显示图像的方法：

```swift
var content = cell.defaultContentConfiguration()
content.image = item.image
ImageCache.publicCache.load(url: item.url as NSURL, item: item) { (fetchedItem, image) in
    if let img = image, img != fetchedItem.image {
        var updatedSnapshot = self.dataSource.snapshot()
        if let datasourceIndex = updatedSnapshot.indexOfItem(fetchedItem) {
            let item = self.imageObjects[datasourceIndex]
            item.image = img
            updatedSnapshot.reloadItems([item])
            self.dataSource.apply(updatedSnapshot, animatingDifferences: true)
        }
    }
}
cell.contentConfiguration = content
```

## 另请参阅

### 数据

- [使用数据填充表格](filling-a-table-with-data.md) — 使用数据源对象动态创建并配置表格单元格，或从 Storyboard 静态提供它们。
- [UITableViewDataSource](uitableviewdatasource.md) — 对象为管理数据并向表格视图提供单元格而采用的方法。
- [UITableViewDataSourcePrefetching](uitableviewdatasourceprefetching.md) — 一种协议，可提前警告表格视图的数据需求，以便尽早开始可能长时间运行的数据操作。
- [UITableViewDiffableDataSource](uitableviewdiffabledatasource-2euir.md) — 用于管理数据并向表格视图提供单元格的对象。
- [NSDiffableDataSourceSnapshot](nsdiffabledatasourcesnapshot-swift.struct.md) — 视图中数据在特定时间点的状态表示。
- [UILocalizedIndexedCollation](uilocalizedindexedcollation.md) — 用于整理、排序和本地化带有章节索引的表格视图数据的对象。
- [UIDataSourceTranslating](uidatasourcetranslating.md) — 用于管理数据源对象的高级接口。
- [UIRefreshControl](uirefreshcontrol.md) — 可启动滚动视图（scroll view）内容刷新操作的标准控制。

## 下载

- [AsynchronouslyLoadingImagesIntoTableAndCollectionViews.zip](https://docs-assets.developer.apple.com/published/ddaa59c48206/AsynchronouslyLoadingImagesIntoTableAndCollectionViews.zip)
