---
title: SKDownloadState.finished
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 6.0+（16.0 起废弃）, iPadOS 6.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.8+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 6.2+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skdownloadstate/finished
source_url: 'https://developer.apple.com/documentation/storekit/skdownloadstate/finished'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skdownloadstate/finished.json'
content_hash: 'sha256:5cb5969d182d3437'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKDownloadState](../skdownloadstate.md)

# SKDownloadState.finished

<sub>Case</sub>

Indicates that the content was successfully downloaded.

> [!warning] Deprecated
> Hosted content is no longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
case finished
```

## See Also

### Constants

- [SKDownloadStateWaiting](waiting.md) — Indicates that the download has not started yet. _(deprecated)_
- [SKDownloadStateActive](active.md) — Indicates that the content is currently being downloaded. _(deprecated)_
- [SKDownloadStatePaused](paused.md) — Indicates that your app paused the download. _(deprecated)_
- [SKDownloadStateFailed](failed.md) — Indicates that an error occurred while the file was being downloaded. _(deprecated)_
- [SKDownloadStateCancelled](cancelled.md) — Indicates that your app canceled the download. _(deprecated)_
