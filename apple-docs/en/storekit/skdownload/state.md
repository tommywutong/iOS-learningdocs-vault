---
title: state
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+（16.0 起废弃）, iPadOS 12.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.8+（13.0 起废弃）, tvOS 12.0+（16.0 起废弃）, watchOS 6.2+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skdownload/state
source_url: 'https://developer.apple.com/documentation/storekit/skdownload/state'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skdownload/state.json'
content_hash: 'sha256:b9ddda892bcdc2fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKDownload](../skdownload.md)

# state

<sub>Instance Property</sub>

The current state of the download object.

> [!warning] Deprecated
> Hosted content is no longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var state: SKDownloadState { get }
```

## Discussion

After you queue a download object, the payment queue object calls your transaction observer when the state of the download object changes. Your transaction observer should read the [state](state.md) property and use it to determine how to proceed. For more information on the different states, see [SKDownloadState](../skdownloadstate.md).

## See Also

### Getting State Information

- [progress](progress.md) — A value that indicates how much of the file has been downloaded. _(deprecated)_
- [timeRemaining](timeremaining.md) — An estimated time, in seconds, to finish downloading the content. _(deprecated)_
- [SKDownloadTimeRemainingUnknown](../skdownloadtimeremainingunknown.md) — Indicates that the system cannot determine how much time is needed to finish downloading the content. _(deprecated)_
- [SKDownloadState](../skdownloadstate.md) — The states that a download operation can be in. _(deprecated)_
- [downloadState](downloadstate.md) — The current state of the download object. _(deprecated)_
