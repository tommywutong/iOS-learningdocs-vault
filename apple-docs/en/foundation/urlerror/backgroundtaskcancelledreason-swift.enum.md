---
title: URLError.BackgroundTaskCancelledReason
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlerror/backgroundtaskcancelledreason-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/urlerror/backgroundtaskcancelledreason-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlerror/backgroundtaskcancelledreason-swift.enum.json'
content_hash: 'sha256:0fdc660d870ea991'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLError](../urlerror.md)

# URLError.BackgroundTaskCancelledReason

<sub>Enumeration</sub>

An enumeration of reasons used to explain the cancellation of a background task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum BackgroundTaskCancelledReason
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Cancellation reasons

- [URLError.BackgroundTaskCancelledReason.backgroundUpdatesDisabled](backgroundtaskcancelledreason-swift.enum/backgroundupdatesdisabled.md) — A reason that indicates the system canceled the background task because background tasks are disabled.
- [URLError.BackgroundTaskCancelledReason.insufficientSystemResources](backgroundtaskcancelledreason-swift.enum/insufficientsystemresources.md) — A reason that indicates the system canceled the background task because it lacks sufficient resources to perform the task.
- [URLError.BackgroundTaskCancelledReason.userForceQuitApplication](backgroundtaskcancelledreason-swift.enum/userforcequitapplication.md) — A reason that indicates the system canceled the background task because the user force-quit the application.

## See Also

### Error details

- [failingURL](failingurl.md) — The URL which caused a load to fail.
- [failureURLPeerTrust](failureurlpeertrust.md) — The state of a failed SSL handshake.
- [failureURLString](failureurlstring.md) — The string for the URL which caused a load to fail. _(deprecated)_
- [downloadTaskResumeData](downloadtaskresumedata.md) — An opaque data object used to resume a failed download task.
- [backgroundTaskCancelledReason](backgroundtaskcancelledreason-swift.property.md) — The reason for canceling a background task.
- [networkUnavailableReason](networkunavailablereason-swift.property.md) — The reason the network was unavailable for a task.
- [NetworkUnavailableReason](networkunavailablereason-swift.enum.md) — An enumeration of reasons explaining why a task couldn’t satisfy networking constraints.
