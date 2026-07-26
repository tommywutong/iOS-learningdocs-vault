---
title: AVAssetDownloadTaskMinimumRequiredMediaBitrateKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetdownloadtaskminimumrequiredmediabitratekey
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadtaskminimumrequiredmediabitratekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadtaskminimumrequiredmediabitratekey.json'
content_hash: 'sha256:18e1f63eda57482b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetDownloadTaskMinimumRequiredMediaBitrateKey

<sub>Global Variable</sub>

A key that indicates the minimum bit rate of the variant to download.

> [!warning] Deprecated
> Use AVAssetDownloadConfiguration:variantQualifiers with assetVariantQualifierWithPredicate using desired comparison value against averageBitRate/peakBitRate instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
let AVAssetDownloadTaskMinimumRequiredMediaBitrateKey: String
```

## Discussion

By default, a download task selects the highest bit rate variant available. To download a variant of a particular size, provide an [NSNumber](../foundation/nsnumber.md) value that indicates the preferred bit rate.

## See Also

### Download option keys

- [AVAssetDownloadTaskMinimumRequiredPresentationSizeKey](avassetdownloadtaskminimumrequiredpresentationsizekey.md) — A key that indicates the minimum presentation size of the variant to download. _(deprecated)_
- [AVAssetDownloadTaskMediaSelectionKey](avassetdownloadtaskmediaselectionkey.md) — A key that indicates which media selection to download. _(deprecated)_
- [AVAssetDownloadTaskMediaSelectionPrefersMultichannelKey](avassetdownloadtaskmediaselectionprefersmultichannelkey.md) — A key that indicates whether the task downloads media selections with support for multichannel playback, when available. _(deprecated)_
- [AVAssetDownloadTaskPrefersHDRKey](avassetdownloadtaskprefershdrkey.md) — A key that indicates whether the task downloads HDR instead of SDR video, when available. _(deprecated)_
- [AVAssetDownloadTaskPrefersLosslessAudioKey](avassetdownloadtaskpreferslosslessaudiokey.md) — A key that indicates whether the task downloads media selections in lossless audio format, when available. _(deprecated)_
