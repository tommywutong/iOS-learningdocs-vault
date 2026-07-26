---
title: options
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetdownloadtask/options
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadtask/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadtask/options.json'
content_hash: 'sha256:dd117bccf5be788d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetDownloadTask](../avassetdownloadtask.md)

# options

<sub>Instance Property</sub>

The configuration options for the task.

> [!warning] Deprecated
> Use AVAssetDownloadConfiguration instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var options: [String : Any]? { get }
```

## See Also

### Accessing task information

- [URLAsset](urlasset.md) — The asset that this task downloads.
- [loadedTimeRanges](loadedtimeranges.md) — The time ranges of the downloaded media that are ready for playback. _(deprecated)_
- [destinationURL](destinationurl.md) — The local file URL to where the task downloads the asset. _(deprecated)_
