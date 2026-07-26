---
title: downloadTaskResumeData
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlerror/downloadtaskresumedata
source_url: 'https://developer.apple.com/documentation/foundation/urlerror/downloadtaskresumedata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlerror/downloadtaskresumedata.json'
content_hash: 'sha256:29c3bff25b698374'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLError](../urlerror.md)

# downloadTaskResumeData

<sub>Instance Property</sub>

An opaque data object used to resume a failed download task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var downloadTaskResumeData: Data? { get }
```

## Discussion

Pass this object to [- downloadTaskWithResumeData:](<../urlsession/downloadtask(withresumedata_).md>) or [- downloadTaskWithResumeData:completionHandler:](<../urlsession/downloadtask(withresumedata_completionhandler_).md>) to create a new download task that can attempt to resume the failed download.

## See Also

### Error details

- [failingURL](failingurl.md) — The URL which caused a load to fail.
- [failureURLPeerTrust](failureurlpeertrust.md) — The state of a failed SSL handshake.
- [failureURLString](failureurlstring.md) — The string for the URL which caused a load to fail. _(deprecated)_
- [backgroundTaskCancelledReason](backgroundtaskcancelledreason-swift.property.md) — The reason for canceling a background task.
- [BackgroundTaskCancelledReason](backgroundtaskcancelledreason-swift.enum.md) — An enumeration of reasons used to explain the cancellation of a background task.
- [networkUnavailableReason](networkunavailablereason-swift.property.md) — The reason the network was unavailable for a task.
- [NetworkUnavailableReason](networkunavailablereason-swift.enum.md) — An enumeration of reasons explaining why a task couldn’t satisfy networking constraints.
