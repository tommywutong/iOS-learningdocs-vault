---
title: destinationURL
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（10.0 起废弃）, iPadOS 9.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetdownloadtask/destinationurl
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadtask/destinationurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadtask/destinationurl.json'
content_hash: 'sha256:e10d19010535090c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetDownloadTask](../avassetdownloadtask.md)

# destinationURL

<sub>Instance Property</sub>

The local file URL to where the task downloads the asset.

> [!warning] Deprecated
> Use the URL property of URLAsset instead

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var destinationURL: URL { get }
```

## See Also

### Accessing task information

- [URLAsset](urlasset.md) — The asset that this task downloads.
- [loadedTimeRanges](loadedtimeranges.md) — The time ranges of the downloaded media that are ready for playback. _(deprecated)_
- [options](options.md) — The configuration options for the task. _(deprecated)_
