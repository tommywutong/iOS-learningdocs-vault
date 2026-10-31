---
title: 呈现章节标记
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/presenting-chapter-markers
source_url: 'https://developer.apple.com/documentation/avfoundation/presenting-chapter-markers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/presenting-chapter-markers.json'
content_hash: 'sha256:e330f6a8ec433213'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [媒体播放](media-playback.md)

# 呈现章节标记

<sub>文章</sub>

添加章节标记，让用户能够快速导览你的内容。

## 概述

章节标记让用户能够快速导览你的内容。[AVPlayerViewController](../avkit/avplayerviewcontroller.md) 如果在当前播放的资产中找到章节标记，就会自动呈现章节选择界面。当你想创建自己的自定章节选择界面时，也可以随时直接检索这些数据。

### 检索定时元数据

章节标记是一种定时元数据，只适用于资产时间线内的各个时间范围。你可以使用 [- chapterMetadataGroupsBestMatchingPreferredLanguages:](<avasset/chaptermetadatagroups(bestmatchingpreferredlanguages_).md>) 或 [- chapterMetadataGroupsWithTitleLocale:containingItemsWithCommonKeys:](<avasset/chaptermetadatagroups(withtitlelocale_containingitemswithcommonkeys_).md>) 方法来检索资产的章节元数据。在你异步加载资产的 [availableChapterLocales](avasset/availablechapterlocales.md) 键的值之后，这些方法就可以在不阻塞的情况下调用。

```swift
let asset = AVAsset(url: <# Asset URL #>)
let chapterLocalesKey = "availableChapterLocales"
 
asset.loadValuesAsynchronously(forKeys: [chapterLocalesKey]) {
    var error: NSError?
    let status = asset.statusOfValue(forKey: chapterLocalesKey, error: &error)
    if status == .loaded {
        let languages = Locale.preferredLanguages
        let chapterMetadata = asset.chapterMetadataGroups(bestMatchingPreferredLanguages: languages)
        // 处理章节元数据。
    }
    else {
        // 处理其他状态情况。
    }
}
```

### 将定时元数据转换为章节数据

上述方法返回的值是一个 [AVTimedMetadataGroup](avtimedmetadatagroup.md) 对象数组，每个对象表示一个单独的章节标记。[AVTimedMetadataGroup](avtimedmetadatagroup.md) 对象包含一个 [CMTimeRange](../coremedia/cmtimerange.md)（定义其元数据适用的时间范围）、一个表示章节标题的 [AVMetadataItem](avmetadataitem.md) 对象数组，以及可选的章节缩略图。下面的示例展示如何将 [AVTimedMetadataGroup](avtimedmetadatagroup.md) 数据转换为名为 `Chapter` 的自定模型对象数组，以传递给 App 的视图层。

```swift
func convertTimedMetadataGroupsToChapters(groups: [AVTimedMetadataGroup]) -> [Chapter] {
    return groups.map { group in
        // 检索标题元数据项。
        let titleItems = AVMetadataItem.metadataItems(from: group.items,
                                                      filteredByIdentifier: .commonIdentifierTitle)

        // 检索插图元数据项。
        let artworkItems = AVMetadataItem.metadataItems(from: group.items,
                                                        filteredByIdentifier: .commonIdentifierArtwork)

        var title = "Default Title"
        var image = UIImage(named: "placeholder")!

        if let titleValue = titleItems.first?.stringValue {
            title = titleValue
        }

        if let imgData = artworkItems.first?.dataValue, let imageValue = UIImage(data: imgData) {
            image = imageValue
        }

        return Chapter(time: group.timeRange.start, title: title, image: image)
    }
}
```

转换完相关数据后，你就可以构建章节选择界面，并使用章节对象的时间值，通过 [AVPlayer](avplayer.md) 对象的 [- seekToTime:](<avplayer/seek(to_)-87h2r.md>) 方法跳转当前呈现。

## 另请参阅

### 定时元数据

- [AVMetadataGroup](avmetadatagroup.md) — 与时间线片段关联的元数据项集合。
- [AVTimedMetadataGroup](avtimedmetadatagroup.md) — 在特定时间范围内有效可用的元数据项集合。
- [AVMutableTimedMetadataGroup](avmutabletimedmetadatagroup.md) — 在特定时间范围内有效可用的可变元数据项集合。
- [AVDateRangeMetadataGroup](avdaterangemetadatagroup.md) — 在特定日期范围内有效可用的元数据项集合。
- [AVMutableDateRangeMetadataGroup](avmutabledaterangemetadatagroup.md) — 在特定日期范围内有效可用的可变元数据项集合。
- [AVPlayerItemMediaDataCollector](avplayeritemmediadatacollector.md) — 媒体数据收集器的抽象基类。
- [AVPlayerItemMetadataCollector](avplayeritemmetadatacollector.md) — 一个用于捕获为 HTTP Live Streaming 资产定义的日期范围元数据的对象。
