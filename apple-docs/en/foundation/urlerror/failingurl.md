---
title: failingURL
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlerror/failingurl
source_url: 'https://developer.apple.com/documentation/foundation/urlerror/failingurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlerror/failingurl.json'
content_hash: 'sha256:656936a182766b6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLError](../urlerror.md)

# failingURL

<sub>Instance Property</sub>

The URL which caused a load to fail.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var failingURL: URL? { get }
```

## See Also

### Error details

- [failureURLPeerTrust](failureurlpeertrust.md) — The state of a failed SSL handshake.
- [failureURLString](failureurlstring.md) — The string for the URL which caused a load to fail. _(deprecated)_
- [downloadTaskResumeData](downloadtaskresumedata.md) — An opaque data object used to resume a failed download task.
- [backgroundTaskCancelledReason](backgroundtaskcancelledreason-swift.property.md) — The reason for canceling a background task.
- [BackgroundTaskCancelledReason](backgroundtaskcancelledreason-swift.enum.md) — An enumeration of reasons used to explain the cancellation of a background task.
- [networkUnavailableReason](networkunavailablereason-swift.property.md) — The reason the network was unavailable for a task.
- [NetworkUnavailableReason](networkunavailablereason-swift.enum.md) — An enumeration of reasons explaining why a task couldn’t satisfy networking constraints.
