---
title: timedOut
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeyrequest/retryreason/timedout
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/retryreason/timedout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyrequest/retryreason/timedout.json'
content_hash: 'sha256:2f202bdc2863e833'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVContentKeyRequest](../../avcontentkeyrequest.md) · [RetryReason](../retryreason.md)

# timedOut

<sub>Type Property</sub>

A key response that wasn’t set soon enough.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let timedOut: AVContentKeyRequest.RetryReason
```

## Discussion

The response timed out because the initial request or response (or both) took too long, or because the lease expired during the request.

## See Also

### Reasons for content key request retry

- [AVContentKeyRequestRetryReasonReceivedObsoleteContentKey](receivedobsoletecontentkey.md) — An obsolete key response that was set on the previous content key request.
- [AVContentKeyRequestRetryReasonReceivedResponseWithExpiredLease](receivedresponsewithexpiredlease.md) — A key response with an expired lease that was set on the previous content key request.
