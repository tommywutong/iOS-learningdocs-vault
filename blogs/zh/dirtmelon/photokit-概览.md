---
title: PhotoKit-概览
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/photokit-overview/'
original_language: zh
published: 2019-04-23
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:283c4c8b7bca9fed'
translated: n/a
---

> 原文：[PhotoKit-概览](https://dirtmelon.github.io/posts/photokit-overview/)　·　dirtmelon

iOS 8 开始提供，分为 Photos 和 Photos UI 两部分。 作用：

- 从用户照片库中获取照片和视频资源，相册
- 添加，删除和修改资源或相册
- 编辑照片或者视频的内容或者元数据

![511_introducing_the_photos_frameworks-007](https://raw.githubusercontent.com/dirtmelon/blog-images/main/511_introducing_the_photos_frameworks-007.png)

## PhotoKit 对象模型

`PHObject` ，PhotoKit 中的基类，`PHAsset` ，`PHAssetCollection` ，`PHCollectionList` 和 `PHObjectPlaceholder` 都继承于它，只包含 `localIdentifier` 这个属性，用于判断是否相等和进行 hash 。

`PHAsset`，PhotoKit 中表示图片或者视频资源的模型，包含了媒体的元数据，如 `isFavorite` ，`location` ，`pixelWidth` 和 `pixelHeight` 等。通过 `PHAsset` 可以获取对应的图片或者视频。

`PHCollection` ，`PHAssetCollection` 和 `PHCollectionList` 继承的父类。

`PHAssetCollection` ，`PHAsset` 的集合，可以是相册，时刻或者智能相册。

`PHCollectionList` ，`PHCollection` 的集合，例如照片库中的时刻列表，年份列表或者用户创建的相册。

![511_introducing_the_photos_frameworks-021](https://raw.githubusercontent.com/dirtmelon/blog-images/main/511_introducing_the_photos_frameworks-021.png)

## 获取资源

获取对应资源的方法都由对应的类的类方法提供，它们都是以 fetchXXX 形式命名。PhotoKit 提供了一个 `PHFetchOptions` 类给我们设置提取时的排序和过滤方式。

基本上完整的流程如下：

首先生成 `PHFetchOptions` 对象（也可以不设置），对应的 options 参数设为 nil ，然后通过 `PHAsset` 的 fetch 方法获取所有资源或者单独视频类型：

```swift
let options = PHFetchOptions()
        allPhotosOptions.sortDescriptors = [NSSortDescriptor(key: "creationDate", ascending: true)]
let medias = PHAsset.fetchAssets(with: options)
let videos = PHAsset.fetchAssets(with: .video, options: nil)
```

也可以获取相册 `PHAssetCollection` 或者 `PHCollectionList` 的 fetch 方法先获取 `PHAssetCollection` ，然后通过 `PHAsset` 的 fetch 方法获取对应的 assets：

```swift
let smartAlbums = PHAssetCollection.fetchAssetCollections(with: .smartAlbum, subtype: .albumRegular, options: nil)
let userCollections = PHCollectionList.fetchTopLevelUserCollections(with: nil)

let assets = PHAsset.fetchAssets(in: collection, options: nil)
```

这些获取方法都是同步的，但是官方文档中有说明 PHFetchResult 对象会从照片库中动态加载需要资源，即使处理大量的数据时也可以提供良好的性能。

> Unlike an `NSArray object`, however, a `PHFetchResult object` dynamically loads its contents from the Photos library as needed, providing optimal performance even when handling a large number of results.

## Transient Collections

PhotoKit 提供了一些方法让我们可以创建临时的资源集合，但是它们不会存储到用户照片库，它只会保存在当前的运行时中。可以用于搜索结果，用户选择图片，获取内容，复用 View Controller 等。

## 获取照片或者视频

不同于获取资源时的同步方法，这里的方法大部分都是异步的，因为它们有可能是存在 iCloud ，需要下载至本地，有可能是极大的图片，处理需要一定的时间。PhotoKit 提供了 `PHImageManager` 类来获取照片或者视频。

`PHImageManager` 针对照片和视频提供了不同的获取方法：

1. 获取照片

```swift
 func requestImage(for: PHAsset, targetSize: CGSize, contentMode: PHImageContentMode, options: PHImageRequestOptions?, resultHandler: (UIImage?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID
```

直接获取 UIImage ，提供了 `targetSize` 和 `contentMode` 参数，`targetSize` 指明请求获取到的照片大小，如果我们用一个 `CollectionView` 来展示图片，就需要根据 `cellSize` 来指定图片的大小，以免图片过大造成卡顿和占用内存过多。`contentMode (PHImageContentMode)` 的用法跟 UIView 的 `contentMode` 类似，指定图片是按比例缩放还是按比例填充至 `targetSize` 。

```swift
func requestImageData(for: PHAsset, options: PHImageRequestOptions?, resultHandler: (Data?, String?, UIImage.Orientation, [AnyHashable : Any]?) -> Void) -> PHImageRequestID
```

获取图片的 `Data` ，无法指定目标 Data 的图片来源的大小。`resultHandler` 中的第二个属性表示 Data 的格式，在 iOS 12 上有可能是 `public.jpeg` ，`public.png` ， `public.heic` 或者`com.compuserve.gif`。

`PHImageRequestOptions` 对象决定了怎么获取图像，它有这些属性：

- ：

  ，分以下几种模式：

    - ，图片管理器会提供多次的结果来平衡图片质量和响应速度，也就是说有可能多次调用

      ，在准备好高质量的图片以前先返回一个较低质量的图片给你用于展示。
    - ，只返回高质量的图片。
    - ，如果高质量的图片无法快速加载，

      则提供低质量的图片，可以通过检查

      中的

      值来判断图片的质量。
- :

  ，图片管理器如何设置图像大小：

    - none ：不重新设置图像大小
    - .fast ：比 .exact 效率更高，但是有可能跟 targetSize 大小不一样
    - .exact ：返回图像必须和目标大小相匹配
- ：裁剪图片的部分区域，如果需要进行裁剪，

  必须为

  模式。
- 设为

  ，则

  不起作用。 iCloud 相关属性：
- ：

  ，如果图片没有存储在本地，且

  为

  ，图片管理器则从 iCloud 中下载。如果

  为

  ，则

  为 nil ，且可以通过

  中

  值来判断是否存储于 iCloud 中。
- ：`(Double, Error?, UnsafeMutablePointer

    - ：表示下载进度，从 0.0 到 1.0
    - ：当下载图片出错时 error 有值，否则为 nil
    - ：如果需要取消下载，则在

      里进行设置
    - ：提供这次图片请求的额外信息

1. 获取视频

```swift
func requestPlayerItem(forVideo: PHAsset, options: PHVideoRequestOptions?, resultHandler: (AVPlayerItem?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID
```

获取视频对应的 `AVPlayerItem` 对象，用于播放视频，异步加载。

```swift
func requestExportSession(forVideo: PHAsset,options: PHVideoRequestOptions?,exportPreset: String,resultHandler: (AVAssetExportSession?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID
```

获取视频对应的 `AVAssetExportSession` 对象，用于将视频数据保存到文件中，`exportPreset` 表示视频质量。

```swift
func requestAVAsset(forVideo: PHAsset,options: PHVideoRequestOptions?,resultHandler: (AVAsset?, AVAudioMix?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID
```

返回视频对应的 `AVFoundation` 的相关对象。

`PHVideoRequestOptions` 的用法跟 `PHImageRequestOptions` 类似。

1. iOS 9.1 后，新增了获取 Live Photo 的方法：

```swift
func requestLivePhoto(for: PHAsset, targetSize: CGSize, contentMode: PHImageContentMode, options: PHLivePhotoRequestOptions?, resultHandler: (PHLivePhoto?, [AnyHashable : Any]?) -> Void) -> PHImageRequestID
```

Live Photo 是一张图片，会捕获拍照前后的声音和动作。就像 `UIImage` 对象如何表示图像的即用形式一样，Live Photo 对象也准备好了声音，图片和动作用于表示 Live Photo 。显示 Live Photo 需要用到 `PHLivePhotoView` 。也可以使用 `requestImage(for:targetSize:contentMode:options:resultHandler:)` 方法来直接获取 `PHLivePhoto` 的图片。

## 滑动性能

当在 Collection View 上展示照片时，可以使用 `PHImageCachingManager` 来预先加载一些图像和将一些图像从缓存中移除。

![511_introducing_the_photos_frameworks-094](https://raw.githubusercontent.com/dirtmelon/blog-images/main/511_introducing_the_photos_frameworks-094.png)

滚动式预先加载有可能显示的 `PHAssets` ：

```swift
func startCachingImages(for: [PHAsset], targetSize: CGSize, contentMode: PHImageContentMode, options: PHImageRequestOptions?)
```

退出当前显示范围的 `PHAssets` 则停止缓存：

```swift
func stopCachingImages(for: [PHAsset],targetSize: CGSize,contentMode: PHImageContentMode,options: PHImageRequestOptions?)
```

也可以停止所有缓存：

```swift
func stopCachingImagesForAllAssets()
```

`PHImageCachingManager` 有个 `allowsCachingHighQualityImages` 属性，默认为 `true` ，用于是否缓存高质量图片。

我在 iPhone 8P ，iOS 12 上测试了下，是否使用 `startCaching` 和 `stopCaching` 对滚动流畅性影响不大。

`PHCachingImageManger` 应该有自己一套管理 `PHAsset` 相关内存的办法，因为我观察到在滑动停止后，内存会逐渐下降至一个稳定值。

## 观察相册变化

在打开用户照片相关界面后，用户有可能切换至其它 app ，并对相册进行修改，对此，我们需要监听相册变化变化的通知，作出对应的处理。

```swift
PHPhotoLibrary.shared().register(self)
```

然后在遵循 `PHPhotoLibraryChangeObserver` 协议，在相册变化时会调用 `photoLibraryDidChange` 方法，我们需要在里面对相册内容进行处理，注意：`photoLibraryDidChange` 有可能是在后台线程中调用，所以需要手动切换为主线程。

```swift
extension Class: PHPhotoLibraryChangeObserver {
	func photoLibraryDidChange(_ changeInstance: PHChange) {
	}
}
```

`PHChange` 提供了两个方法用于获取变化的数据：

```swift
func changeDetails<T>(for object: T) -> PHObjectChangeDetails<T>? where T : PHObject

func changeDetails<T>(for fetchResult: PHFetchResult<T>) -> PHFetchResultChangeDetails<T>? where T : PHObject
```

这里用到了泛型。 第一个方法可用于获取 `PHAsset` 对象相关的变化。 第二个方法可用于获取 `PHFetchResult` 的变化，主要应用于 UICollectionView/UITableView ，`PHFetchResultChangeDetails` 提供了 `removedIndexes` ， `insertedIndexes` ， `changedIndexes` 和 `enumerateMoves` 用于配合 UICollectionView/UITableView 的相关刷新方法。

## 参考

- https://objccn.io/issue-21-4/#Photo-metadata
- PHImageManager - NSHipster
- https://developer.apple.com/videos/play/wwdc2014/511/
