---
title: AVAssetDownloadTaskPrefersLosslessAudioKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.5+（27.0 起废弃）, iPadOS 14.5+（27.0 起废弃）, Mac Catalyst 14.5+（27.0 起废弃）, macOS 11.3+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetdownloadtaskpreferslosslessaudiokey
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadtaskpreferslosslessaudiokey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadtaskpreferslosslessaudiokey.json'
content_hash: 'sha256:d9d6c0dbcccbd71d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetDownloadTaskPrefersLosslessAudioKey

<sub>Global Variable</sub>

A key that indicates whether the task downloads media selections in lossless audio format, when available.

> [!warning] Deprecated
> Use AVAssetDownloadConfiguration:variantQualifiers with assetVariantQualifierWithPredicate using [NSPredicate predicateWithFormat:@'%d in audioAttributes.formatIDs', kAudioFormatAppleLossless]

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
let AVAssetDownloadTaskPrefersLosslessAudioKey: String
```

## Discussion

By default, a download task prefers downloading lossy audio formats. Provide a Boolean value of [true](../swift/true.md) to change this behavior.

## See Also

### Download option keys

- [AVAssetDownloadTaskMinimumRequiredMediaBitrateKey](avassetdownloadtaskminimumrequiredmediabitratekey.md) — A key that indicates the minimum bit rate of the variant to download. _(deprecated)_
- [AVAssetDownloadTaskMinimumRequiredPresentationSizeKey](avassetdownloadtaskminimumrequiredpresentationsizekey.md) — A key that indicates the minimum presentation size of the variant to download. _(deprecated)_
- [AVAssetDownloadTaskMediaSelectionKey](avassetdownloadtaskmediaselectionkey.md) — A key that indicates which media selection to download. _(deprecated)_
- [AVAssetDownloadTaskMediaSelectionPrefersMultichannelKey](avassetdownloadtaskmediaselectionprefersmultichannelkey.md) — A key that indicates whether the task downloads media selections with support for multichannel playback, when available. _(deprecated)_
- [AVAssetDownloadTaskPrefersHDRKey](avassetdownloadtaskprefershdrkey.md) — A key that indicates whether the task downloads HDR instead of SDR video, when available. _(deprecated)_
