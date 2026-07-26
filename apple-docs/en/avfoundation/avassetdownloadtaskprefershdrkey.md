---
title: AVAssetDownloadTaskPrefersHDRKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetdownloadtaskprefershdrkey
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadtaskprefershdrkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadtaskprefershdrkey.json'
content_hash: 'sha256:e9daae6c0491824a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetDownloadTaskPrefersHDRKey

<sub>Global Variable</sub>

A key that indicates whether the task downloads HDR instead of SDR video, when available.

> [!warning] Deprecated
> Use AVAssetDownloadConfiguration:variantQualifiers with assetVariantQualifierWithPredicate using [NSPredicate predicateWithFormat:@'videoAttributes.videoRange == %@', AVVideoRangePQ]

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
let AVAssetDownloadTaskPrefersHDRKey: String
```

## Discussion

By default, a download task prefers downloading HDR content. Provide a Boolean value of [false](../swift/false.md) to change this behavior.

## See Also

### Download option keys

- [AVAssetDownloadTaskMinimumRequiredMediaBitrateKey](avassetdownloadtaskminimumrequiredmediabitratekey.md) — A key that indicates the minimum bit rate of the variant to download. _(deprecated)_
- [AVAssetDownloadTaskMinimumRequiredPresentationSizeKey](avassetdownloadtaskminimumrequiredpresentationsizekey.md) — A key that indicates the minimum presentation size of the variant to download. _(deprecated)_
- [AVAssetDownloadTaskMediaSelectionKey](avassetdownloadtaskmediaselectionkey.md) — A key that indicates which media selection to download. _(deprecated)_
- [AVAssetDownloadTaskMediaSelectionPrefersMultichannelKey](avassetdownloadtaskmediaselectionprefersmultichannelkey.md) — A key that indicates whether the task downloads media selections with support for multichannel playback, when available. _(deprecated)_
- [AVAssetDownloadTaskPrefersLosslessAudioKey](avassetdownloadtaskpreferslosslessaudiokey.md) — A key that indicates whether the task downloads media selections in lossless audio format, when available. _(deprecated)_
