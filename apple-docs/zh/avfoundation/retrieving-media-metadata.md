---
title: 检索媒体元数据
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/retrieving-media-metadata
source_url: 'https://developer.apple.com/documentation/avfoundation/retrieving-media-metadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/retrieving-media-metadata.json'
content_hash: 'sha256:af8a974119c9016d'
translated: true
---

> 导航： [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Media assets](media-assets.md)

# 检索媒体元数据

<sub>文章</sub>

为媒体 asset 及其轨道加载描述性元数据。

## 概述

媒体容器格式提供描述其内容的元数据。你可以检索这些元数据来访问媒体的相关信息，例如标题、插图和创建日期。AVFoundation 使用 [AVMetadataItem](avmetadataitem.md) 类为元数据值建模。一个元数据项目表示单个值，例如影片的描述或海报图像。无论底层容器和元数据格式是什么，这个类都提供了一个简单一致的接口来处理元数据。

### 加载 asset 的元数据

[AVAsset](avasset.md) 提供多种访问其元数据的方式。你可以通过加载它的 [metadata](avpartialasyncproperty/metadata-16qej.md) 属性的值来获取它的全部元数据。或者，你可以通过加载它的 [commonMetadata](avpartialasyncproperty/commonmetadata-3j3n4.md) 属性的值，获取它持有的所有元数据格式中共有项目的子集。

要获取特定格式的元数据集合，例如 [AVMetadataFormatiTunesMetadata](avmetadataformat/itunesmetadata.md) 或 [AVMetadataFormatQuickTimeMetadata](avmetadataformat/quicktimemetadata.md)，可调用 asset 的 [- loadMetadataForFormat:completionHandler:](<avasset/loadmetadata(for_completionhandler_).md>) 方法，向它传入要加载的特定 [AVMetadataFormat](avmetadataformat.md)。下面的示例迭代 asset 包含的 [availableMetadataFormats](avpartialasyncproperty/availablemetadataformats-4yiq8.md)，并加载每种格式的元数据项目以处理它们的值。

```swift
// A local or remote asset to inspect.
let asset = AVURLAsset(url: url)
for format in try await asset.load(.availableMetadataFormats) {
    let metadata = try await asset.loadMetadata(for: format)
    // Process the format-specific metadata collection.
    print("The available metadata format is \(metadata)")
}
```

### 过滤元数据集合

加载元数据集合后，你可以使用 [AVMetadataItem](avmetadataitem.md) 的类方法把它过滤到特定的值。下面的示例展示如何使用 [+ metadataItemsFromArray:filteredByIdentifier:](<avmetadataitem/metadataitems(from_filteredbyidentifier_).md>) 方法查找标识符为 [AVMetadataCommonIdentifierTitle](avmetadataidentifier/commonidentifiertitle.md) 的项目。

```swift
// Load the asset's metadata.
let metadata = try await asset.load(.metadata)
        
// Find the title in the common key space.
let titleItems = AVMetadataItem.metadataItems(from: metadata,
                                              filteredByIdentifier: .commonIdentifierTitle)
guard let item = titleItems.first else { return }
// Process the title item.
```

元数据项目的过滤方法返回的是项目集合，而不是单个实例。在很多情况下，返回的集合只包含一个元素，但如果媒体包含本地化的元数据，或者你正在从常用键空间检索数据而同一个值存在于多个键空间中，那么每个键空间都会返回一个不同的值。

### 查找特定的值

通过加载元数据项目的 [value](avpartialasyncproperty/value.md) 属性来获取它持有的数据，该属性是一个遵循 [NSCopying](../foundation/nscopying.md) 和 [NSObjectProtocol](../objectivec/nsobjectprotocol.md) 协议的对象。你可以手动把值转换为合适的类型，但使用元数据项目的类型转换属性更安全、更方便。不要加载 [value](avpartialasyncproperty/value.md) 属性，而是视情况加载它的 [stringValue](avpartialasyncproperty/stringvalue.md)、[numberValue](avpartialasyncproperty/numbervalue.md)、[dateValue](avpartialasyncproperty/datevalue.md) 或 [dataValue](avpartialasyncproperty/datavalue.md) 属性，把它转换为特定类型。例如，下面的代码清单展示如何把与一首 iTunes 音乐关联的插图作为数据值获取：

```swift
// The collection of iTunes metadata.
let iTunesMetadata = try await asset.loadMetadata(for: .iTunesMetadata)

// Filter metadata to find the asset's artwork.
guard let artworkItem = AVMetadataItem.metadataItems(from: iTunesMetadata,
                                                     filteredByIdentifier: .iTunesMetadataCoverArt).first else { return }

// Retrieve a Data object that contains the image data.
guard let imageData = try await artworkItem.load(.dataValue) else { return }
```

## 另请参阅

### 元数据

- [AVMetadataItem](avmetadataitem.md) — 音视频 asset 或其某个轨道的元数据项目。
- [AVMutableMetadataItem](avmutablemetadataitem.md) — 音视频 asset 或其某个轨道的可变元数据项目。
- [AVMetadataIdentifier](avmetadataidentifier.md) — 一种为元数据格式定义标识符的结构体。
- [AVMetadataKey](avmetadatakey.md) — 一种定义元数据键的结构体。
- [AVMetadataKeySpace](avmetadatakeyspace.md) — 一种定义元数据键空间的结构体。
- [AVMetadataExtraAttributeKey](avmetadataextraattributekey.md) — 一种为额外元数据特性定义键的结构体。
- [AVMetadataFormat](avmetadataformat.md) — 一种定义元数据格式的结构体。
- [AVMetadataItemFilter](avmetadataitemfilter.md) — 一个从元数据项目中过滤所选信息的对象。
