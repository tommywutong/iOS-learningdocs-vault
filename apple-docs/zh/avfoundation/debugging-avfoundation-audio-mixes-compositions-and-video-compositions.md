---
title: 调试 AVFoundation 音频混合、合成与视频合成
framework: AVFoundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 13.5+, iPadOS 13.5+, Mac Catalyst 13.5+, Xcode 13.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/debugging-avfoundation-audio-mixes-compositions-and-video-compositions
source_url: 'https://developer.apple.com/documentation/avfoundation/debugging-avfoundation-audio-mixes-compositions-and-video-compositions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/debugging-avfoundation-audio-mixes-compositions-and-video-compositions.json'
content_hash: 'sha256:13b17d57d5ecf44c'
translated: true
---

> 导航： [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Video effects](video-effects.md)

# 调试 AVFoundation 音频混合、合成与视频合成

<sub>示例代码</sub>

解决创建合成、视频合成和音频混合时的常见问题。

## 概述

你完全可能用完全合法的值构建出精致而复杂的合成、视频合成和音频混合，却得到出乎意料的结果。这个示例代码项目把合成可视化地显示在屏幕上，并采用视频合成验证处理协议来调试合成与音频混合中的常见陷阱。

### 配置示例代码项目

- 使用 Xcode 13.4.1 或更高版本以及 Swift 5.5 或更高版本构建这个示例。
- 这个示例可在运行 iPadOS 13.5 或更高版本的实体设备上运行。

在任意受支持的设备上构建并运行该 App。使用播放、暂停和进度滑块控制，在屏幕上半部分播放和拖动浏览合成内容。屏幕下半部分的调试视图将合成、视频合成和音频混合可视化。

### 将合成可视化

_可视化_ 指的是查看合成的一张图示，而不是查看它的代码。这个示例实现了 `CompositionDebugView` 类，在屏幕上以视觉方式呈现构成合成的底层 [AVComposition](avcomposition.md)、[AVVideoComposition](avvideocomposition.md) 和 [AVAudioMix](avaudiomix.md) 对象。开发者可以把 `CompositionDebugView` 直接放进自己的 App。它是一个非交互式视图，开发者可以扩展它来绘制自己的视频指令。它有助于发现合成轨道、视频指令和音频混合中的任何重叠和空隙。

### 同步可视化后的合成

`PlayerViewController` 类有一个指向 `Main.storyboard` 中 `CompositionDebugView` 对象的 outlet。

```swift
@IBOutlet weak var compositionDebugView: CompositionDebugView!
```

`PlayerViewController` 创建一个 player item，使用 [AVPlayerViewController](../avkit/avplayerviewcontroller.md) 在屏幕上半部分显示合成，它提供了一个用于控制播放的原生用户界面。它用 `SimpleEditor` 从项目中的视频文件创建的合成、视频合成和音频混合来构建这个 player item。

```swift
// Create a player item from the simple editor composition.
self.playerItem = AVPlayerItem(asset: self.editor.composition())
/*
 Set the player item's video composition and audio mix playback
 settings from the corresponding values in the simple editor.
*/
self.playerItem.videoComposition = self.editor.videoComposition()
self.playerItem.audioMix = self.editor.audioMix()
```

为了让它的 player item 与 `CompositionDebugView` 同步，`PlayerViewController` 调用 `CompositionDebugView` 的 `synchronize` 函数，并把 player item 作为参数传入。

```swift
// Set the player item on the debug view to synchronize playback.
self.compositionDebugView.synchronize(with: self.playerItem)
```

`CompositionDebugView` 的 `synchronize` 函数使用传入的 player item 参数与自身的绘制保持同步。它根据与 player item 关联的合成、视频合成和音频混合来构建其可视化显示。

```swift
func synchronize(with playerItem: AVPlayerItem) {
    self.playerItem = playerItem
    
    if let composition = playerItem.asset as? AVMutableComposition {
        compositionTrackSegmentInfo = trackSegmentInfo(from: composition.tracks)
        duration = CMTimeMaximum(duration, composition.duration)
    }

    if let audioMix = playerItem.audioMix {
        volumeRampAsPoints = volumeRampPoints(from: audioMix, duration: duration)
    }

    if let videoComposition = playerItem.videoComposition {
        videoCompositionStages = videoCompStageInfo(from: videoComposition.instructions)
    }

    drawingLayer.setNeedsDisplay()
    self.setNeedsDisplay()
}
```

