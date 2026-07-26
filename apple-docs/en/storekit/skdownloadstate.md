---
title: SKDownloadState
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 6.0+（16.0 起废弃）, iPadOS 6.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.8+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 6.2+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skdownloadstate
source_url: 'https://developer.apple.com/documentation/storekit/skdownloadstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skdownloadstate.json'
content_hash: 'sha256:23669c458128a10b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKDownloadState

<sub>Enumeration</sub>

The states that a download operation can be in.

> [!warning] Deprecated
> Hosted content is no longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
@frozen enum SKDownloadState
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [SKDownloadStateWaiting](skdownloadstate/waiting.md) — Indicates that the download has not started yet. _(deprecated)_
- [SKDownloadStateActive](skdownloadstate/active.md) — Indicates that the content is currently being downloaded. _(deprecated)_
- [SKDownloadStatePaused](skdownloadstate/paused.md) — Indicates that your app paused the download. _(deprecated)_
- [SKDownloadStateFinished](skdownloadstate/finished.md) — Indicates that the content was successfully downloaded. _(deprecated)_
- [SKDownloadStateFailed](skdownloadstate/failed.md) — Indicates that an error occurred while the file was being downloaded. _(deprecated)_
- [SKDownloadStateCancelled](skdownloadstate/cancelled.md) — Indicates that your app canceled the download. _(deprecated)_

### Initializers

- [init(rawValue:)](<skdownloadstate/init(rawvalue_).md>) _(deprecated)_

## See Also

### Getting State Information

- [state](skdownload/state.md) — The current state of the download object. _(deprecated)_
- [progress](skdownload/progress.md) — A value that indicates how much of the file has been downloaded. _(deprecated)_
- [timeRemaining](skdownload/timeremaining.md) — An estimated time, in seconds, to finish downloading the content. _(deprecated)_
- [SKDownloadTimeRemainingUnknown](skdownloadtimeremainingunknown.md) — Indicates that the system cannot determine how much time is needed to finish downloading the content. _(deprecated)_
- [downloadState](skdownload/downloadstate.md) — The current state of the download object. _(deprecated)_
