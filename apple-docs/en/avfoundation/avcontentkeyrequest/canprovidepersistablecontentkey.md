---
title: canProvidePersistableContentKey
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeyrequest/canprovidepersistablecontentkey
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/canprovidepersistablecontentkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyrequest/canprovidepersistablecontentkey.json'
content_hash: 'sha256:3fca1c3d1ec61f3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeyRequest](../avcontentkeyrequest.md)

# canProvidePersistableContentKey

<sub>Instance Property</sub>

The content key request used to create a persistable content key or respond to a previous request with a persistable content key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var canProvidePersistableContentKey: Bool { get }
```

## Discussion

The value of this property is automatically set to `YES` when the receiver is provided to the content key session’s delegate via the [- contentKeySession:didProvidePersistableContentKeyRequest:](<../avcontentkeysessiondelegate/contentkeysession(__didprovide_)-2wdgz.md>) method. When this property is set to `YES`, the [- persistableContentKeyFromKeyVendorResponse:options:error:](<../avpersistablecontentkeyrequest/persistablecontentkey(fromkeyvendorresponse_options_).md>) method can be used to create a persistable content key from the response.

When this property is set to `NO` and there is a request for a persistable content key, send the [- respondByRequestingPersistableContentKeyRequest](<respondbyrequestingpersistablecontentkeyrequest().md>) method.

## See Also

### Getting content key request properties

- [identifier](identifier.md) — The identifier for the content key.
- [originatingRecipient](originatingrecipient.md) — The AVContentKeyRecipient which initiated this request, if any.
- [error](error.md) — The error description for a failed key request.
- [initializationData](initializationdata.md) — The data used to obtain a key response.
- [renewsExpiringResponseData](renewsexpiringresponsedata.md) — A Boolean value that indicates whether the content key request renews previously provided response data.
- [status](status-swift.property.md) — The current state of the content key request.
- [Status](status-swift.enum.md) — The status for a content key request.