### 创建合成

`SimpleEditor` 类的初始化会创建一个 [AVMutableComposition](avmutablecomposition.md) 来合并这些视频。

```swift
private lazy var editorComposition: AVMutableComposition = {
    var comp = AVMutableComposition()
```

随后，`SimpleEditor` 初始化器调用 `createComposition` 函数把提供的视频剪辑拼接在一起。它把这些剪辑插入合成中交替出现的视频和音频轨道。

```swift
/*
 Place clips into alternating video and audio tracks in the composition,
 and overlap them with transitionDuration. Set up the video composition to cycle
 between "pass through A", "transition from A to B", and "pass through B".
*/
var nextClipStart = CMTime.zero
for clipIndex in 0..<clips.count {
    // Alternating targets: 0, 1, 0, 1, ...
    let asset = clips[clipIndex].asset
    let clipTimeRange = clips[clipIndex].availableTimeRange
    do {
        let clipVideoTrack = asset.tracks(withMediaType: AVMediaType.video)[0]
        try compVideoTrks[clipIndex % 2].insertTimeRange(clipTimeRange, of: clipVideoTrack, at: nextClipStart)
        let clipAudioTracks = asset.tracks(withMediaType: AVMediaType.audio)
        if clipAudioTracks.isEmpty {
            SimpleEditorUtils.display("Each clip must have an audio track.")
            return false
        }
        try compAudioTrks[clipIndex % 2].insertTimeRange(clipTimeRange, of: clipAudioTracks[0], at: nextClipStart)
```

这个示例让第一个剪辑的结尾与第二个剪辑的开头重叠，并在重叠期间为过渡效果创建时间范围。第一个剪辑以过渡结束，第二个剪辑以过渡开始。为了只为重叠期间设置过渡效果，这个示例在重叠期间启用合成，而在视频合成的其余部分禁用它。为此，该示例为每个剪辑创建一个不包括过渡期间的直通（passthrough）时间范围。这个直通时间范围指示视频合成器在不合成的情况下直接通过这些帧。

```swift
passThroughTimeRanges[clipIndex] = CMTimeRangeMake(start: nextClipStart, duration: clipTimeRange.duration)
if clipIndex > 0 {
    passThroughTimeRanges[clipIndex].start = CMTimeAdd(passThroughTimeRanges[clipIndex].start,
                    transitionDuration)
}
passThroughTimeRanges[clipIndex].duration = CMTimeSubtract(passThroughTimeRanges[clipIndex].duration,
                    transitionDuration)

/*
 The end of this clip overlaps the start of the next by
 transitionDuration.
*/
nextClipStart = CMTimeSubtract(CMTimeAdd(nextClipStart, clipTimeRange.duration), transitionDuration)

// Retain the time range for the transition to the next item.
if clipIndex + 1 < clips.count {
    transitionTimeRanges[clipIndex] = CMTimeRangeMake(start: nextClipStart, duration: transitionDuration)
}
```

### 创建视频合成和音频混合

`SimpleEditor` 类的初始化会创建一个 [AVMutableVideoComposition](avmutablevideocomposition.md) 来在剪辑之间应用效果，以及一个 [AVMutableAudioMix](avmutableaudiomix.md) 来混合音频轨道。

```swift
private var editorAudioMix = AVMutableAudioMix()

private lazy var editorVideoComposition: AVMutableVideoComposition = {
    var videoComp = AVMutableVideoComposition()
    // Every videoComposition needs these properties to be set:
    videoComp.frameDuration = CMTimeMake(value: 1, timescale: frameDuration)
    videoComp.renderSize = editorComposition.naturalSize
    return videoComp
}()
```

随后，`SimpleEditor` 初始化器调用 `createVideoCompAndAudioMix` 函数，在视频剪辑之间添加不透明度渐变过渡，并在音频轨道之间添加音量渐变。

