---
title: receivedObsoleteContentKey
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeyrequest/retryreason/receivedobsoletecontentkey
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/retryreason/receivedobsoletecontentkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyrequest/retryreason/receivedobsoletecontentkey.json'
content_hash: 'sha256:38b0d04112335fe2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVContentKeyRequest](../../avcontentkeyrequest.md) · [RetryReason](../retryreason.md)

# receivedObsoleteContentKey

<sub>Type Property</sub>

An obsolete key response that was set on the previous content key request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let receivedObsoleteContentKey: AVContentKeyRequest.RetryReason
```

## See Also

### Reasons for content key request retry

- [AVContentKeyRequestRetryReasonReceivedResponseWithExpiredLease](receivedresponsewithexpiredlease.md) — A key response with an expired lease that was set on the previous content key request.
- [AVContentKeyRequestRetryReasonTimedOut](timedout.md) — A key response that wasn’t set soon enough.
