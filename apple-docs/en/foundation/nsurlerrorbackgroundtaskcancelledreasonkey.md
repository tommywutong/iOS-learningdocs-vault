---
title: NSURLErrorBackgroundTaskCancelledReasonKey
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlerrorbackgroundtaskcancelledreasonkey
source_url: 'https://developer.apple.com/documentation/foundation/nsurlerrorbackgroundtaskcancelledreasonkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlerrorbackgroundtaskcancelledreasonkey.json'
content_hash: 'sha256:94c1ea952b29b3f8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSURLErrorBackgroundTaskCancelledReasonKey

<sub>Global Variable</sub>

A key in the error dictionary that provides the reason for canceling a background task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSURLErrorBackgroundTaskCancelledReasonKey: String
```

## Discussion

The value associated with this key is an [NSNumber](nsnumber.md). For a list of possible values, see URL Session Background Task Cancellation Reasons.

## See Also

### Keys

- [NSURLErrorFailingURLErrorKey](nsurlerrorfailingurlerrorkey.md) — The URL which caused a load to fail.
- [NSURLErrorFailingURLPeerTrustErrorKey](nsurlerrorfailingurlpeertrusterrorkey.md) — The state of a failed SSL handshake.
- [NSURLErrorFailingURLStringErrorKey](nsurlerrorfailingurlstringerrorkey.md) — The URL which caused a load to fail. _(deprecated)_
- [URL Session Background Task Cancellation Reasons](url-session-background-task-cancellation-reasons.md) — Reasons that indicate why the system canceled a background task.
- [NSURLErrorNetworkUnavailableReasonKey](nsurlerrornetworkunavailablereasonkey.md) — The reason the network was unavailable for a task.
- [NetworkUnavailableReason](urlerror/networkunavailablereason-swift.enum.md) — An enumeration of reasons explaining why a task couldn’t satisfy networking constraints.
