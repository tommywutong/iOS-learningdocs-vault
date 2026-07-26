---
title: PhotoKit 与 iCloud 图片
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/photokit-with-iCloud/'
original_language: zh
published: 2017-10-08
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:dd8e799e301c8822'
translated: n/a
---

> 原文：[PhotoKit 与 iCloud 图片](https://dirtmelon.github.io/posts/photokit-with-iCloud/)　·　dirtmelon

## 起因

公司的 app 在前段时间的改版中，需要自定义一个相册界面，调研了一轮开源控件，感觉没有找到比较满意的，就尝试自己写了一个，用了 `PhotoKit`。基本上用下来也没多大问题。

但是在处理iCloud图片的时候遇到了一个小问题。如果用户开启了`优化 iPhone 存储空间`，或者未加载好，`PhotoKit` 是会先拿到这些图片的缩略图，一般来说在相册列表显示多张图片时，为了防止占用内存过多，通常是调用 `requestImage(for:targetSize:contentMode:options:resultHandler:)` 来获取指定尺寸的图片资源，这时候如果你的相册列表显示的图片的尺寸跟缩略图的尺寸大小相同，是可以显示出来的。当你选择后，如果通过 `PHCachingImageManager` 或者 `PHImageManager` 调用 `requestImageData(for:options:resultHandler:)` 方法，你会发现 `resultHandler` 中的 `data` 为空。

## 解决

找到问题后开始着手解决。`PHImageRequestOptions` 中 `isNetworkAccessAllowed` 属性表示是否允许下载来自iCloud中的图片。设置为 `true` 之后调用 `requestImageData(for:options:resultHandler:)` 即可下载来自iCloud的图片。

为了不浪费用户的流量，应该加多一个网络状态判断，如果是手机网络，则弹窗确认是否要同步该iCloud图片。

同时为了更好的用户体验，对下载中的图片，在 UI 上应该加多一个 `loading` 的提示，针对这部分功能，我建了一个 `Dictionary` 来存储同步状态，`key` 为对应的 `PHObject` 的 `localIdentifier`，`value` 则为同步状态，每次 `cell` 复用时，都需要去检查是否存在对应的同步状态，有则对 UI 进行对应的修改。

## 其它问题

1. 获取相册专辑列表的时候，记得在设置对应的 `PHFetchOptions` 的 `predicate` 为 `NSPredicate(format: "estimatedAssetCount > 0")` ，过滤掉空的相册专辑。
2. 在 `cell` 复用时，记得调用 `cancelImageRequest:` 取消 `cell` 之前的加载请求。
