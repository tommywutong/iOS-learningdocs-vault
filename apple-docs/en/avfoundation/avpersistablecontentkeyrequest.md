---
title: AVPersistableContentKeyRequest
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpersistablecontentkeyrequest
source_url: 'https://developer.apple.com/documentation/avfoundation/avpersistablecontentkeyrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpersistablecontentkeyrequest.json'
content_hash: 'sha256:f19c2959ad5a3c5c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPersistableContentKeyRequest

<sub>Class</sub>

An object that encapsulates information about a persistable content decryption key request issued from a content key session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVPersistableContentKeyRequest
```

## Overview

This class allows clients to create and use persistable content keys.

## Relationships

- **Inherits From**: [AVContentKeyRequest](avcontentkeyrequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Requesting persistable content key data

- [- persistableContentKeyFromKeyVendorResponse:options:error:](<avpersistablecontentkeyrequest/persistablecontentkey(fromkeyvendorresponse_options_).md>) — Creates a persistable content key from the content key context data.

## See Also

### FairPlay streaming

- [AVContentKeySession](avcontentkeysession.md) — An object that creates and tracks decryption keys for media data.
- [AVContentKeySessionDelegate](avcontentkeysessiondelegate.md) — A protocol that handles content key requests.
- [AVContentKey](avcontentkey.md) — An object that represents the content key decryptor.
- [AVContentKeySpecifier](avcontentkeyspecifier.md) — An object that uniquely identifies a content key.
- [AVContentKeyRequest](avcontentkeyrequest.md) — An object that encapsulates information about a content decryption key request issued from a content key session object.
- [AVContentKeyResponse](avcontentkeyresponse.md) — An object that encapsulates information about a response to a content decryption key request.
- [AVExternalContentProtectionStatus](avexternalcontentprotectionstatus.md) — Constants that specify whether sufficient protection exists to display the content.
- [AVSampleBufferAttachContentKey](<avsamplebufferattachcontentkey(______).md>) — Attaches a content key to a sample buffer for the purpose of content decryption. _(deprecated)_
