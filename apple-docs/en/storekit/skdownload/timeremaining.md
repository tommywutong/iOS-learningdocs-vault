---
title: timeRemaining
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+（16.0 起废弃）, iPadOS 6.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.8+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 6.2+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skdownload/timeremaining
source_url: 'https://developer.apple.com/documentation/storekit/skdownload/timeremaining'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skdownload/timeremaining.json'
content_hash: 'sha256:2a8c0309c0b7e7ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKDownload](../skdownload.md)

# timeRemaining

<sub>Instance Property</sub>

An estimated time, in seconds, to finish downloading the content.

> [!warning] Deprecated
> Hosted content is no longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var timeRemaining: TimeInterval { get }
```

## Discussion

The system attempts to estimate how long it will take to finish downloading the file. If it cannot create a good estimate, the value of this property is set to [SKDownloadTimeRemainingUnknown](../skdownloadtimeremainingunknown.md).

## See Also

### Getting State Information

- [state](state.md) — The current state of the download object. _(deprecated)_
- [progress](progress.md) — A value that indicates how much of the file has been downloaded. _(deprecated)_
- [SKDownloadTimeRemainingUnknown](../skdownloadtimeremainingunknown.md) — Indicates that the system cannot determine how much time is needed to finish downloading the content. _(deprecated)_
- [SKDownloadState](../skdownloadstate.md) — The states that a download operation can be in. _(deprecated)_
- [downloadState](downloadstate.md) — The current state of the download object. _(deprecated)_
