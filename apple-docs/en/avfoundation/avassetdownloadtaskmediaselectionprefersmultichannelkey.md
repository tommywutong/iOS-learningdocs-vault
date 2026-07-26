---
title: AVAssetDownloadTaskMediaSelectionPrefersMultichannelKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetdownloadtaskmediaselectionprefersmultichannelkey
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadtaskmediaselectionprefersmultichannelkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadtaskmediaselectionprefersmultichannelkey.json'
content_hash: 'sha256:98926099949c24b3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetDownloadTaskMediaSelectionPrefersMultichannelKey

<sub>Global Variable</sub>

A key that indicates whether the task downloads media selections with support for multichannel playback, when available.

> [!warning] Deprecated
> Use AVAssetDownloadConfiguration:variantQualifiers with predicateForChannelCount instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
let AVAssetDownloadTaskMediaSelectionPrefersMultichannelKey: String
```

## Discussion

By default, download tasks retrieve the variant’s stereo audio and the most capable multichannel rendition available. Provide a Boolean value of [false](../swift/false.md) to disable this behavior.

## See Also

### Download option keys

- [AVAssetDownloadTaskMinimumRequiredMediaBitrateKey](avassetdownloadtaskminimumrequiredmediabitratekey.md) — A key that indicates the minimum bit rate of the variant to download. _(deprecated)_
- [AVAssetDownloadTaskMinimumRequiredPresentationSizeKey](avassetdownloadtaskminimumrequiredpresentationsizekey.md) — A key that indicates the minimum presentation size of the variant to download. _(deprecated)_
- [AVAssetDownloadTaskMediaSelectionKey](avassetdownloadtaskmediaselectionkey.md) — A key that indicates which media selection to download. _(deprecated)_
- [AVAssetDownloadTaskPrefersHDRKey](avassetdownloadtaskprefershdrkey.md) — A key that indicates whether the task downloads HDR instead of SDR video, when available. _(deprecated)_
- [AVAssetDownloadTaskPrefersLosslessAudioKey](avassetdownloadtaskpreferslosslessaudiokey.md) — A key that indicates whether the task downloads media selections in lossless audio format, when available. _(deprecated)_
