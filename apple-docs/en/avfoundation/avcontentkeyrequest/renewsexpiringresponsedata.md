---
title: renewsExpiringResponseData
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeyrequest/renewsexpiringresponsedata
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/renewsexpiringresponsedata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyrequest/renewsexpiringresponsedata.json'
content_hash: 'sha256:445e835f646e70e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeyRequest](../avcontentkeyrequest.md)

# renewsExpiringResponseData

<sub>Instance Property</sub>

A Boolean value that indicates whether the content key request renews previously provided response data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var renewsExpiringResponseData: Bool { get }
```

## Discussion

The value of this property is `YES` if the request renews previously provided response data that is expiring or has already expired.

## See Also

### Getting content key request properties

- [identifier](identifier.md) — The identifier for the content key.
- [originatingRecipient](originatingrecipient.md) — The AVContentKeyRecipient which initiated this request, if any.
- [canProvidePersistableContentKey](canprovidepersistablecontentkey.md) — The content key request used to create a persistable content key or respond to a previous request with a persistable content key.
- [error](error.md) — The error description for a failed key request.
- [initializationData](initializationdata.md) — The data used to obtain a key response.
- [status](status-swift.property.md) — The current state of the content key request.
- [Status](status-swift.enum.md) — The status for a content key request.
