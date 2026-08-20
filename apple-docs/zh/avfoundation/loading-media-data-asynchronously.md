---
title: 异步加载媒体数据
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/loading-media-data-asynchronously
source_url: 'https://developer.apple.com/documentation/avfoundation/loading-media-data-asynchronously'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/loading-media-data-asynchronously.json'
content_hash: 'sha256:9d190eec9a9963e5'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [媒体资源](media-assets.md)

# 异步加载媒体数据

<sub>文章</sub>

使用语言级并发（concurrency）功能构建响应式 App，高效加载媒体数据。

## 概述

AVFoundation 使用 [AVAsset](avasset.md) 类来建模含时间线的视听媒体。创建 asset 是一种轻量级操作，因为它会推迟媒体数据的加载，直到真正需要时才进行。asset 加载数据的耗时取决于多种因素，包括媒体的体积、本地设备的能力以及远程网络状况。为了避免阻塞调用线程（thread），你必须异步加载媒体数据。

> [!important] 重要
> 从 iOS 16、tvOS 16、MacCatalyst 16 和 macOS 13 开始，AVFoundation 废弃（deprecated）了 [AVAsset](avasset.md)、[AVAssetTrack](avassettrack.md) 和 [AVMetadataItem](avmetadataitem.md) 中供 Swift 客户端使用的同步属性（property）和方法。此外，它也废弃了使用 [`- loadValuesAsynchronouslyForKeys:completionHandler:`](<avasynchronouskeyvalueloading/loadvaluesasynchronously(forkeys_completionhandler_).md>) 方法异步加载属性值的做法，转而推荐下文介绍的语法。

### 异步加载属性

该框架围绕两个关键类型构建了其异步属性加载能力：[AVAsyncProperty](avasyncproperty.md) 和 [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md)。框架使用 [AVAsyncProperty](avasyncproperty.md) 类来定义需要异步加载的属性的类型安全标识符，并使用 [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md) 协议（protocol）来定义对象异步加载属性的接口。[AVAsset](avasset.md)、[AVAssetTrack](avassettrack.md) 和 [AVMetadataItem](avmetadataitem.md) 都采用了此协议，协议为其提供了一个具有以下签名的异步 [load(_:isolation:)](<avasynchronouskeyvalueloading/load(__isolation_).md>) 方法：

```swift
public func load<T>(_ property: AVAsyncProperty<Self, T>) async throws -> T
```

在异步上下文中调用此方法，并指定 `await` 关键字，以指示执行可挂起，直到数据加载完成。如果属性成功加载，该方法会返回一个类型安全的值；如果加载失败，则抛出错误。

```swift
// 一个 CMTime 值。
let duration = try await asset.load(.duration)
// 该 asset 的 AVMetadataItem 数组。
let metadata = try await asset.load(.metadata)
```

如果你事先知道需要加载多个 asset 属性，可以使用 [load(_:isolation:)](<avasynchronouskeyvalueloading/load(__isolation_).md>) 方法的变体，该变体接受多个标识符并将其结果返回到一个元组（tuple）中。与加载单个属性值一样，同时加载多个属性也是类型安全的操作。

```swift
// 一个 CMTime 值和 AVMetadataItem 数组。
let (duration, metadata) = try await asset.load(.duration, .metadata)
```

> [!note] 注意
> 同时加载多个属性可使 AVFoundation 通过批量加载请求来优化性能。

### 确定属性状态

[AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md) 还提供了一个 [status(of:)](<avasynchronouskeyvalueloading/status(of_).md>) 方法，用于返回属性标识符的状态。它会返回一个 [Status](avasyncproperty/status.md) 值，该值使用下例中展示的 case 来指示属性值的状态：

```swift
// 确定 metadata 属性的已加载状态。
switch asset.status(of: .metadata) {
case .notYetLoaded:
    // 属性的初始状态。
case .loading:
    // asset 正在主动加载属性值。
case .loaded(let metadata):
    // 属性已可以正常使用。
case .failed(let error):
    // 属性值加载失败。
}
```

`.loaded` 和 `.failed` case 提供关联值。`.loaded` case 包含先前加载的属性值，`.failed` case 包含一个指示失败原因的错误。能够访问关联值，使你可以在单个步骤中执行诸如检查属性状态和访问其值等操作。

```swift
// 验证 metadata 属性处于已加载状态。
if case .loaded(let metadata) = asset.status(of: .metadata) {
    // 处理已加载的值。
    processMetadata(metadata)
}
```

### 过滤属性集合

某些属性提供值数组，例如 asset 的 [tracks](avpartialasyncproperty/tracks-44ptx.md) 或其 [metadata](avpartialasyncproperty/metadata-16qej.md)。在许多情况下，你只对其中一部分值感兴趣。[AVAsset](avasset.md) 和 [AVAssetTrack](avassettrack.md) 还提供了过滤其集合（collection）的方法，以仅保留你需要的值。例如，下面的代码列表确定了 asset 中包含的音频采样率。它调用 asset 的 [`- loadTracksWithMediaType:completionHandler:`](<avasset/loadtracks(withmediatype_completionhandler_).md>) 来仅检索其音频轨道。它遍历每个轨道并异步加载轨道的格式描述。最后，它从流描述中检索采样率并对结果进行排序。

```swift
// 异步加载 asset 的音频轨道。
let audioTracks = try await asset.loadTracks(withMediaType: .audio)
var allDescriptions = [CMFormatDescription]()
for track in audioTracks {
    // 异步加载每个音频轨道的格式描述。
    allDescriptions.append(contentsOf: try await track.load(.formatDescriptions))
}
// 收集唯一的采样率，并按从高到低排序。
let sampleRates = Set(allDescriptions).map {
    Float($0.audioStreamBasicDescription?.mSampleRate ?? 0)
}.sorted(by: { $0 > $1 })
```

使用 Swift 并发（Swift concurrency）和 AVFoundation 异步 API，即使是如上所示的高级检查，也能变成简洁的顺序式操作。
