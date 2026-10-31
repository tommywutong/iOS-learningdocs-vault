---
title: 选择字幕和替代音轨
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/selecting-subtitles-and-alternative-audio-tracks
source_url: 'https://developer.apple.com/documentation/avfoundation/selecting-subtitles-and-alternative-audio-tracks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/selecting-subtitles-and-alternative-audio-tracks.json'
content_hash: 'sha256:ed246c9082be03b2'
translated: true
---

> 导航： [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Media playback](media-playback.md)

# 选择字幕和替代音轨

<sub>文章</sub>

通过添加用户母语的字幕和替代音轨，扩大你的 App 对用户的吸引力。

## 概述

作为开发者，你希望让你的 App 尽可能面向广泛的受众。扩大 App 影响面的方式之一，是以用户的母语向他们提供 App，同时为有听力障碍或其他辅助功能需求的用户提供支持。AVKit 和 AVFoundation 通过内置的支持简化了这些问题的处理：呈现字幕和隐藏式字幕，以及选择替代音频和视频轨道。如果你要构建自己的自定播放器，或者想呈现自己的媒体选择界面，可以使用 AVFoundation 的 [AVMediaSelectionGroup](avmediaselectiongroup.md) 和 [AVMediaSelectionOption](avmediaselectionoption.md) 类提供的功能。

### 获取可用的媒体选项

`AVMediaSelectionOption` 对源媒体中包含的替代音频、视频或文本轨道建模。媒体选项用于选择替代机位角度、呈现以用户母语配音的音频，或显示字幕和隐藏式字幕。你通过异步加载并调用 asset 的 [availableMediaCharacteristicsWithMediaSelectionOptions](avasset/availablemediacharacteristicswithmediaselectionoptions.md) 属性来确定有哪些可用的替代媒体呈现方式，该属性返回一个字符串数组，指示可用的媒体特性。可能的返回值包括 [AVMediaCharacteristicAudible](avmediacharacteristic/audible.md)（替代音轨）、[AVMediaCharacteristicVisual](avmediacharacteristic/visual.md)（替代视频轨道）和 [AVMediaCharacteristicLegible](avmediacharacteristic/legible.md)（字幕和隐藏式字幕）。

获取可用选项的数组之后，调用 asset 的 [- mediaSelectionGroupForMediaCharacteristic:](<avasset/mediaselectiongroup(formediacharacteristic_).md>) 方法，向它传入所需的特性。该方法返回关联的 `AVMediaSelectionGroup` 对象；如果指定特性不存在任何组，则返回 `nil`。

`AVMediaSelectionGroup` 充当一组互斥的 `AVMediaSelectionOption` 对象的容器。以下示例展示如何获取 asset 的媒体选择组并显示它们的可用选项：

```swift
for characteristic in asset.availableMediaCharacteristicsWithMediaSelectionOptions {
    print("\(characteristic)")

    // Retrieve the AVMediaSelectionGroup for the specified characteristic.
    if let group = asset.mediaSelectionGroup(forMediaCharacteristic: characteristic) {
        // Print its options.
        for option in group.options {
            print("  Option: \(option.displayName)")
        }
    }
}
```

对于一个包含音频和字幕媒体选项的 asset，其输出类似于以下内容：

```swift
[AVMediaCharacteristicAudible]
  Option: English
  Option: Spanish

[AVMediaCharacteristicLegible]
  Option: English
  Option: German
  Option: Spanish
  Option: French
```

### 选择所需的媒体选项

在你为某个特定媒体特性获取了 `AVMediaSelectionGroup` 对象并确定了所需的 `AVMediaSelectionOption` 对象之后，下一步就是选择它。你可以通过在活跃的 [AVPlayerItem](avplayeritem.md) 上调用 [- selectMediaOption:inMediaSelectionGroup:](<avplayeritem/select(__in_).md>) 来选择一个媒体选项。例如，要呈现该 asset 的西班牙语字幕选项，可以这样选择：

```swift
if let group = asset.mediaSelectionGroup(forMediaCharacteristic: AVMediaCharacteristicLegible) {
    let locale = Locale(identifier: "es-ES")
    let options =
        AVMediaSelectionGroup.mediaSelectionOptions(from: group.options, with: locale)
    if let option = options.first {
        // Select Spanish-language subtitle option
        playerItem.select(option, in: group)
    }
}
```

选择一个媒体选项后，它立即可供呈现。选择字幕或隐藏式字幕选项，会在 [AVPlayerViewController](../avkit/avplayerviewcontroller.md)、[AVPlayerView](../avkit/avplayerview.md) 和 [AVPlayerLayer](avplayerlayer.md) 提供的视频显示中显示关联的文本。选择替代音频或视频选项，会用新选择的媒体替换当前呈现的媒体。

[AVPlayer](avplayer.md) 的默认行为是根据用户的系统偏好自动选择媒体。要接管它进行媒体选择的时机，可把播放器的 [appliesMediaSelectionCriteriaAutomatically](avplayer/appliesmediaselectioncriteriaautomatically.md) 值设为 [false](../swift/false.md) 来禁用默认行为。

## 另请参阅

### 媒体选择

- [AVMediaSelection](avmediaselection.md) — 一个表示 asset 上媒体选择选项完整呈现的对象。
- [AVMediaSelectionGroup](avmediaselectiongroup.md) — 一个表示 asset 内媒体呈现的一组互斥选项的对象。
- [AVMediaSelectionOption](avmediaselectionoption.md) — 一个表示选项组内媒体呈现的某个具体选项的对象。
- [AVMutableMediaSelection](avmutablemediaselection.md) — 一个表示 asset 上媒体选择选项完整呈现的可变对象。
- [AVPlayerMediaSelectionCriteria](avplayermediaselectioncriteria.md) — 一个为播放器指定首选语言和媒体特性的对象。
- [AVCustomMediaSelectionScheme](avcustommediaselectionscheme.md) — 对于明确打算为 AVMediaSelectionOptions 提供替代选择界面而创作的内容，AVCustomMediaSelectionScheme 提供一组用于控制媒体呈现的自定设置。
- [AVMediaPresentationSelector](avmediapresentationselector.md) — 对于明确打算为 AVMediaSelectionOptions 提供替代选择界面而创作的内容，AVMediaPresentationSelector 表示一组互斥的设置。
- [AVMediaPresentationSetting](avmediapresentationsetting.md) — 对于明确打算为 AVMediaSelectionOptions 提供替代选择界面而创作的内容，AVMediaPresentationSetting 表示一个用于控制媒体呈现的可选设置。