```swift
instructions.append(passThroughInstruction)

if currIndex + 1 < clips.count {
    // Add a transition from clip i to clip i+1.
    let transitionInstruction = AVMutableVideoCompositionInstruction()
    transitionInstruction.timeRange = transitionTimeRanges[currIndex]
    let fromLayer = AVMutableVideoCompositionLayerInstruction(assetTrack:
                        compVideoTracks[alternatingIndex])
    let toLayer = AVMutableVideoCompositionLayerInstruction(assetTrack:
                    compVideoTracks[1 - alternatingIndex])
    // Sets an opacity ramp to apply during the specified time range.
    toLayer.setOpacityRamp(fromStartOpacity: 0.0, toEndOpacity: 1.0,
                        timeRange: transitionTimeRanges[currIndex])

    transitionInstruction.layerInstructions = [toLayer, fromLayer]

    instructions.append(transitionInstruction)

    // Add an audio mix to the first clip to fade in the volume ramps.
    let trackMix1 = AVMutableAudioMixInputParameters(track: compAudioTracks[0])
    trackMix1.setVolumeRamp(fromStartVolume: 1.0, toEndVolume: 0.0,
                            timeRange: transitionTimeRanges[0])

    trackMixArray.append(trackMix1)

    // Add an audio mix to the second clip to fade out the volume ramps.
    let trackMix2 = AVMutableAudioMixInputParameters(track: compAudioTracks[1])
    trackMix2.setVolumeRamp(fromStartVolume: 0.0, toEndVolume: 1.0,
                            timeRange: transitionTimeRanges[0])
    trackMix2.setVolumeRamp(fromStartVolume: 1.0, toEndVolume: 1.0,
                            timeRange: passThroughTimeRanges[1])
    trackMixArray.append(trackMix2)
}

editorAudioMix.inputParameters = trackMixArray
editorVideoComposition.instructions = instructions
```

### 调试视频合成

这个示例在 `SimpleEditor` 类中实现了 [AVVideoCompositionValidationHandling](avvideocompositionvalidationhandling.md) 协议方法来调试视频合成。这些方法用于识别错误，并指示在发现特定错误之后是否需要继续验证视频合成。

该示例对每个函数的实现都会显示一个相应的错误对话框，并返回 `false` 来停止对视频合成的任何进一步验证。更多信息参见 [AVVideoCompositionValidationHandling](avvideocompositionvalidationhandling.md) 文档。

```swift
func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingEmptyTimeRange timeRange: CMTimeRange) -> Bool {
        SimpleEditorUtils.display("Empty time range detected during validation.")
        return false // Stop validation after finding errors.
}

func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTimeRangeIn videoCompositionInstruction: AVVideoCompositionInstructionProtocol) -> Bool {
        SimpleEditorUtils.display("Invalid time range detected during validation.")
        return false // Stop validation after finding errors.
}

func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidValueForKey key: String) -> Bool {
        SimpleEditorUtils.display("Invalid value for \(key) detected during validation.")
        return false // Stop validation after finding errors.
}

func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTrackIDIn videoCompositionInstruction: AVVideoCompositionInstructionProtocol, layerInstruction: AVVideoCompositionLayerInstruction, asset: AVAsset) -> Bool {
        SimpleEditorUtils.display("Invalid track ID detected during validation.")
        return false // Stop validation after finding errors.
}
```

## 另请参阅

### 内置视频合成

- [编辑和播放 HDR 视频](editing-and-playing-hdr-video.md) — 使用 AVFoundation 的 HDR 编辑和播放能力，在你的 App 中支持高动态范围（HDR）视频内容。
- [AVVideoComposition](avvideocomposition.md) — 一个描述如何在特定时间点合成视频帧的对象。
- [AVVideoCompositionInstruction](avvideocompositioninstruction-swift.class.md) — 合成器执行的一个操作。
- [AVVideoCompositionLayerInstruction](avvideocompositionlayerinstruction.md) — 用于修改合成中给定轨道所应用的变换、裁剪和不透明度渐变的对象。
- [AVMutableVideoComposition](avmutablevideocomposition.md) — 可变的视频合成子类。 _(已废弃)_
- [AVMutableVideoCompositionInstruction](avmutablevideocompositioninstruction.md) — 可变的视频合成指令子类。 _(已废弃)_
- [AVMutableVideoCompositionLayerInstruction](avmutablevideocompositionlayerinstruction.md) — 用于修改可变合成中给定轨道所应用的变换、裁剪和不透明度渐变的对象。 _(已废弃)_

## 下载

- [DebuggingAVFoundationAudioMixesCompositionsAndVideoCompositions.zip](https://docs-assets.developer.apple.com/published/46bb8c54cf2e/DebuggingAVFoundationAudioMixesCompositionsAndVideoCompositions.zip)
