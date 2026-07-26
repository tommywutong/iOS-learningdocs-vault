---
title: Time pitch algorithm settings
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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Audio settings](audio-settings.md)

# Time pitch algorithm settings

<sub>API Collection</sub>

The constants that define the values for the time pitch algorithms.

## Overview

In iOS and macOS, the default algorithm for playback for apps linked on or after iOS 15 or macOS 12 is [AVAudioTimePitchAlgorithmTimeDomain](avaudiotimepitchalgorithm/timedomain.md).

For iOS versions prior to iOS 15, the default value is [AVAudioTimePitchAlgorithmLowQualityZeroLatency](avaudiotimepitchalgorithm/lowqualityzerolatency.md), and for macOS versions prior to macOS 12, the default value is [AVAudioTimePitchAlgorithmSpectral](avaudiotimepitchalgorithm/spectral.md).

The default value for export and other offline processing is [AVAudioTimePitchAlgorithmSpectral](avaudiotimepitchalgorithm/spectral.md).

For scaled audio edits, such as when the [timeMapping](avassettracksegment/timemapping.md) of an [AVAssetTrackSegment](avassettracksegment.md) is between `timeRanges` of unequal duration, it’s important to choose an algorithm that supports the full range of edit rates present in the source media. The pitch algorithm [AVAudioTimePitchAlgorithmSpectral](avaudiotimepitchalgorithm/spectral.md) is often the best choice due to the highly inclusive range of rates it supports, assuming that it’s desirable to maintain a constant pitch regardless of the edit rate. If it’s desirable to allow the pitch to vary with the edit rate, [AVAudioTimePitchAlgorithmVarispeed](avaudiotimepitchalgorithm/varispeed.md) is the best choice.

## Topics

### Constants

- [AVAudioTimePitchAlgorithmTimeDomain](avaudiotimepitchalgorithm/timedomain.md) — A modest quality time pitch algorithm that’s suitable for voice.
- [AVAudioTimePitchAlgorithmVarispeed](avaudiotimepitchalgorithm/varispeed.md) — A high-quality time pitch algorithm that doesn’t perform pitch correction.
- [AVAudioTimePitchAlgorithmSpectral](avaudiotimepitchalgorithm/spectral.md) — A highest-quality time pitch algorithm that’s suitable for music.
- [AVAudioTimePitchAlgorithmLowQualityZeroLatency](avaudiotimepitchalgorithm/lowqualityzerolatency.md) — A low-quality and very low computationally intensive pitch algorithm. _(deprecated)_

## See Also

### Settings

- [Sample rate conversion settings](sample-rate-conversion-settings.md) — The constants that define sample rate converter audio quality settings.
- [AVAudioQuality](../avfaudio/avaudioquality.md) — The values that specify the sample rate audio quality for encoding and conversion.
- [Encoder settings](encoder-settings.md) — The constants that define the audio encoder settings for the audio recorder class.
