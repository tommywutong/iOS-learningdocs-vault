---
title: loadedTimeRanges
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetdownloadtask/loadedtimeranges
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetdownloadtask/loadedtimeranges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetdownloadtask/loadedtimeranges.json'
content_hash: 'sha256:4cde62172bdb9b26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetDownloadTask](../avassetdownloadtask.md)

# loadedTimeRanges

<sub>Instance Property</sub>

The time ranges of the downloaded media that are ready for playback.

> [!warning] Deprecated
> Use NSURLSessionTask.progress instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var loadedTimeRanges: [NSValue] { get }
```

## Discussion

The time ranges that this property provides may be discontinuous.

## See Also

### Accessing task information

- [URLAsset](urlasset.md) — The asset that this task downloads.
- [options](options.md) — The configuration options for the task. _(deprecated)_
- [destinationURL](destinationurl.md) — The local file URL to where the task downloads the asset. _(deprecated)_
