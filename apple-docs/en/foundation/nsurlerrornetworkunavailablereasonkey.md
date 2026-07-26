---
title: NSURLErrorNetworkUnavailableReasonKey
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlerrornetworkunavailablereasonkey
source_url: 'https://developer.apple.com/documentation/foundation/nsurlerrornetworkunavailablereasonkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlerrornetworkunavailablereasonkey.json'
content_hash: 'sha256:d1a175f81722d11f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSURLErrorNetworkUnavailableReasonKey

<sub>Global Variable</sub>

The reason the network was unavailable for a task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSURLErrorNetworkUnavailableReasonKey: String
```

## Discussion

The value associated with this key is an [NSNumber](nsnumber.md). For possible values, see [NSURLErrorNetworkUnavailableReason](nsurlerrornetworkunavailablereason.md).

## See Also

### Keys

- [NSURLErrorFailingURLErrorKey](nsurlerrorfailingurlerrorkey.md) — The URL which caused a load to fail.
- [NSURLErrorFailingURLPeerTrustErrorKey](nsurlerrorfailingurlpeertrusterrorkey.md) — The state of a failed SSL handshake.
- [NSURLErrorFailingURLStringErrorKey](nsurlerrorfailingurlstringerrorkey.md) — The URL which caused a load to fail. _(deprecated)_
- [NSURLErrorBackgroundTaskCancelledReasonKey](nsurlerrorbackgroundtaskcancelledreasonkey.md) — A key in the error dictionary that provides the reason for canceling a background task.
- [URL Session Background Task Cancellation Reasons](url-session-background-task-cancellation-reasons.md) — Reasons that indicate why the system canceled a background task.
- [NetworkUnavailableReason](urlerror/networkunavailablereason-swift.enum.md) — An enumeration of reasons explaining why a task couldn’t satisfy networking constraints.
