---
title: 使用 AVFoundation 播放和存储 HTTP Live Stream
framework: AVFoundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, Xcode 16.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/using-avfoundation-to-play-and-persist-http-live-streams
source_url: 'https://developer.apple.com/documentation/avfoundation/using-avfoundation-to-play-and-persist-http-live-streams'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/using-avfoundation-to-play-and-persist-http-live-streams.json'
content_hash: 'sha256:8d996703b8aeea7f'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [离线播放与存储](offline-playback-and-storage.md)

# 使用 AVFoundation 播放和存储 HTTP Live Stream

<sub>示例代码</sub>

播放 HTTP Live Stream（HLS），并将流存储到磁盘以便离线播放。

## 概述

此示例提供了一个 HTTP Live Stream（HLS）目录，你可以通过点击表格中对应流的行来播放。要管理流的下载，请点击表格中与该流关联的按钮。点击按钮会触发过渡到新的视图控制器（view controller），该控制器提供用于启动下载、取消正在进行的下载或从设备中删除已下载流的界面。

该示例创建并初始化了一个 [AVAssetDownloadConfiguration](avassetdownloadconfiguration.md)，并使用下载配置为流的下载创建了一个 [AVAssetDownloadTask](avassetdownloadtask.md)。该示例展示了如何设置一个主要的 [AVAssetDownloadContentConfiguration](avassetdownloadcontentconfiguration.md) 和至少一个要下载的辅助内容配置。

