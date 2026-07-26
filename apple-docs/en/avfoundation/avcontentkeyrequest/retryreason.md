---
title: AVContentKeyRequest.RetryReason
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeyrequest/retryreason
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/retryreason'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyrequest/retryreason.json'
content_hash: 'sha256:f62d5d40244c464b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeyRequest](../avcontentkeyrequest.md)

# AVContentKeyRequest.RetryReason

<sub>Structure</sub>

The reason for asking the client to retry a content key request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct RetryReason
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Reasons for content key request retry

- [AVContentKeyRequestRetryReasonReceivedObsoleteContentKey](retryreason/receivedobsoletecontentkey.md) — An obsolete key response that was set on the previous content key request.
- [AVContentKeyRequestRetryReasonReceivedResponseWithExpiredLease](retryreason/receivedresponsewithexpiredlease.md) — A key response with an expired lease that was set on the previous content key request.
- [AVContentKeyRequestRetryReasonTimedOut](retryreason/timedout.md) — A key response that wasn’t set soon enough.

### Initializers

- [init(rawValue:)](<retryreason/init(rawvalue_).md>) — Creates a retry reason with a string.

## See Also

### Inspecting a request

- [contentKey](contentkey.md) — The generated content key.
- [contentKeySpecifier](contentkeyspecifier.md) — The requested content key specifier.
- [options](options.md) — A dictionary of options used to initialize key loading.
