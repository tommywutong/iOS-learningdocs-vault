---
title: downloadState
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+（12.0 起废弃）, iPadOS 6.0+（12.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 9.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skdownload/downloadstate
source_url: 'https://developer.apple.com/documentation/storekit/skdownload/downloadstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skdownload/downloadstate.json'
content_hash: 'sha256:c6d45534cc81777d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKDownload](../skdownload.md)

# downloadState

<sub>Instance Property</sub>

The current state of the download object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var downloadState: SKDownloadState { get }
```

## Discussion

After you queue a download object, the payment queue object calls your transaction observer when the state of the download object changes. Your transaction observer should read the [downloadState](downloadstate.md) property and use it to determine how to proceed. For more information on the different states, see [SKDownloadState](../skdownloadstate.md).

## See Also

### Getting State Information

- [state](state.md) — The current state of the download object. _(deprecated)_
- [progress](progress.md) — A value that indicates how much of the file has been downloaded. _(deprecated)_
- [timeRemaining](timeremaining.md) — An estimated time, in seconds, to finish downloading the content. _(deprecated)_
- [SKDownloadTimeRemainingUnknown](../skdownloadtimeremainingunknown.md) — Indicates that the system cannot determine how much time is needed to finish downloading the content. _(deprecated)_
- [SKDownloadState](../skdownloadstate.md) — The states that a download operation can be in. _(deprecated)_
