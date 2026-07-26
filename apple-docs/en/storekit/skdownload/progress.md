---
title: progress
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+（16.0 起废弃）, iPadOS 6.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.8+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 6.2+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skdownload/progress
source_url: 'https://developer.apple.com/documentation/storekit/skdownload/progress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skdownload/progress.json'
content_hash: 'sha256:2aa60947bac672ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKDownload](../skdownload.md)

# progress

<sub>Instance Property</sub>

A value that indicates how much of the file has been downloaded.

> [!warning] Deprecated
> Hosted content is no longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var progress: Float { get }
```

## Discussion

The value of this property is a floating point number between `0.0` and `1.0`, inclusive, where `0.0` means no data has been download and `1.0` means all the data has been downloaded. Typically, your app uses the value of this property to update a user interface element, such as a progress bar, that displays how much of the file has been downloaded.

Do not use the value of this property to determine whether the download has completed. Instead, use the [downloadState](downloadstate.md) property.

## See Also

### Getting State Information

- [state](state.md) — The current state of the download object. _(deprecated)_
- [timeRemaining](timeremaining.md) — An estimated time, in seconds, to finish downloading the content. _(deprecated)_
- [SKDownloadTimeRemainingUnknown](../skdownloadtimeremainingunknown.md) — Indicates that the system cannot determine how much time is needed to finish downloading the content. _(deprecated)_
- [SKDownloadState](../skdownloadstate.md) — The states that a download operation can be in. _(deprecated)_
- [downloadState](downloadstate.md) — The current state of the download object. _(deprecated)_
