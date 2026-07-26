---
title: failureURLString
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（18.4 起废弃）, iPadOS 8.0+（18.4 起废弃）, Mac Catalyst 8.0+（18.4 起废弃）, macOS 10.10+（15.4 起废弃）, tvOS 9.0+（18.4 起废弃）, visionOS 1.0+（2.4 起废弃）, watchOS 2.0+（11.4 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/urlerror/failureurlstring
source_url: 'https://developer.apple.com/documentation/foundation/urlerror/failureurlstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlerror/failureurlstring.json'
content_hash: 'sha256:e7f0d62eb21b5df7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLError](../urlerror.md)

# failureURLString

<sub>Instance Property</sub>

The string for the URL which caused a load to fail.

> [!warning] Deprecated
> Use failingURL instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var failureURLString: String? { get }
```

## See Also

### Error details

- [failingURL](failingurl.md) — The URL which caused a load to fail.
- [failureURLPeerTrust](failureurlpeertrust.md) — The state of a failed SSL handshake.
- [downloadTaskResumeData](downloadtaskresumedata.md) — An opaque data object used to resume a failed download task.
- [backgroundTaskCancelledReason](backgroundtaskcancelledreason-swift.property.md) — The reason for canceling a background task.
- [BackgroundTaskCancelledReason](backgroundtaskcancelledreason-swift.enum.md) — An enumeration of reasons used to explain the cancellation of a background task.
- [networkUnavailableReason](networkunavailablereason-swift.property.md) — The reason the network was unavailable for a task.
- [NetworkUnavailableReason](networkunavailablereason-swift.enum.md) — An enumeration of reasons explaining why a task couldn’t satisfy networking constraints.