> [!note] 注意
> 此示例不支持保存 FairPlay Streaming (FPS) 内容。有关演示如何下载 FPS 内容的示例版本，请参阅 [FairPlay Streaming Server SDK](https://developer.apple.com/streaming/fps/)。

### 配置示例代码项目

在运行 iOS 15 或更高版本的实体设备或模拟器上构建并运行示例。

如果希望添加自己的流来使用此示例进行测试，请在 Xcode 项目的 `Streams.plist` 文件中添加一个条目。你需要为以下两个重要键提供值：

- **`name`** — 示例中 HLS 流的显示名称。
- **`playlist_url`** — HLS 流主播放列表的 URL。

如果添加的任何流未通过安全方式托管，你需要在 Xcode 项目的 `Info.plist` 文件中添加一个 App Transport Security (ATS) 例外。有关 ATS 和相关属性列表键的更多信息，请参见 [NSAppTransportSecurity](../bundleresources/information-property-list/nsapptransportsecurity.md)。

### 播放流

要播放项目，请点击表格中的一行。点击该项目会触发过渡到新的视图控制器（view controller）。作为该过渡的一部分，表格视图（table view）会创建一个 `AssetPlaybackManager` 实例，并将相应的媒体资源（asset）分配给它，如下例所示：

```swift
override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
    super.prepare(for: segue, sender: sender)

    if segue.identifier == AssetListTableViewController.presentPlayerViewControllerSegueID {
        guard let cell = sender as? AssetListTableViewCell,
            let playerViewControler = segue.destination as? AVPlayerViewController else { return }

        /*
         获取 destinationViewController 的引用，以便在稍后的 AssetPlaybackManager
         委托回调中使用。
         */
        playerViewController = playerViewControler

        // 加载新的 Asset 到 AssetPlaybackManager 中以供播放。
        AssetPlaybackManager.sharedManager.setAssetForPlayback(cell.asset)
    }
}
```

将 asset 分配给 `AssetPlaybackManager` 会使其为 asset 创建 `AVPlayerItem`，并在此过程中移除任何先前的 asset：

```swift
private var asset: Asset? {
    willSet {
        /// 移除任何先前的 KVO 观察者。
        guard let urlAssetObserver = urlAssetObserver else { return }
        
        urlAssetObserver.invalidate()
    }
    
    didSet {
        if let asset {
            Task {
                do {
                    if try await asset.urlAsset.load(.isPlayable) {
                        playerItem = AVPlayerItem(asset: asset.urlAsset)
                        player.replaceCurrentItem(with: playerItem)
                    } else {
                        // 该 asset 不可播放，因此重置播放器状态。
                        resetPlayer()
                    }
                } catch {
                    logger.error("Unable to load `isPlayable` property.")
                }
            }
        } else {
            resetPlayer()
        }
    }
}
```

`AssetPlaybackManager` 使用键值观察（KVO）监视 `AVPlayerItem` 对象的 `status`，并在 `status` 变为 `.readyToPlay`（可播放）时启动播放：

```swift
playerItemObserver = playerItem?.observe(\AVPlayerItem.status, options: [.new, .initial]) { [weak self] (item, _) in
    guard let strongSelf = self else { return }
    
    if item.status == .readyToPlay {
        if !strongSelf.readyForPlayback {
            strongSelf.readyForPlayback = true
            strongSelf.delegate?.streamPlaybackManager(strongSelf, playerReadyToPlay: strongSelf.player)
        }
    } else if item.status == .failed {
        let error = item.error
        
        logger.error("Error: \(String(describing: error?.localizedDescription))")
    }
```

### 下载流

当用户通过点击相应流表格视图单元格中的按钮来启动下载时，`AssetPersistenceManager` 的实例会调用以下函数，以使用 `AVAssetDownloadConfiguration` 创建一个 `AVAssetDownloadTask` 对象，用于为流的 [AVURLAsset](avurlasset.md) 下载多个 [AVMediaSelection](avmediaselection.md)：

```swift
func downloadStream(for asset: Asset) async throws {

    // 获取 asset 媒体选择组的默认媒体选择。
    let preferredMediaSelection = try await asset.urlAsset.load(.preferredMediaSelection)

    /*
     使用 `AVAssetDownloadConfiguration` 创建并初始化一个 `AVAssetDownloadTask`，
     用于在 `AVURLAsset` 上下载多个 `AVMediaSelection`。
     `AVAssetDownloadConfiguration` 中的 `primaryContentConfiguration`
     请求一个比特率高于资源中较低比特率变体的变体。
     */
    let config = AVAssetDownloadConfiguration(asset: asset.urlAsset, title: asset.stream.name)
    /// 主要内容配置设置。
    let primaryQualifier = AVAssetVariantQualifier(predicate: NSPredicate(format: "peakBitRate > 265000"))
    config.primaryContentConfiguration.variantQualifiers = [primaryQualifier]
    
    /// 使用上述配置好的 `AVAssetDownloadConfiguration` 创建 `AVAssetDownloadTask`。
    let task = assetDownloadURLSession.makeAssetDownloadTask(downloadConfiguration: config)

    /// 为了更好地追踪 `AVAssetDownloadTask`，将 `taskDescription` 设置为示例中唯一的值。
    task.taskDescription = asset.stream.name

    activeDownloadsMap[task] = asset
    
    /// 使用 `task.progress` 值在 UI 中提供下载进度更新。
    let progressObservation: NSKeyValueObservation = task.progress.observe(\.fractionCompleted) { progress, _ in
        Task { @MainActor in
            var userInfo = [String: Any]()
            userInfo[Asset.Keys.name] = asset.stream.name
            userInfo[Asset.Keys.percentDownloaded] = progress.fractionCompleted
            NotificationCenter.default.post(name: .AssetDownloadProgress, object: nil, userInfo: userInfo)
        }
    }
    self.progressObservers.append(progressObservation)

    task.resume()

    var userInfo = [String: Any]()
    userInfo[Asset.Keys.name] = asset.stream.name
    userInfo[Asset.Keys.downloadState] = Asset.DownloadState.downloading.rawValue
    userInfo[Asset.Keys.downloadSelectionDisplayName] = await displayNamesForSelectedMediaOptions(preferredMediaSelection)

    NotificationCenter.default.post(name: .AssetDownloadStateChanged, object: nil, userInfo: userInfo)
}
```

> [!note] 注意
> 你无法在 HTTP Live Stream 正在播放时保存它。如果尝试保存直播流，系统会抛出异常。只有视频点播 (VOD) 流支持离线播放。

### 取消正在进行的下载

点击相应流表格视图单元格中的按钮以显示附件视图，然后点击取消以停止下载流。`AssetPersistenceManager` 中的以下函数通过调用 `URLSessionTask` 的 [cancel()](<../foundation/urlsessiontask/cancel().md>) 方法来取消下载。

```swift
func cancelDownload(for asset: Asset) {
    var task: AVAssetDownloadTask?

    for (taskKey, assetVal) in activeDownloadsMap where asset == assetVal {
        task = taskKey
        break
    }

    task?.cancel()
}
```

### 从磁盘中删除已下载的流

点击相应流表格视图单元格中的按钮以显示附件视图，然后点击删除以删除已下载的流文件。`AssetPersistenceManager` 中的以下函数用于删除设备上已下载的流。首先，识别设备上文件对应的 asset URL，然后调用 `FileManager` 的 [removeItem(at:)](<../foundation/filemanager/removeitem(at_).md>) 方法来删除指定 URL 处的已下载流。

```swift
func deleteAsset(_ asset: Asset) {
    let userDefaults = UserDefaults.standard

    do {
        if let localFileLocation = localAssetForStream(withName: asset.stream.name)?.urlAsset.url {
            try FileManager.default.removeItem(at: localFileLocation)

            userDefaults.removeObject(forKey: asset.stream.name)

            var userInfo = [String: Any]()
            userInfo[Asset.Keys.name] = asset.stream.name
            userInfo[Asset.Keys.downloadState] = Asset.DownloadState.notDownloaded.rawValue

            NotificationCenter.default.post(name: .AssetDownloadStateChanged, object: nil,
                                            userInfo: userInfo)
        }
    } catch {
        logger.error("An error occured deleting the file: \(error)")
    }
}
```

### 衡量播放性能

> [!note] 注意
> 你可以在播放期间在控制台中查看各项性能指标。

例如，以下代码用于计算播放流所花费的总时间，该时间从 `AVPlayerItemAccessLog` 中获得：

```swift
var totalDurationWatched: Double {
    // 通过遍历访问日志（AccessLog）事件来计算已观看的总时长。
    var totalDurationWatched = 0.0
    if accessLog != nil && !accessLog!.events.isEmpty {
        for event in accessLog!.events where event.durationWatched > 0 {
                totalDurationWatched += event.durationWatched
        }
    }
    return totalDurationWatched
}
```

## 另请参阅

### Asset 下载

- [AVAssetDownloadURLSession](avassetdownloadurlsession.md) — 一个 URL 会话，用于创建和管理 asset 下载任务。
- [AVAssetDownloadTask](avassetdownloadtask.md) — 一个 URL 会话任务，用于将远程 asset 下载到设备以便离线播放。
- [AVAggregateAssetDownloadTask](avaggregateassetdownloadtask.md) — 为 asset 下载多个媒体选择的任务。 _(已废弃)_

## 下载

- [UsingAVFoundationToPlayAndPersistHTTPLiveStreams.zip](https://docs-assets.developer.apple.com/published/24fb505506c6/UsingAVFoundationToPlayAndPersistHTTPLiveStreams.zip)
