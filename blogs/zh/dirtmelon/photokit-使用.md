---
title: PhotoKit-使用
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/photoKit-usage/'
original_language: zh
published: 2019-06-09
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d834b9a8f0701214'
translated: n/a
---

> 原文：[PhotoKit-使用](https://dirtmelon.github.io/posts/photoKit-usage/)　·　dirtmelon

## 相机胶卷

一般情况下我们都希望自定义相册界面时获取到的数据跟系统的相机胶卷数据是一致的。

`PHAsset` 中 有个 `fetchAssets(with:options:)` 的方法，可以获取到手机中全部的 `PHAsset` ，但是排序不对，而且系统的相机胶卷其实也是一个相册，所以还是要获取到对应的 `PHAssetCollection` 。

`PHAssetCollection` 中有 ` fetchAssetCollections(with:subtype:options:)` 方法来获取相册。需要指定 `PHAssetCollectionType` 和 `PHAssetCollectionSubtype` 。先看第一个 `PHAssetCollectionType ` 参数，分为 `album` ，`smartAlbum` 和 `moment` 。相机胶卷在系统中属于智能相册，所以选择 `smartAlbum` 。再看第二个 `PHAssetCollectionSubtype` 参数，这里需要结合[官方文档]([PHAssetCollectionSubtype - Photos

Apple Developer Documentation](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype))来选择，从里面发现一个 `smartAlbumUserLibrary` 类型，它的描述如下：

> A smart album that groups all assets that originate in the user’s own library (as opposed to assets from iCloud Shared Albums).

包含了所有 assets ，这个参数获取到的就是相机胶卷相册。调用如下：

```swift
PHAssetCollection.fetchAssetCollections(with: .smartAlbum,
                           	            subtype: .smartAlbumUserLibrary,
                                        options: nil)
```

## 相册的标题

如果没有在 项目的 Info -\> Localizations 中添加 Chinese 选项，则获取到的相册标题还是英文的。

![0784F52B-1A3C-4C15-AD50-984221746BF](https://raw.githubusercontent.com/dirtmelon/blog-images/main/0784F52B-1A3C-4C15-AD50-984221746BFC.png)

## 在 UICollectionView 中显示缩略图

在 UICollectionView 中显示缩略图的时候也需要考虑缩略图在本机中是不存在的，要从 iCloud 上下载下来，这样就需要设置 `PHImageRequestOptions` 的 `isNetworkAccessAllowed` 为 `true` 。

## 相册中的 GIF

需要获取到相册中的 GIF 并显示出来也是有讲究的，下面代码环境为 iOS 13 beta 。

### 如何判断是否为 GIF

1. 通过 KeyValue 形式访问 `uniformTypeIdentifier` 属性，再判断是否等于 `kUTTypeGIF` 。

```swift
extension PHAsset {
	  var isGIF: Bool {
	      if let imageType = value(forKey: "uniformTypeIdentifier") as? String,
   		  imageType == kUTTypeGIF as String {
                return  true
          }
		return false
	}
}
```

1. 获取 `PHAsset` 对应的 `PHAssetResource` ，通过 `uniformTypeIdentifier` 或者 `originalFilename` 来判断是否为 GIF 。

通过 `originalFilename` 的文件后缀判断，文件后缀判断一个不好的地方是有 GIF 也有 gif ，可能是因为 iOS 13 beta 版的关系。

```swift
extension PHAsset {
    var isGIF: Bool {
        guard let filename = PHAssetResource.assetResources(for: self).first?.originalFilename,
            filename("GIF") || filename("gif") else {
                return false
        }
        return true
    }
}
```

通过 `uniformTypeIdentifier` 判断。

```swift
extension PHAsset {
    var isGIF: Bool {
        guard let assetResources = PHAssetResource.assetResources(for: self).first,
            assetResources.uniformTypeIdentifier == kUTTypeGIF as String else {
                return false
        }
        return true
    }
}
```

1. 通过获取 `PHAsset` 的元数据来判断，但是由于 `requestImageData(for:options:resultHandler:)` 获取的是整张原图的数据，消耗较大，不建议使用这个方法来判断是否为 GIF 。

```swift
let requestOptions = PHImageRequestOptions()
requestOptions.version = .original

PHImageManager.default().requestImageData(for: asset,
                                          options: requestOptions) { (data, type, _, _) in
                                               guard let type = type,
                                                     type == kUTTypeGIF as String else {
                                                     	return
                                               	}
                                                	// This is GIF
                                                	print("This is GIF")
}
```

性能测试： 在 iOS 13 beta 1 ，iPhone 8P 上进行 2000 次判断是否为 GIF ，得到的时间消耗如下（单位为 s ）：

1. KeyValue 获取对应的属性进行比较 0.010032176971435547
2. `PHAssetResource` 的 `originalFilename` 的后缀判断 3.440941095352173
3. `PHAssetResource` 的 `uniformTypeIdentifier` 判断 3.4876623153686523

可以看到 `PHAssetResource` 的方法均消耗较大，所以采用第一种方法来判断是否为 GIF 。

### 如何显示 GIF

GIF 跟普通的照片不同，我们需要获取的是 GIF 的原始 `data` ，再由原始 `data` 生成 `UIImage` 。 在获取 `data` 时需要注意 GIF 有可能编辑过，如果有编辑过，则需要指定 `PHImageRequestOptions` 的 `version` 为 `.original` ，否则获取到有可能不是 GIF 的 `data` ，而是普通照片的 `data` 。
