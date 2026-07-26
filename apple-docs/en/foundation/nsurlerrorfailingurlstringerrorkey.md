---
title: NSURLErrorFailingURLStringErrorKey
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 4.0+（18.4 起废弃）, iPadOS 4.0+（18.4 起废弃）, Mac Catalyst 13.1+（18.4 起废弃）, macOS 10.6+（15.4 起废弃）, tvOS 9.0+（18.4 起废弃）, visionOS 1.0+（2.4 起废弃）, watchOS 2.0+（11.4 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsurlerrorfailingurlstringerrorkey
source_url: 'https://developer.apple.com/documentation/foundation/nsurlerrorfailingurlstringerrorkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlerrorfailingurlstringerrorkey.json'
content_hash: 'sha256:04340408e47a59cb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSURLErrorFailingURLStringErrorKey

<sub>Global Variable</sub>

The URL which caused a load to fail.

> [!warning] Deprecated
> Use NSURLErrorFailingURLErrorKey instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSURLErrorFailingURLStringErrorKey: String
```

## Discussion

The corresponding value is an [NSString](nsstring.md) object.

This constant supersedes [NSErrorFailingURLStringKey](nserrorfailingurlstringkey.md), which was deprecated starting in macOS 10.6.  Both constants refer to the same value for backward-compatibility, but this symbol name has a better prefix.

## See Also

### Keys

- [NSURLErrorFailingURLErrorKey](nsurlerrorfailingurlerrorkey.md) — The URL which caused a load to fail.
- [NSURLErrorFailingURLPeerTrustErrorKey](nsurlerrorfailingurlpeertrusterrorkey.md) — The state of a failed SSL handshake.
- [NSURLErrorBackgroundTaskCancelledReasonKey](nsurlerrorbackgroundtaskcancelledreasonkey.md) — A key in the error dictionary that provides the reason for canceling a background task.
- [URL Session Background Task Cancellation Reasons](url-session-background-task-cancellation-reasons.md) — Reasons that indicate why the system canceled a background task.
- [NSURLErrorNetworkUnavailableReasonKey](nsurlerrornetworkunavailablereasonkey.md) — The reason the network was unavailable for a task.
- [NetworkUnavailableReason](urlerror/networkunavailablereason-swift.enum.md) — An enumeration of reasons explaining why a task couldn’t satisfy networking constraints.
