---
title: 时间音高算法设置
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/time-pitch-algorithm-settings
source_url: 'https://developer.apple.com/documentation/avfoundation/time-pitch-algorithm-settings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/time-pitch-algorithm-settings.json'
content_hash: 'sha256:c6b5fa8327e6b610'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [音频设置](audio-settings.md)

# 时间音高算法设置

<sub>API 集合</sub>

定义时间音高算法取值的常量。

## 概述

在 iOS 和 macOS 上，对于链接时以 iOS 15 或 macOS 12 及更高版本为目标的 App，默认的播放算法是 [AVAudioTimePitchAlgorithmTimeDomain](avaudiotimepitchalgorithm/timedomain.md)。

对于 iOS 15 之前的 iOS 版本，默认值为 [AVAudioTimePitchAlgorithmLowQualityZeroLatency](avaudiotimepitchalgorithm/lowqualityzerolatency.md)；对于 macOS 12 之前的 macOS 版本，默认值为 [AVAudioTimePitchAlgorithmSpectral](avaudiotimepitchalgorithm/spectral.md)。

导出和其他离线处理的默认值为 [AVAudioTimePitchAlgorithmSpectral](avaudiotimepitchalgorithm/spectral.md)。

对于缩放音频编辑（例如 [AVAssetTrackSegment](avassettracksegment.md) 的 [timeMapping](avassettracksegment/timemapping.md) 位于时长不等的 `timeRanges` 之间时），选择一个能够支持源媒体中出现的全部编辑速率范围的算法非常重要。假定你希望无论编辑速率如何都保持恒定的音高，那么音高算法 [AVAudioTimePitchAlgorithmSpectral](avaudiotimepitchalgorithm/spectral.md) 因其支持的速率范围非常宽泛而往往是最佳选择。如果你希望音高随编辑速率而变化，则 [AVAudioTimePitchAlgorithmVarispeed](avaudiotimepitchalgorithm/varispeed.md) 是最佳选择。

## 主题

### 常量

- [AVAudioTimePitchAlgorithmTimeDomain](avaudiotimepitchalgorithm/timedomain.md) — 一种质量适中、适用于语音的时间音高算法。
- [AVAudioTimePitchAlgorithmVarispeed](avaudiotimepitchalgorithm/varispeed.md) — 一种高质量、但不执行音高校正的时间音高算法。
- [AVAudioTimePitchAlgorithmSpectral](avaudiotimepitchalgorithm/spectral.md) — 一种质量最高、适用于音乐的时间音高算法。
- [AVAudioTimePitchAlgorithmLowQualityZeroLatency](avaudiotimepitchalgorithm/lowqualityzerolatency.md) — 一种低质量且计算开销非常低的音高算法。 _(已废弃)_

## 另请参阅

### 设置

- [采样率转换设置](sample-rate-conversion-settings.md) — 定义采样率转换器音频质量设置的常量。
- [AVAudioQuality](../avfaudio/avaudioquality.md) — 为编码和转换指定采样率音频质量的值。
- [编码器设置](encoder-settings.md) — 为音频录制器类定义音频编码器设置的常量。
