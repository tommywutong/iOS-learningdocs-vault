---
title: status
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeyrequest/status-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/status-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyrequest/status-swift.property.json'
content_hash: 'sha256:2c1d68b132bd9fcd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeyRequest](../avcontentkeyrequest.md)

# status

<sub>Instance Property</sub>

The current state of the content key request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var status: AVContentKeyRequest.Status { get }
```

## See Also

### Getting content key request properties

- [identifier](identifier.md) — The identifier for the content key.
- [originatingRecipient](originatingrecipient.md) — The AVContentKeyRecipient which initiated this request, if any.
- [canProvidePersistableContentKey](canprovidepersistablecontentkey.md) — The content key request used to create a persistable content key or respond to a previous request with a persistable content key.
- [error](error.md) — The error description for a failed key request.
- [initializationData](initializationdata.md) — The data used to obtain a key response.
- [renewsExpiringResponseData](renewsexpiringresponsedata.md) — A Boolean value that indicates whether the content key request renews previously provided response data.
- [Status](status-swift.enum.md) — The status for a content key request.
