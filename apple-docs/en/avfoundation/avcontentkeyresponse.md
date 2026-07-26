---
title: AVContentKeyResponse
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeyresponse
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyresponse'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyresponse.json'
content_hash: 'sha256:bf5e31327f810587'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVContentKeyResponse

<sub>Class</sub>

An object that encapsulates information about a response to a content decryption key request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVContentKeyResponse
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating new content key responses

- [+ contentKeyResponseWithClearKeyData:initializationVector:](<avcontentkeyresponse/init(clearkeydata_initializationvector_).md>) — Creates a new key response object for key data and initialization vector sent in the clear.
- [+ contentKeyResponseWithFairPlayStreamingKeyResponseData:](<avcontentkeyresponse/init(fairplaystreamingkeyresponsedata_).md>) — Creates a content key response with an encrypted key response data blob when FairPlay Streaming is the key delivery method.
- [+ contentKeyResponseWithAuthorizationTokenData:](<avcontentkeyresponse/init(authorizationtokendata_).md>) — Creates a content key response with an authorization token.

## See Also

### FairPlay streaming

- [AVContentKeySession](avcontentkeysession.md) — An object that creates and tracks decryption keys for media data.
- [AVContentKeySessionDelegate](avcontentkeysessiondelegate.md) — A protocol that handles content key requests.
- [AVContentKey](avcontentkey.md) — An object that represents the content key decryptor.
- [AVContentKeySpecifier](avcontentkeyspecifier.md) — An object that uniquely identifies a content key.
- [AVContentKeyRequest](avcontentkeyrequest.md) — An object that encapsulates information about a content decryption key request issued from a content key session object.
- [AVPersistableContentKeyRequest](avpersistablecontentkeyrequest.md) — An object that encapsulates information about a persistable content decryption key request issued from a content key session.
- [AVExternalContentProtectionStatus](avexternalcontentprotectionstatus.md) — Constants that specify whether sufficient protection exists to display the content.
- [AVSampleBufferAttachContentKey](<avsamplebufferattachcontentkey(______).md>) — Attaches a content key to a sample buffer for the purpose of content decryption. _(deprecated)_
