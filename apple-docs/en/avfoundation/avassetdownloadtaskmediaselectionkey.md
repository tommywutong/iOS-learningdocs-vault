---
title: AVAssetDownloadTaskMediaSelectionKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetdownloadtaskmediaselectionkey
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadtaskmediaselectionkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadtaskmediaselectionkey.json'
content_hash: 'sha256:8e7407c191eb3afe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetDownloadTaskMediaSelectionKey

<sub>Global Variable</sub>

A key that indicates which media selection to download.

> [!warning] Deprecated
> Use AVAssetDownloadConfiguration:mediaSelections instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
let AVAssetDownloadTaskMediaSelectionKey: String
```

## Discussion

By default, a download task automatically retrieves all of an asset’s media selections. To download a specific media selection, provide an [AVMediaSelection](avmediaselection.md) object for this key.

## See Also

### Download option keys

- [AVAssetDownloadTaskMinimumRequiredMediaBitrateKey](avassetdownloadtaskminimumrequiredmediabitratekey.md) — A key that indicates the minimum bit rate of the variant to download. _(deprecated)_
- [AVAssetDownloadTaskMinimumRequiredPresentationSizeKey](avassetdownloadtaskminimumrequiredpresentationsizekey.md) — A key that indicates the minimum presentation size of the variant to download. _(deprecated)_
- [AVAssetDownloadTaskMediaSelectionPrefersMultichannelKey](avassetdownloadtaskmediaselectionprefersmultichannelkey.md) — A key that indicates whether the task downloads media selections with support for multichannel playback, when available. _(deprecated)_
- [AVAssetDownloadTaskPrefersHDRKey](avassetdownloadtaskprefershdrkey.md) — A key that indicates whether the task downloads HDR instead of SDR video, when available. _(deprecated)_
- [AVAssetDownloadTaskPrefersLosslessAudioKey](avassetdownloadtaskpreferslosslessaudiokey.md) — A key that indicates whether the task downloads media selections in lossless audio format, when available. _(deprecated)_
