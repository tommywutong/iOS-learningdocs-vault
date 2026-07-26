---
title: slow-motion-video
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/slow-motion-video/'
original_language: zh
published: 2019-09-08
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:47321c90dc99215a'
translated: n/a
---

> 原文：[slow-motion-video](https://dirtmelon.github.io/posts/slow-motion-video/)　·　dirtmelon

## 起因

有用户反馈上传慢动作视频后，视频为正常状态的视频，而不是慢动作视频，在视频列表界面中显示的视频时间长度也不正确。 打开系统相处进行查看时，显示的视频时间长度也是正常状态的视频时间长度，而不是慢动作状态下的视频时间长度，但是打开播放后就是慢动作视频。 系统提供了编辑慢动作视频的功能，可以选择慢动作区域，由此可以推测出，系统存取在相册中的是正常状态下的视频， 在播放时在通过视频的对应信息来控制播放的速度。 那么如何导出正确的视频资源和显示正确的视频时间呢？

## 播放对应的视频和显示正确的时间

### 播放对应的视频

无论播放的视频是什么类型，都是通过 `PHAsset` 获取到对应的 `AVAsset` ，然后通过 `AVAsset` 进行播放。 在通过 `PHAsset` 获取 `AVAsset` 时，是通过以下方法来获取：

```swift
let imageManager = PHCachingImageManager()
let requestOptions = PHVideoRequestOptions()
requestOptions.version = .original
imageManager.requestAVAsset(forVideo: asset,
                            options: requestOptions,
                            resultHandler: { (asset, audioMix, info) in
})
```

`PHVideoRequestOptions` 有个 `version` 的属性，可用于设置获取到的 `AVAsset` 对应的资源是哪个，再结合相册里面的是正常的视频，可以得出如果设置 `version` 为 `original` ，获取的 `AVAsset` 对应的是正常的视频资源。`version` 还可以设置 `current` ，再设置为 `current` 后，使用 `AVPlayer` 播放的就是慢动作的视频了。

### 显示正确的时间

`PHAsset` 有个 `duration` 属性，一般情况下使用 `PHAsset` 的 `duration` 既可，系统相册估计也是直接使用 `duration` 来表示时间。但是，在遇到慢动作视频的时候，`duration` 显示的则是正常状态的视频时间长度，那么如何获取慢动作视频时间长度呢？我们从上面的代码已经可以获取到慢动作视频对应的 `AVAsset` ，直接使用 `AVAsset` 的 `duration` 属性，再转化为秒，就是慢动作视频的时间长度了：

```swift
let seconds = lround(CMTimeGetSeconds(avAsset.duration))
```

但是普通的视频是可以直接使用 `PHAsset` 的 `duration` ，大多数视频也都是正常视频，是否可以通过 `PHAsset` 判断是否为慢动作视频，从而选择不同的方式来获取视频时间。其实慢动作视频也是通过普通视频以慢动作方式播放出来，其本质还是普通视频，只是帧率比较高。而 `PHAsset` 有个 `mediaSubtypes` 属性，它是 `PHAssetMediaSubtype` 类型，而 `PHAssetMediaSubtype` 则有 `videoHighFrameRate` 这个选项，说明如下：

> High-frame-rate videos are created by the Slow-Mo feature in the Camera app on an iOS device.

可见 `PHAsset` 如果对应的是慢动作视频，那么它的 `mediaSubtype` 就会包含 `videoHighFrameRate` ，所以可以得出判断方式：

```swift
extension PHAsset {
	var isSlowMotionVideo: Bool {
    return mediaSubtypes.contains(PHAssetMediaSubtype.videoHighFrameRate)
  }
}
```

## 如何导出慢动作视频

有文章说到慢动作视频获取到的 `AVAsset` 为 `AVComposition` ，我在 iOS 13.1 和 iOS 12.4.1 上获取的都是 `AVURLAsset` 类，或许其它版本获取到的是 `AVComposition` 类，无论获取到的是 `AVURLAsset` 还是 `AVComposition` 类，我们在编辑视频时都以 video tracks 的最后一条 track 为依据即可。

## 参考文章

[Optimizing for Slow Motion Video in iOS](https://overflow.buffer.com/2016/02/29/slow-motion-video-ios/)
