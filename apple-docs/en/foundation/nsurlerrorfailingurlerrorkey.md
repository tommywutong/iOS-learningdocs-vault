---
title: NSURLErrorFailingURLErrorKey
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlerrorfailingurlerrorkey
source_url: 'https://developer.apple.com/documentation/foundation/nsurlerrorfailingurlerrorkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlerrorfailingurlerrorkey.json'
content_hash: 'sha256:a6fb089be84757dd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSURLErrorFailingURLErrorKey

<sub>Global Variable</sub>

The URL which caused a load to fail.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSURLErrorFailingURLErrorKey: String
```

## Discussion

The corresponding value is an [NSURL](nsurl.md) instance.

## See Also

### Keys

- [NSURLErrorFailingURLPeerTrustErrorKey](nsurlerrorfailingurlpeertrusterrorkey.md) — The state of a failed SSL handshake.
- [NSURLErrorFailingURLStringErrorKey](nsurlerrorfailingurlstringerrorkey.md) — The URL which caused a load to fail. _(deprecated)_
- [NSURLErrorBackgroundTaskCancelledReasonKey](nsurlerrorbackgroundtaskcancelledreasonkey.md) — A key in the error dictionary that provides the reason for canceling a background task.
- [URL Session Background Task Cancellation Reasons](url-session-background-task-cancellation-reasons.md) — Reasons that indicate why the system canceled a background task.
- [NSURLErrorNetworkUnavailableReasonKey](nsurlerrornetworkunavailablereasonkey.md) — The reason the network was unavailable for a task.
- [NetworkUnavailableReason](urlerror/networkunavailablereason-swift.enum.md) — An enumeration of reasons explaining why a task couldn’t satisfy networking constraints.
