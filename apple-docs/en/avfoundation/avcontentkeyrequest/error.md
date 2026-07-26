---
title: error
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeyrequest/error
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyrequest/error.json'
content_hash: 'sha256:7e4f5564ffda5783'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeyRequest](../avcontentkeyrequest.md)

# error

<sub>Instance Property</sub>

The error description for a failed key request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var error: (any Error)? { get }
```

## See Also

### Getting content key request properties

- [identifier](identifier.md) — The identifier for the content key.
- [originatingRecipient](originatingrecipient.md) — The AVContentKeyRecipient which initiated this request, if any.
- [canProvidePersistableContentKey](canprovidepersistablecontentkey.md) — The content key request used to create a persistable content key or respond to a previous request with a persistable content key.
- [initializationData](initializationdata.md) — The data used to obtain a key response.
- [renewsExpiringResponseData](renewsexpiringresponsedata.md) — A Boolean value that indicates whether the content key request renews previously provided response data.
- [status](status-swift.property.md) — The current state of the content key request.
- [Status](status-swift.enum.md) — The status for a content key request.
