---
title: failureURLPeerTrust
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlerror/failureurlpeertrust
source_url: 'https://developer.apple.com/documentation/foundation/urlerror/failureurlpeertrust'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlerror/failureurlpeertrust.json'
content_hash: 'sha256:2cc85fa0d9cde63a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLError](../urlerror.md)

# failureURLPeerTrust

<sub>Instance Property</sub>

The state of a failed SSL handshake.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var failureURLPeerTrust: SecTrust? { get }
```

## See Also

### Error details

- [failingURL](failingurl.md) — The URL which caused a load to fail.
- [failureURLString](failureurlstring.md) — The string for the URL which caused a load to fail. _(deprecated)_
- [downloadTaskResumeData](downloadtaskresumedata.md) — An opaque data object used to resume a failed download task.
- [backgroundTaskCancelledReason](backgroundtaskcancelledreason-swift.property.md) — The reason for canceling a background task.
- [BackgroundTaskCancelledReason](backgroundtaskcancelledreason-swift.enum.md) — An enumeration of reasons used to explain the cancellation of a background task.
- [networkUnavailableReason](networkunavailablereason-swift.property.md) — The reason the network was unavailable for a task.
- [NetworkUnavailableReason](networkunavailablereason-swift.enum.md) — An enumeration of reasons explaining why a task couldn’t satisfy networking constraints.
