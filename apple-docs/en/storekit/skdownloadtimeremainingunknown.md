---
title: SKDownloadTimeRemainingUnknown
framework: StoreKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 6.0+（16.0 起废弃）, iPadOS 6.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.14+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 6.2+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skdownloadtimeremainingunknown
source_url: 'https://developer.apple.com/documentation/storekit/skdownloadtimeremainingunknown'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skdownloadtimeremainingunknown.json'
content_hash: 'sha256:18895a9063226bf4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKDownloadTimeRemainingUnknown

<sub>Global Variable</sub>

Indicates that the system cannot determine how much time is needed to finish downloading the content.

> [!warning] Deprecated
> Hosted content is no longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var SKDownloadTimeRemainingUnknown: TimeInterval
```

## See Also

### Getting State Information

- [state](skdownload/state.md) — The current state of the download object. _(deprecated)_
- [progress](skdownload/progress.md) — A value that indicates how much of the file has been downloaded. _(deprecated)_
- [timeRemaining](skdownload/timeremaining.md) — An estimated time, in seconds, to finish downloading the content. _(deprecated)_
- [SKDownloadState](skdownloadstate.md) — The states that a download operation can be in. _(deprecated)_
- [downloadState](skdownload/downloadstate.md) — The current state of the download object. _(deprecated)_
