---
title: AVContentKey
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, macOS 11.3+, tvOS 14.5+, visionOS 1.0+, watchOS 7.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkey
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkey.json'
content_hash: 'sha256:0df66d40d40b9efd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVContentKey

<sub>Class</sub>

An object that represents the content key decryptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVContentKey
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the specifier

- [contentKeySpecifier](avcontentkey/contentkeyspecifier.md) — The content key’s unique identifier.

### Inspecting protection status

- [externalContentProtectionStatus](avcontentkey/externalcontentprotectionstatus.md) — The external protection status for the content key based on all attached displays.
- [- revoke](<avcontentkey/revoke().md>)

## See Also

### FairPlay streaming

- [AVContentKeySession](avcontentkeysession.md) — An object that creates and tracks decryption keys for media data.
- [AVContentKeySessionDelegate](avcontentkeysessiondelegate.md) — A protocol that handles content key requests.
- [AVContentKeySpecifier](avcontentkeyspecifier.md) — An object that uniquely identifies a content key.
- [AVContentKeyRequest](avcontentkeyrequest.md) — An object that encapsulates information about a content decryption key request issued from a content key session object.
- [AVPersistableContentKeyRequest](avpersistablecontentkeyrequest.md) — An object that encapsulates information about a persistable content decryption key request issued from a content key session.
- [AVContentKeyResponse](avcontentkeyresponse.md) — An object that encapsulates information about a response to a content decryption key request.
- [AVExternalContentProtectionStatus](avexternalcontentprotectionstatus.md) — Constants that specify whether sufficient protection exists to display the content.
- [AVSampleBufferAttachContentKey](<avsamplebufferattachcontentkey(______).md>) — Attaches a content key to a sample buffer for the purpose of content decryption. _(deprecated)_
