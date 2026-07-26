---
title: AVAssetDownloadTaskMinimumRequiredPresentationSizeKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetdownloadtaskminimumrequiredpresentationsizekey
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadtaskminimumrequiredpresentationsizekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadtaskminimumrequiredpresentationsizekey.json'
content_hash: 'sha256:f38216858a86e9f2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetDownloadTaskMinimumRequiredPresentationSizeKey

<sub>Global Variable</sub>

A key that indicates the minimum presentation size of the variant to download.

> [!warning] Deprecated
> Use AVAssetDownloadConfiguration:variantQualifiers with predicateForPresentationWidth and predicateForPresentationHeight instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
let AVAssetDownloadTaskMinimumRequiredPresentationSizeKey: String
```

## Discussion

By default, a download task selects the variant with the largest media presentation size. To download a variant of a particular size, provide a [CGSize](../corefoundation/cgsize.md) value for this key.

## See Also

### Download option keys

- [AVAssetDownloadTaskMinimumRequiredMediaBitrateKey](avassetdownloadtaskminimumrequiredmediabitratekey.md) — A key that indicates the minimum bit rate of the variant to download. _(deprecated)_
- [AVAssetDownloadTaskMediaSelectionKey](avassetdownloadtaskmediaselectionkey.md) — A key that indicates which media selection to download. _(deprecated)_
- [AVAssetDownloadTaskMediaSelectionPrefersMultichannelKey](avassetdownloadtaskmediaselectionprefersmultichannelkey.md) — A key that indicates whether the task downloads media selections with support for multichannel playback, when available. _(deprecated)_
- [AVAssetDownloadTaskPrefersHDRKey](avassetdownloadtaskprefershdrkey.md) — A key that indicates whether the task downloads HDR instead of SDR video, when available. _(deprecated)_
- [AVAssetDownloadTaskPrefersLosslessAudioKey](avassetdownloadtaskpreferslosslessaudiokey.md) — A key that indicates whether the task downloads media selections in lossless audio format, when available. _(deprecated)_
