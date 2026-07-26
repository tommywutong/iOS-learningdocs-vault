---
title: AVContentKeyRequest.Status
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeyrequest/status-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/status-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyrequest/status-swift.enum.json'
content_hash: 'sha256:7b79c5e2e91cb37a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeyRequest](../avcontentkeyrequest.md)

# AVContentKeyRequest.Status

<sub>Enumeration</sub>

The status for a content key request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Status
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Request status

- [AVContentKeyRequestStatusCancelled](status-swift.enum/cancelled.md) — The key request was canceled.
- [AVContentKeyRequestStatusFailed](status-swift.enum/failed.md) — The key request failed.
- [AVContentKeyRequestStatusReceivedResponse](status-swift.enum/receivedresponse.md) — The key request was received, and the key is in use.
- [AVContentKeyRequestStatusRenewed](status-swift.enum/renewed.md) — The key request was renewed.
- [AVContentKeyRequestStatusRequestingResponse](status-swift.enum/requestingresponse.md) — The key request was just created.
- [AVContentKeyRequestStatusRetried](status-swift.enum/retried.md) — The key request was retried.

### Initializers

- [init(rawValue:)](<status-swift.enum/init(rawvalue_).md>)

## See Also

### Getting content key request properties

- [identifier](identifier.md) — The identifier for the content key.
- [originatingRecipient](originatingrecipient.md) — The AVContentKeyRecipient which initiated this request, if any.
- [canProvidePersistableContentKey](canprovidepersistablecontentkey.md) — The content key request used to create a persistable content key or respond to a previous request with a persistable content key.
- [error](error.md) — The error description for a failed key request.
- [initializationData](initializationdata.md) — The data used to obtain a key response.
- [renewsExpiringResponseData](renewsexpiringresponsedata.md) — A Boolean value that indicates whether the content key request renews previously provided response data.
- [status](status-swift.property.md) — The current state of the content key request.
